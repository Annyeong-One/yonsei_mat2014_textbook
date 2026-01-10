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
# Each scope has its own namespace
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

## The LEGB Rule Explained

LEGB stands for the order in which Python searches for names:

1. **L**ocal - Inside the current function
2. **E**nclosing - In any enclosing functions (outer functions)
3. **G**lobal - At the top level of the module
4. **B**uilt-in - In Python's built-in namespace

```python
# B: Built-in
# len, print, str, etc. are always available

x = "global"  # G: Global

def outer():
    x = "enclosing"  # E: Enclosing
    
    def inner():
        x = "local"  # L: Local
        print(x)  # Searches L -> E -> G -> B
    
    inner()

outer()  # Output: local
```

### Visual Representation

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

### Basic Local Scope

```python
def greet():
    message = "Hello"  # Local to greet()
    print(message)

greet()  # Output: Hello
# print(message)  # NameError: name 'message' is not defined
```

### Function Parameters are Local

```python
def add(a, b):  # a and b are local
    result = a + b  # result is local
    return result

sum_value = add(3, 5)
print(sum_value)  # 8
# print(result)  # NameError: result is local to add()
```

### Local Variables Shadow Outer Scopes

```python
x = "global"

def my_function():
    x = "local"  # Creates new local variable
    print(x)     # Prints local x

my_function()  # Output: local
print(x)       # Output: global (unchanged)
```

### Lifetime of Local Variables

Local variables are created when the function is called and destroyed when it returns:

```python
def create_locals():
    temp = 100
    print(f"Inside: {temp}")
    return temp

result = create_locals()  # temp is created
print(f"Returned: {result}")
# temp no longer exists after function returns
```

## Enclosing Namespace (E)

The **enclosing namespace** refers to the scope of any enclosing (outer) functions. This is relevant in nested function definitions.

### Basic Enclosing Scope

```python
def outer():
    x = "enclosing"  # In outer function's scope
    
    def inner():
        print(x)  # Can access x from enclosing scope
    
    inner()

outer()  # Output: enclosing
```

### Multiple Levels of Nesting

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

### Reading vs Modifying Enclosing Variables

```python
# Reading is allowed
def outer():
    x = 10
    
    def inner():
        print(x)  # Reading x is fine
    
    inner()

# Modifying requires nonlocal
def outer_modify():
    x = 10
    
    def inner():
        # x = x + 1  # UnboundLocalError!
        # Python sees assignment, treats x as local
        pass
    
    inner()

# Correct way to modify
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

### Closures and Enclosing Scope

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

### Basic Global Scope

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
#         Hello
```

### Modifying Global Variables

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

### Global Without Modification

```python
# If you only read, no global keyword needed
message = "Original"

def read_global():
    print(message)  # Just reading, no global needed

read_global()  # Output: Original

# But modifying requires global
def modify_global():
    global message
    message = "Modified"

modify_global()
print(message)  # Output: Modified
```

### Creating Global Variables from Functions

```python
def create_global():
    global new_var  # Declare as global
    new_var = "I'm global!"

create_global()
print(new_var)  # I'm global! (accessible outside function)
```

### Multiple Global Variables

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

## Built-in Namespace (B)

The **built-in namespace** contains Python's built-in functions, exceptions, and constants.

### Common Built-in Names

```python
# These are always available without import
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

### Viewing Built-in Names

```python
import builtins

# See all built-in names
print(dir(builtins))

# Check if name is built-in
print('len' in dir(builtins))  # True
print('myfunction' in dir(builtins))  # False
```

### Shadowing Built-in Names

You can (but shouldn't) override built-in names:

```python
# Bad practice - shadowing built-in
list = [1, 2, 3]  # Shadows built-in list type
print(list)       # Prints [1, 2, 3]

# Now you can't use list() constructor
# result = list(range(5))  # TypeError!

# Restore by deleting
del list
result = list(range(5))  # Works again
```

## Name Resolution in Action

### Example 1: All Four Scopes

```python
# B: Built-in (len is built-in)

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

### Example 2: Progressive Search

```python
value = "global"

def outer():
    # value not defined here, will use global
    
    def inner():
        print(value)  # Searches: L (no) → E (no) → G (yes!)
    
    inner()

outer()  # Output: global
```

### Example 3: Stopping at First Match

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

### Basic nonlocal Usage

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

