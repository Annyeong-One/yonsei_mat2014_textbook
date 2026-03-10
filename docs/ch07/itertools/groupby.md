# groupby


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

`groupby()` groups consecutive elements with the same key, making it useful for processing sorted data.

## Basic Grouping

Group consecutive identical elements.

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

## Grouping with Key Function

Use a key function to determine grouping criteria.

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

