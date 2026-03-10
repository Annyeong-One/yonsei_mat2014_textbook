# Weak Reference Patterns


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Observer Pattern

The observer pattern often creates memory leaks because observables hold strong references to observers. Use `WeakSet` to allow observers to be garbage collected when no longer needed elsewhere.

### Problem: Strong References

```python
class Observable:
    def __init__(self):
        self._observers = set()  # Strong references
    
    def subscribe(self, observer):
        self._observers.add(observer)
    
    def notify(self):
        for obs in self._observers:
            obs.update()

# Problem: observers never garbage collected
# even when no other references exist
```

### Solution: WeakSet

```python
import weakref

class Observable:
    def __init__(self):
        self._observers = weakref.WeakSet()
    
    def subscribe(self, observer):
        self._observers.add(observer)
    
    def unsubscribe(self, observer):
        self._observers.discard(observer)
    
    def notify(self):
        # Dead observers automatically removed
        for obs in self._observers:
            obs.update()

# Usage
class Observer:
    def update(self):
        print("Notified!")

subject = Observable()
obs = Observer()
subject.subscribe(obs)

subject.notify()  # "Notified!"

del obs  # Observer can now be garbage collected
subject.notify()  # Nothing happens — observer is gone
```

---

## Self-Cleaning Cache

Caches can consume unbounded memory. Use `WeakValueDictionary` to automatically evict entries when cached objects are no longer referenced elsewhere.

### Problem: Unbounded Cache

```python
cache = {}

def get_object(key):
    if key not in cache:
        obj = create_expensive_object(key)
        cache[key] = obj  # Stays forever!
    return cache[key]

# Cache grows without bound
```

### Solution: WeakValueDictionary

```python
import weakref

cache = weakref.WeakValueDictionary()

def get_object(key):
    obj = cache.get(key)
    if obj is None:
        obj = create_expensive_object(key)
        cache[key] = obj
    return obj

# When no other references to obj exist,
# it's automatically removed from cache
```

### Example: Image Cache

```python
import weakref

class ImageCache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    
    def get_image(self, path):
        image = self._cache.get(path)
        if image is None:
            image = load_image(path)  # Expensive
            self._cache[path] = image
        return image

# Images are cached while in use
# Automatically evicted when no longer referenced
```

---

## Parent-Child Relationships

Bidirectional relationships create reference cycles. Use weak references for back-references (child → parent) to allow garbage collection.

### Problem: Reference Cycle

```python
class Parent:
    def __init__(self):
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self  # Strong back-reference

class Child:
    def __init__(self):
        self.parent = None  # Creates cycle when set

# Cycle: parent -> child -> parent
# Requires cycle GC, delays cleanup
```

### Solution: Weak Back-Reference

```python
import weakref

class Parent:
    def __init__(self):
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.set_parent(self)

class Child:
    def __init__(self):
        self._parent_ref = None
    
    def set_parent(self, parent):
        self._parent_ref = weakref.ref(parent)
    
    @property
    def parent(self):
        if self._parent_ref is None:
            return None
        return self._parent_ref()  # Returns None if parent is dead

# No cycle: parent -> child -> weak_ref
# Parent can be garbage collected immediately
```

### Tree Structure Example

```python
import weakref

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self._parent_ref = None
    
    def add_child(self, child):
        self.children.append(child)
        child._parent_ref = weakref.ref(self)
    
    @property
    def parent(self):
        if self._parent_ref is None:
            return None
        return self._parent_ref()
    
    def path_to_root(self):
        path = [self.value]
        node = self.parent
        while node is not None:
            path.append(node.value)
            node = node.parent
        return path[::-1]

# Usage
root = TreeNode("root")
child = TreeNode("child")
grandchild = TreeNode("grandchild")

root.add_child(child)
child.add_child(grandchild)

print(grandchild.path_to_root())  # ['root', 'child', 'grandchild']
```

---

## Summary

| Pattern | Weak Reference Type | Use Case |
|---------|---------------------|----------|
| Observer | `WeakSet` | Allow observers to be GC'd without explicit unsubscribe |
| Cache | `WeakValueDictionary` | Auto-evict cached objects when no longer used |
| Parent-Child | `weakref.ref()` | Break cycles in bidirectional relationships |

**Key Principle**: Use strong references for ownership (parent → child), weak references for back-references or non-owning relationships (child → parent, cache → cached object, observable → observer).