### nonlocal vs global

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

### nonlocal with Multiple Levels

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

## Common Pitfalls and Gotchas

### 1. UnboundLocalError

```python
x = 10

def buggy_function():
    print(x)  # Tries to access x before assignment
    x = 20    # Python sees this, treats x as local

# buggy_function()  # UnboundLocalError!

# Fix: Use global
def fixed_function():
    global x
    print(x)
    x = 20

fixed_function()
```

### 2. Modifying Mutable Objects

```python
# This works without global (modifying object, not variable)
my_list = [1, 2, 3]

def append_item():
    my_list.append(4)  # Modifying the list object

append_item()
print(my_list)  # [1, 2, 3, 4]

# But reassignment needs global
def replace_list():
    # my_list = [5, 6, 7]  # Creates local variable!
    global my_list
    my_list = [5, 6, 7]   # Modifies global variable

replace_list()
print(my_list)  # [5, 6, 7]
```

### 3. Loop Variables and Closures

```python
# Common mistake
functions = []
for i in range(3):
    functions.append(lambda: i)

# All functions refer to the same i
for f in functions:
    print(f())  # Prints: 2, 2, 2 (all reference final value of i)

# Fix: Use default argument
functions = []
for i in range(3):
    functions.append(lambda x=i: x)  # Captures current value

for f in functions:
    print(f())  # Prints: 0, 1, 2
```

### 4. Shadowing Built-ins

```python
# Accidentally shadowing built-in
def process_data():
    list = [1, 2, 3]  # Shadows built-in list
    # Now can't use list() constructor in this function
    # data = list(range(5))  # TypeError!
    pass

# Better: Use different name
def process_data_better():
    items = [1, 2, 3]
    data = list(range(5))  # Works fine
```

### 5. Namespace Pollution

```python
# Bad: Using global everywhere
count = 0

def increment():
    global count
    count += 1

def decrement():
    global count
    count -= 1

# Better: Encapsulate in class or pass as parameter
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def decrement(self):
        self.count -= 1
```

## Namespace Introspection

### globals() Function

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

### locals() Function

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

### vars() Function

```python
# vars() with no argument is like locals()
def demo():
    x = 10
    y = 20
    print(vars())  # {'x': 10, 'y': 20}

demo()

# vars(object) returns object's __dict__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(vars(p))  # {'name': 'Alice', 'age': 25}
```

### dir() Function

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

### 1. Minimize Global Variables

```python
# Poor - relying on globals
total = 0

def add(x):
    global total
    total += x

# Better - pass values and return results
def add(total, x):
    return total + x

total = 0
total = add(total, 5)
total = add(total, 10)
```

### 2. Use Function Parameters

```python
# Poor - accessing global
config_value = 100

def process():
    return config_value * 2

# Better - pass as parameter
def process(config_value):
    return config_value * 2

result = process(100)
```

### 3. Be Explicit with global/nonlocal

```python
# Poor - implicit global access
counter = 0

def increment():
    global counter  # Be explicit
    counter += 1
```

### 4. Avoid Shadowing Built-ins

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

### 5. Keep Scope as Narrow as Possible

```python
# Poor - wider scope than needed
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

### Example 1: Configuration Management

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

### Example 2: Callback with Closure

```python
def make_callback(prefix):
    """Create callback that uses enclosed prefix."""
    def callback(message):
        print(f"{prefix}: {message}")
    return callback

# Create specialized callbacks
error_handler = make_callback("ERROR")
warning_handler = make_callback("WARNING")
info_handler = make_callback("INFO")

error_handler("File not found")     # ERROR: File not found
warning_handler("Deprecated API")   # WARNING: Deprecated API
info_handler("Process completed")   # INFO: Process completed
```

### Example 3: State Management

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

### LEGB Order
```
Local → Enclosing → Global → Built-in
```

### Scope Keywords
```python
global variable_name    # Modify global variable
nonlocal variable_name  # Modify enclosing variable
```

### Introspection Functions
```python
globals()    # Global namespace dictionary
locals()     # Local namespace dictionary
vars()       # Namespace dictionary
dir()        # List of names in scope
```

### Common Patterns
```python
# Reading from outer scope (no keyword needed)
def outer():
    x = 10
    def inner():
        print(x)  # Just works

# Modifying outer scope (keyword needed)
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
