# namedtuple


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

A **namedtuple** is a tuple subclass with named fields. It combines the immutability of tuples with the readability of classes.

---

## Creating Named Tuples

```python
from collections import namedtuple

# Define the type
Scientist = namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])

# Create instances
marie = Scientist('Marie Curie', 'physics', 1867, True)
einstein = Scientist(name='Albert Einstein', field='physics', born=1879, nobel=True)
```

### Alternative Field Definitions

```python
# Space-separated string
Point = namedtuple('Point', 'x y z')

# Comma-separated string
RGB = namedtuple('RGB', 'red, green, blue')

# List of strings
Person = namedtuple('Person', ['name', 'age', 'city'])
```

---

## Accessing Fields

### By Name (like class)

```python
Scientist = namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])
s = Scientist('Marie Curie', 'physics', 1867, True)

print(s.name)       # Marie Curie
print(s.field)      # physics
print(s.born)       # 1867
print(s.nobel)      # True
```

### By Index (like tuple)

```python
print(s[0])         # Marie Curie
print(s[1])         # physics
print(s[-1])        # True
```

### Slicing

```python
print(s[:2])        # ('Marie Curie', 'physics')
print(s[1:3])       # ('physics', 1867)
```

---

## Immutability

Named tuples are **immutable** like regular tuples:

```python
s = Scientist('Marie Curie', 'physics', 1867, True)

s.name = 'M Curie'  # AttributeError: can't set attribute
s[0] = 'M Curie'    # TypeError: 'Scientist' object does not support item assignment
```

### Creating Modified Copies

Use `_replace()` to create a new instance with some fields changed:

```python
s = Scientist('Marie Curie', 'physics', 1867, True)
s2 = s._replace(name='M. Curie', born=1867)
print(s2)           # Scientist(name='M. Curie', field='physics', born=1867, nobel=True)
print(s)            # Original unchanged
```

---

## Comparison with Regular Class

### Regular Class (Mutable)

```python
class Scientist:
    def __init__(self, name, field, born, nobel):
        self.name = name
        self.field = field
        self.born = born
        self.nobel = nobel

s = Scientist('Marie Curie', 'physics', 1867, True)
s.name = 'M Curie'  # Works! (mutable)
```

### namedtuple (Immutable)

```python
from collections import namedtuple
Scientist = namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])

s = Scientist('Marie Curie', 'physics', 1867, True)
s.name = 'M Curie'  # AttributeError (immutable)
```

---

## Utility Methods

Named tuples provide special methods (prefixed with `_`):

### `_fields`

```python
print(Scientist._fields)    # ('name', 'field', 'born', 'nobel')
```

### `_asdict()`

```python
s = Scientist('Marie Curie', 'physics', 1867, True)
print(s._asdict())
# {'name': 'Marie Curie', 'field': 'physics', 'born': 1867, 'nobel': True}
```

### `_make(iterable)`

```python
data = ['Albert Einstein', 'physics', 1879, True]
einstein = Scientist._make(data)
print(einstein)     # Scientist(name='Albert Einstein', ...)
```

---

## Default Values

Use `defaults` parameter (Python 3.7+):

```python
Scientist = namedtuple('Scientist', ['name', 'field', 'born', 'nobel'], 
                       defaults=[None, False])

# 'born' defaults to None, 'nobel' defaults to False
s = Scientist('Marie Curie', 'physics')
print(s)            # Scientist(name='Marie Curie', field='physics', born=None, nobel=False)
```

---

## Use Cases

### Function Return Values

```python
def get_user_info(user_id):
    UserInfo = namedtuple('UserInfo', ['name', 'email', 'active'])
    return UserInfo('Alice', 'alice@example.com', True)

info = get_user_info(123)
print(info.name)    # Alice (more readable than info[0])
```

### Database Records

```python
Row = namedtuple('Row', ['id', 'name', 'price'])
products = [
    Row(1, 'Apple', 1.50),
    Row(2, 'Banana', 0.75),
]
for p in products:
    print(f"{p.name}: ${p.price}")
```

### Coordinates and Points

```python
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(3, 4)
p2 = Point(0, 0)
distance = ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
```

---

## namedtuple vs typing.NamedTuple

For type hints, use `typing.NamedTuple`:

```python
from typing import NamedTuple

class Scientist(NamedTuple):
    name: str
    field: str
    born: int
    nobel: bool = False     # Default value

s = Scientist('Marie Curie', 'physics', 1867)
print(s.nobel)              # False
```

---

## Summary

| Feature | tuple | namedtuple | class |
|---------|-------|------------|-------|
| Access by index | ✅ | ✅ | ❌ |
| Access by name | ❌ | ✅ | ✅ |
| Mutable | ❌ | ❌ | ✅ |
| Hashable | ✅ | ✅ | Depends |
| Memory | Low | Low | Higher |

**Use namedtuple when:**
- You need readable field names
- Immutability is desired
- Memory efficiency matters
- Simple data container without methods
