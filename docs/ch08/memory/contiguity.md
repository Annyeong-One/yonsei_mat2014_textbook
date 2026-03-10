# Memory Contiguity


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Memory layout affects whether operations return views or copies.


## C Contiguous

C-style row-major memory layout.

### 1. Row-Major Order

```
Array: [[0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11]]

Memory: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

Elements are stored row by row.

### 2. NumPy Default

NumPy arrays are C-contiguous by default.


## Fortran Contiguous

Fortran-style column-major memory layout.

### 1. Column-Major Order

```
Array: [[0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11]]

Memory: [0, 4, 8, 1, 5, 9, 2, 6, 10, 3, 7, 11]
```

Elements are stored column by column.

### 2. Transpose Effect

Transposing a C-contiguous array makes it Fortran-contiguous.


## View Chain Example

Track memory sharing through operations.

### 1. Initial Array

```python
import numpy as np

def main():
    x = np.arange(12)
    print(f"{id(x) = }")

if __name__ == "__main__":
    main()
```

### 2. Reshape (View)

```python
import numpy as np

def main():
    x = np.arange(12)
    print(f"{id(x) = }")

    y = x.reshape(3, 4)  # view
    print(f"{id(y) = }")

    y[-1, -1] = -11
    print(f"{x = }")

if __name__ == "__main__":
    main()
```

`x` and `y` share the same memory block.

### 3. Transpose (View)

```python
import numpy as np

def main():
    x = np.arange(12)
    print(f"{id(x) = }")

    y = x.reshape(3, 4)  # view
    print(f"{id(y) = }")

    z = y.T  # still a view
    print(f"{id(z) = }")

    z[-1, -1] = -11
    print(f"{x = }")

if __name__ == "__main__":
    main()
```

`z` still shares memory but interprets it column-wise.


## Forced Copy

Non-contiguous arrays force copies when reshaped.

### 1. Copy Scenario

```python
import numpy as np

def main():
    x = np.arange(12)
    print(f"{id(x) = }")

    y = x.reshape(3, 4)  # view
    print(f"{id(y) = }")

    z = y.T  # view (Fortran contiguous)
    print(f"{id(z) = }")

    w = z.reshape((-1,))  # COPY (must reorder data)
    print(f"{id(w) = }")

    w[-1] = -11
    print(f"{x = }")
    print(f"{y = }")
    print(f"{z = }")
    print(f"{w = }")

if __name__ == "__main__":
    main()
```

### 2. Why Copy Needed

`z` is Fortran-contiguous `[0,4,8,1,5,9,2,6,10,3,7,11]` in memory.
Flattening to C-order requires reordering, forcing a copy.

### 3. Memory Independence

`w` has different `id()` and modifications don't affect `x`, `y`, `z`.


## Checking Contiguity

Inspect array memory layout flags.

### 1. Flags Attribute

```python
import numpy as np

x = np.arange(12).reshape(3, 4)
print(x.flags)
```

Output:

```
  C_CONTIGUOUS : True
  F_CONTIGUOUS : False
  ...
```

### 2. After Transpose

```python
import numpy as np

x = np.arange(12).reshape(3, 4)
y = x.T
print(y.flags)
```

Output:

```
  C_CONTIGUOUS : False
  F_CONTIGUOUS : True
  ...
```


## Best Practices

Guidelines for working with memory layout.

### 1. Be Aware

Know when operations return views vs copies.

### 2. Use id()

Track object identity to verify memory sharing.

### 3. Explicit Copy

When data integrity is critical, call `.copy()` explicitly.

### 4. Check flags

Use `.flags` to inspect contiguity when debugging.
