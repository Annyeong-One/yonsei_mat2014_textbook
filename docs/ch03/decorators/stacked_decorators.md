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
```

This is equivalent to:

```python
func = decorator_a(decorator_b(decorator_c(func)))
```

**Application order**: `decorator_c` → `decorator_b` → `decorator_a`

**Execution order**: `decorator_a` wrapper runs first


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


## Visualizing the Stack

```python
def decorator_a(func):
    def wrapper(*args):
        print("A: before")
        result = func(*args)
        print("A: after")
        return result
    return wrapper

def decorator_b(func):
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

# Auth check happens before logging
user = {'name': 'Alice', 'authenticated': True}
get_secret_data(user)
# [ACCESS] Alice called get_secret_data
```


## Common Stacking Patterns

| Outer | Inner | Use Case |
|-------|-------|----------|
| `@logger` | `@timer` | Log includes timing |
| `@timer` | `@logger` | Time includes logging overhead |
| `@cache` | `@validate` | Validate before caching |
| `@auth` | `@log` | Log only authenticated calls |
| `@retry` | `@timeout` | Retry timeouts |


## Summary

- Decorators apply **bottom-up**: inner decorator wraps function first
- Decorators execute **top-down**: outer wrapper runs first
- Order affects both behavior and what gets measured/logged
- Use `@wraps(func)` to preserve metadata through the stack
