# Context Managers

Context managers encapsulate setup and cleanup logic, ensuring resources are properly managed even when exceptions occur.

---

## Context Manager Protocol

### 1. Two Required Methods

```python
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        return False

with MyContext() as ctx:
    print("Inside context")
```

### 2. `__enter__` Return Value

```python
def __enter__(self):
    # Setup code
    return value  # Bound to 'as' variable
```

### 3. `__exit__` Parameters

```python
def __exit__(self, exc_type, exc_value, traceback):
    # exc_type: Exception class or None
    # exc_value: Exception instance or None
    # traceback: Traceback object or None
    return False  # Propagate exception
```

---

## File Handling

### 1. Custom File Wrapper

```python
class FileWrapper:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileWrapper("data.txt", "w") as f:
    f.write("Hello, world!")
# File automatically closed
```

### 2. Built-in `open()`

```python
with open("data.txt", "r") as f:
    data = f.read()
# Equivalent to FileWrapper
```

### 3. Guaranteed Cleanup

```python
# Without context manager - risky
f = open("data.txt")
data = f.read()  # Exception here?
f.close()  # Might not run!

# With context manager - safe
with open("data.txt") as f:
    data = f.read()
# Always closed
```

---

## Return Self vs Resource

### 1. Return `self`

```python
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self  # Access timer object
    
    def __exit__(self, *args):
        self.elapsed = time.time() - self.start

with Timer() as t:
    # Do work
    pass
print(t.elapsed)  # Access timer state
```

### 2. Return Resource

```python
class Transaction:
    def __init__(self, conn):
        self.conn = conn
    
    def __enter__(self):
        self.conn.begin()
        return self.conn  # Return connection
    
    def __exit__(self, exc_type, *_):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()

with Transaction(db) as conn:
    conn.execute("INSERT ...")  # Use connection directly
```

### 3. Return None

```python
class CriticalSection:
    def __init__(self, lock):
        self.lock = lock
    
    def __enter__(self):
        self.lock.acquire()
        # No return - don't need anything
    
    def __exit__(self, *args):
        self.lock.release()

with CriticalSection(lock):
    # Just need bracketing
    pass
```

---

## Timing Code Blocks

### 1. Basic Timer

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"⏱ Elapsed: {self.elapsed:.4f}s")

with Timer():
    result = sum(i**2 for i in range(10**6))
```

### 2. With Logging

```python
class Timer:
    def __init__(self, name=""):
        self.name = name
    
    def __enter__(self):
        self.start = time.perf_counter()
        print(f"⏱ Starting {self.name}...")
        return self
    
    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start
        print(f"⏱ {self.name} took {self.elapsed:.4f}s")

with Timer("computation"):
    # Expensive operation
    pass
```

### 3. Nested Timers

```python
with Timer("outer"):
    with Timer("inner1"):
        pass
    with Timer("inner2"):
        pass
```

---

## Database Transactions

### 1. Atomic Operations

```python
class Transaction:
    def __init__(self, connection):
        self.conn = connection
    
    def __enter__(self):
        self.conn.begin()
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
            print("Transaction rolled back")
        else:
            self.conn.commit()
            print("Transaction committed")
        return False

with Transaction(db_connection) as conn:
    conn.execute("INSERT ...")
    conn.execute("UPDATE ...")
    # Auto-commit if no exception
```

### 2. Savepoints

```python
class Savepoint:
    def __init__(self, conn, name):
        self.conn = conn
        self.name = name
    
    def __enter__(self):
        self.conn.execute(f"SAVEPOINT {self.name}")
        return self
    
    def __exit__(self, exc_type, *_):
        if exc_type:
            self.conn.execute(f"ROLLBACK TO {self.name}")
        else:
            self.conn.execute(f"RELEASE {self.name}")
```

### 3. Connection Pooling

```python
class PooledConnection:
    def __init__(self, pool):
        self.pool = pool
        self.conn = None
    
    def __enter__(self):
        self.conn = self.pool.get_connection()
        return self.conn
    
    def __exit__(self, *args):
        self.pool.return_connection(self.conn)
```

---

## Thread Locks

### 1. Lock Manager

```python
from threading import Lock

class CriticalSection:
    def __init__(self, lock):
        self.lock = lock
    
    def __enter__(self):
        self.lock.acquire()
    
    def __exit__(self, *args):
        self.lock.release()

