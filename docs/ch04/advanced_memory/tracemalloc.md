# tracemalloc — Memory Profiling


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The `tracemalloc` module tracks memory allocations in Python, helping you find memory leaks and identify which code is consuming the most memory.

```python
import tracemalloc
```

---

## Why tracemalloc?

- **Find memory leaks**: Track allocations that aren't freed
- **Identify memory hogs**: See which code allocates the most
- **Compare snapshots**: Measure memory growth over time
- **Debug production issues**: Low overhead profiling

---

## Basic Usage

### Start Tracking

```python
import tracemalloc

# Start tracing memory allocations
tracemalloc.start()

# Your code here
data = [i ** 2 for i in range(10000)]

# Get current memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024:.2f} KB")
print(f"Peak:    {peak / 1024:.2f} KB")

# Stop tracing
tracemalloc.stop()
```

### Take Snapshots

```python
import tracemalloc

tracemalloc.start()

# Allocate some memory
x = [i for i in range(100000)]

# Take a snapshot
snapshot = tracemalloc.take_snapshot()

# Get top memory consumers
top_stats = snapshot.statistics('lineno')

print("Top 10 memory allocations:")
for stat in top_stats[:10]:
    print(stat)
```

---

## Snapshot Statistics

### Group by Line Number

```python
import tracemalloc

tracemalloc.start()

# Sample allocations
list1 = [i for i in range(50000)]      # Line A
list2 = [str(i) for i in range(50000)] # Line B
dict1 = {i: i**2 for i in range(10000)}# Line C

snapshot = tracemalloc.take_snapshot()

# Statistics by line number
stats = snapshot.statistics('lineno')
for stat in stats[:5]:
    print(stat)
```

Output:
```
script.py:6: size=1954 KiB, count=50001, average=40 B
script.py:7: size=3125 KiB, count=100001, average=32 B
script.py:8: size=562 KiB, count=10001, average=58 B
```

### Group by Filename

```python
stats = snapshot.statistics('filename')
for stat in stats[:5]:
    print(stat)
```

### Group by Traceback

```python
# Start with deeper traceback (default is 1)
tracemalloc.start(25)  # Store 25 frames

snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics('traceback')

# Show full traceback for top allocation
top = stats[0]
print(f"\nTop allocation: {top.size / 1024:.2f} KB")
for line in top.traceback.format():
    print(line)
```

---

## Comparing Snapshots

The most powerful feature—compare memory before and after:

```python
import tracemalloc

tracemalloc.start()

# Take first snapshot
snapshot1 = tracemalloc.take_snapshot()

# Do some work that might leak memory
cache = {}
for i in range(10000):
    cache[i] = f"value_{i}" * 100

# Take second snapshot
snapshot2 = tracemalloc.take_snapshot()

# Compare snapshots
top_stats = snapshot2.compare_to(snapshot1, 'lineno')

print("Memory differences (top 10):")
for stat in top_stats[:10]:
    print(stat)
```

Output:
```
script.py:12: size=11.5 MiB (+11.5 MiB), count=10000 (+10000), average=1205 B
script.py:11: size=547 KiB (+547 KiB), count=10001 (+10001), average=56 B
```

The `+` indicates memory growth between snapshots.

---

## Finding Memory Leaks

### Pattern: Periodic Snapshots

```python
import tracemalloc
import time

def find_memory_leak():
    tracemalloc.start()
    
    snapshots = []
    leaked_data = []  # Simulated leak
    
    for iteration in range(5):
        # Simulate work that leaks memory
        leaked_data.append([0] * 100000)
        
        # Take snapshot
        snapshot = tracemalloc.take_snapshot()
        snapshots.append(snapshot)
        
        if len(snapshots) > 1:
            # Compare to previous snapshot
            diff = snapshot.compare_to(snapshots[-2], 'lineno')
            print(f"\n=== Iteration {iteration} ===")
            for stat in diff[:3]:
                print(stat)
        
        time.sleep(0.1)
    
    tracemalloc.stop()

find_memory_leak()
```

### Pattern: Context Manager

```python
import tracemalloc
from contextlib import contextmanager

@contextmanager
def trace_memory(name=""):
    """Context manager to trace memory in a block."""
    tracemalloc.start()
    snapshot1 = tracemalloc.take_snapshot()
    
    yield
    
    snapshot2 = tracemalloc.take_snapshot()
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    
    print(f"\n=== Memory trace: {name} ===")
    total = sum(stat.size_diff for stat in top_stats)
    print(f"Total change: {total / 1024:.2f} KB")
    for stat in top_stats[:5]:
        print(stat)
    
    tracemalloc.stop()

# Usage
with trace_memory("Building cache"):
    cache = {i: str(i) * 100 for i in range(10000)}
```

---

## Filtering Results

### Filter by Filename

```python
import tracemalloc

tracemalloc.start()

# ... your code ...

snapshot = tracemalloc.take_snapshot()

# Filter to only show your code (exclude standard library)
snapshot = snapshot.filter_traces((
    tracemalloc.Filter(True, "*/myproject/*"),  # Include
    tracemalloc.Filter(False, "<frozen *>"),     # Exclude
    tracemalloc.Filter(False, "<unknown>"),      # Exclude
))

stats = snapshot.statistics('lineno')
for stat in stats[:10]:
    print(stat)
```

### Filter Class

```python
# Include only files matching pattern
include_filter = tracemalloc.Filter(True, "*/myapp/*.py")

# Exclude standard library
exclude_stdlib = tracemalloc.Filter(False, "/usr/lib/*")

# Exclude specific module
exclude_module = tracemalloc.Filter(False, "*/numpy/*")

# Apply filters
filtered = snapshot.filter_traces([
    include_filter,
    exclude_stdlib,
    exclude_module,
])
```

