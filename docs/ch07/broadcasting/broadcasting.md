# Broadcasting Rules

Broadcasting allows NumPy to perform elementwise operations on arrays of different shapes without explicit loops.


## Motivation

Broadcasting eliminates common inefficiencies in numerical code.

### 1. No Manual Reshaping

Arrays of compatible shapes work directly without explicit dimension manipulation.

### 2. No Explicit Loops

Vectorized operations replace slow Python for-loops.

### 3. No Memory Copies

NumPy virtually expands dimensions without duplicating data in memory.


## Core Rules

NumPy compares shapes from the trailing (rightmost) dimensions.

### 1. Right-to-Left

Dimensions are aligned starting from the last axis and moving left.

### 2. Compatible Sizes

Two dimensions are compatible if they are equal or one of them is 1.

### 3. Expansion Rule

Size-1 dimensions are virtually stretched to match the other array.


## Formal Rule

The compatibility rules expressed mathematically.

### 1. Rule Summary

$$\begin{array}{lll}
s_1=s_2&\Rightarrow&\text{OK}\\
s_1\neq s_2,\ \text{but one of them is 1}&\Rightarrow&\text{OK}\\
\text{one of them does not exist}&\Rightarrow&\text{OK}\\
s_1\neq s_2,\ s_1\neq 1, s_2\neq 1&\Rightarrow&\text{NOT OK}\\
\end{array}$$

### 2. Result Shape

The resultant shape is the element-wise maximum of input shapes across each dimension.


## Visual Alignment

Understanding how shapes align is key to mastering broadcasting.

### 1. Scalar + Vector

```
Array A:         5        shape: ()
Array B:     [1, 2, 3]    shape: (3,)
─────────────────────────────────────
Aligned:         5        shape: (1,) → (3,)
             [1, 2, 3]    shape: (3,)
─────────────────────────────────────
Result:      [6, 7, 8]    shape: (3,)
```

```python
import numpy as np

a = 5
b = np.array([1, 2, 3])
print(a + b)  # [6 7 8]
```

### 2. Vector + Matrix

```
Array A:     [[1, 2, 3],      shape: (2, 3)
              [4, 5, 6]]

Array B:     [10, 20, 30]     shape: (3,)
─────────────────────────────────────────────
Aligned:     [[1, 2, 3],      shape: (2, 3)
              [4, 5, 6]]

             [10, 20, 30]     shape: (1, 3) → (2, 3)
─────────────────────────────────────────────
Result:      [[11, 22, 33],   shape: (2, 3)
              [14, 25, 36]]
```

```python
import numpy as np

M = np.array([[1, 2, 3],
              [4, 5, 6]])
v = np.array([10, 20, 30])
print(M + v)
```

### 3. Column + Row

```
Array A:     [[1],        shape: (3, 1)
              [2],
              [3]]

Array B:     [10, 20]     shape: (2,)
─────────────────────────────────────────────
Aligned:     [[1],        shape: (3, 1) → (3, 2)
              [2],
              [3]]

             [10, 20]     shape: (1, 2) → (3, 2)
─────────────────────────────────────────────
Result:      [[11, 21],   shape: (3, 2)
              [12, 22],
              [13, 23]]
```

```python
import numpy as np

x = np.array([[1], [2], [3]])  # shape (3, 1)
y = np.array([10, 20])          # shape (2,)
print(x + y)
```


## Basic Examples

Simple broadcasting patterns with 2D arrays.

### 1. Matrix × Row

```python
import numpy as np

def main():
    A = np.array([[0, 1], [21, 22]])  # (2, 2)
    B = np.array([[1, 2]])             # (1, 2)
    C = A * B
    print(C)

if __name__ == "__main__":
    main()
```

Output:

```
[[ 0  2]
 [21 44]]
```

### 2. Matrix + Vector

```python
import numpy as np

def main():
    A = np.array([[0, 1], [21, 22]])  # (2, 2)
    B = np.array([1, 2])               #    (2,)
    C = A + B
    print(C)

if __name__ == "__main__":
    main()
```

Output:

```
[[ 1  3]
 [22 24]]
```

### 3. Matrix + Scalar

```python
import numpy as np

def main():
    A = np.array([[1, 2], [3, 4]])  # (2, 2)
    B = 5                            #    ()
    C = A + B
    print(C)

if __name__ == "__main__":
    main()
```

Output:

```
[[6 7]
 [8 9]]
```


## Higher Dimensions

Broadcasting works with tensors of any rank.

### 1. 4D + 3D Arrays

```python
import numpy as np

def main():
    A = np.random.normal(size=(8, 1, 4, 1))
    B = np.random.normal(size=(7, 1, 5))
    C = A + B
    print(f"{A.shape = }")
    print(f"{B.shape =    }")
    print(f"{C.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
A.shape = (8, 1, 4, 1)
B.shape =    (7, 1, 5)
C.shape = (8, 7, 4, 5)
```

### 2. 2D + Singleton

```python
import numpy as np

def main():
    A = np.random.normal(size=(5, 4))
    B = np.random.normal(size=(1,))
    C = A + B
    print(f"{A.shape = }")
    print(f"{B.shape =    }")
    print(f"{C.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
A.shape = (5, 4)
B.shape =    (1,)
C.shape = (5, 4)
```

