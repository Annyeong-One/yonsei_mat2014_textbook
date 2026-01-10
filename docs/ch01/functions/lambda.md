# Lambda Expressions

## Introduction

**Lambda expressions** (or lambda functions) are small, anonymous functions defined using the `lambda` keyword. They provide a concise way to create simple functions without the formal `def` statement.

Lambda functions are particularly useful when you need a simple function for a short period of time, typically as an argument to higher-order functions like `map()`, `filter()`, and `sorted()`.

## Basic Syntax

### 1. Lambda vs Regular

```python
# Regular function
def add(x, y):
    return x + y

# Equivalent lambda
add_lambda = lambda x, y: x + y

print(add(3, 5))        # 8
print(add_lambda(3, 5)) # 8
```

**Syntax**:
```python
lambda parameters: expression
```

- **lambda**: Keyword indicating lambda function
- **parameters**: Function parameters (can be zero or more)
- **expression**: Single expression that is evaluated and returned
- **No return statement**: Result is automatically returned

### 1. Key

1. **Anonymous**: No function name required
2. **Single expression**: Can only contain one expression
3. **Implicit return**: Automatically returns the expression result
4. **Limited**: Cannot contain statements, only expressions

## Creating Lambda

### 1. No Parameters

```python
# Lambda with no
greet = lambda: "Hello, World!"
print(greet())  # Hello, World!
```

### 1. Single Parameter

```python
# Square function
square = lambda x: x ** 2
print(square(5))  # 25

# Check if even
is_even = lambda n: n % 2 == 0
print(is_even(4))  # True
print(is_even(7))  # False
```

### 1. Multiple

```python
# Addition
add = lambda x, y: x + y
print(add(3, 5))  # 8

# Three parameters
multiply_three = lambda a, b, c: a * b * c
print(multiply_three(2, 3, 4))  # 24
```

### 1. Default

```python
# Lambda with default
power = lambda x, n=2: x ** n
print(power(5))     # 25 (default n=2)
print(power(5, 3))  # 125
```

## Common Use Cases

### 1. With map()

Apply function to every item in iterable:

```python
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Convert to strings
strings = list(map(lambda x: str(x), numbers))
print(strings)  # ['1', '2', '3', '4', '5']

# Multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, numbers1, numbers2))
print(sums)  # [5, 7, 9]
```

### 1. With filter()

Filter items based on condition:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Get numbers > 5
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)  # [6, 7, 8, 9, 10]

# Filter strings by
words = ["cat", "elephant", "dog", "butterfly"]
short_words = list(filter(lambda w: len(w) <= 3, words))
print(short_words)  # ['cat', 'dog']
```

### 1. With sorted()

Custom sorting:

```python
# Sort by absolute
numbers = [-5, -2, 1, 3, -4]
sorted_nums = sorted(numbers, key=lambda x: abs(x))
print(sorted_nums)  # [1, -2, 3, -4, -5]

# Sort strings by
words = ["python", "is", "awesome"]
by_length = sorted(words, key=lambda w: len(w))
print(by_length)  # ['is', 'python', 'awesome']

# Sort tuples by
pairs = [(1, 5), (3, 2), (2, 8)]
sorted_pairs = sorted(pairs, key=lambda p: p[1])
print(sorted_pairs)  # [(3, 2), (1, 5), (2, 8)]

# Sort dictionaries by
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20}
]
by_age = sorted(people, key=lambda p: p['age'])
print([p['name'] for p in by_age])  # ['Charlie', 'Alice', 'Bob']
```

### 1. With reduce()

Reduce sequence to single value:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Product of all
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5
```

### 1. Event Handlers

```python
# Button click
button.config(command=lambda: print("Button clicked!"))

# Timer callbacks
timer.after(1000, lambda: update_display())

# Thread execution
thread = threading.Thread(target=lambda: process_data(data))
```

## Lambda in Data

### 1. Dictionary of

```python
# Calculator using
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else None
}

print(operations['add'](10, 5))       # 15
print(operations['multiply'](10, 5))  # 50
```

### 1. List of Functions

