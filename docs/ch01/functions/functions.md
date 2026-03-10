# Function Definition


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Introduction

Functions are reusable blocks of code that perform specific tasks. They are fundamental to writing organized, maintainable, and efficient Python programs. Understanding how functions work, including the call stack mechanism, is essential for becoming a proficient Python programmer.

This chapter covers function definition, invocation, scope, the call stack, and best practices for writing effective functions.

## What is a Function?

A **function** is a named block of code that:
- Performs a specific task
- Can accept input (parameters)
- Can return output (return values)
- Can be called multiple times
- Helps organize code into logical units

### 1. Why Use

1. **Code Reusability**: Write once, use many times
2. **Modularity**: Break complex problems into smaller pieces
3. **Maintainability**: Easier to update and debug
4. **Abstraction**: Hide implementation details
5. **Testing**: Test individual components independently

## Defining Functions

### 1. Basic Function

Use the `def` keyword to define a function:

```python
def greet():
    """Print a greeting message."""
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
```

**Syntax**:
```python
def function_name():
    """Docstring explaining what the function does."""
    # Function body (indented)
    statement1
    statement2
    # ...
```

### 1. Function

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area (length * width)
    """
    area = length * width
    return area
```

Components:
1. **def keyword**: Starts function definition
2. **Function name**: Follows naming conventions (lowercase with underscores)
3. **Parameters**: Input values in parentheses (optional)
4. **Colon**: Marks end of function header
5. **Docstring**: Documents the function (optional but recommended)
6. **Function body**: Indented code that executes when function is called
7. **return statement**: Specifies output (optional)

### 2. Docstrings

Document your functions with docstrings:

```python
def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of a and b
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(1.5, 2.5)
        4.0
    """
    return a + b

# Access docstring
print(add.__doc__)
help(add)
```

## Calling Functions

### 1. Basic Function

```python
def say_hello():
    print("Hello!")

# Call the function
say_hello()  # Output: Hello!

# Call multiple times
say_hello()
say_hello()
```

### 1. Function Call

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # Output: Hello, Alice!
greet("Bob")     # Output: Hello, Bob!
```

### 2. Using Return

```python
def add(a, b):
    return a + b

# Use return value
result = add(5, 3)
print(result)  # Output: 8

# Use in expression
total = add(10, 20) + add(5, 15)
print(total)  # Output: 50

# Chain function calls
def double(x):
    return x * 2

print(double(add(3, 4)))  # Output: 14
```

## Return Statement

### 1. Basic Return

```python
def square(x):
    return x ** 2

result = square(5)  # result = 25
```

### 2. Multiple Return

Return a tuple to return multiple values:

```python
def get_dimensions():
    length = 10
    width = 5
    height = 3
    return length, width, height  # Returns a tuple

# Unpack returned
l, w, h = get_dimensions()
print(f"Length: {l}, Width: {w}, Height: {h}")

# Or use as tuple
dimensions = get_dimensions()
print(dimensions)  # Output: (10, 5, 3)
```

### 1. Early Return

```python
def validate_age(age):
    """Validate age and return error message if invalid."""
    if age < 0:
        return "Age cannot be negative"
    if age > 150:
        return "Age seems unrealistic"
    return "Valid age"

print(validate_age(-5))   # Age cannot be negative
print(validate_age(200))  # Age seems unrealistic
print(validate_age(25))   # Valid age
```

### 2. No Return

Functions without `return` implicitly return `None`:

```python
def print_message(msg):
    print(msg)
    # No return statement

result = print_message("Hello")
print(result)  # Output: None
```

### 3. Return vs Print

```python
# Return - provides
def add_return(a, b):
    return a + b

result = add_return(3, 4)  # result = 7
print(result * 2)          # Output: 14

# Print - displays to
def add_print(a, b):
    print(a + b)

result = add_print(3, 4)   # Prints: 7
# result is None
# print(result * 2) #
```

## Variable Scope

### 1. Local Scope

Variables defined inside a function are local:

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10
# print(x) #
```

### 1. Global Scope

Variables defined outside functions are global:

```python
x = 10  # Global variable

def my_function():
    print(x)  # Can access global variable

my_function()  # Output: 10
print(x)       # Output: 10
```

### 2. Local vs Global

```python
x = 10  # Global

def my_function():
    x = 20  # Local (shadows global)
    print(f"Inside: {x}")

my_function()      # Output: Inside: 20
print(f"Outside: {x}")  # Output: Outside: 10
```

### 3. Modifying Global

Use `global` keyword to modify global variables:

```python
count = 0  # Global

def increment():
    global count  # Declare intent to modify global
    count += 1

increment()
print(count)  # Output: 1

increment()
print(count)  # Output: 2
```

### 4. Nonlocal Scope

In nested functions, use `nonlocal` to modify enclosing scope:

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x  # Refers to x in outer()
        x = 20
    
    print(f"Before: {x}")  # Before: 10
    inner()
    print(f"After: {x}")   # After: 20

outer()
```

## The Call Stack

### 1. Understanding the

