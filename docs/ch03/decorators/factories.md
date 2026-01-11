# Decorator Factories

## Parameterized Decorators

### 1. Factory Pattern

```python
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello")

greet()  # Prints Hello 3 times
```

## Multiple Parameters

### 1. Configuration

```python
def log(level="INFO", prefix=""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}] {prefix}{func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log(level="DEBUG", prefix=">> ")
def process():
    pass
```

## Summary

- Factory returns decorator
- Enables parameters
- Three-level nesting
- Flexible configuration
