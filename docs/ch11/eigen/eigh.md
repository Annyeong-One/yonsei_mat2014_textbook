# Symmetric Eigenvalues

`linalg.eigh` computes eigenvalues for symmetric (Hermitian) matrices efficiently.

## linalg.eigh

### 1. Basic Usage

```python
import numpy as np
from scipy import linalg

def main():
    # Symmetric matrix
    A = np.array([[4, 2, 1],
                  [2, 5, 3],
                  [1, 3, 6]])
    
    eigenvalues, eigenvectors = linalg.eigh(A)
    
    print("Eigenvalues (real, sorted):")
    print(eigenvalues)
    print()
    print("Eigenvectors (orthonormal columns):")
    print(eigenvectors)

if __name__ == "__main__":
    main()
```

### 2. Guaranteed Properties

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[4, 2],
                  [2, 3]])
    
    eigenvalues, V = linalg.eigh(A)
    
    # Property 1: Eigenvalues are real
    print(f"Eigenvalues real: {np.all(np.isreal(eigenvalues))}")
    
    # Property 2: Sorted ascending
    print(f"Sorted: {np.all(eigenvalues[:-1] <= eigenvalues[1:])}")
    
    # Property 3: Eigenvectors orthonormal
    print(f"V.T @ V = I: {np.allclose(V.T @ V, np.eye(len(A)))}")

if __name__ == "__main__":
    main()
```

### 3. Spectral Theorem

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[4, 2],
                  [2, 3]])
    
    eigenvalues, V = linalg.eigh(A)
    
    # A = V @ D @ V.T (orthogonal diagonalization)
    D = np.diag(eigenvalues)
    A_reconstructed = V @ D @ V.T
    
    print("A = V @ D @ V.T:")
    print(A_reconstructed)
    print()
    print("Original A:")
    print(A)

if __name__ == "__main__":
    main()
```

## eigh vs eig

### 1. Performance

```python
import numpy as np
from scipy import linalg
import time

def main():
    n = 500
    A = np.random.randn(n, n)
    A = A + A.T  # Symmetric
    
    # General solver
    start = time.perf_counter()
    vals1, vecs1 = linalg.eig(A)
    eig_time = time.perf_counter() - start
    
    # Symmetric solver
    start = time.perf_counter()
    vals2, vecs2 = linalg.eigh(A)
    eigh_time = time.perf_counter() - start
    
    print(f"eig time:  {eig_time:.4f} sec")
    print(f"eigh time: {eigh_time:.4f} sec")
    print(f"Speedup:   {eig_time/eigh_time:.2f}x")

if __name__ == "__main__":
    main()
```

### 2. Numerical Stability

```python
import numpy as np
from scipy import linalg

def main():
    # Symmetric matrix
    A = np.array([[1, 1e-10],
                  [1e-10, 1]])
    
    # eigh guarantees orthogonal eigenvectors
    vals_h, vecs_h = linalg.eigh(A)
    
    # eig may not
    vals_g, vecs_g = linalg.eig(A)
    
    print("eigh orthogonality error:")
    print(np.linalg.norm(vecs_h.T @ vecs_h - np.eye(2)))
    print()
    print("eig orthogonality error:")
    print(np.linalg.norm(vecs_g.T @ vecs_g - np.eye(2)))

if __name__ == "__main__":
    main()
```

## Subset of Eigenvalues

### 1. Eigenvalue Range

```python
import numpy as np
from scipy import linalg

def main():
    A = np.diag([1, 2, 3, 4, 5])
    
    # Only eigenvalues in range [2, 4]
    vals, vecs = linalg.eigh(A, subset_by_value=(2, 4))
    
    print("Eigenvalues in [2, 4]:")
    print(vals)

if __name__ == "__main__":
    main()
```

### 2. Eigenvalue Index Range

```python
import numpy as np
from scipy import linalg

def main():
    A = np.diag([1, 2, 3, 4, 5])
    
    # Only k-th to l-th eigenvalues (0-indexed)
    vals, vecs = linalg.eigh(A, subset_by_index=(1, 3))
    
    print("Eigenvalues 1 to 3 (2nd to 4th smallest):")
    print(vals)

if __name__ == "__main__":
    main()
```

## eigvalsh

### 1. Eigenvalues Only

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[4, 2, 1],
                  [2, 5, 3],
                  [1, 3, 6]])
    
    eigenvalues = linalg.eigvalsh(A)
    
    print("Eigenvalues only:")
    print(eigenvalues)

if __name__ == "__main__":
    main()
```

## Applications

### 1. Principal Component Analysis

```python
import numpy as np
from scipy import linalg

def main():
    np.random.seed(42)
    
    # Generate correlated data
    n_samples = 100
    X = np.random.randn(n_samples, 3) @ np.array([[1, 0.5, 0],
                                                   [0.5, 1, 0.5],
                                                   [0, 0.5, 1]])
    
    # Covariance matrix
    X_centered = X - X.mean(axis=0)
    C = X_centered.T @ X_centered / (n_samples - 1)
    
    # Eigendecomposition
    eigenvalues, eigenvectors = linalg.eigh(C)
    
    # Sort descending
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    print("Variance explained:")
    print(eigenvalues / eigenvalues.sum())
    print()
    print("First principal component:")
    print(eigenvectors[:, 0])

if __name__ == "__main__":
    main()
```

### 2. Positive Definiteness Check

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[4, 2],
                  [2, 3]])
    
    eigenvalues = linalg.eigvalsh(A)
    
    print(f"Eigenvalues: {eigenvalues}")
    
    if np.all(eigenvalues > 0):
        print("Matrix is positive definite")
    elif np.all(eigenvalues >= 0):
        print("Matrix is positive semi-definite")
    else:
        print("Matrix is indefinite")

if __name__ == "__main__":
    main()
```

### 3. Graph Laplacian Spectrum

```python
import numpy as np
from scipy import linalg

def main():
    # Adjacency matrix of a path graph
    A = np.array([[0, 1, 0, 0],
                  [1, 0, 1, 0],
                  [0, 1, 0, 1],
                  [0, 0, 1, 0]])
    
    # Degree matrix
    D = np.diag(A.sum(axis=1))
    
    # Laplacian
    L = D - A
    
    eigenvalues = linalg.eigvalsh(L)
    
    print("Laplacian eigenvalues:")
    print(eigenvalues.round(6))
    print()
    print("Number of connected components:", np.sum(eigenvalues < 1e-10))

if __name__ == "__main__":
    main()
```

## Summary

### 1. Functions

| Function | Description |
|:---------|:------------|
| `linalg.eigh(A)` | Eigenvalues and eigenvectors |
| `linalg.eigvalsh(A)` | Eigenvalues only |
| `subset_by_value` | Select eigenvalue range |
| `subset_by_index` | Select by index |

### 2. Key Properties

- Eigenvalues always real
- Eigenvectors orthonormal
- Results sorted ascending
- Faster than `eig` for symmetric matrices
