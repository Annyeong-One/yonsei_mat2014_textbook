# String Representation

String representation dunder methods control how objects are displayed, printed, and formatted.

---

## `__repr__` Method

### 1. Official Representation

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))  # Point(3, 4)
print(p)        # Point(3, 4)
```

### 2. For Developers

Aimed at developers, debugging, and logging.

### 3. Recreatable

Should ideally allow recreating the object.

```python
# Good __repr__
def __repr__(self):
    return f"Point({self.x}, {self.y})"

# Can recreate:
p2 = eval(repr(p))
```

---

## `__str__` Method

### 1. User-Friendly String

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(str(p))   # (3, 4)
print(repr(p))  # Point(3, 4)
```

### 2. For End Users

Readable output for users, not developers.

### 3. Called by `print()`

```python
print(p)  # Uses __str__ if defined
```

---

## `__repr__` vs `__str__`

### 1. Different Purposes

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

d = Date(2024, 1, 5)
print(repr(d))  # Date(2024, 1, 5)
print(str(d))   # 2024-01-05
```

### 2. Fallback Behavior

If `__str__` not defined, Python uses `__repr__`.

### 3. When to Use

- `__repr__`: debugging, development
- `__str__`: display to users

---

## Comparison Table

### 1. Key Differences

| Feature | `__repr__` | `__str__` |
|---------|-----------|----------|
| Purpose | Developer | User |
| Goal | Unambiguous | Readable |
| Called by | `repr()`, console | `str()`, `print()` |
| Fallback | Default | Uses `__repr__` |

### 2. Priority

Always implement `__repr__`, optionally `__str__`.

### 3. Best Practice

```python
# Minimum - just __repr__
def __repr__(self):
    return f"Point({self.x}, {self.y})"

# Better - both
def __repr__(self):
    return f"Point({self.x}, {self.y})"

def __str__(self):
    return f"({self.x}, {self.y})"
```

---

## Format Method

### 1. `__format__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __format__(self, fmt):
        if fmt == 'p':
            return f"({self.x}, {self.y})"
        elif fmt == 'c':
            return f"{self.x} + {self.y}i"
        else:
            return str(self)

p = Point(3, 4)
print(f"{p:p}")  # (3, 4)
print(f"{p:c}")  # 3 + 4i
```

### 2. Format Specifiers

```python
def __format__(self, fmt):
    if fmt == 'd':
        return f"{self.x}, {self.y}"
    elif fmt == 'v':
        return f"Vector: [{self.x}, {self.y}]"
    return str(self)
```

### 3. Called by f-strings

```python
print(f"Point: {p:v}")
```

---

## Bytes Representation

### 1. `__bytes__`

```python
class Data:
    def __init__(self, value):
        self.value = value
    
    def __bytes__(self):
        return self.value.encode('utf-8')

d = Data("Hello")
print(bytes(d))  # b'Hello'
```

### 2. Binary Protocols

Useful for network protocols and file formats.

### 3. Must Return Bytes

```python
def __bytes__(self):
    return bytes(self.data)  # Must be bytes object
```

---

## Complete Example

### 1. Employee Class

```python
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def __repr__(self):
        return f"Employee({self.name!r}, {self.employee_id!r}, {self.salary})"
    
    def __str__(self):
        return f"{self.name} (ID: {self.employee_id})"
    
    def __format__(self, fmt):
        if fmt == 'full':
            return f"{self.name} (ID: {self.employee_id}, Salary: ${self.salary:,})"
        elif fmt == 'short':
            return f"{self.name}"
        else:
            return str(self)
```

### 2. Usage

```python
e = Employee("Alice Smith", "EMP001", 75000)

print(repr(e))
# Employee('Alice Smith', 'EMP001', 75000)

print(str(e))
# Alice Smith (ID: EMP001)

print(f"{e:full}")
# Alice Smith (ID: EMP001, Salary: $75,000)

print(f"{e:short}")
# Alice Smith
```

### 3. Different Contexts

Each method serves different display needs.

---

## Best Practices

### 1. Always Define `__repr__`

```python
def __repr__(self):
    return f"{self.__class__.__name__}({self.x}, {self.y})"
```

### 2. Make `__repr__` Recreatable

```python
# Good - can eval() this
def __repr__(self):
    return f"Point(x={self.x}, y={self.y})"

# Works:
p2 = eval(repr(p))
```

### 3. Quote Strings in `__repr__`

```python
def __repr__(self):
    return f"Person(name={self.name!r}, age={self.age})"
    # !r adds quotes: Person(name='Alice', age=30)
```

---

## Container Representations

### 1. List-like

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    
    def __repr__(self):
        return f"Playlist({self.songs!r})"
    
    def __str__(self):
        return f"Playlist with {len(self.songs)} songs"

p = Playlist(["A", "B", "C"])
print(repr(p))  # Playlist(['A', 'B', 'C'])
print(str(p))   # Playlist with 3 songs
```

### 2. Dict-like

```python
class Config:
    def __init__(self, settings):
        self.settings = settings
    
    def __repr__(self):
        return f"Config({self.settings!r})"
    
    def __str__(self):
        items = ', '.join(f"{k}={v}" for k, v in self.settings.items())
        return f"Config({items})"
```

### 3. Show Contents

Include relevant internal state.

---

## Interactive Shell

### 1. Console Display

```python
>>> p = Point(3, 4)
>>> p
Point(3, 4)  # Uses __repr__
```

### 2. In Containers

```python
>>> points = [Point(1, 2), Point(3, 4)]
>>> points
[Point(1, 2), Point(3, 4)]  # Uses __repr__
```

### 3. Debugging

```python
import logging
logging.debug(f"Processing {p}")  # Uses __repr__
```

---

## Common Patterns

### 1. Simple Classes

```python
def __repr__(self):
    return f"{self.__class__.__name__}({self.value})"
```

### 2. Multiple Attributes

```python
def __repr__(self):
    attrs = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())
    return f"{self.__class__.__name__}({attrs})"
```

### 3. Custom Formatting

```python
def __str__(self):
    return f"{self.title} by {self.author} ({self.year})"
```

---

## Key Takeaways

- `__repr__`: for developers, debugging.
- `__str__`: for end users, display.
- `__format__`: custom format specifiers.
- Always implement `__repr__`.
- Make `__repr__` recreatable when possible.
- Use `!r` for string quoting in `__repr__`.
