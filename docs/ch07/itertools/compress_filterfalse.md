# compress and filterfalse

`compress()` filters based on a selector iterable, while `filterfalse()` keeps elements where the predicate is False. Use `compress()` when you have a precomputed boolean mask from a separate computation, and `filterfalse()` when you need the complement of the built-in `filter()` — that is, the elements that fail a predicate test.

## compress() - Filter with Selectors

`compress()` pairs each element in a data iterable with a corresponding value in a selector iterable and yields only those elements whose selector is truthy. This is similar to applying a boolean mask to a sequence.

```python
from itertools import compress

data = ['a', 'b', 'c', 'd', 'e']
selectors = [1, 0, 1, 0, 1]

result = list(compress(data, selectors))
print(result)
```

```
['a', 'c', 'e']
```

## filterfalse() - Inverse Filter

`filterfalse()` is the complement of the built-in `filter()`. While `filter()` keeps elements for which the predicate returns `True`, `filterfalse()` keeps elements for which it returns `False`.

```python
from itertools import filterfalse

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Keep even numbers using filterfalse
evens = list(filterfalse(lambda x: x % 2, numbers))
print("Evens:", evens)

# Keep short words
words = ['cat', 'elephant', 'dog', 'bird', 'butterfly']
short = list(filterfalse(lambda w: len(w) > 4, words))
print("Short words:", short)
```

```
Evens: [2, 4, 6, 8]
Short words: ['cat', 'dog', 'bird']
```
