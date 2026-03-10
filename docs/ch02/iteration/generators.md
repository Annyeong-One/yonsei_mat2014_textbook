# Generators and `yield`


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Generators provide a concise way to create iterators using the `yield` keyword. They are central to Python's lazy evaluation model.

---

## Generator Functions

A function becomes a generator if it uses `yield`:

```python
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1
```

Calling it returns a generator object (not the result):

```python
g = count_up(3)
print(type(g))  # <class 'generator'>
```

---

## Execution Model

Generator execution **pauses** at each `yield` and **resumes** on `next()`:

```python
def my_gen():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")

g = my_gen()
print(next(g))  # Start → 1
print(next(g))  # Middle → 2
print(next(g))  # End → StopIteration
```

State (local variables, position) is preserved between yields.

---

## `yield` vs `return`

| Feature | `yield` | `return` |
|---------|---------|----------|
| Pauses execution | ✅ | ❌ (ends function) |
| Preserves state | ✅ | ❌ |
| Can be called multiple times | ✅ | ❌ |
| Creates generator | ✅ | ❌ |

```python
def with_yield():
    yield 1
    yield 2

def with_return():
    return 1
    return 2  # Never reached
```

---

## Generator Expressions

Similar to list comprehensions, but lazy:

```python
# List comprehension (eager)
squares_list = [x*x for x in range(10)]

# Generator expression (lazy)
squares_gen = (x*x for x in range(10))
```

Use parentheses `()` instead of brackets `[]`.

```python
g = (x**2 for x in range(5))
print(next(g))  # 0
print(next(g))  # 1
```

---

## Memory Efficiency

Generators compute values on demand, using minimal memory:

```python
import sys

# List stores all values
lst = [x for x in range(1000000)]
print(sys.getsizeof(lst))  # ~8 MB

# Generator stores only state
gen = (x for x in range(1000000))
print(sys.getsizeof(gen))  # ~200 bytes
```

---

## Memory Comparison

| Type | Memory | Stores All Values? |
|------|--------|-------------------|
| List comprehension | High | ✅ Yes |
| Generator expression | Very low | ❌ No |
| Generator function | Very low | ❌ No |
| Custom iterator | Low | ❌ No |

---

## Generator vs Iterator Class

**Generator** (concise):

```python
def squares(n):
    for i in range(n):
        yield i ** 2
```

**Iterator class** (verbose):

```python
class Squares:
    def __init__(self, n):
        self.n = n
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        result = self.i ** 2
        self.i += 1
        return result
```

Both produce the same values, but generators require less code.

---

## When to Use Generators

- Processing large files line by line
- Infinite sequences
- Data pipelines
- When you don't need all values at once

```python
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()
```

---

## Key Takeaways

- `yield` creates generators (pauses and resumes)
- Generators are lazy and memory-efficient
- Generator expressions use `()` syntax
- Essential for scalable data processing
- Generators are single-use (exhausted after iteration)
