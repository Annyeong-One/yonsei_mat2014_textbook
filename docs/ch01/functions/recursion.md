# Recursion and Stack Overflow

## Introduction

**Recursion** is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems. While recursion can provide elegant solutions to certain problems, it requires careful management to avoid stack overflow errors.

This chapter covers recursive functions, how they work, the call stack during recursion, common recursive patterns, optimization techniques, and how to prevent and handle stack overflow errors.

## What is Recursion?

A recursive function has two key components:

1. **Base case**: The condition that stops the recursion
2. **Recursive case**: The function calling itself with modified arguments

```python
def countdown(n):
    # Base case
    if n <= 0:
        print("Blast off!")
        return
    
    # Recursive case
    print(n)
    countdown(n - 1)

countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Blast off!
```

### How Recursion Works

Each recursive call creates a new stack frame:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

result = factorial(4)
# Call stack progression:
# factorial(4) -> 4 * factorial(3)
#              -> 4 * 3 * factorial(2)
#              -> 4 * 3 * 2 * factorial(1)
#              -> 4 * 3 * 2 * 1 * factorial(0)
#              -> 4 * 3 * 2 * 1 * 1
#              -> 24
```

### Recursion vs Iteration

Many recursive problems can be solved iteratively:

```python
# Recursive factorial
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_recursive(5))  # 120
print(factorial_iterative(5))  # 120
```

**When to use recursion**:
- Problem has recursive structure (tree traversal, divide-and-conquer)
- Code clarity matters more than performance
- Problem is naturally expressed recursively

**When to use iteration**:
- Simple loops suffice
- Performance is critical
- Avoiding stack overflow is important

## Classic Recursive Problems

### 1. Factorial

```python
def factorial(n):
    """Calculate n! recursively."""
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # 120
print(factorial(0))  # 1
```

### 2. Fibonacci Sequence

```python
def fibonacci(n):
    """Return the nth Fibonacci number."""
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8
# Sequence: 0, 1, 1, 2, 3, 5, 8, ...
```

**Warning**: Naive Fibonacci is extremely inefficient due to repeated calculations!

### 3. Sum of List

```python
def sum_list(numbers):
    """Sum all numbers in a list recursively."""
    # Base case
    if not numbers:
        return 0
    # Recursive case
    return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15
```

### 4. Reverse String

```python
def reverse_string(s):
    """Reverse a string recursively."""
    # Base case
    if len(s) <= 1:
        return s
    # Recursive case
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # olleh
```

### 5. Power Function

```python
def power(base, exp):
    """Calculate base^exp recursively."""
    # Base case
    if exp == 0:
        return 1
    # Recursive case
    return base * power(base, exp - 1)

print(power(2, 5))  # 32
```

## The Call Stack in Recursion

### Stack Frame Visualization

Each recursive call adds a frame to the call stack:

```python
def factorial(n):
    print(f"Called with n={n}")
    if n == 0:
        print("Base case reached")
        return 1
    result = n * factorial(n - 1)
    print(f"Returning {result} for n={n}")
    return result

factorial(4)
```

**Output**:
```
Called with n=4
Called with n=3
Called with n=2
Called with n=1
Called with n=0
Base case reached
Returning 1 for n=1
Returning 2 for n=2
Returning 6 for n=3
Returning 24 for n=4
```

**Stack visualization**:
```
Step 1: factorial(4) calls factorial(3)
Stack: [factorial(4)]

Step 2: factorial(3) calls factorial(2)
Stack: [factorial(4), factorial(3)]

Step 3: factorial(2) calls factorial(1)
Stack: [factorial(4), factorial(3), factorial(2)]

Step 4: factorial(1) calls factorial(0)
Stack: [factorial(4), factorial(3), factorial(2), factorial(1)]

Step 5: factorial(0) returns 1 (base case)
Stack: [factorial(4), factorial(3), factorial(2), factorial(1)]

Step 6: factorial(1) returns 1
Stack: [factorial(4), factorial(3), factorial(2)]

Step 7: factorial(2) returns 2
Stack: [factorial(4), factorial(3)]

Step 8: factorial(3) returns 6
Stack: [factorial(4)]

Step 9: factorial(4) returns 24
Stack: []
```

## Stack Overflow

### What is Stack Overflow?

**Stack overflow** occurs when the call stack grows too large and exceeds the system's memory limit.

### Causes of Stack Overflow

1. **No base case**:
```python
def infinite_recursion(n):
    # No base case!
    return infinite_recursion(n - 1)

