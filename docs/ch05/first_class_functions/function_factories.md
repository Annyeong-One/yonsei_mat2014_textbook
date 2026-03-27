# Function Factories

A function factory is a function that creates and returns another function. This pattern leverages closures to generate specialized functions dynamically.

## Basic Pattern

A function factory returns an inner function that captures variables from the enclosing scope:

```python
def make_multiplier(n: int):  # returns a function: int -> int
    def multiply(x: int) -> int:
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

Each call to `make_multiplier` creates a new function with its own captured value of `n`.

## How Closures Work

The inner function `multiply` remembers the value of `n` even after `make_multiplier` has finished executing. This combination of a function and the variables it captures from its enclosing scope is called a **closure**.

```python
def make_adder(n: int):  # returns a function: int -> int
    def add(x: int) -> int:
        return x + n
    return add

add_10 = make_adder(10)
add_100 = make_adder(100)

print(add_10(5))    # 15
print(add_100(5))   # 105
```

`add_10` and `add_100` are independent closures — each holds its own copy of `n`.

## Practical Examples

### Validators

```python
def make_range_validator(min_val: float, max_val: float):  # returns a function: float -> bool
    def validate(x: float) -> bool:
        return min_val <= x <= max_val
    return validate

valid_percentage = make_range_validator(0, 100)
valid_age = make_range_validator(0, 150)

print(valid_percentage(50))   # True
print(valid_percentage(150))  # False
print(valid_age(25))          # True
```

### Greeting Functions

```python
def make_greeter(greeting: str):  # returns a function: str -> str
    def greet(name: str) -> str:
        return f"{greeting}, {name}!"
    return greet

say_hello = make_greeter("Hello")
say_hi = make_greeter("Hi")

print(say_hello("Alice"))  # Hello, Alice!
print(say_hi("Bob"))       # Hi, Bob!
```

### Formatters

```python
def make_formatter(prefix: str, suffix: str = ""):  # returns a function: value -> str
    def format_value(value) -> str:
        return f"{prefix}{value}{suffix}"
    return format_value

format_currency = make_formatter("\$", " USD")
format_percent = make_formatter("", "%")

print(format_currency(100))   # $100 USD
print(format_percent(85.5))   # 85.5%
```

### Power Functions

```python
def make_power(exp: int):  # returns a function: float -> float
    def power(base: float) -> float:
        return base ** exp
    return power

square = make_power(2)
cube = make_power(3)

print(square(4))  # 16
print(cube(4))    # 64
```

## Modifying Captured Variables with nonlocal

A closure can read captured variables freely, but to **modify** them it needs the `nonlocal` keyword. Without `nonlocal`, an assignment inside the inner function would create a new local variable instead of updating the captured one.

```python
def make_counter(start: int = 0, step: int = 1):  # returns a function: () -> int
    count = start
    def counter() -> int:
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

## Late Binding in Loops

Creating closures inside a loop is a common source of bugs. Because closures capture variables **by reference** (not by value), all the closures share the same variable — and see its final value after the loop ends.

```python
# Bug: all functions capture the same variable i
funcs = []
for i in range(3):
    funcs.append(lambda x: x + i)

print(funcs[0](10))  # 12 (not 10!)
print(funcs[1](10))  # 12 (not 11!)

# Fix: capture the current value with a default parameter
funcs = []
for i in range(3):
    funcs.append(lambda x, i=i: x + i)

print(funcs[0](10))  # 10
print(funcs[1](10))  # 11
```

## Key Ideas

Function factories produce specialized functions from a common template. The inner function captures variables from the enclosing scope, forming a closure that remembers those values across calls. This is useful whenever you need a family of related functions that differ only in their configuration — validators, formatters, converters, and similar patterns.

When the inner function needs to *modify* a captured variable (not just read it), use `nonlocal`. When your factory grows complex enough to need multiple methods or shared mutable state, consider using a class instead.

For more on the decorator pattern — a close relative of function factories — see the decorators chapter.
