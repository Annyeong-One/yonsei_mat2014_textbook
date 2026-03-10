# Read-Only Properties


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Creating Read-Only

### 1. Property Without Setter

The simplest way to create a read-only property is to define only the getter:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def area(self):
        from math import pi
        return pi * self._radius ** 2
```

### 2. Attempting to Write

```python
c = Circle(5)
print(c.area)  # ✅ Works: 78.54...
c.area = 100   # ❌ AttributeError: can't set attribute
```

### 3. Why Use Read-Only

- Prevent accidental modification of computed values
- Enforce immutability for specific attributes
- Maintain data consistency
- Express design intent clearly

## Common Patterns

### 1. Computed Values

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    @property
    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
```

### 2. Derived Attributes

```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}."
```

### 3. Configuration Values

```python
class Config:
    def __init__(self):
        self._api_key = "secret123"
    
    @property
    def api_endpoint(self):
        return "https://api.example.com/v1"
    
    @property
    def max_retries(self):
        return 3
```

## Protecting Internal State

### 1. Private Attribute Pattern

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    @property
    def balance(self):
        """Read-only access to balance"""
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
```

### 2. Why This Works

- `_balance` is private (convention)
- `balance` property provides read-only access
- Modifications only through controlled methods
- Maintains invariants

### 3. Usage Example

```python
account = BankAccount(1000)
print(account.balance)  # ✅ 1000
account.deposit(500)    # ✅ Works
# account.balance = 5000  # ❌ Can't set attribute
```

## Immutable Objects

### 1. Full Immutability

```python
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def magnitude(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5
```

### 2. Benefits

- Thread-safe by design
- Can be used as dictionary keys
- Easier to reason about
- Prevents bugs from state mutation

### 3. Creating New Instances

```python
class Point:
    # ... (properties as above)
    
    def move(self, dx, dy):
        """Returns new Point with offset"""
        return Point(self._x + dx, self._y + dy)
```

## Advanced Patterns

### 1. Conditional Read-Only

Make property read-only based on state:

```python
class Document:
    def __init__(self):
        self._content = ""
        self._locked = False
    
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        if self._locked:
            raise AttributeError("Document is locked")
        self._content = value
    
    def lock(self):
        self._locked = True
```

### 2. Lazy Evaluation

```python
class ExpensiveCalculation:
    def __init__(self, data):
        self._data = data
        self._result = None
    
    @property
    def result(self):
        """Computed once, then cached"""
        if self._result is None:
            print("Computing...")
            self._result = sum(x**2 for x in self._data)
        return self._result
```

### 3. Type Conversion

```python
class DataRecord:
    def __init__(self, timestamp_str):
        self._timestamp_str = timestamp_str
    
    @property
    def timestamp(self):
        """Always returns datetime object"""
        from datetime import datetime
        return datetime.fromisoformat(self._timestamp_str)
```

## Comparison

### 1. Read-Only vs Writable

| Aspect | Read-Only Property | Writable Property |
|--------|-------------------|-------------------|
| Setter | Not defined | Defined |
| Assignment | Raises error | Allowed |
| Use case | Computed/protected values | Validated attributes |
| Mutability | Immutable | Mutable |

### 2. Enforcement Levels

| Method | Enforcement | Access |
|--------|-------------|--------|
| Public attribute | None | `obj.x = 5` works |
| `_private` convention | Social | `obj._x = 5` discouraged |
| Read-only property | Strong | `obj.x = 5` raises error |

### 3. Design Principles

**Use read-only properties when:**
- Value is derived from other state
- External modification would break invariants
- Expressing configuration or constants
- Implementing immutable data structures
