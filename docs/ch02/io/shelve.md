# shelve Module


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The shelve module provides persistent dictionary storage using DBM backend. It is simpler than databases for small data persistence needs, storing Python objects as pickled values.

---

## Basic Usage

### Creating a Shelf

```python
import shelve
import tempfile
import os

tmpdir = tempfile.mkdtemp()
shelf_path = os.path.join(tmpdir, 'myshelf')

with shelve.open(shelf_path) as shelf:
    shelf['key1'] = 'value1'
    shelf['key2'] = [1, 2, 3]
    shelf['key3'] = {'nested': 'dict'}

with shelve.open(shelf_path) as shelf:
    print(shelf['key1'])
    print(shelf['key2'])

for f in os.listdir(tmpdir):
    os.remove(os.path.join(tmpdir, f))
os.rmdir(tmpdir)
```

Output:
```
value1
[1, 2, 3]
```

## Shelf Operations

### Dictionary-like Interface

```python
import shelve
import tempfile
import os

tmpdir = tempfile.mkdtemp()
shelf_path = os.path.join(tmpdir, 'test')

with shelve.open(shelf_path) as shelf:
    shelf['name'] = 'Alice'
    shelf['age'] = 30
    
    print(f"Keys: {list(shelf.keys())}")
    print(f"Values: {list(shelf.values())}")
    print(f"'name' in shelf: {'name' in shelf}")

for f in os.listdir(tmpdir):
    os.remove(os.path.join(tmpdir, f))
os.rmdir(tmpdir)
```

Output:
```
Keys: ['name', 'age']
Values: ['Alice', 30]
'name' in shelf: True
```

## Mutable Objects

### Updating Nested Data

```python
import shelve
import tempfile
import os

tmpdir = tempfile.mkdtemp()
shelf_path = os.path.join(tmpdir, 'test')

with shelve.open(shelf_path) as shelf:
    shelf['data'] = {'count': 0}

with shelve.open(shelf_path) as shelf:
    data = shelf['data']
    data['count'] += 1
    shelf['data'] = data

with shelve.open(shelf_path) as shelf:
    print(f"Updated: {shelf['data']}")

for f in os.listdir(tmpdir):
    os.remove(os.path.join(tmpdir, f))
os.rmdir(tmpdir)
```

Output:
```
Updated: {'count': 1}
```

## Practical Applications

### Configuration Storage

```python
import shelve
import tempfile
import os

tmpdir = tempfile.mkdtemp()
shelf_path = os.path.join(tmpdir, 'config')

with shelve.open(shelf_path) as config:
    config['theme'] = 'dark'
    config['language'] = 'en'

with shelve.open(shelf_path) as config:
    theme = config.get('theme', 'light')
    print(f"Theme: {theme}")

for f in os.listdir(tmpdir):
    os.remove(os.path.join(tmpdir, f))
os.rmdir(tmpdir)
```

Output:
```
Theme: dark
```
