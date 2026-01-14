# Array Creation

NumPy's core object is the **ndarray**, a homogeneous, fixed-size array designed for efficient numerical computation.

## From Python Lists

The most common way to create an array is with `np.array`.

### 1. Basic Creation

```python
import numpy as np

def main():
    a = np.array([1, 2, 3])
    print(a)
    print(f"{a.dtype = }")

if __name__ == "__main__":
    main()
```

All elements are stored with the same **dtype**.

### 2. Nested Lists

```python
import numpy as np

def main():
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6]])
    print(matrix)
    print(f"{matrix.shape = }")

if __name__ == "__main__":
    main()
```

### 3. Explicit Dtype

```python
import numpy as np

def main():
    a = np.array([1, 2, 3], dtype=np.float64)
    print(f"{a = }")
    print(f"{a.dtype = }")

if __name__ == "__main__":
    main()
```

## dtypes Overview

A dtype specifies how many bytes each element uses and how bytes are interpreted.

### 1. Default Inference

```python
import numpy as np

def main():
    a = np.array([1, 2, 3])
    b = np.array([1.0, 2.0])
    
    print(f"int array: {a.dtype}")    # int64 (platform-dependent)
    print(f"float array: {b.dtype}")  # float64

if __name__ == "__main__":
    main()
```

### 2. Explicit Dtype

```python
import numpy as np

def main():
    a = np.array([1, 2, 3], dtype=np.float32)
    b = np.array([1, 2, 3], dtype=np.int8)
    
    print(f"{a.dtype = }")
    print(f"{b.dtype = }")

if __name__ == "__main__":
    main()
```

### 3. Memory Impact

Choosing dtype affects memory usage and precision.

```python
import numpy as np

def main():
    a = np.array([1, 2, 3], dtype=np.float64)
    b = np.array([1, 2, 3], dtype=np.float32)
    
    print(f"float64: {a.nbytes} bytes")
    print(f"float32: {b.nbytes} bytes")

if __name__ == "__main__":
    main()
```

## Common Constructors

NumPy provides efficient array constructors that avoid Python loops.

### 1. Zeros and Ones

```python
import numpy as np

def main():
    a = np.zeros((3, 4))
    b = np.ones((2, 2))
    
    print("zeros((3, 4)):")
    print(a)
    print()
    print("ones((2, 2)):")
    print(b)

if __name__ == "__main__":
    main()
```

### 2. Empty and Full

```python
import numpy as np

def main():
    a = np.empty((5,))    # uninitialized
    b = np.full((2, 3), 7)
    
    print(f"empty: {a}")
    print(f"full: {b}")

if __name__ == "__main__":
    main()
```

### 3. Ranges

```python
import numpy as np

def main():
    a = np.arange(0, 10, 2)
    b = np.linspace(0, 1, 5)
    
    print(f"arange: {a}")
    print(f"linspace: {b}")

if __name__ == "__main__":
    main()
```

## Type Promotion

NumPy promotes types automatically to preserve information.

### 1. Mixed Types

```python
import numpy as np

def main():
    a = np.array([1, 2.5])
    print(f"{a = }")
    print(f"{a.dtype = }")  # float64

if __name__ == "__main__":
    main()
```

### 2. Promotion Rules

```python
import numpy as np

def main():
    int_arr = np.array([1, 2, 3])
    float_arr = np.array([0.5, 1.5, 2.5])
    
    result = int_arr + float_arr
    print(f"{result.dtype = }")  # float64

if __name__ == "__main__":
    main()
```

### 3. Preserving Info

Promotion follows fixed rules to avoid data loss.

```python
import numpy as np

def main():
    a = np.array([1, 2], dtype=np.int32)
    b = np.array([1, 2], dtype=np.int64)
    
    result = a + b
    print(f"{result.dtype = }")  # int64 (wider type)

if __name__ == "__main__":
    main()
```

## Key Takeaways

### 1. Homogeneous Data

ndarrays store elements of a single dtype.

### 2. Dtype Control

dtypes control memory usage and numerical precision.

### 3. Use Constructors

NumPy constructors are optimized and avoid Python loops.