The **call stack** is a data structure that tracks function calls:
- When a function is called, a new **stack frame** is created and pushed onto the stack
- The stack frame contains: function parameters, local variables, return address
- When the function returns, its stack frame is popped off
- Execution resumes at the calling location

### 2. Visualizing the

```python
def function_a():
    print("A: Start")
    function_b()
    print("A: End")

def function_b():
    print("B: Start")
    function_c()
    print("B: End")

def function_c():
    print("C: Executing")

function_a()
```

**Call stack visualization**:
```
1. function_a() is called
   Stack: [function_a]
   
2. function_a() calls function_b()
   Stack: [function_a, function_b]
   
3. function_b() calls function_c()
   Stack: [function_a, function_b, function_c]
   
4. function_c() completes
   Stack: [function_a, function_b]
   
5. function_b() completes
   Stack: [function_a]
   
6. function_a() completes
   Stack: []
```

**Output**:
```
A: Start
B: Start
C: Executing
B: End
A: End
```

### 3. Stack Frame

Each stack frame stores:

```python
def calculate_total(price, quantity, tax_rate=0.1):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

# When called:
# Stack frame
# Parameters:
# Local variables:
# Return address:
```

### 1. Stack Trace

When an error occurs, Python shows the call stack:

```python
def level_1():
    level_2()

def level_2():
    level_3()

def level_3():
    raise ValueError("Something went wrong!")

level_1()
```

**Output (traceback)**:
```
Traceback (most recent call last):
  File "script.py", line 11, in <module>
    level_1()
  File "script.py", line 2, in level_1
    level_2()
  File "script.py", line 5, in level_2
    level_3()
  File "script.py", line 8, in level_3
    raise ValueError("Something went wrong!")
ValueError: Something went wrong!
```

The traceback shows the call stack from bottom (where error occurred) to top (initial call).

## Nested Functions

### 1. Defining

```python
def outer(x):
    """Outer function."""
    
    def inner(y):
        """Inner function."""
        return y * 2
    
    result = inner(x)
    return result + 5

print(outer(10))  # Output: 25
```

### 2. Closures

Inner functions can access outer function variables:

```python
def make_multiplier(n):
    """Return a function that multiplies by n."""
    
    def multiplier(x):
        return x * n  # Accesses n from outer scope
    
    return multiplier

times_3 = make_multiplier(3)
times_5 = make_multiplier(5)

print(times_3(10))  # Output: 30
print(times_5(10))  # Output: 50
```

### 3. Encapsulation

```python
def counter():
    """Create a counter with private state."""
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

# Create counter
my_counter = counter()
print(my_counter())  # 1
print(my_counter())  # 2
print(my_counter())  # 3
```

## Function Objects

### 1. Functions are

In Python, functions are objects that can be:
- Assigned to variables
- Passed as arguments
- Returned from other functions
- Stored in data structures

```python
def greet(name):
    return f"Hello, {name}!"

# Assign to variable
say_hello = greet
print(say_hello("Alice"))  # Output: Hello, Alice!

# Store in list
functions = [greet, len, str]
print(functions[0]("Bob"))  # Output: Hello, Bob!

# Pass as argument
def apply_function(func, value):
    return func(value)

print(apply_function(greet, "Charlie"))  # Output: Hello, Charlie!
```

### 1. Function

Functions have attributes:

```python
def my_function():
    """This is my function."""
    pass

print(my_function.__name__)      # my_function
print(my_function.__doc__)       # This is my function.
print(type(my_function))         # <class 'function'>
```

## Higher-Order

Functions that operate on other functions:

```python
# Function that takes
def apply_twice(func, value):
    """Apply function twice to value."""
    return func(func(value))

def add_five(x):
    return x + 5

result = apply_twice(add_five, 10)
print(result)  # Output: 20 (10 + 5 + 5)

# Function that
def make_power(n):
    """Return a function that raises to power n."""
    def power(x):
        return x ** n
    return power

square = make_power(2)
cube = make_power(3)

print(square(5))  # Output: 25
print(cube(5))    # Output: 125
```

## Built-in Functions

Python provides many built-in functions:

```python
# Type conversion
int("42")         # 42
float("3.14")     # 3.14
str(123)          # "123"

# Math
abs(-5)           # 5
max(1, 5, 3)      # 5
min(1, 5, 3)      # 1
sum([1, 2, 3])    # 6
pow(2, 3)         # 8

# Collections
len([1, 2, 3])    # 3
sorted([3, 1, 2]) # [1, 2, 3]
reversed([1, 2, 3]) # reversed iterator

# Type checking
isinstance(5, int)          # True
type(5)                     # <class 'int'>

# Object inspection
dir(list)         # List all attributes
help(len)         # Display documentation
```

## Best Practices

### 1. Single

Each function should do one thing well:

