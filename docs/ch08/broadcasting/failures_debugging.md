# Broadcasting Failures and Debugging

Broadcasting errors are among the most common NumPy mistakes, yet the error messages can be cryptic for newcomers. When shapes are incompatible, NumPy raises a `ValueError` that reports the mismatched shapes but does not explain which axis failed or how to fix it. This page catalogs the most frequent failure patterns and provides systematic debugging techniques.

---

## The Error Message

Every broadcasting failure produces the same `ValueError` format.

### 1. Standard Error Format

```python
import numpy as np

def main():
    A = np.ones((3, 4))
    B = np.ones((3, 5))
    try:
        C = A + B
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

Output:

```
Error: operands could not be broadcast together with shapes (3,4) (3,5)
```

### 2. Reading the Error

The error reports both shapes. Align them from the right to find the incompatible axis:

```
A: (3, 4)
B: (3, 5)
        ↑ 4 != 5, neither is 1 → failure
```

### 3. Three-operand Errors

When chaining operations, the error may involve an intermediate result:

```python
import numpy as np

def main():
    A = np.ones((2, 3))
    B = np.ones((3, 4))
    try:
        C = A + B
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```


## Same-Rank Failures

Both arrays have the same number of dimensions but incompatible sizes.

### 1. Trailing Dimension Mismatch

```python
import numpy as np

def main():
    A = np.ones((4, 3))
    B = np.ones((4, 5))
    try:
        C = A + B  # axis 1: 3 != 5
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### 2. Leading Dimension Mismatch

```python
import numpy as np

def main():
    A = np.ones((3, 4))
    B = np.ones((5, 4))
    try:
        C = A + B  # axis 0: 3 != 5
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### 3. Multiple Axis Mismatch

```python
import numpy as np

def main():
    A = np.ones((3, 4, 5))
    B = np.ones((2, 4, 6))
    try:
        C = A + B  # axis 0: 3 != 2, axis 2: 5 != 6
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```


## Different-Rank Failures

The shorter shape is prepended with ones, but trailing dimensions still must match.

### 1. 1D vs 2D Mismatch

```python
import numpy as np

def main():
    M = np.ones((3, 4))
    v = np.array([1, 2, 3])  # (3,) → (1, 3), but axis 1: 3 != 4
    try:
        result = M + v
    except ValueError as e:
        print(f"Error: {e}")

    # Fix: v should have 4 elements to match axis 1
    v_fixed = np.array([1, 2, 3, 4])
    result = M + v_fixed
    print(f"Fixed result shape: {result.shape}")

if __name__ == "__main__":
    main()
```

### 2. Intended Row Operation

A common mistake: trying to add a vector along rows instead of columns.

```python
import numpy as np

def main():
    M = np.ones((3, 4))
    row_vals = np.array([10, 20, 30])  # (3,) — wrong: aligns with axis 1

    try:
        result = M + row_vals
    except ValueError as e:
        print(f"Error: {e}")

    # Fix: reshape to column vector
    result = M + row_vals[:, np.newaxis]  # (3, 1) broadcasts correctly
    print(f"Fixed result shape: {result.shape}")

if __name__ == "__main__":
    main()
```

### 3. 1D vs 3D Mismatch

```python
import numpy as np

def main():
    A = np.ones((2, 3, 4))
    v = np.array([1, 2, 3])  # (3,) → (1, 1, 3), axis 2: 3 != 4
    try:
        result = A + v
    except ValueError as e:
        print(f"Error: {e}")

    # Fix: reshape to (1, 3, 1) to align with axis 1
    result = A + v[np.newaxis, :, np.newaxis]
    print(f"Fixed result shape: {result.shape}")

if __name__ == "__main__":
    main()
```


## Silent Broadcasting Bugs

Worse than errors: operations that succeed but produce wrong results.

### 1. Accidental Outer Operation

```python
import numpy as np

def main():
    prices = np.array([100, 200, 300])       # (3,) — 3 assets
    weights = np.array([0.5, 0.3, 0.2])[:, np.newaxis]  # (3, 1) — oops

    # Intended: element-wise multiply → (3,)
    # Actual: outer product → (3, 3)
    result = prices * weights
    print(f"Expected shape: (3,)")
    print(f"Actual shape:   {result.shape}")
    print(result)

if __name__ == "__main__":
    main()
```

### 2. Shape (n,) vs (n, 1) vs (1, n)

```python
import numpy as np

