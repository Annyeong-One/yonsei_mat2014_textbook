# Expanding Dimensions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Adding new axes to arrays is essential for broadcasting and batch operations.


## np.expand_dims

The `np.expand_dims` function inserts a new axis at the specified position.

### 1. Axis Parameter

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    print(f"{x.shape = }", end="\n\n")

    y0 = np.expand_dims(x, axis=0)
    y1 = np.expand_dims(x, axis=1)
    y2 = np.expand_dims(x, axis=2)
    y3 = np.expand_dims(x, axis=3)
    print(f"{y0.shape = }")
    print(f"{y1.shape = }")
    print(f"{y2.shape = }")
    print(f"{y3.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (2, 3, 4)

y0.shape = (1, 2, 3, 4)
y1.shape = (2, 1, 3, 4)
y2.shape = (2, 3, 1, 4)
y3.shape = (2, 3, 4, 1)
```

### 2. Axis Meaning

The axis specifies where the new size-1 dimension is inserted.


## Using np.newaxis

The `np.newaxis` constant adds dimensions via indexing syntax.

### 1. Explicit Slicing

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    print(f"{x.shape = }", end="\n\n")

    y1 = x[np.newaxis, :]
    y2 = x[:, np.newaxis]
    y3 = x[:, :, np.newaxis]
    y4 = x[:, :, :, np.newaxis]
    print(f"{y1.shape = }")
    print(f"{y2.shape = }")
    print(f"{y3.shape = }")
    print(f"{y4.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (2, 3, 4)

y1.shape = (1, 2, 3, 4)
y2.shape = (2, 1, 3, 4)
y3.shape = (2, 3, 1, 4)
y4.shape = (2, 3, 4, 1)
```

### 2. With Ellipsis

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    print(f"{x.shape = }", end="\n\n")

    z1 = x[np.newaxis, ...]
    z2 = x[..., np.newaxis]
    print(f"{z1.shape = }")
    print(f"{z2.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (2, 3, 4)

z1.shape = (1, 2, 3, 4)
z2.shape = (2, 3, 4, 1)
```


## Using None

`None` is an alias for `np.newaxis` in indexing.

### 1. Explicit Slicing

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    print(f"{x.shape = }", end="\n\n")

    y1 = x[None, :]
    y2 = x[:, None]
    y3 = x[:, :, None]
    y4 = x[:, :, :, None]
    print(f"{y1.shape = }")
    print(f"{y2.shape = }")
    print(f"{y3.shape = }")
    print(f"{y4.shape = }")

if __name__ == "__main__":
    main()
```

### 2. With Ellipsis

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    print(f"{x.shape = }", end="\n\n")

    z1 = x[None, ...]
    z2 = x[..., None]
    print(f"{z1.shape = }")
    print(f"{z2.shape = }")

if __name__ == "__main__":
    main()
```


## Method Comparison

Three equivalent ways to add dimensions.

### 1. np.expand_dims

Most explicit and readable for complex insertions.

### 2. np.newaxis

Standard NumPy idiom, clear intent.

### 3. None Shorthand

Shortest syntax, common in concise code.
