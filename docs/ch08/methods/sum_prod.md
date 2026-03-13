# Sum Prod Cumsum

## sum and np.sum

### 1. Basic Usage

Sum all elements or along an axis.

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 1],
                  [2, 3]])
    
    print("a =")
    print(a)
    print()
    
    print(f"{a.sum() = }")
    print(f"{a.sum(axis=0) = }")
    print(f"{a.sum(axis=1) = }")

if __name__ == "__main__":
    main()
```

**Output:**

```
a =
[[1 2]
 [3 1]
 [2 3]]

a.sum() = 12
a.sum(axis=0) = array([6, 6])
a.sum(axis=1) = array([3, 4, 5])
```

### 2. Function Syntax

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 1],
                  [2, 3]])
    
    print("a =")
    print(a)
    print()
    
    print(f"{np.sum(a) = }")
    print(f"{np.sum(a, axis=0) = }")
    print(f"{np.sum(a, axis=1) = }")

if __name__ == "__main__":
    main()
```

### 3. Row and Column Sum

```python
import numpy as np

def main():
    a = np.array([
        [8, 3, 9, 0, 10],
        [3, 5, 17, 1, 1],
        [2, 8, 6, 23, 1],
        [15, 7, 3, 2, 9],
        [6, 14, 2, 6, 0],
    ])
    
    print("Matrix:")
    print(a)
    print()
    
    print(f"Total Sum  : {a.sum()}")
    print(f"Column Sum : {a.sum(axis=0)}")
    print(f"Row Sum    : {a.sum(axis=1)}")

if __name__ == "__main__":
    main()
```

**Output:**

```
Matrix:
[[ 8  3  9  0 10]
 [ 3  5 17  1  1]
 [ 2  8  6 23  1]
 [15  7  3  2  9]
 [ 6 14  2  6  0]]

Total Sum  : 150
Column Sum : [34 37 37 32 21]
Row Sum    : [30 27 40 36 28]
```

## cumsum and np.cumsum

### 1. Basic Usage

Cumulative sum returns running totals.

```python
import numpy as np

def main():
    a = np.array([1, 2, 3, 4, 5])
    
    print(f"a = {a}")
    print(f"cumsum = {a.cumsum()}")
    # [1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5]
    # [1, 3, 6, 10, 15]

if __name__ == "__main__":
    main()
```

### 2. With axis Parameter

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 1],
                  [2, 3]])
    
    print("a =")
    print(a)
    print()
    
    print("a.cumsum() (flattened):")
    print(a.cumsum())
    print()
    
    print("a.cumsum(axis=0) (down columns):")
    print(a.cumsum(axis=0))
    print()
    
    print("a.cumsum(axis=1) (across rows):")
    print(a.cumsum(axis=1))

if __name__ == "__main__":
    main()
```

**Output:**

```
a =
[[1 2]
 [3 1]
 [2 3]]

a.cumsum() (flattened):
[ 1  3  6  7  9 12]

a.cumsum(axis=0) (down columns):
[[1 2]
 [4 3]
 [6 6]]

a.cumsum(axis=1) (across rows):
[[1 3]
 [3 4]
 [2 5]]
```

### 3. Function Syntax

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 1],
                  [2, 3]])
    
    print("a =")
    print(a)
    print()
    
    print("np.cumsum(a):")
    print(np.cumsum(a))
    print()
    
    print("np.cumsum(a, axis=0):")
    print(np.cumsum(a, axis=0))
    print()
    
    print("np.cumsum(a, axis=1):")
    print(np.cumsum(a, axis=1))

if __name__ == "__main__":
    main()
```

## prod and np.prod

### 1. Basic Usage

Product of all elements or along an axis.

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 1],
                  [2, 3]])
    
    print("a =")
    print(a)
    print()
    
    print(f"{a.prod() = }")
    print(f"{a.prod(axis=0) = }")
    print(f"{a.prod(axis=1) = }")

if __name__ == "__main__":
    main()
```

**Output:**

```
a =
[[1 2]
 [3 1]
 [2 3]]

