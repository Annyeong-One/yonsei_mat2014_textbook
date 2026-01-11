# Frame Objects

## Call Stack

### 1. Function Calls

Each call creates frame:

```python
def outer():
    return inner()

def inner():
    return deepest()
    
def deepest():
    import inspect
    return inspect.stack()

# Three frames stacked
```

### 2. Frame Structure

```python
import inspect

def example():
    x = 10
    frame = inspect.currentframe()
    
    print(frame.f_locals)   # Local vars
    print(frame.f_globals)  # Global vars
    print(frame.f_code)     # Code object
```

## Frame Contents

### 1. Local Namespace

```python
def function():
    a = 1
    b = 2
    frame = inspect.currentframe()
    print(frame.f_locals)
    # {'a': 1, 'b': 2, 'frame': ...}
```

### 2. Global Namespace

```python
GLOBAL_VAR = 100

def function():
    frame = inspect.currentframe()
    print('GLOBAL_VAR' in frame.f_globals)
    # True
```

## Stack Inspection

### 1. Current Frame

```python
import inspect

def show_frame():
    frame = inspect.currentframe()
    print(f"Function: {frame.f_code.co_name}")
    print(f"Line: {frame.f_lineno}")
    
show_frame()
```

### 2. Call Stack

```python
def outer():
    middle()

def middle():
    inner()
    
def inner():
    import inspect
    for frame_info in inspect.stack():
        print(frame_info.function)
    # inner, middle, outer
```

## Frame Lifetime

### 1. Creation

```python
def function():
    # Frame created at call
    x = 10
    # Frame active
    return x
    # Frame destroyed after return
```

### 2. Nested Calls

```python
def a():
    return b()  # a's frame stays
    
def b():
    return c()  # b's frame stays
    
def c():
    return 42   # c returns, frames unwind
```

## Practical Uses

### 1. Debugging

```python
def debug_info():
    frame = inspect.currentframe()
    caller = frame.f_back
    
    print(f"Called from: {caller.f_code.co_name}")
    print(f"At line: {caller.f_lineno}")
```

### 2. Introspection

```python
def get_caller_locals():
    frame = inspect.currentframe()
    caller_frame = frame.f_back
    return caller_frame.f_locals

def example():
    x = 10
    y = 20
    caller_vars = get_caller_locals()
    print(caller_vars)
```

## Frame Attributes

### 1. Key Attributes

```python
import inspect

def show_attributes():
    f = inspect.currentframe()
    
    print(f.f_locals)    # Local vars
    print(f.f_globals)   # Global vars  
    print(f.f_code)      # Code object
    print(f.f_lineno)    # Current line
    print(f.f_back)      # Caller frame
```

## Summary

### 1. Frame Object

- Created per function call
- Contains local namespace
- Links to globals
- Stack forms call chain

### 2. Uses

- Debugging
- Introspection
- Stack traces
- Context tracking
