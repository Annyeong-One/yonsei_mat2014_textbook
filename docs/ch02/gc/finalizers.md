# Finalizers

## __del__ Method

### 1. Called on GC

```python
class Resource:
    def __del__(self):
        print("Resource freed")

obj = Resource()
del obj  # Prints: Resource freed
```

### 2. Not Guaranteed

```python
class Resource:
    def __del__(self):
        self.cleanup()

# May not be called if:
# - Program exits abruptly
# - Circular references
# - Exceptions in __del__
```

## Problems

### 1. Resurrection

```python
saved = None

class Item:
    def __del__(self):
        global saved
        saved = self  # Resurrect!

obj = Item()
del obj
print(saved)  # Object still exists
```

### 2. Cycles

```python
class Item:
    def __init__(self):
        self.ref = None
    
    def __del__(self):
        print("Cleaning")

a = Item()
b = Item()
a.ref = b
b.ref = a

# __del__ might not be called
```

## Best Practices

### 1. Avoid __del__

```python
# Instead of __del__
class Resource:
    def close(self):
        # Explicit cleanup
        pass

r = Resource()
try:
    use(r)
finally:
    r.close()
```

### 2. Use Context Manager

```python
class Resource:
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.cleanup()

# Guaranteed cleanup
with Resource() as r:
    use(r)
```

### 3. weakref Callbacks

```python
import weakref

def cleanup(ref):
    print("Object collected")

obj = SomeObject()
ref = weakref.ref(obj, cleanup)

# cleanup called on GC
```

## Summary

- __del__ unreliable
- Resurrection possible
- Cycles problematic
- Use context managers
- Or weakref callbacks
