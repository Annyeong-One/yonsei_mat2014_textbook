# `__init__` and

The `__init__` method initializes new objects. Attribute lookup follows a well-defined order.

---

## The `__init__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

`__init__` runs immediately after object creation.

---

## Attribute lookup

When accessing `obj.attr`, Python searches:
1. Instance dictionary
2. Class dictionary
3. Base classes (via MRO)

```python
p = Point(1, 2)
p.x
```

---

## Class vs instance

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
