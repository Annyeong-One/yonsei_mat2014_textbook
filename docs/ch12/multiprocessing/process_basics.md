# Process Basics

The `multiprocessing` module enables true parallel execution by running code in separate processes, each with its own Python interpreter and GIL.

---

## Creating Processes

### Method 1: Using Process with target Function

```python
from multiprocessing import Process
import os
import time

def worker(name, delay):
    """Function to run in a separate process."""
    print(f"Process {os.getpid()}: {name} starting")
    time.sleep(delay)
    print(f"Process {os.getpid()}: {name} finished")

if __name__ == "__main__":
    # Create process
    p = Process(target=worker, args=("Worker-1", 2))
    
    # Start process
    p.start()
    
    print(f"Main process {os.getpid()}: started child")
    
    # Wait for process to complete
    p.join()
    
    print("Main process: child finished")
```

**Important**: Always use `if __name__ == "__main__":` guard to prevent recursive process spawning.

### Method 2: Subclassing Process

```python
from multiprocessing import Process
import os

class WorkerProcess(Process):
    def __init__(self, name, value):
        super().__init__()
        self.name = name
        self.value = value
    
    def run(self):
        """Override run() method."""
        print(f"Process {os.getpid()}: {self.name} computing...")
        result = self.value ** 2
        print(f"Process {os.getpid()}: result = {result}")

if __name__ == "__main__":
    p = WorkerProcess("Squarer", 10)
    p.start()
    p.join()
```

---

## Process Lifecycle

```
                    ┌─────────┐
                    │ Created │
                    └────┬────┘
                         │ start()
                         ▼
                    ┌─────────┐
                    │ Running │
                    └────┬────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
      completes     exception      terminate()
          │              │              │
          ▼              ▼              ▼
     ┌────────┐    ┌────────┐    ┌────────────┐
     │exitcode│    │exitcode│    │ Terminated │
     │   = 0  │    │  != 0  │    │            │
     └────────┘    └────────┘    └────────────┘
```

### Process States

```python
from multiprocessing import Process
import time

def worker():
    time.sleep(2)

if __name__ == "__main__":
    p = Process(target=worker)
    
    print(f"Created - is_alive: {p.is_alive()}")  # False
    print(f"PID: {p.pid}")  # None
    
    p.start()
    print(f"Started - is_alive: {p.is_alive()}")  # True
    print(f"PID: {p.pid}")  # Actual PID
    
    p.join()
    print(f"Joined - is_alive: {p.is_alive()}")   # False
    print(f"Exit code: {p.exitcode}")  # 0 (success)
```

---

## Multiple Processes

### Creating Multiple Processes

```python
from multiprocessing import Process
import os
import time

def worker(worker_id):
    print(f"Worker {worker_id} (PID {os.getpid()}): Starting")
    time.sleep(1)
    print(f"Worker {worker_id} (PID {os.getpid()}): Done")

if __name__ == "__main__":
    # Create processes
    processes = []
    for i in range(4):
        p = Process(target=worker, args=(i,))
        processes.append(p)
    
    # Start all processes
    for p in processes:
        p.start()
    
    # Wait for all processes
    for p in processes:
        p.join()
    
    print("All workers finished")
```

### Parallel Execution Demonstration

```python
from multiprocessing import Process
import os
import time

def cpu_bound_task(task_id, iterations):
    """CPU-intensive task."""
    print(f"Task {task_id} (PID {os.getpid()}): Starting")
    start = time.perf_counter()
    
    # CPU-bound work
    total = sum(i * i for i in range(iterations))
    
    elapsed = time.perf_counter() - start
    print(f"Task {task_id}: Completed in {elapsed:.2f}s")
    return total

if __name__ == "__main__":
    iterations = 10_000_000
    
    # Sequential
    print("Sequential execution:")
    start = time.perf_counter()
    for i in range(4):
        cpu_bound_task(i, iterations)
    seq_time = time.perf_counter() - start
    print(f"Sequential total: {seq_time:.2f}s\n")
    
    # Parallel
    print("Parallel execution:")
    start = time.perf_counter()
    processes = []
    for i in range(4):
        p = Process(target=cpu_bound_task, args=(i, iterations))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
    par_time = time.perf_counter() - start
    print(f"Parallel total: {par_time:.2f}s")
    print(f"Speedup: {seq_time/par_time:.1f}x")
```

