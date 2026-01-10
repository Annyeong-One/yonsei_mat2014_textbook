# `list` and Dynamic

A **list** is an ordered, mutable collection backed by a dynamic array. Lists are the most commonly used data structure in Python.

---

## Creating lists

```python
xs = [1, 2, 3]
empty = []
```

Lists can contain mixed types, but this is usually discouraged in practice.

---

## Mutability

Lists can grow and change:

```python
xs.append(4)
xs[0] = 10
```

This flexibility makes lists extremely useful.

---

## Dynamic array

Internally, Python lists:
- allocate extra capacity,
- resize occasionally,
- provide amortized O(1) append.

Random access is O(1).

---

## Common operations

```python
xs.append(5)
xs.pop()
xs.extend([6, 7])
```

Insertion in the middle is O(n).

---

## Key takeaways

- Lists are mutable dynamic arrays.
- Fast indexing and appends.
- Avoid frequent middle insertions for performance.
