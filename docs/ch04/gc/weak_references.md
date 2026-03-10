# Weak References


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Weak references allow referencing objects without preventing garbage collection.

## Basic Weak References

```python
import weakref

class MyClass:
    pass

obj = MyClass()
weak_ref = weakref.ref(obj)

# Access via call
print(weak_ref())  # <MyClass object>

# After deletion
del obj
print(weak_ref())  # None (object was collected)
```

## WeakValueDictionary

A dictionary that doesn't prevent values from being garbage collected:

```python
import weakref

class Data:
    def __init__(self, value):
        self.value = value

cache = weakref.WeakValueDictionary()

obj = Data(42)
cache['key'] = obj

print(cache['key'].value)  # 42

del obj
# cache['key'] no longer exists (auto-removed)
```

## WeakKeyDictionary

A dictionary that doesn't prevent keys from being garbage collected:

```python
import weakref

cache = weakref.WeakKeyDictionary()

key = MyClass()
cache[key] = "value"

del key
# Entry auto-removed when key is collected
```

---

## Advanced Features

### WeakMethod

For weak references to bound methods:

```python
import weakref

class MyClass:
    def method(self):
        return "called"

obj = MyClass()
weak_method = weakref.WeakMethod(obj.method)

# Call the weak method
result = weak_method()()  # First () gets method, second () calls it
print(result)  # "called"
```

### Proxy Objects

Transparent weak references that act like the original object:

```python
import weakref

obj = [1, 2, 3]
proxy = weakref.proxy(obj)

# Use like normal object
print(proxy[0])  # 1
print(len(proxy))  # 3
proxy.append(4)
print(obj)  # [1, 2, 3, 4]

# After deletion
del obj
# proxy[0]  # ReferenceError: weakly-referenced object no longer exists
```

### Callbacks

Execute code when referenced object is collected:

```python
import weakref

def callback(ref):
    print("Object was collected!")

obj = MyClass()
weak_ref = weakref.ref(obj, callback)

del obj  # Prints: "Object was collected!"
```

---

## Limitations

### Types That Support Weak References

Most objects can be weakly referenced:

```python
import weakref

# These work
ref = weakref.ref([1, 2, 3])      # list
ref = weakref.ref({1, 2, 3})      # set
ref = weakref.ref({'a': 1})       # dict
ref = weakref.ref(MyClass())      # user-defined classes
```

### Types That Don't Support Weak References

Built-in immutable types cannot be weakly referenced:

```python
import weakref

# These raise TypeError
# weakref.ref(42)           # int
# weakref.ref("hello")      # str
# weakref.ref((1, 2, 3))    # tuple
# weakref.ref(None)         # NoneType
# weakref.ref(True)         # bool
```

### Enabling Weak References in Custom Classes

By default, classes with `__slots__` don't support weak references:

```python
class NoWeakRef:
    __slots__ = ['x', 'y']

# weakref.ref(NoWeakRef())  # TypeError

# Add __weakref__ to slots to enable
class WithWeakRef:
    __slots__ = ['x', 'y', '__weakref__']

ref = weakref.ref(WithWeakRef())  # Works
```

---

## Use Cases

### Caching

```python
import weakref

class ExpensiveObject:
    pass

_cache = weakref.WeakValueDictionary()

def get_cached(key):
    if key not in _cache:
        _cache[key] = ExpensiveObject()
    return _cache[key]

# Objects removed from cache when no longer referenced elsewhere
```

### Observer Pattern

```python
import weakref

class Subject:
    def __init__(self):
        self._observers = weakref.WeakSet()
    
    def attach(self, observer):
        self._observers.add(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update()

# Observers auto-removed when deleted
```

### Parent-Child References

```python
import weakref

class Child:
    def __init__(self, parent):
        self._parent = weakref.ref(parent)
    
    @property
    def parent(self):
        return self._parent()

# Avoids circular reference preventing garbage collection
```

---

## Summary

| Type | Description | Use Case |
|------|-------------|----------|
| `weakref.ref()` | Basic weak reference | General use |
| `WeakValueDictionary` | Dict with weak values | Caching |
| `WeakKeyDictionary` | Dict with weak keys | Metadata storage |
| `WeakSet` | Set with weak members | Observer pattern |
| `WeakMethod` | Weak reference to bound method | Callbacks |
| `proxy()` | Transparent weak reference | Drop-in replacement |

Key points:
- Weak references don't prevent garbage collection
- Useful for caches and avoiding circular references
- Not all types support weak references
- Add `__weakref__` to `__slots__` if needed
