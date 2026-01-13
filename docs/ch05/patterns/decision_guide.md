# When to Use What

A practical guide for choosing the right concurrency approach in Python.

---

## Quick Decision Flowchart

```
Start
  │
  ├─ Is your task CPU-intensive?
  │   │
  │   ├─ Yes ──────────────────────────► ProcessPoolExecutor
  │   │                                   (or multiprocessing.Pool)
  │   │
  │   └─ No (I/O-intensive or waiting)
  │       │
  │       ├─ Many concurrent connections (1000+)?
  │       │   │
  │       │   └─ Yes ──────────────────► asyncio
  │       │
  │       └─ Moderate concurrency (10-100)?
  │           │
  │           └─ Yes ──────────────────► ThreadPoolExecutor
  │                                      (or threading)
  │
  └─ Simple parallel map over data?
      │
      └─ Yes ──────────────────────────► concurrent.futures
                                          (easiest choice)
```

---

## Decision Matrix

| Task Type | Recommended Approach | Why |
|-----------|---------------------|-----|
| **CPU-bound computation** | `ProcessPoolExecutor` | Bypasses GIL, true parallelism |
| **File I/O** | `ThreadPoolExecutor` | GIL released during I/O |
| **Network requests** | `ThreadPoolExecutor` | GIL released during I/O |
| **Database queries** | `ThreadPoolExecutor` | GIL released during I/O |
| **Web scraping** | `ThreadPoolExecutor` | Mostly waiting for network |
| **Image processing** | `ProcessPoolExecutor` | CPU-intensive pixel operations |
| **Data transformation** | `ProcessPoolExecutor` | CPU-intensive computation |
| **API calls** | `ThreadPoolExecutor` | Network I/O dominant |
| **High-concurrency server** | `asyncio` | Handles thousands of connections |
| **Mixed I/O + CPU** | Both (pipeline) | Separate stages appropriately |

---

## Detailed Guidelines

### Use ThreadPoolExecutor When:

```python
from concurrent.futures import ThreadPoolExecutor

# ✅ Network requests
def fetch_url(url):
    return requests.get(url).text

with ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(fetch_url, urls)

# ✅ File I/O
def read_file(path):
    return open(path).read()

with ThreadPoolExecutor(max_workers=10) as executor:
    contents = executor.map(read_file, file_paths)

# ✅ Database queries
def query_db(sql):
    return db.execute(sql)

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(query_db, queries)
```

**Characteristics:**
- Task spends most time waiting (I/O)
- Low CPU usage per task
- Need shared memory/state
- Quick startup needed

### Use ProcessPoolExecutor When:

```python
from concurrent.futures import ProcessPoolExecutor

# ✅ Heavy computation
def compute(n):
    return sum(i**2 for i in range(n))

with ProcessPoolExecutor() as executor:
    results = executor.map(compute, large_numbers)

# ✅ Image/video processing
def process_image(image_path):
    img = load_image(image_path)
    return apply_filters(img)

with ProcessPoolExecutor() as executor:
    results = executor.map(process_image, image_paths)

# ✅ Data transformation
def transform(chunk):
    return chunk.apply(complex_operation)

with ProcessPoolExecutor() as executor:
    results = executor.map(transform, data_chunks)
```

**Characteristics:**
- Task is CPU-intensive
- High CPU usage per task
- Can tolerate memory copying overhead
- Objects are picklable

### Use asyncio When:

```python
import asyncio
import aiohttp

# ✅ Many concurrent connections
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

asyncio.run(main())
```

**Characteristics:**
- Very high concurrency (thousands)
- All I/O operations
- Need fine-grained control
- Single-threaded is acceptable

### Use Raw threading/multiprocessing When:

```python
import threading
from multiprocessing import Process, Queue

# ✅ Long-running background tasks
def background_worker():
    while True:
        process_queue()

thread = threading.Thread(target=background_worker, daemon=True)
thread.start()

# ✅ Need fine-grained control over processes
def worker(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        process(item)

queue = Queue()
processes = [Process(target=worker, args=(queue,)) for _ in range(4)]
```

