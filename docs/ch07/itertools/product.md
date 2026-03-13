# product - Cartesian Product

The `product()` function computes the Cartesian product of input iterables, generating all possible combinations.

## Basic Cartesian Product

Generate all combinations of elements from multiple iterables.

```python
from itertools import product

colors = ['red', 'green']
sizes = ['S', 'M', 'L']

combinations = list(product(colors, sizes))
print(combinations)
```

```
[('red', 'S'), ('red', 'M'), ('red', 'L'), ('green', 'S'), ('green', 'M'), ('green', 'L')]
```

## Multiple Iterables and Repeat

Use the `repeat` parameter to generate products with itself.

```python
from itertools import product

# Pairs from a single iterable
pairs = list(product([1, 2, 3], repeat=2))
print(pairs)

# Self-product with 3 iterations
triples = list(product('AB', repeat=3))
print(triples)
```

```
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
[('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'B', 'A'), ('A', 'B', 'B'), ('B', 'A', 'A'), ('B', 'A', 'B'), ('B', 'B', 'A'), ('B', 'B', 'B')]
```

