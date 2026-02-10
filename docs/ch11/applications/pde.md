# PDE Discretization

Sparse matrices from discretizing PDEs.

## 1D Laplacian

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 100
    h = 1 / (n + 1)
    
    # Tridiagonal Laplacian
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n)) / h**2
    
    # Solve -u'' = f with u(0) = u(1) = 0
    x = np.linspace(h, 1-h, n)
    f = np.sin(np.pi * x)
    
    u = splinalg.spsolve(A.tocsr(), f)
    
    print(f"Solution at midpoint: {u[n//2]:.6f}")
    print(f"Exact: {np.sin(np.pi * 0.5) / np.pi**2:.6f}")

if __name__ == "__main__":
    main()
```

## 2D Laplacian

```python
import numpy as np
from scipy import sparse

def main():
    n = 10  # Grid points per dimension
    N = n * n  # Total unknowns
    
    # 5-point stencil
    diag = 4 * np.ones(N)
    off1 = -np.ones(N - 1)
    off1[n-1::n] = 0  # No wrap at row boundaries
    offn = -np.ones(N - n)
    
    A = sparse.diags([offn, off1, diag, off1, offn], 
                     [-n, -1, 0, 1, n], format='csr')
    
    print(f"2D Laplacian: {A.shape}")
    print(f"Nonzeros: {A.nnz}")
    print(f"Density: {A.nnz / N**2:.4%}")

if __name__ == "__main__":
    main()
```
