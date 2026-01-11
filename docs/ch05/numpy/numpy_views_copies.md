# Views vs Copies

## View Semantics

### 1. View Definition

A view shares memory with the original array:

```python
import numpy as np

arr = np.arange(10)
view = arr[::2]  # Slice creates view
view[0] = 999
print(arr[0])  # 999 - modified original
```

### 2. Copy Definition

A copy has independent memory:

```python
arr = np.arange(10)
copy = arr[::2].copy()
copy[0] = 999
print(arr[0])  # 0 - original unchanged
```

### 3. Detection

```python
arr = np.arange(10)
view = arr[::2]
print(view.base is arr)  # True - view
print(view.flags['OWNDATA'])  # False

copy = arr.copy()
print(copy.base is None)  # True - owns data
```

## Creating Views

### 1. Slicing

```python
arr = np.arange(100)
view1 = arr[10:20]    # View
view2 = arr[::2]      # View
view3 = arr[::-1]     # View
```

### 2. Reshaping

```python
arr = np.arange(12)
reshaped = arr.reshape(3, 4)  # View if possible
print(reshaped.base is arr)  # True
```

### 3. Transpose

```python
arr = np.arange(6).reshape(2, 3)
transposed = arr.T  # View
print(transposed.base is arr)  # True
```

## Creating Copies

### 1. Explicit Copy

```python
arr = np.arange(10)
copy = arr.copy()  # Always copies
```

### 2. Fancy Indexing

```python
arr = np.arange(10)
indices = [1, 3, 5]
subset = arr[indices]  # Copy, not view
subset[0] = 999
print(arr[1])  # 1 - unchanged
```

### 3. Boolean Indexing

```python
arr = np.arange(10)
mask = arr > 5
subset = arr[mask]  # Copy
```

## When Views vs Copies

### 1. Basic Indexing → View

```python
arr[5]       # Single element
arr[2:8]     # Slice
arr[::2]     # Stride
arr.T        # Transpose
arr.reshape  # If possible
```

### 2. Fancy Indexing → Copy

```python
arr[[1,3,5]]      # Integer array
arr[arr > 5]      # Boolean array
arr[[True, False, True, ...]]  # Boolean list
```

### 3. Mixed Results

```python
# View then copy
view = arr[2:8]  # View
copy = view[[0, 2, 4]]  # Copy of view
```

## Performance Impact

### 1. Memory Efficiency

```python
# View - no extra memory
large = np.arange(1000000)
view = large[::2]  # Instant, no copy

# Copy - doubles memory
copy = large[::2].copy()  # Allocates 500k elements
```

### 2. Modification Safety

```python
def process(data):
    # Safe - won't modify caller's data
    local = data.copy()
    local += 10
    return local
```

### 3. In-place Operations

```python
arr = np.arange(10)
arr += 10  # In-place, modifies original

view = arr[::2]
view += 100  # Modifies view AND original
```