```python
# List of
transforms = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2
]

value = 3
for transform in transforms:
    value = transform(value)
    print(value)
# Output: 4, 8, 64
```

## Advanced Lambda

### 1. Conditional

```python
# Ternary operator in
max_func = lambda a, b: a if a > b else b
print(max_func(5, 3))  # 5

# Absolute value
abs_func = lambda x: x if x >= 0 else -x
print(abs_func(-5))  # 5

# Grade assignment
get_grade = lambda score: 'A' if score >= 90 else 'B' if score >= 80 else 'C'
print(get_grade(85))  # B
```

### 1. Multiple

```python
# Execute multiple
func = lambda x: (print(f"Input: {x}"), x ** 2)[1]
result = func(5)  # Prints "Input: 5", returns 25
```

### 1. Lambda with

```python
# Default parameter
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(greet("Alice"))              # Hello, Alice!
print(greet("Bob", "Hi"))          # Hi, Bob!
```

### 1. Nested Lambdas

```python
# Lambda returning
def make_multiplier(n):
    return lambda x: x * n

times_3 = make_multiplier(3)
times_5 = make_multiplier(5)

print(times_3(10))  # 30
print(times_5(10))  # 50

# Inline nested lambda
add_and_double = lambda x, y: (lambda z: z * 2)(x + y)
print(add_and_double(3, 5))  # 16 (3+5=8, 8*2=16)
```

## Lambda with Built-in

### 1. min() and max()

```python
# Find word with
words = ["python", "is", "awesome"]
longest = max(words, key=lambda w: len(w))
print(longest)  # awesome

# Find tuple with
pairs = [(1, 5), (3, 2), (2, 8)]
min_pair = min(pairs, key=lambda p: p[1])
print(min_pair)  # (3, 2)
```

### 1. any() and all()

```python
numbers = [1, 2, 3, 4, 5]

# Check if any number
has_even = any(map(lambda x: x % 2 == 0, numbers))
print(has_even)  # True

# Check if all numbers
all_positive = all(map(lambda x: x > 0, numbers))
print(all_positive)  # True
```

## Lambda Limitations

### 1. Single Expression

```python
# Invalid - multiple
# lambda x: print(x);

# Must use regular
def process(x):
    print(x)
    return x ** 2
```

### 1. No Type Hints

```python
# Cannot add type
# lambda x: int: x + 1

# Use regular function
def add_one(x: int) -> int:
    return x + 1
```

### 1. No Docstrings

```python
# Cannot add docstring
# Regular function for
def calculate_area(length, width):
    """Calculate rectangle area."""
    return length * width
```

### 1. Harder to Debug

```python
# Lambda in traceback
nums = [1, 2, 'three', 4]
# list(map(lambda x: x

# Named function gives
def square(x):
    return x ** 2
# list(map(square,
```

### 1. Reduced

```python
# Poor - complex
result = list(filter(lambda x: x > 0 and x < 100 and x % 2 == 0 and x % 3 == 0, range(200)))

# Better - named
def is_valid_number(x):
    """Check if number is positive, < 100, even, and divisible by 3."""
    return 0 < x < 100 and x % 2 == 0 and x % 3 == 0

result = list(filter(is_valid_number, range(200)))
```

## Lambda vs Regular

### 1. When to Use

✅ **Use lambda when**:
- Function is simple (one expression)
- Function is used once or in limited scope
- Passing as argument to higher-order function
- Creating quick throwaway function
- Code is more readable with inline lambda

```python
# Good lambda usage
sorted_names = sorted(names, key=lambda n: n.lower())
doubled = list(map(lambda x: x * 2, numbers))
```

### 1. When to Use

✅ **Use `def` when**:
- Function is complex (multiple statements)
- Function is reused multiple times
- Function needs documentation
- Function needs type hints
- Debugging clarity matters
- Function name adds clarity

```python
# Good regular
def calculate_total_with_tax(price, quantity, tax_rate=0.1):
    """
    Calculate total price including tax.
    
    Args:
        price: Unit price
        quantity: Number of items
        tax_rate: Tax rate as decimal (default 0.1)
    
    Returns:
        Total price with tax
    """
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax
```

## Best Practices

