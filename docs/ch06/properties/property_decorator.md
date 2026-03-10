# Property Decorator


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## What Are Properties?

### 1. Definition

A **property** allows you to **define methods that behave like attributes**. This supports encapsulation while enabling attribute-style access.

It is declared using the `@property` decorator and optionally `@<property>.setter` and `@<property>.deleter`.

### 2. Core Motivation

Use properties to:

- Expose **computed values** as attributes
- Add **getter/setter logic** without changing the external API
- Enforce **validation** or **read-only** access
- Keep internal representation private while providing clean interface

### 3. Basic Syntax

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        from math import pi
        return pi * self._radius ** 2
```

## Read-Only Properties

### 1. Simple Example

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        from math import pi
        return pi * self._radius ** 2

c = Circle(3)
print(c.area)  # attribute-like access, but computed
# c.area = 50  # Error: no setter defined
```

### 2. Why Use Read-Only

- Prevents accidental modification of computed values
- Encapsulates calculation logic
- Maintains data consistency
- Provides clean API without exposing implementation

### 3. Common Use Cases

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
```

## Alternative Approaches

### 1. Without Property

You'd have to do this instead:

```python
class Person:
    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not value.isalpha():
            raise ValueError("Name must be alphabetic")
        self._name = value
```

Accessing looks ugly:

```python
p = Person("Alice")
p.set_name("Bob")
print(p.get_name())
```

### 2. With Property

Using `@property`, you retain **encapsulation** while exposing a **clean interface**:

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

### 3. API Comparison

| Approach | Read Syntax | Write Syntax | Pythonic |
|----------|-------------|--------------|----------|
| Methods | `p.get_name()` | `p.set_name("Bob")` | ❌ |
| Property | `p.name` | `p.name = "Bob"` | ✅ |

## Internal Mechanism

### 1. Descriptor Object

When you define a property:

```python
@property
def name(self): ...
```

Python creates a **descriptor object** of type `property`, which:

- Implements the `__get__`, `__set__`, and `__delete__` methods
- Lives in the class's namespace (`Person.__dict__`)
- Manages how the attribute behaves at the instance level

### 2. Inspection

You can inspect it:

```python
print(type(Person.name))  # <class 'property'>
```

### 3. How It Works

Properties are **descriptors** stored at the class level that intercept attribute access at the instance level.
