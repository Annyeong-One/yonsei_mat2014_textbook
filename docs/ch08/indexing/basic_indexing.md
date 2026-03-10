# Basic Indexing


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

NumPy arrays support flexible indexing to access individual elements.


## Positive Indexing

Access elements using zero-based positive indices.

### 1. 1D Array Access

```python
import numpy as np

def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"{a[1] = }")

    b = np.array(a)
    print(f"{b[1] = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[1] = 1
b[1] = 1
```

### 2. 2D Array Access

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    print(f"{a[1] = }")

    b = np.array(a)
    print(f"{b[1] = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[1] = [1, 2, 3]
b[1] = array([1, 2, 3])
```


## Negative Indexing

Access elements from the end using negative indices.

### 1. 1D Negative Index

```python
import numpy as np

def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"{a[-2] = }")

    b = np.array(a)
    print(f"{b[-2] = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[-2] = 8
b[-2] = 8
```

### 2. 2D Negative Index

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    print(f"{a[-2] = }")

    b = np.array(a)
    print(f"{b[-2] = }, {b[-2].shape = }")
    print(f"{b[-2:-1] = }, {b[-2:-1].shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[-2] = [3, 4, 5]
b[-2] = array([3, 4, 5]), b[-2].shape = (3,)
b[-2:-1] = array([[3, 4, 5]]), b[-2:-1].shape = (1, 3)
```


## List-like Indexing

Chain indices with multiple brackets, works for both lists and arrays.

### 1. Positive Chaining

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    print(f"{a[1][1] = }")

    b = np.array(a)
    print(f"{b[1][1] = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[1][1] = 2
b[1][1] = 2
```

### 2. Negative Chaining

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    print(f"{a[-2][-2] = }")

    b = np.array(a)
    print(f"{b[-2][-2] = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[-2][-2] = 4
b[-2][-2] = 4
```


## NumPy-Only Indexing

Use comma-separated indices inside single brackets (NumPy exclusive).

### 1. Tuple Syntax

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    try:
        print(f"{a[1, 1] = }")
    except TypeError as e:
        print(f"List error: {e}")

    b = np.array(a)
    print(f"{b[1, 1] = }")

if __name__ == "__main__":
    main()
```

Output:

```
List error: list indices must be integers or slices, not tuple
b[1, 1] = 2
```

### 2. Negative Tuple

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    try:
        print(f"{a[-2, -2] = }")
    except TypeError as e:
        print(f"List error: {e}")

    b = np.array(a)
    print(f"{b[-2, -2] = }")

if __name__ == "__main__":
    main()
```

Output:

```
List error: list indices must be integers or slices, not tuple
b[-2, -2] = 4
```


## Iteration Example

Print all elements of a 2D array using indexing.

### 1. Nested Loop

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    rows, cols = a.shape

    for i in range(rows):
        for j in range(cols):
            element = a[i, j]
            if j != cols - 1:
                print(element, end=' ')
            else:
                print(element)

if __name__ == "__main__":
    main()
```

Output:

```
1 2 3
4 5 6
```

### 2. Shape Unpacking

Use `a.shape` to get dimensions for iteration bounds.
