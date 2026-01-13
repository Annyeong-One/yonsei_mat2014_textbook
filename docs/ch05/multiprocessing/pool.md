# Process Pool

A `Pool` manages a collection of worker processes, providing a simple way to parallelize function execution across multiple inputs.

---

## Creating a Pool

### Basic Pool Usage

```python
from multiprocessing import Pool
import os

def square(x):
    print(f"Process {os.getpid()}: computing {x}²")
    return x ** 2

if __name__ == "__main__":
    # Create pool with 4 worker processes
    with Pool(4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
    
    print(results)  # [1, 4, 9, 16, 25]
```

### Default Worker Count

```python
from multiprocessing import Pool, cpu_count

# Default: uses cpu_count() workers
with Pool() as pool:
    print(f"Workers: {pool._processes}")  # Number of CPUs

# Explicit count
with Pool(processes=8) as pool:
    pass
```

---

## Pool Methods

### map() — Parallel Map

Apply function to each item in iterable, return results in order:

```python
from multiprocessing import Pool
import time

def slow_square(x):
    time.sleep(0.5)
    return x ** 2

if __name__ == "__main__":
    numbers = list(range(10))
    
    # Sequential
    start = time.perf_counter()
    results = list(map(slow_square, numbers))
    print(f"Sequential: {time.perf_counter() - start:.2f}s")
    
    # Parallel
    start = time.perf_counter()
    with Pool(4) as pool:
        results = pool.map(slow_square, numbers)
    print(f"Parallel: {time.perf_counter() - start:.2f}s")
    
    print(results)
```

### map() with Chunksize

```python
from multiprocessing import Pool

def process(x):
    return x * 2

if __name__ == "__main__":
    data = list(range(1000))
    
    with Pool(4) as pool:
        # Default: pool divides work automatically
        results = pool.map(process, data)
        
        # Chunksize: send N items to each worker at a time
        # Larger chunks = less IPC overhead, but less load balancing
        results = pool.map(process, data, chunksize=100)
```

### starmap() — Multiple Arguments

```python
from multiprocessing import Pool

def power(base, exp):
    return base ** exp

if __name__ == "__main__":
    # starmap unpacks argument tuples
    args = [(2, 3), (3, 4), (4, 5), (5, 6)]
    
    with Pool(4) as pool:
        results = pool.starmap(power, args)
    
    print(results)  # [8, 81, 1024, 15625]
```

### imap() — Lazy Iterator

Returns results as they complete (memory efficient for large datasets):

```python
from multiprocessing import Pool
import time

def slow_process(x):
    time.sleep(0.5)
    return x ** 2

if __name__ == "__main__":
    with Pool(4) as pool:
        # imap returns iterator, not list
        results = pool.imap(slow_process, range(10))
        
        # Process results as they become available
        for result in results:
            print(f"Got result: {result}")
```

### imap_unordered() — Fastest Results First

Returns results in completion order (not input order):

```python
from multiprocessing import Pool
import time
import random

def variable_task(x):
    delay = random.uniform(0.1, 1.0)
    time.sleep(delay)
    return (x, delay)

if __name__ == "__main__":
    with Pool(4) as pool:
        # Results come in completion order
        for result in pool.imap_unordered(variable_task, range(10)):
            print(f"Completed: {result}")
```

### apply() — Single Function Call

```python
from multiprocessing import Pool

def compute(x, y, z):
    return x + y + z

if __name__ == "__main__":
    with Pool(4) as pool:
        # apply() blocks until result ready
        result = pool.apply(compute, args=(1, 2, 3))
        print(result)  # 6
```

### apply_async() — Asynchronous Single Call

```python
from multiprocessing import Pool
import time

def slow_compute(x):
    time.sleep(1)
    return x ** 2

if __name__ == "__main__":
    with Pool(4) as pool:
        # Submit task, get AsyncResult immediately
        async_result = pool.apply_async(slow_compute, args=(10,))
        
        print("Doing other work...")
        time.sleep(0.5)
        
        # Get result (blocks if not ready)
        result = async_result.get()
        print(f"Result: {result}")
```

