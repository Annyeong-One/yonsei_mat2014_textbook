# NumPy vs C Arrays


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

NumPy arrays and C arrays share memory layout but differ significantly in functionality.


## Memory Layout

Both use contiguous memory blocks for efficiency.

### 1. Contiguous Storage

Both C arrays and NumPy arrays store elements in contiguous memory locations.

### 2. Cache Efficiency

Contiguous layout enables efficient CPU cache utilization.

### 3. SIMD Operations

Both can benefit from SIMD (Single Instruction, Multiple Data) vectorization.


## Size and Flexibility

C arrays are static; NumPy arrays are dynamic.

### 1. C Array Static Size

```c
// C code - size fixed at compile time
int arr[10];  // Cannot resize
```

### 2. NumPy Dynamic Size

```python
import numpy as np

arr = np.array([1, 2, 3])
arr = np.append(arr, [4, 5])  # Can resize
arr = arr.reshape((5, 1))     # Can reshape
```

### 3. Trade-off

Static size in C enables compiler optimizations; dynamic size in NumPy offers flexibility.


## Dimensionality

NumPy natively supports multi-dimensional arrays.

### 1. C Multi-Dimensional

```c
// C code - nested arrays
int matrix[3][4];  // 3x4 matrix
// Accessing: matrix[i][j]
```

### 2. NumPy N-Dimensional

```python
import numpy as np

matrix = np.zeros((3, 4))       # 2D
tensor = np.zeros((3, 4, 5))    # 3D
hyper = np.zeros((2, 3, 4, 5))  # 4D
```

### 3. Arbitrary Dimensions

NumPy handles any number of dimensions seamlessly.


## Built-in Operations

NumPy provides extensive mathematical functions.

### 1. C Manual Operations

```c
// C code - must implement manually
for (int i = 0; i < n; i++) {
    result[i] = a[i] + b[i];
}
```

### 2. NumPy Vectorized

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Built-in operations
c = a + b           # Element-wise add
d = np.dot(a, b)    # Dot product
e = np.sin(a)       # Trigonometric
f = np.sum(a)       # Reduction
```

### 3. Linear Algebra

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])

inv = np.linalg.inv(A)      # Matrix inverse
det = np.linalg.det(A)      # Determinant
eig = np.linalg.eig(A)      # Eigenvalues
```


## Type Support

NumPy supports more data types than C arrays.

### 1. C Primitive Types

```c
// C code - limited types
int arr_int[10];
float arr_float[10];
double arr_double[10];
```

### 2. NumPy Extended Types

```python
import numpy as np

# Standard types
arr_int = np.zeros(10, dtype=np.int64)
arr_float = np.zeros(10, dtype=np.float64)

# Extended types
arr_complex = np.zeros(10, dtype=np.complex128)
arr_bool = np.zeros(10, dtype=np.bool_)
arr_str = np.array(['a', 'b', 'c'])
```

### 3. Custom dtypes

NumPy supports structured arrays with named fields.


## Performance

Both achieve high performance through different means.

### 1. C Compilation

C arrays benefit from ahead-of-time compilation and direct hardware access.

### 2. NumPy Backend

```
NumPy Python API
       ↓
   C Extensions
       ↓
 BLAS/LAPACK Libraries
       ↓
  Optimized Machine Code
```

### 3. When C Wins

Custom algorithms with complex control flow.

### 4. When NumPy Wins

Standard numerical operations with vectorization.


## Comparison Summary

Key differences at a glance.

### 1. C Array Traits

- Low-level, close to hardware
- Static size, fixed at compile time
- Manual memory management
- Limited built-in operations
- Maximum control and performance

### 2. NumPy Array Traits

- High-level, Python interface
- Dynamic size and reshape
- Automatic memory management
- Rich mathematical functions
- Rapid development and readability

### 3. Choosing Between

Use C for embedded systems and maximum control; use NumPy for scientific computing and productivity.
