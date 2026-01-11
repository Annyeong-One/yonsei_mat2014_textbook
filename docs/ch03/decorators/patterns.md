# Decorator Patterns

## Timing

### 1. Measure Execution

```python
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end-start:.4f}s")
        return result
    return wrapper
```

## Memoization

### 1. Cache Results

```python
def memoize(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper
```

## Validation

### 1. Check Arguments

```python
def validate_positive(func):
    @wraps(func)
    def wrapper(x):
        if x <= 0:
            raise ValueError("Must be positive")
        return func(x)
    return wrapper
```

## Summary

- Timing execution
- Caching results
- Validation
- Many patterns
