# Changing Dtype


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

NumPy provides multiple ways to convert array data types.


## The astype Method

The `astype` method returns a copy with the specified dtype.

### 1. Basic Conversion

```python
import numpy as np

def main():
    x = np.zeros((2, 3))
    y = x.astype(np.uint8)
    print(f"{x.dtype = }")
    print(f"{y.dtype = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.dtype = dtype('float64')
y.dtype = dtype('uint8')
```

### 2. Returns Copy

`astype` always creates a new array; the original is unchanged.


## dtype Keyword

Specify dtype directly during array creation.

### 1. At Creation Time

```python
import numpy as np

def main():
    x = np.array([1, 2, 3])
    print(f"{x.dtype = }", end="\n\n")

    x = np.array([1, 2, 3], dtype=np.uint8)
    print(f"{x.dtype = }", end="\n\n")

    x = np.array([1, 2, 3], dtype=np.float32)
    print(f"{x.dtype = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.dtype = dtype('int64')

x.dtype = dtype('uint8')

x.dtype = dtype('float32')
```

### 2. Efficiency

Specifying dtype at creation avoids an extra conversion step.


## Full Replacement

Reassigning a variable replaces everything, including dtype.

### 1. Complete Override

```python
import numpy as np

def main():
    a = np.zeros(shape=(3,), dtype=np.uint8)
    b = np.array([-0.87796192, -0.97481932, -1.8001195], dtype=np.float64)
    print(f"{a = }")
    print(f"{b = }", end="\n\n")

    a = b
    print(f"{a = }")
    print(f"{b = }")

if __name__ == "__main__":
    main()
```

Output:

```
a = array([0, 0, 0], dtype=uint8)
b = array([-0.87796192, -0.97481932, -1.8001195])

a = array([-0.87796192, -0.97481932, -1.8001195])
b = array([-0.87796192, -0.97481932, -1.8001195])
```

### 2. Name Rebinding

This rebinds the name `a` to a new object; no type coercion occurs.


## Partial Same Dtype

Assigning to a slice with matching dtype works correctly.

### 1. Compatible Types

```python
import numpy as np

def main():
    a = np.zeros(shape=(2, 3), dtype=np.float64)
    b = np.array([-0.87796192, -0.97481932, -1.8001195], dtype=np.float64)
    print(f"{a = }")
    print(f"{b = }", end="\n\n")

    a[0, :] = b
    print(f"{a = }")
    print(f"{b = }")

if __name__ == "__main__":
    main()
```

Output:

```
a = array([[0., 0., 0.],
           [0., 0., 0.]])
b = array([-0.87796192, -0.97481932, -1.8001195])

a = array([[-0.87796192, -0.97481932, -1.8001195],
           [ 0.        ,  0.        ,  0.        ]])
b = array([-0.87796192, -0.97481932, -1.8001195])
```

### 2. No Data Loss

When dtypes match, values are copied exactly.


## Partial Diff Dtype

Assigning to a slice with different dtype causes truncation.

### 1. Truncation Example

```python
import numpy as np

def main():
    a = np.zeros(shape=(2, 3), dtype=np.uint8)
    b = np.array([-0.87796192, -0.97481932, -1.8001195], dtype=np.float64)
    print(f"{a = }")
    print(f"{b = }", end="\n\n")

    a[0, :] = b
    print(f"{a = }")
    print(f"{b = }")

if __name__ == "__main__":
    main()
```

Output:

```
a = array([[0, 0, 0],
           [0, 0, 0]], dtype=uint8)
b = array([-0.87796192, -0.97481932, -1.8001195])

a = array([[0, 0, 0],
           [0, 0, 0]], dtype=uint8)
b = array([-0.87796192, -0.97481932, -1.8001195])
```

### 2. Conversion Rules

```python
import numpy as np

def main():
    print(f"{np.uint8(-0.87796192) = }")
    print(f"{np.uint8(-0.97481932) = }")
    print(f"{np.uint8(-1.8001195) = }")

if __name__ == "__main__":
    main()
```

Output:

```
np.uint8(-0.87796192) = 0
np.uint8(-0.97481932) = 0
np.uint8(-1.8001195) = 255
```

### 3. Warning

Negative floats converting to uint8 produce unexpected results due to overflow.
