# Threads vs Processes

Understanding the fundamental differences between threads and processes is essential for choosing the right concurrency model.

---

## Fundamental Difference

### Process

A **process** is an independent program execution with its own:
- Memory space
- Python interpreter
- Global variables
- File descriptors

```
Process 1              Process 2
┌─────────────────┐    ┌─────────────────┐
│ Memory Space    │    │ Memory Space    │
│ ┌─────────────┐ │    │ ┌─────────────┐ │
│ │ Python      │ │    │ │ Python      │ │
│ │ Interpreter │ │    │ │ Interpreter │ │
│ └─────────────┘ │    │ └─────────────┘ │
│ Variables: x=1  │    │ Variables: x=2  │
│ GIL: Own GIL    │    │ GIL: Own GIL    │
└─────────────────┘    └─────────────────┘
     Isolated              Isolated
```

### Thread

A **thread** is a lightweight unit of execution that shares:
- Memory space (with other threads in same process)
- Python interpreter
- Global variables
- File descriptors

```
Process (with threads)
┌───────────────────────────────────────┐
│           Shared Memory Space         │
│  ┌─────────────────────────────────┐  │
│  │      Python Interpreter         │  │
│  │           (One GIL)             │  │
│  └─────────────────────────────────┘  │
│                                       │
│  Thread 1    Thread 2    Thread 3     │
│  ┌───────┐   ┌───────┐   ┌───────┐   │
│  │Stack 1│   │Stack 2│   │Stack 3│   │
│  └───────┘   └───────┘   └───────┘   │
│                                       │
│  Shared Variables: x, y, z            │
└───────────────────────────────────────┘
```

---

## Comparison Table

| Aspect | Thread | Process |
|--------|--------|---------|
| **Memory** | Shared | Isolated |
| **Creation overhead** | Low (~1ms) | High (~100ms) |
| **Memory overhead** | Low (~1MB) | High (~10-50MB) |
| **Communication** | Easy (shared variables) | Complex (IPC required) |
| **GIL impact** | Affected (one GIL) | Not affected (own GIL) |
| **Crash isolation** | Crash affects all threads | Crash isolated to process |
| **Best for** | I/O-bound tasks | CPU-bound tasks |

---

## Memory Sharing Demonstration

### Threads: Shared Memory

```python
import threading
import time

# Shared variable
shared_list = []

def worker(name, count):
    for i in range(count):
        shared_list.append(f"{name}-{i}")
        time.sleep(0.01)

# Create threads
t1 = threading.Thread(target=worker, args=("A", 5))
t2 = threading.Thread(target=worker, args=("B", 5))

t1.start()
t2.start()
t1.join()
t2.join()

print(shared_list)
# ['A-0', 'B-0', 'A-1', 'B-1', 'A-2', ...]  — Interleaved, shared!
```

### Processes: Isolated Memory

```python
from multiprocessing import Process
import time

# This list is NOT shared between processes
shared_list = []

def worker(name, count):
    for i in range(count):
        shared_list.append(f"{name}-{i}")
    print(f"{name}: {shared_list}")  # Each process sees its own copy

# Create processes
p1 = Process(target=worker, args=("A", 5))
p2 = Process(target=worker, args=("B", 5))

p1.start()
p2.start()
p1.join()
p2.join()

print(f"Main: {shared_list}")  # Empty! Main process has its own copy

# Output:
# A: ['A-0', 'A-1', 'A-2', 'A-3', 'A-4']
# B: ['B-0', 'B-1', 'B-2', 'B-3', 'B-4']
# Main: []
```

---

## Creation Overhead

### Benchmark: Thread vs Process Creation

```python
import time
import threading
from multiprocessing import Process

def dummy():
    pass

# Thread creation time
start = time.perf_counter()
threads = [threading.Thread(target=dummy) for _ in range(100)]
for t in threads:
    t.start()
for t in threads:
    t.join()
thread_time = time.perf_counter() - start
print(f"100 threads: {thread_time*1000:.1f}ms")

# Process creation time
start = time.perf_counter()
processes = [Process(target=dummy) for _ in range(100)]
for p in processes:
    p.start()
for p in processes:
    p.join()
process_time = time.perf_counter() - start
print(f"100 processes: {process_time*1000:.1f}ms")

# Typical results:
# 100 threads: 15ms
# 100 processes: 1500ms  (100x slower to create)
```

---

## Communication Methods

### Threads: Direct Variable Access

```python
import threading
import queue

# Method 1: Shared variables (needs synchronization)
result = None
lock = threading.Lock()

def compute():
    global result
    value = expensive_computation()
    with lock:
        result = value

# Method 2: Thread-safe queue (recommended)
result_queue = queue.Queue()

def compute_with_queue():
    value = expensive_computation()
    result_queue.put(value)

thread = threading.Thread(target=compute_with_queue)
thread.start()
thread.join()
result = result_queue.get()
```

### Processes: Inter-Process Communication (IPC)

