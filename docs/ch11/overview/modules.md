# Module Organization

SciPy provides linear algebra functionality across multiple modules.

## Core Modules

### 1. scipy.linalg

Dense matrix operations and decompositions.

```python
from scipy import linalg

# Key functions
# linalg.lu, linalg.qr, linalg.svd
# linalg.eig, linalg.eigh
# linalg.solve, linalg.inv
# linalg.expm, linalg.logm
```

### 2. scipy.sparse

Sparse matrix classes and construction.

```python
from scipy import sparse

# Sparse matrix formats
# sparse.csr_matrix, sparse.csc_matrix
# sparse.coo_matrix, sparse.lil_matrix
# sparse.dia_matrix, sparse.dok_matrix
```

### 3. scipy.sparse.linalg

Sparse linear algebra operations.

```python
from scipy.sparse import linalg as splinalg

# Sparse solvers
# splinalg.spsolve, splinalg.splu
# splinalg.cg, splinalg.gmres
# splinalg.eigs, splinalg.eigsh
```

## Module Overview

### 1. Hierarchy

```
scipy
├── linalg           # Dense operations
│   ├── decompositions (lu, qr, svd, cholesky, schur)
│   ├── eigenvalues (eig, eigh, eigvals)
│   ├── solvers (solve, solve_triangular, solve_banded)
│   ├── matrix functions (expm, logm, sqrtm)
│   └── special matrices (toeplitz, circulant, companion)
│
├── sparse           # Sparse matrix classes
│   ├── csr_matrix, csc_matrix
│   ├── coo_matrix, lil_matrix
│   └── construction functions
│
└── sparse.linalg    # Sparse operations
    ├── direct solvers (spsolve, splu)
    ├── iterative solvers (cg, gmres, bicg)
    └── eigensolvers (eigs, eigsh)
```

### 2. Import Patterns

```python
import numpy as np
from scipy import linalg
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    # Dense matrix
    A_dense = np.array([[4, 1], [1, 3]])
    
    # Dense operations via scipy.linalg
    L = linalg.cholesky(A_dense, lower=True)
    print("Cholesky L:")
    print(L)
    print()
    
    # Sparse matrix
    A_sparse = sparse.csr_matrix(A_dense)
    
    # Sparse operations via scipy.sparse.linalg
    b = np.array([1, 2])
    x = splinalg.spsolve(A_sparse, b)
    print(f"Sparse solve: x = {x}")

if __name__ == "__main__":
    main()
```

## Function Categories

### 1. Decompositions

| Function | Module | Description |
|:---------|:-------|:------------|
| `lu` | `linalg` | LU factorization |
| `qr` | `linalg` | QR factorization |
| `svd` | `linalg` | Singular value decomposition |
| `cholesky` | `linalg` | Cholesky decomposition |
| `schur` | `linalg` | Schur decomposition |
| `hessenberg` | `linalg` | Hessenberg form |

### 2. Eigenvalue Problems

| Function | Module | Description |
|:---------|:-------|:------------|
| `eig` | `linalg` | General eigenvalues |
| `eigh` | `linalg` | Hermitian eigenvalues |
| `eigvals` | `linalg` | Eigenvalues only |
| `eigs` | `sparse.linalg` | Sparse eigenvalues |
| `eigsh` | `sparse.linalg` | Sparse Hermitian eigenvalues |

### 3. Linear Solvers

| Function | Module | Description |
|:---------|:-------|:------------|
| `solve` | `linalg` | Dense system solver |
| `solve_triangular` | `linalg` | Triangular solver |
| `solve_banded` | `linalg` | Banded matrix solver |
| `spsolve` | `sparse.linalg` | Sparse direct solver |
| `cg` | `sparse.linalg` | Conjugate gradient |
| `gmres` | `sparse.linalg` | GMRES iterative |

### 4. Matrix Functions

| Function | Module | Description |
|:---------|:-------|:------------|
| `expm` | `linalg` | Matrix exponential |
| `logm` | `linalg` | Matrix logarithm |
| `sqrtm` | `linalg` | Matrix square root |
| `funm` | `linalg` | General matrix function |

## Practical Usage

### 1. Dense Workflow

```python
import numpy as np
from scipy import linalg

def main():
    A = np.random.randn(100, 100)
    A = A @ A.T  # Make symmetric positive definite
    b = np.random.randn(100)
    
    # Solve using Cholesky
    c, low = linalg.cho_factor(A)
    x = linalg.cho_solve((c, low), b)
    
    print(f"Solution norm: {np.linalg.norm(x):.4f}")
    print(f"Residual: {np.linalg.norm(A @ x - b):.2e}")

if __name__ == "__main__":
    main()
```

### 2. Sparse Workflow

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    # Create sparse matrix
    n = 1000
    diags = [-np.ones(n-1), 2*np.ones(n), -np.ones(n-1)]
    A = sparse.diags(diags, [-1, 0, 1], format='csr')
    
    b = np.ones(n)
    
    # Solve sparse system
    x = splinalg.spsolve(A, b)
    
    print(f"Solution norm: {np.linalg.norm(x):.4f}")
    print(f"Residual: {np.linalg.norm(A @ x - b):.2e}")

if __name__ == "__main__":
    main()
```

## Summary

### 1. Quick Reference

| Task | Module |
|:-----|:-------|
| Dense decompositions | `scipy.linalg` |
| Dense solvers | `scipy.linalg` |
| Matrix functions | `scipy.linalg` |
| Sparse matrices | `scipy.sparse` |
| Sparse solvers | `scipy.sparse.linalg` |
| Sparse eigenvalues | `scipy.sparse.linalg` |
