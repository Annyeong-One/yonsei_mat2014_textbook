# Copy Operations


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

These operations create independent copies with separate memory.


## Method copy

The `.copy()` method creates an explicit copy.

### 1. Slice then Copy

```python
import numpy as np

def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(f"{x = }")

    y = x[1:4].copy()  # returns copy
    y[0] = -1
    print(f"{x = }")

if __name__ == "__main__":
    main()
```

Output:

```
x = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

### 2. Original Unchanged

The copy is independent; mutations don't propagate.


## Function np.copy

The `np.copy()` function creates a copy.

### 1. np.copy Usage

```python
import numpy as np

def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(f"{x = }")

    y = np.copy(x[1:4])  # returns copy
    y[0] = -1
    print(f"{x = }")

if __name__ == "__main__":
    main()
```

Output:

```
x = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

### 2. Equivalent to Method

Both approaches produce identical results.


## Fancy Indexing

Fancy indexing always returns a copy.

### 1. Index Array

```python
import numpy as np

def main():
    x = np.array([0, 1, 2, 3, 4, 5])
    y = x[[0, 2, 4]]  # fancy indexing returns copy
    y[0] = -1
    print(f"{x = }")

if __name__ == "__main__":
    main()
```

Output:

```
x = array([0, 1, 2, 3, 4, 5])
```

### 2. Boolean Indexing

```python
import numpy as np

def main():
    x = np.array([0, 1, 2, 3, 4, 5])
    y = x[x > 2]  # boolean indexing returns copy
    y[0] = -1
    print(f"{x = }")

if __name__ == "__main__":
    main()
```

Output:

```
x = array([0, 1, 2, 3, 4, 5])
```


## Arithmetic Operations

Most arithmetic creates new arrays.

### 1. Addition

```python
import numpy as np

x = np.array([1, 2, 3])
y = x + 1  # creates new array
y[0] = -1
print(f"{x = }")  # x = array([1, 2, 3])
```

### 2. Multiplication

```python
import numpy as np

x = np.array([1, 2, 3])
y = x * 2  # creates new array
```

### 3. In-place Operations

Use `+=`, `*=` to modify in-place without creating copies.


## Copy Summary

Operations that create copies.

### 1. Explicit Copies

- `.copy()` method
- `np.copy()` function

### 2. Implicit Copies

- Fancy indexing: `arr[[0, 2, 4]]`
- Boolean indexing: `arr[arr > 0]`
- Arithmetic: `arr + 1`, `arr * 2`
- Some reshapes (non-contiguous)

### 3. Best Practice

When in doubt, use `.copy()` explicitly for clarity.
