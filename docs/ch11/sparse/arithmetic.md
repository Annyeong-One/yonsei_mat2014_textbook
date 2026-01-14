# Arithmetic Operations

Sparse matrices support efficient arithmetic operations.

## Addition and Subtraction

### 1. Sparse + Sparse

```python
from scipy import sparse

def main():
    A = sparse.csr_matrix([[1, 0], [0, 2]])
    B = sparse.csr_matrix([[0, 3], [4, 0]])
    
    C = A + B
    
    print("A + B =")
    print(C.toarray())

if __name__ == "__main__":
    main()
```

### 2. Sparse + Scalar

```python
from scipy import sparse

def main():
    A = sparse.csr_matrix([[1, 0], [0, 2]])
    
    # Note: adds to ALL entries (converts to dense pattern)
    B = A + 1
    
    print("A + 1 =")
    print(B.toarray())

if __name__ == "__main__":
    main()
```

## Scalar Multiplication

### 1. Scale Matrix

```python
from scipy import sparse

def main():
    A = sparse.csr_matrix([[1, 0, 2], [0, 3, 0]])
    
    B = 2 * A
    C = A * 0.5
    
    print("2 * A =")
    print(B.toarray())

if __name__ == "__main__":
    main()
```

## Matrix-Vector Product

### 1. Sparse @ Dense

```python
import numpy as np
from scipy import sparse

def main():
    A = sparse.csr_matrix([[1, 0, 2],
                           [0, 3, 0],
                           [4, 0, 5]])
    x = np.array([1, 2, 3])
    
    y = A @ x
    
    print(f"A @ x = {y}")

if __name__ == "__main__":
    main()
```

### 2. Performance

```python
import numpy as np
from scipy import sparse
import time

def main():
    n = 10000
    A = sparse.random(n, n, density=0.001, format='csr')
    x = np.random.randn(n)
    
    start = time.perf_counter()
    for _ in range(100):
        y = A @ x
    elapsed = time.perf_counter() - start
    
    print(f"100 sparse matvecs: {elapsed:.4f} sec")

if __name__ == "__main__":
    main()
```

## Element-wise Operations

### 1. Hadamard Product

```python
from scipy import sparse

def main():
    A = sparse.csr_matrix([[1, 2], [3, 4]])
    B = sparse.csr_matrix([[1, 0], [0, 1]])
    
    # Element-wise multiplication
    C = A.multiply(B)
    
    print("A ⊙ B =")
    print(C.toarray())

if __name__ == "__main__":
    main()
```

### 2. Power

```python
from scipy import sparse

def main():
    A = sparse.csr_matrix([[1, 2], [3, 4]])
    
    # Element-wise power
    B = A.power(2)
    
    print("A.^2 =")
    print(B.toarray())

if __name__ == "__main__":
    main()
```

## Summary

| Operation | Method | Preserves Sparsity |
|:----------|:-------|:-------------------|
| A + B | `A + B` | Yes |
| A + scalar | `A + c` | No (fills matrix) |
| c * A | `c * A` | Yes |
| A @ x | `A @ x` | N/A (returns dense) |
| A ⊙ B | `A.multiply(B)` | Yes |
