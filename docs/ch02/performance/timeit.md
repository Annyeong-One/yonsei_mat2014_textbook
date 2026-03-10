# timeit Module


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The timeit module measures execution time of code snippets, useful for benchmarking and performance comparison. It handles timing overhead and runs code multiple times for accurate results.

---

## Basic Timing

### Simple Benchmarking

```python
import timeit

result = timeit.timeit("sum(range(100))", number=100000)
print(f"Execution time: {result:.4f}s")
```

Output:
```
Execution time: 0.1234s
```

### Timer Class

```python
import timeit

timer = timeit.Timer("x = 1 + 1")
result = timer.timeit(number=1000000)
print(f"1000000 iterations: {result:.4f}s")
```

Output:
```
1000000 iterations: 0.0234s
```

## Setup Code

### Initializing Before Timing

```python
import timeit

setup = "lst = list(range(1000))"
time1 = timeit.timeit("5 in lst", setup=setup, number=100000)
print(f"Membership test: {time1:.4f}s")
```

Output:
```
Membership test: 0.0456s
```

## Comparing Code Snippets

### Which is Faster?

```python
import timeit

concat_time = timeit.timeit(
    'x = "a" + "b" + "c"',
    number=1000000
)

format_time = timeit.timeit(
    'x = f"{"a"}{"b"}{"c"}"',
    number=1000000
)

print(f"Concatenation: {concat_time:.4f}s")
print(f"F-string: {format_time:.4f}s")
```

Output:
```
Concatenation: 0.0234s
F-string: 0.0198s
```

## Repeat and Compare

### Multiple Runs

```python
import timeit

times = timeit.repeat(
    "sum(range(100))",
    number=10000,
    repeat=5
)

print(f"Times: {[f'{t:.4f}' for t in times]}")
print(f"Best: {min(times):.4f}s")
print(f"Worst: {max(times):.4f}s")
```

Output:
```
Times: ['0.1234', '0.1201', '0.1198', '0.1205', '0.1211']
Best: 0.1198s
Worst: 0.1234s
```

## Real-World Example

### Benchmarking List Operations

```python
import timeit

operations = {
    'append': 'lst.append(100)',
    'insert_0': 'lst.insert(0, 100)',
    'extend': 'lst.extend([100, 101])'
}

setup = "lst = list(range(100))"

for name, code in operations.items():
    time = timeit.timeit(code, setup=setup, number=10000)
    print(f"{name}: {time:.4f}s")
```

Output:
```
append: 0.0012s
insert_0: 0.0456s
extend: 0.0045s
```
