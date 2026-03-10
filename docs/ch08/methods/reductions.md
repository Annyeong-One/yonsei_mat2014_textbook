# Reductions with axis


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Concept

Reduction operations collapse one or more dimensions of an array by applying an aggregation function. The `axis` parameter specifies which dimension to reduce.

### 1. What is Reduction

A reduction takes an array and produces a smaller array (or scalar) by combining elements along specified dimensions.

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    print("Original array:")
    print(a)
    print(f"Shape: {a.shape}")
    print()
    
    # Full reduction to scalar
    total = a.sum()
    print(f"sum() = {total}")
    print(f"Shape: {np.array(total).shape}")

if __name__ == "__main__":
    main()
```

**Output:**

```
Original array:
[[1 2 3]
 [4 5 6]]
Shape: (2, 3)

sum() = 21
Shape: ()
```

### 2. axis Parameter

The `axis` parameter specifies which dimension to collapse. The result has one fewer dimension.

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    print("a.shape:", a.shape)  # (2, 3)
    print()
    
    # axis=0: collapse rows, keep columns
    print("sum(axis=0):", a.sum(axis=0))
    print("Shape:", a.sum(axis=0).shape)  # (3,)
    print()
    
    # axis=1: collapse columns, keep rows
    print("sum(axis=1):", a.sum(axis=1))
    print("Shape:", a.sum(axis=1).shape)  # (2,)

if __name__ == "__main__":
    main()
```

**Output:**

```
a.shape: (2, 3)

sum(axis=0): [5 7 9]
Shape: (3,)

sum(axis=1): [ 6 15]
Shape: (2,)
```

### 3. Visual Intuition

Think of `axis` as the direction of collapse:

- `axis=0`: Collapse vertically (down rows)
- `axis=1`: Collapse horizontally (across columns)

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])
    
    print("Array (3 rows, 2 cols):")
    print(a)
    print()
    
    # axis=0: sum down each column
    print("axis=0 (sum down):", a.sum(axis=0))
    # [1+3+5, 2+4+6] = [9, 12]
    
    # axis=1: sum across each row
    print("axis=1 (sum across):", a.sum(axis=1))
    # [1+2, 3+4, 5+6] = [3, 7, 11]

if __name__ == "__main__":
    main()
```

## Shape Rules

### 1. Output Shape

The output shape removes the axis dimension from the input shape.

```python
import numpy as np

def main():
    a = np.zeros((2, 3, 4))
    
    print(f"Original shape: {a.shape}")
    print()
    print(f"sum(axis=0).shape: {a.sum(axis=0).shape}")  # (3, 4)
    print(f"sum(axis=1).shape: {a.sum(axis=1).shape}")  # (2, 4)
    print(f"sum(axis=2).shape: {a.sum(axis=2).shape}")  # (2, 3)
    print(f"sum().shape: {a.sum().shape}")              # ()

if __name__ == "__main__":
    main()
```

### 2. keepdims Parameter

Use `keepdims=True` to preserve the reduced dimension as size 1.

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    print(f"Original shape: {a.shape}")
    print()
    
    # Without keepdims
    s1 = a.sum(axis=1)
    print(f"sum(axis=1): {s1}")
    print(f"Shape: {s1.shape}")
    print()
    
    # With keepdims
    s2 = a.sum(axis=1, keepdims=True)
    print(f"sum(axis=1, keepdims=True):")
    print(s2)
    print(f"Shape: {s2.shape}")

if __name__ == "__main__":
    main()
```

**Output:**

```
Original shape: (2, 3)

sum(axis=1): [ 6 15]
Shape: (2,)

sum(axis=1, keepdims=True):
[[ 6]
 [15]]
Shape: (2, 1)
```

### 3. Broadcasting Use

`keepdims=True` is useful for broadcasting operations.

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    # Normalize each row to sum to 1
    row_sums = a.sum(axis=1, keepdims=True)
    normalized = a / row_sums
    
    print("Original:")
    print(a)
    print()
    print("Row sums (keepdims=True):")
    print(row_sums)
    print()
    print("Normalized rows:")
    print(normalized)
    print()
    print("Verify row sums:", normalized.sum(axis=1))

