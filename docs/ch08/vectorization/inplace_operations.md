# In-Place Operations

In-place operations modify arrays without creating new memory allocations.


## Core Concept

In-place operations reduce memory footprint and improve cache efficiency.

### 1. Standard Operation

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
arr = arr * 2  # Creates new array, rebinds name
```

### 2. In-Place Operation

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
arr *= 2  # Modifies array in place
```

### 3. Memory Difference

Standard creates temporary; in-place modifies existing memory.


## Augmented Assignment

Python's augmented assignment operators perform in-place operations.

### 1. Arithmetic In-Place

```python
import numpy as np

arr = np.array([1, 2, 3, 4], dtype=float)

arr += 10    # Add
arr -= 5     # Subtract
arr *= 2     # Multiply
arr /= 4     # Divide
arr **= 2    # Power
arr //= 3    # Floor divide
arr %= 2     # Modulo

print(arr)
```

### 2. Bitwise In-Place

```python
import numpy as np

arr = np.array([1, 2, 3, 4], dtype=int)

arr &= 3     # AND
arr |= 8     # OR
arr ^= 1     # XOR
```


## Memory Verification

Verify that in-place operations don't create new arrays.

### 1. id() Check

```python
import numpy as np

def main():
    arr = np.array([1, 2, 3, 4])
    original_id = id(arr)
    
    arr *= 2
    
    print(f"ID unchanged: {id(arr) == original_id}")

if __name__ == "__main__":
    main()
```

Output:

```
ID unchanged: True
```

### 2. Standard Creates New

```python
import numpy as np

def main():
    arr = np.array([1, 2, 3, 4])
    original_id = id(arr)
    
    arr = arr * 2
    
    print(f"ID unchanged: {id(arr) == original_id}")

if __name__ == "__main__":
    main()
```

Output:

```
ID unchanged: False
```


## out Parameter

Many NumPy functions support an `out` parameter for in-place results.

### 1. Using out

```python
import numpy as np

def main():
    a = np.array([1, 2, 3, 4])
    result = np.empty_like(a)
    
    np.multiply(a, 2, out=result)
    print(result)

if __name__ == "__main__":
    main()
```

### 2. Same Array out

```python
import numpy as np

def main():
    arr = np.array([1, 2, 3, 4])
    np.multiply(arr, 2, out=arr)
    print(arr)

if __name__ == "__main__":
    main()
```

Output:

```
[2 4 6 8]
```

### 3. Chained Operations

```python
import numpy as np

def main():
    arr = np.array([1.0, 2.0, 3.0, 4.0])
    np.sqrt(arr, out=arr)
    np.multiply(arr, 10, out=arr)
    print(arr)

if __name__ == "__main__":
    main()
```


## Performance Benefit

In-place operations improve performance for large arrays.

### 1. Timing Comparison

```python
import numpy as np
import time

def main():
    n = 10_000_000
    
    # Standard operation
    arr1 = np.random.randn(n)
    start = time.perf_counter()
    arr1 = arr1 * 2
    standard_time = time.perf_counter() - start
    
    # In-place operation
    arr2 = np.random.randn(n)
    start = time.perf_counter()
    arr2 *= 2
    inplace_time = time.perf_counter() - start
    
    print(f"Standard time: {standard_time:.4f} sec")
    print(f"In-place time: {inplace_time:.4f} sec")

if __name__ == "__main__":
    main()
```

### 2. Cache Efficiency

In-place avoids cache eviction from temporary allocations.


## Caveats

Be aware of in-place operation limitations.

### 1. View Side Effects

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
view = arr[1:3]
view *= 10
print(arr)  # [1 20 30 4]
```

### 2. dtype Constraints

In-place operations cannot change dtype.

### 3. Broadcasting Limit

In-place requires compatible shapes without expansion.
