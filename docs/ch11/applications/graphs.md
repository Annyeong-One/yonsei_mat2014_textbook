# Graph Algorithms

Sparse matrices for graph representation and analysis.

## Adjacency Matrix

```python
import numpy as np
from scipy import sparse

def main():
    # Graph edges: (from, to)
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
    n_nodes = 4
    
    row = [e[0] for e in edges]
    col = [e[1] for e in edges]
    data = np.ones(len(edges))
    
    # Undirected: symmetrize
    A = sparse.csr_matrix((data, (row, col)), shape=(n_nodes, n_nodes))
    A = A + A.T
    
    print("Adjacency matrix:")
    print(A.toarray())

if __name__ == "__main__":
    main()
```

## Graph Laplacian

```python
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg

def main():
    A = sparse.csr_matrix([[0, 1, 1, 0],
                           [1, 0, 1, 0],
                           [1, 1, 0, 1],
                           [0, 0, 1, 0]])
    
    # Degree matrix
    D = sparse.diags(np.array(A.sum(axis=1)).flatten())
    
    # Laplacian
    L = D - A
    
    # Smallest eigenvalues (connectivity)
    vals, vecs = splinalg.eigsh(L.astype(float), k=2, which='SM')
    print(f"Smallest eigenvalues: {vals}")

if __name__ == "__main__":
    main()
```

Graph connected iff second smallest Laplacian eigenvalue > 0.
