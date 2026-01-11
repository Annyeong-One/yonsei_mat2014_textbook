# Practical Applications

## Decorators

### 1. With State

```python
def counter(func):
    count = 0
    def wrapper(*args):
        nonlocal count
        count += 1
        print(f"Call {count}")
        return func(*args)
    return wrapper
```

## Factory Functions

### 1. Configuration

```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
```

## Summary

- Decorators
- Factories
- Callbacks
- State management
