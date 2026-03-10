# Partial Application


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## functools.partial

### 1. Fix Arguments

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))    # 125
```

## Use Cases

### 1. Configure Functions

```python
from functools import partial

def greet(greeting, name):
    return f"{greeting}, {name}!"

say_hello = partial(greet, "Hello")
say_hi = partial(greet, "Hi")

print(say_hello("Alice"))  # Hello, Alice!
print(say_hi("Bob"))       # Hi, Bob!
```

### 2. Callbacks

```python
def log(level, message):
    print(f"[{level}] {message}")

info = partial(log, "INFO")
error = partial(log, "ERROR")

info("Starting")   # [INFO] Starting
error("Failed")    # [ERROR] Failed
```

## Summary

- Fix some arguments
- Create specialized functions
- Useful for callbacks
- Built-in with functools
