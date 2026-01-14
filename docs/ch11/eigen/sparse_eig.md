# Sparse Eigenvalues

`scipy.sparse.linalg` provides eigensolvers for large sparse matrices.

## eigs - General Sparse

### 1. Basic Usage

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    # Large sparse matrix
    n = 1000
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csr')
    
    # Find 6 largest eigenvalues
    eigenvalues, eigenvectors = splinalg.eigs(A, k=6)
    
    print("6 largest eigenvalues:")
    print(eigenvalues)

if __name__ == "__main__":
    main()
```

### 2. Which Eigenvalues

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 100
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csr')
    
    # 'LM' - largest magnitude (default)
    vals_LM, _ = splinalg.eigs(A, k=3, which='LM')
    
    # 'SM' - smallest magnitude
    vals_SM, _ = splinalg.eigs(A, k=3, which='SM')
    
    # 'LR' - largest real part
    vals_LR, _ = splinalg.eigs(A, k=3, which='LR')
    
    print("Largest magnitude:", vals_LM)
    print("Smallest magnitude:", vals_SM)
    print("Largest real:", vals_LR)

if __name__ == "__main__":
    main()
```

## eigsh - Symmetric Sparse

### 1. Basic Usage

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 1000
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csr')
    
    # For symmetric matrices - faster
    eigenvalues, eigenvectors = splinalg.eigsh(A, k=6)
    
    print("6 eigenvalues (real, sorted):")
    print(eigenvalues)

if __name__ == "__main__":
    main()
```

### 2. Smallest Eigenvalues

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 100
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format='csr')
    
    # Smallest algebraic eigenvalues
    vals_SA, _ = splinalg.eigsh(A, k=3, which='SA')
    
    # Largest algebraic eigenvalues
    vals_LA, _ = splinalg.eigsh(A, k=3, which='LA')
    
    print("Smallest:", vals_SA)
    print("Largest:", vals_LA)

if __name__ == "__main__":
    main()
```

## Applications

### 1. Graph Laplacian Spectrum

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    # Random sparse graph
    np.random.seed(42)
    n = 500
    A = sparse.random(n, n, density=0.02, format='csr')
    A = (A + A.T) / 2  # Symmetric
    A.data[:] = 1  # Binary
    
    # Laplacian
    D = sparse.diags(np.array(A.sum(axis=1)).flatten())
    L = D - A
    
    # Find smallest eigenvalues
    vals, vecs = splinalg.eigsh(L, k=10, which='SM')
    
    print("Smallest Laplacian eigenvalues:")
    print(vals)

if __name__ == "__main__":
    main()
```

### 2. Spectral Clustering

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    n = 200
    A = sparse.random(n, n, density=0.1, format='csr')
    A = (A + A.T) / 2
    
    D = sparse.diags(np.array(A.sum(axis=1)).flatten())
    L = D - A
    
    # Second smallest eigenvector for 2-way partition
    vals, vecs = splinalg.eigsh(L, k=2, which='SM')
    fiedler = vecs[:, 1]
    
    partition = fiedler > 0
    print(f"Partition sizes: {partition.sum()}, {(~partition).sum()}")

if __name__ == "__main__":
    main()
```

## Summary

| Function | Description |
|:---------|:------------|
| `splinalg.eigs(A, k)` | k eigenvalues of sparse A |
| `splinalg.eigsh(A, k)` | k eigenvalues of symmetric sparse A |
| `which='LM'` | Largest magnitude |
| `which='SM'` | Smallest magnitude |
| `which='SA'` | Smallest algebraic (eigsh) |
