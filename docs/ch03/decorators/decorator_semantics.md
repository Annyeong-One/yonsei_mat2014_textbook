# Decorator Semantics

## Basic Syntax

### 1. Decoration

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@decorator
def greet():
    print("Hello")

# Equivalent to:
# greet = decorator(greet)
```

## Execution Time

### 1. At Definition

```python
def decorator(func):
    print(f"Decorating {func.__name__}")
    return func

@decorator  # Prints immediately
def function():
    pass
```

## Multiple Decorators

### 1. Stack Order

```python
@decorator1
@decorator2
@decorator3
def function():
    pass

# Equivalent to:
# function = decorator1(decorator2(decorator3(function)))
```

## Summary

- Syntactic sugar for wrapper
- Executed at definition time
- Bottom-up application
- Returns modified function
