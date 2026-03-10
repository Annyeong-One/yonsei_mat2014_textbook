# Lists vs Arrays


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Performance

### 1. Speed Comparison

```python
import numpy as np
import time

n = 1000000

# Python list
x_list = list(range(n))
start = time.time()
y_list = [xi**2 for xi in x_list]
list_time = time.time() - start

# NumPy array
x_array = np.arange(n)
start = time.time()
y_array = x_array**2
array_time = time.time() - start

print(f"List: {list_time:.3f}s")
print(f"Array: {array_time:.3f}s")
print(f"Speedup: {list_time/array_time:.1f}x")
```

### 2. Memory

```python
import sys

# List overhead
lst = [1, 2, 3, 4, 5]
print(sys.getsizeof(lst))  # 104 bytes

# Array efficiency
arr = np.array([1, 2, 3, 4, 5])
print(arr.nbytes)  # 40 bytes (8 bytes × 5)
```

### 3. Operations

```python
# List - element-wise requires loop
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
result = [a + b for a, b in zip(lst1, lst2)]

# Array - vectorized
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = arr1 + arr2  # Fast, single operation
```

## Type Flexibility

### 1. Lists - Heterogeneous

```python
mixed = [1, 'hello', 3.14, [1, 2], {'key': 'value'}]
```

### 2. Arrays - Homogeneous

```python
arr = np.array([1, 2, 3])  # All int64
# arr = np.array([1, 'hello'])  # Converts all to str
```

### 3. Trade-offs

Lists: Flexible but slow
Arrays: Fast but rigid types

## Use Cases

### 1. Use Lists When

- Heterogeneous data
- Dynamic resizing
- General collections
- Small datasets

### 2. Use Arrays When

- Numerical computation
- Linear algebra
- Large datasets
- Performance critical

### 3. Example

```python
# List - collection
students = ['Alice', 'Bob', 'Charlie']

# Array - numerical data
scores = np.array([85, 92, 78])
mean_score = scores.mean()
```
