# ravel vs flatten


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Both methods flatten arrays to 1D, but differ in memory behavior.


## Method ravel

The `ravel()` method returns a view when possible.

### 1. Basic Usage

```python
import numpy as np

def main():
    x = np.arange(6).reshape((3, 2))
    print(f"{x.shape = }")

    y = x.ravel()  # returns view
    print(f"{y.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (3, 2)
y.shape = (6,)
```

### 2. Memory Sharing

```python
import numpy as np

def main():
    x = np.arange(6).reshape((3, 2))
    y = x.ravel()
    y[0] = -1
    print(f"{x[0, 0] = }")  # -1

if __name__ == "__main__":
    main()
```

### 3. View Behavior

Modifying the raveled array modifies the original.


## Method flatten

The `flatten()` method always returns a copy.

### 1. Basic Usage

```python
import numpy as np

def main():
    x = np.arange(6).reshape((3, 2))
    print(f"{x.shape = }")

    y = x.flatten()  # returns copy
    print(f"{y.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (3, 2)
y.shape = (6,)
```

### 2. Memory Independence

```python
import numpy as np

def main():
    x = np.arange(6).reshape((3, 2))
    y = x.flatten()
    y[0] = -1
    print(f"{x[0, 0] = }")  # 0

if __name__ == "__main__":
    main()
```

### 3. Copy Behavior

Modifying the flattened array does not affect the original.


## Side-by-Side Compare

Direct comparison of the two methods.

### 1. Comparison Code

```python
import numpy as np

def main():
    x = np.arange(6).reshape((3, 2))
    
    # ravel returns view
    r = x.ravel()
    r[0] = 99
    print(f"After ravel modification: x[0,0] = {x[0, 0]}")
    
    # Reset
    x = np.arange(6).reshape((3, 2))
    
    # flatten returns copy
    f = x.flatten()
    f[0] = 99
    print(f"After flatten modification: x[0,0] = {x[0, 0]}")

if __name__ == "__main__":
    main()
```

Output:

```
After ravel modification: x[0,0] = 99
After flatten modification: x[0,0] = 0
```

### 2. Key Difference

`ravel` shares memory; `flatten` does not.


## When to Use Each

Choose based on your memory requirements.

### 1. Use ravel When

- Memory efficiency matters
- You want changes to reflect in original
- Working with large arrays

### 2. Use flatten When

- You need data isolation
- Original must remain unchanged
- Returning from functions

### 3. Performance Note

`ravel` is faster because it avoids memory allocation.


## Order Parameter

Both methods support different flattening orders.

### 1. C Order (Default)

```python
import numpy as np

x = np.array([[1, 2], [3, 4]])
print(x.ravel(order='C'))  # [1 2 3 4]
```

Row-major order (C-style).

### 2. Fortran Order

```python
import numpy as np

x = np.array([[1, 2], [3, 4]])
print(x.ravel(order='F'))  # [1 3 2 4]
```

Column-major order (Fortran-style).
