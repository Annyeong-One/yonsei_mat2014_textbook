# Matrix Norms


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Compute vector and matrix norms using `np.linalg.norm`.

## Vector Norms

### 1. L2 Norm (Euclidean)

```python
import numpy as np

def main():
    x = np.array([3, 4])
    
    norm_l2 = np.linalg.norm(x)
    
    print(f"x = {x}")
    print(f"||x||_2 = {norm_l2}")
    print(f"Manual: sqrt(3² + 4²) = {np.sqrt(3**2 + 4**2)}")

if __name__ == "__main__":
    main()
```

### 2. L1 Norm (Manhattan)

```python
import numpy as np

def main():
    x = np.array([3, -4, 2])
    
    norm_l1 = np.linalg.norm(x, ord=1)
    
    print(f"x = {x}")
    print(f"||x||_1 = {norm_l1}")
    print(f"Manual: |3| + |-4| + |2| = {np.abs(x).sum()}")

if __name__ == "__main__":
    main()
```

### 3. L∞ Norm (Max)

```python
import numpy as np

def main():
    x = np.array([3, -7, 2])
    
    norm_inf = np.linalg.norm(x, ord=np.inf)
    
    print(f"x = {x}")
    print(f"||x||_∞ = {norm_inf}")
    print(f"Manual: max(|3|, |-7|, |2|) = {np.abs(x).max()}")

if __name__ == "__main__":
    main()
```

## General p-Norm

### 1. Mathematical Form

$$\|x\|_p = \left( \sum_i |x_i|^p \right)^{1/p}$$

### 2. Different p Values

```python
import numpy as np

def main():
    x = np.array([1, 2, 3, 4])
    
    print(f"x = {x}")
    print()
    
    for p in [1, 2, 3, 5, 10, np.inf]:
        norm = np.linalg.norm(x, ord=p)
        print(f"||x||_{p} = {norm:.4f}")

if __name__ == "__main__":
    main()
```

### 3. Convergence to Max

As p → ∞, p-norm converges to max norm.

```python
import numpy as np

def main():
    x = np.array([1, 5, 2, 3])
    
    max_val = np.abs(x).max()
    
    print(f"x = {x}")
    print(f"Max element: {max_val}")
    print()
    
    for p in [1, 2, 5, 10, 50, 100]:
        norm = np.linalg.norm(x, ord=p)
        print(f"p={p:3}: {norm:.6f}")

if __name__ == "__main__":
    main()
```

## Matrix Norms

### 1. Frobenius Norm

```python
import numpy as np

def main():
    A = np.array([[1, 2],
                  [3, 4]])
    
    norm_fro = np.linalg.norm(A, 'fro')
    
    print("A =")
    print(A)
    print(f"||A||_F = {norm_fro:.4f}")
    print(f"Manual: sqrt(1² + 2² + 3² + 4²) = {np.sqrt(np.sum(A**2)):.4f}")

if __name__ == "__main__":
    main()
```

### 2. Spectral Norm (2-norm)

Largest singular value.

```python
import numpy as np

def main():
    A = np.array([[1, 2],
                  [3, 4]])
    
    norm_2 = np.linalg.norm(A, 2)
    
    # Verify: largest singular value
    s = np.linalg.svd(A, compute_uv=False)
    
    print("A =")
    print(A)
    print(f"||A||_2 = {norm_2:.4f}")
    print(f"Largest singular value: {s[0]:.4f}")

if __name__ == "__main__":
    main()
```

### 3. Other Matrix Norms

```python
import numpy as np

def main():
    A = np.array([[1, -2, 3],
                  [-4, 5, -6]])
    
    print("A =")
    print(A)
    print()
    
    # Frobenius norm (default for matrices)
    print(f"Frobenius: {np.linalg.norm(A, 'fro'):.4f}")
    
    # Induced 2-norm (spectral)
    print(f"Spectral (2): {np.linalg.norm(A, 2):.4f}")
    
    # Induced 1-norm (max column sum)
    print(f"1-norm: {np.linalg.norm(A, 1):.4f}")
    
    # Induced inf-norm (max row sum)
    print(f"∞-norm: {np.linalg.norm(A, np.inf):.4f}")
    
    # Nuclear norm (sum of singular values)
    print(f"Nuclear: {np.linalg.norm(A, 'nuc'):.4f}")

if __name__ == "__main__":
    main()
```

## Axis Parameter

### 1. Row Norms

```python
import numpy as np

def main():
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    # L2 norm of each row
    row_norms = np.linalg.norm(A, axis=1)
    
    print("A =")
    print(A)
    print(f"Row norms: {row_norms}")

if __name__ == "__main__":
    main()
```