### map_async() — Asynchronous Map

```python
from multiprocessing import Pool
import time

def process(x):
    time.sleep(0.5)
    return x ** 2

if __name__ == "__main__":
    with Pool(4) as pool:
        # Submit all tasks, get AsyncResult
        async_result = pool.map_async(process, range(10))
        
        print("Tasks submitted, doing other work...")
        
        # Check if ready
        while not async_result.ready():
            print("Still working...")
            time.sleep(0.3)
        
        # Get all results
        results = async_result.get()
        print(results)
```

---

## AsyncResult Object

Methods available on `AsyncResult` returned by async methods:

```python
from multiprocessing import Pool
import time

def slow_task(x):
    time.sleep(2)
    return x ** 2

if __name__ == "__main__":
    with Pool(4) as pool:
        async_result = pool.apply_async(slow_task, args=(10,))
        
        # Check if complete
        print(f"Ready: {async_result.ready()}")  # False
        
        # Wait with timeout
        async_result.wait(timeout=1)
        print(f"Ready after wait: {async_result.ready()}")  # Still False
        
        # Check if successful (blocks until complete)
        # print(f"Successful: {async_result.successful()}")
        
        # Get result (blocks until complete)
        result = async_result.get(timeout=5)
        print(f"Result: {result}")
```

---

## Error Handling in Pools

### Handling Exceptions

```python
from multiprocessing import Pool

def risky_task(x):
    if x == 3:
        raise ValueError(f"Cannot process {x}")
    return x ** 2

if __name__ == "__main__":
    with Pool(4) as pool:
        try:
            # Exception raised when iterating results
            results = pool.map(risky_task, [1, 2, 3, 4, 5])
        except ValueError as e:
            print(f"Error: {e}")
```

### Handling Exceptions with imap

```python
from multiprocessing import Pool

def risky_task(x):
    if x == 3:
        raise ValueError(f"Cannot process {x}")
    return x ** 2

if __name__ == "__main__":
    with Pool(4) as pool:
        results = pool.imap(risky_task, range(5))
        
        for i in range(5):
            try:
                result = next(results)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
            except StopIteration:
                break
```

### Error Callback with apply_async

```python
from multiprocessing import Pool

def task(x):
    if x < 0:
        raise ValueError("Negative!")
    return x ** 2

def on_success(result):
    print(f"Success: {result}")

def on_error(error):
    print(f"Error: {error}")

if __name__ == "__main__":
    with Pool(4) as pool:
        # Success case
        pool.apply_async(task, args=(5,), callback=on_success, error_callback=on_error)
        
        # Error case
        pool.apply_async(task, args=(-1,), callback=on_success, error_callback=on_error)
        
        pool.close()
        pool.join()
```

---

## Pool Lifecycle

### Manual Management

```python
from multiprocessing import Pool

def task(x):
    return x ** 2

if __name__ == "__main__":
    pool = Pool(4)
    
    try:
        results = pool.map(task, range(10))
        print(results)
    finally:
        pool.close()  # No more tasks accepted
        pool.join()   # Wait for workers to finish
```

### Context Manager (Recommended)

```python
from multiprocessing import Pool

def task(x):
    return x ** 2

if __name__ == "__main__":
    with Pool(4) as pool:
        results = pool.map(task, range(10))
        print(results)
    # Pool automatically closed and joined
```

### terminate() vs close()

```python
from multiprocessing import Pool

def task(x):
    return x ** 2

if __name__ == "__main__":
    pool = Pool(4)
    
    # close(): No new tasks, wait for existing to finish
    pool.close()
    pool.join()
    
    # terminate(): Kill workers immediately
    pool2 = Pool(4)
    pool2.terminate()  # Don't wait for tasks
    pool2.join()
```

---

## Initializer Functions

