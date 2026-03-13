# __setattr__

## Fundamentals

### 1. Definition

The `__setattr__` method is called **whenever you assign to an attribute** on an object:

```python
obj.attr = value  # Triggers obj.__setattr__('attr', value)
setattr(obj, 'attr', value)  # Also triggers __setattr__
```

### 2. Method Signature

```python
def __setattr__(self, name, value):
    # name: attribute name (string)
    # value: value being assigned
    pass
```

### 3. Universal Assignment Hook

Every attribute assignment goes through `__setattr__`:

```python
self.x = 10       # Calls __setattr__('x', 10)
self.name = "hi"  # Calls __setattr__('name', "hi")
self.data = []    # Calls __setattr__('data', [])
```

## Basic Implementation

### 1. Simple Override

```python
class MyClass:
    def __setattr__(self, name, value):
        print(f"Setting {name} = {value}")
        super().__setattr__(name, value)

obj = MyClass()
obj.x = 42
# Output: Setting x = 42

obj.name = "Alice"
# Output: Setting name = Alice
```

### 2. Without super()

```python
class MyClass:
    def __setattr__(self, name, value):
        print(f"Setting {name} = {value}")
        object.__setattr__(self, name, value)
```

### 3. Must Actually Store

```python
# ❌ BAD - doesn't actually store anything
def __setattr__(self, name, value):
    print(f"Setting {name}")
    # Forgot to actually set it!

# ✅ GOOD
def __setattr__(self, name, value):
    print(f"Setting {name}")
    super().__setattr__(name, value)
```

## Avoiding Recursion

### 1. The Problem

```python
class Broken:
    def __setattr__(self, name, value):
        # ❌ INFINITE RECURSION!
        self.name = value  # Calls __setattr__ again!
```

### 2. Correct Approaches

**Use `super()`:**
```python
class Correct:
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
```

**Use `object.__setattr__`:**
```python
class Correct:
    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
```

**Direct `__dict__` access:**
```python
class Correct:
    def __setattr__(self, name, value):
        self.__dict__[name] = value
```

### 3. In `__init__`

Be careful in constructors:

```python
class Example:
    def __init__(self, value):
        self.value = value  # ✅ Calls __setattr__
    
    def __setattr__(self, name, value):
        print(f"Setting {name}")
        super().__setattr__(name, value)

obj = Example(42)
# Output: Setting value
```

## Practical Examples

### 1. Validation

```python
class Person:
    def __setattr__(self, name, value):
        if name == 'age':
            if not isinstance(value, int):
                raise TypeError("Age must be integer")
            if value < 0 or value > 150:
                raise ValueError("Invalid age range")
        elif name == 'name':
            if not isinstance(value, str):
                raise TypeError("Name must be string")
            if not value.strip():
                raise ValueError("Name cannot be empty")
        
        super().__setattr__(name, value)

person = Person()
person.name = "Alice"  # ✅ OK
person.age = 30        # ✅ OK
# person.age = -5      # ❌ ValueError
# person.name = ""     # ❌ ValueError
```

### 2. Type Coercion

```python
class TypedAttributes:
    def __setattr__(self, name, value):
        if name == 'count':
            value = int(value)  # Convert to int
        elif name == 'price':
            value = float(value)  # Convert to float
        elif name == 'name':
            value = str(value).strip()  # Convert to string
        
        super().__setattr__(name, value)

obj = TypedAttributes()
obj.count = "42"      # Stored as int(42)
obj.price = "19.99"   # Stored as float(19.99)
obj.name = "  hi  "   # Stored as "hi"
```

### 3. Change Tracking

```python
class TrackedObject:
    def __init__(self):
        super().__setattr__('_changes', {})
    
    def __setattr__(self, name, value):
        if name != '_changes':
            # Track old value
            if hasattr(self, name):
                old_value = super().__getattribute__(name)
            else:
                old_value = None
            
            # Record change
            changes = super().__getattribute__('_changes')
            changes[name] = (old_value, value)
        
        super().__setattr__(name, value)

obj = TrackedObject()
obj.x = 10
obj.x = 20
obj.y = 30
print(obj._changes)
# {'x': (None, 10), 'x': (10, 20), 'y': (None, 30)}
```

## Read-Only Attributes

### 1. Protecting Attributes

```python
class ReadOnlyAttrs:
    def __init__(self):
        super().__setattr__('_locked', False)
        self.value = 42
        super().__setattr__('_locked', True)
    
    def __setattr__(self, name, value):
        if super().__getattribute__('_locked'):
            raise AttributeError("Attributes are read-only")
        super().__setattr__(name, value)

obj = ReadOnlyAttrs()
print(obj.value)      # 42
# obj.value = 100     # ❌ AttributeError
# obj.new_attr = 5    # ❌ AttributeError
```

### 2. Protecting Specific Attributes

```python
class ProtectedID:
    def __init__(self, id_value):
        self._id = id_value
        self.name = ""
    
    def __setattr__(self, name, value):
        if name == '_id' and hasattr(self, '_id'):
            raise AttributeError("Cannot modify ID after initialization")
        super().__setattr__(name, value)

obj = ProtectedID(123)
obj.name = "Alice"   # ✅ OK
# obj._id = 456      # ❌ AttributeError
```

