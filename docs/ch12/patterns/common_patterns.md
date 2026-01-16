# Common Concurrency Patterns

Practical patterns for concurrent and parallel programming in Python.

---

## Pattern 1: Parallel Map

Apply a function to each item in a collection:

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def process(item):
    return item ** 2

items = list(range(100))

# I/O-bound: use threads
with ThreadPoolExecutor() as executor:
    results = list(executor.map(process, items))

# CPU-bound: use processes
with ProcessPoolExecutor() as executor:
    results = list(executor.map(process, items))
```

---

## Pattern 2: Producer-Consumer

Separate data production from consumption:

```python
from concurrent.futures import ThreadPoolExecutor
import queue
import threading

def producer(q, items):
    """Produce items into queue."""
    for item in items:
        q.put(item)
    q.put(None)  # Sentinel

def consumer(q, process_func):
    """Consume items from queue."""
    results = []
    while True:
        item = q.get()
        if item is None:
            break
        results.append(process_func(item))
    return results

# Using queue for decoupling
q = queue.Queue(maxsize=10)  # Bounded queue

# Start producer and consumer
with ThreadPoolExecutor(max_workers=2) as executor:
    producer_future = executor.submit(producer, q, range(100))
    consumer_future = executor.submit(consumer, q, lambda x: x ** 2)
    
    producer_future.result()
    results = consumer_future.result()
```

---

## Pattern 3: Pipeline

Chain processing stages:

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import queue

def stage1_fetch(urls):
    """I/O-bound: fetch data."""
    with ThreadPoolExecutor(max_workers=10) as executor:
        return list(executor.map(fetch_url, urls))

def stage2_process(data_list):
    """CPU-bound: process data."""
    with ProcessPoolExecutor() as executor:
        return list(executor.map(process_data, data_list))

def stage3_save(results):
    """I/O-bound: save results."""
    with ThreadPoolExecutor(max_workers=5) as executor:
        return list(executor.map(save_result, results))

# Run pipeline
urls = [...]
raw_data = stage1_fetch(urls)
processed = stage2_process(raw_data)
saved = stage3_save(processed)
```

---

## Pattern 4: Fan-Out / Fan-In

Distribute work, then aggregate results:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def fan_out_fan_in(items, process_func, aggregate_func, max_workers=10):
    """
    Fan-out: Process items concurrently
    Fan-in: Aggregate all results
    """
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Fan-out: submit all tasks
        futures = [executor.submit(process_func, item) for item in items]
        
        # Fan-in: collect results
        results = []
        for future in as_completed(futures):
            try:
                results.append(future.result())
            except Exception as e:
                print(f"Task failed: {e}")
        
        # Aggregate
        return aggregate_func(results)

# Usage
urls = [...]
total_bytes = fan_out_fan_in(
    urls,
    process_func=lambda url: len(requests.get(url).content),
    aggregate_func=sum
)
```

---

## Pattern 5: Worker Pool with Results

Manage workers and collect results:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def worker_pool_with_results(tasks, worker_func, max_workers=10):
    """Execute tasks and return results with task info."""
    results = {}
    errors = {}
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks with tracking
        future_to_task = {
            executor.submit(worker_func, task): task 
            for task in tasks
        }
        
        # Collect results
        for future in as_completed(future_to_task):
            task = future_to_task[future]
            try:
                results[task] = future.result()
            except Exception as e:
                errors[task] = str(e)
    
    return results, errors

# Usage
def fetch(url):
    return requests.get(url).status_code

results, errors = worker_pool_with_results(urls, fetch)
print(f"Successes: {len(results)}, Failures: {len(errors)}")
```

---

## Pattern 6: Timeout with Fallback

Handle slow tasks gracefully:

```python
from concurrent.futures import ThreadPoolExecutor, TimeoutError

def with_timeout(func, args=(), timeout=5, fallback=None):
    """Execute function with timeout and fallback."""
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func, *args)
        try:
            return future.result(timeout=timeout)
        except TimeoutError:
            future.cancel()
            return fallback

# Usage
result = with_timeout(
    slow_api_call,
    args=(url,),
    timeout=5,
    fallback={"error": "timeout"}
)
```

---

## Pattern 7: Rate Limiting

Control request rate:

```python
from concurrent.futures import ThreadPoolExecutor
import time
import threading

class RateLimiter:
    def __init__(self, calls_per_second):
        self.delay = 1.0 / calls_per_second
        self.lock = threading.Lock()
        self.last_call = 0
    
    def wait(self):
        with self.lock:
            now = time.time()
            wait_time = self.last_call + self.delay - now
            if wait_time > 0:
                time.sleep(wait_time)
            self.last_call = time.time()

def rate_limited_fetch(rate_limiter, url):
    rate_limiter.wait()
    return requests.get(url)

# Usage: 10 requests per second max
limiter = RateLimiter(calls_per_second=10)

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [
        executor.submit(rate_limited_fetch, limiter, url)
        for url in urls
    ]
    results = [f.result() for f in futures]
```

