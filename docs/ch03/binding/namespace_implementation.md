# Namespace Implementation

## Dictionary Storage

### 1. Namespace is Dict

```python
# Namespace = dictionary
x = 10
y = 20

print(locals())
# {'x': 10, 'y': 20, ...}
```

### 2. Access

```python
# Direct access
namespace = locals()
print(namespace['x'])  # 10

# Equivalent to
print(x)  # 10
```

## Local Namespace

### 1. Function Locals

```python
def function():
    x = 10
    y = 20
    
    # View namespace
    print(locals())
    # {'x': 10, 'y': 20}

function()
```

### 2. Fast Locals

CPython optimization:

```python
# Local variables stored in array
# locals() creates dict copy

def f():
    x = 10
    # x stored in fast locals (array)
    # Not in dict initially
```

## Global Namespace

### 1. Module Dict

```python
x = 10

# Module __dict__
print(globals()['x'])  # 10

# Same as
print(x)  # 10
```

### 2. Module Attributes

```python
import sys

# Current module
this_module = sys.modules[__name__]

# Access via attribute
x = 10
print(this_module.x)  # 10
```

## Built-in Namespace

### 1. Builtins Module

```python
import builtins

# Access built-ins
print(builtins.len)
print(builtins.print)

# Check existence
print(hasattr(builtins, 'len'))  # True
```

## Dynamic Access

### 1. vars()

```python
x = 10
y = 20

# Get namespace dict
namespace = vars()
print(namespace['x'])  # 10
```

### 2. getattr()

```python
import sys

# Get attribute dynamically
module = sys.modules[__name__]
value = getattr(module, 'x', None)
```

## Frame Namespace

### 1. Frame Locals

```python
import inspect

def function():
    x = 10
    
    frame = inspect.currentframe()
    print(frame.f_locals)
    # {'x': 10, 'frame': ...}

function()
```

### 2. Frame Globals

```python
import inspect

def function():
    frame = inspect.currentframe()
    print('x' in frame.f_globals)

function()
```

## Class Namespace

### 1. Class Dict

```python
class MyClass:
    x = 10
    y = 20

# Class __dict__
print(MyClass.__dict__['x'])  # 10
```

### 2. Instance Dict

```python
class MyClass:
    def __init__(self):
        self.x = 10

obj = MyClass()
print(obj.__dict__)  # {'x': 10}
```

## Modification

### 1. Direct Modification

```python
# Add to namespace
globals()['new_var'] = 42
print(new_var)  # 42
```

### 2. Warning

```python
# locals() modification doesn't work!
def f():
    locals()['x'] = 10
    # print(x)  # NameError

# Use normal assignment
def g():
    x = 10  # Correct
```

## Summary

### 1. Implementation

- Namespaces are dicts
- Fast locals optimization
- Module __dict__
- Class/instance __dict__

### 2. Access

- locals() / globals()
- vars()
- Frame objects
- Direct dict access
