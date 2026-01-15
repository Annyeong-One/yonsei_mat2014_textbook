# CPU-Bound vs I/O-Bound Tasks

Understanding whether your task is CPU-bound or I/O-bound is crucial for choosing the right concurrency strategy.

---

## Definitions

### CPU-Bound

A task is **CPU-bound** when it spends most of its time doing computation — the CPU is the bottleneck.

**Examples:**
- Mathematical calculations
- Image/video processing
- Data compression
- Machine learning training
- Cryptographic operations
- Simulations

```python
def cpu_bound_task(n):
    """Compute sum of squares — CPU is working hard."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total
```

### I/O-Bound

A task is **I/O-bound** when it spends most of its time waiting for input/output operations — the CPU is mostly idle.

**Examples:**
- Network requests (HTTP, database queries)
- File reading/writing
- User input
- API calls
- Web scraping

```python
import requests

def io_bound_task(url):
    """Fetch URL — CPU is mostly waiting."""
    response = requests.get(url)  # Waiting for network
    return response.text
```

---

## Visual Comparison

### CPU-Bound Execution

```
CPU Activity:
████████████████████████████████████████  100% busy

Timeline:
[compute][compute][compute][compute][done]
```

### I/O-Bound Execution

```
CPU Activity:
██░░░░░░░░░░░░░░██░░░░░░░░░░░░░░██░░░░░░  ~20% busy

Timeline:
[send request][.....waiting.....][process response]
```

---

## Identifying Task Type

### Method 1: CPU Usage Monitoring

```python
import time
import psutil

def monitor_cpu(func, *args):
    """Run function while monitoring CPU usage."""
    process = psutil.Process()
    
    start = time.perf_counter()
    cpu_start = process.cpu_times()
    
    result = func(*args)
    
    cpu_end = process.cpu_times()
    elapsed = time.perf_counter() - start
    
    cpu_time = (cpu_end.user - cpu_start.user) + (cpu_end.system - cpu_start.system)
    cpu_percent = (cpu_time / elapsed) * 100
    
    print(f"Elapsed: {elapsed:.2f}s")
    print(f"CPU time: {cpu_time:.2f}s")
    print(f"CPU usage: {cpu_percent:.1f}%")
    
    return result

# CPU-bound: ~100% CPU usage
monitor_cpu(cpu_bound_task, 10_000_000)

# I/O-bound: ~5% CPU usage
monitor_cpu(io_bound_task, "https://httpbin.org/delay/2")
```

### Method 2: Analyze the Code

| Look for... | Task Type |
|-------------|-----------|
| Loops with computation | CPU-bound |
| Mathematical operations | CPU-bound |
| `requests`, `urllib` | I/O-bound |
| File `open()`, `read()`, `write()` | I/O-bound |
| Database queries | I/O-bound |
| `time.sleep()` | I/O-bound (simulated) |
| `subprocess` calls | Usually I/O-bound |

---

## Concurrency Strategy by Task Type

### CPU-Bound → Use Processes

```python
from concurrent.futures import ProcessPoolExecutor
import os

def compute_heavy(n):
    """CPU-intensive task."""
    print(f"Process {os.getpid()}: computing...")
    return sum(i * i for i in range(n))

numbers = [10_000_000, 20_000_000, 30_000_000, 40_000_000]

# ProcessPoolExecutor bypasses GIL
with ProcessPoolExecutor() as executor:
    results = list(executor.map(compute_heavy, numbers))
    
print(results)
```

**Why processes?**
- Each process has its own Python interpreter
- Each process has its own GIL
- True parallel execution on multiple CPU cores

### I/O-Bound → Use Threads

```python
from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_url(url):
    """I/O-intensive task."""
    response = requests.get(url)
    return len(response.content)

urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]

# ThreadPoolExecutor works well — GIL released during I/O
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(fetch_url, urls))

print(results)
```

**Why threads?**
- GIL is released during I/O operations
- Threads are lighter weight than processes
- Shared memory makes data passing easy

---

## Benchmark: Threads vs Processes

### CPU-Bound Benchmark