if __name__ == "__main__":
    main()
```

## Method vs Function

### 1. Two Syntaxes

Most reductions can be called as methods or functions.

```python
import numpy as np

def main():
    a = np.array([[1, 2], [3, 4]])
    
    # Method syntax
    print(f"a.sum() = {a.sum()}")
    print(f"a.sum(axis=0) = {a.sum(axis=0)}")
    
    # Function syntax
    print(f"np.sum(a) = {np.sum(a)}")
    print(f"np.sum(a, axis=0) = {np.sum(a, axis=0)}")

if __name__ == "__main__":
    main()
```

### 2. When to Use Each

```python
import numpy as np

def main():
    """
    Method syntax: a.sum()
    - More concise
    - Object-oriented style
    - Only works on ndarray
    
    Function syntax: np.sum(a)
    - Works on lists and array-like
    - Consistent with other np functions
    - Preferred in functional pipelines
    """
    
    # Function works on lists
    result = np.sum([1, 2, 3])
    print(f"np.sum([1, 2, 3]) = {result}")
    
    # Method requires array
    a = np.array([1, 2, 3])
    print(f"a.sum() = {a.sum()}")

if __name__ == "__main__":
    main()
```

### 3. Common Reductions

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    reductions = [
        ("sum", a.sum()),
        ("prod", a.prod()),
        ("min", a.min()),
        ("max", a.max()),
        ("mean", a.mean()),
        ("std", a.std()),
        ("var", a.var()),
    ]
    
    for name, result in reductions:
        print(f"{name:6}: {result}")

if __name__ == "__main__":
    main()
```

## Mathematical Form

### 1. Sum Notation

For a 2D array $a = (a_{ij})$:

$$
\begin{aligned}
\texttt{a.sum()} &= \sum_i \sum_j a_{ij} \\
\texttt{a.sum(axis=0)[j]} &= \sum_i a_{ij} \\
\texttt{a.sum(axis=1)[i]} &= \sum_j a_{ij}
\end{aligned}
$$

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 1],
                  [2, 3]])
    
    print("a =")
    print(a)
    print()
    print(f"sum over all: {a.sum()}")
    print(f"sum over axis=0 (columns): {a.sum(axis=0)}")
    print(f"sum over axis=1 (rows): {a.sum(axis=1)}")

if __name__ == "__main__":
    main()
```

### 2. Index Interpretation

The axis being summed disappears from the output indices.

```python
import numpy as np

def main():
    # 3D array: shape (2, 3, 4)
    a = np.arange(24).reshape(2, 3, 4)
    
    print(f"a.shape = {a.shape}")
    print()
    
    # axis=0: sum over first index
    # a.sum(axis=0)[j,k] = sum over i of a[i,j,k]
    print(f"sum(axis=0).shape = {a.sum(axis=0).shape}")
    
    # axis=1: sum over second index
    # a.sum(axis=1)[i,k] = sum over j of a[i,j,k]
    print(f"sum(axis=1).shape = {a.sum(axis=1).shape}")
    
    # axis=2: sum over third index
    # a.sum(axis=2)[i,j] = sum over k of a[i,j,k]
    print(f"sum(axis=2).shape = {a.sum(axis=2).shape}")

if __name__ == "__main__":
    main()
```

### 3. Multiple Axes

Reduce over multiple axes simultaneously with a tuple.

```python
import numpy as np

def main():
    a = np.arange(24).reshape(2, 3, 4)
    
    print(f"Original shape: {a.shape}")
    print()
    
    # Sum over axes 0 and 1
    print(f"sum(axis=(0,1)).shape: {a.sum(axis=(0,1)).shape}")
    
    # Sum over axes 1 and 2
    print(f"sum(axis=(1,2)).shape: {a.sum(axis=(1,2)).shape}")
    
    # Sum over all axes (equivalent to sum())
    print(f"sum(axis=(0,1,2)): {a.sum(axis=(0,1,2))}")
    print(f"sum(): {a.sum()}")

if __name__ == "__main__":
    main()
```
