# Weakref Advanced

## WeakMethod

### 1. Bound Methods

```python
import weakref

class MyClass:
    def method(self):
        pass

obj = MyClass()
weak_method = weakref.WeakMethod(obj.method)
```

## Proxy Objects

### 1. Transparent Weak Refs

```python
import weakref

obj = [1, 2, 3]
proxy = weakref.proxy(obj)

# Use like normal object
print(proxy[0])  # 1
```

## Summary

- WeakMethod for bound methods
- Proxy for transparent access
- Advanced use cases
