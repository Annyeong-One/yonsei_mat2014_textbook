# line_profiler


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The `line_profiler` tool profiles code at the line level, showing exactly which lines consume the most time. It requires installation via pip.

---

## Installation and Setup

```bash
pip install line_profiler
```

## Using line_profiler

Mark functions with `@profile` decorator and run with `kernprof`:

```python
# example.py
@profile
def process_data(n):
    result = 0
    for i in range(n):
        result += i ** 2  # Expensive operation
    
    total = sum(range(n))  # Another loop
    return result, total

if __name__ == "__main__":
    process_data(10000)
```

Run with profiler:
```
kernprof -l -v example.py
```

## Output Interpretation

```
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           @profile
     2                                           def process_data(n):
     3         1            2      2.0      0.0      result = 0
     4     10001          456     0.0      5.2      for i in range(n):
     5     10000         8234     0.8     94.2          result += i ** 2
     6         1          122    122.0      1.4      total = sum(range(n))
     7         1            1      1.0      0.0      return result, total
```

## Advanced Features

```python
# Profiling without @profile decorator
from line_profiler import LineProfiler

def expensive_function():
    data = []
    for i in range(100):
        data.append(i ** 2)
    return data

profiler = LineProfiler()
profiler.add_function(expensive_function)
profiler.enable()
expensive_function()
profiler.disable()
profiler.print_stats()
```

## Combining with cProfile

For a complete picture, use both tools:
- **cProfile** identifies which functions are slow
- **line_profiler** identifies which lines within those functions are slow
