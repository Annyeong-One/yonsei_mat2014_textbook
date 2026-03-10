# starmap


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

`starmap()` applies a function to unpacked tuples from an iterable, similar to map but unpacks arguments.

## Using starmap

Apply a function by unpacking tuple arguments.

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

Understand the difference between starmap and regular map.

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

