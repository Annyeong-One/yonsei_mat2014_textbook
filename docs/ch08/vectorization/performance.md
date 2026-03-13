# Performance vs Loops

Vectorization is the single most important performance concept in NumPy.

## Python Loop Cost

### 1. Loop Overhead

A pure Python loop incurs significant overhead.

```python
import numpy as np

def add_with_loop(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i] + b[i])
    return res
```

### 2. Sources of Slowdown

Each iteration involves:

- Interpreter overhead
- Repeated attribute lookups
- Python object creation
- Type checking

### 3. Accumulating Cost

For large arrays, these costs multiply dramatically.

## Vectorized NumPy

### 1. Single Expression

```python
import numpy as np

def add_vectorized(a, b):
    return a + b
```

### 2. Under the Hood

This executes:

- In optimized C loops
- With contiguous memory access
- Without Python-level iteration

### 3. Hardware Benefits

Vectorized code can leverage:

- CPU cache prefetching
- SIMD instructions
- Memory locality

## Speedup Magnitude

### 1. Typical Speedups

Vectorization typically provides:

- 10×–100× faster for small arrays
- 100×–1000× faster for large arrays

### 2. Array Size Effect

```python
import numpy as np
import time

def main():
    for n in [1_000, 100_000, 10_000_000]:
        a = np.random.randn(n)
        
        # Loop
        start = time.perf_counter()
        result = [x ** 2 for x in a]
        loop_time = time.perf_counter() - start
        
        # Vectorized
        start = time.perf_counter()
        result = a ** 2
        vec_time = time.perf_counter() - start
        
        print(f"n={n:>10}: {loop_time/vec_time:>6.0f}x speedup")

if __name__ == "__main__":
    main()
```

### 3. Why Essential

This is why NumPy is essential for numerical work.

## Memory Tradeoffs

### 1. Temporary Arrays

Vectorization may allocate temporary arrays.

```python
import numpy as np

# Creates temporary for (a + b) before multiplying
result = (a + b) * c
```

### 2. Peak Memory

Large operations increase peak memory usage.

### 3. In-Place Operations

Use in-place operations when appropriate:

```python
import numpy as np

def main():
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([4.0, 5.0, 6.0])
    
    a += b  # Modifies a in place
    print(a)

if __name__ == "__main__":
    main()
```

## Practical Guidance

### 1. Avoid Python Loops

Never loop over array elements when vectorization is possible.

### 2. Think in Arrays

Reformulate problems as array operations.

### 3. Profile First

Measure before micro-optimizing.

```python
import numpy as np
import time

def main():
    arr = np.random.randn(1_000_000)
    
    start = time.perf_counter()
    result = np.sum(arr ** 2)
    elapsed = time.perf_counter() - start
    
    print(f"Time: {elapsed:.6f} sec")

if __name__ == "__main__":
    main()
```
