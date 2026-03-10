# defaultdict


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

A `defaultdict` is a dict subclass that automatically creates missing keys using a factory function.

---

## The Problem

Regular dicts raise `KeyError` for missing keys:

```python
# Regular dict: must check or use setdefault
groups = {}
for name, category in data:
    if category not in groups:
        groups[category] = []
    groups[category].append(name)

# Or using setdefault (verbose)
groups = {}
for name, category in data:
    groups.setdefault(category, []).append(name)
```

---

## The Solution

```python
from collections import defaultdict

groups = defaultdict(list)
for name, category in data:
    groups[category].append(name)  # Auto-creates empty list!
```

---

## How It Works

```python
from collections import defaultdict

d = defaultdict(list)   # Factory function: list

# Accessing missing key:
# 1. Calls list() to create []
# 2. Assigns d['new_key'] = []
# 3. Returns the empty list

d['fruits'].append('apple')
print(d)  # defaultdict(<class 'list'>, {'fruits': ['apple']})
```

---

## Common Factory Functions

### `list` — Grouping

```python
from collections import defaultdict

data = [('apple', 'fruit'), ('carrot', 'vegetable'), 
        ('banana', 'fruit'), ('broccoli', 'vegetable')]

groups = defaultdict(list)
for item, category in data:
    groups[category].append(item)

print(dict(groups))
# {'fruit': ['apple', 'banana'], 'vegetable': ['carrot', 'broccoli']}
```

### `int` — Counting

```python
counts = defaultdict(int)  # int() returns 0

for char in 'mississippi':
    counts[char] += 1

print(dict(counts))
# {'m': 1, 'i': 4, 's': 4, 'p': 2}
```

### `set` — Unique Grouping

```python
tags = defaultdict(set)

data = [('doc1', 'python'), ('doc1', 'tutorial'), 
        ('doc2', 'python'), ('doc1', 'python')]  # duplicate

for doc, tag in data:
    tags[doc].add(tag)

print(dict(tags))
# {'doc1': {'python', 'tutorial'}, 'doc2': {'python'}}
```

### `lambda` — Custom Default

```python
# Default value 'N/A'
d = defaultdict(lambda: 'N/A')
d['name'] = 'Alice'
print(d['name'])    # Alice
print(d['age'])     # N/A

# Default value 0.0
prices = defaultdict(lambda: 0.0)
prices['apple'] = 1.50
print(prices['banana'])  # 0.0
```

---

## Nested defaultdict

### Two Levels

```python
# year -> month -> count
stats = defaultdict(lambda: defaultdict(int))

stats['2024']['Jan'] += 100
stats['2024']['Feb'] += 200
stats['2025']['Jan'] += 150

print(stats['2024']['Jan'])  # 100
print(stats['2024']['Mar'])  # 0 (auto-created)
```

### Three Levels

```python
# country -> city -> category -> count
data = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

data['USA']['NYC']['sales'] += 1000
data['USA']['NYC']['returns'] += 50
data['USA']['LA']['sales'] += 800
```

---

## Converting to Regular Dict

```python
d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)

# Convert to regular dict
regular = dict(d)
print(regular)  # {'a': [1], 'b': [2]}

# Nested conversion
import json
print(json.dumps(dict(d)))  # Works after conversion
```

---

## defaultdict vs setdefault

| Aspect | `defaultdict` | `setdefault` |
|--------|---------------|--------------|
| Syntax | `d[key].append(x)` | `d.setdefault(key, []).append(x)` |
| Readability | ✅ Clean | ❌ Verbose |
| Creates on read | ✅ Yes | ❌ No |
| Regular dict | ❌ No | ✅ Yes |

```python
# defaultdict: creates key even on read
d = defaultdict(list)
_ = d['key']          # Creates empty list
print('key' in d)     # True

# setdefault: only creates on explicit call
d = {}
_ = d.get('key', [])  # Does NOT create
print('key' in d)     # False
```

---

## Practical Examples

### Word Index

```python
from collections import defaultdict

text = "the quick brown fox jumps over the lazy dog"
index = defaultdict(list)

for pos, word in enumerate(text.split()):
    index[word].append(pos)

print(dict(index))
# {'the': [0, 6], 'quick': [1], 'brown': [2], ...}
```

### Graph Adjacency List

```python
graph = defaultdict(list)

edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')]
for src, dst in edges:
    graph[src].append(dst)
    graph[dst].append(src)  # Undirected

print(dict(graph))
# {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D'], 'D': ['C']}
```

### Frequency Table

```python
from collections import defaultdict

scores = [85, 90, 85, 78, 90, 90, 85]
freq = defaultdict(int)

for score in scores:
    freq[score] += 1

print(dict(freq))  # {85: 3, 90: 3, 78: 1}
```

---

## Key Takeaways

- `defaultdict(factory)` auto-creates missing keys
- Common factories: `list`, `int`, `set`, `lambda`
- Cleaner than `setdefault()` for grouping/counting
- Use `dict(d)` to convert to regular dict
- Accessing missing key creates it (unlike regular dict)