lock = Lock()
with CriticalSection(lock):
    # Thread-safe code
    shared_resource.update()
```

### 2. Python's Built-in

```python
from threading import Lock

lock = Lock()
with lock:  # Lock itself is a context manager
    # Critical section
    pass
```

### 3. RLock (Reentrant)

```python
from threading import RLock

lock = RLock()
with lock:
    with lock:  # Can acquire multiple times
        pass
```

---

## Exception Handling

### 1. Suppress Exceptions

```python
class SafeDivision:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ZeroDivisionError:
            print("⚠️ Division by zero")
            return True  # Suppress exception
        return False

with SafeDivision():
    print(1 / 0)  # No exception raised
print("Continuing...")
```

### 2. Propagate Exceptions

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    self.cleanup()
    return False  # Don't suppress
```

### 3. Log and Propagate

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type:
        logging.error(f"Exception: {exc_val}")
    self.cleanup()
    return False  # Propagate
```

---

## PyTorch Context Managers

### 1. `torch.no_grad()`

```python
import torch

model = SomeModel()
with torch.no_grad():
    output = model(input)
    # No gradients computed - saves memory
```

### 2. How It Works

```python
class no_grad:
    def __enter__(self):
        self.prev = torch.is_grad_enabled()
        torch.set_grad_enabled(False)
    
    def __exit__(self, *args):
        torch.set_grad_enabled(self.prev)
```

### 3. `torch.inference_mode()`

```python
with torch.inference_mode():
    output = model(input)
    # Even faster than no_grad
```

---

## Mixed Precision

### 1. `autocast()`

```python
from torch.cuda.amp import autocast

with autocast():
    output = model(input)
    # Automatic mixed precision
```

### 2. Why Context Manager

```python
# Only during forward/backward
with autocast():
    output = model(input)
    loss = criterion(output, target)

# Not during optimizer step
optimizer.step()
```

### 3. Localized Effects

Context managers isolate effects to specific blocks.

---

## `contextlib` Module

### 1. `@contextmanager` Decorator

```python
from contextlib import contextmanager

@contextmanager
def temporary_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()

with temporary_file("tmp.txt") as f:
    f.write("data")
```

### 2. Generator-Based

```python
@contextmanager
def timer(name):
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f"{name}: {elapsed:.4f}s")

with timer("operation"):
    # Code to time
    pass
```

### 3. Exception Handling

```python
@contextmanager
def managed_resource():
    resource = acquire()
    try:
        yield resource
    except Exception as e:
        handle_error(e)
        raise
    finally:
        release(resource)
```

---

## State Management

### 1. Temporary Changes

```python
class TemporaryValue:
    def __init__(self, obj, attr, temp_value):
        self.obj = obj
        self.attr = attr
        self.temp_value = temp_value
    
    def __enter__(self):
        self.original = getattr(self.obj, self.attr)
        setattr(self.obj, self.attr, self.temp_value)
    
    def __exit__(self, *args):
        setattr(self.obj, self.attr, self.original)

with TemporaryValue(config, 'debug', True):
    # config.debug is True
    pass
# config.debug restored
```

### 2. Seed Management

```python
import random

@contextmanager
def temporary_seed(seed):
    state = random.getstate()
    random.seed(seed)
    try:
        yield
    finally:
        random.setstate(state)

with temporary_seed(42):
    # Reproducible randomness
    pass
```

### 3. Directory Changes

```python
import os

@contextmanager
def working_directory(path):
    old_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_dir)
```

---

## Best Practices

### 1. Always Cleanup

```python
def __exit__(self, *args):
    # Cleanup must happen
    self.resource.close()
    return False
```

### 2. Document Return Value

```python
class MyContext:
    """
    Context manager for X.
    
    Returns:
        The managed resource (when using 'as')
    """
    def __enter__(self):
        return self.resource
```

### 3. Don't Suppress by Default

```python
def __exit__(self, exc_type, *_):
    self.cleanup()
    return False  # Propagate exceptions
```

---

## Key Takeaways

- `__enter__` for setup, `__exit__` for cleanup.
- `__exit__` runs even with exceptions.
- Return `True` to suppress exceptions.
- Common uses: files, locks, transactions, timing.
- PyTorch uses for grad control, precision.
- `@contextmanager` for simple cases.
