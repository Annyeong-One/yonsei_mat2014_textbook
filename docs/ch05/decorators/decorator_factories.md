# Decorator Factories


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Decorator factories create parameterized decorators, allowing you to customize decorator behavior.

## Basic Factory Pattern

A decorator factory is a function that returns a decorator:

```python
from functools import wraps

def repeat(times):
    """Decorator factory that repeats function execution."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello")

greet()  # Prints "Hello" 3 times
```

### Three Levels of Nesting

```python
def factory(param):           # Level 1: Factory (accepts parameters)
    def decorator(func):      # Level 2: Decorator (accepts function)
        @wraps(func)
        def wrapper(*args):   # Level 3: Wrapper (accepts call arguments)
            # Use param, func, and args
            return func(*args)
        return wrapper
    return decorator
```

---

## Multiple Parameters

### Configuration Decorator

```python
from functools import wraps

def log(level="INFO", prefix=""):
    """Configurable logging decorator."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}] {prefix}{func.__name__} called")
            result = func(*args, **kwargs)
            print(f"[{level}] {prefix}{func.__name__} returned {result}")
            return result
        return wrapper
    return decorator

@log(level="DEBUG", prefix=">> ")
def add(a, b):
    return a + b

add(2, 3)
# [DEBUG] >> add called
# [DEBUG] >> add returned 5
```

### Retry with Configuration

```python
from functools import wraps
import time

def retry(max_attempts=3, delay=1.0, exceptions=(Exception,)):
    """Retry decorator with configurable attempts and delay."""
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
                        print(f"Attempt {attempt} failed, retrying in {delay}s...")
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5, exceptions=(ConnectionError,))
def fetch_data():
    # May fail occasionally
    pass
```

---

## Preserving Metadata with `functools.wraps`

### The Problem

Without `@wraps`, the wrapper replaces the original function's metadata:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet():
    """Say hello."""
    pass

print(greet.__name__)  # 'wrapper' — Lost!
print(greet.__doc__)   # None — Lost!
```

### The Solution

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet():
    """Say hello."""
    pass

print(greet.__name__)  # 'greet' — Preserved!
print(greet.__doc__)   # 'Say hello.' — Preserved!
```

### What `@wraps` Preserves

| Attribute | Description |
|-----------|-------------|
| `__name__` | Function name |
| `__doc__` | Docstring |
| `__module__` | Module where defined |
| `__annotations__` | Type hints |
| `__qualname__` | Qualified name |
| `__dict__` | Function attributes |
| `__wrapped__` | Reference to original function |

### Accessing the Original Function

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet():
    """Say hello."""
    print("Hello")

# Access the original unwrapped function
original = greet.__wrapped__
```

---

## Optional Parameters Pattern

Create decorators that work with or without parentheses:

```python
from functools import wraps

def log(func=None, *, level="INFO"):
    """Decorator that works with or without arguments."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"[{level}] Calling {fn.__name__}")
            return fn(*args, **kwargs)
        return wrapper
    
    if func is not None:
        # Called without arguments: @log
        return decorator(func)
    # Called with arguments: @log(level="DEBUG")
    return decorator

# Both work:
@log
def func1():
    pass

@log(level="DEBUG")
def func2():
    pass
```

---

## Factory with Validation

```python
from functools import wraps

def validate_types(*types):
    """Validate argument types."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Expected {expected_type.__name__}, got {type(arg).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(int, int)
def add(a, b):
    return a + b

add(2, 3)       # Works: 5
add("2", 3)     # TypeError: Expected int, got str
```

---

## Summary

| Concept | Description |
|---------|-------------|
| Decorator factory | Function that returns a decorator |
| Three levels | Factory → Decorator → Wrapper |
| `@wraps(func)` | Preserves original function metadata |
| Optional params | Support both `@deco` and `@deco()` |

**Best Practices**:
- Always use `@wraps(func)` in wrappers
- Use keyword-only arguments for clarity
- Document factory parameters
- Consider optional parameter pattern for flexibility
