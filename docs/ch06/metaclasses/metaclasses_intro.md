# Metaclasses Introduction

A metaclass is a class whose instances are classes. Just as a class defines how instances behave, a metaclass defines how classes behave.

---

## Understanding the Concept

### Everything is an Object

In Python, **classes are objects too**:

```python
class MyClass:
    pass

# MyClass is an object
print(type(MyClass))  # <class 'type'>

# Just like instances are objects
obj = MyClass()
print(type(obj))      # <class '__main__.MyClass'>
```

### The type() Function

`type` has two uses:

```python
# 1. Get the type of an object
print(type(42))        # <class 'int'>
print(type("hello"))   # <class 'str'>
print(type([1, 2]))    # <class 'list'>

# 2. Create a new class dynamically
MyClass = type('MyClass', (), {'x': 10})
print(MyClass.x)       # 10
```

### type is the Default Metaclass

```python
class MyClass:
    pass

# These are equivalent:
# 1. Using class statement
class MyClass:
    x = 10

# 2. Using type() directly
MyClass = type('MyClass', (), {'x': 10})
```

---

## The Class Creation Process

When Python sees a class definition:

```python
class MyClass(BaseClass):
    x = 10
    def method(self):
        pass
```

It executes roughly:

```python
# 1. Collect class body into a namespace dict
namespace = {'x': 10, 'method': method_function}

# 2. Determine metaclass (default: type)
metaclass = type

# 3. Call metaclass to create class
MyClass = metaclass('MyClass', (BaseClass,), namespace)
```

---

## Creating a Metaclass

### Basic Metaclass

```python
class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Creating class: {name}")
        # Create the class using type.__new__
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

class MyClass(metaclass=MyMeta):
    pass
# Output: Creating class: MyClass
```

### __new__ vs __init__ in Metaclass

```python
class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        """Called to CREATE the class object."""
        print(f"__new__: Creating {name}")
        return super().__new__(mcs, name, bases, namespace)
    
    def __init__(cls, name, bases, namespace):
        """Called to INITIALIZE the class object."""
        print(f"__init__: Initializing {name}")
        super().__init__(name, bases, namespace)

class MyClass(metaclass=MyMeta):
    pass
# __new__: Creating MyClass
# __init__: Initializing MyClass
```

### __call__ in Metaclass

Controls instance creation:

```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        """Called when MyClass() is invoked."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass

a = Singleton()
b = Singleton()
print(a is b)  # True
```

---

## Practical Examples

### Automatic Registration

```python
class PluginMeta(type):
    plugins = {}
    
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        # Don't register the base class itself
        if bases:  # Has parent classes
            mcs.plugins[name] = cls
        return cls

class Plugin(metaclass=PluginMeta):
    """Base class for plugins."""
    pass

class AudioPlugin(Plugin):
    pass

class VideoPlugin(Plugin):
    pass

print(PluginMeta.plugins)
# {'AudioPlugin': <class 'AudioPlugin'>, 'VideoPlugin': <class 'VideoPlugin'>}
```

### Attribute Validation

```python
class ValidatedMeta(type):
    def __new__(mcs, name, bases, namespace):
        # Check that required attributes exist
        if bases:  # Not the base class
            if 'required_field' not in namespace:
                raise TypeError(f"{name} must define 'required_field'")
        return super().__new__(mcs, name, bases, namespace)

class Base(metaclass=ValidatedMeta):
    pass

class Valid(Base):
    required_field = "I exist"

# class Invalid(Base):  # TypeError: Invalid must define 'required_field'
#     pass
```

### Method Wrapping

```python
import functools

class LoggedMeta(type):
    def __new__(mcs, name, bases, namespace):
        # Wrap all methods with logging
        for key, value in namespace.items():
            if callable(value) and not key.startswith('_'):
                namespace[key] = mcs.log_call(value)
        return super().__new__(mcs, name, bases, namespace)
    
    @staticmethod
    def log_call(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

class MyClass(metaclass=LoggedMeta):
    def method1(self):
        return "result1"
    
    def method2(self, x):
        return x * 2

obj = MyClass()
obj.method1()  # Calling method1
obj.method2(5) # Calling method2
```

