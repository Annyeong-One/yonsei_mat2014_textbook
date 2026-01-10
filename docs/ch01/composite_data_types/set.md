# `set` and Membership

A **set** is an unordered collection of unique elements, implemented using a hash table.

---

## Creating sets

```python
s = {1, 2, 3}
empty = set()
```

Duplicate elements are automatically removed.

---

## Membership testing

Sets excel at membership checks:

```python
x in s
```

This is O(1) on average.

---

## Set operations

```python
a | b   # union
a & b   # intersection
a - b   # difference
```

These operations are concise and expressive.

---

## Use cases

Sets are ideal for:
- removing duplicates,
- fast membership tests,
- mathematical set operations.

---

## Key takeaways

- Sets store unique elements.
- Extremely fast membership checks.
- Support mathematical set operations.
