# None Type

Python's `None` represents the absence of a value. It is the sole instance of `NoneType` and serves as Python's null value.

## None Basics

Understanding the fundamental nature of `None`.

### 1. The Singleton

`None` is unique—only one instance exists.

```python
print(type(None))  # <class 'NoneType'>

x = None
y = None
print(x is y)      # True (same object)
print(id(x) == id(y))  # True
```

### 2. Assigning None

Use `None` to indicate absence of value.

```python
result = None       # No result yet
config = None       # Not configured
user = None         # No user logged in

# Check assignment
print(result)       # None
```

### 3. Identity Check

Always use `is` or `is not`, never `==`.

```python
x = None

# Correct way
if x is None:
    print("x is None")

if x is not None:
    print("x has a value")

# Avoid this (works but discouraged)
if x == None:
    print("x is None")
```

## Function Returns

How `None` relates to function return values.

### 1. Implicit Return

Functions without explicit return yield `None`.

```python
def greet(name):
    print(f"Hello, {name}!")

result = greet("Alice")
print(result)        # None
print(type(result))  # <class 'NoneType'>
```

### 2. Explicit None Return

Return `None` explicitly for clarity.

```python
def find_user(user_id):
    users = {1: "Alice", 2: "Bob"}
    if user_id in users:
        return users[user_id]
    return None  # Explicit: user not found

print(find_user(1))   # Alice
print(find_user(99))  # None
```

### 3. Checking Return Values

Always check for `None` returns.

```python
def get_config(key):
    config = {"debug": True}
    return config.get(key)  # Returns None if missing

value = get_config("timeout")
if value is None:
    print("Using default timeout")
else:
    print(f"Timeout: {value}")
```

## Default Arguments

Using `None` for safe default parameters.

### 1. Mutable Default Trap

Mutable defaults cause unexpected behavior.

```python
# Wrong: mutable default shared across calls
def add_item_bad(item, lst=[]):
    lst.append(item)
    return lst

print(add_item_bad(1))  # [1]
print(add_item_bad(2))  # [1, 2] - unexpected!
print(add_item_bad(3))  # [1, 2, 3] - keeps growing!
```

### 2. None Default Pattern

Use `None` to avoid the mutable default trap.

```python
# Correct: None default with internal creation
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [2] - fresh list each time
print(add_item(3))  # [3]
```

### 3. Optional Parameters

Distinguish "not provided" from other values.

```python
def divide(a, b=None):
    if b is None:
        return "No divisor provided"
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(divide(10))      # No divisor provided
print(divide(10, 0))   # Cannot divide by zero
print(divide(10, 2))   # 5.0
```

## Placeholder Usage

Using `None` as a placeholder in code.

### 1. Uninitialized State

Mark variables as not yet assigned.

```python
# Initialize as None
database_connection = None
cached_result = None

def connect():
    global database_connection
    database_connection = create_connection()

def get_data():
    global cached_result
    if cached_result is None:
        cached_result = fetch_from_db()
    return cached_result
```

### 2. Sentinel Value

Use `None` to signal special conditions.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return None  # Not found

result = binary_search([1, 3, 5, 7, 9], 5)
if result is not None:
    print(f"Found at index {result}")
```

### 3. Garbage Collection

Remove references to allow cleanup.

```python
# Large data structure
my_data = [1, 2, 3] * 1000000

# Process data...
process(my_data)

# Release memory
my_data = None  # Now eligible for garbage collection
```

## None Safety

Handle `None` carefully to avoid errors.

### 1. Attribute Errors

Accessing attributes on `None` fails.

```python
x = None

# This raises AttributeError
# print(x.upper())
# AttributeError: 'NoneType' object has no attribute 'upper'

# Check first
if x is not None:
    print(x.upper())
else:
    print("No value")
```

### 2. Guard Clauses

Return early for `None` values.

```python
def process_name(name):
    # Guard clause
    if name is None:
        return "Unknown"
    
    # Safe to use name here
    return name.strip().title()

print(process_name("  alice  "))  # Alice
print(process_name(None))         # Unknown
```

### 3. Fallback Values

Provide defaults for `None` values.

```python
def get_username(user):
    name = user.get("name")
    
    # Using or (caution: treats "" as falsy too)
    return name or "Guest"

# Safer: explicit None check
def get_username_safe(user):
    name = user.get("name")
    return "Guest" if name is None else name

print(get_username({}))              # Guest
print(get_username({"name": ""}))    # Guest (maybe unexpected)
print(get_username_safe({"name": ""}))  # "" (empty string preserved)
```

## None vs Falsy

Distinguish `None` from other falsy values.

### 1. Falsy Values List

Many values are falsy but not `None`.

```python
falsy_values = [None, False, 0, 0.0, "", [], {}, set()]

for val in falsy_values:
    print(f"{str(val):10} is None: {val is None}")
# None       is None: True
# False      is None: False
# 0          is None: False
# 0.0        is None: False
#            is None: False
# []         is None: False
# {}         is None: False
# set()      is None: False
```

### 2. Truthiness vs Identity

Use `is None` for None, truthiness for emptiness.

```python
value = 0

# Wrong: treats 0 as "missing"
if not value:
    print("No value")  # Prints! But 0 is a valid value

# Correct: check specifically for None
if value is None:
    print("No value")
else:
    print(f"Value: {value}")  # Value: 0
```

### 3. Explicit Checks

Be explicit about what you're checking.

```python
def process(data):
    # Check for None specifically
    if data is None:
        return "No data provided"
    
    # Check for empty (but not None)
    if not data:
        return "Empty data"
    
    # Process non-empty data
    return f"Processing {len(data)} items"

print(process(None))    # No data provided
print(process([]))      # Empty data
print(process([1, 2]))  # Processing 2 items
```

## None vs NaN

`None` and `NaN` serve different purposes.

### 1. Type Difference

`None` is `NoneType`, `NaN` is `float`.

```python
import math

print(type(None))          # <class 'NoneType'>
print(type(float("nan")))  # <class 'float'>
```

### 2. Comparison Behavior

`NaN` has unusual equality behavior.

```python
import math

x = None
y = float("nan")

# None: identity works
print(x is None)       # True

# NaN: doesn't equal itself!
print(y == y)          # False
print(math.isnan(y))   # True
```

### 3. Operation Behavior

Operations behave differently.

```python
# None: causes TypeError
# result = 5 + None  # TypeError

# NaN: propagates through operations
result = 5 + float("nan")
print(result)  # nan

print(float("nan") * 0)   # nan
print(float("nan") > 5)   # False
print(float("nan") < 5)   # False
```
