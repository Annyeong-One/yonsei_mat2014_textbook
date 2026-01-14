# Format Selection Guide

Choose the right sparse format for your use case.

## Decision Tree

### 1. Building a Matrix?
- Use **LIL** or **COO** for construction
- Convert to CSR/CSC before computation

### 2. Row Operations?
- Use **CSR** for row slicing and matvec

### 3. Column Operations?
- Use **CSC** for column slicing

### 4. Banded Matrix?
- Use **DIA** for diagonal/banded structures

### 5. Solving Linear Systems?
- Use **CSC** for direct solvers
- Use **CSR** for iterative solvers

## Quick Reference

| Task | Recommended Format |
|:-----|:-------------------|
| Build incrementally | LIL, COO |
| Matrix-vector product | CSR |
| Row slicing | CSR |
| Column slicing | CSC |
| Direct solve (splu) | CSC |
| Iterative solve (cg) | CSR |
| Banded matrices | DIA |
| Format conversion | COO |

## Workflow

```python
from scipy import sparse

def main():
    # 1. Build with LIL
    lil = sparse.lil_matrix((1000, 1000))
    # ... add entries ...
    
    # 2. Convert to CSR for computation
    csr = lil.tocsr()
    
    # 3. Use CSR for all operations
    # ... matrix operations ...

if __name__ == "__main__":
    main()
```
