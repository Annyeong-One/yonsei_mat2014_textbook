# gc Module

## Control

### 1. Enable/Disable

```python
import gc

gc.disable()  # Turn off
# Critical section
gc.enable()   # Turn on
```

### 2. Force Collection

```python
import gc

# Collect all generations
collected = gc.collect()
print(f"Collected {collected} objects")
```

## Inspection

### 1. Get Objects

```python
import gc

# All tracked objects
objects = gc.get_objects()
print(len(objects))
```

### 2. Object Stats

```python
import gc

# Count by type
from collections import Counter

types = Counter(type(obj).__name__ for obj in gc.get_objects())
for name, count in types.most_common(10):
    print(f"{name}: {count}")
```

## Thresholds

### 1. View Settings

```python
import gc

# Get thresholds
print(gc.get_threshold())  # (700, 10, 10)
```

### 2. Adjust

```python
import gc

# Set new thresholds
gc.set_threshold(1000, 15, 15)
```

## Debug

### 1. Debug Flags

```python
import gc

# Enable debug output
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
```

### 2. Find Cycles

```python
import gc

# Force collection
gc.collect()

# Get garbage (uncollectable)
garbage = gc.garbage
print(f"Uncollectable: {len(garbage)}")
```

## Summary

- Control collection
- Inspect objects
- Adjust thresholds
- Debug leaks
