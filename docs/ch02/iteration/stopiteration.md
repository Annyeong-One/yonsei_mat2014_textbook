# StopIteration Mechanics


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

StopIteration is the protocol-level signal that an iterator has no more values. Understanding StopIteration is fundamental to Python's iteration protocol and generator behavior.

---

## Iterator Protocol

### Raising StopIteration

```python
class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

counter = CountUp(3)
for value in counter:
    print(value)
```

Output:
```
1
2
3
```

### Manual Iteration

```python
numbers = iter([1, 2, 3])

try:
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))  # Raises StopIteration
except StopIteration:
    print("Iterator exhausted")
```

Output:
```
1
2
3
Iterator exhausted
```

## Generators and StopIteration

### Implicit StopIteration

```python
def count_up(max):
    current = 0
    while current < max:
        current += 1
        yield current

gen = count_up(3)
try:
    while True:
        print(next(gen))
except StopIteration:
    print("Generator finished")
```

Output:
```
1
2
3
Generator finished
```

## Return Values in StopIteration

### PEP 380 Return Mechanism

```python
def search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

result = search([1, 2, 3, 4], 3)
print(f"Found at index: {result}")
```

Output:
```
Found at index: 2
```

## Best Practices

### Catching StopIteration Safely

```python
def safe_next(iterator, default=None):
    try:
        return next(iterator)
    except StopIteration:
        return default

gen = (x for x in [1, 2, 3])
next(gen)
next(gen)
next(gen)
result = safe_next(gen, "exhausted")
print(result)
```

Output:
```
exhausted
```
