# chain and chain.from_iterable

The `chain()` function concatenates multiple iterables into a single iterator, while `chain.from_iterable()` accepts an iterable of iterables.

## chain() - Concatenate Iterables

The `chain()` function combines multiple iterables sequentially.

```python
from itertools import chain

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [10, 20]

result = list(chain(list1, list2, list3))
print(result)
```

```
[1, 2, 3, 'a', 'b', 'c', 10, 20]
```

## chain.from_iterable() - Flatten Iterables

When you have a list of lists, use `from_iterable()` to flatten the structure.

```python
from itertools import chain

lists = [[1, 2], [3, 4], [5, 6]]
result = list(chain.from_iterable(lists))
print(result)

# Flatten a generator expression
nested = ([i, i+10] for i in range(3))
flattened = list(chain.from_iterable(nested))
print(flattened)
```

```
[1, 2, 3, 4, 5, 6]
[0, 10, 1, 11, 2, 12]
```

