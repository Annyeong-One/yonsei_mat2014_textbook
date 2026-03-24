# tee

`tee()` creates multiple independent iterators from a single iterable, useful when you need to iterate over the same data multiple times. Python iterators can only be traversed once — once exhausted, their data is gone. `tee()` solves this by creating independent copies that each maintain their own position, though it buffers consumed elements in memory until all copies have advanced past them.

## Creating Independent Iterators

After calling `tee()`, the original iterator should no longer be used directly. Each returned iterator independently yields all elements from the original source.

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

The second argument to `tee()` specifies the number of independent iterators to create. Each copy can be consumed independently for different computations.

```python
from itertools import tee

source = range(3)
it1, it2, it3 = tee(source, 3)

print("Sum:", sum(it1))
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
