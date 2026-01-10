# `tuple` and Immutability

A **tuple** is an ordered, immutable collection. Tuples are fundamental to Python’s design and are widely used for safety and performance.

---

## 1. Creating tuples

```python
t = (1, 2, 3)
empty = ()
single = (42,)   # comma required
```

Without the comma, `(42)` is just an integer.

---

## 2. Immutability

Tuples cannot be modified after creation:

```python
t = (1, 2, 3)
# t[0] = 10   # TypeError
```

Immutability provides:
- safety against accidental mutation,
- suitability as dictionary keys,
- predictable behavior.

---

## 3. Access and unpacking

```python
x, y = (10, 20)
```

Tuple unpacking is common in:
- function returns,
- loops,
- multiple assignment.

---

## 4. Performance considerations

Compared to lists:
- tuples use less memory,
- access is slightly faster,
- creation is cheaper.

Use tuples for fixed-size, read-only data.

---

## Key takeaways

- Tuples are immutable sequences.
- They are lightweight and safe.
- Ideal for fixed records and keys.
