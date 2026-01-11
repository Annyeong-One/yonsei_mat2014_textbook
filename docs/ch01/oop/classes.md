# Class Definition

Classes define **custom types** in Python. An instance is a concrete object created from a class.

---

## Defining a Class

```python
class Point:
    pass
```

This defines a new class named `Point`.

---

## Creating Instances

```python
p = Point()
```

- `Point` is the class
- `p` is an instance

Each instance has its own identity.

---

## Dynamic Attributes

```python
p.x = 1
p.y = 2
```

Python allows dynamic attribute creation, though it should be used carefully.

---

## Why Classes Matter

Classes allow:
- encapsulation of data and behavior,
- abstraction,
- reusable and maintainable code.

They are fundamental for large systems.

---

## Key Takeaways

- Classes define new types.
- Instances are concrete objects.
- Attributes belong to instances or classes.
