# chain and chain.from_iterable

The `chain()` function concatenates multiple iterables into a single iterator, while `chain.from_iterable()` accepts an iterable of iterables. These tools let you process items from several sources as a single stream without copying them into a new collection, preserving memory efficiency and keeping code concise.

## chain() - Concatenate Iterables

Pass any number of iterables as separate arguments to `chain()`. It yields elements from the first iterable until it is exhausted, then proceeds to the next, and so on.

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

Unlike `chain()`, which requires each iterable as a separate argument, `chain.from_iterable()` accepts a single iterable of iterables. This is essential when the sub-iterables come from a generator or when their count is not known in advance.

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
