# collections Overview

The `collections` module provides specialized container types that extend Python's built-in `list`, `dict`, `tuple`, and `set`.

---

## Why Use collections?

Built-in types are versatile, but specialized containers offer:

- **Cleaner code**: Less boilerplate for common patterns
- **Better performance**: Optimized for specific use cases
- **Safer defaults**: Avoid common pitfalls (e.g., KeyError)

---

## Available Types

| Type | Description | Replaces |
|------|-------------|----------|
| `namedtuple` | Tuple with named fields | Plain tuple, simple class |
| `defaultdict` | Dict with default factory | Dict + `setdefault()` |
| `Counter` | Dict for counting | Dict + manual counting |
| `deque` | Double-ended queue | List (for queue operations) |
| `OrderedDict` | Dict with ordering features | Dict (mostly) |
| `ChainMap` | Multiple dicts as one view | Manual dict merging |

---

## Quick Comparison

### Without collections

```python
# Counting
counts = {}
for item in items:
    if item not in counts:
        counts[item] = 0
    counts[item] += 1

# Grouping
groups = {}
for item in items:
    key = get_key(item)
    if key not in groups:
        groups[key] = []
    groups[key].append(item)

# Queue operations (slow!)
queue = []
queue.append(item)      # O(1)
queue.pop(0)            # O(n) - shifts all elements
```

### With collections

```python
from collections import Counter, defaultdict, deque

# Counting
counts = Counter(items)

# Grouping
groups = defaultdict(list)
for item in items:
    groups[get_key(item)].append(item)

# Queue operations (fast!)
queue = deque()
queue.append(item)      # O(1)
queue.popleft()         # O(1)
```

---

## Import Patterns

```python
# Import specific types
from collections import namedtuple, defaultdict, Counter, deque

# Or import module
import collections
d = collections.defaultdict(list)
```

---

## When to Use Each

| Use Case | Type |
|----------|------|
| Lightweight record/struct | `namedtuple` |
| Grouping items by key | `defaultdict(list)` |
| Counting occurrences | `Counter` |
| Queue / BFS / sliding window | `deque` |
| LRU cache implementation | `OrderedDict` |
| Config layering | `ChainMap` |

---

## Summary

The `collections` module is essential for writing clean, efficient Python code. Master these types to avoid reinventing common patterns.
