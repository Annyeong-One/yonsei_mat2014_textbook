# Infinite Iterators (count, cycle, repeat)

Infinite iterators generate an endless sequence of values. These are useful for creating infinite streams or repeating patterns that can be sliced or combined with other tools.

## count() - Infinite Counter

The `count()` function returns an iterator that generates numbers indefinitely starting from a given value and incrementing by a step.

```python
from itertools import count

# Count from 0 by default
counter = count()
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2

# Count from 10 with step 5
counter2 = count(10, 5)
print(list(next(counter2) for _ in range(4)))  # [10, 15, 20, 25]
```

```
0
1
2
[10, 15, 20, 25]
```

## cycle() - Infinite Cycle

The `cycle()` function repeats an iterable indefinitely, cycling through its elements.

```python
from itertools import cycle, islice

colors = ['red', 'green', 'blue']
color_cycle = cycle(colors)

# Take first 8 elements
result = list(islice(color_cycle, 8))
print(result)
```

```
['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green']
```

## repeat() - Infinite Repetition

The `repeat()` function repeats an element indefinitely or a specified number of times.

```python
from itertools import repeat

# Repeat indefinitely (limited by islice)
from itertools import islice
limited = list(islice(repeat('x'), 5))
print(limited)

# Repeat specific number of times
limited2 = list(repeat('hello', 3))
print(limited2)
```

```
['x', 'x', 'x', 'x', 'x']
['hello', 'hello', 'hello']
```

