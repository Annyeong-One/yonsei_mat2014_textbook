# Practical Decorators

Common real-world decorator patterns for timing, tracing, and debugging.


## Timing Decorator

Measure function execution time without modifying the original code.

### 1. Basic Timer

```python
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start) * 1000:.2f} ms")
        return result
    return wrapper

@time_it
def slow_function():
    time.sleep(0.5)
    return "done"

slow_function()  # slow_function took 500.12 ms
```

### 2. Comparing Functions

```python
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start) * 1000:.2f} ms")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    return [n * n for n in numbers]

@time_it
def calc_cube(numbers):
    return [n * n * n for n in numbers]

data = range(1, 100000)
calc_square(data)
calc_cube(data)
```

Output:
```
calc_square took 12.34 ms
calc_cube took 15.67 ms
```


## Trace Decorator

Visualize recursive function calls with indentation.

### 1. Basic Trace

```python
def trace(func):
    func.indent = 0
    def wrapper(*args):
        print('|  ' * func.indent + '|--', func.__name__, args)
        func.indent += 1
        result = func(*args)
        print('|  ' * func.indent + '|--', 'return', repr(result))
        func.indent -= 1
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
|-- factorial (4,)
|  |-- factorial (3,)
|  |  |-- factorial (2,)
|  |  |  |-- factorial (1,)
|  |  |  |  |-- return 1
|  |  |  |-- return 2
|  |  |-- return 6
|  |-- return 24
```

### 2. Tracing Power Function

```python
@trace
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

power(2, 4)
```

### 3. Fast Power with Trace

```python
@trace
def fast_power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_power(x * x, n // 2)
    else:
        return x * fast_power(x, n - 1)

fast_power(2, 10)  # Only 5 calls instead of 10
```


## Logger Decorator

Log function calls with arguments and return values.

```python
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"  returned: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
```

Output:
```
Calling add
  args: (3, 5)
  kwargs: {}
  returned: 8
```


## Retry Decorator

Automatically retry failed operations.

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    print(f"Attempt {attempts} failed: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unstable_api_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network error")
    return "Success"
```


## Memoization Decorator

Cache function results for repeated calls.

```python
def memoize(func):
    cache = {}
    def wrapper(x):
        if x not in cache:
            cache[x] = func(x)
        return cache[x]
    return wrapper

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))  # Fast due to caching
```

Or use the built-in `@lru_cache`:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```


## Validation Decorator

Validate function arguments.

```python
from functools import wraps

def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Arguments must be positive, got {arg}")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5

print(square_root(16))   # 4.0
print(square_root(-1))   # ValueError
```


## Summary

| Decorator | Purpose |
|-----------|---------|
| `@time_it` | Measure execution time |
| `@trace` | Visualize recursive calls |
| `@logger` | Log function calls |
| `@retry` | Retry failed operations |
| `@memoize` | Cache results |
| `@validate` | Validate arguments |

Practical decorators keep original functions clean while adding cross-cutting concerns.
