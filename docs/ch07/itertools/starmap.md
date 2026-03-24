# starmap

`starmap()` applies a function to unpacked tuples from an iterable, similar to `map()` but with automatic argument unpacking. This is useful when your data arrives as pre-packed argument tuples — for example, from `zip()`, a database query, or a CSV reader — and you want to apply a multi-argument function to each without writing an explicit loop or lambda wrapper.

## Using starmap

Each element in the input iterable is unpacked as positional arguments to the function. This is equivalent to calling `func(*args)` for each `args` tuple in the iterable.

```python
from itertools import starmap
import operator

tuples = [(2, 3), (4, 5), (6, 7)]
results = list(starmap(operator.add, tuples))
print(results)
```

```
[5, 9, 13]
```

## starmap vs map

The key difference from the built-in `map()` is that `map()` passes each element as a single argument, while `starmap()` unpacks each element into separate positional arguments.

```python
from itertools import starmap

def power(base, exp):
    return base ** exp

data = [(2, 3), (3, 2), (5, 2)]

# starmap unpacks tuples
result1 = list(starmap(power, data))
print("starmap:", result1)

# map passes tuples as single arguments
try:
    result2 = list(map(power, data))
except TypeError as e:
    print(f"map error: {e}")
```

```
starmap: [8, 9, 25]
map error: power() missing 1 required positional argument: 'exp'
```