```python
# Poor - doing too
def process_user(user_data):
    # Validate
    if not user_data:
        return False
    # Transform
    user_data = user_data.lower()
    # Save
    database.save(user_data)
    # Send email
    email.send(user_data)

# Better - separate
def validate_user(user_data):
    return bool(user_data)

def transform_user(user_data):
    return user_data.lower()

def save_user(user_data):
    database.save(user_data)

def notify_user(user_data):
    email.send(user_data)

def process_user(user_data):
    if not validate_user(user_data):
        return False
    user_data = transform_user(user_data)
    save_user(user_data)
    notify_user(user_data)
    return True
```

### 1. Keep Functions

Aim for functions that fit on one screen:

```python
# Poor - too long
def process_order(order):
    # 100+ lines of code
    ...

# Better - break into
def validate_order(order):
    ...

def calculate_total(order):
    ...

def apply_discount(order):
    ...

def process_payment(order):
    ...

def process_order(order):
    if not validate_order(order):
        return False
    total = calculate_total(order)
    total = apply_discount(order, total)
    return process_payment(order, total)
```

### 1. Use Descriptive

```python
# Poor
def f(x, y):
    return x * y

# Better
def calculate_area(length, width):
    return length * width
```

### 1. Limit Parameters

Keep parameter count low (ideally ≤ 3):

```python
# Poor - too many
def create_user(name, email, age, address, phone, city, state, zip):
    ...

# Better - use
def create_user(user_data):
    # user_data is a dictionary with all fields
    ...

# Or use a
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int
    address: str

def create_user(user: User):
    ...
```

### 1. Avoid Side

Functions should avoid unexpected changes:

```python
# Poor - modifies
count = 0

def increment():
    global count
    count += 1  # Side effect

# Better - pure
def increment(count):
    return count + 1

count = increment(count)
```

### 1. Document

```python
def calculate_discount(price, discount_rate):
    """
    Calculate discounted price.
    
    Args:
        price (float): Original price
        discount_rate (float): Discount as decimal (0.0 to 1.0)
    
    Returns:
        float: Discounted price
    
    Raises:
        ValueError: If discount_rate not in valid range
    """
    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1")
    return price * (1 - discount_rate)
```

## Common Patterns

### 1. Guard Clauses

Validate inputs early:

```python
def process_payment(amount, account):
    # Guard clauses
    if amount <= 0:
        return "Invalid amount"
    if not account:
        return "Invalid account"
    if account.balance < amount:
        return "Insufficient funds"
    
    # Main logic
    account.balance -= amount
    return "Success"
```

### 2. Factory Functions

Functions that create and return objects:

```python
def create_person(name, age):
    """Factory function for person dictionaries."""
    return {
        'name': name,
        'age': age,
        'is_adult': age >= 18
    }

person = create_person("Alice", 25)
```

### 3. Command Pattern

Functions that encapsulate actions:

```python
def create_command(action, *args, **kwargs):
    """Create a command that can be executed later."""
    def execute():
        return action(*args, **kwargs)
    return execute

# Create commands
cmd1 = create_command(print, "Hello")
cmd2 = create_command(sum, [1, 2, 3])

# Execute later
cmd1()  # Output: Hello
result = cmd2()  # result = 6
```

## Common Pitfalls

### 1. Mutable Default

```python
# Dangerous!
def append_to(element, list=[]):
    list.append(element)
    return list

print(append_to(1))  # [1]
print(append_to(2))  # [1, 2] - unexpected!

# Safe version
def append_to(element, list=None):
    if list is None:
        list = []
    list.append(element)
    return list
```

### 1. Missing Return

```python
def add(a, b):
    result = a + b
    # Forgot return!

value = add(3, 4)
print(value)  # None
```

### 2. Modifying

```python
def sort_list(items):
    items.sort()  # Modifies original list!
    return items

my_list = [3, 1, 2]
sorted_list = sort_list(my_list)
print(my_list)  # [1, 2, 3] - modified!

# Better - don't
def sort_list(items):
    return sorted(items)  # Returns new list
```

### 1. Excessive Global

```python
# Poor - relies on
total = 0

def add_to_total(value):
    global total
    total += value

# Better - pass and
def add_to_total(total, value):
    return total + value

total = add_to_total(total, 5)
```

## Quick Reference

### 1. Function
```python
def function_name(parameters):
    """Docstring."""
    # Function body
    return value
```

### 2. Function Call
```python
result = function_name(arguments)
```

### 3. Scope Keywords
```python
global variable_name  # Modify global variable
nonlocal variable_name  # Modify enclosing scope variable
```

### 4. Return Statement
```python
return value           # Return single value
return val1, val2     # Return multiple values (tuple)
return                # Return None
# No return statement
```

## Summary

- Functions are reusable blocks of code defined with `def`
- Functions can accept **parameters** and return **values**
- Variables have **scope**: local, global, or nonlocal
- The **call stack** tracks function calls using stack frames
- Functions are **first-class objects** that can be passed around
- **Best practices**: single responsibility, small functions, descriptive names, good documentation
- Avoid **side effects** and **mutable default arguments**
- Use **guard clauses** for early validation
- Functions help organize code into **modular**, **testable** units

Understanding functions and the call stack is fundamental to writing clean, efficient Python code. Master these concepts and you'll be well-equipped to tackle more advanced programming challenges.
