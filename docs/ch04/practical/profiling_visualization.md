# Profiling Visualization (snakeviz)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Visualizing profiling data makes it easier to understand performance characteristics. `snakeviz` provides interactive flame graphs for cProfile output.

---

## Installation and Basic Usage

```bash
pip install snakeviz
```

Generate a profile and visualize:
```bash
python -m cProfile -o profile.prof your_script.py
snakeviz profile.prof
```

## Creating Profiler Output

```python
# example_code.py
import cProfile

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def process_data():
    results = []
    for i in range(25, 30):
        results.append(fibonacci(i))
    return results

if __name__ == "__main__":
    cProfile.run('process_data()', filename='profile.prof')
```

View the visualization:
```bash
snakeviz profile.prof
```

## Interpreting Flame Graphs

The visualization shows:
- **Box width**: Time spent in that function
- **Box height**: Call stack depth
- **Colors**: Different functions (random assignment)
- **Hover**: Shows function name and timing details
- **Click**: Zoom into that portion of the call tree

## Command-line Options

```bash
# Open on specific port
snakeviz --port 8080 profile.prof

# Open in specific browser
snakeviz --browser firefox profile.prof

# Don't open browser automatically
snakeviz --nostrip profile.prof
```

## Programmatic Profiling with Visualization

```python
import cProfile
import pstats
from io import StringIO

def slow_function():
    total = 0
    for i in range(100000):
        total += sum(range(i))
    return total

# Profile the function
profiler = cProfile.Profile()
profiler.enable()
slow_function()
profiler.disable()

# Save for visualization
profiler.dump_stats('results.prof')

# Also print text summary
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(5)
```

## Practical Workflow

1. Profile with cProfile
2. Save to .prof file
3. Visualize with snakeviz
4. Identify hot spots (wide boxes)
5. Focus optimization on hot spots
6. Profile again to verify improvements
