# Matrix Multiplication

NumPy provides multiple ways to perform matrix multiplication.

## The @ Operator

### 1. Basic Usage

```python
import numpy as np

def main():
    A = np.array([[1, 2],
                  [3, 4]])
    B = np.array([[5, 6],
                  [7, 8]])
    
    C = A @ B
    
    print("A @ B =")
    print(C)

if __name__ == "__main__":
    main()
```

**Output:**

```
A @ B =
[[19 22]
 [43 50]]
```

### 2. Mathematical Form

$$C_{ij} = \sum_k A_{ik} B_{kj}$$

### 3. Shape Requirements

Inner dimensions must match: `(m, n) @ (n, p) -> (m, p)`.

```python
import numpy as np

def main():
    A = np.random.randn(3, 4)
    B = np.random.randn(4, 5)
    
    C = A @ B
    
    print(f"A shape: {A.shape}")
    print(f"B shape: {B.shape}")
    print(f"C shape: {C.shape}")

if __name__ == "__main__":
    main()
```

## np.matmul

### 1. Equivalent to @

```python
import numpy as np

def main():
    A = np.array([[1, 2],
                  [3, 4]])
    B = np.array([[5, 6],
                  [7, 8]])
    
    C1 = A @ B
    C2 = np.matmul(A, B)
    
    print(f"Results equal: {np.array_equal(C1, C2)}")

if __name__ == "__main__":
    main()
```

### 2. Batch Multiplication

Both `@` and `np.matmul` support batch dimensions.

```python
import numpy as np

def main():
    # Batch of 10 matrices
    A = np.random.randn(10, 3, 4)
    B = np.random.randn(10, 4, 5)
    
    C = A @ B  # or np.matmul(A, B)
    
    print(f"A shape: {A.shape}")
    print(f"B shape: {B.shape}")
    print(f"C shape: {C.shape}")

if __name__ == "__main__":
    main()
```

### 3. Broadcasting

```python
import numpy as np

def main():
    # Single matrix times batch
    A = np.random.randn(3, 4)
    B = np.random.randn(10, 4, 5)
    
    C = A @ B
    
    print(f"A shape: {A.shape}")
    print(f"B shape: {B.shape}")
    print(f"C shape: {C.shape}")

if __name__ == "__main__":
    main()
```

## np.dot

### 1. Vector Dot Product

```python
import numpy as np

def main():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    
    dot = np.dot(a, b)
    
    print(f"a · b = {dot}")
    print(f"Manual: {1*4 + 2*5 + 3*6}")

if __name__ == "__main__":
    main()
```

### 2. Matrix Multiplication

```python
import numpy as np

def main():
    A = np.array([[1, 2],
                  [3, 4]])
    B = np.array([[5, 6],
                  [7, 8]])
    
    C = np.dot(A, B)
    
    print("np.dot(A, B) =")
    print(C)

if __name__ == "__main__":
    main()
```

### 3. Difference from @

`np.dot` and `@` differ for higher-dimensional arrays.

```python
import numpy as np

def main():
    A = np.random.randn(2, 3, 4)
    B = np.random.randn(2, 4, 5)
    
    # @ treats as batch matmul
    C_matmul = A @ B
    print(f"A @ B shape: {C_matmul.shape}")
    
    # np.dot sums over last axis of A and second-to-last of B
    # Result shape differs!

if __name__ == "__main__":
    main()
```

## Matrix-Vector Product

### 1. Ax = b Style

```python
import numpy as np

def main():
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    x = np.array([1, 2, 3])
    
    b = A @ x
    
    print(f"A shape: {A.shape}")
    print(f"x shape: {x.shape}")
    print(f"b shape: {b.shape}")
    print(f"b = {b}")

if __name__ == "__main__":
    main()
```

### 2. Row Vector

```python
import numpy as np

def main():
    x = np.array([1, 2])
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    b = x @ A
    
    print(f"x shape: {x.shape}")
    print(f"A shape: {A.shape}")
    print(f"b shape: {b.shape}")
    print(f"b = {b}")

if __name__ == "__main__":
    main()
```

### 3. Explicit Shapes

```python
import numpy as np

def main():
    A = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])
    x = np.array([[1],
                  [2]])  # Column vector
    
    b = A @ x
    
    print(f"A shape: {A.shape}")
    print(f"x shape: {x.shape}")
    print(f"b shape: {b.shape}")
    print("b =")
    print(b)

if __name__ == "__main__":
    main()
```

## Performance

### 1. BLAS Backend

NumPy uses optimized BLAS libraries (OpenBLAS, MKL).

```python
import numpy as np

def main():
    print(np.show_config())

if __name__ == "__main__":
    main()
```

### 2. Large Matrix Timing

```python
import numpy as np
import time

def main():
    n = 1000
    A = np.random.randn(n, n)
    B = np.random.randn(n, n)
    
    start = time.perf_counter()
    C = A @ B
    elapsed = time.perf_counter() - start
    
    print(f"Matrix size: {n}x{n}")
    print(f"Time: {elapsed:.4f} sec")
    print(f"GFLOPS: {2*n**3/elapsed/1e9:.1f}")

if __name__ == "__main__":
    main()
```

### 3. Contiguous Memory

Ensure arrays are contiguous for best performance.

```python
import numpy as np
import time

def main():
    n = 1000
    A = np.random.randn(n, n)
    
    # Contiguous
    B = np.ascontiguousarray(A.T)
    
    start = time.perf_counter()
    C = B @ B
    t1 = time.perf_counter() - start
    
    # Non-contiguous (transposed view)
    start = time.perf_counter()
    C = A.T @ A.T
    t2 = time.perf_counter() - start
    
    print(f"Contiguous:     {t1:.4f} sec")
    print(f"Non-contiguous: {t2:.4f} sec")

if __name__ == "__main__":
    main()
```

## Best Practices

### 1. Use @ Operator

Prefer `@` for readability; it's equivalent to `np.matmul`.

### 2. Check Shapes

Verify shapes before multiplication to avoid broadcasting surprises.

### 3. Batch Operations

Use batch matmul instead of loops for multiple matrix multiplications.
