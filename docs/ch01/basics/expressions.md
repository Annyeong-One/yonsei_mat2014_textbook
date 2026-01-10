# Expressions and Statements

## Introduction

Understanding the difference between expressions and statements is fundamental to Python programming. While they may seem similar, they serve distinct purposes in your code. This chapter explores both concepts in depth, covering operators, evaluation, and how Python processes your code.

## Expressions vs Statements

### What is an Expression?

An **expression** is any piece of code that evaluates to a value. Expressions can be as simple as a literal or as complex as a function call combined with arithmetic operations.

```python
# Simple expressions
42                    # Evaluates to 42
3 + 5                 # Evaluates to 8
"Hello" + " World"    # Evaluates to "Hello World"
len([1, 2, 3])        # Evaluates to 3
x > 5                 # Evaluates to True or False
```

**Key characteristic**: Expressions always produce a value that can be used elsewhere.

### What is a Statement?

A **statement** is a complete line of code that performs an action. Statements don't necessarily produce a value—they do something.

```python
# Statements
x = 10                # Assignment statement
print("Hello")        # Function call statement
if x > 5:            # Conditional statement
    pass
import math          # Import statement
del x                # Deletion statement
```

**Key characteristic**: Statements perform actions but don't evaluate to a value.

### The Distinction

```python
# Expression (can be used as part of something else)
total = 5 + 3        # 5 + 3 is an expression

# Statement (complete action)
print(5 + 3)         # The whole line is a statement
                     # but 5 + 3 is still an expression within it

# Expression as statement (expression statement)
5 + 3                # Valid but useless (result is discarded)
```

**Important**: 
- Expressions can appear within statements
- Statements cannot appear within expressions
- An expression followed by a newline becomes an expression statement

## Types of Expressions

### 1. Literal Expressions

The simplest expressions—just literal values:

```python
42              # Integer literal
3.14            # Float literal
"Hello"         # String literal
True            # Boolean literal
[1, 2, 3]       # List literal
{"key": "val"}  # Dictionary literal
None            # None literal
```

### 2. Arithmetic Expressions

Mathematical operations using arithmetic operators:

```python
# Basic arithmetic
10 + 5          # Addition: 15
10 - 5          # Subtraction: 5
10 * 5          # Multiplication: 50
10 / 5          # Division: 2.0 (always float in Python 3)
10 // 3         # Floor division: 3
10 % 3          # Modulus (remainder): 1
10 ** 2         # Exponentiation: 100

# Operator precedence (PEMDAS)
result = 2 + 3 * 4        # 14 (not 20)
result = (2 + 3) * 4      # 20 (parentheses first)
result = 10 + 5 * 2 ** 3  # 50 (** before *, then +)
```

### 3. Comparison Expressions

Compare values and evaluate to boolean:

```python
# Comparison operators
5 == 5          # Equal to: True
5 != 3          # Not equal to: True
5 > 3           # Greater than: True
5 < 3           # Less than: False
5 >= 5          # Greater than or equal: True
5 <= 3          # Less than or equal: False

# Chained comparisons
1 < 5 < 10      # True (equivalent to: 1 < 5 and 5 < 10)
x = 5
0 <= x <= 100   # True

# Identity comparisons
x is None       # Check if x is None
x is not None   # Check if x is not None

# Membership tests
'a' in 'abc'           # True
5 in [1, 2, 3, 4, 5]  # True
```

### 4. Logical Expressions

Combine boolean values with logical operators:

```python
# Logical operators
True and False   # False (both must be True)
True or False    # True (at least one must be True)
not True         # False (negation)

# Complex logical expressions
age = 25
has_license = True
can_drive = age >= 18 and has_license  # True

# Short-circuit evaluation
x = 5
result = x > 0 and x < 10  # Second part only evaluated if first is True

# Truth values
bool(0)          # False
bool("")         # False
bool([])         # False
bool(None)       # False
bool(42)         # True
bool("hello")    # True
bool([1, 2])     # True
```

### 5. String Expressions

Operations on strings:

```python
# Concatenation
"Hello" + " " + "World"      # "Hello World"

# Repetition
"Ha" * 3                      # "HaHaHa"

# String formatting
name = "Alice"
f"Hello, {name}!"             # f-string: "Hello, Alice!"
"Hello, {}!".format(name)     # format method: "Hello, Alice!"
"Hello, %s!" % name           # old style: "Hello, Alice!"

# String methods (all return new strings)
"hello".upper()               # "HELLO"
"  trim  ".strip()            # "trim"
"a,b,c".split(",")           # ["a", "b", "c"]
```

### 6. List/Collection Expressions

Operations on collections:

```python
# List operations
[1, 2, 3] + [4, 5]           # [1, 2, 3, 4, 5]
[1, 2] * 3                    # [1, 2, 1, 2, 1, 2]
len([1, 2, 3])                # 3

# List comprehensions
[x * 2 for x in range(5)]     # [0, 2, 4, 6, 8]
[x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Dictionary comprehensions
{x: x**2 for x in range(5)}   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehensions
{x % 3 for x in range(10)}    # {0, 1, 2}

# Generator expressions
(x * 2 for x in range(5))     # Generator object
```

### 7. Function Call Expressions

Calling functions produces values:

```python
# Built-in functions
len([1, 2, 3])        # 3
abs(-5)               # 5
max(1, 5, 3)          # 5
sum([1, 2, 3, 4])     # 10

# User-defined functions
def add(a, b):
    return a + b

result = add(3, 5)    # 8

# Method calls
"hello".upper()       # "HELLO"
[1, 2, 3].append(4)   # None (modifies list in place)
```

### 8. Lambda Expressions

Anonymous function expressions:

```python
# Lambda syntax
square = lambda x: x ** 2
square(5)  # 25

# Used with higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)  # [1, 4, 9, 16, 25]
even = filter(lambda x: x % 2 == 0, numbers)  # [2, 4]

# Multiple arguments
add = lambda a, b: a + b
add(3, 5)  # 8
```

### 9. Conditional Expressions (Ternary Operator)

Inline if-else expressions:

```python
# Syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"  # "adult"

# Nested conditional expressions
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"

# In function calls
max_value = max(a, b) if a is not None and b is not None else 0
```

## Types of Statements

### 1. Assignment Statements

Assign values to variables:

```python
# Simple assignment
x = 10

# Multiple assignment
a, b = 1, 2
x = y = z = 0

# Augmented assignment
x += 5     # Equivalent to: x = x + 5
x -= 3     # Equivalent to: x = x - 3
x *= 2     # Equivalent to: x = x * 2
x /= 4     # Equivalent to: x = x / 4
x //= 2    # Equivalent to: x = x // 2
x %= 3     # Equivalent to: x = x % 3
x **= 2    # Equivalent to: x = x ** 2

# Walrus operator (Python 3.8+)
if (n := len(items)) > 10:
    print(f"List is large: {n} items")
```

### 2. Import Statements

Import modules and packages:

```python
# Basic import
import math
import os, sys

# Import specific items
from math import pi, sqrt
from os import path

# Import with alias
import numpy as np
import pandas as pd

# Import all (generally discouraged)
from math import *

# Relative imports (in packages)
from . import module
from ..package import module
```

### 3. Function Definition Statements

Define functions:

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Function with default parameters
def power(base, exponent=2):
    return base ** exponent