### 1. Keep Lambdas

```python
# Good - simple and
double = lambda x: x * 2

# Poor - too complex
# Use regular function
complex_func = lambda x: (x ** 2 + 3 * x - 5) / (x + 1) if x != -1 else 0
```

### 1. Use Descriptive

```python
# Poor - lambda
f = lambda x: x ** 2

# Better - use
square = lambda x: x ** 2

# Best - use regular
def square(x):
    return x ** 2
```

### 1. Consider List

```python
# Lambda with map
squares = list(map(lambda x: x ** 2, numbers))

# Often better - list
squares = [x ** 2 for x in numbers]

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Often better - list
evens = [x for x in numbers if x % 2 == 0]
```

### 1. Avoid Assigning

```python
# Against PEP 8
square = lambda x: x ** 2

# PEP 8 compliant
def square(x):
    return x ** 2

# Exception: Lambda as
sorted(items, key=lambda x: x.value)
```

### 1. Use Operator

```python
from operator import add, mul, itemgetter

numbers = [1, 2, 3, 4, 5]

# Instead of:
total = reduce(add, numbers)

# Instead of:
pairs = [(1, 5), (3, 2), (2, 8)]
sorted_pairs = sorted(pairs, key=itemgetter(1))
```

## Real-World Examples

### 1. Data Processing

```python
# Process user data
users = [
    {'name': 'Alice', 'age': 25, 'active': True},
    {'name': 'Bob', 'age': 30, 'active': False},
    {'name': 'Charlie', 'age': 35, 'active': True}
]

# Get active users
active_users = list(filter(lambda u: u['active'], users))

# Get names of active
active_names = list(map(lambda u: u['name'], active_users))

# Sort by age
sorted_users = sorted(users, key=lambda u: u['age'])
```

### 1. API Response

```python
# Extract specific
api_data = [
    {'id': 1, 'name': 'Item 1', 'price': 10.99},
    {'id': 2, 'name': 'Item 2', 'price': 20.50},
    {'id': 3, 'name': 'Item 3', 'price': 15.75}
]

# Get item names
names = list(map(lambda item: item['name'], api_data))

# Get items under $20
affordable = list(filter(lambda item: item['price'] < 20, api_data))
```

### 1. GUI Event

```python
# Tkinter button
import tkinter as tk

root = tk.Tk()

# Lambda captures
for i in range(5):
    btn = tk.Button(root, text=f"Button {i}", 
                    command=lambda x=i: print(f"Clicked button {x}"))
    btn.pack()
```

### 1. DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
})

# Apply lambda to
df['age_group'] = df['age'].apply(lambda x: 'Young' if x < 30 else 'Older')

# Filter rows
young_employees = df[df['age'].apply(lambda x: x < 30)]
```

## Quick Reference

### 1. Basic Syntax
```python
lambda parameters: expression
```

### 2. Common Patterns
```python
# Single parameter
lambda x: x * 2

# Multiple parameters
lambda x, y: x + y

# No parameters
lambda: 42

# Default parameter
lambda x, n=2: x ** n

# Conditional
lambda x: 'even' if x % 2 == 0 else 'odd'
```

### 1. Common Uses
```python
# map
list(map(lambda x: x ** 2, numbers))

# filter
list(filter(lambda x: x > 0, numbers))

# sorted
sorted(items, key=lambda x: x.value)

# reduce
reduce(lambda x, y: x + y, numbers)
```

## Summary

- **Lambda functions** are anonymous, single-expression functions
- **Syntax**: `lambda parameters: expression`
- **Common with**: `map()`, `filter()`, `sorted()`, `reduce()`
- **Best for**: Simple, one-time use functions
- **Limitations**: Single expression, no statements, no docstrings
- **Alternatives**: List comprehensions often clearer
- **PEP 8**: Avoid assigning lambdas to variables
- **Use regular functions** for: Complex logic, reusable code, documentation needs
- **Operator module**: Consider for simple operations

Lambda expressions are a powerful tool for concise functional programming in Python. Use them judiciously where they improve code clarity, but don't hesitate to use regular functions when appropriate. The goal is always readable, maintainable code.
