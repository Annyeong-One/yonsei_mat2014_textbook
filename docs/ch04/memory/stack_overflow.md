# Stack Overflow


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The Problem

### 1. Too Deep

```python
def infinite():
    return infinite()

try:
    infinite()
except RecursionError:
    print("Stack overflow!")
```

### 2. Recursion Limit

```python
import sys

print(sys.getrecursionlimit())  # 1000
```

## Causes

### 1. Infinite Recursion

```python
def bad_factorial(n):
    return n * bad_factorial(n - 1)
    # Missing base case!

# Stack overflow
```

### 2. Deep Recursion

```python
def deep(n):
    if n == 0:
        return 0
    return deep(n - 1)

deep(2000)  # May overflow
```

## Solutions

### 1. Base Case

```python
def factorial(n):
    if n <= 1:      # Base case!
        return 1
    return n * factorial(n - 1)
```

### 2. Increase Limit

```python
import sys

sys.setrecursionlimit(2000)

# Use carefully!
```

### 3. Use Iteration

```python
# Better than recursion
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

### 4. Explicit Stack

```python
def iterative_dfs(root):
    stack = [root]
    
    while stack:
        node = stack.pop()
        process(node)
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
```

## Summary

### 1. Stack Overflow

- Too many frames
- Recursion limit
- No tail optimization

### 2. Prevention

- Check base cases
- Use iteration
- Explicit stack
- Increase limit (careful)
