# Tree Recursion


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Tree recursion occurs when a function calls itself multiple times per invocation, creating a tree-like call pattern. This is common in problems with overlapping subproblems.

---

## Fibonacci: Classic Tree Recursion

```python
def fibonacci(n):
    '''Fibonacci sequence using naive recursion'''
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example calls
print(fibonacci(5))   # Output: 5
print(fibonacci(6))   # Output: 8
```

The call tree for `fibonacci(5)`:
```
                fibonacci(5)
              /            \
        fibonacci(4)      fibonacci(3)
        /      \          /      \
    fib(3)  fib(2)    fib(2)  fib(1)
    /  \    / \      / \
fib(2) fib(1) fib(1) fib(0) ...
```

Notice `fibonacci(3)` and `fibonacci(2)` are computed multiple times!

## Counting Recursive Calls

```python
def fibonacci_counted(n, call_count=None):
    '''Fibonacci with call counter'''
    if call_count is None:
        call_count = {'count': 0}
    
    call_count['count'] += 1
    
    if n <= 1:
        return n
    return fibonacci_counted(n - 1, call_count) + fibonacci_counted(n - 2, call_count)

# Count calls for different inputs
for n in [5, 10, 15, 20]:
    call_count = {'count': 0}
    fibonacci_counted(n, call_count)
    print(f"fib({n:2d}): {call_count['count']:6d} calls")
```

Output:
```
fib( 5):     15 calls
fib(10):    177 calls
fib(15):   1973 calls
fib(20):  21891 calls
```

## Binary Search Tree Traversal

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse_tree(node, result=None):
    '''In-order tree traversal'''
    if result is None:
        result = []
    
    if node is None:
        return result
    
    traverse_tree(node.left, result)
    result.append(node.value)
    traverse_tree(node.right, result)
    
    return result

# Build and traverse
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(traverse_tree(root))  # [1, 2, 3, 4, 6]
```

## Performance Comparison

The exponential nature of tree recursion means small input size changes cause huge performance differences. Use memoization (chapter on memoization) to fix this.
