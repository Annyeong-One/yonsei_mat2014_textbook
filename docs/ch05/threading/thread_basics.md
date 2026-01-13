# Thread Basics

The `threading` module provides a way to run multiple threads (lightweight processes) within a single Python process.

---

## Creating Threads

### Method 1: Using Thread with target Function

```python
import threading
import time

def worker(name, delay):
    """Function to run in a thread."""
    print(f"{name}: Starting")
    time.sleep(delay)
    print(f"{name}: Finished")

# Create thread
thread = threading.Thread(target=worker, args=("Thread-1", 2))

# Start thread
thread.start()

print("Main: Thread started")

# Wait for thread to complete
thread.join()

print("Main: Thread finished")
```

Output:
```
Thread-1: Starting
Main: Thread started
Thread-1: Finished
Main: Thread finished
```

### Method 2: Subclassing Thread

```python
import threading
import time

class WorkerThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
        self.result = None
    
    def run(self):
        """Override run() method."""
        print(f"{self.name}: Starting")
        time.sleep(self.delay)
        self.result = f"{self.name} completed"
        print(f"{self.name}: Finished")

# Create and start
thread = WorkerThread("Worker-1", 2)
thread.start()
thread.join()

print(f"Result: {thread.result}")
```

---

## Thread Lifecycle

```
                    ┌─────────┐
                    │ Created │
                    └────┬────┘
                         │ start()
                         ▼
                    ┌─────────┐
        ┌──────────│ Running │──────────┐
        │          └────┬────┘          │
        │               │               │
    wait/sleep      complete        exception
        │               │               │
        ▼               ▼               ▼
   ┌─────────┐    ┌──────────┐    ┌─────────┐
   │ Blocked │    │ Finished │    │ Finished│
   └────┬────┘    └──────────┘    └─────────┘
        │
    resume
        │
        └──────────► Running
```

### Thread States

```python
import threading
import time

def worker():
    time.sleep(1)

thread = threading.Thread(target=worker)

print(f"Created - is_alive: {thread.is_alive()}")  # False

thread.start()
print(f"Started - is_alive: {thread.is_alive()}")  # True

thread.join()
print(f"Joined - is_alive: {thread.is_alive()}")   # False
```

---

## Starting and Joining Threads

### start() — Begin Execution

```python
import threading

def task():
    print("Task running")

thread = threading.Thread(target=task)
thread.start()  # Returns immediately, thread runs in background

# Can only start a thread once
# thread.start()  # RuntimeError: threads can only be started once
```

### join() — Wait for Completion

```python
import threading
import time

def slow_task():
    time.sleep(2)
    print("Slow task done")

thread = threading.Thread(target=slow_task)
thread.start()

print("Waiting for thread...")
thread.join()  # Blocks until thread completes
print("Thread finished")

# With timeout
thread2 = threading.Thread(target=slow_task)
thread2.start()
thread2.join(timeout=1)  # Wait at most 1 second

if thread2.is_alive():
    print("Thread still running after timeout")
```

---

## Multiple Threads

### Creating Multiple Threads

```python
import threading
import time

def worker(worker_id):
    print(f"Worker {worker_id}: Starting")
    time.sleep(1)
    print(f"Worker {worker_id}: Done")

# Create threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All workers finished")
```

### Compact Pattern

```python
import threading

def worker(n):
    return n * 2

# Create, start, and collect threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

# Wait for all
for t in threads:
    t.join()
```

---

## Thread Arguments

### Positional Arguments (args)

```python
import threading

def greet(name, greeting):
    print(f"{greeting}, {name}!")

# Pass as tuple
thread = threading.Thread(target=greet, args=("Alice", "Hello"))
thread.start()
thread.join()
```

### Keyword Arguments (kwargs)

```python
import threading

def greet(name, greeting="Hi"):
    print(f"{greeting}, {name}!")

# Pass as dict
thread = threading.Thread(target=greet, kwargs={"name": "Bob", "greeting": "Hey"})
thread.start()
thread.join()

# Mixed
thread = threading.Thread(target=greet, args=("Charlie",), kwargs={"greeting": "Howdy"})
thread.start()
thread.join()
```

---

## Getting Results from Threads

### Method 1: Shared Variable

```python
import threading

results = {}
lock = threading.Lock()

def compute(task_id, value):
    result = value ** 2
    with lock:
        results[task_id] = result

threads = []
for i in range(5):
    t = threading.Thread(target=compute, args=(i, i + 10))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(results)  # {0: 100, 1: 121, 2: 144, 3: 169, 4: 196}
```

### Method 2: Thread-Safe Queue

