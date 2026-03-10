# Eigenvalues


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Compute eigenvalues and eigenvectors using `np.linalg`.

## np.linalg.eig

### 1. Basic Usage

```python
import numpy as np

def main():
    A = np.array([[4, 2],
                  [1, 3]])
    
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    print(f"Eigenvalues: {eigenvalues}")
    print()
    print("Eigenvectors (columns):")
    print(eigenvectors)

if __name__ == "__main__":
    main()
```

### 2. Mathematical Form

$A v = \lambda v$

where $\lambda$ is eigenvalue, $v$ is eigenvector.

### 3. Verify Result

```python
import numpy as np

def main():
    A = np.array([[4, 2],
                  [1, 3]])
    
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    for i in range(len(eigenvalues)):
        lam = eigenvalues[i]
        v = eigenvectors[:, i]
        
        # A @ v should equal lam * v
        Av = A @ v
        lam_v = lam * v
        
        print(f"λ_{i} = {lam:.4f}")
        print(f"A @ v = {Av}")
        print(f"λ * v = {lam_v}")
        print(f"Match: {np.allclose(Av, lam_v)}")
        print()

if __name__ == "__main__":
    main()
```

## np.linalg.eigvals

### 1. Eigenvalues Only

```python
import numpy as np

def main():
    A = np.array([[4, 2],
                  [1, 3]])
    
    eigenvalues = np.linalg.eigvals(A)
    
    print(f"Eigenvalues: {eigenvalues}")

if __name__ == "__main__":
    main()
```

### 2. Faster Computation

Use when only eigenvalues are needed, not eigenvectors.

### 3. Complex Eigenvalues

```python
import numpy as np

def main():
    # Rotation matrix has complex eigenvalues
    theta = np.pi / 4
    A = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    
    eigenvalues = np.linalg.eigvals(A)
    
    print(f"Eigenvalues: {eigenvalues}")
    print(f"Magnitude: {np.abs(eigenvalues)}")

if __name__ == "__main__":
    main()
```

## np.linalg.eigh

### 1. Symmetric Matrices

Specialized for symmetric (Hermitian) matrices.

```python
import numpy as np

def main():
    # Symmetric matrix
    A = np.array([[4, 2, 1],
                  [2, 5, 3],
                  [1, 3, 6]])
    
    eigenvalues, eigenvectors = np.linalg.eigh(A)
    
    print(f"Eigenvalues: {eigenvalues}")
    print()
    print("Eigenvectors:")
    print(eigenvectors)

if __name__ == "__main__":
    main()
```

### 2. Real Eigenvalues

Symmetric matrices always have real eigenvalues.

```python
import numpy as np

def main():
    A = np.array([[4, 2],
                  [2, 3]])
    
    # eigh guarantees real eigenvalues
    eigenvalues, eigenvectors = np.linalg.eigh(A)
    
    print(f"Eigenvalues (real): {eigenvalues}")
    print(f"Dtype: {eigenvalues.dtype}")

if __name__ == "__main__":
    main()
```

### 3. Orthogonal Eigenvectors

```python
import numpy as np

def main():
    A = np.array([[4, 2, 1],
                  [2, 5, 3],
                  [1, 3, 6]])
    
    eigenvalues, V = np.linalg.eigh(A)
    
    # Eigenvectors are orthonormal
    print("V^T @ V =")
    print(np.round(V.T @ V, 10))

if __name__ == "__main__":
    main()
```

## Sorted Eigenvalues

### 1. eigh Returns Sorted

```python
import numpy as np

def main():
    A = np.array([[5, 2],
                  [2, 3]])
    
    # eigh returns eigenvalues in ascending order
    eigenvalues, eigenvectors = np.linalg.eigh(A)
    
    print(f"Eigenvalues (sorted): {eigenvalues}")

if __name__ == "__main__":
    main()
```

### 2. Sort eig Results

```python
import numpy as np

def main():
    A = np.array([[5, 2],
                  [2, 3]])
    
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    # Sort by eigenvalue magnitude
    idx = np.argsort(np.abs(eigenvalues))[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    print(f"Sorted eigenvalues: {eigenvalues}")

if __name__ == "__main__":
    main()
```

### 3. Largest Eigenvalue

