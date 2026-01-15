# Lambda Expressions

## Introduction

**Lambda expressions** (or lambda functions) are small, anonymous functions defined using the `lambda` keyword. They provide a concise way to create simple functions without the formal `def` statement.

Lambda functions are particularly useful when you need a simple function for a short period of time, typically as an argument to higher-order functions like `map()`, `filter()`, and `sorted()`.

## Basic Syntax

### Lambda vs Regular Function

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

### Key Characteristics

1. **Anonymous**: No function name required
2. **Single expression**: Can only contain one expression
3. **Implicit return**: Automatically returns the expression result
4. **Limited**: Cannot contain statements, only expressions

---

## Creating Lambda Functions

### No Parameters

```python
greet = lambda: "Hello, World!"
print(greet())  # Hello, World!
```

### Single Parameter

```python
# Square function
square = lambda x: x ** 2
print(square(5))  # 25

# Check if even
is_even = lambda n: n % 2 == 0
print(is_even(4))  # True
print(is_even(7))  # False
```

### Multiple Parameters

```python
# Addition
add = lambda x, y: x + y
print(add(3, 5))  # 8

# Three parameters
multiply_three = lambda a, b, c: a * b * c
print(multiply_three(2, 3, 4))  # 24
```

### Default Parameters

```python
power = lambda x, n=2: x ** n
print(power(5))     # 25 (default n=2)
print(power(5, 3))  # 125
```

---

## Common Use Cases

### With map()

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

### With filter()

Filter items based on condition:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Get numbers > 5
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)  # [6, 7, 8, 9, 10]

# Filter strings by length
words = ["cat", "elephant", "dog", "butterfly"]
short_words = list(filter(lambda w: len(w) <= 3, words))
print(short_words)  # ['cat', 'dog']
```

### With sorted() and list.sort()

Custom sorting with `key=` parameter:

**sorted()** returns a new sorted list:

```python
# Sort by absolute value
numbers = [-5, -2, 1, 3, -4]
sorted_nums = sorted(numbers, key=lambda x: abs(x))
print(sorted_nums)  # [1, -2, 3, -4, -5]

# Sort strings by length
words = ["python", "is", "awesome"]
by_length = sorted(words, key=lambda w: len(w))
print(by_length)  # ['is', 'python', 'awesome']

# Sort tuples by second element
pairs = [(1, 5), (3, 2), (2, 8)]
sorted_pairs = sorted(pairs, key=lambda p: p[1])
print(sorted_pairs)  # [(3, 2), (1, 5), (2, 8)]

# Sort dictionaries by value
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20}
]
by_age = sorted(people, key=lambda p: p['age'])
print([p['name'] for p in by_age])  # ['Charlie', 'Alice', 'Bob']
```

**list.sort()** sorts in-place and returns `None`:

```python
# Basic in-place sort with custom key
lst = [-1, 3, -2, 5, 6, 7, 5]
lst.sort(key=lambda x: (x+2)**2)
print(lst)  # [-2, -1, 3, 5, 5, 6, 7]

# With reverse parameter
lst = [-1, 3, -2, 5, 6, 7, 5]
lst.sort(key=lambda x: (x+2)**2, reverse=True)
print(lst)  # [7, 6, 5, 5, 3, -1, -2]

# Case-insensitive string sort
lst = ["CBA", "ABC", "abc"]
lst.sort(key=str.lower)
print(lst)  # ['ABC', 'abc', 'CBA']
```

**sorted() vs list.sort()**:

| Feature | `sorted()` | `list.sort()` |
|---------|------------|---------------|
| Returns | New list | `None` |
| Original | Unchanged | Modified |
| Works on | Any iterable | Lists only |

### With reduce()

Reduce sequence to single value:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5
```

### Event Handlers

```python
# Button click handler
button.config(command=lambda: print("Button clicked!"))

# Timer callbacks
timer.after(1000, lambda: update_display())

# Thread execution
thread = threading.Thread(target=lambda: process_data(data))
```

---

## Lambda in Data Structures

### Dictionary of Functions

```python
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else None
}

print(operations['add'](10, 5))       # 15
print(operations['multiply'](10, 5))  # 50
```

### List of Functions

```python
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

---

## Advanced Lambda Patterns

### Conditional Expressions

```python
# Ternary operator in lambda
max_func = lambda a, b: a if a > b else b
print(max_func(5, 3))  # 5

# Absolute value
abs_func = lambda x: x if x >= 0 else -x
print(abs_func(-5))  # 5

# Grade assignment
get_grade = lambda score: 'A' if score >= 90 else 'B' if score >= 80 else 'C'
print(get_grade(85))  # B
```

### Nested Lambdas

```python
# Lambda returning lambda
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

---

## Lambda with Built-in Functions

### min() and max()

```python
words = ["python", "is", "awesome"]
longest = max(words, key=lambda w: len(w))
print(longest)  # awesome

pairs = [(1, 5), (3, 2), (2, 8)]
min_pair = min(pairs, key=lambda p: p[1])
print(min_pair)  # (3, 2)
```

### any() and all()

```python
numbers = [1, 2, 3, 4, 5]

# Check if any number is even
has_even = any(map(lambda x: x % 2 == 0, numbers))
print(has_even)  # True

# Check if all numbers are positive
all_positive = all(map(lambda x: x > 0, numbers))
print(all_positive)  # True
```

---

