# Block Matrices

Block matrices arise naturally when a system has multiple components that interact in a structured way — for example, coupled differential equations, multi-asset portfolio models, or finite element discretizations. A block diagonal matrix places smaller matrices along the diagonal with zeros elsewhere, preserving the independence of each block. SciPy provides both dense and sparse constructors for block diagonal matrices.

```python
import numpy as np
from scipy import linalg
```

---

## Block Diagonal Matrix

A block diagonal matrix has the form

$$
D = \begin{pmatrix} A_1 & 0 & \cdots & 0 \\ 0 & A_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & A_k \end{pmatrix}
$$

where each $A_i$ is a square (or rectangular) matrix and all off-diagonal blocks are zero.

### Key Properties

- **Determinant**: $\det(D) = \det(A_1) \cdot \det(A_2) \cdots \det(A_k)$
- **Eigenvalues**: the eigenvalues of $D$ are the union of eigenvalues of each $A_i$
- **Inverse**: if each $A_i$ is invertible, then $D^{-1} = \mathrm{diag}(A_1^{-1}, A_2^{-1}, \ldots, A_k^{-1})$

### Construction with scipy.linalg.block_diag

`linalg.block_diag` takes any number of arrays and places them along the diagonal of a new matrix, filling the rest with zeros.

```python
def main():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = np.array([[9]])

    D = linalg.block_diag(A, B, C)
    print(D)

if __name__ == "__main__":
    main()
```

```
[[1 2 0 0 0]
 [3 4 0 0 0]
 [0 0 5 6 0]
 [0 0 7 8 0]
 [0 0 0 0 9]]
```

The 2x2 block $A$ occupies the top-left corner, the 2x2 block $B$ is in the center, and the 1x1 block $C$ is in the bottom-right.

---

## Sparse Block Diagonal

For large-scale problems where the blocks are small relative to the total matrix size, the dense representation wastes memory storing zeros. The sparse variant `scipy.sparse.block_diag` returns a sparse matrix that stores only the nonzero entries.

```python
from scipy import sparse

def main():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    D = sparse.block_diag([A, B])
    print(D.toarray())
    print(f"Format: {D.format}")
    print(f"Nonzeros: {D.nnz} out of {D.shape[0] * D.shape[1]} entries")

if __name__ == "__main__":
    main()
```

```
[[1 2 0 0]
 [3 4 0 0]
 [0 0 5 6]
 [0 0 7 8]]
Format: coo
Nonzeros: 8 out of 16 entries
```

!!! tip "When to Use Sparse"
    The sparse variant becomes worthwhile when the total matrix dimension is much larger than the individual block sizes. For a block diagonal with 100 blocks of size 3x3, the dense matrix is 300x300 (90,000 entries) but only 900 are nonzero — a 99% savings in memory.

---

## General Block Matrices with np.block

NumPy's `np.block` constructs arbitrary block matrices (not just block diagonal) from a nested list of arrays.

```python
A = np.ones((2, 2))
B = np.zeros((2, 3))
C = np.zeros((3, 2))
D = np.eye(3)

# 2x2 block structure
M = np.block([
    [A, B],
    [C, D]
])
print(M)
```

```
[[1. 1. 0. 0. 0.]
 [1. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
```

The nested list structure mirrors the block layout: `[[top-left, top-right], [bottom-left, bottom-right]]`. The inner arrays must have compatible shapes along the concatenation axes.

---

## Summary

| Function | Purpose | Returns |
|----------|---------|---------|
| `scipy.linalg.block_diag(A, B, ...)` | Dense block diagonal matrix | NumPy array |
| `scipy.sparse.block_diag([A, B, ...])` | Sparse block diagonal matrix | Sparse matrix (COO) |
| `np.block([[A, B], [C, D]])` | General block matrix from nested list | NumPy array |

**Key Takeaways**:

- Block diagonal matrices preserve the eigenvalues, determinant, and invertibility structure of the individual blocks
- Use `scipy.linalg.block_diag` for small dense block diagonal matrices
- Use `scipy.sparse.block_diag` when the total size is large and memory matters
- Use `np.block` for general (non-diagonal) block matrix construction from a nested list of arrays
