# Shape and ndim

Every NumPy array has `shape` and `ndim` attributes that describe its structure.


## The shape Attribute

The `shape` attribute returns a tuple indicating the size along each dimension.

### 1. 1D Array Shape

```python
import numpy as np

def main():
    x = np.array([7, 2, 9, 10])
    print(f"{x.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (4,)
```

### 2. 2D Array Shape

```python
import numpy as np

def main():
    y = np.array([[5.2, 3.0, 4.5], [9.1, 0.1, 0.3]])
    print(f"{y.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
y.shape = (2, 3)
```

### 3. 3D Array Shape

```python
import numpy as np

def main():
    z = np.zeros((4, 3, 2))
    print(f"{z.shape = }, {z.dtype = }")

if __name__ == "__main__":
    main()
```

Output:

```
z.shape = (4, 3, 2), z.dtype = dtype('float64')
```


## The ndim Attribute

The `ndim` attribute returns the number of dimensions (axes) of the array.

### 1. 1D Array ndim

```python
import numpy as np

def main():
    x = np.array([7, 2, 9, 10])
    print(f"{x.ndim = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.ndim = 1
```

### 2. 2D Array ndim

```python
import numpy as np

def main():
    y = np.array([[5.2, 3.0, 4.5], [9.1, 0.1, 0.3]])
    print(f"{y.ndim = }")

if __name__ == "__main__":
    main()
```

Output:

```
y.ndim = 2
```

### 3. 3D Array ndim

```python
import numpy as np

def main():
    z = np.zeros((4, 3, 2))
    print(f"{z.ndim = }")

if __name__ == "__main__":
    main()
```

Output:

```
z.ndim = 3
```


## Relationship

The `ndim` equals the length of the `shape` tuple.

### 1. Mathematical Link

```python
import numpy as np

x = np.zeros((4, 3, 2))
assert x.ndim == len(x.shape)
```

### 2. Practical Use

Use `ndim` to check dimensionality before operations that require specific dimensions.
