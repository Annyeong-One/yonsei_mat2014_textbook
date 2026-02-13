# permutations and combinations

These functions generate all permutations (order matters) and combinations (order doesn't matter) from an iterable.

## permutations() - Order Matters

Generate all ordered arrangements of elements.

```python
from itertools import permutations

items = [1, 2, 3]
perms = list(permutations(items, 2))
print(perms)
print(f"Count: {len(perms)}")
```

```
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
Count: 6
```

## combinations() - Order Doesn't Matter

Generate all unique unordered subsets of elements.

```python
from itertools import combinations

items = [1, 2, 3, 4]
combos = list(combinations(items, 2))
print(combos)
print(f"Count: {len(combos)}")
```

```
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
Count: 6
```

## combinations_with_replacement()

Generate combinations where elements can be repeated.

```python
from itertools import combinations_with_replacement

items = ['A', 'B', 'C']
combos = list(combinations_with_replacement(items, 2))
print(combos)
```

```
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
```