---

## Practical Examples

### Memory Usage Decorator

```python
import tracemalloc
import functools

def trace_memory(func):
    """Decorator to trace memory usage of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        
        result = func(*args, **kwargs)
        
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        print(f"{func.__name__}:")
        print(f"  Current memory: {current / 1024:.2f} KB")
        print(f"  Peak memory:    {peak / 1024:.2f} KB")
        
        return result
    return wrapper

@trace_memory
def process_data():
    return [i ** 2 for i in range(100000)]

data = process_data()
```

### Memory Report Class

```python
import tracemalloc

class MemoryProfiler:
    """Track memory across multiple checkpoints."""
    
    def __init__(self):
        self.snapshots = {}
        tracemalloc.start(25)
    
    def checkpoint(self, name):
        """Save a named snapshot."""
        self.snapshots[name] = tracemalloc.take_snapshot()
        print(f"Checkpoint '{name}' saved")
    
    def compare(self, name1, name2):
        """Compare two named snapshots."""
        if name1 not in self.snapshots or name2 not in self.snapshots:
            raise ValueError("Snapshot not found")
        
        stats = self.snapshots[name2].compare_to(
            self.snapshots[name1], 'lineno'
        )
        
        print(f"\n=== {name1} → {name2} ===")
        for stat in stats[:10]:
            if stat.size_diff != 0:
                print(stat)
    
    def current_usage(self):
        """Show current memory usage."""
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current: {current / 1024 / 1024:.2f} MB")
        print(f"Peak:    {peak / 1024 / 1024:.2f} MB")
    
    def stop(self):
        tracemalloc.stop()

# Usage
profiler = MemoryProfiler()
profiler.checkpoint("start")

data = [i for i in range(100000)]
profiler.checkpoint("after_list")

more_data = {i: str(i) for i in range(50000)}
profiler.checkpoint("after_dict")

profiler.compare("start", "after_dict")
profiler.current_usage()
profiler.stop()
```

### Finding Top Allocations in a Module

```python
import tracemalloc

def profile_module_memory(module_path):
    """Profile memory allocations from a specific module."""
    tracemalloc.start(25)
    
    # Import and run the module
    exec(open(module_path).read())
    
    snapshot = tracemalloc.take_snapshot()
    
    # Filter to only the module's allocations
    snapshot = snapshot.filter_traces([
        tracemalloc.Filter(True, module_path)
    ])
    
    stats = snapshot.statistics('traceback')
    
    print(f"\nTop allocations in {module_path}:")
    for stat in stats[:5]:
        print(f"\n{stat.count} allocations, {stat.size / 1024:.1f} KB")
        for line in stat.traceback.format()[:3]:
            print(f"  {line}")
    
    tracemalloc.stop()
```

---

## Performance Considerations

### Overhead

```python
import tracemalloc
import time

# Measure overhead
def benchmark(with_tracing):
    if with_tracing:
        tracemalloc.start()
    
    start = time.perf_counter()
    data = [i ** 2 for i in range(1000000)]
    elapsed = time.perf_counter() - start
    
    if with_tracing:
        tracemalloc.stop()
    
    return elapsed

without = benchmark(False)
with_trace = benchmark(True)

print(f"Without tracing: {without:.3f}s")
print(f"With tracing:    {with_trace:.3f}s")
print(f"Overhead:        {(with_trace/without - 1) * 100:.1f}%")
# Typically 5-30% overhead
```

### Controlling Frame Depth

```python
# Less memory overhead, less detail
tracemalloc.start(1)   # Only 1 frame (default)

# More detail, more memory
tracemalloc.start(25)  # 25 frames deep

# Check current setting
print(tracemalloc.get_traceback_limit())
```

---

## Integration with Other Tools

### With logging

```python
import tracemalloc
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_memory_usage():
    if tracemalloc.is_tracing():
        current, peak = tracemalloc.get_traced_memory()
        logger.info(
            f"Memory - Current: {current/1024/1024:.2f}MB, "
            f"Peak: {peak/1024/1024:.2f}MB"
        )
```

### With unittest

```python
import tracemalloc
import unittest

class MemoryTestCase(unittest.TestCase):
    def setUp(self):
        tracemalloc.start()
        self.snapshot_before = tracemalloc.take_snapshot()
    
    def tearDown(self):
        snapshot_after = tracemalloc.take_snapshot()
        diff = snapshot_after.compare_to(self.snapshot_before, 'lineno')
        
        # Check for unexpected memory growth
        total_growth = sum(s.size_diff for s in diff if s.size_diff > 0)
        if total_growth > 10 * 1024 * 1024:  # 10 MB threshold
            self.fail(f"Memory grew by {total_growth/1024/1024:.2f} MB")
        
        tracemalloc.stop()
```

---

## Summary

| Function | Purpose |
|----------|---------|
| `tracemalloc.start(nframe)` | Start tracing with nframe depth |
| `tracemalloc.stop()` | Stop tracing |
| `tracemalloc.take_snapshot()` | Capture current allocations |
| `tracemalloc.get_traced_memory()` | Get (current, peak) tuple |
| `snapshot.statistics(key)` | Group by 'lineno', 'filename', 'traceback' |
| `snapshot.compare_to(other, key)` | Compare two snapshots |
| `snapshot.filter_traces(filters)` | Filter results |

**Key Takeaways**:

- Use `tracemalloc` to find memory leaks and hotspots
- Compare snapshots to see memory growth over time
- Filter results to focus on your code
- Low overhead (~5-30%) makes it suitable for profiling
- Increase frame depth for detailed tracebacks
- Combine with decorators and context managers for easy profiling
