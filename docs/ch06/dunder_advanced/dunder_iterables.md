# Iteration Protocol


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Iteration dunder methods enable objects to work with `for` loops, comprehensions, and other iteration contexts.

## The Iteration Protocol

```
for item in obj:
    ↓
obj.__iter__()  → returns iterator
    ↓
iterator.__next__()  → returns next value
iterator.__next__()  → returns next value
...
iterator.__next__()  → raises StopIteration
```

## __iter__: Making Objects Iterable

### Basic Iterator

```python
class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return CountdownIterator(self.start)

class CountdownIterator:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Usage
for n in Countdown(5):
    print(n, end=' ')  # 5 4 3 2 1 0
```

### Self-Iterating Class

For simple cases, the object can be its own iterator:

```python
class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high
    
    def __iter__(self):
        self.current = self.low
        return self
    
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Warning: Can only iterate once!
c = Counter(1, 3)
print(list(c))  # [1, 2, 3]
print(list(c))  # [] - exhausted!
```

### Separate Iterator (Reusable)

```python
class Range:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        # Return NEW iterator each time
        return RangeIterator(self.start, self.stop, self.step)

class RangeIterator:
    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

# Can iterate multiple times
r = Range(1, 5)
print(list(r))  # [1, 2, 3, 4]
print(list(r))  # [1, 2, 3, 4] - works again!
```

## Generator-Based __iter__

The simplest way to implement iteration:

```python
class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
    
    def __iter__(self):
        a, b = 0, 1
        while a < self.limit:
            yield a
            a, b = b, a + b

for n in Fibonacci(100):
    print(n, end=' ')  # 0 1 1 2 3 5 8 13 21 34 55 89
```

### Benefits of Generator __iter__

```python
class Lines:
    def __init__(self, filename):
        self.filename = filename
    
    def __iter__(self):
        with open(self.filename) as f:
            for line in f:
                yield line.strip()

# Memory efficient - processes one line at a time
# File automatically closed when iteration completes
# Can iterate multiple times
```

## __next__: Iterator Protocol

```python
class InfiniteCounter:
    """Infinite iterator that never raises StopIteration."""
    
    def __init__(self, start=0):
        self.value = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        current = self.value
        self.value += 1
        return current

counter = InfiniteCounter()
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2

# Use with islice to limit
from itertools import islice
print(list(islice(InfiniteCounter(10), 5)))  # [10, 11, 12, 13, 14]
```

## __reversed__: Reverse Iteration

```python
class Playlist:
    def __init__(self, songs):
        self._songs = list(songs)
    
    def __iter__(self):
        return iter(self._songs)
    
    def __reversed__(self):
        return iter(self._songs[::-1])
    
    def __len__(self):
        return len(self._songs)

songs = Playlist(['A', 'B', 'C', 'D'])

print("Forward:", list(songs))
# Forward: ['A', 'B', 'C', 'D']

print("Reversed:", list(reversed(songs)))
# Reversed: ['D', 'C', 'B', 'A']
```

### Generator-Based __reversed__

```python
class LinkedList:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node
    
    def __init__(self):
        self.head = None
    
    def prepend(self, value):
        self.head = self.Node(value, self.head)
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
    
    def __reversed__(self):
        # Collect and reverse (O(n) space)
        values = list(self)
        for value in reversed(values):
            yield value

ll = LinkedList()
for v in [1, 2, 3, 4]:
    ll.prepend(v)

print(list(ll))           # [4, 3, 2, 1]
print(list(reversed(ll))) # [1, 2, 3, 4]
```

## __getitem__ Fallback

If `__iter__` isn't defined, Python tries `__getitem__`:

```python
class OldStyleSequence:
    """Works with for loops via __getitem__."""
    
    def __init__(self, data):
        self._data = data
    
    def __getitem__(self, index):
        return self._data[index]

old = OldStyleSequence([1, 2, 3])
for item in old:
    print(item)  # Works! Calls __getitem__(0), __getitem__(1), etc.
```

## Iteration in Different Contexts

