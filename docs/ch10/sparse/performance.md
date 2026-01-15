# Performance Tips

Best practices for sparse matrix performance.

## 1. Convert Once

```python
from scipy import sparse

# Bad: repeated conversion
for i in range(100):
    csr = coo.tocsr()
    result = csr @ x

# Good: convert once
csr = coo.tocsr()
for i in range(100):
    result = csr @ x
```

## 2. Use Right Format

| Operation | Best Format |
|:----------|:------------|
| A @ x | CSR |
| A[:, j] | CSC |
| A[i, :] | CSR |
| Build | LIL, COO |

## 3. Avoid Element Access

```python
# Bad: element-by-element
for i in range(n):
    for j in range(n):
        A[i, j] = func(i, j)

# Good: build with COO
rows, cols, data = [], [], []
for i in range(n):
    for j in range(n):
        if (val := func(i, j)) != 0:
            rows.append(i)
            cols.append(j)
            data.append(val)
A = sparse.coo_matrix((data, (rows, cols)))
```

## 4. Preallocate When Possible

Use `lil_matrix` for incremental builds, then convert.

## 5. Monitor Fill-in

Matrix products can dramatically increase density.