```python
import numpy as np

def main():
    np.random.seed(42)
    A = np.random.randn(5, 5)
    A = A @ A.T  # Make symmetric positive semi-definite
    
    eigenvalues, eigenvectors = np.linalg.eigh(A)
    
    # Largest eigenvalue is last (eigh sorts ascending)
    largest_val = eigenvalues[-1]
    largest_vec = eigenvectors[:, -1]
    
    print(f"Largest eigenvalue: {largest_val:.4f}")
    print(f"Corresponding eigenvector: {largest_vec}")

if __name__ == "__main__":
    main()
```

## Spectral Decomposition

### 1. Diagonalization

$A = V \Lambda V^{-1}$

```python
import numpy as np

def main():
    A = np.array([[4, 2],
                  [1, 3]])
    
    eigenvalues, V = np.linalg.eig(A)
    Lambda = np.diag(eigenvalues)
    
    # Reconstruct A
    A_reconstructed = V @ Lambda @ np.linalg.inv(V)
    
    print("Original A:")
    print(A)
    print()
    print("V @ Λ @ V^(-1):")
    print(np.real(A_reconstructed).round(10))

if __name__ == "__main__":
    main()
```

### 2. Symmetric Case

$A = V \Lambda V^T$ (V is orthogonal)

```python
import numpy as np

def main():
    A = np.array([[4, 2],
                  [2, 3]])
    
    eigenvalues, V = np.linalg.eigh(A)
    Lambda = np.diag(eigenvalues)
    
    # Reconstruct (V is orthogonal, so V^(-1) = V^T)
    A_reconstructed = V @ Lambda @ V.T
    
    print("Original A:")
    print(A)
    print()
    print("V @ Λ @ V^T:")
    print(A_reconstructed.round(10))

if __name__ == "__main__":
    main()
```

### 3. Matrix Power

```python
import numpy as np

def main():
    A = np.array([[4, 2],
                  [2, 3]])
    
    eigenvalues, V = np.linalg.eigh(A)
    
    # A^10 = V @ Λ^10 @ V^T
    Lambda_10 = np.diag(eigenvalues ** 10)
    A_10 = V @ Lambda_10 @ V.T
    
    print("A^10 via eigendecomposition:")
    print(A_10.round(2))
    print()
    print("A^10 via matrix_power:")
    print(np.linalg.matrix_power(A, 10).round(2))

if __name__ == "__main__":
    main()
```

## Applications

### 1. Principal Components

```python
import numpy as np

def main():
    np.random.seed(42)
    
    # Generate correlated data
    X = np.random.randn(100, 3)
    X[:, 1] = X[:, 0] + 0.1 * np.random.randn(100)
    
    # Center data
    X_centered = X - X.mean(axis=0)
    
    # Covariance matrix
    cov = np.cov(X_centered.T)
    
    # Eigendecomposition
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    
    # Sort descending
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    print("Eigenvalues (variance explained):")
    print(eigenvalues)
    print()
    print("Variance ratios:")
    print(eigenvalues / eigenvalues.sum())

if __name__ == "__main__":
    main()
```

### 2. Graph Laplacian

```python
import numpy as np

def main():
    # Adjacency matrix
    A = np.array([[0, 1, 1, 0],
                  [1, 0, 1, 1],
                  [1, 1, 0, 1],
                  [0, 1, 1, 0]])
    
    # Degree matrix
    D = np.diag(A.sum(axis=1))
    
    # Laplacian
    L = D - A
    
    eigenvalues, eigenvectors = np.linalg.eigh(L)
    
    print("Laplacian eigenvalues:", eigenvalues.round(4))
    print("Second smallest (algebraic connectivity):", eigenvalues[1])

if __name__ == "__main__":
    main()
```

### 3. Stability Analysis

```python
import numpy as np

def main():
    # System matrix
    A = np.array([[-1, 2],
                  [-1, -1]])
    
    eigenvalues = np.linalg.eigvals(A)
    
    print(f"Eigenvalues: {eigenvalues}")
    print(f"Real parts: {eigenvalues.real}")
    
    # System is stable if all real parts are negative
    is_stable = np.all(eigenvalues.real < 0)
    print(f"System is stable: {is_stable}")

if __name__ == "__main__":
    main()
```

## Best Practices

### 1. Use eigh for Symmetric

`eigh` is faster and more numerically stable for symmetric matrices.

### 2. Check Matrix Properties

Verify symmetry before using `eigh`.

```python
import numpy as np

def main():
    A = np.array([[4, 2],
                  [2, 3]])
    
    is_symmetric = np.allclose(A, A.T)
    print(f"Is symmetric: {is_symmetric}")

if __name__ == "__main__":
    main()
```

### 3. Handle Complex Results

`eig` may return complex eigenvalues even for real matrices.
