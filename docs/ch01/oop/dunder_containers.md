# Container Methods

Container dunder methods enable sequence operations like indexing, iteration, length, and membership testing.

---

## Length Method

### 1. `__len__`

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    
    def __len__(self):
        return len(self.songs)

playlist = Playlist(["Song1", "Song2", "Song3"])
print(len(playlist))  # 3
```

### 2. Built-in Integration

Works with built-in `len()` function.

### 3. Must Return Integer

```python
def __len__(self):
    return len(self.items)  # Must be int
```

---

## Indexing: `__getitem__`

### 1. Get by Index

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    
    def __getitem__(self, index):
        return self.songs[index]

playlist = Playlist(["A", "B", "C"])
print(playlist[0])  # "A"
print(playlist[1])  # "B"
```

### 2. Negative Indexing

```python
print(playlist[-1])  # "C"
```

### 3. Slicing Support

```python
def __getitem__(self, index):
    return self.songs[index]  # Handles slices too

print(playlist[0:2])  # ["A", "B"]
```

---

## Setting Items

### 1. `__setitem__`

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    
    def __setitem__(self, index, value):
        self.songs[index] = value

playlist = Playlist(["A", "B", "C"])
playlist[1] = "X"
print(playlist.songs)  # ["A", "X", "C"]
```

### 2. Validation

```python
def __setitem__(self, index, value):
    if not isinstance(value, str):
        raise TypeError("Songs must be strings")
    self.songs[index] = value
```

### 3. Slice Assignment

```python
def __setitem__(self, index, value):
    self.songs[index] = value

playlist[0:2] = ["X", "Y"]
```

---

## Deleting Items

### 1. `__delitem__`

```python
class Playlist:
    def __delitem__(self, index):
        del self.songs[index]

playlist = Playlist(["A", "B", "C"])
del playlist[1]
print(playlist.songs)  # ["A", "C"]
```

### 2. Supports Slices

```python
del playlist[0:2]  # Delete range
```

### 3. Error Handling

```python
def __delitem__(self, index):
    if index < 0 or index >= len(self.songs):
        raise IndexError("Index out of range")
    del self.songs[index]
```

---

## Membership: `__contains__`

### 1. In Operator

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    
    def __contains__(self, item):
        return item in self.songs

playlist = Playlist(["A", "B", "C"])
print("A" in playlist)  # True
print("X" in playlist)  # False
```

### 2. Not In

```python
print("X" not in playlist)  # True
```

### 3. Custom Logic

```python
def __contains__(self, item):
    # Case-insensitive search
    return item.lower() in [s.lower() for s in self.songs]
```

---

## Iteration: `__iter__`

### 1. Iterator Protocol

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    
    def __iter__(self):
        return iter(self.songs)

playlist = Playlist(["A", "B", "C"])
for song in playlist:
    print(song)
```

### 2. Generator Pattern

```python
def __iter__(self):
    for song in self.songs:
        yield song
```

### 3. Enables Unpacking

```python
a, b, c = playlist
```

---

## Reversed Iteration

### 1. `__reversed__`

```python
class Playlist:
    def __reversed__(self):
        return reversed(self.songs)

playlist = Playlist(["A", "B", "C"])
for song in reversed(playlist):
    print(song)  # C, B, A
```

### 2. Default Behavior

If not defined, Python tries `__getitem__` and `__len__`.

### 3. Custom Logic

```python
def __reversed__(self):
    return iter(self.songs[::-1])
```

---

## Complete Container

### 1. Full Implementation

```python
class Playlist:
    def __init__(self, songs):
        self.songs = list(songs)
    
    def __len__(self):
        return len(self.songs)
    
    def __getitem__(self, index):
        return self.songs[index]
    
    def __setitem__(self, index, value):
        self.songs[index] = value
    
    def __delitem__(self, index):
        del self.songs[index]
    
    def __contains__(self, item):
        return item in self.songs
    
    def __iter__(self):
        return iter(self.songs)
    
    def __reversed__(self):
        return reversed(self.songs)
    
    def __repr__(self):
        return f"Playlist({self.songs})"
```

### 2. Usage Examples

```python
p = Playlist(["A", "B", "C"])

print(len(p))           # 3
print(p[1])             # "B"
p[1] = "X"              # Set item
del p[0]                # Delete item
print("X" in p)         # True
for song in p: ...      # Iterate
```

### 3. Behaves Like List

Container methods make custom classes list-like.

---

## Mapping Protocol

### 1. Dictionary-like

```python
class Config:
    def __init__(self):
        self.data = {}
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __delitem__(self, key):
        del self.data[key]
    
    def __contains__(self, key):
        return key in self.data

config = Config()
config["debug"] = True
print(config["debug"])
```

### 2. Keys Method

```python
def keys(self):
    return self.data.keys()
```

### 3. Items Method

```python
def items(self):
    return self.data.items()
```

---

## Sequence vs Mapping

### 1. Sequence

```python
# Integer indices
def __getitem__(self, index: int):
    return self.items[index]
```

### 2. Mapping

```python
# Any hashable key
def __getitem__(self, key):
    return self.data[key]
```

### 3. Choose Protocol

Sequence for ordered collections, mapping for key-value.

---

## Missing Method

### 1. `__missing__`

```python
class DefaultDict:
    def __init__(self, default_factory):
        self.data = {}
        self.default_factory = default_factory
    
    def __getitem__(self, key):
        if key not in self.data:
            return self.__missing__(key)
        return self.data[key]
    
    def __missing__(self, key):
        value = self.default_factory()
        self.data[key] = value
        return value

d = DefaultDict(list)
d["key"].append(1)  # Creates list automatically
```

### 2. Auto-Vivification

Automatically creates missing values.

### 3. Used by `dict`

Python's `dict` calls `__missing__` if defined.

---

## Context Managers

### 1. `__enter__` and `__exit__`

```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False

with FileManager("data.txt") as f:
    f.write("Hello")
```

### 2. Resource Management

Ensures cleanup even with exceptions.

### 3. Return Value

`__enter__` returns value bound to `as` clause.

---

## Best Practices

### 1. Implement Complete Set

```python
# For sequences, implement:
__len__, __getitem__, __setitem__, __delitem__
__contains__, __iter__
```

### 2. Delegate to Built-ins

```python
def __getitem__(self, index):
    return self.items[index]  # Delegate to list
```

### 3. Handle Edge Cases

```python
def __getitem__(self, index):
    if not isinstance(index, int):
        raise TypeError("Index must be integer")
    return self.items[index]
```

---

## Key Takeaways

- `__len__` enables `len()` function.
- `__getitem__` enables indexing and slicing.
- `__setitem__` and `__delitem__` for modification.
- `__contains__` enables `in` operator.
- `__iter__` makes objects iterable.
- Implement full protocol for consistency.
