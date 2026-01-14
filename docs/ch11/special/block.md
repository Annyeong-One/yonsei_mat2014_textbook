# Block Matrices

Constructing and working with block matrices.

## Block Diagonal

```python
import numpy as np
from scipy import linalg

def main():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = np.array([[9]])
    
    D = linalg.block_diag(A, B, C)
    print(D)

if __name__ == "__main__":
    main()
```

## Sparse Block Diagonal

```python
from scipy import sparse

def main():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    
    D = sparse.block_diag([A, B])
    print(D.toarray())

if __name__ == "__main__":
    main()
```
