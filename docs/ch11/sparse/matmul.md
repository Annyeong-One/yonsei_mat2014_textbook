# Matrix Multiplication

Sparse matrix-matrix multiplication and its considerations.

## Sparse @ Sparse

### 1. Basic Usage

```python
from scipy import sparse

def main():
    A = sparse.csr_matrix([[1, 0], [0, 2]])
    B = sparse.csr_matrix([[1, 2], [3, 4]])
    
    C = A @ B
    
    print("A @ B =")
    print(C.toarray())
    print(f"Result type: {type(C)}")

if __name__ == "__main__":
    main()
```

### 2. Using .dot()

```python
from scipy import sparse

def main():
    A = sparse.csr_matrix([[1, 2], [3, 4]])
    B = sparse.csr_matrix([[5, 6], [7, 8]])
    
    C = A.dot(B)
    
    print("A.dot(B) =")
    print(C.toarray())

if __name__ == "__main__":
    main()
```

## Fill-in

### 1. Sparsity Can Decrease

```python
from scipy import sparse

def main():
    n = 100
    A = sparse.random(n, n, density=0.1, format='csr')
    B = sparse.random(n, n, density=0.1, format='csr')
    
    C = A @ B
    
    print(f"A density: {A.nnz / n**2:.2%}")
    print(f"B density: {B.nnz / n**2:.2%}")
    print(f"C = A@B density: {C.nnz / n**2:.2%}")

if __name__ == "__main__":
    main()
```

### 2. Structured Sparsity

```python
from scipy import sparse

def main():
    # Banded matrices preserve structure better
    n = 100
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csr')
    
    C = A @ A
    
    print(f"A bandwidth: 1")
    print(f"A@A bandwidth: {max(abs(C.nonzero()[0] - C.nonzero()[1]))}")

if __name__ == "__main__":
    main()
```

## Sparse @ Dense

### 1. Matrix-Matrix

```python
import numpy as np
from scipy import sparse

def main():
    A = sparse.csr_matrix([[1, 0], [0, 2]])
    B = np.array([[1, 2], [3, 4]])
    
    C = A @ B  # Result is dense
    
    print("Sparse @ Dense =")
    print(C)
    print(f"Result type: {type(C)}")

if __name__ == "__main__":
    main()
```

## Performance Tips

### 1. CSR for Row-based Multiply

```python
from scipy import sparse
import time

def main():
    n = 1000
    A_csr = sparse.random(n, n, density=0.01, format='csr')
    A_csc = A_csr.tocsc()
    B = sparse.random(n, n, density=0.01, format='csr')
    
    # CSR @ CSR
    start = time.perf_counter()
    C = A_csr @ B
    csr_time = time.perf_counter() - start
    
    # CSC @ CSR
    start = time.perf_counter()
    C = A_csc @ B
    csc_time = time.perf_counter() - start
    
    print(f"CSR @ CSR: {csr_time:.4f} sec")
    print(f"CSC @ CSR: {csc_time:.4f} sec")

if __name__ == "__main__":
    main()
```

## Summary

- `A @ B` returns sparse if both sparse
- Fill-in can increase density of result
- Use CSR format for efficient multiplication
- Result density depends on sparsity patterns
