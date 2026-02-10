# Hessenberg Form

Hessenberg form reduces a matrix to almost-triangular form.

## Basic Decomposition

### 1. linalg.hessenberg

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])
    
    H = linalg.hessenberg(A)
    
    print("A =")
    print(A)
    print()
    print("H (upper Hessenberg):")
    print(H.round(6))

if __name__ == "__main__":
    main()
```

### 2. Mathematical Form

$$A = QHQ^H$$

where:
- $Q$ is unitary
- $H$ is upper Hessenberg (zero below first subdiagonal)

### 3. Structure

```
Upper Hessenberg:
[* * * *]
[* * * *]
[0 * * *]
[0 0 * *]
```

## With Transformation Matrix

### 1. Return Q

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    
    H, Q = linalg.hessenberg(A, calc_q=True)
    
    print("H (Hessenberg form):")
    print(H.round(6))
    print()
    print("Q (unitary):")
    print(Q.round(6))
    print()
    print("Verify Q @ H @ Q.T:")
    print((Q @ H @ Q.T).round(6))

if __name__ == "__main__":
    main()
```

### 2. Verify Orthogonality

```python
import numpy as np
from scipy import linalg

def main():
    A = np.random.randn(4, 4)
    
    H, Q = linalg.hessenberg(A, calc_q=True)
    
    print("Q.T @ Q (should be identity):")
    print((Q.T @ Q).round(10))

if __name__ == "__main__":
    main()
```

## Eigenvalue Computation

### 1. Why Hessenberg

```python
import numpy as np
from scipy import linalg

def main():
    n = 5
    A = np.random.randn(n, n)
    
    # Eigenvalue algorithms work faster on Hessenberg form
    # QR iteration on H: O(n^2) per iteration vs O(n^3) on A
    
    H = linalg.hessenberg(A)
    
    # Eigenvalues are preserved
    eig_A = np.sort(np.linalg.eigvals(A))
    eig_H = np.sort(np.linalg.eigvals(H))
    
    print("Eigenvalues of A:")
    print(eig_A.round(6))
    print()
    print("Eigenvalues of H:")
    print(eig_H.round(6))

if __name__ == "__main__":
    main()
```

### 2. QR Iteration on Hessenberg

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[4, 1, 0],
                  [1, 3, 1],
                  [0, 1, 2]])
    
    # Reduce to Hessenberg first
    H = linalg.hessenberg(A)
    
    # QR iteration (faster on Hessenberg)
    Hk = H.copy()
    for _ in range(30):
        Q, R = np.linalg.qr(Hk)
        Hk = R @ Q
    
    print("Converged to quasi-triangular:")
    print(Hk.round(6))
    print()
    print("Eigenvalues (diagonal):")
    print(np.diag(Hk).round(6))

if __name__ == "__main__":
    main()
```

## Symmetric Case

### 1. Tridiagonal Form

```python
import numpy as np
from scipy import linalg

def main():
    # Symmetric matrix
    A = np.array([[4, 1, 0, 0],
                  [1, 4, 1, 0],
                  [0, 1, 4, 1],
                  [0, 0, 1, 4]])
    
    H = linalg.hessenberg(A)
    
    print("H for symmetric A (tridiagonal):")
    print(H.round(6))

if __name__ == "__main__":
    main()
```

### 2. Why Tridiagonal

For symmetric matrices, Hessenberg form becomes tridiagonal, enabling even faster algorithms.

## Computational Cost

### 1. Complexity Analysis

```python
import numpy as np
from scipy import linalg
import time

def main():
    sizes = [100, 200, 400, 800]
    
    print("Hessenberg reduction times:")
    print(f"{'n':>6} | {'Time (sec)':>12}")
    print("-" * 22)
    
    for n in sizes:
        A = np.random.randn(n, n)
        
        start = time.perf_counter()
        H = linalg.hessenberg(A)
        elapsed = time.perf_counter() - start
        
        print(f"{n:6d} | {elapsed:12.4f}")

if __name__ == "__main__":
    main()
```

### 2. Reduction is O(n³)

Initial reduction: $O(n^3)$

Each QR step on H: $O(n^2)$ instead of $O(n^3)$

## Applications

### 1. Polynomial Eigenvalues

```python
import numpy as np
from scipy import linalg

def main():
    # Roots of p(x) = x^3 - 6x^2 + 11x - 6
    # Are eigenvalues of companion matrix
    
    coeffs = [1, -6, 11, -6]  # x^3 - 6x^2 + 11x - 6
    
    # Companion matrix is already Hessenberg
    C = np.array([[6, -11, 6],
                  [1, 0, 0],
                  [0, 1, 0]])
    
    roots = np.linalg.eigvals(C)
    
    print("Polynomial roots:")
    print(np.sort(roots.real).round(6))
    print()
    print("Verify: (x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6")

if __name__ == "__main__":
    main()
```

### 2. Transfer Function Analysis

```python
import numpy as np
from scipy import linalg

def main():
    # State-space system: dx/dt = Ax
    A = np.array([[0, 1, 0],
                  [0, 0, 1],
                  [-6, -11, -6]])
    
    H, Q = linalg.hessenberg(A, calc_q=True)
    
    print("System in Hessenberg form:")
    print(H.round(6))
    print()
    
    # Eigenvalues determine stability
    eigs = np.linalg.eigvals(H)
    print("Poles (eigenvalues):")
    print(eigs.round(6))

if __name__ == "__main__":
    main()
```

### 3. Matrix Exponential Preprocessing

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    
    # Hessenberg reduction can accelerate exp(A) computation
    H, Q = linalg.hessenberg(A, calc_q=True)
    
    # exp(A) = Q @ exp(H) @ Q.T
    exp_H = linalg.expm(H)
    exp_A = Q @ exp_H @ Q.T
    
    print("exp(A) via Hessenberg:")
    print(exp_A.round(6))
    print()
    print("exp(A) direct:")
    print(linalg.expm(A).round(6))

if __name__ == "__main__":
    main()
```

## Summary

### 1. Functions

| Function | Description |
|:---------|:------------|
| `linalg.hessenberg(A)` | Hessenberg form |
| `linalg.hessenberg(A, calc_q=True)` | With transformation Q |

### 2. Key Properties

- $H$ is upper Hessenberg (zeros below subdiagonal)
- Preserves eigenvalues
- Symmetric A → Tridiagonal H
- Speeds up QR iteration: $O(n^2)$ vs $O(n^3)$ per step
