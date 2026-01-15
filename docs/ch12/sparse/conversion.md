# Format Conversion

Converting between sparse matrix formats.

## Conversion Methods

### 1. To CSR

```python
from scipy import sparse

def main():
    coo = sparse.random(5, 5, density=0.3, format='coo')
    csr = coo.tocsr()
    print(f"Converted to CSR: {type(csr)}")

if __name__ == "__main__":
    main()
```

### 2. To CSC

```python
from scipy import sparse

def main():
    csr = sparse.random(5, 5, density=0.3, format='csr')
    csc = csr.tocsc()
    print(f"Converted to CSC: {type(csc)}")

if __name__ == "__main__":
    main()
```

### 3. To Dense

```python
from scipy import sparse

def main():
    csr = sparse.random(5, 5, density=0.3, format='csr')
    
    # Method 1
    dense1 = csr.toarray()
    
    # Method 2
    dense2 = csr.todense()  # Returns matrix
    
    print(type(dense1))  # ndarray
    print(type(dense2))  # matrix

if __name__ == "__main__":
    main()
```

## Conversion Table

| From/To | `.tocsr()` | `.tocsc()` | `.tocoo()` | `.tolil()` | `.toarray()` |
|:--------|:-----------|:-----------|:-----------|:-----------|:-------------|
| CSR | - | Fast | Fast | Slow | Fast |
| CSC | Fast | - | Fast | Slow | Fast |
| COO | Fast | Fast | - | Fast | Fast |
| LIL | Fast | Fast | Fast | - | Fast |

## Best Practices

### 1. Build then Convert

```python
from scipy import sparse

def main():
    # Build with LIL
    lil = sparse.lil_matrix((1000, 1000))
    for i in range(1000):
        lil[i, i] = 2
        if i > 0:
            lil[i, i-1] = -1
    
    # Convert once for computation
    csr = lil.tocsr()
    
    # Use CSR for all operations
    x = csr @ [1]*1000
    print(f"Result norm: {sum(x)}")

if __name__ == "__main__":
    main()
```

### 2. Avoid Repeated Conversion

```python
from scipy import sparse
import time

def main():
    A = sparse.random(1000, 1000, density=0.01, format='coo')
    
    # Bad: convert every iteration
    start = time.perf_counter()
    for _ in range(100):
        csr = A.tocsr()
        _ = csr.sum()
    bad_time = time.perf_counter() - start
    
    # Good: convert once
    start = time.perf_counter()
    csr = A.tocsr()
    for _ in range(100):
        _ = csr.sum()
    good_time = time.perf_counter() - start
    
    print(f"Bad (repeated): {bad_time:.4f} sec")
    print(f"Good (once):    {good_time:.4f} sec")

if __name__ == "__main__":
    main()
```

## Summary

- Use `.tocsr()` for row operations and general arithmetic
- Use `.tocsc()` for column operations
- Use `.toarray()` only for small matrices or visualization
- Convert once, use many times
