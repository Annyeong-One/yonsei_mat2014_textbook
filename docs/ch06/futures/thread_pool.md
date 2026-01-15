# ThreadPoolExecutor

`ThreadPoolExecutor` manages a pool of worker threads for concurrent execution. Best suited for **I/O-bound tasks** where the GIL is released.

---

## Basic Usage

```python
from concurrent.futures import ThreadPoolExecutor
import time

def fetch_url(url):
    """Simulate fetching a URL."""
    print(f"Fetching {url}...")
    time.sleep(1)  # Simulate network delay
    return f"Content from {url}"

urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
]

# Sequential: ~3 seconds
start = time.perf_counter()
results = [fetch_url(url) for url in urls]
print(f"Sequential: {time.perf_counter() - start:.2f}s")

# Concurrent: ~1 second
start = time.perf_counter()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch_url, urls))
print(f"Concurrent: {time.perf_counter() - start:.2f}s")
```

---

## Creating ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor

# Default workers: min(32, os.cpu_count() + 4)
executor = ThreadPoolExecutor()

# Explicit worker count
executor = ThreadPoolExecutor(max_workers=10)

# With thread naming
executor = ThreadPoolExecutor(
    max_workers=5,
    thread_name_prefix="Downloader"
)

# With initializer
executor = ThreadPoolExecutor(
    max_workers=5,
    initializer=setup_function,
    initargs=(arg1, arg2)
)
```

---

## Using map()

Apply a function to every item in an iterable:

```python
from concurrent.futures import ThreadPoolExecutor
import time

def process(item):
    time.sleep(0.5)
    return item.upper()

items = ["apple", "banana", "cherry", "date", "elderberry"]

with ThreadPoolExecutor(max_workers=5) as executor:
    # Results are returned in input order
    results = list(executor.map(process, items))
    print(results)  # ['APPLE', 'BANANA', 'CHERRY', 'DATE', 'ELDERBERRY']
```

### map() with Multiple Arguments

```python
from concurrent.futures import ThreadPoolExecutor

def power(base, exp):
    return base ** exp

bases = [2, 3, 4, 5]
exps = [3, 4, 5, 6]

with ThreadPoolExecutor() as executor:
    # Use zip for multiple iterables
    results = list(executor.map(power, bases, exps))
    print(results)  # [8, 81, 1024, 15625]
```

### map() with Timeout

```python
from concurrent.futures import ThreadPoolExecutor, TimeoutError
import time

def slow_task(x):
    time.sleep(x)
    return x

with ThreadPoolExecutor() as executor:
    try:
        # Timeout applies to entire iteration
        results = list(executor.map(slow_task, [1, 5, 1], timeout=3))
    except TimeoutError:
        print("Operation timed out!")
```

---

## Using submit()

Submit individual tasks and get Future objects:

```python
from concurrent.futures import ThreadPoolExecutor
import time

def download(url):
    time.sleep(1)
    return f"Downloaded {url}"

with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit returns Future immediately
    future1 = executor.submit(download, "https://site1.com")
    future2 = executor.submit(download, "https://site2.com")
    future3 = executor.submit(download, "https://site3.com")
    
    # Get results
    print(future1.result())
    print(future2.result())
    print(future3.result())
```

### Submitting Multiple Tasks

```python
from concurrent.futures import ThreadPoolExecutor

def process(x):
    return x ** 2

with ThreadPoolExecutor() as executor:
    # Submit all tasks
    futures = [executor.submit(process, i) for i in range(10)]
    
    # Collect results
    results = [f.result() for f in futures]
    print(results)
```

---

## Processing Results as They Complete

### as_completed() — Results in Completion Order

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

def variable_task(task_id):
    delay = random.uniform(0.1, 1.0)
    time.sleep(delay)
    return (task_id, delay)

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(variable_task, i): i for i in range(10)}
    
    # Process results as they complete (fastest first)
    for future in as_completed(futures):
        task_id = futures[future]
        try:
            result = future.result()
            print(f"Task {task_id} completed: {result}")
        except Exception as e:
            print(f"Task {task_id} failed: {e}")
```

### as_completed() with Timeout

```python
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(slow_task, i) for i in range(10)]
    
    try:
        for future in as_completed(futures, timeout=5):
            print(future.result())
    except TimeoutError:
        print("Some tasks didn't complete in time")
```

### wait() — Wait for Specific Conditions

```python
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, ALL_COMPLETED
import time

def task(x):
    time.sleep(x)
    return x

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(task, i) for i in [3, 1, 2]]
    
    # Wait for first to complete
    done, not_done = wait(futures, return_when=FIRST_COMPLETED)
    print(f"First completed: {done.pop().result()}")
    
    # Wait for all to complete
    done, not_done = wait(futures, return_when=ALL_COMPLETED)
    print(f"All done: {[f.result() for f in done]}")
```

---

## Error Handling

### Per-Task Exception Handling

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def risky_task(x):
    if x == 5:
        raise ValueError(f"Cannot process {x}")
    return x ** 2

