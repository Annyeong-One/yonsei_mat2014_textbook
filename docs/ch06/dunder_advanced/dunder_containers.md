# Container Protocol

Container dunder methods enable your objects to behave like built-in collections.

## Core Container Methods

| Method | Called By | Description |
|--------|-----------|-------------|
| `__len__` | `len(obj)` | Return number of items |
| `__getitem__` | `obj[key]` | Get item by key/index |
| `__setitem__` | `obj[key] = value` | Set item by key/index |
| `__delitem__` | `del obj[key]` | Delete item by key/index |
| `__contains__` | `item in obj` | Check membership |

## __len__: Collection Length

```python
class Playlist:
    def __init__(self, songs=None):
        self._songs = songs or []
    
    def __len__(self):
        return len(self._songs)
    
    def add(self, song):
        self._songs.append(song)

playlist = Playlist(['Song A', 'Song B', 'Song C'])
print(len(playlist))  # 3

# Also enables bool() if __bool__ not defined
empty = Playlist()
if not empty:
    print("Playlist is empty")  # Prints this
```

## __getitem__: Item Access

### Index-Based Access

```python
class Sentence:
    def __init__(self, text):
        self._words = text.split()
    
    def __getitem__(self, index):
        return self._words[index]
    
    def __len__(self):
        return len(self._words)

s = Sentence("Hello World from Python")
print(s[0])      # Hello
print(s[-1])     # Python
print(s[1:3])    # ['World', 'from'] (slicing works!)
```

### Key-Based Access

```python
class Config:
    def __init__(self):
        self._data = {}
    
    def __getitem__(self, key):
        return self._data[key]
    
    def __setitem__(self, key, value):
        self._data[key] = value
    
    def __contains__(self, key):
        return key in self._data

config = Config()
config['debug'] = True
config['host'] = 'localhost'

print(config['debug'])      # True
print('debug' in config)    # True
print('missing' in config)  # False
```

### Handling Slices

```python
class MyList:
    def __init__(self, data):
        self._data = list(data)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            # Return a new MyList for slices
            return MyList(self._data[index])
        return self._data[index]
    
    def __setitem__(self, index, value):
        if isinstance(index, slice):
            self._data[index] = value
        else:
            self._data[index] = value
    
    def __repr__(self):
        return f"MyList({self._data})"

lst = MyList([1, 2, 3, 4, 5])
print(lst[1:4])       # MyList([2, 3, 4])
print(lst[::2])       # MyList([1, 3, 5])

lst[1:3] = [20, 30]
print(lst)            # MyList([1, 20, 30, 4, 5])
```

### Multi-Dimensional Access

```python
class Matrix:
    def __init__(self, rows, cols):
        self._data = [[0] * cols for _ in range(rows)]
        self._rows = rows
        self._cols = cols
    
    def __getitem__(self, key):
        if isinstance(key, tuple):
            row, col = key
            return self._data[row][col]
        # Single index returns entire row
        return self._data[key]
    
    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            row, col = key
            self._data[row][col] = value
        else:
            self._data[key] = value
    
    def __repr__(self):
        return f"Matrix({self._data})"

m = Matrix(3, 3)
m[0, 0] = 1
m[1, 1] = 5
m[2, 2] = 9
print(m[1, 1])   # 5
print(m[0])      # [1, 0, 0] (entire row)
```

## __setitem__: Item Assignment

```python
class DefaultDict:
    def __init__(self, default_factory):
        self._data = {}
        self._default = default_factory
    
    def __getitem__(self, key):
        if key not in self._data:
            self._data[key] = self._default()
        return self._data[key]
    
    def __setitem__(self, key, value):
        self._data[key] = value
    
    def __repr__(self):
        return f"DefaultDict({self._data})"

# Auto-create list for missing keys
dd = DefaultDict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
dd['vegetables'].append('carrot')

print(dd)  # DefaultDict({'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})
```

## __delitem__: Item Deletion

```python
class Registry:
    def __init__(self):
        self._items = {}
    
    def __setitem__(self, key, value):
        self._items[key] = value
    
    def __getitem__(self, key):
        return self._items[key]
    
    def __delitem__(self, key):
        if key not in self._items:
            raise KeyError(f"'{key}' not found")
        del self._items[key]
    
    def __contains__(self, key):
        return key in self._items
    
    def __repr__(self):
        return f"Registry({self._items})"

reg = Registry()
reg['user1'] = 'Alice'
reg['user2'] = 'Bob'
print(reg)          # Registry({'user1': 'Alice', 'user2': 'Bob'})

del reg['user1']
print(reg)          # Registry({'user2': 'Bob'})
print('user1' in reg)  # False
```

## __contains__: Membership Test

```python
class Range:
    """Efficient range membership testing."""
    
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __contains__(self, value):
        return self.start <= value < self.stop

r = Range(1, 100)
print(50 in r)   # True
print(100 in r)  # False
print(0 in r)    # False
```

### Without __contains__

If `__contains__` isn't defined, Python falls back to iteration:

