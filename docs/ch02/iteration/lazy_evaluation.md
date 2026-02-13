# Lazy Evaluation Patterns

Lazy evaluation defers computation until values are actually needed. Generators and iterators enable lazy evaluation, reducing memory usage and enabling infinite sequences.

---

## Generator Laziness

### Computation on Demand

```python
def lazy_range(n):
    print("Starting generator")
    for i in range(n):
        print(f"Computing {i}")
        yield i

gen = lazy_range(3)
print("Generator created (nothing computed)")
print(next(gen))
print(next(gen))
```

Output:
```
Generator created (nothing computed)
Starting generator
Computing 0
0
Computing 1
1
```

### Memory Efficiency

```python
# List - all values in memory
nums_list = [x**2 for x in range(1000000)]
print(f"List uses memory for 1M items")

# Generator - one value at a time
nums_gen = (x**2 for x in range(1000000))
print(f"Generator created (lazy)")
print(next(nums_gen))
```

Output:
```
List uses memory for 1M items
Generator created (lazy)
0
```

## Infinite Sequences

### Creating Infinite Generators

```python
def infinite_counter(start=0):
    current = start
    while True:
        yield current
        current += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter))
```

Output:
```
0
1
2
3
4
```

### Fibonacci Sequence

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(8)])
```

Output:
```
[0, 1, 1, 2, 3, 5, 8, 13]
```

## Chaining Operations

### Lazy Composition

```python
def multiply(iterable, factor):
    for value in iterable:
        yield value * factor

def add_offset(iterable, offset):
    for value in iterable:
        yield value + offset

pipeline = add_offset(multiply(range(5), 2), 10)
print(list(pipeline))
```

Output:
```
[10, 12, 14, 16, 18]
```

### Filtering Lazily

```python
def lazy_filter(iterable, predicate):
    for value in iterable:
        if predicate(value):
            yield value

nums = range(10)
evens = lazy_filter(nums, lambda x: x % 2 == 0)
print(list(evens))
```

Output:
```
[0, 2, 4, 6, 8]
```
