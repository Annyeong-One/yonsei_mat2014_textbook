# LEGB Rule

## Introduction

The **LEGB rule** is Python's name resolution mechanism that determines where to look for variables. When Python encounters a variable name, it searches through namespaces in a specific order: **L**ocal, **E**nclosing, **G**lobal, and **B**uilt-in.

Understanding the LEGB rule is crucial for:
- Avoiding naming conflicts
- Understanding variable scope
- Debugging name resolution issues
- Writing clear, maintainable code

This chapter provides a comprehensive explanation of the LEGB rule with detailed examples and best practices.

## What is a Namespace?

A **namespace** is a mapping from names to objects. Think of it as a dictionary where keys are variable names and values are the objects those names refer to.

```python
# Each scope has its
x = 10  # Global namespace
y = 20  # Global namespace

def my_function():
    z = 30  # Local namespace (of my_function)
    print(z)
```

**Key Points**:
- Namespaces prevent naming conflicts
- Different namespaces can have the same variable names
- Namespaces are created at different times and have different lifetimes

## The LEGB Rule

LEGB stands for the order in which Python searches for names:

1. **L**ocal - Inside the current function
2. **E**nclosing - In any enclosing functions (outer functions)
3. **G**lobal - At the top level of the module
4. **B**uilt-in - In Python's built-in namespace

```python
# B: Built-in
# len, print, str,

x = "global"  # G: Global

def outer():
    x = "enclosing"  # E: Enclosing
    
    def inner():
        x = "local"  # L: Local
        print(x)  # Searches L -> E -> G -> B
    
    inner()

outer()  # Output: local
```

### 1. Visual

```
┌─────────────────────────────────────┐
│ Built-in Namespace (B)              │
│ len, print, str, int, etc.          │
│ ┌───────────────────────────────┐   │
│ │ Global Namespace (G)          │   │
│ │ Module-level variables        │   │
│ │ ┌─────────────────────────┐   │   │
│ │ │ Enclosing Namespace (E) │   │   │
│ │ │ Outer function          │   │   │
│ │ │ ┌─────────────────────┐ │   │   │
│ │ │ │ Local Namespace (L)│ │   │   │
│ │ │ │ Current function   │ │   │   │
│ │ │ └─────────────────────┘ │   │   │
│ │ └─────────────────────────┘   │   │
│ └───────────────────────────────┘   │
└─────────────────────────────────────┘

Python searches from innermost to outermost: L → E → G → B
```

## Local Namespace (L)

The **local namespace** contains names defined inside the current function.

### 1. Basic Local Scope

```python
def greet():
    message = "Hello"  # Local to greet()
    print(message)

greet()  # Output: Hello
# print(message) #
```

### 1. Function

```python
def add(a, b):  # a and b are local
    result = a + b  # result is local
    return result

sum_value = add(3, 5)
print(sum_value)  # 8
# print(result) #
```

### 1. Local Variables

```python
x = "global"

def my_function():
    x = "local"  # Creates new local variable
    print(x)     # Prints local x

my_function()  # Output: local
print(x)       # Output: global (unchanged)
```

### 2. Lifetime of Local

Local variables are created when the function is called and destroyed when it returns:

```python
def create_locals():
    temp = 100
    print(f"Inside: {temp}")
    return temp

result = create_locals()  # temp is created
print(f"Returned: {result}")
# temp no longer
```

## Enclosing Namespace

The **enclosing namespace** refers to the scope of any enclosing (outer) functions. This is relevant in nested function definitions.

### 1. Basic Enclosing

```python
def outer():
    x = "enclosing"  # In outer function's scope
    
    def inner():
        print(x)  # Can access x from enclosing scope
    
    inner()

outer()  # Output: enclosing
```

### 2. Multiple Levels

```python
def level1():
    x = "level1"
    
    def level2():
        y = "level2"
        
        def level3():
            z = "level3"
            print(f"x: {x}")  # From level1 (enclosing)
            print(f"y: {y}")  # From level2 (enclosing)
            print(f"z: {z}")  # From level3 (local)
        
        level3()
    
    level2()

level1()
# Output:
# x: level1
# y: level2
# z: level3
```