```python
class NoContains:
    def __init__(self, data):
        self._data = data
    
    def __iter__(self):
        return iter(self._data)

nc = NoContains([1, 2, 3])
print(2 in nc)  # True (iterates through all items)
```

## __missing__: Dict Subclass Hook

`__missing__` is called by dict subclasses when a key isn't found.

```python
class AutoDict(dict):
    def __missing__(self, key):
        # Auto-create nested dicts
        self[key] = AutoDict()
        return self[key]

d = AutoDict()
d['a']['b']['c'] = 42
print(d)  # {'a': {'b': {'c': 42}}}
```

```python
class CountingDict(dict):
    def __init__(self):
        super().__init__()
        self.access_count = {}
    
    def __missing__(self, key):
        return 0  # Default value for missing keys
    
    def __getitem__(self, key):
        self.access_count[key] = self.access_count.get(key, 0) + 1
        return super().__getitem__(key) if key in self else self.__missing__(key)

cd = CountingDict()
cd['a'] = 1
print(cd['a'])     # 1
print(cd['a'])     # 1
print(cd['b'])     # 0 (missing, returns default)
print(cd.access_count)  # {'a': 2, 'b': 1}
```

## Practical Example: Sparse Matrix

```python
class SparseMatrix:
    """Memory-efficient matrix that only stores non-zero values."""
    
    def __init__(self, rows, cols, default=0):
        self._data = {}
        self.rows = rows
        self.cols = cols
        self.default = default
    
    def _validate_key(self, key):
        if not isinstance(key, tuple) or len(key) != 2:
            raise TypeError("Index must be a tuple (row, col)")
        row, col = key
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Index out of bounds")
    
    def __getitem__(self, key):
        self._validate_key(key)
        return self._data.get(key, self.default)
    
    def __setitem__(self, key, value):
        self._validate_key(key)
        if value == self.default:
            self._data.pop(key, None)  # Don't store default values
        else:
            self._data[key] = value
    
    def __delitem__(self, key):
        self._validate_key(key)
        self._data.pop(key, None)
    
    def __contains__(self, key):
        return key in self._data
    
    def __len__(self):
        return len(self._data)  # Number of non-default values
    
    def __repr__(self):
        return f"SparseMatrix({self.rows}x{self.cols}, {len(self)} non-zero)"

# Usage
m = SparseMatrix(1000, 1000)
m[0, 0] = 1
m[500, 500] = 42
m[999, 999] = -1

print(m[0, 0])      # 1
print(m[1, 1])      # 0 (default)
print(len(m))       # 3 (only 3 stored values)
print((500, 500) in m)  # True
print((1, 1) in m)      # False
```

## Sequence ABC Implementation

```python
from collections.abc import MutableSequence

class TypedList(MutableSequence):
    """List that only accepts items of a specific type."""
    
    def __init__(self, item_type, items=None):
        self._type = item_type
        self._data = []
        if items:
            for item in items:
                self.append(item)
    
    def _check_type(self, value):
        if not isinstance(value, self._type):
            raise TypeError(f"Expected {self._type.__name__}, got {type(value).__name__}")
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        self._check_type(value)
        self._data[index] = value
    
    def __delitem__(self, index):
        del self._data[index]
    
    def __len__(self):
        return len(self._data)
    
    def insert(self, index, value):
        self._check_type(value)
        self._data.insert(index, value)
    
    def __repr__(self):
        return f"TypedList[{self._type.__name__}]({self._data})"

# Usage
int_list = TypedList(int, [1, 2, 3])
int_list.append(4)
print(int_list)  # TypedList[int]([1, 2, 3, 4])

# int_list.append("five")  # TypeError: Expected int, got str
```

## Mapping ABC Implementation

```python
from collections.abc import MutableMapping

class CaseInsensitiveDict(MutableMapping):
    """Dictionary with case-insensitive string keys."""
    
    def __init__(self, data=None):
        self._data = {}
        if data:
            for key, value in data.items():
                self[key] = value
    
    def _normalize_key(self, key):
        if isinstance(key, str):
            return key.lower()
        return key
    
    def __getitem__(self, key):
        return self._data[self._normalize_key(key)]
    
    def __setitem__(self, key, value):
        self._data[self._normalize_key(key)] = value
    
    def __delitem__(self, key):
        del self._data[self._normalize_key(key)]
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)
    
    def __repr__(self):
        return f"CaseInsensitiveDict({self._data})"

# Usage
headers = CaseInsensitiveDict()
headers['Content-Type'] = 'application/json'
print(headers['content-type'])  # application/json
print(headers['CONTENT-TYPE'])  # application/json
print('content-type' in headers)  # True
```

## Key Takeaways

- `__len__` enables `len()` and boolean evaluation
- `__getitem__` enables indexing, slicing, and iteration fallback
- `__setitem__` enables item assignment with `[]`
- `__delitem__` enables item deletion with `del`
- `__contains__` enables `in` operator (falls back to iteration)
- `__missing__` is a dict-specific hook for missing keys
- Handle both integers and slices in `__getitem__` for sequence types
- Use `collections.abc` base classes for full protocol compliance
- Tuples as keys enable multi-dimensional access: `obj[row, col]`
