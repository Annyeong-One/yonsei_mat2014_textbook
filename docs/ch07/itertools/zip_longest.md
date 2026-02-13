# zip_longest

`zip_longest()` zips iterables of different lengths, filling missing values with a specified default.

## Zipping Different Length Iterables

Unlike regular `zip()`, `zip_longest()` continues until all iterables are exhausted.

```python
from itertools import zip_longest

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

result = list(zip_longest(list1, list2, fillvalue='*'))
print(result)
```

```
[(1, 'a'), (2, 'b'), (3, 'c'), ('*', 'd'), ('*', 'e')]
```

## Custom Fill Value

Use any value to fill missing entries.

```python
from itertools import zip_longest

names = ['Alice', 'Bob']
scores = [95, 87, 92, 88]

result = list(zip_longest(names, scores, fillvalue='N/A'))
for name, score in result:
    print(f"{name}: {score}")
```

```
Alice: 95
Bob: 87
N/A: 92
N/A: 88
```