```python
import threading
import queue

def compute(value, result_queue):
    result = value ** 2
    result_queue.put((value, result))

result_queue = queue.Queue()
threads = []

for i in range(5):
    t = threading.Thread(target=compute, args=(i, result_queue))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Collect results
results = []
while not result_queue.empty():
    results.append(result_queue.get())

print(results)
```

### Method 3: Thread Subclass with Attribute

```python
import threading

class ComputeThread(threading.Thread):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.result = None
    
    def run(self):
        self.result = self.value ** 2

threads = [ComputeThread(i) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

results = [t.result for t in threads]
print(results)  # [0, 1, 4, 9, 16]
```

---

## Thread Properties

### Thread Name

```python
import threading

def worker():
    print(f"Running in: {threading.current_thread().name}")

# Auto-generated name
t1 = threading.Thread(target=worker)
t1.start()  # "Thread-1"

# Custom name
t2 = threading.Thread(target=worker, name="MyWorker")
t2.start()  # "MyWorker"
```

### Daemon Threads

Daemon threads are automatically killed when the main program exits:

```python
import threading
import time

def background_task():
    while True:
        print("Background running...")
        time.sleep(1)

# Non-daemon (default): program waits for thread
t1 = threading.Thread(target=background_task)
t1.daemon = False  # Default
# t1.start()  # Program would never exit!

# Daemon: thread killed when main exits
t2 = threading.Thread(target=background_task, daemon=True)
t2.start()

time.sleep(3)
print("Main exiting...")
# Daemon thread is killed here
```

### Current Thread Info

```python
import threading

def show_info():
    current = threading.current_thread()
    print(f"Name: {current.name}")
    print(f"Ident: {current.ident}")
    print(f"Native ID: {current.native_id}")
    print(f"Daemon: {current.daemon}")
    print(f"Is alive: {current.is_alive()}")

thread = threading.Thread(target=show_info, name="InfoThread")
thread.start()
thread.join()

# Main thread info
print(f"\nMain thread: {threading.main_thread().name}")
print(f"Active threads: {threading.active_count()}")
print(f"All threads: {threading.enumerate()}")
```

---

## Exception Handling

### Exceptions in Threads

Exceptions in threads don't propagate to the main thread:

```python
import threading
import time

def risky_task():
    time.sleep(0.5)
    raise ValueError("Something went wrong!")

thread = threading.Thread(target=risky_task)
thread.start()
thread.join()

print("Main continues...")  # This still runs!
# Exception is printed but not raised in main thread
```

### Catching Exceptions

```python
import threading
import traceback

class SafeThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exception = None
    
    def run(self):
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        except Exception as e:
            self.exception = e
            self.traceback = traceback.format_exc()

def risky_task():
    raise ValueError("Error!")

thread = SafeThread(target=risky_task)
thread.start()
thread.join()

if thread.exception:
    print(f"Thread raised: {thread.exception}")
    print(thread.traceback)
```

---

## Practical Example: Parallel Downloads

```python
import threading
import time
import random

def download_file(filename):
    """Simulate file download."""
    print(f"Downloading {filename}...")
    # Simulate varying download times
    time.sleep(random.uniform(0.5, 2.0))
    print(f"Completed {filename}")
    return f"{filename}: {random.randint(100, 1000)} bytes"

def download_sequential(files):
    """Download files one by one."""
    results = []
    for f in files:
        results.append(download_file(f))
    return results

def download_parallel(files):
    """Download files in parallel using threads."""
    results = []
    lock = threading.Lock()
    
    def download_and_store(filename):
        result = download_file(filename)
        with lock:
            results.append(result)
    
    threads = []
    for f in files:
        t = threading.Thread(target=download_and_store, args=(f,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    return results

# Test
files = ["file1.zip", "file2.zip", "file3.zip", "file4.zip", "file5.zip"]

# Sequential
start = time.perf_counter()
download_sequential(files)
seq_time = time.perf_counter() - start
print(f"\nSequential: {seq_time:.2f}s")

# Parallel
start = time.perf_counter()
download_parallel(files)
par_time = time.perf_counter() - start
print(f"Parallel: {par_time:.2f}s")
print(f"Speedup: {seq_time/par_time:.1f}x")
```

---

## Key Takeaways

- Create threads with `threading.Thread(target=func, args=())`
- Call `start()` to begin execution, `join()` to wait for completion
- Threads share memory — use locks for safe access
- Get results via shared variables, queues, or thread subclass attributes
- Daemon threads are killed when main program exits
- Exceptions in threads don't propagate — handle them explicitly
- Best for I/O-bound tasks where GIL is released
