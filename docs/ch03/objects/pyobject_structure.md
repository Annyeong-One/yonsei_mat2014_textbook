# PyObject Structure

## CPython Internal

### 1. Base Structure

Every object has:
- Reference count
- Type pointer
- Value data

### 2. Reference Count

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))

y = x
print(sys.getrefcount(x))  # Increased
```

## Type Object

### 1. Type Info

```python
x = [1, 2, 3]

# Type determines behavior
print(type(x).__name__)
```

## Object Data

### 1. Type-Specific

```python
x = 42              # Integer data
s = "hello"         # String data
lst = [1, 2, 3]     # List items
```

## Memory Layout

### 1. Heap Allocation

```python
# All objects on heap
x = 42
y = [1, 2, 3]
z = "hello"
```

## Three Properties

### 1. In Python

```python
x = [1, 2, 3]

print(id(x))        # Identity
print(type(x))      # Type
print(x)            # Value
```

## Summary

### 1. Every Object

- Reference count
- Type pointer
- Value data

### 2. Enables

- Auto memory management
- Dynamic typing
- Efficient sharing
