# np.array Basics

The `np.array` function converts Python sequences into NumPy arrays. Understanding array dimensions is fundamental to working with NumPy.


## Dimension Concepts

NumPy arrays generalize scalars, vectors, and matrices into n-dimensional structures.

$$\begin{array}{lll}
\text{0D Array}&=&\text{Scalar}\\
\text{1D Array}&=&\text{Vector}\\
\text{2D Array}&=&\text{Matrix}\\
\text{3D Array}&=&\text{Color Image}\\
\text{4D Array}&=&\text{Batch of Images}\\
\end{array}$$

Each dimension adds another axis of indexing.


## Creating 0D Arrays

A 0D array holds a single scalar value with no axes.

### 1. Scalar Creation

```python
import numpy as np

def main():
    a = np.array(21)
    print(f'{a = }')
    print(f'{type(a) = }')
    print(f'{a.ndim = }')
    print(f'{a.shape = }')
    print(f'{a.dtype = }')

if __name__ == "__main__":
    main()
```

Output:

```
a = array(21)
type(a) = <class 'numpy.ndarray'>
a.ndim = 0
a.shape = ()
a.dtype = dtype('int64')
```

### 2. Scalar vs Tuple

```python
a = 3
print(a)      # 3

b = 3,
print(b)      # (3,)
```

A trailing comma creates a tuple, not a scalar.


## Creating 1D Arrays

A 1D array represents a vector with a single axis.

### 1. From Python List

```python
import numpy as np

def main():
    a = np.array([1, 2, 3])
    print(f'{a = }')
    print(f'{type(a) = }')
    print(f'{a.ndim = }')
    print(f'{a.shape = }')
    print(f'{a.dtype = }')

if __name__ == "__main__":
    main()
```

Output:

```
a = array([1, 2, 3])
type(a) = <class 'numpy.ndarray'>
a.ndim = 1
a.shape = (3,)
a.dtype = dtype('int64')
```

### 2. Specifying dtype

```python
import numpy as np

def main():
    a = np.array([1, 2, 3], dtype=np.uint8)
    print(f'{a = }')
    print(f'{type(a) = }')
    print(f'{a.ndim = }')
    print(f'{a.shape = }')
    print(f'{a.dtype = }')

if __name__ == "__main__":
    main()
```

Output:

```
a = array([1, 2, 3], dtype=uint8)
a.dtype = dtype('uint8')
```


## Creating 2D Arrays

A 2D array represents a matrix with rows and columns.

### 1. Nested Lists

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(f'{a = }')
    print(f'{type(a) = }')
    print(f'{a.ndim = }')
    print(f'{a.shape = }')
    print(f'{a.dtype = }')

if __name__ == "__main__":
    main()
```

Output:

```
a = array([[1, 2, 3],
           [4, 5, 6]])
a.ndim = 2
a.shape = (2, 3)
```

### 2. Shape Interpretation

The shape `(2, 3)` means 2 rows and 3 columns.


## Creating 3D Arrays

A 3D array adds depth, commonly used for color images.

### 1. Triple Nesting

```python
import numpy as np

def main():
    a = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[1, 4, 2], [5, 7, 3]]])
    print(f'{a = }')
    print(f'{type(a) = }')
    print(f'{a.ndim = }')
    print(f'{a.shape = }')
    print(f'{a.dtype = }')

if __name__ == "__main__":
    main()
```

Output:

```
a.ndim = 3
a.shape = (2, 2, 3)
```

### 2. Image Interpretation

For images, shape `(H, W, C)` represents height, width, and color channels.


## Key Attributes

Every ndarray has essential attributes for inspection.

### 1. ndim Attribute

The `ndim` attribute returns the number of dimensions.

### 2. shape Attribute

The `shape` attribute returns a tuple of dimension sizes.

### 3. dtype Attribute

The `dtype` attribute indicates the data type of elements.
