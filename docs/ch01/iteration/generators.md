# Generators and `yield`

Generators provide a concise way to create iterators using the `yield` keyword. They are central to Python’s lazy evaluation model.

---

## 1. Generator functions

A function becomes a generator if it uses `yield`:

```python
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1
```

Calling it returns a generator object.

---

## 2. Execution model

- Execution pauses at `yield`.
- State is saved.
- Resumes on next iteration.

```python
g = count_up(3)
next(g)  # 0
next(g)  # 1
```

---

## 3. Memory efficiency

Generators:
- do not store all values,
- compute values on demand,
- are ideal for large or infinite sequences.

---

## 4. Generator expressions

Similar to list comprehensions, but lazy:

```python
squares = (x*x for x in range(10))
```

---

## Key takeaways

- `yield` creates generators.
- Generators are lazy and memory-efficient.
- Essential for scalable data processing.