## Lambda Limitations

### Single Expression Only

```python
# Invalid - multiple statements not allowed
# lambda x: print(x); return x ** 2

# Must use regular function
def process(x):
    print(x)
    return x ** 2
```

### No Type Hints

```python
# Cannot add type hints to lambda
# lambda x: int: x + 1  # Invalid

# Use regular function for type hints
def add_one(x: int) -> int:
    return x + 1
```

### No Docstrings

```python
# Cannot add docstring to lambda
# Use regular function for documentation
def calculate_area(length, width):
    """Calculate rectangle area."""
    return length * width
```

### Harder to Debug

```python
# Lambda in traceback shows "<lambda>"
nums = [1, 2, 'three', 4]
# list(map(lambda x: x ** 2, nums))  # Error points to <lambda>

# Named function gives clearer traceback
def square(x):
    return x ** 2
# list(map(square, nums))  # Error points to "square"
```

---

## When to Use Lambda

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
filtered = list(filter(lambda x: x > 0, numbers))
```

## When NOT to Use Lambda

✅ **Use `def` when**:
- Function is complex (multiple statements)
- Function is reused multiple times
- Function needs documentation
- Function needs type hints
- Debugging clarity matters
- Function name adds clarity

```python
# Bad - too complex for lambda
process = lambda x: x * 2 if x > 0 else -x if x < 0 else 0

# Better - use def for complex logic
def process(x):
    if x > 0:
        return x * 2
    elif x < 0:
        return -x
    else:
        return 0
```

```python
# Good regular function with documentation
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

---

## Best Practices

### 1. Keep Lambdas Simple

```python
# Good - simple and clear
double = lambda x: x * 2
sorted(data, key=lambda x: x[1])

# Bad - too complex, use def instead
complex_func = lambda x: (x ** 2 + 3 * x - 5) / (x + 1) if x != -1 else 0
```

### 2. Prefer List Comprehensions

```python
numbers = [1, 2, 3, 4, 5]

# Lambda with map
squares = list(map(lambda x: x ** 2, numbers))

# Often clearer - list comprehension
squares = [x ** 2 for x in numbers]

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Often clearer - list comprehension
evens = [x for x in numbers if x % 2 == 0]
```

### 3. Avoid Assigning Lambdas to Variables

```python
# Against PEP 8
square = lambda x: x ** 2

# PEP 8 compliant
def square(x):
    return x ** 2

# Exception: Lambda as argument is fine
sorted(items, key=lambda x: x.value)
```

### 4. Use Operator Module for Simple Operations

```python
from operator import add, mul, itemgetter

numbers = [1, 2, 3, 4, 5]

# Instead of lambda
total = reduce(lambda x, y: x + y, numbers)
# Use operator
total = reduce(add, numbers)

# Instead of lambda for item access
pairs = [(1, 5), (3, 2), (2, 8)]
sorted_pairs = sorted(pairs, key=lambda p: p[1])
# Use itemgetter
sorted_pairs = sorted(pairs, key=itemgetter(1))
```

---

## Real-World Examples

### Data Processing

```python
users = [
    {'name': 'Alice', 'age': 25, 'active': True},
    {'name': 'Bob', 'age': 30, 'active': False},
    {'name': 'Charlie', 'age': 35, 'active': True}
]

# Get active users sorted by age
active_users = sorted(
    filter(lambda u: u['active'], users),
    key=lambda u: u['age']
)
```

### GUI Event Handlers

```python
import tkinter as tk

root = tk.Tk()

# Lambda captures loop variable correctly with default parameter
for i in range(5):
    btn = tk.Button(
        root, 
        text=f"Button {i}", 
        command=lambda x=i: print(f"Clicked button {x}")
    )
    btn.pack()
```

### DataFrame Operations

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
})

# Apply lambda to column
df['age_group'] = df['age'].apply(lambda x: 'Young' if x < 30 else 'Older')

# Filter rows
young_employees = df[df['age'].apply(lambda x: x < 30)]
```

---

## Quick Reference

### Syntax
```python
lambda parameters: expression
```

### Common Patterns
```python
lambda x: x * 2              # Single parameter
lambda x, y: x + y           # Multiple parameters
lambda: 42                   # No parameters
lambda x, n=2: x ** n        # Default parameter
lambda x: 'yes' if x else 'no'  # Conditional
```

### Common Uses
```python
list(map(lambda x: x ** 2, numbers))      # Transform
list(filter(lambda x: x > 0, numbers))    # Filter
sorted(items, key=lambda x: x.value)      # Sort
reduce(lambda x, y: x + y, numbers)       # Reduce
```

---

## Summary

| Aspect | Lambda | Regular Function |
|--------|--------|------------------|
| Syntax | `lambda x: x + 1` | `def f(x): return x + 1` |
| Name | Anonymous | Named |
| Expressions | Single only | Multiple statements |
| Documentation | No docstring | Docstring supported |
| Type hints | Not supported | Supported |
| Debugging | Shows `<lambda>` | Shows function name |
| Best for | Simple, one-time use | Complex, reusable code |

**Key Takeaways**:

- Lambda functions are anonymous, single-expression functions
- Best used as arguments to higher-order functions
- Keep them simple — use `def` for complex logic
- List comprehensions often clearer than `map`/`filter` with lambda
- Avoid assigning lambdas to variables (PEP 8)
- Consider `operator` module for simple operations
