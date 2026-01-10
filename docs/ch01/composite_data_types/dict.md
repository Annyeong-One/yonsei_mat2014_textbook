# `dict` and Hash

A **dictionary** maps keys to values using a hash table. It is one of Python’s most powerful and widely used data types.

---

## Creating

```python
d = {"a": 1, "b": 2}
empty = {}
```

Keys must be hashable (immutable).

---

## Hash table semantics

Dictionary operations are:
- average O(1) for lookup, insert, delete,
- unordered historically, insertion-ordered since Python 3.7.

```python
d["c"] = 3
value = d["a"]
```

---

## Common patterns

```python
if "x" in d:
    print(d["x"])
```

Or safer:

```python
d.get("x", 0)
```

---

## Use cases

Dictionaries are used for:
- configurations,
- lookup tables,
- counters and caches.

They underpin much of Python’s standard library.

---

## Key takeaways

- Dictionaries are hash tables.
- Extremely fast lookups.
- Keys must be immutable.
