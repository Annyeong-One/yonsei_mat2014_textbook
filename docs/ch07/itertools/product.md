# product - Cartesian Product

The `product()` function computes the Cartesian product of input iterables, generating all ordered tuples by selecting one element from each iterable. It replaces nested for-loops with a single flat iterator, producing more concise code and avoiding deep indentation when iterating over multiple dimensions.

## Basic Cartesian Product

Pass two or more iterables to `product()` and it yields every possible ordered tuple containing one element from each. This is equivalent to nested for-loops but expressed as a single flat iterator.

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

The `repeat` parameter specifies how many times the input iterable is repeated in the product. `product(A, repeat=3)` is equivalent to `product(A, A, A)`.

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
