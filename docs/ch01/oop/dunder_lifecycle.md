# Object Lifecycle

Object lifecycle methods control creation, initialization, and destruction of Python objects.

---

## Object Creation: `__new__`

### 1. Memory Allocation

```python
class MyInt(int):
    def __new__(cls, value):
        print("Creating instance...")
        return super().__new__(cls, value)

x = MyInt(5)
print(x)  # 5
```

`__new__` allocates memory and returns the object.

### 2. Class Method Nature

```python
def __new__(cls, *args, **kwargs):
    instance = super().__new__(cls)
    return instance
```

Receives `cls` as first parameter, not `self`.

### 3. No Decorator Needed

`__new__` doesn't need `@classmethod` decorator—Python handles it specially.

---

## Why No `@classmethod`

### 1. Special Interpreter Handling

```python
class MyClass:
    def __new__(cls, *args):
        print(f"__new__ called with cls = {cls}")
        return super().__new__(cls)
    
    def __init__(self, *args):
        print(f"__init__ called with self = {self}")
```

Python's interpreter automatically passes `cls`.

### 2. Called by Interpreter

```python
# Internally Python does:
instance = MyClass.__new__(MyClass, ...)
```

Direct interpreter invocation, not decorator machinery.

### 3. Comparison Table

| Aspect | `__new__` | `@classmethod` |
|--------|-----------|----------------|
| First arg `cls` | ✅ | ✅ |
| Needs decorator | ❌ | ✅ |
| Called by | Interpreter | Developer |
| Purpose | Object creation | Class utilities |

---

## Object Initialization

### 1. `__init__` Method

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
```

Called after `__new__` to set up instance state.

### 2. Mutates Instance

```python
def __init__(self, name, age):
    self.name = name  # sets attributes
    self.age = age
```

Modifies the object created by `__new__`.

### 3. Returns None

```python
def __init__(self, value):
    self.value = value
    # Must return None (implicit)
```

---

## Creation vs Initialization

### 1. Two-Step Process

```python
# Step 1: __new__ creates
instance = MyClass.__new__(MyClass, args)

# Step 2: __init__ initializes
MyClass.__init__(instance, args)
```

### 2. When to Use `__new__`

- Subclassing immutable types (`int`, `str`, `tuple`)
- Singleton pattern
- Custom memory allocation
- Metaclass programming

### 3. When to Use `__init__`

- Regular classes (99% of cases)
- Setting instance attributes
- Standard object setup

---

## Immutable Type Example

### 1. Subclassing `int`

```python
class PositiveInt(int):
    def __new__(cls, value):
        if value < 0:
            raise ValueError("Must be positive")
        return super().__new__(cls, value)

x = PositiveInt(5)   # OK
y = PositiveInt(-5)  # ValueError
```

### 2. Why `__new__` Needed

```python
# Can't use __init__ because int is immutable
class BadInt(int):
    def __init__(self, value):
        # Too late! Object already created
        if value < 0:
            raise ValueError("Must be positive")
```

### 3. Immutable Types

`int`, `float`, `str`, `tuple`, `frozenset` require `__new__`.

---

## Singleton Pattern

### 1. Using `__new__`

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

### 2. Single Instance

Only one object ever created.

### 3. Thread Safety

```python
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

---

## Object Destruction

### 1. `__del__` Method

```python
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"{name} created")
    
    def __del__(self):
        print(f"{self.name} destroyed")

r = Resource("MyResource")
del r  # Triggers __del__
```

### 2. Garbage Collection

```python
obj = Resource("Test")
obj = None  # Old object becomes garbage
# __del__ called when garbage collected
```

### 3. Non-Deterministic

```python
# Timing is unpredictable
def create():
    obj = Resource("Temp")
    # When is __del__ called? Unknown!
```

---

## `__del__` Pitfalls

### 1. Reference Cycles

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __del__(self):
        print(f"Deleting {self.value}")

a = Node(1)
b = Node(2)
a.next = b
b.next = a  # Cycle!
# __del__ may never run
```

### 2. Exception Swallowing

```python
class Bad:
    def __del__(self):
        raise Exception("Error!")
        # Exception is printed but swallowed
```

### 3. Limited Use

Use `__del__` only for logging/debugging, not cleanup.

---

## Better Alternatives

### 1. Context Managers

```python
class FileResource:
    def __enter__(self):
        self.file = open("data.txt")
        return self.file
    
    def __exit__(self, *args):
        self.file.close()

with FileResource() as f:
    f.write("data")
# Guaranteed cleanup
```

### 2. Explicit Methods

```python
class Connection:
    def close(self):
        # Explicit cleanup
        pass

conn = Connection()
try:
    # Use connection
    pass
finally:
    conn.close()
```

### 3. Weakref Callbacks

```python
import weakref

def cleanup(ref):
    print("Object deleted")

obj = SomeClass()
weakref.ref(obj, cleanup)
```

---

## Complete Lifecycle

### 1. Full Example

```python
class LifeCycle:
    def __new__(cls, name):
        print(f"1. __new__ called")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        print(f"2. __init__ called")
        self.name = name
    
    def __del__(self):
        print(f"3. __del__ called for {self.name}")

obj = LifeCycle("Test")
del obj
```

### 2. Output Order

```
1. __new__ called
2. __init__ called
3. __del__ called for Test
```

### 3. Typical Flow

`__new__` → `__init__` → ... → `__del__`

---

## Summary Table

### 1. Lifecycle Methods

| Stage | Method | Purpose |
|-------|--------|---------|
| Creation | `__new__` | Allocate memory |
| Initialization | `__init__` | Set attributes |
| Destruction | `__del__` | Cleanup (avoid) |

### 2. When to Override

| Method | When |
|--------|------|
| `__new__` | Immutable types, singletons |
| `__init__` | Always (standard setup) |
| `__del__` | Rarely (debugging only) |

### 3. Best Practices

- Use `__init__` for normal classes
- Use `__new__` for immutables/singletons
- Avoid `__del__` for cleanup
- Use context managers instead

---

## Key Takeaways

- `__new__` creates, `__init__` initializes.
- `__new__` doesn't need `@classmethod`.
- Use `__new__` for immutable types.
- `__del__` is unreliable—use context managers.
- Lifecycle: creation → initialization → destruction.
