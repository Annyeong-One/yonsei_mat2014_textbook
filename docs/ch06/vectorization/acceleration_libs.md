# Acceleration Libraries

External libraries provide additional speedups beyond pure NumPy.


## numexpr

Optimized evaluation of array expressions.

### 1. Installation

```bash
pip install numexpr
```

### 2. Basic Usage

```python
import numpy as np
import numexpr as ne

def main():
    a = np.random.randn(1_000_000)
    b = np.random.randn(1_000_000)
    
    # NumPy (creates temporaries)
    result_np = 2 * a + 3 * b ** 2
    
    # numexpr (avoids temporaries)
    result_ne = ne.evaluate("2 * a + 3 * b ** 2")

if __name__ == "__main__":
    main()
```

### 3. Why It's Faster

- Avoids intermediate array allocations
- Uses multiple CPU cores automatically
- Optimizes memory access patterns


## numexpr Benchmark

Compare numexpr vs pure NumPy.

### 1. Timing Code

```python
import numpy as np
import numexpr as ne
import time

def main():
    n = 10_000_000
    a = np.random.randn(n)
    b = np.random.randn(n)
    
    # NumPy timing
    start = time.perf_counter()
    for _ in range(10):
        result = 2 * a + 3 * b ** 2
    np_time = time.perf_counter() - start
    
    # numexpr timing
    start = time.perf_counter()
    for _ in range(10):
        result = ne.evaluate("2 * a + 3 * b ** 2")
    ne_time = time.perf_counter() - start
    
    print(f"NumPy time:   {np_time:.4f} sec")
    print(f"numexpr time: {ne_time:.4f} sec")
    print(f"Speedup:      {np_time/ne_time:.1f}x")

if __name__ == "__main__":
    main()
```

### 2. Typical Speedup

2-10x faster for complex expressions with large arrays.


## Numba

Just-in-time compilation for Python functions.

### 1. Installation

```bash
pip install numba
```

### 2. Basic JIT

```python
import numpy as np
from numba import jit

@jit(nopython=True)
def sum_squares(arr):
    total = 0.0
    for i in range(len(arr)):
        total += arr[i] ** 2
    return total

def main():
    arr = np.random.randn(1_000_000)
    result = sum_squares(arr)  # First call compiles
    result = sum_squares(arr)  # Subsequent calls fast

if __name__ == "__main__":
    main()
```

### 3. nopython Mode

`nopython=True` ensures full compilation without Python fallback.


## Numba Parallel

Automatic parallelization with Numba.

### 1. Parallel Loop

```python
import numpy as np
from numba import jit, prange

@jit(nopython=True, parallel=True)
def parallel_sum(arr):
    total = 0.0
    for i in prange(len(arr)):
        total += arr[i] ** 2
    return total

def main():
    arr = np.random.randn(10_000_000)
    result = parallel_sum(arr)

if __name__ == "__main__":
    main()
```

### 2. prange

Use `prange` instead of `range` for parallel iteration.

### 3. Multi-core Speedup

Automatically distributes work across CPU cores.


## Cython

Static typing and C compilation for Python code.

### 1. Installation

```bash
pip install cython
```

### 2. Cython File (.pyx)

```cython
# sum_squares.pyx
import numpy as np
cimport numpy as np

def sum_squares_cy(np.ndarray[np.float64_t, ndim=1] arr):
    cdef double total = 0.0
    cdef int i
    cdef int n = arr.shape[0]
    
    for i in range(n):
        total += arr[i] ** 2
    
    return total
```

### 3. Compilation

Requires setup.py or build configuration to compile.


## Comparison Table

Choose the right tool for your needs.

### 1. Summary

| Library | Use Case | Speedup | Complexity |
|:--------|:---------|:--------|:-----------|
| numexpr | Array expressions | 2-10x | Low |
| Numba | Numerical loops | 10-100x | Medium |
| Cython | General Python | 10-100x | High |

### 2. Quick Wins

Use numexpr for immediate gains with minimal code changes.

### 3. Maximum Speed

Use Numba or Cython when loops cannot be vectorized.


## Best Practices

Guidelines for using acceleration libraries.

### 1. Profile First

Identify bottlenecks before adding dependencies.

### 2. Start Simple

Try numexpr before Numba; try Numba before Cython.

### 3. Test Correctness

Verify results match original implementation.
