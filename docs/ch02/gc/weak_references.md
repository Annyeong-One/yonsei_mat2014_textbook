# Weak References

강한 참조와 달리 가비지 컬렉션을 방해하지 않는 참조입니다.

## Strong vs Weak References

### Strong References (Normal)

```python
x = [1, 2, 3]
y = x
# Strong refs prevent GC
# refcount = 2
```

### Weak References

```python
import weakref

obj = [1, 2, 3]
weak = weakref.ref(obj)

print(weak())  # [1, 2, 3]

del obj
print(weak())  # None (collected)
```

| Type | Prevents GC | Use Case |
|------|-------------|----------|
| Strong | Yes | Ownership |
| Weak | No | Caching, back-references |

---

## Weak Reference Types

### 1. weakref.ref()

```python
import weakref

obj = [1, 2, 3]
ref = weakref.ref(obj)

# Access (always check for None)
if ref() is not None:
    print(ref())
```

### 2. WeakValueDictionary

```python
import weakref

cache = weakref.WeakValueDictionary()
obj = [1, 2, 3]
cache['key'] = obj

del obj
# cache['key'] automatically removed
```

### 3. WeakKeyDictionary

```python
import weakref

data = weakref.WeakKeyDictionary()
key_obj = SomeClass()
data[key_obj] = "value"

del key_obj
# Entry automatically removed
```

### 4. WeakSet

```python
import weakref

objects = weakref.WeakSet()
obj = [1, 2, 3]
objects.add(obj)

del obj
# obj removed from set automatically
```

---

## Callbacks

객체가 수집될 때 콜백을 실행할 수 있습니다.

```python
import weakref

def callback(ref):
    print("Object collected")

obj = [1, 2, 3]
ref = weakref.ref(obj, callback)

del obj  # Prints: Object collected
```

---

## Breaking Reference Cycles

순환 참조를 방지하는 방법입니다.

### Manual Breaking

```python
class Node:
    def __init__(self):
        self.next = None

# Create cycle
a = Node()
b = Node()
a.next = b
b.next = a

# Break cycle before cleanup
a.next = None
```

### Context Managers

```python
class Resource:
    def __init__(self):
        self.ref = None
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.ref = None  # Break reference

with Resource() as r:
    # use r
    pass
# ref cleared automatically
```

### Weak Back-References

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
        return self._parent_ref()

# No cycle: parent → child → weak_ref
```

---

## When to Use Weak References

### ✅ Use For

| Use Case | Type | Reason |
|----------|------|--------|
| Caches | `WeakValueDictionary` | Auto-evict when unused |
| Observers | `WeakSet` | Auto-unsubscribe |
| Back-references | `weakref.ref()` | Break cycles |
| Callbacks | `weakref.ref(obj, fn)` | Cleanup notification |

### ❌ Don't Use For

- Data that must be accessible (use strong refs)
- Simple, non-cyclic structures
- Immutable types (int, str can't be weakref'd)

---

## Limitations

### Not All Types Support Weak References

```python
import weakref

# TypeError: cannot create weak reference
# x = 42
# ref = weakref.ref(x)

# These work
obj = [1, 2, 3]
ref = weakref.ref(obj)  # ✓

class MyClass:
    pass
ref = weakref.ref(MyClass())  # ✓
```

Types that **cannot** be weakref'd:
- `int`, `str`, `tuple`, `frozenset`
- Most built-in immutable types

---

## Summary

| Feature | Description |
|---------|-------------|
| Purpose | Reference without preventing GC |
| Main Types | `ref()`, `WeakValueDictionary`, `WeakSet` |
| Use Cases | Caching, observers, back-references |
| Callbacks | Available via `weakref.ref(obj, callback)` |
| Limitation | Not all types supported |
