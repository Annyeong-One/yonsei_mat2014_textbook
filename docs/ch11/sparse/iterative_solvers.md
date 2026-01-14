# Iterative Solvers

Iterative methods for large sparse linear systems.

## Conjugate Gradient (CG)

### 1. For SPD Matrices

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 1000
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csr')
    b = np.ones(n)
    
    x, info = splinalg.cg(A, b)
    
    print(f"Converged: {info == 0}")
    print(f"Residual: {np.linalg.norm(A @ x - b):.2e}")

if __name__ == "__main__":
    main()
```

### 2. With Tolerance

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 1000
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csr')
    b = np.ones(n)
    
    x, info = splinalg.cg(A, b, tol=1e-10, maxiter=500)
    
    print(f"Info: {info}")
    print(f"Residual: {np.linalg.norm(A @ x - b):.2e}")

if __name__ == "__main__":
    main()
```

## GMRES

### 1. For General Matrices

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 500
    A = sparse.random(n, n, density=0.01, format='csr')
    A = A + sparse.eye(n) * 10  # Make diagonally dominant
    b = np.ones(n)
    
    x, info = splinalg.gmres(A, b)
    
    print(f"Converged: {info == 0}")
    print(f"Residual: {np.linalg.norm(A @ x - b):.2e}")

if __name__ == "__main__":
    main()
```

## BiCGSTAB

### 1. Another Option for Non-symmetric

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 500
    A = sparse.random(n, n, density=0.01, format='csr')
    A = A + sparse.eye(n) * 10
    b = np.ones(n)
    
    x, info = splinalg.bicgstab(A, b)
    
    print(f"Converged: {info == 0}")
    print(f"Residual: {np.linalg.norm(A @ x - b):.2e}")

if __name__ == "__main__":
    main()
```

## Callback for Monitoring

### 1. Track Convergence

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 500
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csr')
    b = np.ones(n)
    
    residuals = []
    def callback(xk):
        r = np.linalg.norm(A @ xk - b)
        residuals.append(r)
    
    x, info = splinalg.cg(A, b, callback=callback)
    
    print(f"Iterations: {len(residuals)}")
    print(f"Final residual: {residuals[-1]:.2e}")

if __name__ == "__main__":
    main()
```

## Method Selection

| Method | Matrix Type | Memory |
|:-------|:------------|:-------|
| CG | SPD | Low |
| GMRES | General | High (grows) |
| BiCGSTAB | General | Low |
| MINRES | Symmetric | Low |

## Summary

| Function | Use Case |
|:---------|:---------|
| `cg(A, b)` | Symmetric positive definite |
| `gmres(A, b)` | General (non-symmetric) |
| `bicgstab(A, b)` | General, memory-efficient |
| `minres(A, b)` | Symmetric indefinite |
