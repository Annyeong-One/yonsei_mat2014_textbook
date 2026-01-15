# Thread Synchronization

When multiple threads access shared data, synchronization is essential to prevent race conditions and ensure data integrity.

---

## The Problem: Race Conditions

### Without Synchronization

```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(100_000):
        counter += 1  # Not atomic!

# Create two threads
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Expected: 200000")
print(f"Actual: {counter}")  # Often less than 200000!
```

### Why It Happens

`counter += 1` is not atomic — it's actually three operations:

```python
# What looks like one operation:
counter += 1

# Is actually:
temp = counter      # 1. Read current value
temp = temp + 1     # 2. Increment
counter = temp      # 3. Write back

# Thread 1: Read counter (0)
# Thread 2: Read counter (0)  ← Same value!
# Thread 1: Write counter (1)
# Thread 2: Write counter (1)  ← Overwrites Thread 1's work!
```

---

## Lock (Mutex)

A `Lock` ensures only one thread can execute a section of code at a time.

### Basic Lock Usage

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100_000):
        lock.acquire()       # Get the lock
        try:
            counter += 1
        finally:
            lock.release()   # Always release!

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Counter: {counter}")  # Always 200000
```

### Lock as Context Manager (Recommended)

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100_000):
        with lock:           # Automatically acquires and releases
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Counter: {counter}")  # Always 200000
```

### Non-Blocking Lock Acquisition

```python
import threading
import time

lock = threading.Lock()

def try_acquire():
    if lock.acquire(blocking=False):
        try:
            print(f"{threading.current_thread().name}: Got lock")
            time.sleep(1)
        finally:
            lock.release()
    else:
        print(f"{threading.current_thread().name}: Lock busy, skipping")

# With timeout
def try_acquire_timeout():
    if lock.acquire(timeout=0.5):
        try:
            print(f"{threading.current_thread().name}: Got lock")
            time.sleep(1)
        finally:
            lock.release()
    else:
        print(f"{threading.current_thread().name}: Timeout")
```

---

## RLock (Reentrant Lock)

A regular `Lock` cannot be acquired twice by the same thread. `RLock` allows the same thread to acquire it multiple times.

### The Problem with Regular Lock

```python
import threading

lock = threading.Lock()

def outer():
    with lock:
        print("Outer acquired lock")
        inner()  # Deadlock! Lock already held

def inner():
    with lock:  # Blocks forever waiting for lock
        print("Inner acquired lock")

# This will deadlock with regular Lock
```

### RLock Solution

```python
import threading

rlock = threading.RLock()

def outer():
    with rlock:
        print("Outer acquired lock")
        inner()

def inner():
    with rlock:  # Same thread can acquire again
        print("Inner acquired lock")

outer()  # Works!
# Output:
# Outer acquired lock
# Inner acquired lock
```

### When to Use RLock

```python
import threading

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.RLock()  # Use RLock for recursive access
    
    def deposit(self, amount):
        with self.lock:
            self.balance += amount
    
    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False
    
    def transfer(self, other, amount):
        with self.lock:  # First acquisition
            if self.withdraw(amount):  # Second acquisition (same lock)
                other.deposit(amount)
                return True
            return False
```

---

## Semaphore

A `Semaphore` allows a limited number of threads to access a resource simultaneously.

### Basic Semaphore

```python
import threading
import time

# Allow max 3 concurrent accesses
semaphore = threading.Semaphore(3)

def worker(worker_id):
    print(f"Worker {worker_id}: Waiting for semaphore")
    with semaphore:
        print(f"Worker {worker_id}: Acquired semaphore")
        time.sleep(2)  # Simulate work
        print(f"Worker {worker_id}: Releasing semaphore")

# Start 10 workers, but only 3 run at a time
threads = [threading.Thread(target=worker, args=(i,)) for i in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

### Practical Example: Connection Pool

```python
import threading
import time
import random

class ConnectionPool:
    def __init__(self, max_connections):
        self.semaphore = threading.Semaphore(max_connections)
        self.connections = [f"conn_{i}" for i in range(max_connections)]
        self.lock = threading.Lock()
    
    def get_connection(self):
        self.semaphore.acquire()
        with self.lock:
            conn = self.connections.pop()
        return conn
    
    def release_connection(self, conn):
        with self.lock:
            self.connections.append(conn)
        self.semaphore.release()

pool = ConnectionPool(3)

def database_query(query_id):
    conn = pool.get_connection()
    try:
        print(f"Query {query_id}: Using {conn}")
        time.sleep(random.uniform(0.5, 1.5))
    finally:
        pool.release_connection(conn)
        print(f"Query {query_id}: Released {conn}")

