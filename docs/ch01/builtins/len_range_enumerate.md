# `len()`, `range()`,


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

These built-in functions appear everywhere in Python code:
- `len()` tells you *how many* items are in a container.
- `range()` generates integer sequences (commonly for loops).
- `enumerate()` loops over items *with their indices*.

---

## `len()`

### 1. What it does

`len(x)` returns the number of elements in a container-like object.

```python
len([10, 20, 30])          # 3
len("quant")               # 5
len({"a": 1, "b": 2})      # 2  (number of keys)
```

### 2. Common uses

```python
items = ["a", "b", "c"]
if len(items) == 0:
    print("empty")
```

---

## `range()`

### 1. Basic forms

- `range(stop)` → `0, 1, ..., stop-1`
- `range(start, stop)` → `start, ..., stop-1`
- `range(start, stop, step)` → step can be negative

```python
list(range(5))            # [0, 1, 2, 3, 4]
list(range(2, 6))         # [2, 3, 4, 5]
list(range(10, 0, -2))    # [10, 8, 6, 4, 2]
```

> Note: `range()` is *lazy* (it doesn’t create a full list unless you ask).

### 2. Typical loop

```python
for i in range(3):
    print(i)
```

### 3. Using range with

```python
xs = [10, 20, 30]
for i in range(len(xs)):
    print(i, xs[i])
```

This works, but `enumerate()` is often cleaner.

---

## `enumerate()`

### 1. Why it’s useful

`enumerate(iterable)` produces pairs `(index, value)`.

```python
xs = [10, 20, 30]
for i, x in enumerate(xs):
    print(i, x)
# 0 10
# 1 20
# 2 30
```

### 1. Starting from a Different Index

```python
for i, x in enumerate(xs, start=1):
    print(i, x)
# 1 10
# 2 20
# 3 30
```

### 1. Common pattern:

```python
s = "finance"
for i, ch in enumerate(s):
    if ch == "a":
        print("found at", i)
```

---

## Key takeaways

- `len()` gives the size of a container.
- `range()` is a lazy sequence of integers (great for loops).
- `enumerate()` is the cleanest way to loop with indices.
