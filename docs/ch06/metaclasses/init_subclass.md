# \_\_init_subclass\_\_


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

`__init_subclass__` (Python 3.6+) is a hook that's called whenever a class is subclassed. It provides a simpler alternative to metaclasses for many common use cases.

```python
class Base:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Called when any class inherits from Base
```

---

## Basic Usage

```python
class Plugin:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"New plugin registered: {cls.__name__}")

class AudioPlugin(Plugin):
    pass
# Output: New plugin registered: AudioPlugin

class VideoPlugin(Plugin):
    pass
# Output: New plugin registered: VideoPlugin
```

---

## How It Works

When you define a subclass:

```python
class Child(Parent):
    pass
```

Python automatically calls:

```python
Parent.__init_subclass__(Child)
```

The hook receives:
- `cls`: The newly created subclass (not the parent)
- `**kwargs`: Any keyword arguments from the class definition

---

## Passing Arguments

You can pass arguments in the class definition:

```python
class Serializable:
    def __init_subclass__(cls, format="json", **kwargs):
        super().__init_subclass__(**kwargs)
        cls._format = format
        print(f"{cls.__name__} uses {format} format")

class User(Serializable, format="xml"):
    pass
# Output: User uses xml format

class Product(Serializable):  # Uses default
    pass
# Output: Product uses json format

print(User._format)     # xml
print(Product._format)  # json
```

---

## Practical Examples

### Plugin Registration

```python
class Plugin:
    _registry = {}
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Register plugin by name
        Plugin._registry[cls.__name__] = cls
    
    @classmethod
    def get_plugin(cls, name):
        return cls._registry.get(name)

class ImageProcessor(Plugin):
    def process(self, data):
        return f"Processing image: {data}"

class TextProcessor(Plugin):
    def process(self, data):
        return f"Processing text: {data}"

# Access registered plugins
print(Plugin._registry)
# {'ImageProcessor': <class 'ImageProcessor'>, 'TextProcessor': <class 'TextProcessor'>}

processor = Plugin.get_plugin("ImageProcessor")()
print(processor.process("photo.jpg"))
```

### Validation

```python
class ValidatedModel:
    required_fields = []
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        
        # Check that required fields are defined
        for field in cls.required_fields:
            if not hasattr(cls, field):
                raise TypeError(
                    f"{cls.__name__} must define '{field}'"
                )

class UserModel(ValidatedModel):
    required_fields = ['name', 'email']
    name = str
    email = str
    # ✓ Valid - has both required fields

# class InvalidModel(ValidatedModel):
#     required_fields = ['name', 'email']
#     name = str
#     # TypeError: InvalidModel must define 'email'
```

### Automatic Method Addition

```python
class AutoRepr:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        
        # Add __repr__ based on __init__ parameters
        if hasattr(cls, '__init__'):
            import inspect
            sig = inspect.signature(cls.__init__)
            params = [p for p in sig.parameters if p != 'self']
            
            def __repr__(self):
                values = ', '.join(
                    f"{p}={getattr(self, p)!r}" 
                    for p in params 
                    if hasattr(self, p)
                )
                return f"{self.__class__.__name__}({values})"
            
            cls.__repr__ = __repr__

class Person(AutoRepr):
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p)  # Person(name='Alice', age=30)
```

### Configuration Inheritance

```python
class Configurable:
    _config = {}
    
    def __init_subclass__(cls, **config):
        super().__init_subclass__()
        # Inherit parent config and update with new values
        cls._config = {**cls._config, **config}

class BaseService(Configurable, timeout=30, retries=3):
    pass

class DatabaseService(BaseService, timeout=60):
    pass

class CacheService(BaseService, retries=5):
    pass

print(BaseService._config)     # {'timeout': 30, 'retries': 3}
print(DatabaseService._config) # {'timeout': 60, 'retries': 3}
print(CacheService._config)    # {'timeout': 30, 'retries': 5}
```

### Enforcing Abstract Methods

```python
class Interface:
    _required_methods = []
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        
        # Skip abstract classes
        if getattr(cls, '_abstract', False):
            return
        
        # Check all required methods are implemented
        missing = []
        for method in cls._required_methods:
            if not callable(getattr(cls, method, None)):
                missing.append(method)
        
        if missing:
            raise TypeError(
                f"{cls.__name__} must implement: {', '.join(missing)}"
            )

class Repository(Interface):
    _abstract = True
    _required_methods = ['get', 'save', 'delete']

class UserRepository(Repository):
    def get(self, id):
        return {"id": id}
    
    def save(self, entity):
        pass
    
    def delete(self, id):
        pass
# ✓ Valid

# class BadRepository(Repository):
#     def get(self, id):
#         return {"id": id}
# TypeError: BadRepository must implement: save, delete
```

---

## With Multiple Inheritance

```python
class A:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"A.__init_subclass__ for {cls.__name__}")

class B:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"B.__init_subclass__ for {cls.__name__}")

class C(A, B):
    pass
# Output:
# B.__init_subclass__ for C
# A.__init_subclass__ for C
```

**Important**: Always call `super().__init_subclass__(**kwargs)` to support multiple inheritance!

---

## __init_subclass__ vs Metaclass

| Feature | `__init_subclass__` | Metaclass |
|---------|---------------------|-----------|
| Complexity | Simple | Complex |
| Called when | Class is subclassed | Class is created |
| Access to | Subclass only | Full creation process |
| Modify namespace | No | Yes (via `__prepare__`) |
| Control instantiation | No | Yes (via `__call__`) |
| Use case | Registration, validation | DSLs, ORMs |

### When to Use __init_subclass__

- Registering subclasses
- Validating class definitions
- Adding methods or attributes
- Simple class customization

### When to Use Metaclass

- Modifying class before creation
- Controlling instance creation
- Custom namespace handling
- Complex framework behavior

---

## Common Patterns

### Optional Hook

```python
class OptionalHook:
    def __init_subclass__(cls, register=True, **kwargs):
        super().__init_subclass__(**kwargs)
        if register:
            cls._registered = True
        else:
            cls._registered = False

class Registered(OptionalHook):
    pass

class NotRegistered(OptionalHook, register=False):
    pass

print(Registered._registered)     # True
print(NotRegistered._registered)  # False
```

### Chained Hooks

```python
class Logger:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"[LOG] Created: {cls.__name__}")

class Validator:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"[VALIDATE] Checking: {cls.__name__}")

class MyClass(Logger, Validator):
    pass
# [VALIDATE] Checking: MyClass
# [LOG] Created: MyClass
```

---

## Summary

| Feature | Example |
|---------|---------|
| Basic hook | `def __init_subclass__(cls, **kwargs):` |
| With arguments | `class Child(Parent, arg=value):` |
| Always call super | `super().__init_subclass__(**kwargs)` |
| Access subclass | `cls` parameter |

**Key Takeaways**:

- `__init_subclass__` is called when a class is subclassed
- Simpler alternative to metaclasses for many use cases
- Always call `super().__init_subclass__(**kwargs)`
- Can receive keyword arguments from class definition
- Use for registration, validation, and automatic setup
- Prefer over metaclasses unless you need `__prepare__` or `__call__`
