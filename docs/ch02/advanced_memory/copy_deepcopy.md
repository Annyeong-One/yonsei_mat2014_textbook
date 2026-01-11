# Copy vs Deepcopy

## Shallow Copy

### 1. copy.copy()

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

# Top level copied
print(shallow is original)  # False

# Contents shared
print(shallow[0] is original[0])  # True
```

### 2. Modify Nested

```python
shallow[0].append(3)

print(original)  # [[1, 2, 3], [3, 4]]
print(shallow)   # [[1, 2, 3], [3, 4]]
# Both changed!
```

## Deep Copy

### 1. copy.deepcopy()

```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

# Everything copied
print(deep is original)  # False
print(deep[0] is original[0])  # False
```

### 2. Independent

```python
deep[0].append(3)

print(original)  # [[1, 2], [3, 4]]
print(deep)      # [[1, 2, 3], [3, 4]]
# Only deep changed
```

## When to Use

### 1. Shallow

```python
# Fast, less memory
# OK if no nested mutables
data = [1, 2, 3]
copy = data.copy()
```

### 2. Deep

```python
# Slow, more memory
# Need for nested structures
data = [[1, 2], [3, 4]]
copy = copy.deepcopy(data)
```

## Summary

- Shallow: top level only
- Deep: recursive copy
- Shallow faster
- Deep independent
- Choose based on structure
