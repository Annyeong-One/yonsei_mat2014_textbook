# Properties as Descriptors

## The Connection

### 1. Property IS a Descriptor

The `@property` decorator creates a descriptor object:

```python
class Example:
    @property
    def value(self):
        return self._value

# Property is a descriptor!
print(type(Example.value))  # <class 'property'>
print(hasattr(Example.value, '__get__'))  # True
print(hasattr(Example.value, '__set__'))  # True (if setter defined)
```

### 2. How Property Works

```python
# When you write:
@property
def value(self):
    return self._value

# Python creates:
value = property(fget=value_getter_function)

# Which is a descriptor with __get__, __set__, __delete__
```

### 3. Accessing Property

```python
obj.value
    ↓
type(obj).__dict__['value'].__get__(obj, type(obj))
    ↓
Calls the getter function
```

## Property Implementation

### 1. Simplified Property

```python
class Property:
    """Simplified property implementation"""
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(instance)
    
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)
    
    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)
    
    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel)
    
    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel)
    
    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel)

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @Property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value

c = Circle(5)
print(c.radius)  # 5
c.radius = 10
print(c.radius)  # 10
```

### 2. Property Data Descriptor

```python
class Example:
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val

# Has both __get__ and __set__ → data descriptor
desc = type(Example.value)
print(hasattr(Example.value, '__get__'))   # True
print(hasattr(Example.value, '__set__'))   # True

# Data descriptor wins over instance dict
obj = Example()
obj.__dict__['value'] = 999
obj.value = 42
print(obj.value)  # 42 (not 999)
```

### 3. Read-Only Property

```python
class Example:
    @property
    def value(self):
        return self._value

# Only has __get__ → non-data descriptor
print(hasattr(Example.value, '__get__'))   # True
print(hasattr(Example.value, '__set__'))   # False

# Can be overridden by instance dict
obj = Example()
obj._value = 42
obj.__dict__['value'] = 999
print(obj.value)  # 999 (instance dict wins)
```

## Custom Property-Like Descriptors

### 1. Validated Property

```python
class ValidatedProperty:
    def __init__(self, validator):
        self.validator = validator
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f'_{name}'
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, None)
    
    def __set__(self, instance, value):
        if not self.validator(value):
            raise ValueError(f"Validation failed for {self.name}")
        setattr(instance, self.name, value)

class Person:
    age = ValidatedProperty(lambda x: 0 <= x <= 150)
    name = ValidatedProperty(lambda x: len(x) > 0)

p = Person()
p.age = 30  # ✅ OK
# p.age = 200  # ❌ ValueError
```

### 2. Computed Property with Caching

```python
class CachedProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # Check cache in instance dict
        value = instance.__dict__.get(self.name)
        if value is None:
            # Compute and cache
            value = self.func(instance)
            instance.__dict__[self.name] = value
        return value
    
    def __set__(self, instance, value):
        # Allow manual override
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        # Clear cache
        instance.__dict__.pop(self.name, None)

class DataLoader:
    @CachedProperty
    def data(self):
        print("Loading data...")
        return [1, 2, 3, 4, 5]

loader = DataLoader()
print(loader.data)  # Loading data... [1, 2, 3, 4, 5]
print(loader.data)  # [1, 2, 3, 4, 5] (cached)
del loader.data
print(loader.data)  # Loading data... [1, 2, 3, 4, 5]
```

### 3. Type-Enforced Property

```python
class TypedProperty:
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f'_{name}'
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, None)
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name[1:]} must be {self.expected_type.__name__}"
            )
        setattr(instance, self.name, value)

class Product:
    name = TypedProperty(str)
    price = TypedProperty((int, float))
    quantity = TypedProperty(int)

p = Product()
p.name = "Widget"  # ✅ OK
p.price = 19.99    # ✅ OK
# p.name = 123     # ❌ TypeError
```

## Property vs Custom Descriptor

### 1. When to Use Property

Use `@property` when:
- Simple getter/setter/deleter logic
- One-off attribute management
- Quick prototyping
- Standard property behavior is sufficient

```python
class Circle:
    @property
    def area(self):
        return 3.14 * self.radius ** 2
```

