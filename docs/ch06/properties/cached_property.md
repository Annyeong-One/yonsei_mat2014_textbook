# Cached Properties

## Concept

### 1. What Is Caching?

A **cached property** computes its value **once** on first access, stores the result inside the instance (usually in `__dict__`), and on future accesses, just returns the cached value — skipping recomputation.

### 2. When to Use

Use cached properties when:

- Computation is expensive (database queries, heavy calculations)
- Result doesn't change after first computation
- Want to trade memory for speed
- Need lazy evaluation

### 3. Built-in vs Custom

- **Python ≥ 3.8**: `@functools.cached_property`
- **Custom**: Build your own using descriptors

## Custom Implementation

### 1. Descriptor Class

```python
class CachedProperty:
    def __init__(self, func):
        self.func = func
        self.__doc__ = func.__doc__
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name not in instance.__dict__:
            print(f"Computing and caching: {self.name}")
            instance.__dict__[self.name] = self.func(instance)
        else:
            print(f"Using cached value: {self.name}")
        return instance.__dict__[self.name]
```

### 2. Using Custom Descriptor

```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @CachedProperty
    def area(self):
        print("Calculating area...")
        return math.pi * self.radius ** 2

    @CachedProperty
    def perimeter(self):
        print("Calculating perimeter...")
        return 2 * math.pi * self.radius
```

### 3. Behavior Example

```python
c = Circle(10)

print(c.area)      # → Calculates and caches
# Output: Computing and caching: area
#         Calculating area...
#         314.159...

print(c.area)      # → Uses cached value
# Output: Using cached value: area
#         314.159...
```

## How It Works

### 1. Initialization

When you decorate:

```python
@CachedProperty
def area(self):
    ...
```

You are doing at class definition time:

```python
Circle.area = CachedProperty(area)
```

The `CachedProperty.__init__` stores:
- `self.func = area` → original method
- `self.__doc__ = area.__doc__` → docstring
- `self.name = 'area'` → attribute name

### 2. First Access

When you do `c.area`, Python calls:

```python
Circle.area.__get__(c, Circle)
```

Inside `__get__`:

1. Check if `instance is None` (class access) → return descriptor
2. Check if `'area'` in `instance.__dict__` → not yet
3. Compute: `instance.__dict__['area'] = self.func(instance)`
4. Return cached value

### 3. Subsequent Access

When you do `c.area` again:

1. Check if `instance is None` → no
2. Check if `'area'` in `instance.__dict__` → **yes, found!**
3. Skip computation, return cached value directly

## Built-in Version

### 1. Using functools

Python 3.8+ provides built-in cached property:

```python
from functools import cached_property

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        print("Computing area...")
        return math.pi * self.radius ** 2
```

### 2. Behavior

```python
c = Circle(10)
print(c.area)  # Computing area... 314.159...
print(c.area)  # 314.159... (no recomputation)
```

### 3. Clearing Cache

To clear cached value:

```python
del c.area  # Remove from instance.__dict__
print(c.area)  # Recomputes
```

## Practical Examples

### 1. Database Query

```python
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    
    @cached_property
    def profile(self):
        print(f"Fetching profile for user {self.user_id}...")
        # Expensive database query
        return db.query(f"SELECT * FROM users WHERE id={self.user_id}")
```

### 2. File Reading

```python
class ConfigFile:
    def __init__(self, path):
        self.path = path
    
    @cached_property
    def data(self):
        print(f"Reading {self.path}...")
        with open(self.path) as f:
            return f.read()
```

### 3. Complex Computation

```python
class Matrix:
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def determinant(self):
        print("Computing determinant...")
        # Expensive calculation
        return self._compute_determinant()
```

## Comparison Table

### 1. Property vs Cached Property

| Feature | `@property` | `@cached_property` |
|---------|-------------|-------------------|
| Computation | Every access | Once on first access |
| Storage | Not stored | Stored in `__dict__` |
| Speed | Slower | Faster after first |
| Memory | Less | More |
| Use case | Dynamic values | Static expensive values |

### 2. When to Choose

**Use `@property` when:**
- Value changes over time
- Computation is cheap
- Need fresh value each time

**Use `@cached_property` when:**
- Value is constant after creation
- Computation is expensive
- Multiple accesses expected
