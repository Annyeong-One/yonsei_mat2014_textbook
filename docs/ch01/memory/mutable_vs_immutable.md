# Mutable vs Immutable Objects

Python objects are either **mutable** or **immutable**. This distinction affects assignment, function calls, and correctness.

---

## 1. Immutable objects

Immutable objects cannot be changed after creation.

Examples:
- `int`, `float`, `bool`
- `str`, `tuple`

```python
x = 10
x += 1   # creates a new object
```

---

## 2. Mutable objects

Mutable objects can be changed in place.

Examples:
- `list`, `dict`, `set`

```python
xs = [1, 2]
xs.append(3)
```

---

## 3. Why it matters

Mutability affects:
- aliasing,
- function side effects,
- dictionary key validity.

Immutability provides safety and predictability.

---

## Key takeaways

- Immutable objects never change.
- Mutable objects can be modified in place.
- Mutability determines aliasing behavior.
