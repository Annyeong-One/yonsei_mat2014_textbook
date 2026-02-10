# Deadlocks

A **deadlock** occurs when two or more threads are blocked forever, each waiting for resources held by the other.

## Classic Deadlock Example

### Two Threads, Two Locks

```python
import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_1():
    print("Thread 1: Acquiring lock_a...")
    with lock_a:
        print("Thread 1: Got lock_a")
        time.sleep(0.1)  # Simulate work
        
        print("Thread 1: Acquiring lock_b...")
        with lock_b:  # DEADLOCK: Thread 2 holds lock_b
            print("Thread 1: Got lock_b")

def thread_2():
    print("Thread 2: Acquiring lock_b...")
    with lock_b:
        print("Thread 2: Got lock_b")
        time.sleep(0.1)  # Simulate work
        
        print("Thread 2: Acquiring lock_a...")
        with lock_a:  # DEADLOCK: Thread 1 holds lock_a
            print("Thread 2: Got lock_a")

t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

t1.start()
t2.start()

# Program hangs here - both threads waiting forever
t1.join()
t2.join()
```

### What Happens

```
Time    Thread 1              Thread 2
────────────────────────────────────────────
0       Acquire lock_a ✓     Acquire lock_b ✓
1       Wait for lock_b      Wait for lock_a
2       (blocked)            (blocked)
...     DEADLOCK!            DEADLOCK!
```

## Deadlock Conditions (Coffman Conditions)

All four must be present for deadlock:

1. **Mutual Exclusion**: Resources cannot be shared
2. **Hold and Wait**: Thread holds one resource while waiting for another
3. **No Preemption**: Resources cannot be forcibly taken
4. **Circular Wait**: Circular chain of waiting threads

## Solutions to Prevent Deadlock

### 1. Lock Ordering (Most Common)

Always acquire locks in the same order:

```python
import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def safe_thread_1():
    # Always acquire in order: lock_a, then lock_b
    with lock_a:
        with lock_b:
            print("Thread 1: Got both locks")

def safe_thread_2():
    # Same order: lock_a, then lock_b
    with lock_a:
        with lock_b:
            print("Thread 2: Got both locks")

# No deadlock - consistent ordering
t1 = threading.Thread(target=safe_thread_1)
t2 = threading.Thread(target=safe_thread_2)
t1.start()
t2.start()
t1.join()
t2.join()
```

### 2. Lock Ordering with IDs

For dynamic lock sets, use object IDs:

```python
import threading

def acquire_locks(*locks):
    """Acquire multiple locks in consistent order."""
    # Sort by id to ensure consistent ordering
    sorted_locks = sorted(locks, key=id)
    
    for lock in sorted_locks:
        lock.acquire()
    
    try:
        yield
    finally:
        for lock in reversed(sorted_locks):
            lock.release()

# Usage
lock_a = threading.Lock()
lock_b = threading.Lock()

def safe_operation(lock1, lock2):
    with acquire_locks(lock1, lock2):
        print("Got both locks safely")

# Both orderings are safe
t1 = threading.Thread(target=safe_operation, args=(lock_a, lock_b))
t2 = threading.Thread(target=safe_operation, args=(lock_b, lock_a))  # Different order OK
t1.start()
t2.start()
```

### 3. Try-Lock with Timeout

Attempt to acquire lock with timeout:

```python
import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_with_timeout():
    while True:
        lock_a.acquire()
        try:
            # Try to get lock_b with timeout
            if lock_b.acquire(timeout=0.1):
                try:
                    print("Got both locks!")
                    return
                finally:
                    lock_b.release()
            else:
                print("Couldn't get lock_b, retrying...")
        finally:
            lock_a.release()
        
        # Back off before retry
        time.sleep(0.01)
```

### 4. Try-Lock All-or-Nothing

Acquire all locks or none:

```python
import threading
import random
import time

def try_acquire_all(*locks, timeout=1.0):
    """Try to acquire all locks, release all if any fails."""
    acquired = []
    deadline = time.time() + timeout
    
    for lock in locks:
        remaining = deadline - time.time()
        if remaining <= 0:
            # Timeout - release all acquired
            for l in acquired:
                l.release()
            return False
        
        if lock.acquire(timeout=remaining):
            acquired.append(lock)
        else:
            # Failed - release all acquired
            for l in acquired:
                l.release()
            return False
    
    return True

def release_all(*locks):
    for lock in locks:
        lock.release()

# Usage
lock_a = threading.Lock()
lock_b = threading.Lock()

def safe_worker():
    if try_acquire_all(lock_a, lock_b, timeout=1.0):
        try:
            print("Got all locks")
        finally:
            release_all(lock_a, lock_b)
    else:
        print("Failed to acquire locks")
```

