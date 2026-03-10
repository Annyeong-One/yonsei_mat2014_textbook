# Parameters and


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Introduction

Parameters and return values are the primary mechanisms for data flow in and out of functions. Understanding how to effectively use different types of parameters and return values is crucial for writing flexible, reusable functions.

This chapter covers all aspects of function parameters (positional, keyword, default, variable-length) and return values (single, multiple, None) with comprehensive examples and best practices.

## Function Parameters

### 1. Basic Parameters

Parameters are variables listed in the function definition:

```python
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")  # "Alice" is an argument
```

**Terminology**:
- **Parameter**: Variable in function definition
- **Argument**: Actual value passed when calling function

### 2. Positional

Parameters matched by position:

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}")

describe_pet("dog", "Buddy")
# Output: I have a dog

describe_pet("Buddy", "dog")  # Wrong order!
# Output: I have a
```

### 1. Keyword Arguments

Arguments specified by parameter name:

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}")

# Using keyword
describe_pet(animal_type="cat", pet_name="Whiskers")
describe_pet(pet_name="Whiskers", animal_type="cat")  # Order doesn't matter

# Mix positional and
describe_pet("hamster", pet_name="Fluffy")
```

### 1. Default

Parameters with default values:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                    # Hello, Alice!
greet("Bob", "Hi")                # Hi, Bob!
greet("Charlie", greeting="Hey")  # Hey, Charlie!
```

**Rules**:
- Default parameters must come after non-default parameters
- Default values are evaluated once at function definition

```python
# Correct
def func(a, b, c=0, d=1):
    pass

# Error - non-default
def func(a, b=0, c):  # SyntaxError
    pass
```

## Variable-Length

### 1. *args - Arbitrary

Collect extra positional arguments into a tuple:

```python
def sum_all(*numbers):
    """Sum any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all())               # 0
```

**Usage**:
```python
def print_info(name, *hobbies):
    print(f"Name: {name}")
    print(f"Hobbies: {', '.join(hobbies)}")

print_info("Alice", "reading", "coding", "hiking")
# Name: Alice
# Hobbies: reading,
```

### 1. **kwargs -

Collect extra keyword arguments into a dictionary:

```python
def create_profile(name, **details):
    """Create user profile with arbitrary details."""
    print(f"Name: {name}")
    for key, value in details.items():
        print(f"{key}: {value}")

create_profile("Alice", age=25, city="NYC", job="Engineer")
# Name: Alice
# age: 25
# city: NYC
# job: Engineer
```

### 1. Combining *args

```python
def flexible_function(required, *args, **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

flexible_function(1, 2, 3, name="Alice", age=25)
# Required: 1
# Args: (2, 3)
# Kwargs: {'name':
```

**Order**: 
```python
def func(pos1, pos2, default=0, *args, **kwargs):
    pass

# Correct order:
# Positional
# Default parameters
# *args
# **kwargs
```

## Unpacking Arguments

### 1. Unpacking

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # Unpacks to add(1, 2, 3)
print(result)  # 6

# With tuples
coords = (10, 20, 30)
result = add(*coords)
print(result)  # 60
```

### 1. Unpacking

```python
def greet(first_name, last_name, age):
    print(f"Hello, {first_name} {last_name}, age {age}")

person = {
    'first_name': 'Alice',
    'last_name': 'Smith',
    'age': 25
}

greet(**person)  # Unpacks to greet(first_name='Alice', ...)
# Output: Hello, Alice
```

## Keyword-Only

Force parameters to be passed as keyword arguments using `*`:

```python
def create_user(name, age, *, email, phone):
    """email and phone must be passed as keyword arguments."""
    print(f"Name: {name}, Age: {age}")
    print(f"Email: {email}, Phone: {phone}")

# Correct
create_user("Alice", 25, email="alice@example.com", phone="123-456")

# Error - email and phone must be keyword arguments
# create_user("Alice", 25, "alice@example.com", "123-456")  # TypeError
```

### 1. Keyword-Only with *args

```python
def process_data(*data, sort=False, reverse=False):
    """Process variable data with options."""
    result = list(data)
    if sort:
        result.sort(reverse=reverse)
    return result

print(process_data(3, 1, 4, 1, 5, sort=True))
# [1, 1, 3, 4, 5]

print(process_data(3, 1, 4, 1, 5, sort=True, reverse=True))
# [5, 4, 3, 1, 1]
```

## Positional-Only Parameters

Force parameters to be positional using `/`:

```python
def divide(a, b, /):
    """a and b must be positional arguments."""
    return a / b

# Correct
result = divide(10, 2)  # 5.0

# Error - cannot use
# result =
```

### 1. Combining / and *

```python
def func(pos_only, /, standard, *, kwd_only):
    """
    pos_only: positional only
    standard: positional or keyword
    kwd_only: keyword only
    """
    print(f"{pos_only}, {standard}, {kwd_only}")

# Valid calls
func(1, 2, kwd_only=3)
func(1, standard=2, kwd_only=3)

# Invalid
# func(pos_only=1,
# func(1, 2, 3) #
```

## Return Values

### 1. Single Return

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

### 2. Multiple Return

Return a tuple to return multiple values:

```python
def get_min_max(numbers):
    """Return both minimum and maximum."""
    return min(numbers), max(numbers)

# Unpack return values
minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")
# Min: 1, Max: 9

# Or use as tuple
result = get_min_max([1, 5, 3, 9, 2])
print(result)  # (1, 9)
```

### 1. Named Return

Use namedtuple or dataclass for clarity:

```python
from collections import namedtuple

# Using namedtuple
Point = namedtuple('Point', ['x', 'y'])

def get_point():
    return Point(10, 20)

p = get_point()
print(f"x: {p.x}, y: {p.y}")
# x: 10, y: 20

# Using dataclass
from dataclasses import dataclass

@dataclass
class Result:
    success: bool
    message: str
    data: dict

def process_data(data):
    if not data:
        return Result(False, "No data provided", {})
    return Result(True, "Success", data)
```

### 1. Returning None

Functions without explicit return return `None`:

```python
def greet(name):
    print(f"Hello, {name}")
    # No return statement

result = greet("Alice")
print(result)  # None

# Explicit None return
def validate(value):
    if value < 0:
        return None
    return value

result = validate(-5)
if result is None:
    print("Invalid value")
```

### 1. Conditional

```python
def get_grade(score):
    """Return letter grade based on score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print(get_grade(85))  # B