```python
from multiprocessing import Process, Queue, Pipe, Value, Array

# Method 1: Queue (recommended)
def worker_queue(q):
    result = expensive_computation()
    q.put(result)

q = Queue()
p = Process(target=worker_queue, args=(q,))
p.start()
p.join()
result = q.get()

# Method 2: Pipe
def worker_pipe(conn):
    result = expensive_computation()
    conn.send(result)
    conn.close()

parent_conn, child_conn = Pipe()
p = Process(target=worker_pipe, args=(child_conn,))
p.start()
result = parent_conn.recv()
p.join()

# Method 3: Shared Value
def worker_value(shared_val):
    shared_val.value = 42

shared = Value('i', 0)  # 'i' = integer
p = Process(target=worker_value, args=(shared,))
p.start()
p.join()
print(shared.value)  # 42

# Method 4: Shared Array
def worker_array(shared_arr):
    for i in range(len(shared_arr)):
        shared_arr[i] = i * 2

shared = Array('d', [0.0, 0.0, 0.0])  # 'd' = double
p = Process(target=worker_array, args=(shared,))
p.start()
p.join()
print(list(shared))  # [0.0, 2.0, 4.0]
```

---

## Error Isolation

### Threads: Crash Affects Entire Process

```python
import threading
import time

def risky_worker():
    time.sleep(0.5)
    raise RuntimeError("Worker crashed!")

def stable_worker():
    for i in range(5):
        print(f"Stable worker: {i}")
        time.sleep(0.3)

t1 = threading.Thread(target=risky_worker)
t2 = threading.Thread(target=stable_worker)

t1.start()
t2.start()

t1.join()  # Exception propagates but thread terminates
t2.join()

# Both threads run in same process
# Unhandled exception in t1 prints traceback but t2 continues
# However, if t1 corrupts shared state, t2 is affected
```

### Processes: Crash is Isolated

```python
from multiprocessing import Process
import time

def risky_worker():
    time.sleep(0.5)
    raise RuntimeError("Worker crashed!")

def stable_worker():
    for i in range(5):
        print(f"Stable worker: {i}")
        time.sleep(0.3)

p1 = Process(target=risky_worker)
p2 = Process(target=stable_worker)

p1.start()
p2.start()

p1.join()
p2.join()

print(f"p1 exit code: {p1.exitcode}")  # Non-zero (crashed)
print(f"p2 exit code: {p2.exitcode}")  # 0 (success)

# p1 crash does NOT affect p2
```

---

## Resource Limits

### Operating System Limits

```python
import threading
from multiprocessing import Process
import resource

# Check limits (Unix)
soft, hard = resource.getrlimit(resource.RLIMIT_NPROC)
print(f"Max processes: soft={soft}, hard={hard}")

# Threads are limited by memory, not explicit limit
# Typical: thousands of threads possible
# But: each thread uses ~1MB stack by default

# Processes are limited by OS
# Typical: hundreds to thousands depending on system
```

### Practical Limits

| Resource | Threads | Processes |
|----------|---------|-----------|
| **Reasonable count** | 10-100 | 2-16 (CPU cores) |
| **Memory per unit** | ~1MB (stack) | ~50MB+ (full Python) |
| **Creation time** | ~0.1ms | ~10-100ms |
| **Context switch** | Fast | Slower |

---

## When to Use Each

### Use Threads When:

```python
from concurrent.futures import ThreadPoolExecutor

# ✓ I/O-bound tasks
# ✓ Need shared state
# ✓ Many concurrent tasks
# ✓ Low memory requirements

def fetch_url(url):
    import requests
    return requests.get(url).text

urls = ["http://example.com"] * 100

with ThreadPoolExecutor(max_workers=20) as executor:
    results = list(executor.map(fetch_url, urls))
```

### Use Processes When:

```python
from concurrent.futures import ProcessPoolExecutor

# ✓ CPU-bound tasks
# ✓ Need true parallelism
# ✓ Crash isolation required
# ✓ Can tolerate memory overhead

def compute_heavy(n):
    return sum(i ** 2 for i in range(n))

numbers = [10_000_000] * 8

with ProcessPoolExecutor() as executor:
    results = list(executor.map(compute_heavy, numbers))
```

---

## Summary Comparison

```
                    Threads              Processes
                    ───────              ─────────
Memory:             Shared               Isolated
GIL:                Blocked by GIL       Each has own GIL
Creation:           Fast                 Slow
Communication:      Easy                 Requires IPC
Best for:           I/O-bound            CPU-bound
Crash impact:       Affects process      Isolated
Memory usage:       Low                  High
Parallelism:        Concurrent           True parallel
```

---

## Key Takeaways

- **Threads** share memory, are lightweight, but limited by GIL for CPU work
- **Processes** have isolated memory, bypass GIL, enable true parallelism
- **Communication**: Threads use shared variables; processes need queues/pipes
- **Error isolation**: Process crashes are isolated; thread crashes can corrupt shared state
- **Rule of thumb**: Threads for I/O, processes for CPU
- **concurrent.futures** abstracts the choice with unified API
