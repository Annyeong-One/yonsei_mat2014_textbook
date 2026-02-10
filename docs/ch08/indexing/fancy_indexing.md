# Fancy Indexing

Fancy indexing selects elements using arrays of indices instead of scalars or slices.


## 1D Fancy Indexing

Select multiple elements by passing a list or array of indices.

### 1. List of Indices

```python
import numpy as np

def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = np.array(a)
    print(f"{b[[0, 1, 3]] = }")

if __name__ == "__main__":
    main()
```

Output:

```
b[[0, 1, 3]] = array([0, 1, 3])
```

### 2. Array of Indices

```python
import numpy as np

def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = np.array(a)
    print(f"{b[np.array([0, 1, 3])] = }")

if __name__ == "__main__":
    main()
```

Output:

```
b[np.array([0, 1, 3])] = array([0, 1, 3])
```


## 2D Fancy Indexing

Select multiple rows from a 2D array.

### 1. Row Selection

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    b = np.array(a)
    print(f"{b[[0, 1, 3]] = }")

if __name__ == "__main__":
    main()
```

Output:

```
b[[0, 1, 3]] = array([[0, 1, 2],
                      [1, 2, 3],
                      [3, 4, 5]])
```

### 2. With np.array

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    b = np.array(a)
    print(f"{b[np.array([0, 1, 3])] = }")

if __name__ == "__main__":
    main()
```

Output:

```
b[np.array([0, 1, 3])] = array([[0, 1, 2],
                                [1, 2, 3],
                                [3, 4, 5]])
```


## Multi-Axis Fancy

Index both rows and columns simultaneously.

### 1. Paired Indices

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    b = np.array(a)
    print(f"{b[[0, 1, 3], [0, 0, -1]] = }")

if __name__ == "__main__":
    main()
```

Output:

```
b[[0, 1, 3], [0, 0, -1]] = array([0, 1, 6])
```

### 2. How It Works

Pairs `(row[i], col[i])` are selected: `(0,0)`, `(1,0)`, `(3,-1)`.

### 3. With np.array

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    b = np.array(a)
    print(f"{b[np.array([0, 1, 3]), np.array([0, 0, -1])] = }")

if __name__ == "__main__":
    main()
```

Output:

```
b[np.array([0, 1, 3]), np.array([0, 0, -1])] = array([0, 1, 6])
```


## Boolean Masking

Select elements where a condition is True.

### 1. Create Mask

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
mask = arr > 20
print(f"{mask = }")
print(f"{arr[mask] = }")
```

Output:

```
mask = array([False, False,  True,  True,  True])
arr[mask] = array([30, 40, 50])
```

### 2. Inline Condition

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(f"{arr[arr > 20] = }")
```

Output:

```
arr[arr > 20] = array([30, 40, 50])
```


## Use Cases

Fancy indexing enables expressive data selection.

### 1. Data Filtering

Select rows matching specific criteria from datasets.

### 2. Reordering

Rearrange array elements in arbitrary order.

### 3. Sampling

Select random subsets using random index arrays.
