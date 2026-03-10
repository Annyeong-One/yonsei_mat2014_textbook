# Function Factories


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

A function factory is a function that creates and returns another function. This pattern leverages closures to generate specialized functions dynamically.


## Basic Pattern

A function factory returns an inner function that captures variables from the enclosing scope.

```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

The inner function `multiply` captures `n` from the enclosing scope, creating a closure.


## How It Works

```python
def make_adder(n):
    def add(x):
        return x + n
    return add

add_10 = make_adder(10)
add_100 = make_adder(100)

print(add_10(5))    # 15
print(add_100(5))   # 105
```

Each call to `make_adder` creates a new closure with its own captured value of `n`.


## Inspecting Closures

Use `__closure__` to examine captured variables.

```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)

print(double.__closure__)           # (<cell object>,)
print(double.__closure__[0].cell_contents)  # 2
```


## Practical Examples

### 1. Power Functions

```python
def make_power(exp):
    def power(base):
        return base ** exp
    return power

square = make_power(2)
cube = make_power(3)

print(square(4))  # 16
print(cube(4))    # 64
```

### 2. Greeting Functions

```python
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

say_hello = make_greeter("Hello")
say_hi = make_greeter("Hi")

print(say_hello("Alice"))  # Hello, Alice!
print(say_hi("Bob"))       # Hi, Bob!
```

### 3. Validators

```python
def make_range_validator(min_val, max_val):
    def validate(x):
        return min_val <= x <= max_val
    return validate

valid_percentage = make_range_validator(0, 100)
valid_age = make_range_validator(0, 150)

print(valid_percentage(50))   # True
print(valid_percentage(150))  # False
print(valid_age(25))          # True
```

### 4. Formatters

```python
def make_formatter(prefix, suffix=""):
    def format_value(value):
        return f"{prefix}{value}{suffix}"
    return format_value

format_currency = make_formatter("$", " USD")
format_percent = make_formatter("", "%")

print(format_currency(100))   # \$100 USD
print(format_percent(85.5))   # 85.5%
```


## Function Wrappers

Function factories can wrap existing functions to add behavior.

```python
def make_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned {result}")
        return result
    return wrapper

def add(a, b):
    return a + b

logged_add = make_logger(add)
logged_add(3, 5)
# Calling add
# Returned 8
```

This pattern is the foundation for **decorators**.


## With Default Parameters

Combine closures with default parameters for flexible factories.

```python
def make_counter(start=0, step=1):
    count = start
    def counter():
        nonlocal count
        current = count
        count += step
        return current
    return counter

counter = make_counter()
print(counter())  # 0
print(counter())  # 1
print(counter())  # 2

by_tens = make_counter(start=10, step=10)
print(by_tens())  # 10
print(by_tens())  # 20
```


## Factory vs Class

Function factories can replace simple classes.

```python
# Class approach
class Multiplier:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return x * self.n

double = Multiplier(2)
print(double(5))  # 10

# Factory approach (simpler for this case)
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
print(double(5))  # 10
```

Use factories when:
- Logic is simple (one function)
- No need for multiple methods
- No need for mutable state access


## Common Pitfalls

### Late Binding in Loops

```python
# Wrong: all functions capture final value of i
funcs = []
for i in range(3):
    funcs.append(lambda x: x + i)

print(funcs[0](10))  # 12 (not 10!)
print(funcs[1](10))  # 12 (not 11!)

# Fix: capture value with default parameter
funcs = []
for i in range(3):
    funcs.append(lambda x, i=i: x + i)

print(funcs[0](10))  # 10
print(funcs[1](10))  # 11
```


## Summary

- Function factories create specialized functions dynamically
- Inner functions capture variables via closures
- Use `__closure__` to inspect captured values
- Foundation for decorators and wrappers
- Simpler than classes for single-function behavior
- Watch for late binding issues in loops
