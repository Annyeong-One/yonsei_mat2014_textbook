# `map()`, `filter()`, and `sorted()`

These higher-order built-in functions apply operations to collections in a functional style.

---

## 1. `map()`

Applies a function to each element:

```python
xs = [1, 2, 3]
ys = list(map(lambda x: x * 2, xs))
```

Equivalent to a list comprehension:

```python
ys = [x * 2 for x in xs]
```

---

## 2. `filter()`

Keeps elements for which a predicate is true:

```python
xs = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, xs))
```

Equivalent to:

```python
evens = [x for x in xs if x % 2 == 0]
```

---

## 3. `sorted()`

Returns a new sorted list:

```python
sorted([3, 1, 2])
```

Works on any iterable and does not modify the original.

---

## 4. Pythonic style

List comprehensions are often clearer, but `map` and `filter` are useful when:
- composing functions,
- avoiding intermediate lists,
- expressing intent clearly.

---

## Key takeaways

- `map` transforms elements.
- `filter` selects elements.
- `sorted` returns a new ordered list.
