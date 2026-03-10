# Practical Decorator Patterns


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Common real-world decorator patterns for timing, caching, validation, and more.

## Timing Decorator

Measure function execution time without modifying the original code.

```python
import time
from functools import wraps

def timer(func):
    """Measure and print execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.5)
    return "done"

slow_function()  # slow_function took 0.5012 seconds
```

### Comparing Algorithms

```python
@timer
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

@timer
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

data = list(range(1000, 0, -1))
bubble_sort(data)  # bubble_sort took 0.0892 seconds
quick_sort(data)   # quick_sort took 0.0023 seconds
```

---

## Trace Decorator

Visualize recursive function calls with indentation.

```python
def trace(func):
    """Trace recursive function calls."""
    trace.depth = 0
    
    @wraps(func)
    def wrapper(*args):
        indent = '│  ' * trace.depth
        print(f"{indent}├─ {func.__name__}{args}")
        trace.depth += 1
        result = func(*args)
        trace.depth -= 1
        print(f"{indent}├─ return {result}")
        return result
    return wrapper

@trace
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

factorial(4)
```

Output:
```
├─ factorial(4,)
│  ├─ factorial(3,)
│  │  ├─ factorial(2,)
│  │  │  ├─ factorial(1,)
│  │  │  ├─ return 1
│  │  ├─ return 2
│  ├─ return 6
├─ return 24
```

---

## Logger Decorator

Log function calls with arguments and return values.

```python
from functools import wraps
import logging

logging.basicConfig(level=logging.DEBUG)

def logger(func):
    """Log function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug(f"Calling {func.__name__}")
        logging.debug(f"  args: {args}")
        logging.debug(f"  kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.debug(f"  returned: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
```

---

## Memoization (Caching)

Cache function results for repeated calls.

### Simple Memoization

```python
def memoize(func):
    """Cache function results."""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))  # Fast due to caching
```

### Using Built-in `lru_cache`

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))
print(fibonacci.cache_info())  # CacheInfo(hits=98, misses=101, ...)
```

---

## Retry Decorator

Automatically retry failed operations.

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1.0, exceptions=(Exception,)):
    """Retry failed function calls."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts:
                        print(f"Attempt {attempt} failed: {e}. Retrying...")
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5, exceptions=(ConnectionError,))
def fetch_data(url):
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network error")
    return "Data"
```

---

## Validation Decorator

Validate function arguments.

### Type Validation

```python
from functools import wraps

def validate_types(*types):
    """Validate argument types."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg, expected in zip(args, types):
                if not isinstance(arg, expected):
                    raise TypeError(
                        f"Expected {expected.__name__}, got {type(arg).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(int, int)
def add(a, b):
    return a + b

add(2, 3)      # Works: 5
add("2", 3)    # TypeError
```

### Range Validation

```python
def validate_range(min_val=None, max_val=None):
    """Validate numeric arguments are within range."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if isinstance(arg, (int, float)):
                    if min_val is not None and arg < min_val:
                        raise ValueError(f"Value {arg} below minimum {min_val}")
                    if max_val is not None and arg > max_val:
                        raise ValueError(f"Value {arg} above maximum {max_val}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_range(min_val=0, max_val=100)
def set_percentage(value):
    return value

set_percentage(50)   # Works
set_percentage(150)  # ValueError
```

---

## Rate Limiting

Limit how often a function can be called.

```python
import time
from functools import wraps

def rate_limit(calls_per_second=1):
    """Limit function call rate."""
    min_interval = 1.0 / calls_per_second
    last_call = [0.0]  # Mutable container for closure
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_call[0]
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            last_call[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(calls_per_second=2)
def api_call():
    print(f"Called at {time.time():.2f}")

# Will be limited to 2 calls per second
for _ in range(5):
    api_call()
```

---

## Deprecation Warning

Warn when deprecated functions are used.

```python
import warnings
from functools import wraps

def deprecated(message=""):
    """Mark a function as deprecated."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(
                f"{func.__name__} is deprecated. {message}",
                DeprecationWarning,
                stacklevel=2
            )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@deprecated("Use new_function() instead")
def old_function():
    return "old"

old_function()  # DeprecationWarning: old_function is deprecated. Use new_function() instead
```

---

## Summary

| Decorator | Purpose | Key Feature |
|-----------|---------|-------------|
| `@timer` | Measure execution time | Performance profiling |
| `@trace` | Visualize call stack | Debugging recursion |
| `@logger` | Log function calls | Debugging, audit trail |
| `@memoize` | Cache results | Performance optimization |
| `@retry` | Retry on failure | Resilience |
| `@validate` | Validate arguments | Input safety |
| `@rate_limit` | Limit call frequency | API protection |
| `@deprecated` | Warn about old functions | Migration support |

**Key Benefits**:
- Keep original functions clean
- Reusable across many functions
- Easy to enable/disable
- Separate concerns (single responsibility)