### 1. Reading vs

```python
# Reading is allowed
def outer():
    x = 10
    
    def inner():
        print(x)  # Reading x is fine
    
    inner()

# Modifying requires
def outer_modify():
    x = 10
    
    def inner():
        # x = x + 1  # UnboundLocalError!
        # Python sees assignment, treats x as local
        pass
    
    inner()

# Correct way to
def outer_correct():
    x = 10
    
    def inner():
        nonlocal x  # Declare we want to modify enclosing x
        x = x + 1
        print(x)
    
    inner()  # Output: 11
    print(x)  # Output: 11

outer_correct()
```

### 1. Closures and

```python
def make_counter():
    count = 0  # In enclosing scope
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

# Create counters
counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1 (separate enclosing scope)
print(counter1())  # 3
```

## Global Namespace (G)

The **global namespace** contains names defined at the module level (top level of a Python file).

### 1. Basic Global

```python
# Global variables
count = 0
message = "Hello"

def display():
    # Can read global variables
    print(count)
    print(message)

display()
# Output: 0
# Hello
```

### 1. Modifying Global

```python
count = 0

def increment():
    global count  # Declare intent to modify global
    count += 1

increment()
print(count)  # 1

increment()
print(count)  # 2
```

### 2. Global Without

```python
# If you only read, no
message = "Original"

def read_global():
    print(message)  # Just reading, no global needed

read_global()  # Output: Original

# But modifying
def modify_global():
    global message
    message = "Modified"

modify_global()
print(message)  # Output: Modified
```

### 1. Creating Global

```python
def create_global():
    global new_var  # Declare as global
    new_var = "I'm global!"

create_global()
print(new_var)  # I'm global! (accessible outside function)
```

### 2. Multiple Global

```python
x = 1
y = 2
z = 3

def modify_all():
    global x, y, z  # Declare multiple globals
    x = 10
    y = 20
    z = 30

modify_all()
print(x, y, z)  # Output: 10 20 30
```

## Built-in Namespace

The **built-in namespace** contains Python's built-in functions, exceptions, and constants.

### 1. Common Built-in

```python
# These are always
print(len([1, 2, 3]))      # len is built-in
print(max(5, 10))          # max is built-in
print(type(42))            # type is built-in
print(abs(-5))             # abs is built-in

# Built-in exceptions
try:
    x = 1 / 0
except ZeroDivisionError:  # Built-in exception
    print("Division by zero")

# Built-in constants
print(True)   # Built-in
print(False)  # Built-in
print(None)   # Built-in
```

### 1. Viewing Built-in

```python
import builtins

# See all built-in
print(dir(builtins))

# Check if name is
print('len' in dir(builtins))  # True
print('myfunction' in dir(builtins))  # False
```

### 1. Shadowing

