# Stack & Heap Overview

## Two Memory Areas

### 1. Stack

Function call frames and local names:

```python
def function():
    x = 10          # Name on stack
    y = 20          # Name on stack
    return x + y

# Stack grows/shrinks with calls
```

### 2. Heap

Objects storage:

```python
x = [1, 2, 3]       # Object on heap
y = "hello"         # Object on heap
z = 42              # Object on heap
```

## Stack Properties

### 1. Fast Access

```python
def compute():
    a = 10          # Fast stack access
    b = 20
    return a + b
```

### 2. Automatic Management

```python
def f():
    x = 10          # Stack allocated
    return x
    # x deallocated when f returns
```

### 3. Limited Size

```python
def recursive(n):
    if n == 0:
        return
    return recursive(n - 1)

# Too deep causes stack overflow
```

## Heap Properties

### 1. Dynamic Size

```python
# Can grow as needed
lst = []
for i in range(1000000):
    lst.append(i)   # Heap grows
```

### 2. Manual Management

```python
x = [1, 2, 3]       # Heap allocated
# Stays until GC'd
del x               # Remove reference
```

### 3. Slower Access

```python
# Heap access slower than stack
# But necessary for objects
```

## What Goes Where

### 1. Stack

- Function frames
- Local name bindings
- Return addresses
- Parameters

### 2. Heap

- All Python objects
- Lists, dicts, strings
- Integers, floats
- User-defined objects

## Memory Visualization

### 1. Example

```python
def process():
    x = [1, 2, 3]
    y = x
    return y
```

**Memory:**
```
Stack:
  [process frame]
    x -----> 
    y -----> [1, 2, 3] (Heap)
    
Heap:
  [1, 2, 3] object
```

### 2. Multiple Frames

```python
def outer():
    a = [1, 2]
    return inner(a)

def inner(param):
    b = param
    return b
```

**Stack:**
```
[outer frame]
  a -----> [1, 2] (Heap)
  
[inner frame]  
  param -----> [1, 2] (Heap)
  b -----> [1, 2] (Heap)
```

## Frame Objects

### 1. Stack Frame

```python
import inspect

def example():
    frame = inspect.currentframe()
    print(frame.f_locals)

example()
```

### 2. Frame Info

```python
def show_frame():
    frame = inspect.currentframe()
    print(f"Function: {frame.f_code.co_name}")
    print(f"Line: {frame.f_lineno}")
    
show_frame()
```

## Summary

### 1. Stack

- Fast, limited size
- Function frames
- Name bindings
- Auto management

### 2. Heap

- Slower, dynamic size
- All objects
- Manual/GC management
- Longer lifetime
