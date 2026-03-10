# Object Lifecycle


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Lifecycle dunder methods control how objects are created, initialized, and destroyed.

## Overview: Object Creation Flow

```
MyClass(args)
    ↓
MyClass.__new__(cls, args)   → Creates instance
    ↓
MyClass.__init__(self, args) → Initializes instance
    ↓
(object used)
    ↓
MyClass.__del__(self)        → Called before destruction (unreliable)
```

## `__new__`: Object Creation

`__new__` is a static method that creates and returns a new instance.

### Basic __new__

```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        print(f"Creating instance of {cls.__name__}")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, value):
        print(f"Initializing with value={value}")
        self.value = value

obj = MyClass(42)
# Output:
# Creating instance of MyClass
# Initializing with value=42
```

### When to Use __new__

`__new__` is rarely needed, but useful for:

1. **Subclassing immutable types** (str, int, tuple)
2. **Implementing singletons**
3. **Object caching/flyweight pattern**
4. **Custom metaclasses**

## Subclassing Immutable Types

Immutable types must be modified in `__new__` because `__init__` is too late.

```python
class UpperStr(str):
    """String that's always uppercase."""
    
    def __new__(cls, value):
        # Must modify in __new__ - str is immutable
        instance = super().__new__(cls, value.upper())
        return instance

s = UpperStr("hello")
print(s)         # HELLO
print(type(s))   # <class '__main__.UpperStr'>
```

```python
class EvenInt(int):
    """Integer that rounds to nearest even number."""
    
    def __new__(cls, value):
        # Round to nearest even
        rounded = round(value / 2) * 2
        return super().__new__(cls, rounded)

print(EvenInt(3))   # 4
print(EvenInt(4))   # 4
print(EvenInt(5))   # 6
```

```python
class NamedTuple(tuple):
    """Simple named tuple implementation."""
    
    def __new__(cls, name, values):
        instance = super().__new__(cls, values)
        instance.name = name  # Can add attributes after creation
        return instance

point = NamedTuple("origin", (0, 0))
print(point)        # (0, 0)
print(point.name)   # origin
```

## Singleton Pattern

Ensure only one instance of a class exists.

```python
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value=None):
        # Note: __init__ runs every time!
        if value is not None:
            self.value = value

a = Singleton(1)
b = Singleton(2)

print(a is b)      # True
print(a.value)     # 2 (overwritten by second __init__)
print(id(a), id(b))  # Same id
```

### Singleton with Init Guard

```python
class BetterSingleton:
    _instance = None
    _initialized = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value):
        if not BetterSingleton._initialized:
            self.value = value
            BetterSingleton._initialized = True

a = BetterSingleton(1)
b = BetterSingleton(2)

print(a.value)  # 1 (preserved)
print(b.value)  # 1 (same object)
```

## Object Caching / Flyweight Pattern

Reuse existing objects for identical values.

```python
class CachedInt:
    _cache = {}
    
    def __new__(cls, value):
        if value in cls._cache:
            return cls._cache[value]
        
        instance = super().__new__(cls)
        instance.value = value
        cls._cache[value] = instance
        return instance
    
    def __init__(self, value):
        pass  # Already initialized in __new__
    
    def __repr__(self):
        return f"CachedInt({self.value})"

a = CachedInt(5)
b = CachedInt(5)
c = CachedInt(10)

print(a is b)  # True (same cached object)
print(a is c)  # False (different value)
```

### LRU Cache for Limited Memory

```python
from collections import OrderedDict

class LRUCachedObject:
    _cache = OrderedDict()
    _max_size = 100
    
    def __new__(cls, key):
        if key in cls._cache:
            # Move to end (most recently used)
            cls._cache.move_to_end(key)
            return cls._cache[key]
        
        instance = super().__new__(cls)
        instance.key = key
        
        cls._cache[key] = instance
        if len(cls._cache) > cls._max_size:
            cls._cache.popitem(last=False)  # Remove oldest
        
        return instance
```

## `__init__`: Object Initialization

`__init__` initializes an already-created instance.

### Basic __init__

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._validate()
    
    def _validate(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

p = Person("Alice", 30)
print(p.name)  # Alice
```

### __init__ Must Return None

```python
class Wrong:
    def __init__(self, value):
        self.value = value
        return self  # TypeError!

# TypeError: __init__() should return None, not 'Wrong'
```

### Flexible Initialization

```python
class Connection:
    def __init__(self, host=None, port=None, *, url=None):
        if url:
            # Parse URL
            self.host, self.port = self._parse_url(url)
        else:
            self.host = host or 'localhost'
            self.port = port or 8080
    
    def _parse_url(self, url):
        # Simplified parsing
        parts = url.replace('://', ':').split(':')
        return parts[1], int(parts[2])
    
    def __repr__(self):
        return f"Connection({self.host}:{self.port})"

# Multiple initialization patterns
c1 = Connection('example.com', 443)
c2 = Connection(url='https://api.example.com:8443')
c3 = Connection()  # defaults

print(c1)  # Connection(example.com:443)
print(c2)  # Connection(api.example.com:8443)
print(c3)  # Connection(localhost:8080)
```

## `__del__`: Object Destruction

`__del__` is called when an object is about to be destroyed.

### Basic __del__

```python
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"Acquiring {name}")
    
    def __del__(self):
        print(f"Releasing {self.name}")

