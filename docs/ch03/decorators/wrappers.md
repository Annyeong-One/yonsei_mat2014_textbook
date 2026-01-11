# Wrappers

## Basic Wrapper

### 1. Pattern

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Before logic
        result = func(*args, **kwargs)
        # After logic
        return result
    return wrapper
```

## Preserving Metadata

### 1. functools.wraps

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## State in Wrappers

### 1. Closure State

```python
def count_calls(func):
    count = 0
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Call {count}")
        return func(*args, **kwargs)
    
    return wrapper
```

## Summary

- Wrapper pattern common
- Use @wraps for metadata
- Can maintain state
- Flexible pattern
