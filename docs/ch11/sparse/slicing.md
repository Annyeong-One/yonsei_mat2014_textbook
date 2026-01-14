# Slicing and Indexing

Accessing elements and submatrices in sparse matrices.

## Element Access

### 1. Single Element

```python
from scipy import sparse

def main():
    A = sparse.csr_matrix([[1, 0, 2],
                           [0, 3, 0],
                           [4, 0, 5]])
    
    print(f"A[0, 0] = {A[0, 0]}")
    print(f"A[0, 2] = {A[0, 2]}")
    print(f"A[1, 0] = {A[1, 0]}")  # Zero element

if __name__ == "__main__":
    main()
```

## Row and Column Slicing

### 1. Row Slicing (CSR efficient)

```python
from scipy import sparse

def main():
    A = sparse.csr_matrix([[1, 0, 2],
                           [0, 3, 0],
                           [4, 0, 5]])
    
    row_0 = A[0, :]
    rows_0_1 = A[0:2, :]
    
    print("Row 0:")
    print(row_0.toarray())
    print()
    print("Rows 0-1:")
    print(rows_0_1.toarray())

if __name__ == "__main__":
    main()
```

### 2. Column Slicing (CSC efficient)

```python
from scipy import sparse

def main():
    A = sparse.csc_matrix([[1, 0, 2],
                           [0, 3, 0],
                           [4, 0, 5]])
    
    col_0 = A[:, 0]
    cols_0_1 = A[:, 0:2]
    
    print("Column 0:")
    print(col_0.toarray())

if __name__ == "__main__":
    main()
```

## Fancy Indexing

### 1. Row Selection

```python
from scipy import sparse
import numpy as np

def main():
    A = sparse.csr_matrix([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9],
                           [10, 11, 12]])
    
    rows = [0, 2, 3]
    B = A[rows, :]
    
    print("Selected rows [0, 2, 3]:")
    print(B.toarray())

if __name__ == "__main__":
    main()
```

### 2. Boolean Indexing

```python
from scipy import sparse
import numpy as np

def main():
    A = sparse.csr_matrix([[1, 2], [3, 4], [5, 6]])
    
    mask = np.array([True, False, True])
    B = A[mask, :]
    
    print("Boolean selected rows:")
    print(B.toarray())

if __name__ == "__main__":
    main()
```

## Modifying Elements

### 1. Set Single Element

```python
from scipy import sparse

def main():
    A = sparse.lil_matrix((3, 3))
    
    A[0, 0] = 1
    A[1, 1] = 2
    A[2, 2] = 3
    
    print(A.toarray())

if __name__ == "__main__":
    main()
```

### 2. LIL for Modification

```python
from scipy import sparse

def main():
    # CSR is inefficient for element-by-element modification
    # Use LIL, then convert
    
    lil = sparse.lil_matrix((5, 5))
    for i in range(5):
        lil[i, i] = i + 1
    
    csr = lil.tocsr()
    print(csr.toarray())

if __name__ == "__main__":
    main()
```

## Performance

### 1. Format Matters

| Operation | CSR | CSC | COO |
|:----------|:----|:----|:----|
| Row slice | Fast | Slow | Slow |
| Col slice | Slow | Fast | Slow |
| Element access | Medium | Medium | Slow |
| Modification | Slow | Slow | Fast |

## Summary

- Use CSR for row operations
- Use CSC for column operations  
- Use LIL for building/modifying
- Avoid element-by-element access on CSR/CSC
