# `dict` and Hash Tables

A **dictionary** maps keys to values using a hash table. It is one of Python's most powerful and widely used data types.

---

## Creating Dictionaries

```python
d = {"a": 1, "b": 2}
empty = {}
```

### Alternative Construction

```python
dict(a=1, b=2)                    # {'a': 1, 'b': 2}
dict([('a', 1), ('b', 2)])        # From list of tuples
dict.fromkeys(['a', 'b'], 0)      # {'a': 0, 'b': 0}
```

---

## Keys Must Be Hashable

Keys must be immutable (hashable):

```python
d = {"string": 1}       # ✓ str
d = {42: "value"}       # ✓ int
d = {(1, 2): "tuple"}   # ✓ tuple (if elements hashable)

d = {[1, 2]: "list"}    # ✗ TypeError: unhashable type: 'list'
```

### The int/float Key Gotcha

```python
d = {1: "int", 1.0: "float"}
print(d)    # {1: 'float'}
```

Since `1 == 1.0` and `hash(1) == hash(1.0)`, they're the same key — later value wins.

---

## Basic Operations

### Access

```python
d = {"a": 1, "b": 2}
d["a"]          # 1
d["x"]          # KeyError!
d.get("x")      # None (no error)
d.get("x", 0)   # 0 (default)
```

### Add / Update

```python
d["c"] = 3      # Add new key
d["a"] = 10     # Update existing
```

### Delete

```python
del d["a"]              # KeyError if missing
d.pop("b")              # Remove and return value
d.pop("x", None)        # No error with default
```

---

## Iteration

```python
d = {"a": 1, "b": 2}

for key in d:           # Keys (default)
    print(key)

for key in d.keys():    # Explicit keys
    print(key)

for val in d.values():  # Values only
    print(val)

for k, v in d.items():  # Key-value pairs
    print(k, v)
```

---

## Membership Testing

```python
"a" in d        # True (checks keys)
"x" not in d    # True
```

---

## Merging Dictionaries

### Using `update()`

```python
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)   # d1 = {"a": 1, "b": 2}
```

### Using `**` Unpacking (Python 3.5+)

```python
d = {**d1, **d2}    # New dict, later wins on conflicts
```

### Using `|` Operator (Python 3.9+)

```python
d = d1 | d2         # New dict
d1 |= d2            # Update in-place
```

---

## Dict Unpacking

```python
d = {"a": 1, "b": 2}

# Unpack keys
a, b = d
print(a, b)     # 'a' 'b'

# Unpack items
for k, v in d.items():
    print(k, v)
```

---

## Hash Table Internals

### How Lookup Works

1. Compute `hash(key)`
2. Find slot: `index = hash(key) & (table_size - 1)`
3. If collision, probe next slot
4. Compare `hash` then `key == stored_key`

### Time Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Lookup | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |

Worst case is rare with good hash distribution.

### Why Keys Must Be Immutable

- Hash is computed from key's value
- If key changes, hash changes
- Key becomes "lost" in wrong slot

---

## Insertion Order

Since Python 3.7, dictionaries maintain **insertion order**:

```python
d = {"c": 3, "a": 1, "b": 2}
list(d.keys())  # ['c', 'a', 'b']
```

---

## Common Patterns

### Counting

```python
text = "hello"
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

Or use `collections.Counter`:

```python
from collections import Counter
counts = Counter(text)
counts.most_common(2)  # [('l', 2), ('h', 1)]
```

### Grouping

```python
words = ["apple", "ant", "banana", "bear"]
groups = {}
for word in words:
    key = word[0]
    groups.setdefault(key, []).append(word)
# {'a': ['apple', 'ant'], 'b': ['banana', 'bear']}
```

---

## Key Takeaways

- Dictionaries are hash tables with O(1) average operations
- Keys must be immutable (hashable)
- `1` and `1.0` are the same key (equal values, equal hashes)
- Insertion order preserved since Python 3.7
- Use `get()` to avoid KeyError
- Use `Counter` for counting, `defaultdict` for grouping