### 2. Column Norms

```python
import numpy as np

def main():
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    # L2 norm of each column
    col_norms = np.linalg.norm(A, axis=0)
    
    print("A =")
    print(A)
    print(f"Column norms: {col_norms}")

if __name__ == "__main__":
    main()
```

### 3. Batch Norms

```python
import numpy as np

def main():
    # Batch of vectors (10 vectors, each length 5)
    X = np.random.randn(10, 5)
    
    # Norm of each vector
    norms = np.linalg.norm(X, axis=1)
    
    print(f"X shape: {X.shape}")
    print(f"Norms shape: {norms.shape}")
    print(f"Norms: {norms}")

if __name__ == "__main__":
    main()
```

## Applications

### 1. Normalization

```python
import numpy as np

def main():
    x = np.array([3, 4, 0])
    
    # Unit vector
    x_normalized = x / np.linalg.norm(x)
    
    print(f"Original: {x}")
    print(f"Normalized: {x_normalized}")
    print(f"Norm of normalized: {np.linalg.norm(x_normalized):.10f}")

if __name__ == "__main__":
    main()
```

### 2. Distance

```python
import numpy as np

def main():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    
    # Euclidean distance
    distance = np.linalg.norm(a - b)
    
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"||a - b|| = {distance:.4f}")

if __name__ == "__main__":
    main()
```

### 3. Matrix Error

```python
import numpy as np

def main():
    A = np.array([[1, 2],
                  [3, 4]])
    B = np.array([[1.1, 1.9],
                  [3.05, 4.1]])
    
    # Frobenius error
    error = np.linalg.norm(A - B, 'fro')
    
    # Relative error
    rel_error = error / np.linalg.norm(A, 'fro')
    
    print(f"Absolute error: {error:.4f}")
    print(f"Relative error: {rel_error:.4%}")

if __name__ == "__main__":
    main()
```

## Regularization

### 1. L2 Regularization

```python
import numpy as np

def main():
    np.random.seed(42)
    
    # Model weights
    w = np.random.randn(10)
    
    # L2 regularization (weight decay)
    lambda_reg = 0.01
    l2_penalty = lambda_reg * np.linalg.norm(w) ** 2
    
    print(f"Weights norm: {np.linalg.norm(w):.4f}")
    print(f"L2 penalty: {l2_penalty:.4f}")

if __name__ == "__main__":
    main()
```

### 2. L1 Regularization

```python
import numpy as np

def main():
    np.random.seed(42)
    
    # Model weights
    w = np.random.randn(10)
    
    # L1 regularization (sparsity)
    lambda_reg = 0.01
    l1_penalty = lambda_reg * np.linalg.norm(w, 1)
    
    print(f"Weights L1 norm: {np.linalg.norm(w, 1):.4f}")
    print(f"L1 penalty: {l1_penalty:.4f}")

if __name__ == "__main__":
    main()
```

### 3. Nuclear Norm

Low-rank regularization for matrices.

```python
import numpy as np

def main():
    np.random.seed(42)
    
    # Matrix (e.g., recommendation matrix)
    M = np.random.randn(5, 4)
    
    # Nuclear norm = sum of singular values
    nuclear_norm = np.linalg.norm(M, 'nuc')
    
    # Verify with SVD
    s = np.linalg.svd(M, compute_uv=False)
    
    print(f"Nuclear norm: {nuclear_norm:.4f}")
    print(f"Sum of singular values: {s.sum():.4f}")

if __name__ == "__main__":
    main()
```

## Summary Table

### 1. Vector Norms

| Norm | `ord` | Formula |
|:-----|:------|:--------|
| L1 | `1` | $\sum \|x_i\|$ |
| L2 | `2` or None | $\sqrt{\sum x_i^2}$ |
| L∞ | `np.inf` | $\max \|x_i\|$ |
| p-norm | `p` | $(\sum \|x_i\|^p)^{1/p}$ |

### 2. Matrix Norms

| Norm | `ord` | Description |
|:-----|:------|:------------|
| Frobenius | `'fro'` | $\sqrt{\sum_{ij} A_{ij}^2}$ |
| Spectral | `2` | Largest singular value |
| Nuclear | `'nuc'` | Sum of singular values |
| 1-norm | `1` | Max column sum |
| ∞-norm | `np.inf` | Max row sum |

### 3. Choosing a Norm

- **Distance**: L2 (Euclidean)
- **Sparsity**: L1
- **Matrix approximation error**: Frobenius
- **Matrix condition**: Spectral (2-norm)