### 3. 3D + 2D Arrays

```python
import numpy as np

def main():
    A = np.random.normal(size=(15, 3, 5))
    B = np.random.normal(size=(3, 5))
    C = A + B
    print(f"{A.shape = }")
    print(f"{B.shape =     }")
    print(f"{C.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
A.shape = (15, 3, 5)
B.shape =     (3, 5)
C.shape = (15, 3, 5)
```


## Error Cases

Incompatible shapes raise `ValueError`.

### 1. Same Rank Mismatch

```python
import numpy as np

def main():
    A = np.random.normal(size=(2, 3))
    B = np.random.normal(size=(2, 7))
    try:
        C = A + B
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

Output:

```
Error: operands could not be broadcast together with shapes (2,3) (2,7)
```

### 2. Different Rank Mismatch

```python
import numpy as np

def main():
    A = np.random.normal(size=(3, 1))
    B = np.random.normal(size=(8, 4, 3))
    try:
        C = A + B
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

Output:

```
Error: operands could not be broadcast together with shapes (3,1) (8,4,3)
```

### 3. Another Mismatch

```python
import numpy as np

def main():
    A = np.random.normal(size=(2, 1))
    B = np.random.normal(size=(8, 4, 3))
    try:
        C = A + B
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

Output:

```
Error: operands could not be broadcast together with shapes (2,1) (8,4,3)
```


## Normalization Example

A practical application of broadcasting.

### 1. Column-wise Normalize

```python
import numpy as np

def main():
    num_paths, num_steps = 10, 100
    Z = np.random.standard_normal((num_paths, num_steps))
    print(f"{Z.shape              = }")
    print(f"{Z.mean(axis=0).shape =     }")
    print(f"{Z.std(axis=0).shape  =     }")

    Z = (Z - Z.mean(axis=0)) / Z.std(axis=0)
    print(f"{Z.shape              = }")

if __name__ == "__main__":
    main()
```

Output:

```
Z.shape              = (10, 100)
Z.mean(axis=0).shape =     (100,)
Z.std(axis=0).shape  =     (100,)
Z.shape              = (10, 100)
```

### 2. How It Works

`Z.mean(axis=0)` has shape `(100,)` which broadcasts against `Z` with shape `(10, 100)`.


## Performance Compare

Broadcasting dramatically outperforms explicit Python loops.

### 1. Loop Approach

```python
import numpy as np
import time

def add_with_loops(M, v):
    result = np.empty_like(M)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            result[i, j] = M[i, j] + v[j]
    return result

M = np.random.randn(1000, 1000)
v = np.random.randn(1000)

start = time.perf_counter()
result_loop = add_with_loops(M, v)
loop_time = time.perf_counter() - start
print(f"Loop time: {loop_time:.4f} sec")
```

### 2. Broadcast Approach

```python
import numpy as np
import time

M = np.random.randn(1000, 1000)
v = np.random.randn(1000)

start = time.perf_counter()
result_broadcast = M + v
broadcast_time = time.perf_counter() - start
print(f"Broadcast time: {broadcast_time:.6f} sec")
```

### 3. Speedup Factor

```python
import numpy as np
import time

def add_with_loops(M, v):
    result = np.empty_like(M)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            result[i, j] = M[i, j] + v[j]
    return result

def main():
    np.random.seed(42)
    M = np.random.randn(1000, 1000)
    v = np.random.randn(1000)

    start = time.perf_counter()
    result_loop = add_with_loops(M, v)
    loop_time = time.perf_counter() - start

    start = time.perf_counter()
    result_broadcast = M + v
    broadcast_time = time.perf_counter() - start

    assert np.allclose(result_loop, result_broadcast)

    print(f"Loop time:      {loop_time:.4f} sec")
    print(f"Broadcast time: {broadcast_time:.6f} sec")
    print(f"Speedup:        {loop_time / broadcast_time:.0f}x")

if __name__ == "__main__":
    main()
```

Typical output:

```
Loop time:      0.3521 sec
Broadcast time: 0.001243 sec
Speedup:        283x
```


## Memory Efficiency

Broadcasting avoids unnecessary memory allocation.

### 1. No Data Copy

```python
import numpy as np

v = np.array([1, 2, 3])
M = np.zeros((1000, 3))
result = M + v  # v is virtually expanded
```

### 2. Virtual Expansion

NumPy's stride mechanism allows size-1 dimensions to be reused without copying.

### 3. Large Array Savings

For a `(10000, 10000)` matrix plus a `(10000,)` vector, broadcasting saves ~800 MB of memory.


## Common Pitfalls

Avoid these broadcasting mistakes.

### 1. Dimension Assumptions

Erroneous assumptions regarding implicit dimension expansion.

### 2. Missing Reshapes

Failure to use `np.reshape` or `np.newaxis` when necessary.

### 3. Memory Amplification

Unintended memory growth in operations involving large singleton expansions.


## Key Takeaways

Essential points for effective broadcasting.

### 1. Align Right

Shapes are compared from the trailing dimension leftward.

### 2. Size-1 Expands

Dimensions of size 1 stretch to match the corresponding dimension.

### 3. Use for Speed

Broadcasting is 100-1000x faster than Python loops.
