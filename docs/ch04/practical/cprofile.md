# cProfile Module


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python's built-in `cProfile` module provides a deterministic profiler that measures CPU time spent in each function. It's essential for identifying performance bottlenecks in your code.

---

## Basic Usage

The `cProfile` module offers several ways to profile code: command-line usage, direct module calls, or context managers.

### Command-line Profiling

```python
# example_module.py
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    result = fibonacci(30)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```

Run with profiling:
```
python -m cProfile -s cumulative example_module.py
```

### Programmatic Profiling

```python
import cProfile
import pstats
from io import StringIO

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Create profiler and run code
profiler = cProfile.Profile()
profiler.enable()

result = fibonacci(30)

profiler.disable()

# Print statistics
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 functions
```

## Interpreting Results

cProfile output shows:
- **ncalls**: Number of calls to the function
- **tottime**: Total time spent in the function (excluding subfunctions)
- **cumtime**: Cumulative time (including called functions)
- **filename:lineno(function)**: Where the function is defined

```
   ncalls  tottime  cumtime      filename:lineno(function)
   832039    0.156    0.321 example.py:1(fibonacci)
        1    0.000    0.320 example.py:6(main)
```

## Saving and Loading Profiling Data

```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Your code here
for i in range(1000):
    sum([i**2 for i in range(100)])

profiler.disable()

# Save to file
profiler.dump_stats('profile_data.prof')

# Load and analyze later
stats = pstats.Stats('profile_data.prof')
stats.sort_stats('cumulative')
stats.print_stats(5)
```

## Performance Tips

- Use `sort_stats()` with 'cumulative' for wall-clock time analysis
- Filter results with `print_stats(10)` to see top functions
- Compare profiles before and after optimizations
- Profile on realistic data to get accurate measurements
