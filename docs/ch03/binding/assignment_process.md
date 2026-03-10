# Assignment Process


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Understanding how Python executes assignment statements and binds names to objects.

## Assignment Steps

When Python executes an assignment statement, it follows these steps:

### Step 1: Evaluate the Right-Hand Side (RHS)

The expression on the right side is evaluated first:

```python
x = 2 + 3
# 1. Evaluate 2 + 3 → 5
# 2. Bind x to 5
```

```python
y = len([1, 2, 3]) * 2
# 1. Evaluate len([1, 2, 3]) → 3
# 2. Evaluate 3 * 2 → 6
# 3. Bind y to 6
```

### Step 2: Create/Update Binding

The name is bound to the resulting object in the appropriate namespace:

```python
x = 42  # Creates binding in local namespace
# Equivalent to: locals()['x'] = 42
```

## Basic Binding Operations

### Create Binding

```python
x = 42
# Name 'x' now bound to 42
print(x)  # 42
```

### Rebinding

Assigning to an existing name creates a new binding:

```python
x = 42
x = "hello"  # x now refers to a different object
```

The old object (`42`) is not modified—`x` simply points to a new object.

### Delete Binding

```python
x = 42
print(x)  # 42

del x
# print(x)  # NameError
```

Note that `del` removes the binding, not the object:

```python
x = [1, 2, 3]
y = x

del x
print(y)  # [1, 2, 3] - object still exists
```

## Multiple Assignment

### Simultaneous (Tuple Unpacking)

```python
a, b = 1, 2
# Equivalent to:
# temp = (1, 2)
# a = temp[0]
# b = temp[1]
```

```python
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3
```

### Chained Assignment

```python
x = y = z = 0
# All three names bound to the same object
print(x is y is z)  # True
```

### Swap Values

```python
a, b = b, a
# RHS evaluated first: (b, a) tuple created
# Then unpacked to a, b
```

## Namespace and Scope

### Local Namespace

```python
def function():
    x = 10  # Binds in local namespace
    y = 20
    print(locals())  # {'x': 10, 'y': 20}

function()
# print(x)  # NameError - not in scope
```

### Global Namespace

```python
x = 10  # Module-level binding

def function():
    print(x)  # Access global

function()  # 10
print('x' in globals())  # True
```

### Namespace Updates

Assignment modifies the appropriate namespace:

```python
x = 10  # Updates globals()

def func():
    y = 20  # Updates locals()
    global z
    z = 30  # Updates globals()
```

## Special Binding Forms

### Import Bindings

```python
import math
# 'math' bound in namespace
print('math' in dir())  # True

from math import pi
# 'pi' bound in namespace
print(pi)  # 3.14159...
```

### Function and Class Bindings

```python
def greet():
    return "Hello"

# 'greet' bound to function object
print(type(greet))  # <class 'function'>
```

```python
class MyClass:
    pass

# 'MyClass' bound to class object
print(type(MyClass))  # <class 'type'>
```

### Walrus Operator

```python
x = (a := 5) + (b := 10)
# 1. Evaluate (a := 5) → assigns 5 to a, returns 5
# 2. Evaluate (b := 10) → assigns 10 to b, returns 10
# 3. Evaluate 5 + 10 → 15
# 4. Bind x to 15
```

## Summary

| Step | Description |
|------|-------------|
| 1 | Evaluate right-hand side expression |
| 2 | Create object (if needed) |
| 3 | Bind name to object in namespace |

### Binding Operations

| Operation | Syntax | Effect |
|-----------|--------|--------|
| Create | `x = value` | New binding |
| Update | `x = new_value` | Rebind name |
| Delete | `del x` | Remove binding |
| Access | `x` | Lookup in namespace |

Key points:
- RHS always evaluated first
- Assignment binds names, doesn't copy values
- Multiple assignment uses unpacking
- Namespace determines scope of binding
- `del` removes bindings, not objects
