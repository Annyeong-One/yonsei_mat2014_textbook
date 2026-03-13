# itertools Recipes

Common utility functions built from itertools primitives, providing elegant solutions to frequent programming tasks.

## flatten() - Flatten Nested Iterables

Flatten a list of lists into a single sequence.

```python
from itertools import chain

def flatten(list_of_lists):
    return chain.from_iterable(list_of_lists)

data = [[1, 2], [3, 4], [5, 6]]
result = list(flatten(data))
print(result)
```

```
[1, 2, 3, 4, 5, 6]
```

## roundrobin() - Interleave Iterables

Take elements from each iterable in turn.

```python
from itertools import cycle, chain

def roundrobin(*iterables):
    pending = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(iter(it).__next__ for it in iterables)

result = list(roundrobin('ABC', 'D', 'EF'))
print(result)
```

```
['A', 'D', 'E', 'B', 'F', 'C']
```

## partition() - Separate Elements by Predicate

Partition an iterable into two based on a condition.

```python
from itertools import tee

def partition(pred, iterable):
    t1, t2 = tee(iterable)
    return (filter(pred, t1), filterfalse(pred, t2))

from itertools import filterfalse
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens, odds = partition(lambda x: x % 2 == 0, numbers)
print("Evens:", list(evens))
print("Odds:", list(odds))
```

```
Evens: [2, 4, 6, 8]
Odds: [1, 3, 5, 7]
```

