# islice

`islice()` extracts a slice from an iterator without consuming the entire iterator or materializing it into memory.

## Basic Slicing with islice

Extract specific elements from an iterator using `islice(iterable, start, stop, step)`.

```python
from itertools import islice

numbers = range(10)

# Get elements from index 2 to 5
result1 = list(islice(numbers, 2, 5))
print(result1)

# Get first 4 elements
result2 = list(islice(numbers, 4))
print(result2)

# Get every 2nd element starting from index 1
result3 = list(islice(numbers, 1, None, 2))
print(result3)
```

```
[2, 3, 4]
[0, 1, 2, 3]
[1, 3, 5, 7, 9]
```

## Practical Use Case

Use `islice()` to paginate through large datasets efficiently.

```python
from itertools import islice

def paginate(iterable, page_size):
    it = iter(iterable)
    while True:
        page = list(islice(it, page_size))
        if not page:
            break
        yield page

# Paginate a range
data = range(10)
for i, page in enumerate(paginate(data, 3)):
    print(f"Page {i}: {page}")
```

```
Page 0: [0, 1, 2]
Page 1: [3, 4, 5]
Page 2: [6, 7, 8]
Page 3: [9]
```