```

### 2. Returning

```python
def divide(a, b):
    """Return result or error message."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

result = divide(10, 2)
print(result)  # 5.0

result = divide(10, 0)
print(result)  # Error: Division by zero
```

## Type Hints (Python

Add type information to parameters and return values:

```python
def greet(name: str, age: int) -> str:
    """
    Greet a person.
    
    Args:
        name: Person's name
        age: Person's age
    
    Returns:
        Greeting message
    """
    return f"Hello, {name}! You are {age} years old."

result = greet("Alice", 25)
```

### 1. Complex Type

```python
from typing import List, Dict, Tuple, Optional, Union

def process_numbers(numbers: List[int]) -> Tuple[int, int]:
    """Return sum and average of numbers."""
    total = sum(numbers)
    avg = total // len(numbers)
    return total, avg

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    """Return user dict or None if not found."""
    # Implementation
    return None

def parse_value(value: str) -> Union[int, float]:
    """Return int or float depending on value."""
    if '.' in value:
        return float(value)
    return int(value)
```

## Parameter Passing:

Python uses **"pass by assignment"**:

### 1. Immutable Objects

Changes don't affect the original:

```python
def modify_number(x):
    x = 100  # Creates new local variable
    print(f"Inside: {x}")

num = 10
modify_number(num)
print(f"Outside: {num}")  # Still 10
# Inside: 100
# Outside: 10
```

### 1. Mutable Objects

Changes affect the original:

```python
def modify_list(lst):
    lst.append(4)  # Modifies original list
    print(f"Inside: {lst}")

numbers = [1, 2, 3]
modify_list(numbers)
print(f"Outside: {numbers}")  # Modified!
# Inside: [1, 2, 3, 4]
# Outside: [1, 2, 3,

# To avoid
modify_list(numbers[:])  # Pass a copy
```

### 1. Reassignment vs

```python
def reassign_list(lst):
    lst = [10, 20, 30]  # Creates new local variable
    print(f"Inside: {lst}")

def modify_list(lst):
    lst.append(4)  # Modifies original
    print(f"Inside: {lst}")

numbers = [1, 2, 3]

reassign_list(numbers)
print(f"After reassign: {numbers}")  # Unchanged
# Inside: [10, 20, 30]
# After reassign: [1,

modify_list(numbers)
print(f"After modify: {numbers}")  # Changed!
# Inside: [1, 2, 3, 4]
# After modify: [1, 2,
```

## Advanced Parameter

### 1. Builder Pattern

```python
def create_user(name, age=None, email=None, phone=None):
    """Create user with optional fields."""
    user = {'name': name}
    if age is not None:
        user['age'] = age
    if email is not None:
        user['email'] = email
    if phone is not None:
        user['phone'] = phone
    return user

user1 = create_user("Alice")
user2 = create_user("Bob", age=30, email="bob@example.com")
```

### 2. Options

```python
def process_data(data, **options):
    """Process data with configurable options."""
    # Default options
    defaults = {
        'sort': False,
        'reverse': False,
        'unique': False
    }
    # Merge with provided options
    defaults.update(options)
    
    result = list(data)
    if defaults['unique']:
        result = list(set(result))
    if defaults['sort']:
        result.sort(reverse=defaults['reverse'])
    return result

result = process_data([3, 1, 4, 1, 5], sort=True, unique=True)
print(result)  # [1, 3, 4, 5]
```

### 3. Callback

```python
def process_items(items, callback):
    """Process each item with callback function."""
    results = []
    for item in items:
        result = callback(item)
        results.append(result)
    return results

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled = process_items(numbers, double)
print(doubled)  # [2, 4, 6, 8, 10]

# With lambda
squared = process_items(numbers, lambda x: x ** 2)
print(squared)  # [1, 4, 9, 16, 25]
```

## Best Practices

### 1. Limit Parameter

Keep parameters to 3-4 maximum:

```python
# Poor - too many
def create_account(name, email, age, address, city, state, zip_code, phone):
    pass

# Better - use
def create_account(user_data):
    pass

# Or use dataclass
from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    email: str
    age: int
    address: str

def create_account(user: UserData):
    pass
```

### 1. Use Descriptive

```python
# Poor
def calc(x, y, z):
    return x * y + z

# Better
def calculate_total(price, quantity, tax):
    return price * quantity + tax
```

### 1. Provide

```python
# Poor - unclear
def connect(host, port=0):
    pass

# Better - meaningful
def connect(host, port=8080):
    pass
```

### 1. Avoid Mutable

```python
# Dangerous!
def add_item(item, items=[]):
    items.append(item)
    return items

# Safe
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### 1. Use Type Hints

```python
def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area."""
    return length * width
