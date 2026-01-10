# Class Definition and Instances

Classes define **custom types** in Python. An instance is a concrete object created from a class.

---

## 1. Defining a class

```python
class Point:
    pass
```

This defines a new class named `Point`.

---

## 2. Creating instances

```python
p = Point()
```

- `Point` is the class
- `p` is an instance

Each instance has its own identity.

---

## 3. Adding attributes dynamically

```python
p.x = 1
p.y = 2
```

Python allows dynamic attribute creation, though it should be used carefully.

---

## 4. Why classes matter

Classes allow:
- encapsulation of data and behavior,
- abstraction,
- reusable and maintainable code.

They are fundamental for large systems.

---

## Key takeaways

- Classes define new types.
- Instances are concrete objects.
- Attributes belong to instances or classes.
