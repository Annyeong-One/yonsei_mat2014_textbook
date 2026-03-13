# Shape After Indexing

Indexing and slicing affect array dimensions differently.


## Index vs Slice

Single index reduces dimensions; slice preserves them.

### 1. Single Index

```python
import numpy as np

def main():
    a = np.zeros((8, 8, 8, 8))
    print(f"{a[1].shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[1].shape = (8, 8, 8)
```

### 2. Slice of One

```python
import numpy as np

def main():
    a = np.zeros((8, 8, 8, 8))
    print(f"{a[1:2].shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[1:2].shape = (1, 8, 8, 8)
```

### 3. Key Difference

`a[1]` removes a dimension; `a[1:2]` keeps it with size 1.


## Mixed Operations

Combining indices and slices on different axes.

### 1. Index Two Axes

```python
import numpy as np

def main():
    a = np.zeros((8, 8, 8, 8))
    print(f"{a[1, :, 3, :].shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[1, :, 3, :].shape = (8, 8)
```

### 2. Index and Slice

```python
import numpy as np

def main():
    a = np.zeros((8, 8, 8, 8))
    print(f"{a[1:2, :, 3, :].shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[1:2, :, 3, :].shape = (1, 8, 8)
```

### 3. All Slices

```python
import numpy as np

def main():
    a = np.zeros((8, 8, 8, 8))
    print(f"{a[1:2, :, 3:4, :].shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[1:2, :, 3:4, :].shape = (1, 8, 1, 8)
```


## Complete Comparison

Side-by-side comparison of all cases.

### 1. Summary Table

```python
import numpy as np

def main():
    a = np.zeros((8, 8, 8, 8))
    print(f"{a[1].shape = }")
    print(f"{a[1:2].shape = }")
    print(f"{a[1, :, 3, :].shape = }")
    print(f"{a[1:2, :, 3, :].shape = }")
    print(f"{a[1:2, :, 3:4, :].shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[1].shape = (8, 8, 8)
a[1:2].shape = (1, 8, 8, 8)
a[1, :, 3, :].shape = (8, 8)
a[1:2, :, 3, :].shape = (1, 8, 8)
a[1:2, :, 3:4, :].shape = (1, 8, 1, 8)
```

### 2. Dimension Rule

Each integer index removes one dimension; each slice keeps it.


## Practical Impact

Understanding shape changes is crucial for array operations.

### 1. Broadcasting

Shape mismatches cause broadcasting errors; use slices to preserve dimensions.

### 2. Neural Networks

Batch dimensions must be preserved; use `[0:1]` instead of `[0]`.

### 3. Matrix Operations

Some operations require 2D arrays; slicing maintains dimensionality.
