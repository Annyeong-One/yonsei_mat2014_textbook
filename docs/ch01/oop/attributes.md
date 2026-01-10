# `__init__` and Attribute Lookup

The `__init__` method initializes new objects. Attribute lookup follows a well-defined order.

---

## 1. The `__init__` method

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

`__init__` runs immediately after object creation.

---

## 2. Attribute lookup order

When accessing `obj.attr`, Python searches:
1. Instance dictionary
2. Class dictionary
3. Base classes (via MRO)

```python
p = Point(1, 2)
p.x
```

---

## 3. Class vs instance attributes

```python
class A:
    v = 10

a = A()
a.v      # 10
```

Instance attributes override class attributes.

---

## Key takeaways

- `__init__` initializes instances.
- Attribute lookup follows instance → class → bases.
- Class attributes are shared.
