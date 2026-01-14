# Matrix Logarithm

The matrix logarithm is the inverse of matrix exponential.

## linalg.logm

### 1. Basic Usage

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[2, 0],
                  [0, 3]])
    
    log_A = linalg.logm(A)
    
    print("A =")
    print(A)
    print()
    print("log(A) =")
    print(log_A)

if __name__ == "__main__":
    main()
```

### 2. Inverse Relationship

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 0.5],
                  [0, 2]])
    
    # log(exp(A)) = A
    exp_A = linalg.expm(A)
    log_exp_A = linalg.logm(exp_A)
    
    print("A =")
    print(A)
    print()
    print("log(exp(A)) =")
    print(log_exp_A.real.round(10))

if __name__ == "__main__":
    main()
```

### 3. exp(log(A)) = A

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[2, 1],
                  [0, 3]])
    
    log_A = linalg.logm(A)
    exp_log_A = linalg.expm(log_A)
    
    print("A =")
    print(A)
    print()
    print("exp(log(A)) =")
    print(exp_log_A.real.round(10))

if __name__ == "__main__":
    main()
```

## Requirements

### 1. No Negative Eigenvalues

```python
import numpy as np
from scipy import linalg

def main():
    # Matrix with negative eigenvalue
    A = np.array([[-1, 0],
                  [0, 2]])
    
    # logm may return complex result
    log_A = linalg.logm(A)
    
    print("A eigenvalues:", np.linalg.eigvals(A))
    print()
    print("log(A) (complex):")
    print(log_A)

if __name__ == "__main__":
    main()
```

### 2. Nonsingular Matrix

```python
import numpy as np
from scipy import linalg

def main():
    # Singular matrix - logarithm undefined
    A = np.array([[1, 0],
                  [0, 0]])
    
    try:
        log_A = linalg.logm(A)
        print(log_A)
    except Exception as e:
        print(f"Error: log undefined for singular matrix")

if __name__ == "__main__":
    main()
```

## Applications

### 1. Rotation Interpolation

```python
import numpy as np
from scipy import linalg

def main():
    # Interpolate between rotations
    theta1, theta2 = 0, np.pi/2
    
    R1 = np.array([[np.cos(theta1), -np.sin(theta1)],
                   [np.sin(theta1), np.cos(theta1)]])
    R2 = np.array([[np.cos(theta2), -np.sin(theta2)],
                   [np.sin(theta2), np.cos(theta2)]])
    
    # Interpolation: R(t) = R1 @ exp(t * log(R1.T @ R2))
    log_diff = linalg.logm(R1.T @ R2)
    
    for t in [0, 0.25, 0.5, 0.75, 1.0]:
        R_t = R1 @ linalg.expm(t * log_diff)
        angle = np.arctan2(R_t[1, 0], R_t[0, 0])
        print(f"t={t}: angle = {np.degrees(angle):.1f}°")

if __name__ == "__main__":
    main()
```

### 2. Principal Logarithm

```python
import numpy as np
from scipy import linalg

def main():
    # For positive definite matrix, log is real
    A = np.array([[4, 2],
                  [2, 3]])
    
    log_A = linalg.logm(A)
    
    print("Symmetric positive definite A:")
    print(A)
    print()
    print("log(A) (real):")
    print(log_A.real.round(6))

if __name__ == "__main__":
    main()
```

## Summary

| Function | Description |
|:---------|:------------|
| `linalg.logm(A)` | Matrix logarithm |

Key: Requires nonsingular A. May be complex for matrices with negative eigenvalues.
