# Profiling Tools


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Empirical performance analysis guides optimization efforts.


## IPython %timeit

Quick timing in interactive environments.

### 1. Basic Usage

```python
%timeit arr ** 2
```

Output:

```
1.23 µs ± 45.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```

### 2. Multi-line Timing

```python
%%timeit
result = np.zeros(1000)
for i in range(1000):
    result[i] = i ** 2
```

### 3. Control Runs

```python
%timeit -n 100 -r 5 arr ** 2  # 100 loops, 5 runs
```


## timeit Module

Scripted benchmarks outside IPython.

### 1. Basic Script

```python
import timeit
import numpy as np

def main():
    setup = "import numpy as np; arr = np.random.randn(10000)"
    stmt = "arr ** 2"
    
    time = timeit.timeit(stmt, setup, number=1000)
    print(f"Total time: {time:.4f} sec")
    print(f"Per call:   {time/1000*1000:.4f} ms")

if __name__ == "__main__":
    main()
```

### 2. Compare Functions

```python
import timeit
import numpy as np

def method_loop(arr):
    result = np.empty_like(arr)
    for i in range(len(arr)):
        result[i] = arr[i] ** 2
    return result

def method_vectorized(arr):
    return arr ** 2

def main():
    arr = np.random.randn(10000)
    
    loop_time = timeit.timeit(
        lambda: method_loop(arr), number=100
    )
    vec_time = timeit.timeit(
        lambda: method_vectorized(arr), number=100
    )
    
    print(f"Loop time:       {loop_time:.4f} sec")
    print(f"Vectorized time: {vec_time:.4f} sec")
    print(f"Speedup:         {loop_time/vec_time:.0f}x")

if __name__ == "__main__":
    main()
```


## time.perf_counter

Manual timing with high precision.

### 1. Basic Pattern

```python
import time
import numpy as np

def main():
    arr = np.random.randn(1_000_000)
    
    start = time.perf_counter()
    result = arr ** 2
    elapsed = time.perf_counter() - start
    
    print(f"Elapsed: {elapsed:.6f} sec")

if __name__ == "__main__":
    main()
```

### 2. Multiple Runs

```python
import time
import numpy as np

def main():
    arr = np.random.randn(1_000_000)
    times = []
    
    for _ in range(10):
        start = time.perf_counter()
        result = arr ** 2
        times.append(time.perf_counter() - start)
    
    print(f"Mean: {np.mean(times):.6f} sec")
    print(f"Std:  {np.std(times):.6f} sec")

if __name__ == "__main__":
    main()
```


## cProfile Module

Function-level profiling for entire programs.

### 1. Command Line

```bash
python -m cProfile -s cumtime my_script.py
```

### 2. In Script

```python
import cProfile
import numpy as np

def my_function():
    arr = np.random.randn(100000)
    for _ in range(100):
        result = arr ** 2

cProfile.run('my_function()')
```

### 3. Output Example

```
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      100    0.050    0.001    0.050    0.001 {method 'random' ...}
      100    0.030    0.000    0.030    0.000 {built-in method numpy...}
```


## line_profiler

Line-by-line timing for detailed analysis.

### 1. Installation

```bash
pip install line_profiler
```

### 2. Decorator Usage

```python
@profile
def my_function():
    arr = np.random.randn(100000)  # Line 1
    result = arr ** 2               # Line 2
    total = np.sum(result)          # Line 3
    return total
```

### 3. Run Command

```bash
kernprof -l -v my_script.py
```


## memory_profiler

Track memory usage during execution.

### 1. Installation

```bash
pip install memory_profiler
```

### 2. Usage

```python
from memory_profiler import profile

@profile
def my_function():
    arr = np.random.randn(1_000_000)
    result = arr ** 2
    return result
```

### 3. Output Example

```
Line #    Mem usage    Increment  Line Contents
     3     50.0 MiB     50.0 MiB   arr = np.random.randn(1_000_000)
     4     57.6 MiB      7.6 MiB   result = arr ** 2
```


## Best Practices

Guidelines for effective profiling.

### 1. Profile First

Identify bottlenecks before optimizing.

### 2. Representative Data

Use realistic data sizes for meaningful results.

### 3. Multiple Runs

Average over multiple runs to reduce variance.
