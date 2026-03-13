# Slicing Arrays

Slicing extracts contiguous subsequences from arrays using `start:stop:step` syntax.


## 1D Array Slicing

Basic slicing works identically for lists and NumPy arrays.

### 1. Range Slice

```python
import numpy as np

def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = np.array(a)
    print(f"{a = }")
    print(f"{b = }", end="\n\n")

    print(f"{a[1:2] = }")
    print(f"{b[1:2] = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[1:2] = [1]
b[1:2] = array([1])
```

### 2. From Start

```python
import numpy as np

def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = np.array(a)

    print(f"{a[:5] = }")
    print(f"{b[:5] = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[:5] = [0, 1, 2, 3, 4]
b[:5] = array([0, 1, 2, 3, 4])
```

### 3. To End

```python
import numpy as np

def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = np.array(a)

    print(f"{a[1:] = }")
    print(f"{b[1:] = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[1:] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b[1:] = array([1, 2, 3, 4, 5, 6, 7, 8, 9])
```


## Step Slicing

The third parameter specifies the step size.

### 1. Step from Start

```python
import numpy as np

def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = np.array(a)

    print(f"{a[:5:2] = }")
    print(f"{b[:5:2] = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[:5:2] = [0, 2, 4]
b[:5:2] = array([0, 2, 4])
```

### 2. Step to End

```python
import numpy as np

def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = np.array(a)

    print(f"{a[1::2] = }")
    print(f"{b[1::2] = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[1::2] = [1, 3, 5, 7, 9]
b[1::2] = array([1, 3, 5, 7, 9])
```

### 3. Reverse Array

```python
import numpy as np

def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = np.array(a)

    print(f"{a[::-1] = }")
    print(f"{b[::-1] = }")

if __name__ == "__main__":
    main()
```

Output:

```
a[::-1] = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
b[::-1] = array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
```


## 2D Array Slicing

Slicing 2D arrays operates on rows by default.

### 1. Row Range

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    b = np.array(a)

    print("a[:3]")
    print(a[:3], end="\n\n")
    print("b[:3]")
    print(b[:3])

if __name__ == "__main__":
    main()
```

### 2. Row with Step

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    b = np.array(a)

    print("a[:4:2]")
    print(a[:4:2], end="\n\n")
    print("b[:4:2]")
    print(b[:4:2])

if __name__ == "__main__":
    main()
```

### 3. Reverse Rows

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    b = np.array(a)

    print("a[::-1]")
    print(a[::-1], end="\n\n")
    print("b[::-1]")
    print(b[::-1])

if __name__ == "__main__":
    main()
```


## Multi-Axis Slicing

NumPy allows simultaneous slicing across multiple axes.

### 1. Row Slice Only

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    b = np.array(a)

    try:
        print(a[1, :])
    except TypeError as e:
        print(f"List error: {e}")
    print("b[1, :]")
    print(b[1, :])

if __name__ == "__main__":
    main()
```

Output:

```
List error: list indices must be integers or slices, not tuple
b[1, :]
[1 2 3]
```

### 2. Column Slice Only

```python
import numpy as np

def main():
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    b = np.array(a)

    try:
        print(a[:, 1])
    except TypeError as e:
        print(f"List error: {e}")
    print("b[:, 1]")
    print(b[:, 1])

if __name__ == "__main__":
    main()
```

Output:

```
List error: list indices must be integers or slices, not tuple
b[:, 1]
[1 2 3 4 5]
```

### 3. Both Axes

```python
import numpy as np

mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat[0:2, 1:])
```

Output:

```
[[2 3]
 [5 6]]
```
