# Direct Solvers

Direct methods for solving sparse linear systems.

## spsolve

### 1. Basic Usage

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    A = sparse.csr_matrix([[4, 1, 0],
                           [1, 4, 1],
                           [0, 1, 4]])
    b = np.array([1, 2, 1])
    
    x = splinalg.spsolve(A, b)
    
    print(f"Solution: x = {x}")
    print(f"Residual: {np.linalg.norm(A @ x - b):.2e}")

if __name__ == "__main__":
    main()
```

## splu - Sparse LU

### 1. Factor Once, Solve Multiple

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 1000
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csc')
    
    # Factor once
    lu = splinalg.splu(A)
    
    # Solve multiple systems
    for i in range(3):
        b = np.random.randn(n)
        x = lu.solve(b)
        print(f"System {i}: residual = {np.linalg.norm(A @ x - b):.2e}")

if __name__ == "__main__":
    main()
```

### 2. Fill-in Management

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 100
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csc')
    
    lu = splinalg.splu(A)
    
    print(f"Original nnz: {A.nnz}")
    print(f"L nnz: {lu.L.nnz}")
    print(f"U nnz: {lu.U.nnz}")

if __name__ == "__main__":
    main()
```

## spilu - Incomplete LU

### 1. Preconditioner

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 100
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csc')
    
    # Incomplete LU (for preconditioning)
    ilu = splinalg.spilu(A)
    
    print(f"Original nnz: {A.nnz}")
    print(f"ILU L nnz: {ilu.L.nnz}")
    print(f"ILU U nnz: {ilu.U.nnz}")

if __name__ == "__main__":
    main()
```

## Performance

### 1. Sparse vs Dense

```python
import numpy as np
from scipy import sparse, linalg
from scipy.sparse import linalg as splinalg
import time

def main():
    n = 2000
    A_sparse = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csc')
    A_dense = A_sparse.toarray()
    b = np.random.randn(n)
    
    # Dense solve
    start = time.perf_counter()
    x_dense = linalg.solve(A_dense, b)
    dense_time = time.perf_counter() - start
    
    # Sparse solve
    start = time.perf_counter()
    x_sparse = splinalg.spsolve(A_sparse, b)
    sparse_time = time.perf_counter() - start
    
    print(f"Dense solve:  {dense_time:.4f} sec")
    print(f"Sparse solve: {sparse_time:.4f} sec")
    print(f"Speedup: {dense_time/sparse_time:.1f}x")

if __name__ == "__main__":
    main()
```

## Summary

| Function | Description |
|:---------|:------------|
| `spsolve(A, b)` | Direct sparse solve |
| `splu(A)` | Sparse LU factorization |
| `spilu(A)` | Incomplete LU (preconditioner) |

Use CSC format for direct solvers.