---

## Pattern 8: Retry with Backoff

Retry failed tasks with exponential backoff:

```python
from concurrent.futures import ThreadPoolExecutor
import time
import random

def retry_with_backoff(func, max_retries=3, base_delay=1):
    """Retry function with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            print(f"Attempt {attempt + 1} failed, retrying in {delay:.1f}s")
            time.sleep(delay)

def robust_fetch(url):
    return retry_with_backoff(lambda: requests.get(url, timeout=5))

# With executor
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(robust_fetch, url) for url in urls]
    results = [f.result() for f in futures]
```

---

## Pattern 9: Progress Tracking

Track completion progress:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

class ProgressTracker:
    def __init__(self, total):
        self.total = total
        self.completed = 0
        self.lock = threading.Lock()
    
    def update(self):
        with self.lock:
            self.completed += 1
            percent = 100 * self.completed / self.total
            print(f"\rProgress: {self.completed}/{self.total} ({percent:.0f}%)", end="")
    
    def finish(self):
        print()  # New line

def process_with_progress(items, func, max_workers=10):
    tracker = ProgressTracker(len(items))
    
    def wrapped(item):
        result = func(item)
        tracker.update()
        return result
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(wrapped, items))
    
    tracker.finish()
    return results

# Usage
results = process_with_progress(urls, fetch_url)
```

---

## Pattern 10: Batch Processing

Process items in batches:

```python
from concurrent.futures import ProcessPoolExecutor

def batch_process(items, func, batch_size=100, max_workers=None):
    """Process items in batches for better efficiency."""
    def process_batch(batch):
        return [func(item) for item in batch]
    
    # Create batches
    batches = [
        items[i:i + batch_size]
        for i in range(0, len(items), batch_size)
    ]
    
    # Process batches in parallel
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        batch_results = list(executor.map(process_batch, batches))
    
    # Flatten results
    return [item for batch in batch_results for item in batch]

# Usage
results = batch_process(large_list, expensive_func, batch_size=1000)
```

---

## Pattern 11: Graceful Shutdown

Handle shutdown cleanly:

```python
from concurrent.futures import ThreadPoolExecutor
import signal
import threading

class GracefulExecutor:
    def __init__(self, max_workers=10):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.shutdown_event = threading.Event()
        
        # Handle Ctrl+C
        signal.signal(signal.SIGINT, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        print("\nShutdown requested...")
        self.shutdown_event.set()
        self.executor.shutdown(wait=False, cancel_futures=True)
    
    def submit(self, func, *args):
        if self.shutdown_event.is_set():
            return None
        return self.executor.submit(func, *args)
    
    def map(self, func, items):
        futures = []
        for item in items:
            if self.shutdown_event.is_set():
                break
            futures.append(self.executor.submit(func, item))
        return [f.result() for f in futures if f and not f.cancelled()]
    
    def shutdown(self):
        self.executor.shutdown(wait=True)

# Usage
executor = GracefulExecutor()
try:
    results = executor.map(slow_task, items)
finally:
    executor.shutdown()
```

---

## Pattern 12: Resource Pool

Manage limited resources:

```python
from concurrent.futures import ThreadPoolExecutor
import threading

class ResourcePool:
    def __init__(self, resources):
        self.resources = list(resources)
        self.semaphore = threading.Semaphore(len(resources))
        self.lock = threading.Lock()
    
    def acquire(self):
        self.semaphore.acquire()
        with self.lock:
            return self.resources.pop()
    
    def release(self, resource):
        with self.lock:
            self.resources.append(resource)
        self.semaphore.release()

def use_pooled_resource(pool, task_func, *args):
    """Use a resource from pool for task."""
    resource = pool.acquire()
    try:
        return task_func(resource, *args)
    finally:
        pool.release(resource)

# Usage: Database connection pool
connections = [create_connection() for _ in range(5)]
pool = ResourcePool(connections)

def query(conn, sql):
    return conn.execute(sql)

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [
        executor.submit(use_pooled_resource, pool, query, sql)
        for sql in queries
    ]
    results = [f.result() for f in futures]
```

---

## Key Takeaways

1. **Parallel Map**: Simplest pattern for independent tasks
2. **Producer-Consumer**: Decouple production from processing
3. **Pipeline**: Chain stages with appropriate executors
4. **Fan-Out/Fan-In**: Distribute work, aggregate results
5. **Timeout/Retry**: Handle failures gracefully
6. **Rate Limiting**: Control resource usage
7. **Progress Tracking**: Monitor long-running jobs
8. **Batch Processing**: Reduce overhead for many small tasks
9. **Graceful Shutdown**: Clean termination handling
10. **Resource Pool**: Manage limited resources safely
