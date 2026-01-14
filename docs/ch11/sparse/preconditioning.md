# Preconditioning

Preconditioners accelerate iterative solver convergence.

## Why Precondition

### 1. Condition Number Effect

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 500
    # Ill-conditioned system
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csr')
    A = A + sparse.diags([0.01], [n//2], shape=(n, n))
    b = np.ones(n)
    
    # Without preconditioning
    x1, info1 = splinalg.cg(A, b, maxiter=1000)
    
    # With ILU preconditioning
    M = splinalg.spilu(A.tocsc())
    M_op = splinalg.LinearOperator(A.shape, M.solve)
    x2, info2 = splinalg.cg(A, b, M=M_op, maxiter=1000)
    
    print(f"Without precond: info={info1}")
    print(f"With ILU precond: info={info2}")

if __name__ == "__main__":
    main()
```

## ILU Preconditioner

### 1. Incomplete LU

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 1000
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csc')
    b = np.ones(n)
    
    # Create ILU preconditioner
    ilu = splinalg.spilu(A)
    M = splinalg.LinearOperator(A.shape, ilu.solve)
    
    # Solve with preconditioning
    x, info = splinalg.cg(A.tocsr(), b, M=M)
    
    print(f"Residual: {np.linalg.norm(A @ x - b):.2e}")

if __name__ == "__main__":
    main()
```

## Diagonal Preconditioner

### 1. Jacobi Preconditioner

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 500
    A = sparse.diags([-1, 4, -1], [-1, 0, 1], shape=(n, n), format='csr')
    b = np.ones(n)
    
    # Jacobi: M = diag(A)
    diag_A = A.diagonal()
    M = splinalg.LinearOperator(A.shape, lambda x: x / diag_A)
    
    x, info = splinalg.cg(A, b, M=M)
    
    print(f"Converged: {info == 0}")

if __name__ == "__main__":
    main()
```

## Performance Comparison

### 1. Iteration Count

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 1000
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csr')
    b = np.ones(n)
    
    def count_iterations(M=None):
        count = [0]
        def callback(xk):
            count[0] += 1
        splinalg.cg(A, b, M=M, callback=callback, tol=1e-10)
        return count[0]
    
    # No preconditioning
    iters_none = count_iterations()
    
    # ILU preconditioning
    ilu = splinalg.spilu(A.tocsc())
    M_ilu = splinalg.LinearOperator(A.shape, ilu.solve)
    iters_ilu = count_iterations(M_ilu)
    
    print(f"No precond:  {iters_none} iterations")
    print(f"ILU precond: {iters_ilu} iterations")

if __name__ == "__main__":
    main()
```

## Summary

| Preconditioner | Cost | Effectiveness |
|:---------------|:-----|:--------------|
| Jacobi (diagonal) | Low | Moderate |
| ILU | Medium | Good |
| Sparse Cholesky | High | Excellent |

Key: Choose preconditioner based on cost vs. iteration reduction trade-off.
