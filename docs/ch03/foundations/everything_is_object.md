# Everything is an Object


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python is an object-oriented language where **everything is an object** — integers, floats, strings, lists, functions, and even classes themselves.

---

## The `+` Operator: Polymorphism in Action

The same operator behaves differently based on the object's type:

```python
# Numeric addition
print(1 + 1)              # 2 (int)
print(1.0 + 1.0)          # 2.0 (float)
print(1 + 1.0)            # 2.0 (int + float → float)
print(True + True)        # 2 (bool is subclass of int)

# String concatenation
print("Hello" + "World")  # HelloWorld

# List concatenation
print([1, 2] + [3, 4])    # [1, 2, 3, 4]

# Tuple concatenation
print((1, 2) + (3, 4))    # (1, 2, 3, 4)
```

### Types That Don't Support `+`

```python
# These raise TypeError
None + None               # NoneType doesn't support +
{1, 2} + {3, 4}           # set doesn't support +
{"a": 1} + {"b": 2}       # dict doesn't support +
```

---

## How `+` Actually Works

When you write `a + b`, Python calls the `__add__` method:

```python
a + b                     # Syntactic sugar
a.__add__(b)              # Method call on object
type(a).__add__(a, b)     # Equivalent class method call
```

### Examples

```python
# Integer
1 + 2                     # 3
int.__add__(1, 2)         # 3
(1).__add__(2)            # 3

# String
"Hello" + "World"         # HelloWorld
str.__add__("Hello", "World")  # HelloWorld

# List
[1, 2] + [3, 4]           # [1, 2, 3, 4]
list.__add__([1, 2], [3, 4])   # [1, 2, 3, 4]
```

---

## Custom `__add__`: Operator Overloading

You can define how `+` works for your own classes:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)            # Vector(4, 6)
```

### How It Works

```python
v1 + v2                   # Calls v1.__add__(v2)
Vector.__add__(v1, v2)    # Equivalent
```

---

## Primitive Data Types

All primitives are objects:

```python
a = 10          # int
print(type(a))  # <class 'int'>

a = 3.14        # float
print(type(a))  # <class 'float'>

a = 1 + 2j      # complex
print(type(a))  # <class 'complex'>

a = "Hello"     # str
print(type(a))  # <class 'str'>

a = True        # bool
print(type(a))  # <class 'bool'>

a = None        # NoneType
print(type(a))  # <class 'NoneType'>
```

---

## Composite Data Types

Collections are also objects:

```python
a = [1, 2, 3]           # list
b = (1, 2, 3)           # tuple
c = {1, 2, 3}           # set
d = frozenset({1, 2})   # frozenset
e = {"a": 1, "b": 2}    # dict

print(type(a))  # <class 'list'>
print(type(b))  # <class 'tuple'>
print(type(c))  # <class 'set'>
print(type(d))  # <class 'frozenset'>
print(type(e))  # <class 'dict'>
```

---

## Functions and Classes Are Objects Too

```python
def greet():
    return "Hello"

print(type(greet))        # <class 'function'>
print(greet.__name__)     # greet

class MyClass:
    pass

print(type(MyClass))      # <class 'type'>
print(MyClass.__name__)   # MyClass
```

---

## Python's Object Model

Python supports key OOP principles:

| Principle | Description |
|-----------|-------------|
| **Encapsulation** | Objects bundle state (attributes) and behavior (methods) |
| **Inheritance** | Classes can inherit from other classes |
| **Polymorphism** | Same operator/method behaves differently by type |
| **Abstraction** | Implementation details hidden behind interfaces |

---

## Common Dunder Methods

"Dunder" = double underscore. These methods define object behavior:

| Method | Operator/Function |
|--------|-------------------|
| `__add__` | `+` |
| `__sub__` | `-` |
| `__mul__` | `*` |
| `__truediv__` | `/` |
| `__eq__` | `==` |
| `__lt__` | `<` |
| `__len__` | `len()` |
| `__str__` | `str()`, `print()` |
| `__repr__` | `repr()` |
| `__getitem__` | `obj[key]` |
| `__setitem__` | `obj[key] = value` |

---

## Key Takeaways

- **Everything in Python is an object** — int, str, list, function, class
- **Operators are method calls**: `a + b` → `a.__add__(b)`
- **Operator overloading**: Define `__add__` to customize `+` for your classes
- **Polymorphism**: Same operator behaves differently based on type
- **Type introspection**: Use `type()` to see any object's class
- Understanding Python's object model is fundamental to mastering the language
