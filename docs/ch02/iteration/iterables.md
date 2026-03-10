# Iterables and Iterators


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

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
- `__iter__()` — returns itself
- `__next__()` — returns next value

---

## Iterable vs Iterator

| Feature | Iterable | Iterator |
|---------|----------|----------|
| Has `__iter__()` | ✅ | ✅ |
| Has `__next__()` | ❌ | ✅ |
| Can use in `for` | ✅ | ✅ |
| Can call `next()` | ❌ (need `iter()`) | ✅ |

```python
nums = [1, 2, 3]           # Iterable
it = iter(nums)            # Iterator

print("__iter__" in dir(nums))  # True
print("__next__" in dir(nums))  # False
print("__next__" in dir(it))    # True
```

---

## How `for` Loop Works

When you write:

```python
for x in [1, 2, 3]:
    print(x)
```

Python does this internally:

```python
it = iter([1, 2, 3])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
```

---

## Built-in Iterators

These functions return **iterators** (lazy evaluation):

| Function | Description |
|----------|-------------|
| `zip()` | Pairs elements from multiple iterables |
| `enumerate()` | Pairs index with element |
| `map()` | Applies function to each element |
| `filter()` | Filters elements by predicate |
| `reversed()` | Reverses a sequence |

```python
# All return iterators
z = zip([1, 2], ['a', 'b'])
e = enumerate(['x', 'y'])
m = map(str.upper, ['a', 'b'])
f = filter(lambda x: x > 0, [-1, 2, 3])

print(next(z))  # (1, 'a')
print(next(e))  # (0, 'x')
print(next(m))  # 'A'
print(next(f))  # 2
```

---

## Custom Iterator

Create your own iterator by implementing the protocol:

```python
class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

for n in CountUp(3):
    print(n)  # 1, 2, 3
```

---

## Single-pass Nature

Iterators are **consumed** as you iterate:

```python
it = iter([1, 2, 3])
list(it)   # [1, 2, 3]
list(it)   # [] (exhausted)
```

---

## Key Takeaways

- **Iterables** can produce iterators via `iter()`
- **Iterators** yield values lazily via `next()`
- Iterators are single-use
- `for` loop uses `iter()` and `next()` internally
- `zip`, `map`, `filter`, `enumerate` return iterators
