# Variables and Naming

## Introduction

Variables are fundamental building blocks in Python that store data values. Unlike some programming languages, Python variables don't require explicit type declaration—the interpreter infers the type automatically based on the assigned value. This chapter covers everything you need to know about creating, naming, and working with variables in Python.

## What is a Variable?

A **variable** is a named location in memory that stores a value. Think of it as a labeled container that holds data you want to use in your program.

```python
# Creating a variable
message = "Hello, World!"
age = 25
price = 19.99
is_active = True
```

In the examples above:
- `message` stores a string
- `age` stores an integer
- `price` stores a floating-point number
- `is_active` stores a boolean value

## Variable Assignment

### 1. Basic Assignment

The equals sign (`=`) is the assignment operator in Python:

```python
x = 10          # Assign integer 10 to variable x
name = "Alice"  # Assign string "Alice" to variable name
```

**Important**: The assignment operator works from right to left. The value on the right is assigned to the variable on the left.

### 2. Multiple

Python allows you to assign values to multiple variables in a single line:

```python
# Assign the same
a = b = c = 100

# Assign different
x, y, z = 1, 2, 3

# Swapping variables
a, b = 10, 20
a, b = b, a  # Now a = 20, b = 10
```

### 1. Unpacking

You can unpack sequences (like lists or tuples) into individual variables:

```python
# Unpacking a list
coordinates = [10, 20, 30]
x, y, z = coordinates

# Unpacking with the *
first, *middle, last = [1, 2, 3, 4, 5]
# Overview

# Ignoring values with
x, _, z = [1, 2, 3]  # _ is conventionally used for unwanted values
```

## Naming Rules

Python has specific rules and conventions for naming variables. Following these ensures your code is valid and readable.

### 1. Required Rules

These rules are **mandatory**—violating them causes syntax errors:

1. **Must start with a letter or underscore**
   ```python
   # Valid
   name = "John"
   _private = 42
   
   # Invalid
   2name = "John"     # SyntaxError: cannot start with digit
   @variable = 10     # SyntaxError: cannot start with special character
   ```

2. **Can only contain letters, numbers, and underscores**
   ```python
   # Valid
   user_name = "Alice"
   var123 = 100
   _temp_value = 50
   
   # Invalid
   user-name = "Alice"    # SyntaxError: hyphens not allowed
   var@123 = 100          # SyntaxError: @ not allowed
   my variable = 50       # SyntaxError: spaces not allowed
   ```

3. **Case-sensitive**
   ```python
   name = "Alice"
   Name = "Bob"
   NAME = "Charlie"
   # These are three different variables
   ```

4. **Cannot be a reserved keyword**
   ```python
   # Invalid - these are Python keywords
   class = 10      # SyntaxError
   for = 20        # SyntaxError
   if = 30         # SyntaxError
   ```

### 2. Python Keywords

Python reserves certain words that have special meaning. You cannot use these as variable names:

```python
# Python 3.x keywords
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

To see all keywords in your Python version:

```python
import keyword
print(keyword.kwlist)
```

### 1. Naming

While not required by Python, following these conventions makes your code more readable and professional:

1. **Use lowercase with underscores** (snake_case) for variable names
   ```python
   # Good
   user_name = "Alice"
   total_price = 99.99
   is_valid = True
   
   # Avoid (but valid)
   UserName = "Alice"      # Looks like a class name
   totalPrice = 99.99      # camelCase not conventional in Python
   ISVALID = True          # Looks like a constant
   ```

2. **Use ALL_CAPS for constants**
   ```python
   MAX_SIZE = 100
   PI = 3.14159
   API_KEY = "your-api-key"
   ```

3. **Use meaningful, descriptive names**
   ```python
   # Good
   student_count = 25
   average_temperature = 72.5
   
   # Poor
   sc = 25              # Not descriptive
   x = 72.5             # Unclear meaning
   temp = 72.5          # Ambiguous (temporary or temperature?)
   ```

4. **Avoid single-letter names** (except for counters, coordinates, or mathematical contexts)
   ```python
   # Acceptable
   for i in range(10):  # Loop counter
       print(i)
   
   x, y = 10, 20        # Coordinates
   
   # Better for most cases
   for student_index in range(10):
       print(student_index)
   
   horizontal_position, vertical_position = 10, 20
   ```

5. **Use leading underscore for "private" or internal variables**
   ```python
   _internal_value = 42      # Suggests internal use
   __private_value = 100     # Name mangling (advanced topic)
   ```

6. **Avoid trailing underscore** (except to avoid keyword conflicts)
   ```python
   class_ = "Math"       # Acceptable to avoid 'class' keyword
   type_ = "integer"     # Acceptable to avoid 'type' keyword
   ```

## Variable Types

Python is dynamically typed—you don't declare types explicitly:

```python
# The type is
count = 10              # int
price = 19.99           # float
name = "Alice"          # str
is_active = True        # bool
items = [1, 2, 3]       # list
data = {"key": "value"} # dict
```

### 1. Checking Variable

Use the `type()` function to check a variable's type:

```python
x = 42
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>

name = "Alice"
print(type(name))  # <class 'str'>
```

### 2. Type Conversion

Convert between types explicitly:

```python
# String to integer
age_str = "25"
age = int(age_str)  # 25

# Integer to string
count = 100
count_str = str(count)  # "100"

# String to float
price_str = "19.99"
price = float(price_str)  # 19.99

# Float to integer
value = int(3.9)  # 3
```

## Variable Scope

Variables have different scopes depending on where they're defined:

### 1. Local Variables

Variables defined inside a function are local to that function:

```python
def greet():
    message = "Hello"  # Local variable
    print(message)

greet()  # Output: Hello
print(message)  # NameError: name 'message' is not defined
```

### 2. Global Variables

Variables defined outside all functions are global:

```python
count = 0  # Global variable

def increment():
    global count  # Declare that we're using the global variable
    count += 1

increment()
print(count)  # Output: 1
```

### 3. Nonlocal

In nested functions, use `nonlocal` to modify variables from the enclosing scope:

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x  # Refers to x from outer()
        x = 20
    
    inner()
    print(x)  # Output: 20

outer()
```

## Constants

Python doesn't have built-in constant types, but convention uses ALL_CAPS:

```python
# Constants (by
MAX_CONNECTIONS = 100
PI = 3.14159
DEFAULT_TIMEOUT = 30

# These can still be
MAX_CONNECTIONS = 200  # Valid but discouraged
```

For truly immutable values, use tuples or named tuples:

```python
from collections import namedtuple

Config = namedtuple('Config', ['max_size', 'timeout'])
settings = Config(max_size=100, timeout=30)

# settings.max_size =
```

## Common Naming

### 1. Boolean Variables

Prefix with `is_`, `has_`, `can_`, or similar:

```python
is_valid = True
has_permission = False
can_edit = True
should_update = False
```

### 2. Collections

Use plural nouns:

```python
students = ["Alice", "Bob", "Charlie"]
prices = [10.99, 20.50, 15.75]
user_ids = {101, 102, 103}
```

### 3. Counters and

Use descriptive names or conventional single letters:

```python
# Loop counters
for i in range(10):
    pass

# More descriptive
for student_index in range(len(students)):
    pass

for row_num, row_data in enumerate(data):
    pass
```

### 1. Temporary

Use descriptive names even for temporary values:

```python
# Poor
t = user_input.strip().lower()
result = process(t)

# Better
normalized_input = user_input.strip().lower()
result = process(normalized_input)
```

## Variable Deletion

Use the `del` statement to delete variables:

```python
x = 10
print(x)  # Output: 10

del x
print(x)  # NameError: name 'x' is not defined
```

**Note**: Deletion is rarely needed in Python due to automatic garbage collection.

## Variable Identity

### 1. Identity vs

