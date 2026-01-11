# GC Performance

## Impact

### 1. Collection Pauses

```python
import gc
import time

# Measure pause
start = time.time()
collected = gc.collect()
pause = time.time() - start

print(f"Pause: {pause*1000:.2f}ms")
print(f"Collected: {collected}")
```

### 2. Frequency Matters

```python
import gc

# Default: frequent gen-0
print(gc.get_threshold())  # (700, 10, 10)

# Adjust for workload
gc.set_threshold(10000, 100, 100)
# Fewer collections, longer pauses
```

## Optimization

### 1. Disable During Critical

```python
import gc

gc.disable()
try:
    # Performance-critical code
    compute()
finally:
    gc.enable()
    gc.collect()  # Collect after
```

### 2. Manual Control

```python
import gc

# Disable auto
gc.disable()

# Collect periodically
for i in range(1000):
    process()
    
    if i % 100 == 0:
        gc.collect()
```

### 3. Reduce Allocations

```python
# Bad: many allocations
result = []
for i in range(1000):
    result.append([i])

# Better: pre-allocate
result = [None] * 1000
for i in range(1000):
    result[i] = i
```

## Monitoring

### 1. Collection Stats

```python
import gc

# Before
before = gc.get_count()

# Run code
process()

# After
after = gc.get_count()
print(f"Collections: {after[0] - before[0]}")
```

### 2. Debug Stats

```python
import gc

gc.set_debug(gc.DEBUG_STATS)
gc.collect()
# Prints collection statistics
```

## Summary

- Collection causes pauses
- Adjust thresholds
- Disable during critical
- Reduce allocations
- Monitor impact