def main():
    v = np.array([1, 2, 3])
    print(f"v.shape           = {v.shape}")          # (3,)
    print(f"v[:, None].shape  = {v[:, None].shape}")  # (3, 1)
    print(f"v[None, :].shape  = {v[None, :].shape}")  # (1, 3)

    # These produce different results with a (3, 3) matrix
    M = np.ones((3, 3))
    print(f"M + v      → shape {(M + v).shape}")             # (3, 3) — adds to each row
    print(f"M + v[:,None] → shape {(M + v[:, None]).shape}")  # (3, 3) — adds to each column

if __name__ == "__main__":
    main()
```

### 3. Detecting Silent Bugs

Always verify the output shape matches your expectation:

```python
import numpy as np

def main():
    A = np.ones((100, 5))
    B = np.ones((5, 1))
    result = A * B
    expected_shape = (100, 5)
    assert result.shape == expected_shape, (
        f"Shape mismatch: got {result.shape}, expected {expected_shape}"
    )
    print("Shape check passed")

if __name__ == "__main__":
    main()
```


## Debugging Techniques

Systematic approaches to diagnose broadcasting problems.

### 1. Print Shapes Before the Operation

```python
import numpy as np

def main():
    A = np.random.randn(10, 3)
    B = np.random.randn(3, 1)
    print(f"A.shape = {A.shape}")
    print(f"B.shape = {B.shape}")
    # Visually right-align:
    # A: (10, 3)
    # B:  (3, 1)
    # axis 0: 10 vs 3 — neither is 1 → would fail if both were same ndim
    # But B is prepended: (1, 3, 1)? No — B is 2D, A is 2D → no prepending
    # axis 0: 10 vs 3 — FAIL
    try:
        C = A + B
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### 2. Use np.broadcast_shapes

```python
import numpy as np

def main():
    # Test compatibility without creating arrays
    try:
        result_shape = np.broadcast_shapes((3, 4), (4,))
        print(f"Compatible: {result_shape}")
    except ValueError as e:
        print(f"Incompatible: {e}")

    try:
        result_shape = np.broadcast_shapes((3, 4), (3,))
        print(f"Compatible: {result_shape}")
    except ValueError as e:
        print(f"Incompatible: {e}")

if __name__ == "__main__":
    main()
```

Output:

```
Compatible: (3, 4)
Incompatible: shape mismatch: objects cannot be broadcast to a single shape.  Mismatch is between arg 0 with shape (3, 4) and arg 1 with shape (3,).
```

### 3. Use np.broadcast_to for Inspection

```python
import numpy as np

def main():
    v = np.array([1, 2, 3])
    # See what v looks like when broadcast to (4, 3)
    expanded = np.broadcast_to(v, (4, 3))
    print(f"Original shape: {v.shape}")
    print(f"Broadcast shape: {expanded.shape}")
    print(expanded)

if __name__ == "__main__":
    main()
```


## Quick Fix Reference

Common errors and their one-line fixes.

### 1. Fix Table

| Error Shapes | Intended Operation | Fix |
|---|---|---|
| `(m, n)` + `(m,)` | Add along rows | `v[:, np.newaxis]` makes `(m, 1)` |
| `(m, n)` + `(k,)` where `k != n` | Wrong vector length | Use vector of length `n` |
| `(a, b, c)` + `(b,)` | Add along middle axis | `v[np.newaxis, :, np.newaxis]` |
| `(m,)` + `(n,)` where `m != n` | Element-wise | Ensure same length |

### 2. The reshape Approach

```python
import numpy as np

def main():
    A = np.ones((2, 3, 4))
    v = np.array([10, 20, 30])  # want to add along axis 1

    # Method 1: np.newaxis
    result1 = A + v[np.newaxis, :, np.newaxis]

    # Method 2: reshape
    result2 = A + v.reshape(1, 3, 1)

    print(np.allclose(result1, result2))  # True

if __name__ == "__main__":
    main()
```

### 3. The expand_dims Approach

```python
import numpy as np

def main():
    A = np.ones((2, 3, 4))
    v = np.array([10, 20, 30])

    v_expanded = np.expand_dims(v, axis=(0, 2))  # (1, 3, 1)
    result = A + v_expanded
    print(f"result.shape = {result.shape}")

if __name__ == "__main__":
    main()
```


## Summary

Broadcasting failures follow predictable patterns. The key debugging strategy is to right-align the shapes and check each axis pair: both sizes must be equal or one must be 1. Use `np.broadcast_shapes` to test compatibility without creating arrays, and always verify output shapes to catch silent bugs where broadcasting succeeds but produces unintended results.
