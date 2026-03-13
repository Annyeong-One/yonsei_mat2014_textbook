# Stacked Decorators

Multiple decorators can be applied to a single function. The order of application matters.

## Basic Stacking

Decorators are applied bottom-up (inner first), but execute top-down.

```python
@decorator_a
@decorator_b
@decorator_c
def func():
    pass

# Equivalent to:
func = decorator_a(decorator_b(decorator_c(func)))
```

**Application order**: `decorator_c` → `decorator_b` → `decorator_a`

**Execution order**: `decorator_a`'s wrapper runs first

---

## Visualizing the Stack

```python
from functools import wraps

def decorator_a(func):
    @wraps(func)
    def wrapper(*args):
        print("A: before")
        result = func(*args)
        print("A: after")
        return result
    return wrapper

def decorator_b(func):
    @wraps(func)
    def wrapper(*args):
        print("B: before")
        result = func(*args)
        print("B: after")
        return result
    return wrapper

@decorator_a
@decorator_b
def greet(name):
    print(f"Hello, {name}!")
    return name

greet("Alice")
```

Output:
```
A: before
B: before
Hello, Alice!
B: after
A: after
```

The outer decorator (`decorator_a`) wraps the inner decorator (`decorator_b`), which wraps the original function.

---

## Example: Logger and Timer

```python
import time
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished {func.__name__}")
        return result
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__}: {end - start:.4f}s")
        return result
    return wrapper
```

### Order 1: Logger Outside

```python
@logger
@timer
def compute(n):
    return sum(range(n))

compute(1000000)
```

Output:
```
[LOG] Calling compute
[TIME] compute: 0.0234s
[LOG] Finished compute
```

The timing is logged as part of the function execution.

### Order 2: Timer Outside

```python
@timer
@logger
def compute(n):
    return sum(range(n))

compute(1000000)
```

Output:
```
[LOG] Calling compute
[LOG] Finished compute
[TIME] compute: 0.0234s
```

The timer includes the logging overhead.

---

## Practical Example: Auth + Logging

```python
from functools import wraps

def require_auth(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get('authenticated'):
            raise PermissionError("Authentication required")
        return func(user, *args, **kwargs)
    return wrapper

def log_access(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        print(f"[ACCESS] {user.get('name')} called {func.__name__}")
        return func(user, *args, **kwargs)
    return wrapper

@log_access
@require_auth
def get_secret_data(user):
    return "Secret: 42"

# Auth check happens first (inner), then logging (outer)
user = {'name': 'Alice', 'authenticated': True}
get_secret_data(user)
# [ACCESS] Alice called get_secret_data
```

---

## Common Stacking Patterns

| Outer | Inner | Use Case |
|-------|-------|----------|
| `@logger` | `@timer` | Log includes timing info |
| `@timer` | `@logger` | Time includes logging overhead |
| `@cache` | `@validate` | Validate before caching |
| `@log` | `@auth` | Log only authenticated calls |
| `@retry` | `@timeout` | Retry timed-out operations |

---

## Order Matters: Real Examples

### Caching with Validation

```python
@cache        # Cache validated results
@validate     # Validate first
def compute(x):
    pass
```

If reversed, invalid inputs might be cached.

### Rate Limiting with Auth

```python
@rate_limit   # Apply rate limit
@require_auth # Check auth first
def api_endpoint(user):
    pass
```

Unauthenticated requests shouldn't count against rate limit.

### Metrics with Error Handling

```python
@track_errors  # Track errors
@track_timing  # Time the operation
def process():
    pass
```

Error tracking wraps timing to catch timing-related issues.

---

## Debugging Stacked Decorators

### Check the Wrapper Chain

```python
@decorator_a
@decorator_b
def func():
    pass

# See the chain
print(func.__name__)       # Should be 'func' if @wraps used
print(func.__wrapped__)    # The next layer
print(func.__wrapped__.__wrapped__)  # Original function
```

### Temporarily Disable

```python
# Comment out decorators to isolate issues
# @decorator_a
@decorator_b
def func():
    pass
```

---

## Summary

| Aspect | Description |
|--------|-------------|
| Application | Bottom-up (inner decorator applied first) |
| Execution | Top-down (outer wrapper runs first) |
| Nesting | Each decorator wraps the previous result |
| Metadata | Use `@wraps(func)` at each level |

**Key Rules**:
- Decorators apply bottom-up, execute top-down
- Order affects both behavior and measurements
- Inner decorators are "closer" to the original function
- Always use `@wraps(func)` to preserve metadata through the stack
