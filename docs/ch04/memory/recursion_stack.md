# Recursion & Stack


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Stack Depth

### 1. Recursion Limit

```python
import sys

# Default limit
print(sys.getrecursionlimit())  # Usually 1000
```

### 2. Stack Overflow

```python
def infinite():
    return infinite()

try:
    infinite()
except RecursionError as e:
    print("Stack overflow!")
```

## Recursive Frames

### 1. Frame Per Call

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# factorial(5) creates 5 frames
```

**Stack:**
```
[factorial(5)]
[factorial(4)]
[factorial(3)]
[factorial(2)]
[factorial(1)]  # Base case
```

### 2. Memory Growth

```python
def deep_recursion(n):
    if n == 0:
        return
    return deep_recursion(n - 1)

# Each call adds frame to stack
deep_recursion(100)  # 100 frames
```

## Tail Recursion

### 1. Not Optimized

Python doesn't optimize tail calls:

```python
def factorial(n, acc=1):
    if n <= 1:
        return acc
    return factorial(n - 1, n * acc)

# Still creates frames
```

### 2. Use Iteration

```python
# Better: iterative
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# No stack growth
```

## Adjust Limit

### 1. Increase Limit

```python
import sys

# Increase (carefully!)
sys.setrecursionlimit(2000)

# Now can recurse deeper
```

### 2. Dangers

```python
# Too high risks:
# - Stack overflow crash
# - Memory exhaustion
# - System instability

# Use with caution!
```

## Deep Recursion

### 1. Problem

```python
def tree_depth(node):
    if not node:
        return 0
    left = tree_depth(node.left)
    right = tree_depth(node.right)
    return 1 + max(left, right)

# Deep tree → stack overflow
```

### 2. Solution

```python
# Use iteration + explicit stack
def tree_depth(root):
    if not root:
        return 0
        
    stack = [(root, 1)]
    max_depth = 0
    
    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
    
    return max_depth
```

## Stack Trace

### 1. View Stack

```python
import traceback

def a():
    b()

def b():
    c()
    
def c():
    traceback.print_stack()

a()
# Shows full call chain
```

### 2. Exception Stack

```python
def outer():
    middle()

def middle():
    inner()
    
def inner():
    raise ValueError("Error!")

try:
    outer()
except ValueError:
    traceback.print_exc()
    # Shows: inner -> middle -> outer
```

## Summary

### 1. Recursion

- Each call adds frame
- Limited by stack size
- Not tail-optimized
- Use iteration when deep

### 2. Stack Management

- Check recursion limit
- Increase carefully
- Prefer iteration
- Use explicit stack
