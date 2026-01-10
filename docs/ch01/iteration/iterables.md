# Iterables and

Iteration is a core concept in Python. Understanding **iterables** and **iterators** explains how `for` loops, comprehensions, and many built-ins work.

---

## Iterables

An **iterable** is any object that can be looped over.

Examples:
- lists, tuples, strings
- dictionaries
- sets
- files

Formally, an object is iterable if it implements `__iter__()`.

```python
iter([1, 2, 3])
```

---

## Iterators

An **iterator** is an object that:
- produces values one at a time,
- remembers its state,
- raises `StopIteration` when exhausted.

It implements:
- `__iter__()`
- `__next__()`

---

## Relationship between

```python
xs = [1, 2, 3]
it = iter(xs)
next(it)  # 1
next(it)  # 2
```

- The list is iterable.
- `it` is an iterator.

---

## Single-pass nature

Iterators are **consumed** as you iterate:

```python
list(it)   # remaining elements
list(it)   # empty
```

---

## Key takeaways

- Iterables can produce iterators.
- Iterators yield values lazily.
- Iterators are single-use.