---

## Process Arguments

### Positional Arguments (args)

```python
from multiprocessing import Process

def greet(name, greeting):
    print(f"{greeting}, {name}!")

if __name__ == "__main__":
    p = Process(target=greet, args=("Alice", "Hello"))
    p.start()
    p.join()
```

### Keyword Arguments (kwargs)

```python
from multiprocessing import Process

def greet(name, greeting="Hi"):
    print(f"{greeting}, {name}!")

if __name__ == "__main__":
    p = Process(target=greet, kwargs={"name": "Bob", "greeting": "Hey"})
    p.start()
    p.join()
```

---

## Getting Results from Processes

Processes have **isolated memory** — you cannot simply return values or use shared variables like with threads.

### Method 1: Queue

```python
from multiprocessing import Process, Queue

def compute(x, result_queue):
    """Compute and put result in queue."""
    result = x ** 2
    result_queue.put((x, result))

if __name__ == "__main__":
    result_queue = Queue()
    processes = []
    
    for i in range(5):
        p = Process(target=compute, args=(i, result_queue))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
    
    # Collect results
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    
    print(results)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
```

### Method 2: Pipe

```python
from multiprocessing import Process, Pipe

def compute(x, conn):
    """Compute and send result through pipe."""
    result = x ** 2
    conn.send((x, result))
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    
    p = Process(target=compute, args=(10, child_conn))
    p.start()
    
    result = parent_conn.recv()
    print(f"Result: {result}")  # (10, 100)
    
    p.join()
```

### Method 3: Shared Value

```python
from multiprocessing import Process, Value

def compute(shared_value):
    """Modify shared value."""
    shared_value.value = 42

if __name__ == "__main__":
    # 'i' = signed integer, 'd' = double
    shared = Value('i', 0)
    
    p = Process(target=compute, args=(shared,))
    p.start()
    p.join()
    
    print(f"Result: {shared.value}")  # 42
```

### Method 4: Shared Array

```python
from multiprocessing import Process, Array

def fill_array(shared_array):
    """Fill shared array."""
    for i in range(len(shared_array)):
        shared_array[i] = i * 2

if __name__ == "__main__":
    # 'd' = double, 5 elements
    shared = Array('d', 5)
    
    p = Process(target=fill_array, args=(shared,))
    p.start()
    p.join()
    
    print(f"Result: {list(shared)}")  # [0.0, 2.0, 4.0, 6.0, 8.0]
```

---

## Process Properties

### Process Name and PID

```python
from multiprocessing import Process, current_process
import os

def show_info():
    proc = current_process()
    print(f"Name: {proc.name}")
    print(f"PID: {proc.pid}")
    print(f"os.getpid(): {os.getpid()}")
    print(f"Parent PID: {os.getppid()}")

if __name__ == "__main__":
    p = Process(target=show_info, name="MyWorker")
    p.start()
    p.join()
```

### Daemon Processes

Daemon processes are terminated when the main process exits:

```python
from multiprocessing import Process
import time

def background_task():
    while True:
        print("Background running...")
        time.sleep(1)

if __name__ == "__main__":
    # Daemon process
    p = Process(target=background_task, daemon=True)
    p.start()
    
    time.sleep(3)
    print("Main exiting...")
    # Daemon process is killed here
```

### Exit Codes

```python
from multiprocessing import Process
import sys

def success_task():
    pass  # Exit code 0

def failure_task():
    sys.exit(1)  # Exit code 1

def exception_task():
    raise ValueError("Error!")  # Exit code 1

if __name__ == "__main__":
    p1 = Process(target=success_task)
    p2 = Process(target=failure_task)
    p3 = Process(target=exception_task)
    
    for p in [p1, p2, p3]:
        p.start()
    
    for p in [p1, p2, p3]:
        p.join()
    
    print(f"Success exit code: {p1.exitcode}")   # 0
    print(f"Failure exit code: {p2.exitcode}")   # 1
    print(f"Exception exit code: {p3.exitcode}") # 1
```

---

## Terminating Processes