```python
class Numbers:
    def __init__(self, data):
        self._data = data
    
    def __iter__(self):
        return iter(self._data)

nums = Numbers([1, 2, 3, 4, 5])

# for loop
for n in nums:
    print(n)

# List comprehension
squares = [n**2 for n in nums]

# Generator expression
evens = (n for n in nums if n % 2 == 0)

# Unpacking
a, b, c, d, e = nums

# Built-in functions
print(sum(nums))      # 15
print(max(nums))      # 5
print(list(nums))     # [1, 2, 3, 4, 5]
print(tuple(nums))    # (1, 2, 3, 4, 5)
print(set(nums))      # {1, 2, 3, 4, 5}
print(sorted(nums, reverse=True))  # [5, 4, 3, 2, 1]

# in operator (uses __iter__ if no __contains__)
print(3 in nums)  # True

# any/all
print(any(n > 4 for n in nums))  # True
print(all(n > 0 for n in nums))  # True
```

## Practical Example: File-Like Iteration

```python
class CSVReader:
    """Iterate over CSV file as dictionaries."""
    
    def __init__(self, filename):
        self.filename = filename
    
    def __iter__(self):
        with open(self.filename) as f:
            headers = None
            for line in f:
                values = line.strip().split(',')
                if headers is None:
                    headers = values
                else:
                    yield dict(zip(headers, values))

# Usage
# for row in CSVReader('data.csv'):
#     print(row['name'], row['age'])
```

## Practical Example: Database-Like Iteration

```python
class QueryResult:
    """Iterate over query results with lazy loading."""
    
    def __init__(self, data, batch_size=100):
        self._data = data
        self._batch_size = batch_size
    
    def __iter__(self):
        for i in range(0, len(self._data), self._batch_size):
            batch = self._data[i:i + self._batch_size]
            for item in batch:
                yield item
    
    def __len__(self):
        return len(self._data)

# Simulated usage
results = QueryResult(list(range(1000)), batch_size=100)
for row in results:
    if row > 10:
        break
    print(row)
```

## Practical Example: Tree Traversal

```python
class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []
    
    def __iter__(self):
        """Pre-order traversal."""
        yield self.value
        for child in self.children:
            yield from child  # Recursive iteration
    
    def __reversed__(self):
        """Post-order traversal."""
        for child in reversed(self.children):
            yield from reversed(child)
        yield self.value

# Build tree:      1
#                / | \
#               2  3  4
#              / \
#             5   6

tree = TreeNode(1, [
    TreeNode(2, [TreeNode(5), TreeNode(6)]),
    TreeNode(3),
    TreeNode(4)
])

print("Pre-order:", list(tree))
# Pre-order: [1, 2, 5, 6, 3, 4]

print("Post-order:", list(reversed(tree)))
# Post-order: [4, 3, 6, 5, 2, 1]
```

## Async Iteration (__aiter__, __anext__)

For async contexts (Python 3.5+):

```python
class AsyncRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __aiter__(self):
        self.current = self.start
        return self
    
    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)  # Simulate async work
        value = self.current
        self.current += 1
        return value

# Usage
# async for n in AsyncRange(0, 5):
#     print(n)
```

## Iterator vs Iterable

```python
# Iterable: has __iter__, can be iterated multiple times
class Iterable:
    def __init__(self, data):
        self._data = data
    
    def __iter__(self):
        return iter(self._data)  # Returns NEW iterator

# Iterator: has __iter__ AND __next__, typically single-use
class Iterator:
    def __init__(self, data):
        self._data = data
        self._index = 0
    
    def __iter__(self):
        return self  # Returns SELF
    
    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration
        value = self._data[self._index]
        self._index += 1
        return value

# Testing
iterable = Iterable([1, 2, 3])
print(list(iterable))  # [1, 2, 3]
print(list(iterable))  # [1, 2, 3] - works again!

iterator = Iterator([1, 2, 3])
print(list(iterator))  # [1, 2, 3]
print(list(iterator))  # [] - exhausted!
```

## Using collections.abc

```python
from collections.abc import Iterator, Iterable

class MyIterator(Iterator):
    """Only need to implement __next__."""
    
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    
    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

# __iter__ is provided by Iterator ABC
it = MyIterator(3)
print(list(it))  # [1, 2, 3]
```

## Key Takeaways

- `__iter__` returns an iterator object
- `__next__` returns the next value or raises `StopIteration`
- Use generators in `__iter__` for simple cases
- Separate iterator classes allow multiple simultaneous iterations
- `__reversed__` enables custom `reversed()` behavior
- `__getitem__` provides fallback iteration if `__iter__` is missing
- Iterators are typically single-use; iterables can be reused
- Use `collections.abc` base classes for compliance
- `yield from` enables clean recursive iteration
