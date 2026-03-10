# Optimization Strategies


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Strategic code optimization requires identifying bottlenecks and applying targeted improvements. Here are proven techniques.

---

## Algorithmic Optimization

Always start with algorithm improvement for the biggest gains:

```python
# O(n²) - Inefficient
def find_duplicates_slow(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.append(numbers[i])
    return list(set(duplicates))

# O(n) - Efficient
def find_duplicates_fast(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return duplicates
```

## Built-in Functions vs. Loops

```python
# Slow: Python loop
def sum_squares_slow(numbers):
    total = 0
    for n in numbers:
        total += n ** 2
    return total

# Fast: Built-in function
def sum_squares_fast(numbers):
    return sum(n ** 2 for n in numbers)

# Fastest: NumPy for large data
import numpy as np
def sum_squares_numpy(numbers):
    return np.sum(np.array(numbers) ** 2)
```

## Caching and Memoization

```python
from functools import lru_cache

# Without caching: O(2^n)
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

# With caching: O(n)
@lru_cache(maxsize=None)
def fib_fast(n):
    if n <= 1:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)
```

## String Operations

```python
# Slow: String concatenation in loop
result = ""
for i in range(1000):
    result += f"Item {i}
"

# Fast: Use join
result = "
".join(f"Item {i}" for i in range(1000))

# Also fast: StringIO for multiple operations
from io import StringIO
output = StringIO()
for i in range(1000):
    output.write(f"Item {i}
")
result = output.getvalue()
```

## Optimization Checklist

- Profile first to identify bottlenecks
- Improve algorithm complexity before micro-optimizations
- Use built-in functions (they're written in C)
- Avoid repeated attribute lookups
- Consider data structure choice (list vs. set vs. dict)
- Use generators for large datasets
- Cache expensive computations
- Consider NumPy/Pandas for numerical work