### terminate() — Forceful Stop

```python
from multiprocessing import Process
import time

def long_task():
    print("Starting long task...")
    time.sleep(60)
    print("Long task done")  # Never reached

if __name__ == "__main__":
    p = Process(target=long_task)
    p.start()
    
    time.sleep(2)
    print("Terminating process...")
    p.terminate()  # Send SIGTERM
    p.join()
    
    print(f"Exit code: {p.exitcode}")  # -15 (SIGTERM)
```

### kill() — Immediate Stop (Python 3.7+)

```python
from multiprocessing import Process
import time

def stubborn_task():
    import signal
    signal.signal(signal.SIGTERM, signal.SIG_IGN)  # Ignore SIGTERM
    while True:
        time.sleep(1)

if __name__ == "__main__":
    p = Process(target=stubborn_task)
    p.start()
    
    time.sleep(1)
    p.kill()  # Send SIGKILL (cannot be ignored)
    p.join()
    
    print(f"Exit code: {p.exitcode}")  # -9 (SIGKILL)
```

---

## Start Methods

Different ways to start new processes:

```python
import multiprocessing as mp

# Check current method
print(mp.get_start_method())

# Set method (must be called before any process creation)
# mp.set_start_method('spawn')
```

| Method | Platforms | Description |
|--------|-----------|-------------|
| `spawn` | All | Start fresh Python interpreter (safest, default on Windows/macOS) |
| `fork` | Unix | Copy parent process (fast, default on Linux) |
| `forkserver` | Unix | Fork from a server process |

### spawn vs fork

```python
import multiprocessing as mp

# spawn: Safe, clean, but slower
# - New Python interpreter
# - Only picklable objects passed
# - No inherited state

# fork: Fast, but potential issues
# - Copies entire process memory
# - Can cause issues with threads
# - Inherits open file handles
```

---

## Exception Handling

### Exceptions in Child Processes

Exceptions in child processes don't propagate to parent:

```python
from multiprocessing import Process

def risky_task():
    raise ValueError("Something went wrong!")

if __name__ == "__main__":
    p = Process(target=risky_task)
    p.start()
    p.join()
    
    print(f"Exit code: {p.exitcode}")  # 1 (error)
    print("Main continues...")  # Parent not affected
```

### Capturing Exceptions

```python
from multiprocessing import Process, Queue
import traceback

def safe_task(func, args, result_queue):
    """Wrapper that captures exceptions."""
    try:
        result = func(*args)
        result_queue.put(("success", result))
    except Exception as e:
        result_queue.put(("error", str(e), traceback.format_exc()))

def risky_compute(x):
    if x < 0:
        raise ValueError("Negative not allowed")
    return x ** 2

if __name__ == "__main__":
    result_queue = Queue()
    
    # Test with valid input
    p1 = Process(target=safe_task, args=(risky_compute, (5,), result_queue))
    p1.start()
    p1.join()
    
    # Test with invalid input
    p2 = Process(target=safe_task, args=(risky_compute, (-1,), result_queue))
    p2.start()
    p2.join()
    
    # Check results
    while not result_queue.empty():
        result = result_queue.get()
        if result[0] == "success":
            print(f"Success: {result[1]}")
        else:
            print(f"Error: {result[1]}")
            print(result[2])
```

---

## CPU Count

```python
import multiprocessing as mp
import os

# Number of CPUs
print(f"multiprocessing.cpu_count(): {mp.cpu_count()}")
print(f"os.cpu_count(): {os.cpu_count()}")

# Rule of thumb for process count:
# CPU-bound: num_processes = cpu_count()
# I/O-bound with some CPU: num_processes = cpu_count() * 2
```

---

## Key Takeaways

- **Processes** have isolated memory — bypass GIL for true parallelism
- Always use `if __name__ == "__main__":` guard
- Use `Queue` or `Pipe` to communicate between processes
- Use `Value` and `Array` for simple shared state
- `start()` creates the process, `join()` waits for completion
- Check `exitcode` for process result (0 = success)
- Use `terminate()` or `kill()` to stop processes forcefully
- Match process count to CPU cores for CPU-bound tasks
- Processes have more overhead than threads — use for CPU-bound work