threads = [threading.Thread(target=database_query, args=(i,)) for i in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

### BoundedSemaphore

Raises error if released more times than acquired:

```python
import threading

# Regular semaphore: no error on extra release
sem = threading.Semaphore(2)
sem.release()
sem.release()
sem.release()  # No error, but counter is now 5!

# BoundedSemaphore: catches bugs
bsem = threading.BoundedSemaphore(2)
bsem.release()  # ValueError: Semaphore released too many times
```

---

## Event

An `Event` is a simple flag that threads can wait on.

### Basic Event Usage

```python
import threading
import time

event = threading.Event()

def waiter(name):
    print(f"{name}: Waiting for event...")
    event.wait()  # Block until event is set
    print(f"{name}: Event received!")

def setter():
    print("Setter: Preparing...")
    time.sleep(2)
    print("Setter: Setting event")
    event.set()

# Start waiters
for i in range(3):
    threading.Thread(target=waiter, args=(f"Waiter-{i}",)).start()

# Start setter
threading.Thread(target=setter).start()
```

### Event Methods

```python
import threading

event = threading.Event()

# Check if set
print(event.is_set())  # False

# Wait with timeout
result = event.wait(timeout=1.0)  # Returns True if set, False on timeout

# Set the event (wake all waiting threads)
event.set()
print(event.is_set())  # True

# Clear the event
event.clear()
print(event.is_set())  # False
```

### Practical Example: Startup Coordination

```python
import threading
import time

db_ready = threading.Event()
cache_ready = threading.Event()

def init_database():
    print("Database: Initializing...")
    time.sleep(2)
    print("Database: Ready")
    db_ready.set()

def init_cache():
    print("Cache: Waiting for database...")
    db_ready.wait()  # Cache depends on database
    print("Cache: Initializing...")
    time.sleep(1)
    print("Cache: Ready")
    cache_ready.set()

def main_app():
    print("App: Waiting for all services...")
    db_ready.wait()
    cache_ready.wait()
    print("App: All services ready, starting...")

threading.Thread(target=init_database).start()
threading.Thread(target=init_cache).start()
threading.Thread(target=main_app).start()
```

---

## Condition

A `Condition` combines a lock with the ability to wait for a condition to be true.

### Basic Condition Usage

```python
import threading
import time

condition = threading.Condition()
items = []

def producer():
    for i in range(5):
        time.sleep(0.5)
        with condition:
            items.append(f"item-{i}")
            print(f"Produced: item-{i}")
            condition.notify()  # Wake up one waiting consumer

def consumer():
    while True:
        with condition:
            while not items:  # Wait until items available
                print("Consumer: Waiting...")
                condition.wait()
            item = items.pop(0)
            print(f"Consumed: {item}")
        
        if item == "item-4":
            break

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()
```

### Producer-Consumer Pattern

```python
import threading
import time
import random

class BoundedBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.condition = threading.Condition()
    
    def put(self, item):
        with self.condition:
            while len(self.buffer) >= self.capacity:
                print(f"Buffer full, producer waiting...")
                self.condition.wait()
            
            self.buffer.append(item)
            print(f"Produced: {item}, buffer size: {len(self.buffer)}")
            self.condition.notify_all()
    
    def get(self):
        with self.condition:
            while len(self.buffer) == 0:
                print(f"Buffer empty, consumer waiting...")
                self.condition.wait()
            
            item = self.buffer.pop(0)
            print(f"Consumed: {item}, buffer size: {len(self.buffer)}")
            self.condition.notify_all()
            return item

buffer = BoundedBuffer(capacity=3)

def producer(producer_id):
    for i in range(5):
        time.sleep(random.uniform(0.1, 0.5))
        buffer.put(f"P{producer_id}-{i}")

def consumer(consumer_id):
    for _ in range(5):
        time.sleep(random.uniform(0.1, 0.5))
        buffer.get()

# 2 producers, 2 consumers
threads = []
for i in range(2):
    threads.append(threading.Thread(target=producer, args=(i,)))
    threads.append(threading.Thread(target=consumer, args=(i,)))

for t in threads:
    t.start()
for t in threads:
    t.join()
```

---

## Barrier

A `Barrier` synchronizes a fixed number of threads at a certain point.

```python
import threading
import time
import random

barrier = threading.Barrier(3)

def worker(worker_id):
    # Phase 1: Each thread does independent work
    work_time = random.uniform(0.5, 2.0)
    print(f"Worker {worker_id}: Working for {work_time:.1f}s")
    time.sleep(work_time)
    
    # Synchronization point
    print(f"Worker {worker_id}: Reached barrier, waiting...")
    barrier.wait()  # All threads must reach here before any continue
    
    # Phase 2: Continue after all threads synchronized
    print(f"Worker {worker_id}: Continuing after barrier")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

---

## Summary: Synchronization Primitives

| Primitive | Purpose | Use Case |
|-----------|---------|----------|
| **Lock** | Mutual exclusion | Protect shared data |
| **RLock** | Reentrant mutual exclusion | Recursive functions with locks |
| **Semaphore** | Limit concurrent access | Connection pools, rate limiting |
| **Event** | Simple signaling | Start/stop signals, coordination |
| **Condition** | Wait for complex conditions | Producer-consumer, state changes |
| **Barrier** | Synchronize multiple threads | Phased computation |

---

## Key Takeaways

- **Always** use synchronization when multiple threads access shared mutable data
- Use `with lock:` syntax for automatic acquisition and release
- `Lock` for simple mutual exclusion, `RLock` for recursive access
- `Semaphore` to limit concurrent resource access
- `Event` for simple signaling between threads
- `Condition` for complex waiting conditions (producer-consumer)
- `Barrier` to synchronize threads at specific points
- Avoid holding locks longer than necessary to prevent contention
