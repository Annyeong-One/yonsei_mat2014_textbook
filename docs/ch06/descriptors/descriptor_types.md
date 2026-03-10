# Data vs Non-Data


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Two Types

### 1. Definitions

**Data Descriptor:**
- Defines `__set__` and/or `__delete__` (at least one)
- Takes **priority** over instance `__dict__`

**Non-Data Descriptor:**
- Defines **only** `__get__`
- **Defers** to instance `__dict__` if it exists

### 2. Key Difference

```python
# Data descriptor - has __set__
class DataDesc:
    def __get__(self, instance, owner):
        return "data descriptor"
    
    def __set__(self, instance, value):
        pass  # Even empty __set__ makes it data descriptor

# Non-data descriptor - only __get__
class NonDataDesc:
    def __get__(self, instance, owner):
        return "non-data descriptor"
```

### 3. Priority Table

| Lookup Order | What Python Checks |
|--------------|-------------------|
| 1st | Data descriptors from class |
| 2nd | Instance `__dict__` |
| 3rd | Non-data descriptors from class |
| 4th | Class `__dict__` |
| 5th | `__getattr__` if defined |

## Priority Demonstration

### 1. Data Descriptor Wins

```python
class DataDescriptor:
    def __get__(self, instance, owner):
        return "from data descriptor"
    
    def __set__(self, instance, value):
        print(f"Setting via descriptor: {value}")

class MyClass:
    attr = DataDescriptor()

obj = MyClass()

# Try to set in instance dict
obj.__dict__['attr'] = "instance value"

# Data descriptor wins!
print(obj.attr)  # "from data descriptor"
```

### 2. Instance Dict Wins

```python
class NonDataDescriptor:
    def __get__(self, instance, owner):
        return "from non-data descriptor"

class MyClass:
    attr = NonDataDescriptor()

obj = MyClass()

# Set in instance dict
obj.__dict__['attr'] = "instance value"

# Instance dict wins!
print(obj.attr)  # "instance value"
```

### 3. Side-by-Side Comparison

```python
class DataDesc:
    def __get__(self, instance, owner):
        return "data"
    def __set__(self, instance, value):
        pass

class NonDataDesc:
    def __get__(self, instance, owner):
        return "non-data"

class Example:
    data_attr = DataDesc()
    nondata_attr = NonDataDesc()

obj = Example()

# Set in instance __dict__
obj.__dict__['data_attr'] = "instance data"
obj.__dict__['nondata_attr'] = "instance non-data"

print(obj.data_attr)     # "data" (descriptor wins)
print(obj.nondata_attr)  # "instance non-data" (instance wins)
```

## Real-World Examples

### 1. Property is Data Descriptor

```python
class Example:
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val

obj = Example()

# Property has both __get__ and __set__
print(hasattr(type(obj).__dict__['value'], '__get__'))  # True
print(hasattr(type(obj).__dict__['value'], '__set__'))  # True

# Try to override in instance dict
obj.__dict__['value'] = 999

# Property still wins!
obj.value = 42
print(obj.value)  # 42 (not 999)
```

### 2. Methods are Non-Data

```python
class Example:
    def method(self):
        return "original method"

obj = Example()

# Methods only have __get__ (non-data descriptor)
print(hasattr(type(obj).__dict__['method'], '__get__'))  # True
print(hasattr(type(obj).__dict__['method'], '__set__'))  # False

# Can override in instance dict!
obj.__dict__['method'] = lambda: "overridden"
print(obj.method())  # "overridden"
```

### 3. Read-Only Property

```python
class ReadOnlyProperty:
    """Non-data descriptor (no __set__)"""
    def __init__(self, func):
        self.func = func
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.func(instance)

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @ReadOnlyProperty
    def area(self):
        from math import pi
        return pi * self.radius ** 2

c = Circle(5)
print(c.area)  # 78.54...

# Can override because it's non-data!
c.__dict__['area'] = 100
print(c.area)  # 100
```

## Why This Matters

### 1. Property Behavior

Properties need `__set__` to override instance attributes:

```python
class Person:
    @property
    def name(self):
        return self._name
    
    # Without setter - non-data descriptor
    # With setter - data descriptor

p = Person()
p._name = "Alice"

# If property has no setter (non-data):
# p.name can be overridden by p.__dict__['name']

# If property has setter (data):
# p.name always uses property, can't override
```

### 2. Method Rebinding

Methods can be overridden per-instance:

```python
class Example:
    def method(self):
        return "class method"

obj1 = Example()
obj2 = Example()

# Override just for obj1
obj1.method = lambda: "custom method"

print(obj1.method())  # "custom method"
print(obj2.method())  # "class method"
```

### 3. Caching Pattern

Non-data descriptors enable caching:

```python
class cached_property:
    """Computes once, then replaces itself"""
    def __init__(self, func):
        self.func = func
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        # Compute value
        value = self.func(instance)
        # Replace descriptor with value in instance dict
        instance.__dict__[self.func.__name__] = value
        return value

class Expensive:
    @cached_property
    def data(self):
        print("Computing...")
        return [1, 2, 3, 4, 5]

obj = Expensive()
print(obj.data)  # Computing... [1, 2, 3, 4, 5]
print(obj.data)  # [1, 2, 3, 4, 5] (from __dict__, no computing)
```

