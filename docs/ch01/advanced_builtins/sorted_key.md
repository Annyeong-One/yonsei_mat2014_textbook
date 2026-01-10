# `key=` Functions and Custom Ordering

The `key` argument allows precise control over sorting and ordering operations.

---

## 1. Basic usage

```python
xs = ["aaa", "b", "cc"]
sorted(xs, key=len)
```

Elements are ordered by `len(x)`.

---

## 2. Sorting complex objects

```python
data = [("AAPL", 180), ("GOOG", 130)]
sorted(data, key=lambda x: x[1])
```

This sorts by price.

---

## 3. Stability of sorting

Python’s sorting is **stable**:
- equal keys preserve original order.

This enables multi-stage sorting.

---

## 4. Custom ordering logic

The `key` function should:
- be fast,
- return comparable values,
- avoid side effects.

---

## Key takeaways

- `key` controls how elements are compared.
- Sorting is stable.
- Prefer `key` over custom comparison functions.
