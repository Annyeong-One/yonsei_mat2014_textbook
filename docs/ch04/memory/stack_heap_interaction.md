# Stack-Heap Interaction

## Name-Object Binding

### 1. Names on Stack

```python
def function():
    x = [1, 2, 3]   # x on stack
                    # [1,2,3] on heap
```

**Memory:**
```
Stack:          Heap:
[frame]
  x -------->  [1, 2, 3]
```

### 2. Multiple Names

```python
def function():
    x = [1, 2, 3]
    y = x
    z = x
```

**Memory:**
```
Stack:          Heap:
[frame]
  x -------->
  y -------->  [1, 2, 3]
  z -------->
```

## Function Calls

### 1. Parameter Passing

```python
def process(lst):
    lst.append(4)

data = [1, 2, 3]
process(data)
```

**Memory:**
```
Stack:              Heap:
[main]
  data -------->
                    [1, 2, 3]
[process]
  lst -------->
```

### 2. Return Values

```python
def create():
    x = [1, 2, 3]
    return x

result = create()
```

**After return:**
```
Stack:          Heap:
[main]
  result ----> [1, 2, 3]
```

## Scope Impact

### 1. Local Scope

```python
def outer():
    x = [1, 2, 3]   # x in outer frame
    
    def inner():
        y = x       # y in inner frame
                    # Both point to heap
    inner()
```

### 2. Global Scope

```python
GLOBAL = [1, 2, 3]  # Global frame

def function():
    local = GLOBAL   # Local frame
                     # Both point to heap
```

## Object Lifetime

### 1. Outlives Frame

```python
def create():
    x = [1, 2, 3]
    return x
    # x removed from stack
    # Object stays on heap

result = create()
# Object still accessible
```

### 2. Multiple References

```python
def function():
    x = [1, 2, 3]
    global GLOBAL
    GLOBAL = x
    # x removed at return
    # Object kept by GLOBAL
```

## Closures

### 1. Captured Variables

```python
def outer():
    x = [1, 2, 3]   # Heap object
    
    def inner():
        return x    # Captures reference
    
    return inner

f = outer()
# outer frame gone
# x kept for closure
```

## Memory Efficiency

### 1. Sharing Objects

```python
# Efficient: one object
data = [1, 2, 3]
refs = [data] * 100

# 100 stack entries
# 1 heap object
```

### 2. Copying Objects

```python
# Inefficient: many objects
refs = [
    [1, 2, 3].copy()
    for _ in range(100)
]

# 100 stack entries
# 100 heap objects
```

## Summary

### 1. Interaction

- Names on stack
- Objects on heap
- Names point to objects
- Multiple names → one object

### 2. Lifetime

- Stack: function scope
- Heap: until GC'd
- Objects outlive frames
