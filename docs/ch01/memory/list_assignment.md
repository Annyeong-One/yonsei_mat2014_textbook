# List Assignment and Aliasing

Lists are mutable, so assignment can easily lead to **aliasing bugs** if misunderstood.

---

## 1. Aliasing example

```python
a = [1, 2, 3]
b = a
b.append(4)
```

Now:
```python
a  # [1, 2, 3, 4]
```

Both names refer to the same list.

---

## 2. Copying lists

To create a copy:

```python
b = a.copy()
# or
b = a[:]
```

Now modifications are independent.

---

## 3. Nested lists

Shallow copies do not copy nested objects:

```python
x = [[1], [2]]
y = x.copy()
y[0].append(99)
```

Both `x` and `y` are affected.

---

## Key takeaways

- Assignment creates aliases.
- Use `.copy()` for independent lists.
- Beware of shallow vs deep copies.
