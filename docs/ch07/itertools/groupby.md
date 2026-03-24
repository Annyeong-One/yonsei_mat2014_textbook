# groupby

`groupby()` groups consecutive elements with the same key, making it useful for processing sorted data. Unlike SQL-style GROUP BY or `pandas.groupby`, this function only groups elements that are adjacent in the input sequence. To group all matching elements together, sort the input by the key first. This iterator-based approach works well for streaming data where items arrive in order.

## Basic Grouping

Without a key function, `groupby()` groups consecutive elements that are equal. Note that the trailing `1` in the example forms its own group because it is separated from the earlier `1`s by other values.

```python
from itertools import groupby

data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1]
grouped = groupby(data)

for key, group in grouped:
    print(f"{key}: {list(group)}")
```

```
1: [1, 1, 1]
2: [2, 2]
3: [3, 3, 3, 3]
1: [1]
```

The trailing `1` appears as a separate group because `groupby()` only groups consecutive elements. To group all `1`s together, sort the data first.

## Grouping with Key Function

A key function maps each element to a grouping value. `groupby()` starts a new group whenever the key value changes, so the input should be sorted by the same key for exhaustive grouping.

```python
from itertools import groupby

words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
# Group by first letter
grouped = groupby(words, key=lambda x: x[0])

for letter, items in grouped:
    print(f"{letter}: {list(items)}")
```

```
a: ['apple', 'apricot']
b: ['banana', 'blueberry']
c: ['cherry']
```
