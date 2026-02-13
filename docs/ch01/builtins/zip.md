# zip()

The zip() function combines multiple iterables into tuples, pairing corresponding elements. It's essential for iterating over multiple sequences simultaneously and is particularly useful for parallel processing and data alignment.

---

## Basic zip() Usage

### Zipping Two Lists

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

Output:
```
Alice: 25
Bob: 30
Charlie: 35
```

### Creating a Dictionary

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]

d = dict(zip(keys, values))
print(d)
```

Output:
```
{'a': 1, 'b': 2, 'c': 3}
```

## Handling Different Lengths

### Default Behavior (Stops at Shortest)

```python
short = [1, 2]
long = ["a", "b", "c", "d"]

result = list(zip(short, long))
print(result)
```

Output:
```
[(1, 'a'), (2, 'b')]
```

### Using itertools.zip_longest

```python
from itertools import zip_longest

short = [1, 2]
long = ["a", "b", "c", "d"]

result = list(zip_longest(short, long, fillvalue=None))
print(result)
```

Output:
```
[(1, 'a'), (2, 'b'), (None, 'c'), (None, 'd')]
```

## Multiple Sequences

### Zipping Three or More Iterables

```python
ids = [1, 2, 3]
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

for id, name, score in zip(ids, names, scores):
    print(f"{id}. {name}: {score}")
```

Output:
```
1. Alice: 95
2. Bob: 87
3. Charlie: 92
```

## Practical Applications

### Transposing a Matrix

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(zip(*matrix))
print(transposed)
```

Output:
```
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

### Parallel Processing

```python
numbers = [1, 2, 3, 4]
multipliers = [10, 20, 30, 40]

products = [x * y for x, y in zip(numbers, multipliers)]
print(products)
```

Output:
```
[10, 40, 90, 160]
```