### 5. Using RLock for Recursive Calls

Regular Lock causes self-deadlock with recursion:

```python
import threading

# WRONG: Self-deadlock with regular Lock
lock = threading.Lock()

def recursive_bad(n):
    with lock:
        if n > 0:
            recursive_bad(n - 1)  # DEADLOCK!

# CORRECT: Use RLock for recursive locking
rlock = threading.RLock()

def recursive_good(n):
    with rlock:
        if n > 0:
            recursive_good(n - 1)  # OK - same thread can reacquire

recursive_good(5)  # Works fine
```

## Common Deadlock Scenarios

### 1. Lock-in-Lock

```python
# BAD: Nested locks acquired in inconsistent order
def transfer_bad(from_account, to_account, amount):
    with from_account.lock:
        with to_account.lock:
            from_account.balance -= amount
            to_account.balance += amount

# If two threads call:
# Thread 1: transfer(A, B, 100)  - acquires A, waits for B
# Thread 2: transfer(B, A, 50)   - acquires B, waits for A
# DEADLOCK!

# GOOD: Consistent lock ordering
def transfer_good(from_account, to_account, amount):
    # Sort by account ID for consistent ordering
    first, second = sorted([from_account, to_account], key=lambda a: a.id)
    
    with first.lock:
        with second.lock:
            from_account.balance -= amount
            to_account.balance += amount
```

### 2. Lock-Then-Wait

```python
import threading
import queue

# BAD: Holding lock while waiting
lock = threading.Lock()
q = queue.Queue()

def producer_bad():
    with lock:
        # If queue is full, blocks while holding lock
        q.put("item")  # Other threads can't proceed!

# GOOD: Don't hold lock while blocking
def producer_good():
    item = prepare_item()
    q.put(item)  # Queue handles its own synchronization
    
    with lock:
        update_stats()  # Only lock when needed
```

### 3. Callback Deadlock

```python
import threading

lock = threading.Lock()
callbacks = []

def register_callback(cb):
    with lock:
        callbacks.append(cb)

def trigger_callbacks():
    with lock:
        for cb in callbacks:
            cb()  # DANGER: callback might call register_callback!

# BETTER: Copy list, release lock before calling
def trigger_callbacks_safe():
    with lock:
        cbs = list(callbacks)
    
    for cb in cbs:  # Lock released
        cb()
```

## Detecting Deadlocks

### 1. Timeout-Based Detection

```python
import threading

def acquire_with_deadlock_detection(lock, timeout=5.0, name="lock"):
    acquired = lock.acquire(timeout=timeout)
    if not acquired:
        # Potential deadlock
        print(f"WARNING: Possible deadlock waiting for {name}")
        print(f"Current thread: {threading.current_thread().name}")
        # Could log stack traces, alert monitoring, etc.
        raise TimeoutError(f"Timeout acquiring {name}")
    return acquired
```

### 2. Using faulthandler

```python
import faulthandler
import threading
import time

# Enable traceback dump on hang
faulthandler.enable()

# Also dump on SIGUSR1 (Unix)
import signal
faulthandler.register(signal.SIGUSR1)

# If program hangs, send SIGUSR1 to see thread stacks
# kill -USR1 <pid>
```

### 3. Thread Dump

```python
import sys
import threading
import traceback

def dump_threads():
    """Print stack traces of all threads."""
    print("\n*** THREAD DUMP ***")
    for thread_id, frame in sys._current_frames().items():
        thread = threading._active.get(thread_id)
        name = thread.name if thread else f"Thread-{thread_id}"
        print(f"\n{name}:")
        traceback.print_stack(frame)
```

## Key Takeaways

- Deadlock requires: mutual exclusion, hold-and-wait, no preemption, circular wait
- **Prevention**: Lock ordering, try-lock with timeout, acquire all-or-nothing
- Use `RLock` for recursive locking scenarios
- Don't hold locks while blocking on other operations
- Copy data before calling callbacks with locks held
- Use timeouts to detect potential deadlocks
- Test concurrent code thoroughly with different thread interleavings
