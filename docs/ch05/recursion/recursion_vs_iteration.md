# Recursion vs Iteration

Both recursion and iteration solve repetitive problems, but they differ in clarity, efficiency, and use cases. Understanding trade-offs helps you choose correctly.

---

## Sum Calculation: Both Approaches

```python
# Recursive: Natural for mathematical definitions
def sum_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])

# Iterative: More memory-efficient
def sum_iterative(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print(sum_recursive(numbers))   # 15
print(sum_iterative(numbers))   # 15
```

## Factorial Comparison

```python
# Recursive: Elegant, matches mathematical notation
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative: More predictable performance
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_recursive(5))   # 120
print(factorial_iterative(5))   # 120
```

## Tree Traversal: Recursion's Strength

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

# Recursive: Simple and clear
def count_nodes_recursive(node):
    count = 1
    for child in node.children:
        count += count_nodes_recursive(child)
    return count

# Iterative: Requires stack data structure
def count_nodes_iterative(root):
    count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        count += 1
        stack.extend(node.children)
    return count
```

## Performance and Memory

```python
import sys

# Check stack depth limit
print(f"Recursion limit: {sys.getrecursionlimit()}")

# Iterative uses constant stack space
# Recursive uses O(n) stack space

# For large n, iteration is safer
def large_sum_iterative(n):
    return sum(range(n))

def large_sum_recursive(n):
    if n <= 0:
        return 0
    return n + large_sum_recursive(n - 1)
```

## When to Use Each

**Use Recursion for:**
- Tree/graph traversal
- Divide-and-conquer algorithms
- Mathematical problem definitions
- When code clarity is priority

**Use Iteration for:**
- Simple loops (for, while)
- Processing sequences
- When memory/stack is limited
- Performance-critical code