### 3. Conditional Write Protection

```python
class Document:
    def __init__(self):
        self._finalized = False
        self.content = ""
    
    def finalize(self):
        self._finalized = True
    
    def __setattr__(self, name, value):
        if name != '_finalized':
            if hasattr(self, '_finalized') and self._finalized:
                raise AttributeError("Document is finalized")
        super().__setattr__(name, value)

doc = Document()
doc.content = "Draft"  # ✅ OK
doc.finalize()
# doc.content = "New"  # ❌ AttributeError
```

## Logging and Debugging

### 1. Attribute Logger

```python
class LoggedAttributes:
    def __setattr__(self, name, value):
        print(f"[SET] {name} = {value} (type: {type(value).__name__})")
        super().__setattr__(name, value)

obj = LoggedAttributes()
obj.x = 42
# [SET] x = 42 (type: int)
obj.name = "Alice"
# [SET] name = Alice (type: str)
```

### 2. With Timestamps

```python
from datetime import datetime

class TimestampedAttributes:
    def __init__(self):
        super().__setattr__('_timestamps', {})
    
    def __setattr__(self, name, value):
        if name != '_timestamps':
            timestamps = super().__getattribute__('_timestamps')
            timestamps[name] = datetime.now()
        super().__setattr__(name, value)

obj = TimestampedAttributes()
obj.x = 10
obj.y = 20
print(obj._timestamps)
# {'x': datetime(...), 'y': datetime(...)}
```

### 3. Audit Trail

```python
class AuditedObject:
    def __init__(self):
        super().__setattr__('_history', [])
    
    def __setattr__(self, name, value):
        if name != '_history':
            history = super().__getattribute__('_history')
            history.append({
                'attr': name,
                'value': value,
                'time': datetime.now()
            })
        super().__setattr__(name, value)
```

## Interaction with Properties

### 1. Properties Take Priority

```python
class Example:
    def __init__(self):
        self._value = 0
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        print("Property setter")
        self._value = val
    
    def __setattr__(self, name, value):
        print(f"__setattr__: {name}")
        super().__setattr__(name, value)

obj = Example()
obj.value = 42
# Output:
# __setattr__: _value
# __setattr__: value
# Property setter
# __setattr__: _value
```

### 2. Call Order

```python
obj.value = 42
    ↓
__setattr__('value', 42) called
    ↓
super().__setattr__('value', 42)
    ↓
Finds property descriptor in class
    ↓
Calls property's __set__ method
    ↓
Inside setter: self._value = val
    ↓
__setattr__('_value', val) called again
```

### 3. Bypassing Properties

```python
def __setattr__(self, name, value):
    if name == 'special':
        # Bypass property, set directly
        self.__dict__[name] = value
    else:
        super().__setattr__(name, value)
```

## Advanced Patterns

### 1. Attribute Registry

```python
class RegisteredAttributes:
    _registry = {}
    
    def __setattr__(self, name, value):
        # Register all attributes
        RegisteredAttributes._registry[id(self), name] = value
        super().__setattr__(name, value)
    
    @classmethod
    def get_all_values(cls):
        return list(cls._registry.values())
```

### 2. Proxy Pattern

```python
class Proxy:
    def __init__(self, obj):
        object.__setattr__(self, '_obj', obj)
    
    def __setattr__(self, name, value):
        if name == '_obj':
            object.__setattr__(self, name, value)
        else:
            setattr(object.__getattribute__(self, '_obj'), name, value)

class Target:
    def __init__(self):
        self.value = 0

proxy = Proxy(Target())
proxy.value = 42
```

### 3. Slots Enforcement

```python
class StrictSlots:
    __slots__ = ['x', 'y']
    
    def __setattr__(self, name, value):
        if name not in self.__slots__:
            raise AttributeError(f"'{name}' not in __slots__")
        super().__setattr__(name, value)

obj = StrictSlots()
obj.x = 10  # ✅ OK
# obj.z = 20  # ❌ AttributeError
```

## Common Mistakes

### 1. Infinite Recursion

```python
# ❌ BAD
def __setattr__(self, name, value):
    self.name = value  # Recursion!

# ✅ GOOD
def __setattr__(self, name, value):
    super().__setattr__(name, value)
```

### 2. Not Storing Values

```python
# ❌ BAD - validation but no storage
def __setattr__(self, name, value):
    if isinstance(value, int):
        print("Valid")
    # Value is never stored!

# ✅ GOOD
def __setattr__(self, name, value):
    if isinstance(value, int):
        print("Valid")
    super().__setattr__(name, value)
```

### 3. Breaking `__init__`

```python
# ❌ BAD
def __setattr__(self, name, value):
    if hasattr(self, 'initialized'):
        # Logic here
        pass
    # Can't set 'initialized' in __init__!

# ✅ GOOD
def __setattr__(self, name, value):
    if name == 'initialized' or not hasattr(self, 'initialized'):
        super().__setattr__(name, value)
    else:
        # Logic here
        super().__setattr__(name, value)
```
