# View vs Copy Basics

NumPy operations return either views (shared memory) or copies (independent memory).


## Core Concept

Understanding memory sharing is essential for correct NumPy code.

### 1. View Definition

A view shares memory with the original array; mutations propagate to both.

### 2. Copy Definition

A copy allocates new memory; mutations are isolated from the original.

### 3. Default Behavior

NumPy prefers views for fast computation and efficient memory usage.


## Visual Comparison

Views and copies have different memory relationships.

### 1. View Diagram

```
Original Array:  [1, 2, 3, 4, 5]
                      ↑
                 (shared memory)
                      ↓
View:               [2, 3, 4]
```

### 2. Copy Diagram

```
Original Array:  [1, 2, 3, 4, 5]
                 (separate memory)
Copy:               [2, 3, 4]
```


## Basic Demonstration

Observe how views and copies behave differently.

### 1. View Mutation

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
view = arr[1:4]
view[0] = 99
print(arr)  # [1 99 3 4 5]
```

The original array is modified.

### 2. Copy Mutation

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
copy = arr[1:4].copy()
copy[0] = -1
print(arr)  # [1 2 3 4 5]
```

The original array is unchanged.


## Why Views Exist

Views provide significant performance benefits.

### 1. Memory Efficiency

No data duplication means lower memory consumption.

### 2. Speed

Avoiding memory allocation and copying is faster.

### 3. Large Arrays

Critical when working with gigabyte-scale datasets.


## When to Copy

Explicit copies protect data integrity.

### 1. Data Preservation

Copy when you need to preserve the original unchanged.

### 2. Multi-threaded Code

Copy to avoid race conditions in parallel processing.

### 3. Function Returns

Copy when returning array subsets from functions.