a.prod() = 36
a.prod(axis=0) = array([6, 6])
a.prod(axis=1) = array([2, 3, 6])
```

### 2. Function Syntax

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 1],
                  [2, 3]])
    
    print("a =")
    print(a)
    print()
    
    print(f"{np.prod(a) = }")
    print(f"{np.prod(a, axis=0) = }")
    print(f"{np.prod(a, axis=1) = }")

if __name__ == "__main__":
    main()
```

### 3. Factorial Example

```python
import numpy as np

def main():
    # Compute 5! = 1 * 2 * 3 * 4 * 5
    n = 5
    factorial = np.arange(1, n + 1).prod()
    
    print(f"{n}! = {factorial}")
    
    # Multiple factorials
    for n in range(1, 8):
        fact = np.arange(1, n + 1).prod()
        print(f"{n}! = {fact}")

if __name__ == "__main__":
    main()
```

## cumprod and np.cumprod

### 1. Basic Usage

Cumulative product returns running products.

```python
import numpy as np

def main():
    a = np.array([1, 2, 3, 4, 5])
    
    print(f"a = {a}")
    print(f"cumprod = {a.cumprod()}")
    # [1, 1*2, 1*2*3, 1*2*3*4, 1*2*3*4*5]
    # [1, 2, 6, 24, 120]

if __name__ == "__main__":
    main()
```

### 2. With axis Parameter

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 1],
                  [2, 3]])
    
    print("a =")
    print(a)
    print()
    
    print("a.cumprod() (flattened):")
    print(a.cumprod())
    print()
    
    print("a.cumprod(axis=0) (down columns):")
    print(a.cumprod(axis=0))
    print()
    
    print("a.cumprod(axis=1) (across rows):")
    print(a.cumprod(axis=1))

if __name__ == "__main__":
    main()
```

**Output:**

```
a =
[[1 2]
 [3 1]
 [2 3]]

a.cumprod() (flattened):
[ 1  2  6  6 12 36]

a.cumprod(axis=0) (down columns):
[[1 2]
 [3 2]
 [6 6]]

a.cumprod(axis=1) (across rows):
[[1 2]
 [3 3]
 [2 6]]
```

### 3. Function Syntax

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 1],
                  [2, 3]])
    
    print("a =")
    print(a)
    print()
    
    print("np.cumprod(a):")
    print(np.cumprod(a))
    print()
    
    print("np.cumprod(a, axis=0):")
    print(np.cumprod(a, axis=0))
    print()
    
    print("np.cumprod(a, axis=1):")
    print(np.cumprod(a, axis=1))

if __name__ == "__main__":
    main()
```

## np.squeeze

### 1. Remove Size-1 Dims

`np.squeeze` removes dimensions of size 1.

```python
import numpy as np

def main():
    A = np.zeros((1, 3, 1))
    B = A.squeeze()
    C = A.squeeze(axis=2)
    
    print(f"{A.shape = }")
    print(f"{B.shape = }")
    print(f"{C.shape = }")

if __name__ == "__main__":
    main()
```

**Output:**

```
A.shape = (1, 3, 1)
B.shape = (3,)
C.shape = (1, 3)
```

### 2. Selective Squeeze

```python
import numpy as np

def main():
    a = np.zeros((1, 4, 1, 5, 1))
    
    print(f"Original: {a.shape}")
    print()
    
    # Squeeze all size-1 dimensions
    print(f"squeeze(): {a.squeeze().shape}")
    
    # Squeeze specific axis
    print(f"squeeze(axis=0): {a.squeeze(axis=0).shape}")
    print(f"squeeze(axis=2): {a.squeeze(axis=2).shape}")
    print(f"squeeze(axis=4): {a.squeeze(axis=4).shape}")

if __name__ == "__main__":
    main()
```

### 3. After Reduction

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    # keepdims creates size-1 dimension
    row_sum = a.sum(axis=1, keepdims=True)
    print(f"With keepdims: {row_sum.shape}")
    print(row_sum)
    print()
    
    # Squeeze removes it
    squeezed = row_sum.squeeze()
    print(f"After squeeze: {squeezed.shape}")
    print(squeezed)

if __name__ == "__main__":
    main()
```
