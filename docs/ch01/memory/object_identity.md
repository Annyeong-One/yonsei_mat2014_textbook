# Object Identity and

In Python, variables do not store values directly. They store **references** to objects. Understanding identity is crucial for correct reasoning about programs.

---

## Identity vs value

Every object has:
- **identity**: its memory address (conceptually),
- **value**: the data it represents,
- **type**.

```python
x = 10
id(x)
```

`id(x)` uniquely identifies the object during its lifetime.

---

## Names and bindings

```python
a = 10
b = a
```

- `a` and `b` refer to the *same object*.
- No copying occurs.

---

## Equality vs identity

```python
a == b   # value equality
a is b   # identity equality
```

Use:
- `==` for value comparison,
- `is` for identity (e.g. with `None`).

---

## Key takeaways

- Variables are references to objects.
- Identity (`is`) differs from equality (`==`).
- Multiple names can reference the same object.
