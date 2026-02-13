# Iterator Chaining

Iterator chaining combines multiple iterators or transformation functions into a pipeline. The itertools module provides powerful tools for creating complex iteration patterns with minimal memory overhead.

---

## Basic Chaining

### Composing Generators

```python
def add_one(iterable):
    for value in iterable:
        yield value + 1

def double(iterable):
    for value in iterable:
        yield value * 2

numbers = range(1, 4)
result = double(add_one(numbers))
print(list(result))
```

Output:
```
[4, 6, 8]
```

### Iterator Chaining Order

```python
numbers = [1, 2, 3]

# Different order, different result
result1 = double(add_one(numbers))
result2 = add_one(double(numbers))

print(f"Add then double: {list(result1)}")
print(f"Double then add: {list(result2)}")
```

Output:
```
Add then double: [4, 6, 8]
Double then add: [3, 5, 7]
```

## itertools Chains

### Chaining Iterables

```python
from itertools import chain

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

combined = chain(list1, list2, list3)
print(list(combined))
```

Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Chain from Iterable

```python
from itertools import chain

nested = [[1, 2], [3, 4], [5, 6]]
flattened = chain.from_iterable(nested)
print(list(flattened))
```

Output:
```
[1, 2, 3, 4, 5, 6]
```

## Complex Pipelines

### Multi-Step Processing

```python
from itertools import filter, map

numbers = range(1, 11)
result = filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers))
print(list(result))
```

Output:
```
[4, 16, 36, 64, 100]
```

### Real-World Example

```python
import itertools

def read_lines():
    data = ["hello world", "foo bar", "test data"]
    for line in data:
        yield line

def split_words(lines):
    for line in lines:
        yield from line.split()

def uppercase(words):
    for word in words:
        yield word.upper()

pipeline = uppercase(split_words(read_lines()))
print(list(pipeline))
```

Output:
```
['HELLO', 'WORLD', 'FOO', 'BAR', 'TEST', 'DATA']
```
