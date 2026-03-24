# takewhile and dropwhile

`takewhile()` returns elements while a condition is True, while `dropwhile()` skips elements while a condition is True, then yields all remaining elements. These functions operate on the leading portion of a sequence based on a predicate, making them especially useful for sorted or ordered data and for lazy evaluation over potentially infinite iterators.

## takewhile() - Take While Condition is True

`takewhile()` yields elements from the start of the iterable as long as the predicate returns `True`. It stops permanently at the first element that fails the predicate, even if later elements would pass.

```python
from itertools import takewhile

numbers = [1, 2, 3, 4, 5, 3, 2, 1]

# Take while less than 4
result = list(takewhile(lambda x: x < 4, numbers))
print(result)
```

```
[1, 2, 3]
```

## dropwhile() - Drop While Condition is True

`dropwhile()` discards elements from the start of the iterable as long as the predicate returns `True`. Once the predicate returns `False` for the first time, it yields that element and all subsequent elements unconditionally.

```python
from itertools import dropwhile

numbers = [1, 2, 3, 4, 5, 3, 2, 1]

# Drop while less than 4
result = list(dropwhile(lambda x: x < 4, numbers))
print(result)

# Practical: skip whitespace at start
lines = ['  ', '  ', 'content', 'more']
content = list(dropwhile(str.isspace, lines))
print(content)
```

```
[4, 5, 3, 2, 1]
['content', 'more']
```
