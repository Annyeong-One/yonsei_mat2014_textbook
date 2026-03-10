# Descriptor Introduction


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## What Is a Descriptor?

### 1. Definition

A **descriptor** is any object that defines at least one of these three special methods:

- `__get__(self, instance, owner)` - controls **getting** an attribute
- `__set__(self, instance, value)` - controls **setting** an attribute
- `__delete__(self, instance)` - controls **deleting** an attribute

### 2. Key Concept

Descriptors are objects that **live on classes** but manage attribute access for **instances**.

```python
class MyDescriptor:
    def __get__(self, instance, owner):
        return "descriptor value"

class MyClass:
    attr = MyDescriptor()  # Descriptor lives here (class level)

obj = MyClass()
print(obj.attr)  # "descriptor value" (accessed on instance)
```

### 3. You've Used Them

You've already used descriptors, even if you didn't know:

- `@property` - is a descriptor
- Methods - become bound methods via descriptors
- `classmethod` and `staticmethod` - are descriptors
- ORM fields (Django, SQLAlchemy) - use descriptors

## How Python Uses Descriptors

### 1. Attribute Access Protocol

When you access `obj.attr`, Python:

1. Checks if `attr` is a **data descriptor** in the class
2. Checks `obj.__dict__` for instance attribute
3. Checks if `attr` is a **non-data descriptor** in the class
4. Checks class attributes
5. Calls `__getattr__` if defined
6. Raises `AttributeError`

### 2. Descriptor Lives on Class

```python
class Descriptor:
    def __get__(self, instance, owner):
        return "value"

class MyClass:
    attr = Descriptor()  # Lives in class namespace

# Accessing from class
print(MyClass.attr)  # Descriptor.__get__(None, MyClass)

# Accessing from instance
obj = MyClass()
print(obj.attr)      # Descriptor.__get__(obj, MyClass)
```

### 3. Manages Instance Access

```python
class Descriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self  # Accessed from class
        return f"Value for {instance}"  # Accessed from instance

class MyClass:
    attr = Descriptor()

print(MyClass.attr)    # <Descriptor object>
obj = MyClass()
print(obj.attr)        # "Value for <MyClass object>"
```

## Simple Example

### 1. Basic Descriptor

```python
class SimpleDescriptor:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(f"Getting {self.name}")
        return instance.__dict__.get(self.name, None)
    
    def __set__(self, instance, value):
        print(f"Setting {self.name} = {value}")
        instance.__dict__[self.name] = value

class MyClass:
    x = SimpleDescriptor('x')
    y = SimpleDescriptor('y')

obj = MyClass()
obj.x = 10  # Setting x = 10
print(obj.x)  # Getting x → 10

obj.y = 20  # Setting y = 20
print(obj.y)  # Getting y → 20
```

### 2. Why Use This?

Instead of:
```python
class MyClass:
    def get_x(self):
        return self._x
    
    def set_x(self, value):
        self._x = value
```

You can:
```python
class MyClass:
    x = ManagedAttribute('x')
```

### 3. Benefits

- ✅ Cleaner syntax
- ✅ Reusable attribute logic
- ✅ Attribute-style access with method-level control
- ✅ DRY (Don't Repeat Yourself)

## Where Descriptors Shine

### 1. Validation

```python
class TypedDescriptor:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} must be {self.expected_type.__name__}"
            )
        instance.__dict__[self.name] = value
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

class Person:
    name = TypedDescriptor('name', str)
    age = TypedDescriptor('age', int)

p = Person()
p.name = "Alice"  # ✅ OK
p.age = 30        # ✅ OK
# p.age = "30"    # ❌ TypeError
```

### 2. Lazy Loading

```python
class LazyProperty:
    def __init__(self, func):
        self.func = func
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        # Cache by replacing descriptor with value
        setattr(instance, self.func.__name__, value)
        return value

class DataLoader:
    @LazyProperty
    def data(self):
        print("Loading data...")
        return [1, 2, 3, 4, 5]

obj = DataLoader()
print(obj.data)  # Loading data... [1, 2, 3, 4, 5]
print(obj.data)  # [1, 2, 3, 4, 5] (no loading)
```

### 3. Computed Properties

```python
class Quantity:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)
    
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        instance.__dict__[self.name] = value

class Product:
    price = Quantity('price')
    quantity = Quantity('quantity')
    
    @property
    def total(self):
        return self.price * self.quantity

prod = Product()
prod.price = 10
prod.quantity = 5
print(prod.total)  # 50
```

## Descriptor vs Property

### 1. Property Is a Descriptor

```python
# Using property
class Example:
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

# Property is actually a descriptor!
print(type(Example.__dict__['x']))  # <class 'property'>
```

### 2. When to Use Each

**Use `@property` when:**
- One-off attribute with custom logic
- Simple getter/setter/deleter
- Specific to one class

**Use descriptor when:**
- Reusable across multiple classes
- Complex attribute management
- Need to share logic

### 3. Comparison

```python
# Property - specific to one attribute
class Circle:
    @property
    def area(self):
        return 3.14 * self.radius ** 2

# Descriptor - reusable pattern
class PositiveNumber:
    def __init__(self, name):
        self.name = name
    
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Must be positive")
        instance.__dict__[self.name] = value
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 1)

class Rectangle:
    width = PositiveNumber('width')
    height = PositiveNumber('height')

class Circle:
    radius = PositiveNumber('radius')
```

## Common Use Cases

### 1. Type Enforcement

```python
class Integer:
    def __init__(self, name):
        self.name = name
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be int")
        instance.__dict__[self.name] = value
```

### 2. Value Validation

```python
class Bounded:
    def __init__(self, name, min_val, max_val):
        self.name = name
        self.min_val = min_val
        self.max_val = max_val
    
    def __set__(self, instance, value):
        if not self.min_val <= value <= self.max_val:
            raise ValueError(f"{self.name} must be in [{self.min_val}, {self.max_val}]")
        instance.__dict__[self.name] = value
```

### 3. Read-Only Attributes

```python
class ReadOnly:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, value):
        raise AttributeError("Read-only attribute")

class Config:
    MAX_CONNECTIONS = ReadOnly('MAX_CONNECTIONS', 100)
```

### 4. Logging Access

```python
class LoggedAccess:
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
```

## Why Descriptors Matter

### 1. Framework Building

ORMs use descriptors extensively:

```python
# Django-style models
class User(Model):
    name = CharField(max_length=100)
    age = IntegerField()
    email = EmailField()
```

Each field is a descriptor that handles database storage/retrieval.

### 2. Attribute Management

Descriptors centralize attribute logic:

```python
class ManagedAttribute:
    """Handles validation, logging, caching"""
    def __init__(self, validator, logger):
        self.validator = validator
        self.logger = logger
```

### 3. Code Reuse

Write once, use everywhere:

```python
# Define once
class NonNegative:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Must be non-negative")
        instance.__dict__[self.name] = value

# Use everywhere
class BankAccount:
    balance = NonNegative()

class ShoppingCart:
    total = NonNegative()

class Inventory:
    quantity = NonNegative()
```
