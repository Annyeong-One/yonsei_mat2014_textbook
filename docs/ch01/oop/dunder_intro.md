# Dunder Methods

Dunder methods (double underscore methods) enable operator overloading and customize object behavior in Python.

---

## What are Dunder Methods

### 1. Special Method Names

```python
class MyNumber:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return MyNumber(self.value + other.value)
```

Methods with `__name__` pattern define special behavior.

### 2. Double Underscores

"Dunder" = "double underscore" prefix and suffix.

### 3. Reserved Names

Python reserves these for specific operations.

---

## Operator Overloading

### 1. Syntactic Sugar

```python
x = MyNumber(5)
y = MyNumber(3)

# These are equivalent:
result = x + y
result = x.__add__(y)
```

Operators call dunder methods automatically.

### 2. Custom Behavior

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Vector(4, 6)
```

### 3. Polymorphic Operators

Same operator behaves differently for different types.

---

## Why Dunder Methods

### 1. Pythonic Code

```python
# Without dunder methods
result = vector1.add(vector2)

# With dunder methods
result = vector1 + vector2  # More readable
```

### 2. Built-in Integration

```python
class Container:
    def __len__(self):
        return self.size

c = Container()
print(len(c))  # Works with built-in len()
```

### 3. Consistent Interface

Objects behave like built-in types.

---

## Common Dunder Methods

### 1. Initialization

```python
def __init__(self, value):
    self.value = value
```

Constructor - called during object creation.

### 2. String Representation

```python
def __repr__(self):
    return f"MyClass({self.value})"

def __str__(self):
    return f"Value: {self.value}"
```

### 3. Operator Methods

```python
def __add__(self, other):
    return MyClass(self.value + other.value)

def __eq__(self, other):
    return self.value == other.value
```

---

## How It Works

### 1. Method Lookup

```python
x + y
# Python looks for x.__add__(y)
```

Python translates operators to method calls.

### 2. Automatic Invocation

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        print("__add__ called!")
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Prints: __add__ called!
```

### 3. No Manual Calls

Don't call `obj.__add__(other)` directly—use `obj + other`.

---

## Categories of Dunder

### 1. Object Lifecycle

- `__init__`: initialization
- `__del__`: cleanup
- `__new__`: object creation

### 2. Representation

- `__repr__`: developer representation
- `__str__`: user-friendly string
- `__format__`: custom formatting

### 3. Operators

- Arithmetic: `__add__`, `__sub__`, `__mul__`
- Comparison: `__eq__`, `__lt__`, `__le__`
- Bitwise: `__and__`, `__or__`, `__xor__`

### 4. Containers

- `__len__`: length
- `__getitem__`: indexing
- `__contains__`: membership

---

## Basic Example

### 1. Simple Class

```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Number(self.value + other.value)
    
    def __repr__(self):
        return f"Number({self.value})"
```

### 2. Usage

```python
a = Number(5)
b = Number(3)
c = a + b
print(c)  # Number(8)
```

### 3. Multiple Operators

```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Number(self.value + other.value)
    
    def __mul__(self, other):
        return Number(self.value * other.value)
    
    def __repr__(self):
        return f"Number({self.value})"

a = Number(5)
b = Number(3)
print(a + b)  # Number(8)
print(a * b)  # Number(15)
```

---

## Design Principles

### 1. Follow Semantics

```python
# Good - mathematically sensible
def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

# Bad - confusing semantics
def __add__(self, other):
    return self.x * other.y  # Unexpected!
```

### 2. Type Consistency

```python
def __add__(self, other):
    # Return same type as operands
    return Vector(self.x + other.x, self.y + other.y)
```

### 3. Immutability Preferred

```python
# Good - returns new object
def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

# Risky - modifies in place
def __add__(self, other):
    self.x += other.x
    return self
```

---

## Not Overloadable

### 1. Logical Operators

`and`, `or`, `not` cannot be overloaded directly.

### 2. Identity Operator

`is` checks object identity—no dunder method.

### 3. Assignment

`=` is not overloadable—it binds names.

---

## Key Takeaways

- Dunder methods enable operator overloading.
- Format: `__methodname__`
- Operators call dunder methods automatically.
- Makes custom objects behave like built-ins.
- Follow clear, mathematical semantics.
