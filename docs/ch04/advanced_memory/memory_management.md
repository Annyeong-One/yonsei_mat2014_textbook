# Memory Management

Understanding copy semantics, memory views, and `__slots__` for efficient memory usage.

## Copy vs Deepcopy

### Shallow Copy

A shallow copy creates a new container but references the same nested objects:

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

# Top level is copied
print(shallow is original)  # False

# Nested objects are shared
print(shallow[0] is original[0])  # True
```

**Mutation affects both:**

```python
shallow[0].append(3)

print(original)  # [[1, 2, 3], [3, 4]]
print(shallow)   # [[1, 2, 3], [3, 4]]
# Both changed!
```

### Deep Copy

A deep copy recursively copies all nested objects:

```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

# Everything is copied
print(deep is original)  # False
print(deep[0] is original[0])  # False
```

**Changes are independent:**

```python
deep[0].append(3)

print(original)  # [[1, 2], [3, 4]]
print(deep)      # [[1, 2, 3], [3, 4]]
# Only deep changed
```

### When to Use Each

| Situation | Use | Example |
|-----------|-----|---------|
| Flat data | Shallow | `[1, 2, 3].copy()` |
| Nested mutable | Deep | `copy.deepcopy(nested)` |
| Performance critical | Shallow | Large data, no nesting |
| Complete independence | Deep | Complex structures |

```python
# Shallow: fast, less memory
data = [1, 2, 3]
backup = data.copy()

# Deep: slow, more memory, but safe
nested = [[1, 2], {'a': [3, 4]}]
backup = copy.deepcopy(nested)
```

---

## Memory Views

Memory views provide zero-copy access to buffer data.

### Creating Memory Views

```python
data = bytearray(b'Hello World')
view = memoryview(data)

# Access without copying
print(view[0])  # 72 (ASCII for 'H')
print(bytes(view[0:5]))  # b'Hello'
```

### Zero-Copy Slicing

```python
data = bytearray(range(100))
view = memoryview(data)

# Slice creates a view, not a copy
slice_view = view[10:20]
print(bytes(slice_view))  # b'\n\x0b\x0c...'

# Verify no copy
slice_view[0] = 255
print(data[10])  # 255 (original modified)
```

### Use Cases

**Large Data Processing:**

```python
import array

arr = array.array('i', range(1000000))
view = memoryview(arr)

# Process in chunks without copying
for i in range(0, len(view), 1000):
    chunk = view[i:i+1000]
    process(chunk)
```

**Network Buffers:**

```python
buffer = bytearray(4096)
view = memoryview(buffer)

# Receive directly into buffer
bytes_received = socket.recv_into(view)

# Process without copying
data = view[:bytes_received]
```

**In-Place Modification:**

```python
data = bytearray(b'Hello')
view = memoryview(data)

view[0] = ord('J')
print(data)  # bytearray(b'Jello')
```

### Memory View Properties

```python
view = memoryview(bytearray(100))

print(view.nbytes)    # Total bytes
print(view.readonly)  # False for bytearray
print(view.format)    # 'B' (unsigned char)
print(view.itemsize)  # 1 byte per item
```

---

## `__slots__`

`__slots__` reduces memory usage by eliminating the instance `__dict__`.

### Without Slots (Default)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
print(p.__dict__)  # {'x': 10, 'y': 20}
```

### With Slots

```python
class Point:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
# p.__dict__  # AttributeError: no __dict__
print(p.x, p.y)  # 10 20
```

### Memory Comparison

```python
import sys

class WithDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

d = WithDict(1, 2)
s = WithSlots(1, 2)

print(sys.getsizeof(d))  # ~48 bytes (+ dict ~104)
print(sys.getsizeof(s))  # ~48 bytes (no dict overhead)
```

### Restrictions

**No Dynamic Attributes:**

```python
class Point:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
# p.z = 30  # AttributeError: 'Point' has no attribute 'z'
```

**Inheritance Considerations:**

```python
class Point:
    __slots__ = ['x', 'y']

class Point3D(Point):
    __slots__ = ['z']  # Only add new slots
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
```

**Enabling Weak References:**

```python
class Point:
    __slots__ = ['x', 'y', '__weakref__']  # Add __weakref__
```

### When to Use `__slots__`

```python
# Good: millions of instances
class Particle:
    __slots__ = ['x', 'y', 'vx', 'vy', 'mass']

particles = [Particle() for _ in range(1000000)]
# Saves significant memory

# Not needed: few instances
class Config:
    def __init__(self):
        self.debug = False
        self.verbose = True
# Only one instance, slots unnecessary
```

---

## Summary

| Technique | Purpose | Use When |
|-----------|---------|----------|
| Shallow copy | Quick duplicate | Flat structures |
| Deep copy | Full independence | Nested mutables |
| Memory views | Zero-copy access | Large buffers |
| `__slots__` | Reduce memory | Many instances |

Key points:
- Understand shallow vs deep copy to avoid aliasing bugs
- Use memory views for efficient buffer manipulation
- Use `__slots__` when creating many instances of a class
- `__slots__` prevents dynamic attribute addition
- Always profile before optimizing
