# Memory Views

## memoryview Objects

### 1. Zero-Copy

```python
data = bytearray(b'Hello World')
view = memoryview(data)

# Access without copying
print(view[0])  # 72 (H)
```

### 2. Slicing

```python
data = bytearray(range(10))
view = memoryview(data)

# View slice (no copy)
slice_view = view[2:5]
print(bytes(slice_view))  # b''
```

## Use Cases

### 1. Large Data

```python
# Efficient for large arrays
import array

arr = array.array('i', range(1000000))
view = memoryview(arr)

# Process without copying
```

### 2. Network Buffers

```python
# Efficient buffer handling
buffer = bytearray(1024)
view = memoryview(buffer)

# Read into view
socket.recv_into(view)
```

## Modification

### 1. In-Place

```python
data = bytearray(b'Hello')
view = memoryview(data)

view[0] = ord('J')
print(data)  # bytearray(b'Jello')
```

## Summary

- Zero-copy views
- Efficient for large data
- In-place modification
- Network buffers
