# SciPy vs NumPy Linalg

SciPy's `scipy.linalg` extends NumPy's linear algebra capabilities.

## Module Comparison

### 1. Basic Import

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2], [3, 4]])
    
    # Both modules provide similar functions
    det_np = np.linalg.det(A)
    det_sp = linalg.det(A)
    
    print(f"NumPy det: {det_np}")
    print(f"SciPy det: {det_sp}")

if __name__ == "__main__":
    main()
```

### 2. Key Differences

| Feature | `numpy.linalg` | `scipy.linalg` |
|:--------|:---------------|:---------------|
| Scope | Core operations | Comprehensive |
| Decompositions | Basic (SVD, QR, Cholesky) | Extended (LU, Schur, Hessenberg) |
| Matrix functions | None | expm, logm, sqrtm |
| Special matrices | Limited | Extensive |
| LAPACK access | Indirect | Direct |
| Sparse support | No | Via `scipy.sparse.linalg` |

### 3. When to Use Which

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[4, 2], [2, 5]])
    
    # NumPy: simple operations
    eigvals_np = np.linalg.eigvals(A)
    print(f"NumPy eigvals: {eigvals_np}")
    
    # SciPy: more control and options
    eigvals_sp = linalg.eigvals(A)
    print(f"SciPy eigvals: {eigvals_sp}")

if __name__ == "__main__":
    main()
```

## Extended Functionality

### 1. Decompositions

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 10]])
    
    # LU decomposition (SciPy only)
    P, L, U = linalg.lu(A)
    
    print("P (permutation):")
    print(P)
    print()
    print("L (lower):")
    print(L)
    print()
    print("U (upper):")
    print(U)

if __name__ == "__main__":
    main()
```

### 2. Matrix Functions

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2], [0, 1]])
    
    # Matrix exponential (SciPy only)
    exp_A = linalg.expm(A)
    
    print("A =")
    print(A)
    print()
    print("exp(A) =")
    print(exp_A)

if __name__ == "__main__":
    main()
```

### 3. Special Solvers

```python
import numpy as np
from scipy import linalg

def main():
    # Triangular system (SciPy provides specialized solver)
    U = np.array([[2, 1, 3],
                  [0, 4, 2],
                  [0, 0, 5]])
    b = np.array([10, 14, 15])
    
    # Specialized triangular solver
    x = linalg.solve_triangular(U, b)
    
    print(f"x = {x}")
    print(f"Verify U @ x = {U @ x}")

if __name__ == "__main__":
    main()
```

## LAPACK and BLAS Access

### 1. Low-Level Routines

```python
import numpy as np
from scipy import linalg

def main():
    # Access LAPACK routines directly
    A = np.array([[1, 2], [3, 4]], dtype=float)
    
    # Get LAPACK function for LU factorization
    getrf = linalg.get_lapack_funcs('getrf', (A,))
    
    lu, piv, info = getrf(A)
    print(f"LU result:\n{lu}")
    print(f"Pivot indices: {piv}")
    print(f"Info: {info}")

if __name__ == "__main__":
    main()
```

### 2. BLAS Operations

```python
import numpy as np
from scipy import linalg

def main():
    # Access BLAS for optimized operations
    x = np.array([1, 2, 3], dtype=float)
    y = np.array([4, 5, 6], dtype=float)
    
    # Get BLAS dot product function
    ddot = linalg.get_blas_funcs('dot', (x, y))
    
    result = ddot(x, y)
    print(f"BLAS dot product: {result}")
    print(f"NumPy dot product: {np.dot(x, y)}")

if __name__ == "__main__":
    main()
```

## Recommendation

### 1. Use NumPy When

- Basic operations (det, inv, solve, eig)
- Minimizing dependencies
- Simple scripts

### 2. Use SciPy When

- Advanced decompositions (LU, Schur, Hessenberg)
- Matrix functions (expm, logm, sqrtm)
- Specialized solvers (triangular, banded)
- Maximum performance via LAPACK

### 3. General Advice

```python
# Recommended import pattern
import numpy as np
from scipy import linalg

# Use scipy.linalg as default for comprehensive functionality
```