# infinite_recursion(10)  # RecursionError!
```

2. **Base case never reached**:
```python
def buggy_countdown(n):
    if n == 0:  # Base case
        return
    print(n)
    buggy_countdown(n + 1)  # Goes wrong direction!

# buggy_countdown(5)  # RecursionError!
```

3. **Too many recursive calls**:
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci(1000)  # RecursionError!
```

### Python's Recursion Limit

Python has a default recursion limit (usually 1000):

```python
import sys

# Check current limit
print(sys.getrecursionlimit())  # 1000 (default)

# Increase limit (use with caution!)
sys.setrecursionlimit(5000)

# Test limit
def test_depth(n):
    if n == 0:
        return
    test_depth(n - 1)

try:
    test_depth(2000)
    print("Success!")
except RecursionError:
    print("RecursionError: maximum recursion depth exceeded")
```

**Warning**: Increasing the recursion limit doesn't add memory—it just allows deeper recursion before hitting the actual memory limit!

### Detecting Stack Overflow

```python
def safe_recursion(n):
    try:
        if n == 0:
            return 0
        return n + safe_recursion(n - 1)
    except RecursionError:
        print("Recursion limit exceeded!")
        return -1

result = safe_recursion(5000)
```

## Avoiding Stack Overflow

### 1. Use Iteration Instead

Convert recursion to loops:

```python
# Recursive (can overflow)
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

# Iterative (safe)
def sum_iterative(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum_iterative(10000))  # No problem!
```

### 2. Tail Recursion

A function is **tail recursive** if the recursive call is the last operation:

```python
# Not tail recursive (multiplication after recursive call)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # Operation after recursion

# Tail recursive (accumulator pattern)
def factorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)  # No operation after

print(factorial_tail(5))  # 120
```

**Note**: Python doesn't optimize tail recursion (unlike some languages), so this doesn't prevent stack overflow by itself.

### 3. Memoization

Cache results to avoid repeated calculations:

```python
# Naive Fibonacci (exponential time)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# Memoized Fibonacci (linear time)
def fib_memo(n, cache=None):
    if cache is None:
        cache = {}
    
    if n in cache:
        return cache[n]
    
    if n <= 1:
        return n
    
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

# Using decorator
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

print(fib_cached(100))  # Fast!
```

### 4. Increase Stack Size (Careful!)

```python
import sys
import threading

# Increase thread stack size
threading.stack_size(67108864)  # 64 MB

def deep_recursion(n):
    if n == 0:
        return 0
    return deep_recursion(n - 1) + 1

# Run in thread with larger stack
thread = threading.Thread(target=lambda: print(deep_recursion(50000)))
thread.start()
thread.join()
```

### 5. Convert to Dynamic Programming

```python
# Recursive Fibonacci (slow, can overflow)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Dynamic programming (fast, no overflow)
def fib_dp(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

print(fib_dp(1000))  # Fast and safe!
```

## Advanced Recursive Patterns

### 1. Multiple Recursive Calls

```python
def fibonacci(n):
    """Two recursive calls per function."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Tree-like recursion structure
```

### 2. Mutual Recursion

Functions calling each other:

```python
def is_even(n):
    """Check if n is even using mutual recursion."""
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    """Check if n is odd using mutual recursion."""
    if n == 0:
        return False
    return is_even(n - 1)

print(is_even(4))  # True
print(is_odd(5))   # True
```

### 3. Tree Recursion

Recursing through tree structures:

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_sum(node):
    """Sum all values in binary tree."""
    if node is None:
        return 0
    return node.value + tree_sum(node.left) + tree_sum(node.right)

# Example tree:
#     1
#    / \
#   2   3
#  / \
# 4   5

root = TreeNode(1,
    TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3)
)

print(tree_sum(root))  # 15
```

### 4. Backtracking

Try different paths and backtrack if they don't work:

```python
def find_path(maze, x, y, path=[]):
    """Find path through maze using backtracking."""
    # Check bounds and if position is valid
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return False
    if maze[x][y] == 1:  # Wall
        return False
    if (x, y) in path:  # Already visited
        return False
    
    # Add current position to path
    path.append((x, y))
    
    # Check if reached goal
    if maze[x][y] == 9:
        return True
    
    # Try all four directions
    if (find_path(maze, x + 1, y, path) or
        find_path(maze, x - 1, y, path) or
        find_path(maze, x, y + 1, path) or
        find_path(maze, x, y - 1, path)):
        return True
    
    # Backtrack
    path.pop()
    return False

maze = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 9]
]

path = []
if find_path(maze, 0, 0, path):
    print("Path found:", path)