# Function with *args and **kwargs
def flexible_function(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

# Type hints
def add(a: int, b: int) -> int:
    return a + b
```

### 4. Class Definition Statements

Define classes:

```python
# Basic class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
```

### 5. Control Flow Statements

Control program execution (covered in detail in control_flow.md):

```python
# if statement
if condition:
    # do something
    pass

# for loop
for item in collection:
    # process item
    pass

# while loop
while condition:
    # do something
    pass

# try-except
try:
    # risky code
    pass
except Exception as e:
    # handle error
    pass
```

### 6. Other Statements

```python
# pass statement (does nothing)
def not_implemented():
    pass

# del statement (delete references)
x = 10
del x

# return statement (in functions)
def add(a, b):
    return a + b

# yield statement (in generators)
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# break and continue (in loops)
for i in range(10):
    if i == 5:
        break  # Exit loop
    if i % 2 == 0:
        continue  # Skip to next iteration
    print(i)

# assert statement (debugging)
assert x > 0, "x must be positive"

# with statement (context management)
with open('file.txt', 'r') as f:
    content = f.read()
```

## Operator Precedence

Python evaluates expressions according to operator precedence (highest to lowest):

| Precedence | Operator | Description |
|------------|----------|-------------|
| 1 (highest) | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `~x` | Unary plus, minus, bitwise NOT |
| 4 | `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulus |
| 5 | `+`, `-` | Addition, subtraction |
| 6 | `<<`, `>>` | Bitwise shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `is not`, `in`, `not in` | Comparisons, identity, membership |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 (lowest) | `or` | Logical OR |

### Precedence Examples

```python
# Arithmetic precedence
2 + 3 * 4          # 14 (not 20)
(2 + 3) * 4        # 20

# Comparison and logical
x = 5
x > 3 and x < 10   # True
not x > 10         # True (equivalent to: not (x > 10))

# Mixed operations
result = 2 + 3 * 4 ** 2  # 2 + 3 * 16 = 2 + 48 = 50
```

### Using Parentheses for Clarity

Even when not required, parentheses improve readability:

```python
# Less clear
result = a and b or c and d

# More clear
result = (a and b) or (c and d)
```

## Expression Evaluation

### Left-to-Right Evaluation

Python evaluates expressions from left to right (except for exponentiation):

```python
# Left to right
result = 10 - 5 - 2  # (10 - 5) - 2 = 3

# Exponentiation is right to left
result = 2 ** 3 ** 2  # 2 ** (3 ** 2) = 2 ** 9 = 512
```

### Short-Circuit Evaluation

Logical operators use short-circuit evaluation:

```python
# 'and' stops at first False
def expensive_check():
    print("Running expensive check")
    return True

False and expensive_check()  # expensive_check() is NOT called

# 'or' stops at first True
True or expensive_check()    # expensive_check() is NOT called

# Practical use
x = None
value = x and x.some_method()  # Won't call some_method() if x is None
```

### Lazy Evaluation in Generators

Generator expressions are evaluated lazily:

```python
# List comprehension (eager - computed immediately)
squares_list = [x ** 2 for x in range(1000000)]  # Takes memory

# Generator expression (lazy - computed on demand)
squares_gen = (x ** 2 for x in range(1000000))   # Almost no memory

# Values computed only when needed
next(squares_gen)  # Computes and returns first value
```

## Type Coercion

### Implicit Type Coercion

Python automatically converts types in some contexts:

```python
# Numeric operations
3 + 4.5        # 7.5 (int + float → float)
True + 5       # 6 (bool treated as int: True = 1, False = 0)

# String formatting
"Answer: " + str(42)  # "Answer: 42"
```

### Explicit Type Conversion

```python
# To integer
int(3.14)      # 3 (truncates)
int("42")      # 42
int("1010", 2) # 10 (binary to decimal)

# To float
float(42)      # 42.0
float("3.14")  # 3.14

# To string
str(42)        # "42"
str([1, 2, 3]) # "[1, 2, 3]"

# To boolean
bool(0)        # False
bool(1)        # True
bool("")       # False
bool("hello")  # True

# To list
list("abc")    # ['a', 'b', 'c']
list((1, 2))   # [1, 2]

# To tuple
tuple([1, 2])  # (1, 2)
```

## Expression Statements

An expression followed by a newline becomes an expression statement:

```python
# Expression statement (result is discarded)
5 + 3          # Valid but useless

# Useful expression statements
print("Hello") # Function call
list.append(5) # Method call

# Interactive mode vs script
>>> 5 + 3      # In REPL, displays 8
8
# In script, same line does nothing (result discarded)
```

## Compound Expressions

### Nesting Expressions

```python
# Nested function calls
result = max(abs(-5), abs(-3), abs(-7))  # 7

# Complex expressions
total = sum([x ** 2 for x in range(10) if x % 2 == 0])

# Multiple operations
value = ((a + b) * c - d) / e
```

### Readability Considerations

Break complex expressions for clarity:

```python
# Hard to read
result = sum([x**2 for x in range(100) if x%2==0 and x>10 and x<90])

# Better
even_numbers = [x for x in range(100) if x % 2 == 0]
in_range = [x for x in even_numbers if 10 < x < 90]
squares = [x ** 2 for x in in_range]
result = sum(squares)

# Or with intermediate variables
numbers = range(100)
filtered = [x for x in numbers if x % 2 == 0 and 10 < x < 90]
result = sum(x ** 2 for x in filtered)
```

## Common Patterns and Idioms

### Swapping Variables

```python
# Pythonic way
a, b = b, a

# Old way (using temporary variable)
temp = a
a = b
b = temp
```

### Chaining Comparisons

```python
# Pythonic
if 0 <= x <= 100:
    pass

# Less pythonic
if x >= 0 and x <= 100:
    pass
```

### Default Values with `or`

```python
# Get value or default
name = input_name or "Guest"

# Be careful with falsy values
count = 0
result = count or 10  # 10, but maybe count = 0 is valid!

# Better for falsy values
result = count if count is not None else 10
```

### Conditional Assignment

```python
# Set value based on condition
status = "pass" if score >= 60 else "fail"

# Multiple conditions
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
```

## Best Practices

### 1. Keep Expressions Simple

```python
# Complex (hard to debug)
result = func1(func2(x) + func3(y)) * func4(z) if condition else default

# Better (easier to understand and debug)
value1 = func2(x) + func3(y)
value2 = func1(value1) * func4(z)
result = value2 if condition else default
```

### 2. Use Meaningful Variable Names

```python
# Poor
x = (a + b) * c - d / e

# Better
total_cost = (base_price + tax) * quantity - discount / 100
```

### 3. Avoid Side Effects in Expressions

```python
# Poor (modifies list in expression)
if items.append(new_item) or len(items) > 10:
    pass

# Better (separate modification and check)
items.append(new_item)
if len(items) > 10:
    pass
```

### 4. Use Parentheses for Clarity

```python
# Unclear precedence
result = a and b or c and d

# Clear with parentheses
result = (a and b) or (c and d)
```

### 5. One Statement Per Line

```python
# Poor (hard to read)
x = 1; y = 2; z = 3

# Better
x = 1
y = 2
z = 3
```

## Common Pitfalls

### 1. Integer Division

```python
# Python 3: always returns float
result = 5 / 2   # 2.5

# Use // for integer division
result = 5 // 2  # 2
```

### 2. Mutable Default Arguments

```python
# Dangerous!
def append_to(element, list=[]):
    list.append(element)
    return list

# Both calls modify the same list
append_to(1)  # [1]
append_to(2)  # [1, 2] - unexpected!

# Safe version
def append_to(element, list=None):
    if list is None:
        list = []
    list.append(element)
    return list
```

### 3. Expression vs Statement Confusion

```python
# This is a statement, not an expression
x = print("Hello")  # x is None (print returns None)

# This is an expression
x = len("Hello")    # x is 5
```

### 4. Comparison Chaining

```python
# Be careful with logic
a = 5
# This doesn't mean "x not equal to 1 or 2"
if x != 1 or 2:  # Always True! (2 is truthy)
    pass

# Correct way
if x != 1 and x != 2:
    pass

# Or
if x not in (1, 2):
    pass
```

## Summary

- **Expressions** evaluate to values; **statements** perform actions
- Expressions can be simple (literals) or complex (combinations of operators and function calls)
- Python has rich set of operators with well-defined precedence rules
- Use parentheses for clarity even when not strictly necessary
- Understand short-circuit evaluation for efficient code
- Keep expressions readable—break complex ones into multiple lines
- Statements include assignments, imports, function definitions, and control flow
- Expression statements (expression + newline) are valid but should do something useful

Understanding expressions and statements is crucial for writing clear, correct Python code. Master these concepts to write more expressive and maintainable programs.
