# View Operations


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

These operations return views that share memory with the original array.


## Slicing

Array slices return views by default.

### 1. Basic Slice

```python
import numpy as np

def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(f"{x = }")

    y = x[1:4]  # returns view
    y[0] = -1
    print(f"{x = }")

if __name__ == "__main__":
    main()
```

Output:

```
x = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = array([ 0, -1,  2,  3,  4,  5,  6,  7,  8,  9])
```

### 2. Mutation Propagates

Modifying the slice modifies the original array.


## Method reshape

The `reshape` method returns a view when possible.

### 1. reshape View

```python
import numpy as np

def main():
    x = np.arange(6)
    print(f"{x = }")

    y = x.reshape((3, 2))  # returns view
    y[0, 0] = 6
    print(f"{x = }")

if __name__ == "__main__":
    main()
```

Output:

```
x = array([0, 1, 2, 3, 4, 5])
x = array([6, 1, 2, 3, 4, 5])
```

### 2. Same Memory

The reshaped array shares the underlying data buffer.


## Function np.reshape

The `np.reshape` function also returns a view.

### 1. np.reshape View

```python
import numpy as np

def main():
    x = np.arange(6)
    print(f"{x = }")

    y = np.reshape(x, (3, 2))  # returns view
    y[0, 0] = 6
    print(f"{x = }")

if __name__ == "__main__":
    main()
```

Output:

```
x = array([0, 1, 2, 3, 4, 5])
x = array([6, 1, 2, 3, 4, 5])
```

### 2. Equivalent Behavior

Method and function behave identically.


## Attribute T

The transpose attribute `.T` returns a view.

### 1. Transpose View

```python
import numpy as np

def main():
    x = np.array([[1, 2], [3, 4]])
    print(f"{x = }")

    y = x.T  # returns view
    y[0, 0] = 6
    print(f"{x = }")

if __name__ == "__main__":
    main()
```

Output:

```
x = array([[1, 2],
           [3, 4]])
x = array([[6, 2],
           [3, 4]])
```

### 2. Shared Data

Transposed array shares memory with original.


## Function np.transpose

The `np.transpose` function returns a view.

### 1. np.transpose View

```python
import numpy as np

def main():
    x = np.array([[1, 2], [3, 4]])
    print(f"{x = }")

    y = np.transpose(x)  # returns view
    y[0, 0] = 6
    print(f"{x = }")

if __name__ == "__main__":
    main()
```

Output:

```
x = array([[1, 2],
           [3, 4]])
x = array([[6, 2],
           [3, 4]])
```

### 2. Same as .T

Function and attribute produce equivalent views.


## View Summary

Common operations returning views.

### 1. List of Operations

- Slicing: `arr[1:4]`
- Reshape: `arr.reshape(shape)`
- Transpose: `arr.T`
- Ravel: `arr.ravel()`
- Squeeze: `np.squeeze(arr)`
- Expand dims: `arr[np.newaxis]`

### 2. General Rule

Operations that reinterpret existing data return views.