```python
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def cpu_task(n):
    return sum(i ** 2 for i in range(n))

data = [5_000_000] * 4

# Sequential
start = time.perf_counter()
results = [cpu_task(n) for n in data]
seq_time = time.perf_counter() - start
print(f"Sequential:    {seq_time:.2f}s")

# Threads (limited by GIL)
start = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(cpu_task, data))
thread_time = time.perf_counter() - start
print(f"Threads:       {thread_time:.2f}s")

# Processes (true parallelism)
start = time.perf_counter()
with ProcessPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(cpu_task, data))
proc_time = time.perf_counter() - start
print(f"Processes:     {proc_time:.2f}s")

# Typical results (4-core machine):
# Sequential:    3.2s
# Threads:       3.5s  ← No speedup (GIL)
# Processes:     0.9s  ← ~4x speedup ✓
```

### I/O-Bound Benchmark

```python
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def io_task(seconds):
    time.sleep(seconds)  # Simulate I/O
    return seconds

data = [1] * 4

# Sequential
start = time.perf_counter()
results = [io_task(n) for n in data]
seq_time = time.perf_counter() - start
print(f"Sequential:    {seq_time:.2f}s")

# Threads
start = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(io_task, data))
thread_time = time.perf_counter() - start
print(f"Threads:       {thread_time:.2f}s")

# Processes
start = time.perf_counter()
with ProcessPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(io_task, data))
proc_time = time.perf_counter() - start
print(f"Processes:     {proc_time:.2f}s")

# Typical results:
# Sequential:    4.0s
# Threads:       1.0s  ← 4x speedup ✓
# Processes:     1.1s  ← Similar, but more overhead
```

---

## Mixed Workloads

Many real applications have both CPU and I/O components.

### Example: Download and Process Images

```python
import requests
from PIL import Image
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def download_image(url):
    """I/O-bound: fetch from network."""
    response = requests.get(url)
    return response.content

def process_image(image_bytes):
    """CPU-bound: resize and transform."""
    img = Image.open(BytesIO(image_bytes))
    img = img.resize((100, 100))
    # More CPU-intensive operations...
    return img

urls = ["https://example.com/img1.jpg", "https://example.com/img2.jpg", ...]

# Stage 1: Download (I/O-bound) — use threads
with ThreadPoolExecutor(max_workers=10) as executor:
    image_bytes_list = list(executor.map(download_image, urls))

# Stage 2: Process (CPU-bound) — use processes
with ProcessPoolExecutor() as executor:
    processed_images = list(executor.map(process_image, image_bytes_list))
```

### Example: Web Scraping with Parsing

```python
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def scrape_and_parse(url):
    """Mixed: I/O (fetch) + CPU (parse)."""
    # I/O-bound part
    response = requests.get(url)
    
    # CPU-bound part (but usually fast enough)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('a')

# For mixed tasks where I/O dominates, threads work well
urls = [...]
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(scrape_and_parse, urls))
```

---

## Decision Matrix

| Task Type | Sequential | Threads | Processes |
|-----------|------------|---------|-----------|
| CPU-bound | Baseline | No speedup | ✓ Best |
| I/O-bound | Baseline | ✓ Best | Good (more overhead) |
| Mixed (I/O dominant) | Baseline | ✓ Best | Good |
| Mixed (CPU dominant) | Baseline | Some speedup | ✓ Best |

---

## Quick Decision Guide

```python
def choose_executor(task_type):
    """Choose the right executor for your task."""
    
    if task_type == "cpu_bound":
        # CPU-bound: need true parallelism
        from concurrent.futures import ProcessPoolExecutor
        return ProcessPoolExecutor()
    
    elif task_type == "io_bound":
        # I/O-bound: threads work, lower overhead
        from concurrent.futures import ThreadPoolExecutor
        return ThreadPoolExecutor(max_workers=20)
    
    elif task_type == "mixed_io_dominant":
        # Mixed but mostly waiting: threads fine
        from concurrent.futures import ThreadPoolExecutor
        return ThreadPoolExecutor(max_workers=10)
    
    elif task_type == "mixed_cpu_dominant":
        # Mixed but mostly computing: processes
        from concurrent.futures import ProcessPoolExecutor
        return ProcessPoolExecutor()
```

---

## Key Takeaways

- **CPU-bound**: CPU is busy computing → use **processes**
- **I/O-bound**: CPU is waiting for I/O → use **threads**
- **GIL** blocks thread parallelism for CPU work, but releases during I/O
- **Measure** your task's CPU usage to determine type
- **Mixed workloads**: Consider which component dominates, or use two-stage pipeline
- **When in doubt**: Start with threads for simplicity, switch to processes if no speedup
