# Schur Decomposition

Schur decomposition factors a matrix into quasi-triangular form.

## Basic Decomposition

### 1. linalg.schur

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2, 3],
                  [0, 4, 5],
                  [0, 0, 6]])
    
    T, Z = linalg.schur(A)
    
    print("A =")
    print(A)
    print()
    print("T (quasi-triangular):")
    print(T)
    print()
    print("Z (unitary):")
    print(Z)
    print()
    print("Verify Z @ T @ Z.T:")
    print((Z @ T @ Z.T).round(10))

if __name__ == "__main__":
    main()
```

### 2. Mathematical Form

$$A = ZTZ^H$$

where:
- $Z$ is unitary ($Z^HZ = I$)
- $T$ is upper quasi-triangular (upper triangular with possible 2×2 blocks on diagonal)

### 3. Real vs Complex

```python
import numpy as np
from scipy import linalg

def main():
    # Matrix with complex eigenvalues
    A = np.array([[0, -1],
                  [1, 0]])
    
    # Real Schur (2x2 blocks for complex eigenvalue pairs)
    T_real, Z_real = linalg.schur(A, output='real')
    print("Real Schur T:")
    print(T_real)
    print()
    
    # Complex Schur (truly upper triangular)
    T_complex, Z_complex = linalg.schur(A, output='complex')
    print("Complex Schur T:")
    print(T_complex)

if __name__ == "__main__":
    main()
```

## Eigenvalues from Schur

### 1. Diagonal Contains Eigenvalues

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[4, 1, 0],
                  [1, 3, 1],
                  [0, 1, 2]])
    
    T, Z = linalg.schur(A, output='complex')
    
    print("Eigenvalues from Schur diagonal:")
    print(np.diag(T))
    print()
    print("Eigenvalues direct:")
    print(np.linalg.eigvals(A))

if __name__ == "__main__":
    main()
```

### 2. Why Use Schur

```python
import numpy as np
from scipy import linalg

def main():
    # Schur is always computable, even for defective matrices
    # Eigendecomposition may fail
    
    # Defective matrix (eigenvalue with algebraic > geometric multiplicity)
    A = np.array([[1, 1],
                  [0, 1]])
    
    T, Z = linalg.schur(A)
    print("Schur T:")
    print(T)
    print()
    print("Eigenvalues from T diagonal:", np.diag(T))

if __name__ == "__main__":
    main()
```

## Sorted Schur

### 1. linalg.rsf2csf

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[0, -1, 0],
                  [1, 0, 0],
                  [0, 0, 2]])
    
    # Real Schur form
    T_real, Z_real = linalg.schur(A, output='real')
    print("Real Schur T:")
    print(T_real)
    print()
    
    # Convert to complex Schur
    T_complex, Z_complex = linalg.rsf2csf(T_real, Z_real)
    print("Complex Schur T:")
    print(T_complex.round(10))

if __name__ == "__main__":
    main()
```

### 2. Ordering Eigenvalues

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2, 3],
                  [0, 4, 5],
                  [0, 0, 6]])
    
    # Get Schur form
    T, Z = linalg.schur(A)
    
    # Order by eigenvalue magnitude (custom sort)
    def select(eigval):
        return abs(eigval) < 3  # Select small eigenvalues first
    
    T_sorted, Z_sorted = linalg.schur(A, sort=select)
    
    print("Original T diagonal:", np.diag(T))
    print("Sorted T diagonal:  ", np.diag(T_sorted))

if __name__ == "__main__":
    main()
```

## Matrix Functions via Schur

### 1. Why Schur for Matrix Functions

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2],
                  [0, 3]])
    
    # Matrix exponential uses Schur internally
    # exp(A) = Z @ exp(T) @ Z.H
    
    T, Z = linalg.schur(A, output='complex')
    
    # exp(T) is easier because T is triangular
    exp_T = linalg.expm(T)
    exp_A_via_schur = Z @ exp_T @ Z.conj().T
    
    # Direct
    exp_A_direct = linalg.expm(A)
    
    print("exp(A) via Schur:")
    print(exp_A_via_schur.real.round(6))
    print()
    print("exp(A) direct:")
    print(exp_A_direct.round(6))

if __name__ == "__main__":
    main()
```

### 2. Matrix Square Root

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[4, 0],
                  [0, 9]])
    
    T, Z = linalg.schur(A, output='complex')
    
    # sqrt(T) for triangular is straightforward
    sqrt_T = np.diag(np.sqrt(np.diag(T)))
    sqrt_A = Z @ sqrt_T @ Z.conj().T
    
    print("sqrt(A):")
    print(sqrt_A.real.round(6))
    print()
    print("Verify sqrt(A) @ sqrt(A):")
    print((sqrt_A @ sqrt_A).real.round(6))

if __name__ == "__main__":
    main()
```

## Sylvester Equation

### 1. Solving AX + XB = C

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2],
                  [0, 3]])
    B = np.array([[4, 0],
                  [0, 5]])
    C = np.array([[1, 1],
                  [1, 1]])
    
    # Solve AX + XB = C
    X = linalg.solve_sylvester(A, B, C)
    
    print("Solution X:")
    print(X)
    print()
    print("Verify A @ X + X @ B:")
    print(A @ X + X @ B)

if __name__ == "__main__":
    main()
```

### 2. Schur-Based Solution

Sylvester equation solver uses Schur decomposition internally for numerical stability.

## Applications

### 1. Control Theory

```python
import numpy as np
from scipy import linalg

def main():
    # System stability analysis
    A = np.array([[-1, 1],
                  [0, -2]])
    
    T, Z = linalg.schur(A, output='complex')
    eigenvalues = np.diag(T)
    
    print("System matrix eigenvalues:")
    print(eigenvalues)
    print()
    
    if np.all(eigenvalues.real < 0):
        print("System is stable (all eigenvalues have negative real parts)")
    else:
        print("System is unstable")

if __name__ == "__main__":
    main()
```

### 2. Invariant Subspaces

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[2, 1, 0],
                  [0, 3, 1],
                  [0, 0, 4]])
    
    # Sort eigenvalues: put eigenvalue 2 first
    T, Z = linalg.schur(A, sort=lambda x: x.real < 2.5)
    
    print("Sorted Schur T:")
    print(T)
    print()
    
    # First column of Z spans invariant subspace for eigenvalue 2
    print("Invariant subspace (first column of Z):")
    print(Z[:, 0])

if __name__ == "__main__":
    main()
```

## Summary

### 1. Functions

| Function | Description |
|:---------|:------------|
| `linalg.schur(A)` | Schur decomposition |
| `linalg.schur(A, output='complex')` | Complex Schur |
| `linalg.schur(A, sort=f)` | Sorted Schur |
| `linalg.rsf2csf(T, Z)` | Real to complex Schur |

### 2. Key Properties

- Always exists (unlike eigendecomposition)
- T is quasi-triangular (real) or triangular (complex)
- Eigenvalues on diagonal of T
- Useful for matrix functions and equations
