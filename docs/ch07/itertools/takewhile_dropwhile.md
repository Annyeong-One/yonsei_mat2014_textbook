# takewhile and dropwhile

`takewhile()` returns elements while a condition is True, while `dropwhile()` skips elements until a condition becomes True.

## takewhile() - Take While Condition is True

Extract leading elements that satisfy a condition.

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

Skip leading elements that satisfy a condition.

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

