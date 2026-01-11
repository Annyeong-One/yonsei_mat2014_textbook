# Iterable Protocol

The iterable protocol enables objects to work with loops, comprehensions, and iteration-based operations.

---

## Iterable vs Iterator

### 1. Iterable

```python
class MyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return MyRangeIterator(self.start, self.stop)

r = MyRange(0, 5)
for i in r:  # Iterable
    print(i)
```

Has `__iter__()` that returns an iterator.

### 2. Iterator

```python
class MyRangeIterator:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
```

Has both `__iter__()` and `__next__()`.

### 3. Key Difference

- **Iterable**: can be looped over
- **Iterator**: manages iteration state

---

## Protocol Requirements

### 1. Iterable Protocol

```python
def __iter__(self):
    # Return an iterator
    return SomeIterator()
```

Must return an object with `__next__()`.

### 2. Iterator Protocol

```python
def __iter__(self):
    return self

def __next__(self):
    # Return next value or raise StopIteration
    pass
```

Must have both methods.

### 3. Flow Diagram

```
for x in iterable:
    # 1. Call iterable.__iter__() → get iterator
    # 2. Call iterator.__next__() repeatedly
    # 3. Stop when StopIteration raised
```

---

## Simple Iterator

### 1. Combined Approach

```python
class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        value = self.start
        self.start -= 1
        return value

for i in Countdown(5):
    print(i)  # 5, 4, 3, 2, 1
```

### 2. Problem: Single Use

```python
c = Countdown(3)
list(c)  # [3, 2, 1]
list(c)  # [] - exhausted!
```

### 3. Stateful Object

Iterator modifies itself—can't reuse.

---

## Separated Design

### 1. Iterable Class

```python
class RangeIterable:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return RangeIterator(self.start, self.stop)
```

### 2. Iterator Class

```python
class RangeIterator:
    def __init__(self, current, stop):
        self.current = current
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
```

### 3. Multiple Iterations

```python
r = RangeIterable(0, 3)
list(r)  # [0, 1, 2]
list(r)  # [0, 1, 2] - works again!
```

---

## Infinite Iterators

### 1. Fibonacci Sequence

```python
class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

fib = Fibonacci()
from itertools import islice
print(list(islice(fib, 10)))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### 2. Never Exhausts

```python
# Infinite - never raises StopIteration
for num in Fibonacci():
    if num > 100:
        break
    print(num)
```

### 3. Use with `itertools`

```python
from itertools import islice, takewhile

# Take first 5
list(islice(Fibonacci(), 5))

# Take while < 100
list(takewhile(lambda x: x < 100, Fibonacci()))
```

---

## StopIteration

### 1. Signal End

```python
def __next__(self):
    if self.current >= self.stop:
        raise StopIteration
    # Return value
```

Exception marks iteration complete.

### 2. Automatic Handling

```python
# for loop catches StopIteration
for item in iterator:
    pass  # Stops when StopIteration raised
```

### 3. Manual Iteration

```python
it = iter([1, 2, 3])
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # StopIteration
```

---

## Built-in `iter()` and `next()`

### 1. `iter()` Function

```python
obj = [1, 2, 3]
it = iter(obj)  # Calls obj.__iter__()
```

### 2. `next()` Function

```python
value = next(it)  # Calls it.__next__()
```

### 3. Default Value

```python
value = next(it, "default")
# Returns "default" instead of raising StopIteration
```

---

## Generator Alternative

### 1. Generator Function

```python
def my_range(start, stop):
    current = start
    while current < stop:
        yield current
        current += 1

for i in my_range(0, 5):
    print(i)
```

### 2. Simpler Syntax

```python
# Class-based
class MyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return MyRangeIterator(self.start, self.stop)

# Generator-based
def my_range(start, stop):
    while start < stop:
        yield start
        start += 1
```

### 3. Automatic Iterator

Generators automatically implement iterator protocol.

---

## Custom Iteration Logic

### 1. Even Numbers

```python
class EvenNumbers:
    def __init__(self, max_val):
        self.max = max_val
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

for num in EvenNumbers(10):
    print(num)  # 0, 2, 4, 6, 8, 10
```

### 2. Reverse Iteration

```python
class ReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
```

### 3. Filtered Iteration

```python
class FilteredIterator:
    def __init__(self, iterable, predicate):
        self.iterator = iter(iterable)
        self.predicate = predicate
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            value = next(self.iterator)
            if self.predicate(value):
                return value
```

---

## Real-World Examples

### 1. File Lines

```python
class FileLines:
    def __init__(self, filename):
        self.file = open(filename)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()

for line in FileLines("data.txt"):
    print(line)
```

### 2. Batch Iterator

```python
class BatchIterator:
    def __init__(self, data, batch_size):
        self.data = data
        self.batch_size = batch_size
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        batch = self.data[self.index:self.index + self.batch_size]
        self.index += self.batch_size
        return batch
```

### 3. Sliding Window

```python
class SlidingWindow:
    def __init__(self, data, window_size):
        self.data = data
        self.window_size = window_size
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index + self.window_size > len(self.data):
            raise StopIteration
        window = self.data[self.index:self.index + self.window_size]
        self.index += 1
        return window
```

---

## Lazy Evaluation

### 1. Compute on Demand

```python
class LazySquares:
    def __init__(self, n):
        self.n = n
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        result = self.i ** 2
        self.i += 1
        return result

# Doesn't compute all squares upfront
for sq in LazySquares(5):
    print(sq)
```

### 2. Memory Efficient

```python
# Bad: stores all in memory
def all_squares(n):
    return [i**2 for i in range(n)]

# Good: generates on demand
class LazySquares:
    # As above
```

### 3. Infinite Streams

Lazy evaluation enables infinite sequences.

---

## Best Practices

### 1. Separate Iterable/Iterator

```python
# Good
class MyIterable:
    def __iter__(self):
        return MyIterator()

class MyIterator:
    def __next__(self):
        pass
```

### 2. Use Generators

```python
# Simpler for most cases
def my_generator():
    yield value
```

### 3. Document Behavior

```python
class MyIterator:
    """
    Iterates over values from start to stop.
    Single-use iterator.
    """
```

---

## Key Takeaways

- Iterable has `__iter__()`, returns iterator.
- Iterator has `__iter__()` and `__next__()`.
- Separate iterable/iterator for reusability.
- `StopIteration` signals end.
- Generators often simpler than classes.
- Enables lazy, memory-efficient iteration.
