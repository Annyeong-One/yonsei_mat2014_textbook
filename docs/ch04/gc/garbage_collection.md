# Garbage Collection


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

순환 참조를 처리하는 Python의 가비지 컬렉터입니다.

## Generational GC

Python은 세대별 가비지 컬렉션을 사용합니다. "대부분의 객체는 일찍 죽는다"는 약한 세대 가설(Weak Generational Hypothesis)에 기반합니다.

### Three Generations

```python
import gc

# (gen0_count, gen1_count, gen2_count)
print(gc.get_count())
```

| Generation | Description | Collection Frequency |
|------------|-------------|---------------------|
| Gen 0 | Young objects | Most frequent |
| Gen 1 | Survived 1 collection | Less frequent |
| Gen 2 | Long-lived objects | Rare |

### Promotion

```python
# Object created → Gen 0
# Survives collection → Gen 1
# Survives again → Gen 2
```

### Thresholds

```python
import gc

# (threshold0, threshold1, threshold2)
print(gc.get_threshold())  # Default: (700, 10, 10)

# Gen 0: every 700 allocations
# Gen 1: every 10 gen-0 collections
# Gen 2: every 10 gen-1 collections
```

---

## gc Module

### Enable/Disable

```python
import gc

gc.disable()  # Turn off
# Critical section
gc.enable()   # Turn on
```

### Force Collection

```python
import gc

# Collect all generations
collected = gc.collect()
print(f"Collected {collected} objects")

# Collect specific generation
gc.collect(0)  # Gen 0 only
gc.collect(1)  # Gen 0 and 1
gc.collect(2)  # All generations
```

### Inspect Objects

```python
import gc

# All tracked objects
objects = gc.get_objects()
print(len(objects))

# Count by type
from collections import Counter

types = Counter(type(obj).__name__ for obj in gc.get_objects())
for name, count in types.most_common(10):
    print(f"{name}: {count}")
```

### Adjust Thresholds

```python
import gc

# Get current thresholds
print(gc.get_threshold())  # (700, 10, 10)

# Set new thresholds
gc.set_threshold(1000, 15, 15)
```

### Generation Statistics

```python
import gc

stats = gc.get_stats()
for i, stat in enumerate(stats):
    print(f"Gen {i}: {stat}")
```

---

## Debugging

### Debug Flags

```python
import gc

# Enable debug output
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
```

| Flag | Description |
|------|-------------|
| `DEBUG_STATS` | Print collection statistics |
| `DEBUG_COLLECTABLE` | Print collectable objects |
| `DEBUG_UNCOLLECTABLE` | Print uncollectable objects |
| `DEBUG_LEAK` | Debug leaks (COLLECTABLE + UNCOLLECTABLE) |

### Find Uncollectable Objects

```python
import gc

gc.collect()

# Get garbage (uncollectable)
garbage = gc.garbage
print(f"Uncollectable: {len(garbage)}")
```

---

## Cycle Detection Example

```python
import gc

class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None

# Create cycle
a = Node('a')
b = Node('b')
a.ref = b
b.ref = a

# Delete references
del a, b

# Objects still exist (cycle)
print(f"Before: {gc.get_count()}")

# Force collection
collected = gc.collect()
print(f"Collected: {collected}")

print(f"After: {gc.get_count()}")
```

## Summary

| Feature | Description |
|---------|-------------|
| Algorithm | Mark-and-sweep with generations |
| Generations | 3 (young, middle, old) |
| Trigger | Allocation threshold |
| Control | `gc.enable()`, `gc.disable()`, `gc.collect()` |
| Tuning | `gc.set_threshold()` |