### 2. When to Use Custom Descriptor

Use custom descriptor when:
- Reusable validation logic
- Complex attribute behavior
- Need to share logic across multiple classes
- Building frameworks or libraries

```python
class PositiveNumber:
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Must be positive")
        instance.__dict__[self.name] = value

class Rectangle:
    width = PositiveNumber()
    height = PositiveNumber()

class Circle:
    radius = PositiveNumber()
```

### 3. Comparison Table

| Aspect | `@property` | Custom Descriptor |
|--------|-------------|-------------------|
| Syntax | Decorator | Class definition |
| Reusability | Per class | Across classes |
| Complexity | Simple | Can be complex |
| Use case | Specific attributes | Generic patterns |
| Examples | Computed values | Validation, ORM fields |

## Advanced Patterns

### 1. Chained Properties

```python
class ChainedProperty:
    def __init__(self, func):
        self.func = func
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.func(instance)
    
    def __set__(self, instance, value):
        # Allow chaining
        self.func(instance).__set__(value)
        return instance

class Builder:
    @ChainedProperty
    def name(self):
        return self

b = Builder().name("Alice").name("Bob")
```

### 2. Property with Dependencies

```python
class DependentProperty:
    def __init__(self, func, *dependencies):
        self.func = func
        self.dependencies = dependencies
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f'_cached_{name}'
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # Check if dependencies changed
        cache_key = tuple(getattr(instance, d) for d in self.dependencies)
        cached = getattr(instance, self.name, None)
        
        if cached is None or cached[0] != cache_key:
            value = self.func(instance)
            setattr(instance, self.name, (cache_key, value))
        
        return cached[1] if cached else self.func(instance)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @DependentProperty
    def area(self):
        print("Computing area")
        return self.width * self.height
    
    area.dependencies = ('width', 'height')

r = Rectangle(5, 10)
print(r.area)  # Computing area... 50
r.width = 6
print(r.area)  # Computing area... 60 (recomputed)
```

### 3. Lazy Property

```python
class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        # Replace descriptor with computed value
        setattr(instance, self.name, value)
        return value

class DataLoader:
    @LazyProperty
    def data(self):
        print("Loading...")
        return [1, 2, 3, 4, 5]

loader = DataLoader()
print(type(loader.__class__.data))  # <class 'LazyProperty'>
print(loader.data)                  # Loading... [1, 2, 3, 4, 5]
print(type(loader.data))            # <class 'list'>
```

## Internals

### 1. Property Object Structure

```python
class Example:
    @property
    def value(self):
        """Get value"""
        return self._value

prop = Example.value
print(prop.fget)      # <function value at ...>
print(prop.fset)      # None
print(prop.fdel)      # None
print(prop.__doc__)   # "Get value"
```

### 2. Decorator Chain

```python
class Example:
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val

# Is equivalent to:
def get_value(self):
    return self._value

def set_value(self, val):
    self._value = val

value = property(get_value)
value = value.setter(set_value)
```

### 3. Manual Property Creation

```python
class Example:
    def _get_value(self):
        return self._value
    
    def _set_value(self, val):
        if val < 0:
            raise ValueError("Must be non-negative")
        self._value = val
    
    def _del_value(self):
        del self._value
    
    value = property(_get_value, _set_value, _del_value, "Value property")

obj = Example()
obj.value = 42
print(obj.value)  # 42
```

## Summary

### 1. Key Takeaways

- Properties ARE descriptors (specifically, data descriptors when they have a setter)
- Properties use `__get__`, `__set__`, and `__delete__` under the hood
- Custom descriptors allow reusable property-like behavior
- Choose properties for simplicity, descriptors for reusability

### 2. Mental Model

```python
@property               Custom Descriptor
    ↓                          ↓
Creates property object    Creates descriptor class
    ↓                          ↓
Descriptor protocol        Descriptor protocol
    ↓                          ↓
__get__, __set__, __delete__
```

### 3. Best Practices

- Use `@property` as default choice
- Create custom descriptors when reusing logic
- Document descriptor behavior clearly
- Test edge cases (class access, None checks)
- Consider using `__set_name__` for automatic naming
