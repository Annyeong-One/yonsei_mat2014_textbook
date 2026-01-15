# Why Sparse Matrices

Sparse matrices efficiently represent matrices with mostly zero entries.

## Memory Efficiency

### 1. Dense vs Sparse Storage

```python
import numpy as np
from scipy import sparse
import sys

def main():
    n = 10000
    density = 0.001  # 0.1% nonzero
    
    # Dense storage
    A_dense = np.zeros((n, n))
    k = int(n * n * density)
    rows = np.random.randint(0, n, k)
    cols = np.random.randint(0, n, k)
    A_dense[rows, cols] = np.random.randn(k)
    
    # Sparse storage
    A_sparse = sparse.csr_matrix(A_dense)
    
    dense_size = A_dense.nbytes
    sparse_size = A_sparse.data.nbytes + A_sparse.indices.nbytes + A_sparse.indptr.nbytes
    
    print(f"Matrix size: {n} x {n}")
    print(f"Nonzeros: {k} ({density*100}%)")
    print(f"Dense storage:  {dense_size / 1e6:.1f} MB")
    print(f"Sparse storage: {sparse_size / 1e6:.3f} MB")
    print(f"Compression: {dense_size / sparse_size:.0f}x")

if __name__ == "__main__":
    main()
```

### 2. Complexity Analysis

| Storage | Memory |
|:--------|:-------|
| Dense | $O(mn)$ |
| Sparse | $O(k)$ where $k$ = nonzeros |

### 3. When Sparse Wins

```python
import numpy as np
from scipy import sparse

def main():
    n = 1000
    
    for density in [0.001, 0.01, 0.1, 0.5]:
        k = int(n * n * density)
        
        dense_mem = n * n * 8  # 8 bytes per float64
        sparse_mem = k * 8 + k * 4 + (n + 1) * 4  # data + indices + indptr
        
        ratio = dense_mem / sparse_mem
        winner = "Sparse" if ratio > 1 else "Dense"
        
        print(f"Density {density*100:5.1f}%: {winner} wins ({ratio:.1f}x)")

if __name__ == "__main__":
    main()
```

## Computational Efficiency

### 1. Matrix-Vector Multiply

```python
import numpy as np
from scipy import sparse
import time

def main():
    n = 5000
    density = 0.01
    
    # Create sparse matrix
    A_sparse = sparse.random(n, n, density=density, format='csr')
    A_dense = A_sparse.toarray()
    x = np.random.randn(n)
    
    # Dense multiplication
    start = time.perf_counter()
    for _ in range(10):
        y_dense = A_dense @ x
    dense_time = time.perf_counter() - start
    
    # Sparse multiplication
    start = time.perf_counter()
    for _ in range(10):
        y_sparse = A_sparse @ x
    sparse_time = time.perf_counter() - start
    
    print(f"Dense:  {dense_time:.4f} sec")
    print(f"Sparse: {sparse_time:.4f} sec")
    print(f"Speedup: {dense_time/sparse_time:.1f}x")

if __name__ == "__main__":
    main()
```

### 2. Operation Complexity

| Operation | Dense | Sparse |
|:----------|:------|:-------|
| $Ax$ (matrix-vector) | $O(n^2)$ | $O(k)$ |
| $A + B$ | $O(n^2)$ | $O(k_A + k_B)$ |
| Memory | $O(n^2)$ | $O(k)$ |

## Where Sparse Matrices Arise

### 1. PDEs (Finite Differences)

```python
import numpy as np
from scipy import sparse

def main():
    # 1D Laplacian: tridiagonal
    n = 100
    A = sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n))
    
    print(f"1D Laplacian ({n}x{n})")
    print(f"Nonzeros: {A.nnz}")
    print(f"Density: {A.nnz / (n*n) * 100:.2f}%")

if __name__ == "__main__":
    main()
```

### 2. Graphs (Adjacency)

```python
import numpy as np
from scipy import sparse

def main():
    # Social network: each person has ~150 connections
    n_people = 1_000_000
    avg_connections = 150
    
    # Theoretical storage
    dense_gb = n_people * n_people * 8 / 1e9
    sparse_gb = n_people * avg_connections * 12 / 1e9  # data + indices
    
    print(f"Network: {n_people:,} people, {avg_connections} avg connections")
    print(f"Dense storage:  {dense_gb:,.0f} GB (impossible)")
    print(f"Sparse storage: {sparse_gb:.2f} GB (feasible)")

if __name__ == "__main__":
    main()
```

### 3. Machine Learning (Features)

```python
import numpy as np
from scipy import sparse

def main():
    # Text classification: bag of words
    n_documents = 100_000
    vocabulary = 50_000
    avg_words_per_doc = 200
    
    # Feature matrix
    dense_gb = n_documents * vocabulary * 8 / 1e9
    sparse_gb = n_documents * avg_words_per_doc * 12 / 1e9
    
    print(f"Documents: {n_documents:,}")
    print(f"Vocabulary: {vocabulary:,}")
    print(f"Dense:  {dense_gb:.1f} GB")
    print(f"Sparse: {sparse_gb:.2f} GB")

if __name__ == "__main__":
    main()
```

## Summary

### 1. Use Sparse When

- Most entries are zero (density < 10%)
- Matrix is too large for dense storage
- Structure enables sparse operations

### 2. Use Dense When

- Matrix is small
- High density (> 30%)
- Need all dense operations
