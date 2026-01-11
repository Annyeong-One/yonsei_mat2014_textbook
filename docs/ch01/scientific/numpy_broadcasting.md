# Broadcasting Rules

## Fundamentals

### 1. Definition

Broadcasting allows operations between arrays of different shapes by automatically expanding dimensions.

### 2. Basic Rule

Two dimensions are compatible when:
- They are equal, or
- One of them is 1

### 3. Simple Example

```python
import numpy as np

a = np.array([[1], [2], [3]])  # (3, 1)
b = np.array([10, 20, 30])     # (3,)
c = a + b  # Broadcasts to (3, 3)
```

## Broadcasting Mechanics

### 1. Dimension Alignment

NumPy aligns shapes from right to left:

```python
# (3, 4) + (4,)
# Becomes: (3, 4) + (1, 4) → (3, 4) ✅

# (3, 4) + (3, 1)
# Both compatible → (3, 4) ✅
```

### 2. Stretching

Size-1 dimensions stretch to match:

```python
a = np.ones((3, 1, 4))
b = np.ones((1, 2, 1))
c = a + b  # (3, 2, 4)
```

### 3. Incompatibility

```python
a = np.ones((3, 4))
b = np.ones((3,))
# Incompatible: can't align (3,) with columns
```

## Common Patterns

### 1. Row-wise Operations

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row_mean = matrix.mean(axis=1, keepdims=True)  # (2, 1)
centered = matrix - row_mean  # Broadcasting (2, 3) - (2, 1)
```

### 2. Column-wise Operations

```python
col_std = matrix.std(axis=0, keepdims=True)  # (1, 3)
normalized = matrix / col_std  # Broadcasting (2, 3) / (1, 3)
```

### 3. Outer Product

```python
a = np.array([1, 2, 3])[:, np.newaxis]  # (3, 1)
b = np.array([10, 20])                   # (2,)
outer = a * b  # (3, 2)
```
