# Memory Preallocation

Preallocate arrays before iterative population to avoid dynamic allocation overhead.


## The Problem

Dynamic allocation in loops causes catastrophic inefficiency.

### 1. Bad Pattern

```python
import numpy as np

def build_array_bad(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return np.array(result)
```

### 2. Why It's Slow

- Each `append` may trigger reallocation
- Memory fragmentation increases
- Type conversion at the end adds overhead

### 3. Hidden Cost

Python lists store pointers, not contiguous data.


## Preallocation Solution

Allocate the full array before the loop.

### 1. Good Pattern

```python
import numpy as np

def build_array_good(n):
    result = np.empty(n, dtype=np.float64)
    for i in range(n):
        result[i] = i ** 2
    return result
```

### 2. Why It's Fast

- Single allocation upfront
- Contiguous memory access
- No type conversion needed

### 3. Best Pattern

```python
import numpy as np

def build_array_best(n):
    return np.arange(n) ** 2  # Fully vectorized
```


## Timing Comparison

Measure the performance difference.

### 1. Benchmark Code

```python
import numpy as np
import time

def with_append(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return np.array(result)

def with_prealloc(n):
    result = np.empty(n, dtype=np.int64)
    for i in range(n):
        result[i] = i ** 2
    return result

def main():
    n = 100_000
    
    start = time.perf_counter()
    _ = with_append(n)
    append_time = time.perf_counter() - start
    
    start = time.perf_counter()
    _ = with_prealloc(n)
    prealloc_time = time.perf_counter() - start
    
    print(f"Append time:     {append_time:.4f} sec")
    print(f"Prealloc time:   {prealloc_time:.4f} sec")
    print(f"Speedup:         {append_time / prealloc_time:.1f}x")

if __name__ == "__main__":
    main()
```

### 2. Typical Results

```
Append time:     0.0450 sec
Prealloc time:   0.0120 sec
Speedup:         3.8x
```


## Allocation Functions

Choose the right function for preallocation.

### 1. np.empty

```python
import numpy as np

arr = np.empty((1000, 1000))  # Fastest, uninitialized
```

No initialization; use when you'll overwrite all values.

### 2. np.zeros

```python
import numpy as np

arr = np.zeros((1000, 1000))  # Initialized to zero
```

Safe default when partial filling is possible.

### 3. np.empty_like

```python
import numpy as np

template = np.random.randn(100, 100)
arr = np.empty_like(template)  # Match shape and dtype
```


## 2D Preallocation

Apply preallocation to multi-dimensional arrays.

### 1. Matrix Building

```python
import numpy as np

def build_matrix(rows, cols):
    result = np.empty((rows, cols), dtype=np.float64)
    for i in range(rows):
        for j in range(cols):
            result[i, j] = i * cols + j
    return result
```

### 2. Row-wise Building

```python
import numpy as np

def build_by_rows(rows, cols):
    result = np.empty((rows, cols), dtype=np.float64)
    for i in range(rows):
        result[i, :] = np.arange(cols) + i * cols
    return result
```

### 3. Fully Vectorized

```python
import numpy as np

def build_vectorized(rows, cols):
    return np.arange(rows * cols).reshape(rows, cols)
```


## Best Practices

Guidelines for effective preallocation.

### 1. Know Final Size

Preallocation requires knowing dimensions upfront.

### 2. Specify dtype

Always specify dtype to avoid implicit conversions.

### 3. Prefer Vectorization

Preallocation helps loops, but vectorization eliminates them.