- `is` checks if two variables refer to the same object (identity)
- `==` checks if two variables have the same value (equality)

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (same value)
print(a is b)  # False (different objects)
print(a is c)  # True (same object)
```

### 2. The `id()`

Get the unique identifier of an object:

```python
x = 10
y = 10
z = x

print(id(x))  # e.g., 140234567890
print(id(y))  # Same as x (Python optimizes small integers)
print(id(z))  # Same as x (z references same object)
```

## Best Practices

### 1. Use Meaningful

```python
# Poor
d = 86400  # What does 'd' represent?

# Good
seconds_per_day = 86400
```

### 1. Be Consistent

```python
# Pick a naming style
user_name = "Alice"    # snake_case
user_age = 25          # snake_case
user_email = "alice@example.com"  # snake_case
```

### 1. Avoid Name

```python
# Poor - shadows
list = [1, 2, 3]  # Now you can't use list() constructor

# Good
item_list = [1, 2, 3]
```

### 1. Use Type Hints

```python
# Type hints make code
name: str = "Alice"
age: int = 25
prices: list[float] = [10.99, 20.50]

def greet(name: str) -> str:
    return f"Hello, {name}!"
```

### 1. Initialize

```python
# Poor - undefined
if condition:
    result = calculate()
# result might not

# Good - initialize
result = None
if condition:
    result = calculate()
```

## Common Pitfalls

### 1. Mutable Default

```python
# Dangerous - list is
def add_item(item, items=[]):
    items.append(item)
    return items

# Better - use None as
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### 1. Variable

```python
# Variables can change
x = 10      # int
x = "ten"   # now str - perfectly valid in Python
```

### 1. Integer Division

```python
# Python 2 vs Python 3
result = 5 / 2

# Python 2: result = 2
# Python 3: result =

# Use // for integer
result = 5 // 2  # 2 in both Python 2 and 3
```

## Advanced Topics

### 1. Variable

```python
# PEP 526 variable
count: int  # Declare without assignment
count = 0   # Later assignment

# Complex types
from typing import List, Dict, Optional

names: List[str] = ["Alice", "Bob"]
ages: Dict[str, int] = {"Alice": 25, "Bob": 30}
optional_value: Optional[int] = None
```

### 1. Walrus Operator

Assign and use a variable in the same expression:

```python
# Without walrus
data = get_data()
if data:
    process(data)

# With walrus operator
if (data := get_data()):
    process(data)
```

### 1. Variable

```python
# Unpacking in for
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

for number, letter in pairs:
    print(f"{number}: {letter}")

# Dictionary unpacking
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key} = {value}")
```

## Quick Reference

### 1. Variable Creation
```python
x = 10                    # Simple assignment
x = y = z = 0            # Multiple assignment
a, b, c = 1, 2, 3        # Unpacking
```

### 2. Naming Rules
```python
valid_name = 10          # Valid
_private = 20            # Valid
name2 = 30               # Valid

2invalid = 10            # Invalid (starts with digit)
my-var = 20              # Invalid (hyphen not allowed)
class = 30               # Invalid (keyword)
```

### 3. Type Checking
```python
x = 42
type(x)                  # <class 'int'>
isinstance(x, int)       # True
```

### 4. Scope
```python
global_var = 10          # Global scope

def function():
    local_var = 20       # Local scope
    global global_var    # Access global
    global_var = 30
```

## Summary

- Variables store data values and don't require type declaration
- Variable names must follow specific rules: start with letter/underscore, contain only letters/numbers/underscores, avoid keywords
- Follow PEP 8 conventions: use snake_case, meaningful names, ALL_CAPS for constants
- Python is dynamically typed—variables can change types
- Use `global` and `nonlocal` keywords to modify variables from outer scopes
- Practice good naming: be descriptive, consistent, and follow conventions

Understanding variables and naming rules is fundamental to writing clean, readable Python code. Following these guidelines will make your code easier to understand, maintain, and debug.
