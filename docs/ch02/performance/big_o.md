# Big-O Notation

Big-O notation describes how algorithm performance scales with input size. Understanding Big-O is essential for choosing algorithms and data structures that perform well at scale.

---

## Common Complexities

### Comparing Orders of Growth

```python
def demonstrate_complexity():
    def constant(n):
        return n
    
    def linear(n):
        total = 0
        for i in range(n):
            total += i
        return total
    
    def quadratic(n):
        total = 0
        for i in range(n):
            for j in range(n):
                total += 1
        return total
    
    n = 1000
    
    print(f"O(1): {constant(n)}")
    print(f"O(n): {linear(n)}")
    print(f"O(n²): {quadratic(100)}")

demonstrate_complexity()
```

Output:
```
O(1): 1000
O(n): 499500
O(n²): 10000
```

## Analysis Examples

### Linear Search vs Binary Search

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

data = list(range(1000000))

print(f"Linear: {linear_search(data, 999999)}")
print(f"Binary: {binary_search(data, 999999)}")
```

Output:
```
Linear: 999999
Binary: 999999
```

## Space Complexity

### Memory Usage Patterns

```python
def space_o1():
    x = 10
    return x * 2

def space_on(n):
    lst = list(range(n))
    return sum(lst)

def space_on_sq(n):
    matrix = [[0] * n for _ in range(n)]
    return matrix

space_o1()
space_on(1000)

matrix = space_on_sq(100)
print(f"Matrix created: {len(matrix)}x{len(matrix[0])}")
```

Output:
```
Matrix created: 100x100
```

## Practical Guidelines

### Choosing Algorithms

```python
import timeit

small_n = 100

setup_small = "arr = list(range(100)); target = 50"
linear_time = timeit.timeit("target in arr", setup=setup_small, number=10000)

print(f"Search time for small data: {linear_time:.6f}s")
print("For large data, use binary search or hash tables (O(1) lookup)")
```

Output:
```
Search time for small data: 0.000123s
For large data, use binary search or hash tables (O(1) lookup)
```
