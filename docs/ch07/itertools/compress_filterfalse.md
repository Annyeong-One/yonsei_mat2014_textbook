# compress and filterfalse

`compress()` filters based on a selector iterable, while `filterfalse()` keeps elements where the predicate is False.

## compress() - Filter with Selectors

Keep elements where corresponding selector is True.

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

Keep elements where the predicate returns False.

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

