# Closures vs Decorators

Closures and decorators are related but distinct concepts. Understanding their relationship clarifies when to use each.


## Definitions

### Closure

A function that **retains access to variables** from its enclosing scope, even after that scope has finished executing.

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor  # 'factor' captured from enclosing scope
    return multiply

times3 = make_multiplier(3)
print(times3(10))  # 30
```

**Key idea**: Function + captured environment = closure

### Decorator

A function that **takes another function as input**, modifies or enhances it, and **returns a new function**.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b
```

**Key idea**: Function enhancer that wraps behavior


## Relationship

**Decorators are built on closures.**

The `wrapper` function inside a decorator is a closure — it captures `func` from the enclosing scope.

```python
def my_decorator(func):      # Outer function
    def wrapper(*args):       # Inner function (closure)
        print("Before")
        result = func(*args)  # 'func' is a free variable
        print("After")
        return result
    return wrapper            # Return the closure
```


## Side-by-Side Comparison

| Feature | Closure | Decorator |
|---------|---------|-----------|
| **Purpose** | Retain state from outer function | Modify/enhance function behavior |
| **Returns** | A nested function | A new function wrapping the original |
| **Captures** | Variables from enclosing scope | The decorated function |
| **Used for** | Function factories, stateful functions | Logging, timing, caching, validation |
| **Foundation** | Core concept | Built on closures |


## Use Cases

### When to Use Closures

- **Function factories**: Generate specialized functions

```python
def make_power(exp):
    def power(base):
        return base ** exp
    return power

square = make_power(2)
cube = make_power(3)
```

- **Stateful functions**: Track state across calls

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
```

### When to Use Decorators

- **Cross-cutting concerns**: Add behavior without modifying code

```python
@timer
def slow_function():
    ...

@cache
def expensive_computation(x):
    ...

@validate_input
def process_data(data):
    ...
```

- **Reusable wrappers**: Apply same enhancement to many functions

```python
@logger
def func_a(): ...

@logger
def func_b(): ...

@logger
def func_c(): ...
```


## Closure Without Decorator

Not all closures are decorators:

```python
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

say_hello = make_greeter("Hello")
say_hi = make_greeter("Hi")

print(say_hello("Alice"))  # Hello, Alice!
```

This is a closure (captures `greeting`) but not a decorator (doesn't wrap a function).


## Decorator Using Closure

All decorators use closures internally:

```python
def repeat(n):                    # Decorator factory
    def decorator(func):          # Actual decorator
        def wrapper(*args):       # Closure (captures func and n)
            for _ in range(n):
                func(*args)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()  # Prints "Hi!" three times
```

Here we have:
- `decorator` is a closure (captures `n`)
- `wrapper` is a closure (captures `func` and `n`)


## Class Alternatives

Both closures and decorators can be implemented with classes:

### Closure as Class

```python
# Closure version
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

# Class version
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

times3 = Multiplier(3)
print(times3(10))  # 30
```

### Decorator as Class

```python
# Function decorator
def logger(func):
    def wrapper(*args):
        print(f"Calling {func.__name__}")
        return func(*args)
    return wrapper

# Class decorator
class Logger:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args):
        print(f"Calling {self.func.__name__}")
        return self.func(*args)

@Logger
def add(a, b):
    return a + b
```


## Summary

| Concept | Think of it as... |
|---------|-------------------|
| **Closure** | Function + external memory |
| **Decorator** | Function wrapper/enhancer |

- **Closures** capture and retain state
- **Decorators** modify function behavior
- **Decorators use closures** internally
- Both can be replaced by classes for complex cases