```

### 5. Divide and Conquer

```python
def merge_sort(arr):
    """Sort array using divide and conquer."""
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer (merge)
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# [3, 9, 10, 27, 38, 43, 82]
```

## Recursion Best Practices

### 1. Always Have a Base Case

```python
# Wrong - no base case
def infinite(n):
    return infinite(n - 1)  # Never stops!

# Correct - clear base case
def countdown(n):
    if n <= 0:  # Base case
        return
    print(n)
    countdown(n - 1)
```

### 2. Ensure Progress Toward Base Case

```python
# Wrong - not progressing
def bad_factorial(n):
    if n == 0:
        return 1
    return n * bad_factorial(n)  # n doesn't change!

# Correct - making progress
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # n decreases
```

### 3. Use Meaningful Variable Names

```python
# Poor
def f(n):
    if n == 0:
        return 0
    return n + f(n - 1)

# Better
def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)
```

### 4. Consider Iteration for Simple Cases

```python
# Recursion overkill
def sum_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])

# Better - use built-in
total = sum(numbers)
```

### 5. Add Safeguards

```python
def safe_factorial(n, max_depth=100):
    """Factorial with depth limit."""
    if max_depth <= 0:
        raise RecursionError("Maximum recursion depth reached")
    if n == 0:
        return 1
    return n * safe_factorial(n - 1, max_depth - 1)
```

### 6. Document Recursive Functions

```python
def fibonacci(n):
    """
    Calculate the nth Fibonacci number recursively.
    
    Args:
        n (int): Position in Fibonacci sequence (n >= 0)
    
    Returns:
        int: The nth Fibonacci number
    
    Raises:
        ValueError: If n is negative
    
    Note:
        This implementation is inefficient for large n.
        Consider using memoization or iteration.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

## Debugging Recursive Functions

### 1. Add Print Statements

```python
def factorial(n, depth=0):
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")
    
    if n == 0:
        print(f"{indent}Base case: returning 1")
        return 1
    
    result = n * factorial(n - 1, depth + 1)
    print(f"{indent}factorial({n}) returning {result}")
    return result

factorial(4)
```

### 2. Visualize the Call Tree

```python
def visualize_recursion(func):
    """Decorator to visualize recursive calls."""
    def wrapper(n, depth=0):
        print("  " * depth + f"-> {func.__name__}({n})")
        result = func(n)
        print("  " * depth + f"<- {result}")
        return result
    return wrapper

@visualize_recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### 3. Set Breakpoints

```python
def debug_factorial(n):
    if n == 2:  # Set breakpoint condition
        import pdb; pdb.set_trace()
    
    if n == 0:
        return 1
    return n * debug_factorial(n - 1)
```

## Quick Reference

### Recursive Function Template
```python
def recursive_function(parameters):
    # Base case(s)
    if base_condition:
        return base_value
    
    # Recursive case
    # 1. Modify parameters
    # 2. Make recursive call
    # 3. Combine results
    return combine(recursive_function(modified_parameters))
```

### Common Patterns
```python
# Linear recursion
def linear(n):
    if n == 0:
        return base
    return combine(n, linear(n - 1))

# Tree recursion
def tree(n):
    if n == 0:
        return base
    return combine(tree(n-1), tree(n-2))

# Tail recursion
def tail(n, acc=initial):
    if n == 0:
        return acc
    return tail(n - 1, update(acc, n))
```

### Avoiding Stack Overflow
```python
# 1. Use iteration
for i in range(n):
    ...

# 2. Use memoization
from functools import lru_cache
@lru_cache(maxsize=None)
def func(n):
    ...

# 3. Check depth
if depth > MAX_DEPTH:
    raise RecursionError()

# 4. Increase limit (careful!)
import sys
sys.setrecursionlimit(new_limit)
```

## Summary

- **Recursion**: Function calling itself with simpler inputs
- **Base case**: Stopping condition (essential!)
- **Recursive case**: Function calling itself
- **Call stack**: Tracks all active function calls
- **Stack overflow**: Occurs when call stack grows too large
- **Python recursion limit**: Default 1000 calls
- **Avoidance strategies**: Iteration, memoization, tail recursion, dynamic programming
- **Best practices**: Clear base case, progress toward base case, add safeguards
- **When to use**: Tree structures, divide-and-conquer, naturally recursive problems
- **When not to use**: Simple loops, performance-critical code, deep recursion

Recursion is a powerful technique but requires careful implementation. Understanding the call stack and potential for stack overflow is crucial for writing correct, efficient recursive functions.