### Interface Enforcement

```python
class InterfaceMeta(type):
    required_methods = []
    
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        
        # Skip check for base class
        if bases and mcs.required_methods:
            for method in mcs.required_methods:
                if method not in namespace:
                    raise TypeError(
                        f"{name} must implement {method}()"
                    )
        return cls

class ServiceMeta(InterfaceMeta):
    required_methods = ['start', 'stop', 'status']

class Service(metaclass=ServiceMeta):
    """Base service class."""
    def start(self): pass
    def stop(self): pass
    def status(self): pass

class DatabaseService(Service):
    def start(self):
        print("DB starting")
    
    def stop(self):
        print("DB stopping")
    
    def status(self):
        return "running"
```

---

## Metaclass vs Alternatives

### When NOT to Use Metaclasses

Most use cases have simpler alternatives:

| Need | Alternative |
|------|-------------|
| Modify class creation | `__init_subclass__` |
| Add methods | Class decorators |
| Validate attributes | Descriptors |
| Singleton pattern | Module-level instance |
| Registration | Class decorators |

### __init_subclass__ (Python 3.6+)

Simpler alternative for many cases:

```python
class Plugin:
    plugins = {}
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.plugins[cls.__name__] = cls

class AudioPlugin(Plugin):
    pass

class VideoPlugin(Plugin):
    pass

print(Plugin.plugins)
# {'AudioPlugin': <class 'AudioPlugin'>, 'VideoPlugin': <class 'VideoPlugin'>}
```

### Class Decorators

```python
def register(cls):
    registry[cls.__name__] = cls
    return cls

def add_method(cls):
    cls.new_method = lambda self: "added"
    return cls

@register
@add_method
class MyClass:
    pass
```

---

## Advanced: __prepare__

Control the namespace dict used during class creation:

```python
from collections import OrderedDict

class OrderedMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases):
        # Return custom namespace (must be dict-like)
        return OrderedDict()
    
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, dict(namespace))
        cls._field_order = list(namespace.keys())
        return cls

class Record(metaclass=OrderedMeta):
    first = 1
    second = 2
    third = 3

print(Record._field_order)
# ['__module__', '__qualname__', 'first', 'second', 'third']
```

---

## When to Use Metaclasses

**Use metaclasses when you need to:**

- Modify class creation before the class exists
- Automatically register all subclasses
- Enforce class-level invariants
- Create DSLs (Domain Specific Languages)
- Build frameworks (ORMs, serializers)

**Famous examples:**

- Django models (`ModelBase`)
- SQLAlchemy ORM (`DeclarativeMeta`)
- ABC module (`ABCMeta`)
- Enum (`EnumMeta`)

---

## Summary

```python
# Class hierarchy
object  # Base of all objects
   ↑
 type   # Metaclass - creates classes (type is its own metaclass)
   ↑
MyMeta  # Custom metaclass
   ↓
MyClass # Regular class (instance of MyMeta)
   ↓
  obj   # Instance of MyClass
```

| Hook | Called When | Use For |
|------|-------------|---------|
| `__new__` | Creating class | Modify namespace, validate |
| `__init__` | Initializing class | Post-creation setup |
| `__call__` | Creating instance | Singleton, pooling |
| `__prepare__` | Before body execution | Custom namespace |

**Key Takeaways**:

- Classes are instances of metaclasses
- `type` is the default metaclass for all classes
- Metaclasses control class creation and behavior
- Use `__init_subclass__` or decorators when possible
- Reserve metaclasses for framework-level code
- "If you wonder whether you need metaclasses, you don't" — Tim Peters
