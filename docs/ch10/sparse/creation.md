# Creating Sparse Matrices

Methods for constructing sparse matrices in SciPy.

## From Dense Array

### 1. Direct Conversion

```python
import numpy as np
from scipy import sparse

def main():
    A = np.array([[1, 0, 2],
                  [0, 0, 3],
                  [4, 5, 6]])
    
    csr = sparse.csr_matrix(A)
    csc = sparse.csc_matrix(A)
    coo = sparse.coo_matrix(A)
    
    print(f"CSR: {csr.nnz} nonzeros")
    print(f"CSC: {csc.nnz} nonzeros")
    print(f"COO: {coo.nnz} nonzeros")

if __name__ == "__main__":
    main()
```

## From Triplets

### 1. COO Format

```python
import numpy as np
from scipy import sparse

def main():
    row = np.array([0, 0, 1, 2, 2])
    col = np.array([0, 2, 2, 0, 1])
    data = np.array([1, 2, 3, 4, 5])
    
    A = sparse.coo_matrix((data, (row, col)), shape=(3, 3))
    
    print(A.toarray())

if __name__ == "__main__":
    main()
```

## Diagonal Matrices

### 1. sparse.diags

```python
import numpy as np
from scipy import sparse

def main():
    # Tridiagonal
    n = 5
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n))
    
    print(A.toarray())

if __name__ == "__main__":
    main()
```

### 2. Multiple Diagonals

```python
import numpy as np
from scipy import sparse

def main():
    diagonals = [np.ones(4), 2*np.ones(5), np.ones(4)]
    A = sparse.diags(diagonals, [-1, 0, 1])
    
    print(A.toarray())

if __name__ == "__main__":
    main()
```

## Special Matrices

### 1. Identity

```python
from scipy import sparse

def main():
    I = sparse.eye(5)
    print(I.toarray())

if __name__ == "__main__":
    main()
```

### 2. Random Sparse

```python
from scipy import sparse

def main():
    A = sparse.random(5, 5, density=0.3, format='csr')
    print(f"Density: {A.nnz / 25:.2f}")
    print(A.toarray().round(2))

if __name__ == "__main__":
    main()
```

## Incremental Building

### 1. LIL Matrix

```python
from scipy import sparse

def main():
    lil = sparse.lil_matrix((5, 5))
    
    # Add entries one by one
    lil[0, 0] = 1
    lil[1, 1] = 2
    lil[2, 2] = 3
    lil[0, 4] = 4
    
    # Convert for computation
    csr = lil.tocsr()
    print(csr.toarray())

if __name__ == "__main__":
    main()
```

## Summary

| Method | Use Case |
|:-------|:---------|
| `csr_matrix(A)` | From dense array |
| `coo_matrix((data, (row, col)))` | From triplets |
| `diags(d, offsets)` | Diagonal/banded |
| `eye(n)` | Identity matrix |
| `random(m, n, density)` | Random sparse |
| `lil_matrix((m, n))` | Incremental build |