```

### 2. Document

```python
def process_payment(amount, account, *, fee_rate=0.02):
    """
    Process payment with optional fee.
    
    Args:
        amount (float): Payment amount
        account (Account): Account object
        fee_rate (float, optional): Fee as decimal. Defaults to 0.02.
    
    Returns:
        bool: True if successful, False otherwise
    
    Raises:
        ValueError: If amount is negative
        InsufficientFundsError: If account balance is too low
    """
    pass
```

### 3. Return Early for

```python
def process_order(order):
    # Guard clauses - return early
    if not order:
        return None
    if order.amount <= 0:
        return None
    if not order.customer:
        return None
    
    # Main logic
    return calculate_total(order)
```

### 4. Return Consistent

```python
# Poor - inconsistent
def get_user(user_id):
    if user_id == 0:
        return None
    if user_id < 0:
        return False
    return {'id': user_id, 'name': 'User'}

# Better - consistent
def get_user(user_id):
    if user_id <= 0:
        return None
    return {'id': user_id, 'name': 'User'}
```

## Common Pitfalls

### 1. Mutable Default

```python
# Wrong!
def append_to(element, target=[]):
    target.append(element)
    return target

list1 = append_to(1)  # [1]
list2 = append_to(2)  # [1, 2] - unexpected!

# Correct
def append_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target
```

### 1. Modifying

```python
def sort_numbers(numbers):
    numbers.sort()  # Modifies original!
    return numbers

nums = [3, 1, 2]
sorted_nums = sort_numbers(nums)
print(nums)  # [1, 2, 3] - modified!

# Better - don't
def sort_numbers(numbers):
    return sorted(numbers)  # Returns new list
```

### 1. Using

```python
# Poor - too flexible,
def do_something(*args, **kwargs):
    pass

# Better - explicit
def do_something(name, value, options=None):
    pass
```

### 1. Not Validating

```python
# Risky - no
def divide(a, b):
    return a / b  # ZeroDivisionError if b is 0!

# Better - validate
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

## Quick Reference

### 1. Parameter Types
```python
def func(
    pos,              # Positional
    pos_default=0,    # Positional with default
    *args,            # Variable positional
    kwd_only,         # Keyword-only (after *)
    **kwargs          # Variable keyword
):
    pass
```

### 2. Calling with
```python
func(1)                    # Positional
func(pos=1)                # Keyword
func(1, 2, 3)              # Multiple positional
func(*[1, 2, 3])           # Unpack list
func(**{'pos': 1})         # Unpack dict
```

### 3. Return Values
```python
return value               # Single value
return val1, val2          # Multiple values (tuple)
return                     # None
# No return also
```

### 1. Type Hints
```python
def func(name: str, age: int = 0) -> str:
    return f"{name} is {age}"
```

## Summary

- **Parameters** receive input; **arguments** are values passed
- **Positional parameters**: matched by position
- **Keyword arguments**: specified by name
- **Default parameters**: have default values
- **\*args**: collect extra positional arguments
- **\*\*kwargs**: collect extra keyword arguments
- **Keyword-only**: force parameters to be passed by name (after `*`)
- **Positional-only**: force parameters to be positional (before `/`)
- **Return values**: can be single, multiple (tuple), or None
- **Type hints**: document expected types
- **Best practices**: limit parameters, use descriptive names, validate inputs, return consistent types
- **Avoid**: mutable defaults, modifying arguments, inconsistent returns

Understanding parameters and return values thoroughly enables you to write flexible, robust functions that are easy to use and maintain.
