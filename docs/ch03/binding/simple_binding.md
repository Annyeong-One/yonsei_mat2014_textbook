# Simple Binding

## Basic Assignment

### 1. Create Binding

```python
# Create new binding
x = 42

# Name 'x' now bound to 42
print(x)  # 42
```

### 2. Rebinding

```python
# Initial binding
x = 42

# Rebind to new value
x = 100

print(x)  # 100
```

## Multiple Bindings

### 1. Simultaneous

```python
# Create multiple bindings
x, y, z = 1, 2, 3

print(x, y, z)  # 1 2 3
```

### 2. Chained

```python
# All bind to same object
a = b = c = [1, 2, 3]

print(a is b is c)  # True
```

## Namespace

### 1. Local Namespace

```python
def function():
    x = 10  # Binds in local namespace
    y = 20
    print(locals())  # {'x': 10, 'y': 20}

function()
```

### 2. Global Namespace

```python
# Module-level bindings
x = 10
y = 20

print('x' in globals())  # True
```

## Deletion

### 1. Remove Binding

```python
x = 42
print(x)  # 42

del x
# print(x)  # NameError
```

### 2. Object Remains

```python
x = [1, 2, 3]
y = x

del x
print(y)  # [1, 2, 3] - object still exists
```

## Scope

### 1. Local Scope

```python
def function():
    x = 10  # Local binding
    print(x)  # 10

function()
# print(x)  # NameError - not in scope
```

### 2. Global Access

```python
x = 10  # Global

def function():
    print(x)  # Access global
    
function()  # 10
```

## Import Bindings

### 1. Module Import

```python
import math

# 'math' bound in namespace
print('math' in dir())  # True
```

### 2. From Import

```python
from math import pi

# 'pi' bound in namespace
print(pi)  # 3.14159...
```

## Class/Function

### 1. Function Binding

```python
def greet():
    return "Hello"

# 'greet' bound to function
print(type(greet))  # <class 'function'>
```

### 2. Class Binding

```python
class MyClass:
    pass

# 'MyClass' bound to class
print(type(MyClass))  # <class 'type'>
```

## Summary

### 1. Operations

- Create: `x = value`
- Update: `x = new_value`
- Delete: `del x`
- Access: `x`

### 2. Scopes

- Local: function/method
- Global: module
- Builtin: Python internals
