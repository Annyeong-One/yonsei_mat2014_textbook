# zip_longest

When combining iterables of unequal length, Python's built-in `zip()` silently truncates to the shortest input — which can cause data loss. `zip_longest()` from the `itertools` module solves this by continuing until every iterable is exhausted, filling in a default value for the shorter ones.

## Zipping Different Length Iterables

The following example pairs a 3-element list with a 5-element list. The `fillvalue` parameter specifies what to substitute for the missing entries in the shorter iterable.

```python
from itertools import zip_longest

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

result = list(zip_longest(list1, list2, fillvalue='*'))
print(result)
```

```text
[(1, 'a'), (2, 'b'), (3, 'c'), ('*', 'd'), ('*', 'e')]
```

## Custom Fill Value

The default fill value is `None`, but you can pass any object via the `fillvalue` parameter. This is especially useful when the fill value must be meaningful in downstream processing — for example, using `'N/A'` for missing names.

```python
from itertools import zip_longest

names = ['Alice', 'Bob']
scores = [95, 87, 92, 88]

result = list(zip_longest(names, scores, fillvalue='N/A'))
for name, score in result:
    print(f"{name}: {score}")
```

```text
Alice: 95
Bob: 87
N/A: 92
N/A: 88
```