r = Resource("database connection")
# Acquiring database connection
del r
# Releasing database connection
```

### Why __del__ is Unreliable

```python
# Problem 1: Timing is unpredictable
class Unreliable:
    def __del__(self):
        print("Destructor called")

obj = Unreliable()
obj = None  # May or may not trigger __del__ immediately

# Problem 2: Circular references may prevent __del__
class Node:
    def __init__(self):
        self.ref = None
    
    def __del__(self):
        print("Node destroyed")

a = Node()
b = Node()
a.ref = b
b.ref = a  # Circular reference
del a, b   # __del__ may never be called!

# Problem 3: Exceptions in __del__ are ignored
class BadDestructor:
    def __del__(self):
        raise RuntimeError("Oops!")  # Silently ignored

obj = BadDestructor()
del obj  # No exception raised, just a warning
```

### Better Alternative: Context Managers

```python
class Resource:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print(f"Acquiring {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Releasing {self.name}")
        return False
    
    def use(self):
        print(f"Using {self.name}")

# Guaranteed cleanup with context manager
with Resource("database") as r:
    r.use()
# Releasing happens even if exception occurs
```

## Complete Lifecycle Example

```python
class TrackedObject:
    _count = 0
    
    def __new__(cls, name):
        print(f"1. __new__: Creating instance of {cls.__name__}")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        print(f"2. __init__: Initializing with name={name}")
        self.name = name
        TrackedObject._count += 1
        self.id = TrackedObject._count
    
    def __repr__(self):
        return f"TrackedObject(name={self.name!r}, id={self.id})"
    
    def __del__(self):
        print(f"3. __del__: Destroying {self.name} (id={self.id})")

print("Creating object:")
obj = TrackedObject("test")
print(f"Object: {obj}")
print("\nDeleting object:")
del obj
print("Done")

# Output:
# Creating object:
# 1. __new__: Creating instance of TrackedObject
# 2. __init__: Initializing with name=test
# Object: TrackedObject(name='test', id=1)
#
# Deleting object:
# 3. __del__: Destroying test (id=1)
# Done
```

## Factory Methods Using __new__

```python
class Shape:
    def __new__(cls, shape_type, *args):
        if cls is not Shape:
            # Called on subclass, proceed normally
            return super().__new__(cls)
        
        # Factory: create appropriate subclass
        if shape_type == 'circle':
            return Circle.__new__(Circle)
        elif shape_type == 'square':
            return Square.__new__(Square)
        else:
            raise ValueError(f"Unknown shape: {shape_type}")

class Circle(Shape):
    def __init__(self, shape_type, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Square(Shape):
    def __init__(self, shape_type, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

# Factory usage
c = Shape('circle', 5)
s = Shape('square', 4)
print(type(c))    # <class '__main__.Circle'>
print(c.area())   # 78.53975
print(type(s))    # <class '__main__.Square'>
print(s.area())   # 16
```

## __init_subclass__: Customizing Subclass Creation

Python 3.6+ provides `__init_subclass__` for customizing subclass behavior.

```python
class Plugin:
    _registry = {}
    
    def __init_subclass__(cls, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        plugin_name = name or cls.__name__.lower()
        Plugin._registry[plugin_name] = cls
        print(f"Registered plugin: {plugin_name}")
    
    @classmethod
    def get_plugin(cls, name):
        return cls._registry.get(name)

class AudioPlugin(Plugin, name='audio'):
    pass

class VideoPlugin(Plugin):  # Uses class name
    pass

# Output:
# Registered plugin: audio
# Registered plugin: videoplugin

print(Plugin._registry)
# {'audio': <class 'AudioPlugin'>, 'videoplugin': <class 'VideoPlugin'>}
```

## Key Takeaways

- `__new__` creates instances; use for immutables, singletons, caching
- `__init__` initializes instances; most common place for setup
- `__del__` is unreliable; prefer context managers for cleanup
- `__new__` receives class, `__init__` receives instance
- `__new__` must return an instance; `__init__` must return `None`
- For reliable cleanup, use `with` statements and `__enter__`/`__exit__`
- Use `__init_subclass__` to customize subclass creation (Python 3.6+)