**Characteristics:**
- Need long-running workers
- Custom synchronization required
- Complex communication patterns
- Pool pattern doesn't fit

---

## Anti-Patterns to Avoid

### ❌ Threads for CPU-Bound Work

```python
# Bad: No speedup due to GIL
with ThreadPoolExecutor() as executor:
    results = executor.map(heavy_computation, data)

# Good: Use processes
with ProcessPoolExecutor() as executor:
    results = executor.map(heavy_computation, data)
```

### ❌ Processes for Quick I/O Tasks

```python
# Bad: Process overhead dominates
with ProcessPoolExecutor() as executor:
    results = executor.map(quick_api_call, urls)

# Good: Use threads
with ThreadPoolExecutor() as executor:
    results = executor.map(quick_api_call, urls)
```

### ❌ Too Many Workers

```python
# Bad: Resource waste
with ThreadPoolExecutor(max_workers=1000) as executor:
    ...

# Good: Match to workload
# I/O-bound: 10-50 threads typically sufficient
# CPU-bound: os.cpu_count() processes
```

### ❌ Shared Mutable State Without Locks

```python
# Bad: Race condition
results = []
def worker(x):
    results.append(x ** 2)  # Not thread-safe!

# Good: Use thread-safe structures
from queue import Queue
result_queue = Queue()
def worker(x):
    result_queue.put(x ** 2)
```

---

## Performance Comparison

### Benchmark Template

```python
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def benchmark(name, executor_class, func, data, workers=None):
    start = time.perf_counter()
    with executor_class(max_workers=workers) as executor:
        list(executor.map(func, data))
    elapsed = time.perf_counter() - start
    print(f"{name}: {elapsed:.2f}s")

# Test your specific workload
data = [...]

# Sequential baseline
start = time.perf_counter()
results = [func(x) for x in data]
print(f"Sequential: {time.perf_counter() - start:.2f}s")

# Threads
benchmark("Threads", ThreadPoolExecutor, func, data, workers=10)

# Processes
benchmark("Processes", ProcessPoolExecutor, func, data)
```

### Typical Results

| Workload | Sequential | Threads | Processes |
|----------|------------|---------|-----------|
| CPU-bound (4 items) | 4.0s | 4.2s ❌ | 1.1s ✅ |
| I/O-bound (4 items) | 4.0s | 1.1s ✅ | 1.2s |
| Mixed (4 items) | 4.0s | 2.5s | 1.5s ✅ |

---

## Choosing Worker Count

### ThreadPoolExecutor

```python
import os

# I/O-bound: more threads than CPUs
# Most time waiting, not computing
max_workers = 20  # or even 50-100 for pure I/O

# Mixed workload
max_workers = os.cpu_count() * 2

# Default (Python 3.8+)
# min(32, os.cpu_count() + 4)
```

### ProcessPoolExecutor

```python
import os

# CPU-bound: match CPU cores
max_workers = os.cpu_count()

# Leave headroom for system
max_workers = max(1, os.cpu_count() - 1)

# Default
# os.cpu_count()
```

---

## Summary Table

| Approach | Best For | GIL | Overhead | Memory |
|----------|----------|-----|----------|--------|
| `ThreadPoolExecutor` | I/O-bound | Blocked | Low | Shared |
| `ProcessPoolExecutor` | CPU-bound | Bypassed | High | Isolated |
| `asyncio` | High concurrency I/O | Blocked | Lowest | Shared |
| Raw `threading` | Custom thread control | Blocked | Low | Shared |
| Raw `multiprocessing` | Custom process control | Bypassed | High | Isolated |

---

## Key Takeaways

1. **I/O-bound** (network, files, database) → **Threads**
2. **CPU-bound** (computation, processing) → **Processes**
3. **Very high concurrency** (10,000+ connections) → **asyncio**
4. **Simple parallel map** → **concurrent.futures** (start here)
5. **Mixed workloads** → Pipeline with appropriate executor per stage
6. **When in doubt** → Start with `ThreadPoolExecutor`, measure, adjust
7. **Always measure** your specific workload before deciding
