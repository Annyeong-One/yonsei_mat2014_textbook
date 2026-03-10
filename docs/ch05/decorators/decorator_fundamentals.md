# Decorator Fundamentals


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

A decorator is a function that takes another function as input and returns a modified version of it. Decorators provide a clean syntax for wrapping functions with additional behavior.

## Basic Syntax

### The `@` Syntax

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

The `@decorator` syntax is syntactic sugar—it automatically passes the function to the decorator and reassigns the result.

### Calling Decorated Functions

```python
greet()
# Output:
# Before
# Hello
# After
```

---

## The Wrapper Pattern

### Basic Structure

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Before logic (pre-processing)
        result = func(*args, **kwargs)
        # After logic (post-processing)
        return result
    return wrapper
```

**Key elements**:
- `func`: The original function being decorated
- `wrapper`: The new function that wraps the original
- `*args, **kwargs`: Accepts any arguments to pass through
- `return result`: Preserves the original return value

### Why `*args, **kwargs`?

```python
def decorator(func):
    def wrapper(*args, **kwargs):  # Accept ANY arguments
        return func(*args, **kwargs)  # Pass them through
    return wrapper

@decorator
def add(a, b):
    return a + b

@decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Both work with the same decorator
add(2, 3)           # 5
greet("Alice")      # "Hello, Alice!"
```

---

## Execution Time

### Decorators Run at Definition Time

```python
def decorator(func):
    print(f"Decorating {func.__name__}")  # Runs immediately!
    return func

@decorator  # Prints "Decorating function" when this line executes
def function():
    pass

# The decorator has already run before we call function()
```

This is important: the decorator itself runs when Python loads the module, not when you call the decorated function.

---

## Preserving Function Metadata

### The Problem

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet():
    """Say hello."""
    print("Hello")

print(greet.__name__)  # 'wrapper' — Wrong!
print(greet.__doc__)   # None — Lost!
```

### The Solution: `functools.wraps`

```python
from functools import wraps

def decorator(func):
    @wraps(func)  # Copies metadata from func to wrapper
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet():
    """Say hello."""
    print("Hello")

print(greet.__name__)  # 'greet' — Correct!
print(greet.__doc__)   # 'Say hello.' — Preserved!
```

**Always use `@wraps`**—it preserves:
- `__name__`: Function name
- `__doc__`: Docstring
- `__module__`: Module name
- `__annotations__`: Type hints
- `__dict__`: Function attributes

---

## State in Decorators

### Using Closure Variables

```python
from functools import wraps

def count_calls(func):
    count = 0
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Call #{count}")
        return func(*args, **kwargs)
    
    return wrapper

@count_calls
def greet():
    print("Hello")

greet()  # Call #1, Hello
greet()  # Call #2, Hello
```

### Using Function Attributes

```python
from functools import wraps

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    
    wrapper.calls = 0
    return wrapper

@count_calls
def greet():
    print("Hello")

greet()
greet()
print(greet.calls)  # 2 — Accessible from outside
```

---

## Closures vs Decorators

### Closure

A function that **retains access to variables** from its enclosing scope:

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor  # 'factor' captured from enclosing scope
    return multiply

times3 = make_multiplier(3)
print(times3(10))  # 30
```

### Decorator

A function that **takes another function as input** and **returns a new function**:

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

### Relationship

**Decorators are built on closures.** The `wrapper` function inside a decorator is a closure—it captures `func` from the enclosing scope.

### Comparison

| Feature | Closure | Decorator |
|---------|---------|-----------|
| **Purpose** | Retain state from outer function | Modify/enhance function behavior |
| **Returns** | A nested function | A new function wrapping the original |
| **Captures** | Variables from enclosing scope | The decorated function |
| **Used for** | Function factories, stateful functions | Logging, timing, caching, validation |

### When to Use Each

**Closures** for function factories:

```python
def make_power(exp):
    def power(base):
        return base ** exp
    return power

square = make_power(2)
cube = make_power(3)
```

**Decorators** for cross-cutting concerns:

```python
@timer
def slow_function():
    ...

@cache
def expensive_computation(x):
    ...
```

---

## Common Decorator Template

```python
from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # === BEFORE the original function ===
        # Pre-processing, validation, logging, etc.
        
        # === CALL the original function ===
        result = func(*args, **kwargs)
        
        # === AFTER the original function ===
        # Post-processing, cleanup, etc.
        
        return result
    return wrapper
```

---

## Summary

| Concept | Description |
|---------|-------------|
| `@decorator` | Syntactic sugar for `func = decorator(func)` |
| Wrapper pattern | Inner function that wraps the original |
| `*args, **kwargs` | Accept and pass through any arguments |
| `@wraps(func)` | Preserve original function's metadata |
| Execution time | Decorator runs at definition, wrapper runs at call |
| Closure | Function + captured environment |

**Key Takeaways**:
- Decorators are functions that transform functions
- Always use `@wraps` to preserve metadata
- The wrapper pattern is the foundation of most decorators
- Decorators run at definition time, not call time
- Decorators use closures internally