with ThreadPoolExecutor() as executor:
    futures = {executor.submit(risky_task, i): i for i in range(10)}
    
    results = []
    errors = []
    
    for future in as_completed(futures):
        task_id = futures[future]
        try:
            result = future.result()
            results.append((task_id, result))
        except Exception as e:
            errors.append((task_id, str(e)))
    
    print(f"Successes: {len(results)}")
    print(f"Failures: {errors}")
```

### Graceful Degradation

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_with_fallback(url):
    try:
        return fetch(url)
    except Exception:
        return fetch_from_cache(url)

with ThreadPoolExecutor() as executor:
    results = list(executor.map(fetch_with_fallback, urls))
```

---

## Practical Examples

### Web Scraping

```python
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    """Fetch and parse a webpage."""
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title')
    return {
        'url': url,
        'title': title.text if title else 'No title',
        'links': len(soup.find_all('a'))
    }

urls = [
    "https://example.com",
    "https://python.org",
    "https://github.com",
]

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(scrape_page, urls))

for r in results:
    print(f"{r['url']}: {r['title']} ({r['links']} links)")
```

### Bulk API Requests

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

def fetch_user(user_id):
    """Fetch user data from API."""
    response = requests.get(
        f"https://api.example.com/users/{user_id}",
        timeout=5
    )
    return response.json()

user_ids = range(1, 101)

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = {executor.submit(fetch_user, uid): uid for uid in user_ids}
    
    users = []
    for future in as_completed(futures):
        uid = futures[future]
        try:
            user = future.result()
            users.append(user)
        except Exception as e:
            print(f"Failed to fetch user {uid}: {e}")

print(f"Fetched {len(users)} users")
```

### File I/O

```python
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def read_file(filepath):
    """Read and return file contents."""
    return Path(filepath).read_text()

def process_file(filepath):
    """Read, process, and return result."""
    content = Path(filepath).read_text()
    return {
        'path': str(filepath),
        'lines': len(content.splitlines()),
        'chars': len(content)
    }

files = list(Path('.').glob('*.py'))

with ThreadPoolExecutor(max_workers=10) as executor:
    stats = list(executor.map(process_file, files))

for s in stats:
    print(f"{s['path']}: {s['lines']} lines, {s['chars']} chars")
```

### Database Operations

```python
from concurrent.futures import ThreadPoolExecutor
import threading

# Thread-local database connection
_local = threading.local()

def init_db_connection(connection_string):
    """Initialize database connection for each thread."""
    _local.conn = create_connection(connection_string)

def query_db(sql):
    """Execute query using thread's connection."""
    cursor = _local.conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

queries = [
    "SELECT * FROM users LIMIT 100",
    "SELECT * FROM orders LIMIT 100",
    "SELECT * FROM products LIMIT 100",
]

with ThreadPoolExecutor(
    max_workers=3,
    initializer=init_db_connection,
    initargs=("postgresql://localhost/mydb",)
) as executor:
    results = list(executor.map(query_db, queries))
```

---

## Best Practices

### 1. Choose Appropriate Worker Count

```python
# I/O-bound: more workers than CPUs
# Network requests, file I/O
executor = ThreadPoolExecutor(max_workers=20)

# Mixed workload: moderate count
executor = ThreadPoolExecutor(max_workers=10)

# Default is often reasonable
executor = ThreadPoolExecutor()  # min(32, cpu_count + 4)
```

### 2. Use Context Manager

```python
# Good: automatic cleanup
with ThreadPoolExecutor() as executor:
    results = executor.map(func, data)

# Avoid: manual management
executor = ThreadPoolExecutor()
try:
    results = executor.map(func, data)
finally:
    executor.shutdown()
```

### 3. Handle Timeouts

```python
from concurrent.futures import ThreadPoolExecutor, TimeoutError

with ThreadPoolExecutor() as executor:
    future = executor.submit(potentially_slow_task)
    try:
        result = future.result(timeout=30)
    except TimeoutError:
        print("Task timed out")
```

### 4. Don't Use for CPU-Bound Tasks

```python
# Bad: GIL prevents parallelism
with ThreadPoolExecutor() as executor:
    results = executor.map(cpu_intensive_task, data)  # No speedup!

# Good: Use ProcessPoolExecutor for CPU-bound
with ProcessPoolExecutor() as executor:
    results = executor.map(cpu_intensive_task, data)
```

---

## Key Takeaways

- Use `ThreadPoolExecutor` for **I/O-bound tasks** (network, files, databases)
- GIL is released during I/O, allowing true concurrency
- `map()` for same function applied to many inputs
- `submit()` for individual tasks with Future objects
- `as_completed()` to process results as they finish
- Set `max_workers` based on workload (10-50 for I/O)
- Use initializer for per-thread setup (connections)
- Always use context manager for automatic cleanup
- **Not suitable for CPU-bound tasks** — use `ProcessPoolExecutor` instead
