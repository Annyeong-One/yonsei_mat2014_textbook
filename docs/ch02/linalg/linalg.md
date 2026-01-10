# Linear Algebra

NumPy provides a rich set of linear algebra routines built on optimized BLAS and LAPACK libraries. These are central to quantitative finance, statistics, and machine learning.

---

## Vectors and matrices

In NumPy:
- 1D arrays represent vectors,
- 2D arrays represent matrices.

```python
import numpy as np

v = np.array([1.0, 2.0, 3.0])
A = np.array([[1.0, 0.0],
              [0.0, 1.0]])
```

---

## Matrix operations

### 1. Matrix

Use the `@` operator:

```python
A @ A
A @ v[:2]
```

This performs true linear algebra multiplication (not elementwise).

### 2. Transpose

```python
A.T
```

---

## Linear algebra

The `np.linalg` submodule includes:

```python
np.linalg.inv(A)      # inverse
np.linalg.det(A)      # determinant
np.linalg.eig(A)      # eigenvalues/eigenvectors
np.linalg.solve(A, b) # solve Ax = b
```

Avoid explicit inverses when solving systems.

---

## Numerical

- Linear algebra is numerically sensitive.
- Conditioning matters.
- Small perturbations can cause large errors.

Use stable algorithms (`solve` over `inv`).

---

## Financial

Linear algebra underlies:
- portfolio optimization,
- factor models,
- PCA and risk decomposition,
- regression and calibration.

---

## Key takeaways

- Use `@` for matrix multiplication.
- Prefer `solve` to explicit inverses.
- Numerical stability matters.
