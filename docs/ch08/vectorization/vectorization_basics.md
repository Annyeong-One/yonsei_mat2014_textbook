# Vectorization Basics


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Vectorization replaces explicit loops with bulk array operations optimized in C.


## Core Principle

Suppress Python-level loops for orders-of-magnitude speedup.

### 1. Loop Approach

```python
import numpy as np

def square_with_loop(arr):
    result = np.empty_like(arr)
    for i in range(len(arr)):
        result[i] = arr[i] ** 2
    return result
```

### 2. Vectorized Approach

```python
import numpy as np

def square_vectorized(arr):
    return arr ** 2
```

### 3. Key Difference

Vectorized code executes in optimized C; loops execute in slow Python.


## Performance Gain

Vectorization yields dramatic speedups.

### 1. Timing Comparison

```python
import numpy as np
import time

def main():
    arr = np.random.randn(1_000_000)
    
    # Loop timing
    start = time.perf_counter()
    result_loop = np.empty_like(arr)
    for i in range(len(arr)):
        result_loop[i] = arr[i] ** 2
    loop_time = time.perf_counter() - start
    
    # Vectorized timing
    start = time.perf_counter()
    result_vec = arr ** 2
    vec_time = time.perf_counter() - start
    
    print(f"Loop time:       {loop_time:.4f} sec")
    print(f"Vectorized time: {vec_time:.6f} sec")
    print(f"Speedup:         {loop_time / vec_time:.0f}x")

if __name__ == "__main__":
    main()
```

### 2. Typical Results

```
Loop time:       0.3200 sec
Vectorized time: 0.001500 sec
Speedup:         213x
```

### 3. Scale Matters

Speedup increases with array size.


## Common Patterns

Recognize loop patterns that can be vectorized.

### 1. Element-wise Math

```python
import numpy as np

# Loop
for i in range(len(arr)):
    result[i] = np.sin(arr[i])

# Vectorized
result = np.sin(arr)
```

### 2. Conditional Logic

```python
import numpy as np

# Loop
for i in range(len(arr)):
    if arr[i] > 0:
        result[i] = arr[i]
    else:
        result[i] = 0

# Vectorized
result = np.where(arr > 0, arr, 0)
```

### 3. Aggregation

```python
import numpy as np

# Loop
total = 0
for i in range(len(arr)):
    total += arr[i]

# Vectorized
total = np.sum(arr)
```


## Universal Functions

NumPy ufuncs are inherently vectorized.

### 1. Math Functions

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(np.sqrt(arr))   # [1.  1.41 1.73 2.]
print(np.exp(arr))    # [2.71 7.38 20.08 54.59]
print(np.log(arr))    # [0.  0.69 1.09 1.38]
```

### 2. Comparison Functions

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([2, 2, 2])
print(np.maximum(a, b))  # [2 2 3]
print(np.minimum(a, b))  # [1 2 2]
```

### 3. Custom ufuncs

Use `np.vectorize` for custom functions (convenience, not performance).


## When Loops Are OK

Some situations still require explicit loops.

### 1. Sequential Dependence

When iteration `i` depends on result of `i-1`.

### 2. Complex Logic

When vectorization would be unreadable or impossible.

### 3. Small Arrays

Overhead matters less for tiny arrays.
