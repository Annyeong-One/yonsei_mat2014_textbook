# `__init__` and Lookup

The `__init__` method initializes new objects. Attribute lookup follows a well-defined order.

---

## The `__init__` Method

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

`__init__` runs immediately after object creation.

---

## Attribute Lookup Order

When accessing `obj.attr`, Python searches:

### 1. Instance Dictionary

```python
p = Point(1, 2)
p.x  # searches instance first
```

### 2. Class Dictionary

```python
class A:
    v = 10

a = A()
a.v  # found in class
```

### 3. Base Classes (MRO)

```python
class Parent:
    x = 1

class Child(Parent):
    pass

c = Child()
c.x  # found in Parent
```

---

## Class vs Instance

```python
class A:
    v = 10

a = A()
a.v = 20  # creates instance attribute
```

Instance attributes override class attributes.

---

## Key Takeaways

- `__init__` initializes instances.
- Attribute lookup follows instance → class → bases.
- Class attributes are shared across instances.
