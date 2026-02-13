# Benchmarking Methodology

Proper benchmarking requires careful methodology to get accurate, reproducible results. Learn best practices for performance testing.

---

## Using timeit Module

The `timeit` module is the standard way to benchmark small code snippets:

```python
import timeit

# Method 1: Direct timing
time1 = timeit.timeit('sum(range(100))', number=1000000)
print(f"Time: {time1:.4f} seconds")

# Method 2: Using a function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

time2 = timeit.timeit(lambda: fibonacci(20), number=100)
print(f"Average: {time2/100:.6f} seconds")
```

## Statistical Benchmarking

```python
import timeit
import statistics

def benchmark(func, number=100, repeat=5):
    times = timeit.repeat(
        lambda: func(),
        number=number,
        repeat=repeat
    )
    return {
        'min': min(times),
        'max': max(times),
        'mean': statistics.mean(times),
        'stdev': statistics.stdev(times) if len(times) > 1 else 0
    }

def test_function():
    return sum(i ** 2 for i in range(1000))

stats = benchmark(test_function)
print(f"Mean: {stats['mean']:.4f}s ± {stats['stdev']:.4f}s")
```

## Comparing Implementations

```python
import timeit

# Compare two approaches
list_comp = 'result = [x**2 for x in range(1000)]'
map_func = 'result = list(map(lambda x: x**2, range(1000)))'
generator = 'result = (x**2 for x in range(1000))'

time_list = timeit.timeit(list_comp, number=100000)
time_map = timeit.timeit(map_func, number=100000)
time_gen = timeit.timeit(generator, number=100000)

print(f"List comprehension: {time_list:.4f}s")
print(f"Map function: {time_map:.4f}s")
print(f"Generator: {time_gen:.4f}s")
```

## Best Practices

- Run benchmarks multiple times (10-100+)
- Disable background processes
- Use realistic data sizes
- Warm up code before benchmarking (JIT compilation)
- Profile on production-like hardware
- Compare against baselines, not absolute times
- Report mean, min, max, and standard deviation
