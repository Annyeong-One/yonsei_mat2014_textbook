# Thread-Local Storage

`threading.local()` provides storage where each thread has its own independent copy of data.

## The Problem: Shared State

Without thread-local storage, all threads share the same global variables:

```python
import threading
import time

# Global variable - shared by all threads
request_id = None

def handle_request(req_id):
    global request_id
    request_id = req_id
    time.sleep(0.1)  # Simulate processing
    # BUG: request_id may have been overwritten by another thread!
    print(f"Processing request {request_id}")

threads = []
for i in range(5):
    t = threading.Thread(target=handle_request, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Output might show wrong request IDs!
```

## Solution: threading.local()

Each thread gets its own copy of the data:

```python
import threading
import time

# Thread-local storage
local_data = threading.local()

def handle_request(req_id):
    local_data.request_id = req_id
    time.sleep(0.1)
    # Each thread sees its own request_id
    print(f"Thread {threading.current_thread().name}: request {local_data.request_id}")

threads = []
for i in range(5):
    t = threading.Thread(target=handle_request, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Output: Each thread shows its correct request_id
```

## How It Works

```python
import threading

local = threading.local()

def show_value():
    thread_name = threading.current_thread().name
    if hasattr(local, 'value'):
        print(f"{thread_name}: value = {local.value}")
    else:
        print(f"{thread_name}: no value set")

def set_value(val):
    local.value = val
    show_value()

# Main thread
local.value = "main"
show_value()  # main: value = main

# Other threads don't see main's value
t1 = threading.Thread(target=show_value, name="Thread-1")
t1.start()
t1.join()  # Thread-1: no value set

# Each thread sets its own value
t2 = threading.Thread(target=set_value, args=("thread2",), name="Thread-2")
t2.start()
t2.join()  # Thread-2: value = thread2

# Main thread's value unchanged
show_value()  # main: value = main
```

## Practical Examples

### 1. Request Context in Web Server

```python
import threading
from contextlib import contextmanager

# Thread-local request context
_request_context = threading.local()

@contextmanager
def request_context(request_id, user_id):
    """Set request context for current thread."""
    _request_context.request_id = request_id
    _request_context.user_id = user_id
    try:
        yield
    finally:
        del _request_context.request_id
        del _request_context.user_id

def get_current_user():
    """Get user from current request context."""
    return getattr(_request_context, 'user_id', None)

def get_request_id():
    """Get current request ID."""
    return getattr(_request_context, 'request_id', None)

def process_data():
    user = get_current_user()
    req = get_request_id()
    print(f"Processing for user {user} (request {req})")

def handle_request(request_id, user_id):
    with request_context(request_id, user_id):
        process_data()

# Simulate concurrent requests
threads = []
for i in range(3):
    t = threading.Thread(target=handle_request, args=(f"req-{i}", f"user-{i}"))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### 2. Database Connection Per Thread

```python
import threading
import sqlite3

class ThreadLocalDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self._local = threading.local()
    
    @property
    def connection(self):
        """Get connection for current thread, create if needed."""
        if not hasattr(self._local, 'conn'):
            self._local.conn = sqlite3.connect(self.db_path)
        return self._local.conn
    
    def execute(self, query, params=()):
        """Execute query on thread's connection."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    def close(self):
        """Close current thread's connection."""
        if hasattr(self._local, 'conn'):
            self._local.conn.close()
            del self._local.conn

# Usage
db = ThreadLocalDB('mydb.sqlite')

def worker(worker_id):
    # Each thread gets its own connection
    db.execute("INSERT INTO logs VALUES (?)", (f"worker-{worker_id}",))
    db.connection.commit()

threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

### 3. Logging Context

```python
import threading
import logging

class ContextFilter(logging.Filter):
    """Add thread-local context to log records."""
    
    def __init__(self):
        super().__init__()
        self._local = threading.local()
    
    def set_context(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self._local, key, value)
    
    def clear_context(self):
        self._local.__dict__.clear()
    
    def filter(self, record):
        for key, value in self._local.__dict__.items():
            setattr(record, key, value)
        return True

# Setup
context_filter = ContextFilter()
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '%(asctime)s [%(request_id)s] %(message)s'
))
handler.addFilter(context_filter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def process_request(request_id):
    context_filter.set_context(request_id=request_id)
    try:
        logger.info("Starting request")
        # ... do work ...
        logger.info("Request completed")
    finally:
        context_filter.clear_context()
```

### 4. Transaction Scope

```python
import threading
from contextlib import contextmanager

class TransactionManager:
    def __init__(self):
        self._local = threading.local()
    
    @property
    def current_transaction(self):
        return getattr(self._local, 'transaction', None)
    
    @contextmanager
    def transaction(self):
        if self.current_transaction is not None:
            raise RuntimeError("Nested transactions not supported")
        
        self._local.transaction = Transaction()
        try:
            yield self._local.transaction
            self._local.transaction.commit()
        except Exception:
            self._local.transaction.rollback()
            raise
        finally:
            del self._local.transaction

class Transaction:
    def __init__(self):
        self.operations = []
    
    def add(self, op):
        self.operations.append(op)
    
    def commit(self):
        print(f"Committing {len(self.operations)} operations")
    
    def rollback(self):
        print("Rolling back")

# Usage
tm = TransactionManager()

def worker(worker_id):
    with tm.transaction() as txn:
        txn.add(f"operation from worker {worker_id}")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

## Subclassing threading.local

For initialization logic, subclass `threading.local`:

```python
import threading

class MyLocal(threading.local):
    def __init__(self, default_value):
        # Called once per thread when first accessed
        self.value = default_value
        self.initialized = True

local = MyLocal("default")

def show():
    print(f"{threading.current_thread().name}: {local.value}")

# Main thread
show()  # MainThread: default
local.value = "main"
show()  # MainThread: main

# New thread gets fresh default
t = threading.Thread(target=show)
t.start()
t.join()  # Thread-1: default
```

## Important Considerations

### Data is Thread-Specific, Not Task-Specific

Thread-local data persists for the lifetime of the thread:

```python
import threading
from concurrent.futures import ThreadPoolExecutor

local = threading.local()

def task(task_id):
    # May see leftover data from previous task on same thread!
    old = getattr(local, 'task_id', 'none')
    local.task_id = task_id
    return f"Task {task_id} (previous: {old})"

with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(task, range(10)))
    print(results)
# Tasks reuse threads, so they may see previous task's data
```

### Cleanup Pattern

```python
def task_with_cleanup(task_id):
    local.task_id = task_id
    try:
        # ... do work ...
        pass
    finally:
        del local.task_id  # Clean up
```

## threading.local vs contextvars

| Feature | threading.local | contextvars |
|---------|-----------------|-------------|
| Thread isolation | ✅ | ✅ |
| Async task isolation | ❌ | ✅ |
| Copy on task creation | ❌ | ✅ |
| Python version | 2.4+ | 3.7+ |

For async code, use `contextvars` instead.

## Key Takeaways

- `threading.local()` provides thread-isolated storage
- Each thread sees its own copy of attributes
- Useful for request context, connections, transactions
- Data persists for thread lifetime (clean up in thread pools)
- For async code, use `contextvars` instead
- Subclass for custom initialization logic