You can (but shouldn't) override built-in names:

```python
# Bad practice -
list = [1, 2, 3]  # Shadows built-in list type
print(list)       # Prints [1, 2, 3]

# Now you can't use
# result =

# Restore by deleting
del list
result = list(range(5))  # Works again
```

## Name Resolution in

### 1. Key point

```python
# B: Built-in (len is

x = "global x"  # G: Global

def outer():
    x = "enclosing x"  # E: Enclosing
    
    def inner():
        x = "local x"  # L: Local
        print(x)         # Searches L → E → G → B
        print(len("hi")) # Uses built-in len
    
    inner()
    print(x)  # Prints enclosing x

outer()
print(x)  # Prints global x
```

**Output**:
```
local x
2
enclosing x
global x
```

### 1. Key point

```python
value = "global"

def outer():
    # value not defined here, will use global
    
    def inner():
        print(value)  # Searches: L (no) → E (no) → G (yes!)
    
    inner()

outer()  # Output: global
```

### 2. Key point

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        # x = "local"  # If uncommented, this would be used
        print(x)  # Searches: L (no) → E (yes!)
    
    inner()

outer()  # Output: enclosing
```

## The nonlocal Keyword

The `nonlocal` keyword allows you to modify variables in enclosing (but not global) scope.

### 1. Basic nonlocal

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

### 2. nonlocal vs

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner_global():
        global x
        x = "modified global"
    
    def inner_nonlocal():
        nonlocal x
        x = "modified enclosing"
    
    print(f"Before: outer x = {x}")
    inner_nonlocal()
    print(f"After nonlocal: outer x = {x}")
    inner_global()
    print(f"After global: outer x = {x}")

outer()
print(f"Global x = {x}")
```

**Output**:
```
Before: outer x = enclosing
After nonlocal: outer x = modified enclosing
After global: outer x = modified enclosing
Global x = modified global
```

### 3. nonlocal with

```python
def level1():
    x = "level1"
    
    def level2():
        x = "level2"
        
        def level3():
            nonlocal x  # Refers to nearest enclosing x (level2)
            x = "modified"
        
        print(f"Before level3: {x}")
        level3()
        print(f"After level3: {x}")
    
    level2()
    print(f"level1 x: {x}")  # Unchanged

level1()
```

**Output**:
```
Before level3: level2
After level3: modified
level1 x: level1
```

## Common Pitfalls and

### 1. UnboundLocalError

```python
x = 10

def buggy_function():
    print(x)  # Tries to access x before assignment
    x = 20    # Python sees this, treats x as local

# buggy_function() #

# Fix: Use global
def fixed_function():
    global x
    print(x)
    x = 20

fixed_function()
```

### 1. Modifying Mutable

```python
# This works without
my_list = [1, 2, 3]

def append_item():
    my_list.append(4)  # Modifying the list object

append_item()
print(my_list)  # [1, 2, 3, 4]

# But reassignment
def replace_list():
    # my_list = [5, 6, 7]  # Creates local variable!
    global my_list
    my_list = [5, 6, 7]   # Modifies global variable

replace_list()
print(my_list)  # [5, 6, 7]
```

### 1. Loop Variables

```python
# Common mistake
functions = []
for i in range(3):
    functions.append(lambda: i)

# All functions refer
for f in functions:
    print(f())  # Prints: 2, 2, 2 (all reference final value of i)

# Fix: Use default
functions = []
for i in range(3):
    functions.append(lambda x=i: x)  # Captures current value

for f in functions:
    print(f())  # Prints: 0, 1, 2
```

### 1. Shadowing

```python
# Accidentally
def process_data():
    list = [1, 2, 3]  # Shadows built-in list
    # Now can't use list() constructor in this function
    # data = list(range(5))  # TypeError!
    pass

# Better: Use
def process_data_better():
    items = [1, 2, 3]
    data = list(range(5))  # Works fine
```

### 1. Namespace

```python
# Bad: Using global
count = 0

def increment():
    global count
    count += 1

def decrement():
    global count
    count -= 1

# Better: Encapsulate
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def decrement(self):
        self.count -= 1
```

## Namespace

### 1. globals()

Returns dictionary of global namespace:

```python
x = 10
y = 20

def show_globals():
    print(globals()['x'])  # 10
    print(globals()['y'])  # 20
    
    # See all global names
    for name in globals():
        if not name.startswith('__'):
            print(f"{name}: {globals()[name]}")

show_globals()
```

### 2. locals() Function

Returns dictionary of local namespace:

```python
def my_function():
    a = 1
    b = 2
    c = 3
    
    print(locals())  # {'a': 1, 'b': 2, 'c': 3}
    
    # Access local variables
    for name, value in locals().items():
        print(f"{name} = {value}")

my_function()
```

### 3. vars() Function

```python
# vars() with no
def demo():
    x = 10
    y = 20
    print(vars())  # {'x': 10, 'y': 20}

demo()

# vars(object) returns
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(vars(p))  # {'name': 'Alice', 'age': 25}
```

### 1. dir() Function

Lists names in current scope:

```python
x = 10
y = 20

def my_function():
    z = 30
    print(dir())  # Shows local names including 'z'

print(dir())  # Shows global names including 'x', 'y'
my_function()
```

## Best Practices

### 1. Minimize Global

```python
# Poor - relying on
total = 0

def add(x):
    global total
    total += x

# Better - pass values
def add(total, x):
    return total + x

total = 0
total = add(total, 5)
total = add(total, 10)
```

### 1. Use Function

```python
# Poor - accessing
config_value = 100

def process():
    return config_value * 2

# Better - pass as
def process(config_value):
    return config_value * 2

result = process(100)
```

### 1. Be Explicit with

```python
# Poor - implicit
counter = 0

def increment():
    global counter  # Be explicit
    counter += 1
```

### 1. Avoid Shadowing

```python
# Bad
list = [1, 2, 3]
dict = {'a': 1}
sum = 42

# Good
items = [1, 2, 3]
mapping = {'a': 1}
total = 42
```

### 1. Keep Scope as

```python
# Poor - wider scope
result = 0

def calculate(x, y):
    global result
    result = x + y
    return result

# Better - local scope
def calculate(x, y):
    result = x + y
    return result

result = calculate(5, 3)
```

## Practical Examples

### 1. Key point

```python
# Global configuration
CONFIG = {
    'debug': True,
    'max_retries': 3,
    'timeout': 30
}

def process_data(data):
    # Read from global config
    if CONFIG['debug']:
        print(f"Processing {len(data)} items")
    
    # Process data...
    return data

def update_config(key, value):
    global CONFIG
    CONFIG[key] = value

# Usage
data = [1, 2, 3]
process_data(data)
update_config('debug', False)
```

### 1. Key point

```python
def make_callback(prefix):
    """Create callback that uses enclosed prefix."""
    def callback(message):
        print(f"{prefix}: {message}")
    return callback

# Create specialized
error_handler = make_callback("ERROR")
warning_handler = make_callback("WARNING")
info_handler = make_callback("INFO")

error_handler("File not found")     # ERROR: File not found
warning_handler("Deprecated API")   # WARNING: Deprecated API
info_handler("Process completed")   # INFO: Process completed
```

### 1. Key point

```python
def create_account(initial_balance):
    """Create account with private balance."""
    balance = initial_balance  # Enclosing scope
    
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    
    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return balance
        else:
            raise ValueError("Insufficient funds")
    
    def get_balance():
        return balance
    
    return deposit, withdraw, get_balance

# Create account
deposit, withdraw, get_balance = create_account(1000)

print(get_balance())  # 1000
deposit(500)
print(get_balance())  # 1500
withdraw(200)
print(get_balance())  # 1300
```

## Quick Reference

### 1. LEGB Order
```
Local → Enclosing → Global → Built-in
```

### 2. Scope Keywords
```python
global variable_name    # Modify global variable
nonlocal variable_name  # Modify enclosing variable
```

### 3. Introspection
```python
globals()    # Global namespace dictionary
locals()     # Local namespace dictionary
vars()       # Namespace dictionary
dir()        # List of names in scope
```

### 4. Common Patterns
```python
# Reading from outer
def outer():
    x = 10
    def inner():
        print(x)  # Just works

# Modifying outer
def outer():
    x = 10
    def inner():
        nonlocal x  # Required
        x = 20
```

## Summary

- **LEGB Rule**: Python searches Local → Enclosing → Global → Built-in
- **Local (L)**: Variables defined in current function
- **Enclosing (E)**: Variables in outer functions (closures)
- **Global (G)**: Module-level variables
- **Built-in (B)**: Python's built-in names
- **global keyword**: Modify global variables from local scope
- **nonlocal keyword**: Modify enclosing (but not global) variables
- **Best practices**: Minimize globals, use parameters, avoid shadowing built-ins
- **Common pitfall**: UnboundLocalError when reading then assigning
- **Introspection**: Use `globals()`, `locals()`, `vars()`, `dir()`

Understanding the LEGB rule is fundamental to mastering Python's scoping and avoiding common namespace-related bugs. Always strive for clear, explicit code with minimal reliance on global state.