## Making Descriptors Data

### 1. Add Empty __set__

```python
class BecomeData:
    def __get__(self, instance, owner):
        return "value"
    
    def __set__(self, instance, value):
        # Even if empty, makes it data descriptor
        raise AttributeError("Read-only")

class Example:
    attr = BecomeData()

obj = Example()
obj.__dict__['attr'] = "won't work"
print(obj.attr)  # "value" (descriptor wins)
```

### 2. Add __delete__

```python
class AlsoData:
    def __get__(self, instance, owner):
        return "value"
    
    def __delete__(self, instance):
        # Having __delete__ also makes it data descriptor
        raise AttributeError("Cannot delete")
```

### 3. Comparison

```python
# Non-data (only __get__)
class NonData:
    def __get__(self, instance, owner):
        return "non-data"

# Data (__get__ + __set__)
class Data1:
    def __get__(self, instance, owner):
        return "data"
    def __set__(self, instance, value):
        pass

# Data (__get__ + __delete__)
class Data2:
    def __get__(self, instance, owner):
        return "data"
    def __delete__(self, instance):
        pass

# Data (__get__ + __set__ + __delete__)
class Data3:
    def __get__(self, instance, owner):
        return "data"
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass
```

## Practical Implications

### 1. Validation Requires Data

```python
class ValidatedAge:
    """Must be data descriptor to validate"""
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('_age', 0)
    
    def __set__(self, instance, value):
        if not 0 <= value <= 150:
            raise ValueError("Invalid age")
        instance.__dict__['_age'] = value

class Person:
    age = ValidatedAge()

p = Person()
p.age = 30  # ✅ Validated
# p.__dict__['_age'] = 200  # ⚠️ Bypasses validation!
# But: p.age still goes through descriptor
```

### 2. Computed Without Caching

```python
class AlwaysComputed:
    """Data descriptor - always computes"""
    def __init__(self, func):
        self.func = func
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.func(instance)
    
    def __set__(self, instance, value):
        raise AttributeError("Read-only computed property")

class Rectangle:
    @AlwaysComputed
    def area(self):
        print("Computing area")
        return self.width * self.height

# Computes every time
r = Rectangle()
r.width, r.height = 5, 10
print(r.area)  # Computing area... 50
print(r.area)  # Computing area... 50 (not cached)
```

### 3. Cached with Non-Data

```python
class CachedProperty:
    """Non-data descriptor - caches by self-replacement"""
    def __init__(self, func):
        self.func = func
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        # Store in instance dict - becomes regular attribute
        setattr(instance, self.func.__name__, value)
        return value

class Rectangle:
    @CachedProperty
    def area(self):
        print("Computing area")
        return self.width * self.height

r = Rectangle()
r.width, r.height = 5, 10
print(r.area)  # Computing area... 50
print(r.area)  # 50 (from __dict__, cached)
```

## Testing Descriptor Type

### 1. Check Methods

```python
def is_data_descriptor(obj):
    """Check if object is a data descriptor"""
    return (hasattr(obj, '__set__') or hasattr(obj, '__delete__'))

def is_non_data_descriptor(obj):
    """Check if object is non-data descriptor"""
    return hasattr(obj, '__get__') and not is_data_descriptor(obj)

# Test
class DataDesc:
    def __get__(self, instance, owner): pass
    def __set__(self, instance, value): pass

class NonDataDesc:
    def __get__(self, instance, owner): pass

print(is_data_descriptor(DataDesc()))      # True
print(is_non_data_descriptor(NonDataDesc()))  # True
```

### 2. Inspect Property

```python
class Example:
    @property
    def read_only(self):
        return 42
    
    @property
    def read_write(self):
        return self._value
    
    @read_write.setter
    def read_write(self, value):
        self._value = value

# Check types
ro = type(Example.read_only)
rw = type(Example.read_write)

print(hasattr(Example.read_only, '__set__'))    # False (non-data)
print(hasattr(Example.read_write, '__set__'))   # True (data)
```

## Summary Table

### 1. Type Characteristics

| Type | Has __get__ | Has __set__ or __delete__ | Priority |
|------|-------------|--------------------------|----------|
| Data | Yes | Yes | Before instance dict |
| Non-data | Yes | No | After instance dict |

### 2. Common Examples

| Example | Type | Reason |
|---------|------|--------|
| `@property` with setter | Data | Has `__set__` |
| `@property` without setter | Non-data | Only `__get__` |
| Methods | Non-data | Only `__get__` |
| `@classmethod` | Non-data | Only `__get__` |
| `@staticmethod` | Non-data | Only `__get__` |
| `@functools.cached_property` | Non-data | Only `__get__` |

### 3. Use Cases

| Need | Use |
|------|-----|
| Validation | Data descriptor |
| Computed property | Either (depends on caching) |
| Caching with replacement | Non-data descriptor |
| Always compute fresh | Data descriptor |
| Method-like behavior | Non-data descriptor |
