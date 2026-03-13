# __get__ __set__ __delete__

## The Three Methods

### 1. Method Signatures

```python
class Descriptor:
    def __get__(self, instance, owner):
        """Called on attribute read"""
        pass
    
    def __set__(self, instance, value):
        """Called on attribute write"""
        pass
    
    def __delete__(self, instance):
        """Called on attribute deletion"""
        pass
```

### 2. Parameters

**`__get__(self, instance, owner)`:**
- `self` - the descriptor object itself
- `instance` - the instance being accessed (`None` if accessed from class)
- `owner` - the class that owns the descriptor

**`__set__(self, instance, value)`:**
- `self` - the descriptor object itself
- `instance` - the instance being modified
- `value` - the value being assigned

**`__delete__(self, instance)`:**
- `self` - the descriptor object itself
- `instance` - the instance where attribute is being deleted

### 3. When They're Called

```python
obj.attr        # → __get__(descriptor, obj, type(obj))
obj.attr = val  # → __set__(descriptor, obj, val)
del obj.attr    # → __delete__(descriptor, obj)

Class.attr      # → __get__(descriptor, None, Class)
```

## __get__ Method

### 1. Basic Implementation

```python
class GetDescriptor:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        print(f"__get__ called")
        print(f"  self = {self}")
        print(f"  instance = {instance}")
        print(f"  owner = {owner}")
        
        if instance is None:
            return self  # Accessed from class
        
        return instance.__dict__.get(self.name, "default")

class MyClass:
    attr = GetDescriptor('attr')

# Access from class
print(MyClass.attr)
# __get__ called
#   self = <GetDescriptor object>
#   instance = None
#   owner = <class 'MyClass'>

# Access from instance
obj = MyClass()
obj.attr = 42
print(obj.attr)
# __get__ called
#   self = <GetDescriptor object>
#   instance = <MyClass object>
#   owner = <class 'MyClass'>
# 42
```

### 2. Handling Class vs Instance

```python
class SmartGetter:
    def __init__(self, value):
        self.value = value
    
    def __get__(self, instance, owner):
        if instance is None:
            # Accessed from class - return descriptor
            return self
        # Accessed from instance - return value
        return self.value

class Example:
    x = SmartGetter(42)

print(Example.x)      # <SmartGetter object>
print(Example().x)    # 42
```

### 3. Computed Values

```python
class ComputedProperty:
    def __init__(self, func):
        self.func = func
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.func(instance)

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @ComputedProperty
    def area(self):
        from math import pi
        return pi * self.radius ** 2

c = Circle(5)
print(c.area)  # 78.54... (computed each time)
```

## __set__ Method

### 1. Basic Implementation

```python
class SetDescriptor:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        print(f"__set__ called")
        print(f"  self = {self}")
        print(f"  instance = {instance}")
        print(f"  value = {value}")
        
        instance.__dict__[self.name] = value

class MyClass:
    attr = SetDescriptor('attr')

obj = MyClass()
obj.attr = 42
# __set__ called
#   self = <SetDescriptor object>
#   instance = <MyClass object>
#   value = 42
```

### 2. Validation

```python
class ValidatedDescriptor:
    def __init__(self, name, validator):
        self.name = name
        self.validator = validator
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        instance.__dict__[self.name] = value

class Person:
    age = ValidatedDescriptor('age', lambda x: 0 <= x <= 150)
    name = ValidatedDescriptor('name', lambda x: len(x) > 0)

p = Person()
p.age = 30      # ✅ OK
# p.age = 200   # ❌ ValueError
p.name = "Alice"  # ✅ OK
# p.name = ""   # ❌ ValueError
```

### 3. Type Enforcement

```python
class TypedDescriptor:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} must be {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        instance.__dict__[self.name] = value

class Product:
    name = TypedDescriptor('name', str)
    price = TypedDescriptor('price', (int, float))
    quantity = TypedDescriptor('quantity', int)

prod = Product()
prod.name = "Widget"   # ✅ OK
prod.price = 19.99     # ✅ OK
# prod.name = 123      # ❌ TypeError
```

## __delete__ Method

### 1. Basic Implementation

```python
class DeleteDescriptor:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        print(f"__delete__ called")
        print(f"  self = {self}")
        print(f"  instance = {instance}")
        
        del instance.__dict__[self.name]

class MyClass:
    attr = DeleteDescriptor('attr')

obj = MyClass()
obj.attr = 42
del obj.attr
# __delete__ called
#   self = <DeleteDescriptor object>
#   instance = <MyClass object>
```