Run setup code in each worker process:

```python
from multiprocessing import Pool
import os

# Global variable in worker processes
worker_data = None

def init_worker(shared_data):
    """Called once when each worker starts."""
    global worker_data
    worker_data = shared_data
    print(f"Worker {os.getpid()} initialized with {shared_data}")

def process_item(x):
    """Use initialized data."""
    return x * worker_data

if __name__ == "__main__":
    # Pass initializer and its arguments
    with Pool(4, initializer=init_worker, initargs=(10,)) as pool:
        results = pool.map(process_item, [1, 2, 3, 4, 5])
    
    print(results)  # [10, 20, 30, 40, 50]
```

### Database Connection per Worker

```python
from multiprocessing import Pool
import os

# Worker-local database connection
db_connection = None

def init_db():
    """Initialize database connection for this worker."""
    global db_connection
    db_connection = create_database_connection()
    print(f"Worker {os.getpid()}: DB connected")

def query(sql):
    """Use worker's database connection."""
    return db_connection.execute(sql)

if __name__ == "__main__":
    with Pool(4, initializer=init_db) as pool:
        queries = ["SELECT * FROM users", "SELECT * FROM orders"]
        results = pool.map(query, queries)
```

---

## Practical Examples

### Parallel File Processing

```python
from multiprocessing import Pool
from pathlib import Path

def process_file(filepath):
    """Process a single file."""
    content = Path(filepath).read_text()
    word_count = len(content.split())
    return (filepath, word_count)

if __name__ == "__main__":
    files = list(Path(".").glob("*.txt"))
    
    with Pool() as pool:
        results = pool.map(process_file, files)
    
    for filepath, count in results:
        print(f"{filepath}: {count} words")
```

### Parallel Image Processing

```python
from multiprocessing import Pool
from pathlib import Path
# from PIL import Image  # Uncomment if using PIL

def resize_image(args):
    """Resize a single image."""
    input_path, output_path, size = args
    # img = Image.open(input_path)
    # img = img.resize(size)
    # img.save(output_path)
    return f"Resized {input_path}"

if __name__ == "__main__":
    images = [
        ("img1.jpg", "out1.jpg", (100, 100)),
        ("img2.jpg", "out2.jpg", (100, 100)),
        ("img3.jpg", "out3.jpg", (100, 100)),
    ]
    
    with Pool() as pool:
        results = pool.map(resize_image, images)
    
    print(results)
```

### Parallel Web Scraping (I/O + CPU)

```python
from multiprocessing import Pool
import time

def fetch_and_parse(url):
    """Fetch URL and parse content."""
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # return len(soup.find_all('a'))
    time.sleep(0.5)  # Simulate
    return f"Parsed {url}"

if __name__ == "__main__":
    urls = [f"https://example.com/page{i}" for i in range(20)]
    
    with Pool(8) as pool:
        results = pool.map(fetch_and_parse, urls)
    
    print(results)
```

---

## Pool Method Summary

| Method | Blocking | Ordered | Use Case |
|--------|----------|---------|----------|
| `map()` | Yes | Yes | Simple parallel map |
| `starmap()` | Yes | Yes | Multiple arguments |
| `imap()` | Iterator | Yes | Memory efficient |
| `imap_unordered()` | Iterator | No | Fastest results first |
| `apply()` | Yes | N/A | Single function call |
| `apply_async()` | No | N/A | Async single call |
| `map_async()` | No | Yes | Async parallel map |

---

## Key Takeaways

- Use `Pool` for simple parallel function application
- `map()` is the most common method — parallel version of built-in `map()`
- `starmap()` for functions with multiple arguments
- `imap_unordered()` for best performance when order doesn't matter
- Use context manager (`with Pool() as pool:`) for automatic cleanup
- `initializer` sets up per-worker resources (database connections, etc.)
- Match pool size to CPU count for CPU-bound tasks
- Use `chunksize` to tune performance for large datasets
