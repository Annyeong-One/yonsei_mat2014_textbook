# Matrix Exponential

The matrix exponential $e^A$ is fundamental in solving differential equations.

## linalg.expm

### 1. Basic Usage

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2],
                  [0, 3]])
    
    exp_A = linalg.expm(A)
    
    print("A =")
    print(A)
    print()
    print("exp(A) =")
    print(exp_A)

if __name__ == "__main__":
    main()
```

### 2. Definition

$$e^A = \sum_{k=0}^{\infty} \frac{A^k}{k!} = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots$$

### 3. Diagonal Matrix

```python
import numpy as np
from scipy import linalg

def main():
    # For diagonal matrices: exp(D) has exp on diagonal
    D = np.diag([1, 2, 3])
    
    exp_D = linalg.expm(D)
    
    print("exp(D) =")
    print(exp_D)
    print()
    print("Diagonal elements:", np.diag(exp_D))
    print("Expected:", np.exp([1, 2, 3]))

if __name__ == "__main__":
    main()
```

## Properties

### 1. exp(0) = I

```python
import numpy as np
from scipy import linalg

def main():
    n = 3
    Z = np.zeros((n, n))
    
    print("exp(0) =")
    print(linalg.expm(Z))

if __name__ == "__main__":
    main()
```

### 2. exp(A) exp(-A) = I

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2],
                  [3, 4]])
    
    exp_A = linalg.expm(A)
    exp_neg_A = linalg.expm(-A)
    
    print("exp(A) @ exp(-A) =")
    print((exp_A @ exp_neg_A).round(10))

if __name__ == "__main__":
    main()
```

### 3. Commuting Matrices

```python
import numpy as np
from scipy import linalg

def main():
    # If AB = BA, then exp(A+B) = exp(A) exp(B)
    A = np.diag([1, 2])
    B = np.diag([3, 4])
    
    exp_ApB = linalg.expm(A + B)
    exp_A_exp_B = linalg.expm(A) @ linalg.expm(B)
    
    print("exp(A+B) =")
    print(exp_ApB)
    print()
    print("exp(A) @ exp(B) =")
    print(exp_A_exp_B)

if __name__ == "__main__":
    main()
```

## Applications

### 1. Linear ODE Solution

```python
import numpy as np
from scipy import linalg

def main():
    # dx/dt = Ax, x(0) = x0
    # Solution: x(t) = exp(At) @ x0
    
    A = np.array([[-1, 1],
                  [0, -2]])
    x0 = np.array([1, 1])
    
    # Solution at t = 1
    t = 1
    x_t = linalg.expm(A * t) @ x0
    
    print(f"x(0) = {x0}")
    print(f"x({t}) = {x_t}")

if __name__ == "__main__":
    main()
```

### 2. State Transition Matrix

```python
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

def main():
    A = np.array([[-0.5, 1],
                  [-1, -0.5]])
    x0 = np.array([1, 0])
    
    times = np.linspace(0, 10, 100)
    trajectory = np.array([linalg.expm(A * t) @ x0 for t in times])
    
    fig, ax = plt.subplots()
    ax.plot(trajectory[:, 0], trajectory[:, 1])
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_title('System Trajectory')
    ax.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()
```

### 3. Rotation Matrix

```python
import numpy as np
from scipy import linalg

def main():
    # Skew-symmetric matrix generates rotation
    theta = np.pi / 4
    A = np.array([[0, -theta],
                  [theta, 0]])
    
    R = linalg.expm(A)
    
    print(f"Rotation by {np.degrees(theta)} degrees:")
    print(R)
    print()
    print("Expected:")
    print(np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]]))

if __name__ == "__main__":
    main()
```

## Summary

| Function | Description |
|:---------|:------------|
| `linalg.expm(A)` | Matrix exponential |
| `linalg.expm_frechet(A, E)` | Frechet derivative |

Key: $e^A \neq$ element-wise exp. Use `np.exp(A)` for element-wise.
