# Lookup Hierarchy

## Attribute Resolution

### 1. The Resolution Order

When you access `obj.attr`, Python searches in this order:

1. **Data descriptors** from `type(obj)` and its bases
2. **Instance attributes** from `obj.__dict__`
3. **Non-data descriptors** from `type(obj)` and its bases
4. **Class attributes** from `type(obj)` and its bases
5. **`__getattr__`** if defined and attribute not found

### 2. Key Principle

**Data descriptors override instance attributes**, while **non-data descriptors defer to instance attributes**.

### 3. Visual Flow

```
obj.attr
    ↓
__getattribute__ called
    ↓
Check data descriptors in class
    ↓
Check instance __dict__
    ↓
Check non-data descriptors in class
    ↓
Check class attributes
    ↓
__getattr__ (if defined)
    ↓
AttributeError
```

## Data vs Non-Data

### 1. Data Descriptor

Defines `__set__` or `__delete__` (or both):

```python
class DataDescriptor:
    def __get__(self, instance, owner):
        return "data descriptor value"
    
    def __set__(self, instance, value):
        print(f"Setting to {value}")

class MyClass:
    attr = DataDescriptor()

obj = MyClass()
obj.__dict__['attr'] = "instance value"

# Data descriptor wins!
print(obj.attr)  # "data descriptor value"
```

### 2. Non-Data Descriptor

Defines only `__get__`:

```python
class NonDataDescriptor:
    def __get__(self, instance, owner):
        return "non-data descriptor value"

class MyClass:
    attr = NonDataDescriptor()

obj = MyClass()
obj.__dict__['attr'] = "instance value"

# Instance dict wins!
print(obj.attr)  # "instance value"
```

### 3. Comparison Table

| Type | Methods | Priority | Example |
|------|---------|----------|---------|
| Data descriptor | `__get__` + `__set__`/`__delete__` | Highest | `property` with setter |
| Non-data descriptor | `__get__` only | After instance | Methods, `property` without setter |
| Instance attribute | In `__dict__` | Middle | `self.x = 5` |
| Class attribute | In class | Lowest | `MyClass.x = 5` |

## MRO and Inheritance

### 1. Method Resolution Order

For inherited classes, Python follows the **MRO** (Method Resolution Order):

```python
class A:
    x = "A"

class B(A):
    pass

class C(A):
    x = "C"

class D(B, C):
    pass

print(D.mro())
# [D, B, C, A, object]

print(D.x)  # "C" (found in C before A)
```

### 2. Linearization

Python uses **C3 linearization** to create a consistent MRO that:
- Preserves local precedence order
- Respects monotonicity
- Ensures each class appears only once

### 3. Searching Through MRO

```python
class Base:
    def method(self):
        return "Base"

class Child(Base):
    pass

obj = Child()
# Searches: Child → Base → object
print(obj.method())  # "Base"
```

## Descriptor Protocol

### 1. How Descriptors Work

When accessing `obj.attr`:

```python
# Python internally does:
type(obj).__dict__['attr'].__get__(obj, type(obj))
```

### 2. Property as Descriptor

```python
class MyClass:
    @property
    def name(self):
        return self._name

# Internally:
# MyClass.name is a property object (descriptor)
# obj.name calls: MyClass.name.__get__(obj, MyClass)
```

### 3. Methods as Descriptors

Functions are non-data descriptors:

```python
class MyClass:
    def method(self):
        return "method called"

obj = MyClass()
# obj.method calls: MyClass.method.__get__(obj, MyClass)
# Returns a bound method
```

## Practical Examples

### 1. Priority Demonstration

```python
class Example:
    # Class attribute
    value = "class"
    
    @property  # Data descriptor
    def prop(self):
        return "property"

obj = Example()

# Instance attribute
obj.__dict__['value'] = "instance"
obj.__dict__['prop'] = "instance prop"

print(obj.value)  # "instance" (instance wins over class)
print(obj.prop)   # "property" (descriptor wins over instance)
```

### 2. Method Binding

```python
class MyClass:
    def method(self):
        return "called"

obj = MyClass()

# Function in class dict
print(type(MyClass.__dict__['method']))  # <class 'function'>

# Descriptor protocol creates bound method
print(type(obj.method))  # <class 'method'>
print(obj.method())      # "called"
```

### 3. Override Pattern

```python
class ConfigurableClass:
    # Default from class
    timeout = 30
    
    def __init__(self, timeout=None):
        # Override with instance value if provided
        if timeout is not None:
            self.timeout = timeout

obj1 = ConfigurableClass()
obj2 = ConfigurableClass(timeout=60)

print(obj1.timeout)  # 30 (from class)
print(obj2.timeout)  # 60 (from instance)
```

## Common Pitfalls

### 1. Shadowing Class Attributes

```python
class Counter:
    count = 0
    
    def increment(self):
        self.count += 1  # ❌ Creates instance attribute!

c1 = Counter()
c1.increment()
print(c1.count)        # 1 (instance)
print(Counter.count)   # 0 (class unchanged)
```

**Fix:**
```python
def increment(self):
    Counter.count += 1  # ✅ Modifies class attribute
```

### 2. Descriptor Access Levels

```python
class MyDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            # Accessed from class
            return self
        # Accessed from instance
        return "value"

class MyClass:
    attr = MyDescriptor()

print(MyClass.attr)      # <MyDescriptor object>
print(MyClass().attr)    # "value"
```

### 3. Understanding `__dict__`

```python
class Example:
    class_var = "class"

obj = Example()
obj.instance_var = "instance"

print(obj.__dict__)        # {'instance_var': 'instance'}
print(Example.__dict__)    # {..., 'class_var': 'class', ...}
```