### 2. Protected Deletion

```python
class ProtectedDescriptor:
    def __init__(self, name, deletable=True):
        self.name = name
        self.deletable = deletable
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        if not self.deletable:
            raise AttributeError(f"Cannot delete {self.name}")
        del instance.__dict__[self.name]

class Person:
    id = ProtectedDescriptor('id', deletable=False)
    name = ProtectedDescriptor('name', deletable=True)

p = Person()
p.id = 123
p.name = "Alice"

del p.name  # ✅ OK
# del p.id  # ❌ AttributeError
```

### 3. Cleanup on Delete

```python
class ResourceDescriptor:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        resource = instance.__dict__.get(self.name)
        if resource and hasattr(resource, 'close'):
            print(f"Closing resource: {self.name}")
            resource.close()
        del instance.__dict__[self.name]

class FileHandler:
    file = ResourceDescriptor('file')

handler = FileHandler()
handler.file = open('test.txt', 'w')
del handler.file  # Closes file before deleting
```

## Complete Example

### 1. Full Descriptor

```python
class ManagedAttribute:
    def __init__(self, name, validator=None, default=None):
        self.name = name
        self.validator = validator
        self.default = default
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, self.default)
    
    def __set__(self, instance, value):
        if self.validator and not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}")
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        if self.name in instance.__dict__:
            del instance.__dict__[self.name]

class Person:
    name = ManagedAttribute(
        'name',
        validator=lambda x: isinstance(x, str) and len(x) > 0
    )
    age = ManagedAttribute(
        'age',
        validator=lambda x: isinstance(x, int) and 0 <= x <= 150,
        default=0
    )

p = Person()
p.name = "Alice"
p.age = 30
print(p.name, p.age)  # Alice 30

del p.age
print(p.age)  # 0 (default)
```

### 2. With Logging

```python
class LoggedDescriptor:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = instance.__dict__.get(self.name)
        print(f"[GET] {self.name} = {value}")
        return value
    
    def __set__(self, instance, value):
        print(f"[SET] {self.name} = {value}")
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        print(f"[DEL] {self.name}")
        if self.name in instance.__dict__:
            del instance.__dict__[self.name]

class Example:
    x = LoggedDescriptor('x')
    y = LoggedDescriptor('y')

obj = Example()
obj.x = 10      # [SET] x = 10
print(obj.x)    # [GET] x = 10
del obj.x       # [DEL] x
```

### 3. With Caching

```python
class CachedDescriptor:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # Check cache
        cache_name = f'_cached_{self.name}'
        if cache_name not in instance.__dict__:
            # Compute and cache
            value = self.func(instance)
            instance.__dict__[cache_name] = value
        
        return instance.__dict__[cache_name]
    
    def __set__(self, instance, value):
        raise AttributeError("Cannot set computed property")
    
    def __delete__(self, instance):
        # Clear cache
        cache_name = f'_cached_{self.name}'
        if cache_name in instance.__dict__:
            del instance.__dict__[cache_name]

class ExpensiveCalculation:
    def __init__(self, data):
        self.data = data
    
    @CachedDescriptor
    def result(self):
        print("Computing...")
        return sum(x**2 for x in self.data)

obj = ExpensiveCalculation([1, 2, 3, 4, 5])
print(obj.result)  # Computing... 55
print(obj.result)  # 55 (from cache)
del obj.result     # Clear cache
print(obj.result)  # Computing... 55
```

## Method Interaction

### 1. All Three Together

When all three methods are defined, they work together:

```python
obj.attr        # → __get__
obj.attr = val  # → __set__
del obj.attr    # → __delete__
```

### 2. Only Some Defined

You don't need all three:

```python
# Read-only descriptor (no __set__)
class ReadOnly:
    def __get__(self, instance, owner):
        return "constant"

# Write-only descriptor (unusual, but possible)
class WriteOnly:
    def __set__(self, instance, value):
        instance.__dict__['_value'] = value
```

### 3. Call Order

```python
class TrackedDescriptor:
    def __get__(self, instance, owner):
        print("1. __get__")
        return instance.__dict__.get('value', 0)
    
    def __set__(self, instance, value):
        print("2. __set__")
        instance.__dict__['value'] = value
    
    def __delete__(self, instance):
        print("3. __delete__")
        del instance.__dict__['value']

class Example:
    attr = TrackedDescriptor()

obj = Example()
obj.attr = 10   # 2. __set__
x = obj.attr    # 1. __get__
del obj.attr    # 3. __delete__
```
