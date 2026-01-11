# functools.wraps

## Problem

### 1. Lost Metadata

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet():
    '''Say hello'''
    pass

print(greet.__name__)  # 'wrapper' - lost!
print(greet.__doc__)   # None - lost!
```

## Solution

### 1. Use @wraps

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet():
    '''Say hello'''
    pass

print(greet.__name__)  # 'greet' - preserved!
print(greet.__doc__)   # 'Say hello' - preserved!
```

## What It Preserves

### 1. Attributes

- __name__
- __doc__
- __module__
- __annotations__
- __qualname__

## Summary

- Always use @wraps
- Preserves metadata
- Standard practice
- Helps debugging
