# sys.setrecursionlimit()


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python limits recursion depth to prevent stack overflow. The default is typically 1000. Understanding and adjusting this limit is important for deep recursion.

---

## The Default Limit

```python
import sys

# Check current limit
print(f"Default recursion limit: {sys.getrecursionlimit()}")
# Output: Default recursion limit: 1000

# Each recursive call uses stack space
def count_depth(n):
    if n == 0:
        return n
    return count_depth(n - 1)

try:
    result = count_depth(1000)
    print("Reached depth 1000")
except RecursionError:
    print("RecursionError: maximum recursion depth exceeded")
```

## Increasing the Limit

```python
import sys

# Increase the limit
sys.setrecursionlimit(5000)
print(f"New recursion limit: {sys.getrecursionlimit()}")

# Now deeper recursion works
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# This now works (would fail with default limit)
result = factorial(2000)
print(f"factorial(2000) computed successfully")
```

## When to Increase

```python
import sys

def process_deep_tree(node, depth=0):
    '''Process deeply nested tree structure'''
    if node is None:
        return
    
    # Process node
    if depth % 100 == 0:
        print(f"Depth: {depth}")
    
    process_deep_tree(node.left, depth + 1)
    process_deep_tree(node.right, depth + 1)

# For deep structures, increase limit temporarily
old_limit = sys.getrecursionlimit()
sys.setrecursionlimit(10000)
try:
    process_deep_tree(root)
finally:
    sys.setrecursionlimit(old_limit)  # Restore original
```

## Caveats

```python
import sys

# Set too high: risk actual stack overflow (hard crash)
sys.setrecursionlimit(1000000)  # Dangerous!

# Better practice: increase moderately for specific task
sys.setrecursionlimit(5000)

# Watch for:
# - Memory consumption increases with limit
# - Stack overflows might not give clean errors
# - Prefer iteration for deep recursion
```

## Best Practices

```python
import sys

def safe_deep_recursion(data):
    '''Safely handle potentially deep recursion'''
    old_limit = sys.getrecursionlimit()
    
    # Increase limit for this operation only
    sys.setrecursionlimit(10000)
    
    try:
        return process_recursively(data)
    finally:
        # Always restore original limit
        sys.setrecursionlimit(old_limit)
```

## Alternative: Use Iteration

For very deep recursion, prefer iteration:

```python
# Recursive: limited by sys.getrecursionlimit()
def sum_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])

# Iterative: no limit
def sum_iterative(numbers):
    return sum(numbers)
```
