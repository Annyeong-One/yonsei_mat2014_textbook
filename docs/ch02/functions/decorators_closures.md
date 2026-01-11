# Decorators & Closures

## Basic Decorator

### 1. Function Wrapper

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

greet()
# Before
# Hello
# After
```

### 2. Using Closure

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi")
```

## Decorator Closure

### 1. Captures State

```python
def counter(func):
    count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Call #{count}")
        return func(*args, **kwargs)
    
    return wrapper

@counter
def function():
    pass

function()  # Call #1
function()  # Call #2
```

## Summary

- Decorators use closures
- Wrapper captures function
- Can maintain state
- Parameterized decorators
