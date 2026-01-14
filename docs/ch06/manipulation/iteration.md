# Array Iteration

NumPy provides several ways to iterate over array elements.

## Basic For Loop

### 1. 1D Array

```python
import numpy as np

def main():
    a = np.array([1, 2, 3, 4, 5])
    
    print("Iterating over 1D array:")
    for element in a:
        print(element)

if __name__ == "__main__":
    main()
```

### 2. 2D Array

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    
    print("Iterating over 2D array (row by row):")
    for row in a:
        print(row)

if __name__ == "__main__":
    main()
```

### 3. 3D Array

```python
import numpy as np

def main():
    a = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]]])
    
    print(f"Shape: {a.shape}")
    print()
    print("Iterating over 3D array:")
    for matrix in a:
        print(matrix)
        print()

if __name__ == "__main__":
    main()
```

## Nested Loops

### 1. 2D Iteration

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 4]])
    
    print("Nested iteration over 2D array:")
    for i, row in enumerate(a):
        for j, val in enumerate(row):
            print(f"a[{i},{j}] = {val}")

if __name__ == "__main__":
    main()
```

### 2. 3D Iteration

```python
import numpy as np

def main():
    a = np.arange(8).reshape(2, 2, 2)
    
    print(f"Shape: {a.shape}")
    print()
    
    for i in a:
        for j in i:
            for k in j:
                print(k, end='\t')
    print()

if __name__ == "__main__":
    main()
```

## np.nditer

### 1. Basic Usage

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    print("Using np.nditer:")
    for x in np.nditer(a):
        print(x, end=' ')
    print()

if __name__ == "__main__":
    main()
```

### 2. Order Control

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    print("C order (row-major):")
    for x in np.nditer(a, order='C'):
        print(x, end=' ')
    print()
    
    print("F order (column-major):")
    for x in np.nditer(a, order='F'):
        print(x, end=' ')
    print()

if __name__ == "__main__":
    main()
```

### 3. Any Dimension

```python
import numpy as np

def main():
    a1 = np.array([1, 2, 3])
    a2 = np.array([[1, 2], [3, 4]])
    a3 = np.arange(8).reshape(2, 2, 2)
    
    for arr, name in [(a1, '1D'), (a2, '2D'), (a3, '3D')]:
        print(f"{name}: ", end='')
        for x in np.nditer(arr):
            print(x, end=' ')
        print()

if __name__ == "__main__":
    main()
```

## Modifying Arrays

### 1. Read-Write Mode

```python
import numpy as np

def main():
    a = np.array([1, 2, 3, 4])
    
    print(f"Before: {a}")
    
    for x in np.nditer(a, op_flags=['readwrite']):
        x[...] = x * 2
    
    print(f"After: {a}")

if __name__ == "__main__":
    main()
```

### 2. External Loop

```python
import numpy as np

def main():
    a = np.arange(12).reshape(3, 4)
    
    print("External loop (process chunks):")
    for x in np.nditer(a, flags=['external_loop'], order='C'):
        print(x)

if __name__ == "__main__":
    main()
```

## np.ndenumerate

### 1. Index and Value

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 4]])
    
    print("Using np.ndenumerate:")
    for idx, val in np.ndenumerate(a):
        print(f"Index {idx}: value {val}")

if __name__ == "__main__":
    main()
```

### 2. 3D Array

```python
import numpy as np

def main():
    a = np.arange(8).reshape(2, 2, 2)
    
    print("3D array enumeration:")
    for idx, val in np.ndenumerate(a):
        print(f"{idx}: {val}")

if __name__ == "__main__":
    main()
```

### 3. Conditional Processing

```python
import numpy as np

def main():
    a = np.array([[1, 5, 3],
                  [7, 2, 8],
                  [4, 6, 9]])
    
    print("Elements greater than 5:")
    for idx, val in np.ndenumerate(a):
        if val > 5:
            print(f"a{list(idx)} = {val}")

if __name__ == "__main__":
    main()
```

## np.ndindex

### 1. Generate Indices

```python
import numpy as np

def main():
    for idx in np.ndindex(2, 3):
        print(idx)

if __name__ == "__main__":
    main()
```

### 2. Use with Array

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    print("Using ndindex:")
    for idx in np.ndindex(a.shape):
        print(f"a{list(idx)} = {a[idx]}")

if __name__ == "__main__":
    main()
```

## flat Iterator

### 1. Using .flat

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    print("Using .flat iterator:")
    for x in a.flat:
        print(x, end=' ')
    print()

if __name__ == "__main__":
    main()
```

### 2. Indexing with flat

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    print(f"a.flat[0] = {a.flat[0]}")
    print(f"a.flat[3] = {a.flat[3]}")
    print(f"a.flat[-1] = {a.flat[-1]}")

if __name__ == "__main__":
    main()
```

## Performance

### 1. Loop vs Vectorized

```python
import numpy as np
import time

def main():
    a = np.random.randn(1000, 1000)
    
    # Loop (slow)
    start = time.perf_counter()
    result1 = np.empty_like(a)
    for idx, val in np.ndenumerate(a):
        result1[idx] = val ** 2
    loop_time = time.perf_counter() - start
    
    # Vectorized (fast)
    start = time.perf_counter()
    result2 = a ** 2
    vec_time = time.perf_counter() - start
    
    print(f"Loop time: {loop_time:.4f} sec")
    print(f"Vectorized: {vec_time:.6f} sec")
    print(f"Speedup: {loop_time/vec_time:.0f}x")

if __name__ == "__main__":
    main()
```

### 2. When to Use Loops

- Complex conditional logic
- Element depends on previous elements
- Debugging and prototyping

### 3. Prefer Vectorization

For performance, always prefer vectorized operations.

## Summary Table

### 1. Iteration Methods

| Method | Description |
|:-------|:------------|
| `for x in a` | Iterate over first axis |
| `np.nditer(a)` | Flat iteration, any shape |
| `np.ndenumerate(a)` | (index, value) pairs |
| `np.ndindex(shape)` | Generate all indices |
| `a.flat` | Flat iterator attribute |

### 2. nditer Flags

| Flag | Description |
|:-----|:------------|
| `'readwrite'` | Can modify elements |
| `'external_loop'` | Yield chunks |
| `order='C'` | Row-major order |
| `order='F'` | Column-major order |
