# tee


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

`tee()` creates multiple independent iterators from a single iterable, useful when you need to iterate over the same data multiple times.

## Creating Independent Iterators

Use `tee()` to create multiple copies of an iterator.

```python
from itertools import tee

data = [1, 2, 3, 4, 5]
it1, it2 = tee(iter(data), 2)

print("Iterator 1:", list(it1))
print("Iterator 2:", list(it2))
```

```
Iterator 1: [1, 2, 3, 4, 5]
Iterator 2: [1, 2, 3, 4, 5]
```

## Multiple Independent Iterations

Create more than two independent iterators.

```python
from itertools import tee

source = range(3)
it1, it2, it3 = tee(source, 3)

# Process different parts with different iterators
print("Sum:", sum(it1))
print("Product:", 1)
for val in it2:
    print(f"Value: {val}")
print("Doubled:", list(2*x for x in it3))
```

```
Sum: 3
Value: 0
Value: 1
Value: 2
Doubled: [0, 2, 4]
```

