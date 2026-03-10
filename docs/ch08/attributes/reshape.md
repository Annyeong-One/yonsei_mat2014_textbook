# Reshaping Arrays


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Reshaping changes an array's dimensions while preserving its data.


## Method reshape

The `reshape` method returns a new view with the specified shape.

### 1. Basic Usage

```python
import numpy as np

def main():
    x = np.arange(6)
    print(f"{x.shape = }")
    print(x, end="\n\n")

    y = x.reshape((3, 2))
    print(f"{y.shape = }")
    print(y)

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (6,)
[0 1 2 3 4 5]

y.shape = (3, 2)
[[0 1]
 [2 3]
 [4 5]]
```

### 2. Total Size Rule

The product of new dimensions must equal the original total size.


## Function np.reshape

The `np.reshape` function provides the same functionality.

### 1. Function Syntax

```python
import numpy as np

def main():
    x = np.arange(6)
    print(f"{x.shape = }")
    print(x, end="\n\n")

    y = np.reshape(x, (3, 2))
    print(f"{y.shape = }")
    print(y)

if __name__ == "__main__":
    main()
```

### 2. Method vs Function

Both are equivalent; the method syntax is more common.


## The -1 Wildcard

Using `-1` lets NumPy infer one dimension automatically.

### 1. Flatten to 1D

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    y = x.reshape((-1,))
    print(f"{x.shape = }")
    print(f"{y.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (2, 3, 4)
y.shape = (24,)
```

### 2. Keep First Axis

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    z = x.reshape((2, -1))
    print(f"{x.shape = }")
    print(f"{z.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (2, 3, 4)
z.shape = (2, 12)
```

### 3. Keep Last Axis

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    w = x.reshape((-1, 4))
    print(f"{x.shape = }")
    print(f"{w.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (2, 3, 4)
w.shape = (6, 4)
```


## Multiple Examples

Combining all `-1` examples in one block.

### 1. All Together

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    y = x.reshape((-1,))
    z = x.reshape((2, -1))
    w = x.reshape((-1, 4))
    print(f"{x.shape = }")
    print(f"{y.shape = }")
    print(f"{z.shape = }")
    print(f"{w.shape = }")

if __name__ == "__main__":
    main()
```

### 2. Only One -1

You can only use `-1` for a single dimension per reshape call.
