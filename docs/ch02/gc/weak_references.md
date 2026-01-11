# Weak References

## Overview

### 1. Don't Prevent GC

```python
import weakref

obj = [1, 2, 3]
weak = weakref.ref(obj)

print(weak())  # [1, 2, 3]

del obj
print(weak())  # None (collected)
```

### 2. Use Cases

```python
# Cache without preventing GC
cache = weakref.WeakValueDictionary()

obj = SomeObject()
cache['key'] = obj

# obj can be collected
del obj
# cache['key'] now gone
```

## Types

### 1. WeakRef

```python
import weakref

obj = [1, 2, 3]
ref = weakref.ref(obj)

# Access
if ref() is not None:
    print(ref())
```

### 2. WeakValueDictionary

```python
import weakref

cache = weakref.WeakValueDictionary()
obj = [1, 2, 3]
cache['key'] = obj

# Weak reference stored
```

### 3. WeakSet

```python
import weakref

objects = weakref.WeakSet()
obj = [1, 2, 3]
objects.add(obj)

del obj
# obj removed from set
```

## Callbacks

### 1. On Death

```python
import weakref

def callback(ref):
    print("Object collected")

obj = [1, 2, 3]
ref = weakref.ref(obj, callback)

del obj  # Prints: Object collected
```

## Limitations

### 1. Not All Types

```python
# Can't weakref int, str
# x = 42
# ref = weakref.ref(x)  # TypeError

# But can weakref list, dict
obj = [1, 2, 3]
ref = weakref.ref(obj)  # Works
```

## Summary

- Don't prevent GC
- For caching
- Callbacks available
- Not all types supported
