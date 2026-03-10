# Squeezing Dimensions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The `np.squeeze` function removes all size-1 dimensions from an array.


## np.squeeze Function

Removes axes of length one from the array shape.

### 1. Basic Usage

```python
import numpy as np

def main():
    x = np.random.normal(size=(1, 3, 1, 2, 1, 5, 1))
    y = np.squeeze(x)
    print(f"{x.shape = }")
    print(f"{y.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (1, 3, 1, 2, 1, 5, 1)
y.shape = (3, 2, 5)
```

### 2. All Size-1 Removed

Every dimension with size 1 is eliminated from the result.


## Selective Squeeze

Remove only specific size-1 axes using the `axis` parameter.

### 1. Single Axis

```python
import numpy as np

def main():
    x = np.zeros((1, 3, 1, 4))
    y = np.squeeze(x, axis=0)
    print(f"{x.shape = }")
    print(f"{y.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (1, 3, 1, 4)
y.shape = (3, 1, 4)
```

### 2. Multiple Axes

```python
import numpy as np

def main():
    x = np.zeros((1, 3, 1, 4))
    y = np.squeeze(x, axis=(0, 2))
    print(f"{x.shape = }")
    print(f"{y.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (1, 3, 1, 4)
y.shape = (3, 4)
```


## Error Handling

Squeezing non-singleton dimensions raises an error.

### 1. ValueError Example

```python
import numpy as np

def main():
    x = np.zeros((1, 3, 1, 4))
    try:
        y = np.squeeze(x, axis=1)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### 2. Safe Practice

Only squeeze axes you know have size 1.


## Common Use Cases

Squeeze is frequently needed after certain operations.

### 1. After Slicing

Slicing with a single index reduces dimensionality; squeeze cleans up.

### 2. Model Outputs

Neural network outputs often have extra batch or channel dimensions.

### 3. Broadcasting Result

Broadcasting may introduce size-1 dimensions that need removal.
