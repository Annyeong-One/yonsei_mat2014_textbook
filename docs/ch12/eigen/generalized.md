# Generalized Eigenvalues

Generalized eigenvalue problems solve $Av = \lambda Bv$.

## linalg.eig with Two Matrices

### 1. Basic Usage

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2],
                  [3, 4]])
    B = np.array([[5, 6],
                  [7, 8]])
    
    # Solve A @ v = λ @ B @ v
    eigenvalues, eigenvectors = linalg.eig(A, B)
    
    print("Generalized eigenvalues:")
    print(eigenvalues)
    print()
    print("Generalized eigenvectors:")
    print(eigenvectors)

if __name__ == "__main__":
    main()
```

### 2. Verify Solution

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[4, 2],
                  [2, 3]])
    B = np.array([[2, 0],
                  [0, 1]])
    
    eigenvalues, eigenvectors = linalg.eig(A, B)
    
    for i in range(len(eigenvalues)):
        lam = eigenvalues[i]
        v = eigenvectors[:, i]
        
        Av = A @ v
        lam_Bv = lam * B @ v
        
        print(f"Eigenvalue {i}: λ = {lam:.4f}")
        print(f"  Match: {np.allclose(Av, lam_Bv)}")

if __name__ == "__main__":
    main()
```

## Symmetric Generalized Problem

### 1. linalg.eigh with B

```python
import numpy as np
from scipy import linalg

def main():
    # Both A and B symmetric, B positive definite
    A = np.array([[4, 2],
                  [2, 3]])
    B = np.array([[2, 0.5],
                  [0.5, 1]])
    
    eigenvalues, eigenvectors = linalg.eigh(A, B)
    
    print("Eigenvalues (real, sorted):")
    print(eigenvalues)

if __name__ == "__main__":
    main()
```

### 2. B-Orthogonality

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[4, 2],
                  [2, 3]])
    B = np.array([[2, 0],
                  [0, 1]])
    
    eigenvalues, V = linalg.eigh(A, B)
    
    # Eigenvectors are B-orthonormal: V.T @ B @ V = I
    print("V.T @ B @ V:")
    print((V.T @ B @ V).round(10))

if __name__ == "__main__":
    main()
```

## Applications

### 1. Vibration Analysis

```python
import numpy as np
from scipy import linalg

def main():
    # Mass-spring system: K @ x = ω² @ M @ x
    K = np.array([[3, -1, 0],
                  [-1, 2, -1],
                  [0, -1, 1]])
    M = np.array([[2, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]])
    
    eigenvalues, modes = linalg.eigh(K, M)
    
    print("Natural frequencies (ω):")
    print(np.sqrt(eigenvalues))

if __name__ == "__main__":
    main()
```

### 2. Fisher's Linear Discriminant

```python
import numpy as np
from scipy import linalg

def main():
    np.random.seed(42)
    
    class1 = np.random.randn(50, 3) + [0, 0, 0]
    class2 = np.random.randn(50, 3) + [2, 1, 1]
    
    S_W = np.cov(class1.T) + np.cov(class2.T)
    m1, m2 = class1.mean(axis=0), class2.mean(axis=0)
    diff = (m1 - m2).reshape(-1, 1)
    S_B = diff @ diff.T
    
    eigenvalues, eigenvectors = linalg.eig(S_B, S_W)
    idx = np.argmax(eigenvalues.real)
    w = eigenvectors[:, idx].real
    
    print("Optimal projection:")
    print(w / np.linalg.norm(w))

if __name__ == "__main__":
    main()
```

## Summary

| Function | Description |
|:---------|:------------|
| `linalg.eig(A, B)` | General Av = λBv |
| `linalg.eigh(A, B)` | Symmetric A, SPD B |
| `linalg.qz(A, B)` | QZ decomposition |
