# dict Methods

Python dictionaries provide many built-in methods for manipulation.

---

## Accessing Values

### `get(key[, default])`

Safe access without KeyError:

```python
d = {"a": 1, "b": 2}
d.get("a")          # 1
d.get("x")          # None
d.get("x", 0)       # 0 (custom default)
```

### `keys()`, `values()`, `items()`

Return view objects:

```python
d = {"a": 1, "b": 2}

d.keys()    # dict_keys(['a', 'b'])
d.values()  # dict_values([1, 2])
d.items()   # dict_items([('a', 1), ('b', 2)])
```

Views are dynamic — they reflect changes:

```python
keys = d.keys()
d["c"] = 3
print(list(keys))  # ['a', 'b', 'c']
```

---

## Adding / Updating

### `update(other)`

Merge another dict or iterable:

```python
d = {"a": 1}
d.update({"b": 2, "c": 3})
d.update([("d", 4)])
d.update(e=5)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

### `setdefault(key[, default])`

Get value if exists, else set and return default:

```python
d = {"a": 1}
d.setdefault("a", 10)   # Returns 1, d unchanged
d.setdefault("b", 10)   # Returns 10, d = {"a": 1, "b": 10}
```

Useful for grouping:

```python
groups = {}
for word in ["apple", "ant", "banana"]:
    groups.setdefault(word[0], []).append(word)
# {'a': ['apple', 'ant'], 'b': ['banana']}
```

---

## Removing Items

### `pop(key[, default])`

Remove and return value:

```python
d = {"a": 1, "b": 2}
d.pop("a")          # Returns 1, d = {"b": 2}
d.pop("x")          # KeyError!
d.pop("x", None)    # Returns None, no error
```

### `popitem()`

Remove and return last item (LIFO):

```python
d = {"a": 1, "b": 2, "c": 3}
d.popitem()         # ('c', 3)
print(d)            # {'a': 1, 'b': 2}
```

### `del` Statement

```python
del d["a"]          # KeyError if missing
```

### `clear()`

Remove all items:

```python
d = {"a": 1, "b": 2}
d.clear()           # {}
```

---

## Copying

### `copy()`

Shallow copy:

```python
d = {"a": [1, 2]}
d2 = d.copy()
d["a"].append(3)
print(d2)           # {"a": [1, 2, 3]} — nested list shared!
```

For deep copy:

```python
import copy
d2 = copy.deepcopy(d)
```

---

## Creating from Keys

### `dict.fromkeys(keys[, value])`

Create dict with keys from iterable:

```python
dict.fromkeys(["a", "b", "c"])       # {'a': None, 'b': None, 'c': None}
dict.fromkeys(["a", "b"], 0)         # {'a': 0, 'b': 0}
```

**Warning**: Mutable default is shared:

```python
d = dict.fromkeys(["a", "b"], [])
d["a"].append(1)
print(d)            # {'a': [1], 'b': [1]} — same list!
```

---

## Comparison Summary

| Method | Action | Returns | Modifies Dict |
|--------|--------|---------|---------------|
| `get(k)` | Access safely | Value or None | No |
| `keys()` | All keys | View | No |
| `values()` | All values | View | No |
| `items()` | All pairs | View | No |
| `update(d2)` | Merge | None | Yes |
| `setdefault(k, v)` | Get or set | Value | Maybe |
| `pop(k)` | Remove by key | Value | Yes |
| `popitem()` | Remove last | Tuple | Yes |
| `clear()` | Remove all | None | Yes |
| `copy()` | Shallow copy | New dict | No |

---

## collections.Counter

For counting, use `Counter` instead of manual dict:

```python
from collections import Counter

text = "hello"
c = Counter(text)       # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
c["l"]                  # 2
c["z"]                  # 0 (no KeyError!)
c.most_common(2)        # [('l', 2), ('h', 1)]
```

---

## collections.defaultdict

Auto-create missing keys:

```python
from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)        # No KeyError
d["a"].append(2)
print(d)                # defaultdict(<class 'list'>, {'a': [1, 2]})

d = defaultdict(int)
d["x"] += 1             # No KeyError
print(d["x"])           # 1
```
