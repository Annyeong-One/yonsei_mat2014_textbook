# dataclasses


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The `dataclasses` module (Python 3.7+) automatically generates boilerplate code for classes that primarily store data. It reduces repetitive `__init__`, `__repr__`, `__eq__`, and other methods.

```python
from dataclasses import dataclass, field
```

---

## The Problem: Boilerplate

Without dataclasses, simple data containers require lots of repetitive code:

```python
# Traditional approach - verbose!
class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))
```

---

## The Solution: @dataclass

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0

# All of this is auto-generated:
p = Point(1.0, 2.0)
print(p)              # Point(x=1.0, y=2.0, z=0.0)
print(p == Point(1.0, 2.0))  # True
```

---

## Basic Usage

### Defining Fields

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = ""  # Default value

# Positional or keyword arguments
p1 = Person("Alice", 30)
p2 = Person(name="Bob", age=25, email="bob@example.com")

print(p1)  # Person(name='Alice', age=30, email='')
```

### Type Hints are Required

```python
@dataclass
class Item:
    name: str        # Required
    price: float     # Required
    quantity: int = 1  # Optional with default
    
    # Without type hint - NOT a field!
    category = "general"  # Class attribute, not instance field
```

### Field Ordering

Fields with defaults must come after fields without defaults:

```python
@dataclass
class Product:
    name: str          # No default - must be first
    id: int            # No default
    price: float = 0.0  # Has default - must be after
    stock: int = 0      # Has default
```

---

## Decorator Parameters

```python
@dataclass(
    init=True,       # Generate __init__
    repr=True,       # Generate __repr__
    eq=True,         # Generate __eq__
    order=False,     # Generate __lt__, __le__, __gt__, __ge__
    unsafe_hash=False,  # Force __hash__ generation
    frozen=False,    # Make instances immutable
    match_args=True, # Enable pattern matching (3.10+)
    kw_only=False,   # All fields keyword-only (3.10+)
    slots=False,     # Use __slots__ (3.10+)
)
class MyClass:
    ...
```

### Common Configurations

```python
# Immutable (like a named tuple)
@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float

p = ImmutablePoint(1.0, 2.0)
# p.x = 3.0  # FrozenInstanceError!

# Sortable
@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int = 0

versions = [Version(2, 0), Version(1, 5), Version(1, 10)]
print(sorted(versions))
# [Version(major=1, minor=5, patch=0), Version(major=1, minor=10, patch=0), ...]

# Memory efficient (Python 3.10+)
@dataclass(slots=True)
class EfficientPoint:
    x: float
    y: float
```

---

## The field() Function

For advanced field configuration:

```python
from dataclasses import dataclass, field

@dataclass
class Config:
    name: str
    tags: list = field(default_factory=list)  # Mutable default
    _id: int = field(default=0, repr=False)   # Hidden from repr
    computed: str = field(init=False)          # Not in __init__
    
    def __post_init__(self):
        self.computed = f"{self.name}-{self._id}"
```

### field() Parameters

| Parameter | Description |
|-----------|-------------|
| `default` | Default value (for immutables) |
| `default_factory` | Callable for mutable defaults |
| `repr` | Include in `__repr__` |
| `hash` | Include in `__hash__` |
| `compare` | Include in comparisons |
| `init` | Include in `__init__` |
| `kw_only` | Keyword-only argument (3.10+) |

### Mutable Default Values

**Never use mutable defaults directly!**

```python
# ✗ WRONG - shared mutable default
@dataclass
class Bad:
    items: list = []  # All instances share same list!

# ✓ CORRECT - factory function
@dataclass
class Good:
    items: list = field(default_factory=list)
```

---

## __post_init__

Called after `__init__` for additional initialization:

```python
from dataclasses import dataclass, field

@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)
    
    def __post_init__(self):
        self.area = self.width * self.height

r = Rectangle(5, 10)
print(r.area)  # 50.0
```

### Validation in __post_init__

```python
@dataclass
class Person:
    name: str
    age: int
    
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        if not self.name:
            raise ValueError("Name cannot be empty")
```

---

## Inheritance

```python
from dataclasses import dataclass

@dataclass
class Animal:
    name: str
    age: int

@dataclass
class Dog(Animal):
    breed: str
    
dog = Dog("Buddy", 3, "Labrador")
print(dog)  # Dog(name='Buddy', age=3, breed='Labrador')
```

### Field Ordering with Inheritance

```python
@dataclass
class Base:
    x: int
    y: int = 0  # Has default

@dataclass
class Child(Base):
    z: int  # No default - ERROR! Would come after y
    
# Fix: Give z a default too
@dataclass
class Child(Base):
    z: int = 0  # Now valid
```

---

## Conversion Methods

### asdict() and astuple()

```python
from dataclasses import dataclass, asdict, astuple

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0

p = Point(1.0, 2.0, 3.0)

# Convert to dict
d = asdict(p)
print(d)  # {'x': 1.0, 'y': 2.0, 'z': 3.0}

# Convert to tuple
t = astuple(p)
print(t)  # (1.0, 2.0, 3.0)
```

### Nested Dataclasses

```python
@dataclass
class Address:
    city: str
    zip_code: str

@dataclass
class Person:
    name: str
    address: Address

p = Person("Alice", Address("NYC", "10001"))

# asdict converts nested dataclasses too
d = asdict(p)
print(d)
# {'name': 'Alice', 'address': {'city': 'NYC', 'zip_code': '10001'}}
```

---

## Practical Examples

### Configuration Object

```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 5432
    database: str = "mydb"
    user: str = "admin"
    password: str = field(default="", repr=False)  # Hide password
    pool_size: int = 5
    
    @property
    def connection_string(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
```

### API Response Model

```python
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class User:
    id: int
    username: str
    email: str
    created_at: datetime = field(default_factory=datetime.now)
    roles: List[str] = field(default_factory=list)
    profile: Optional[dict] = None

# JSON-like creation
user = User(
    id=1,
    username="alice",
    email="alice@example.com",
    roles=["admin", "user"]
)
```

### Immutable Value Object

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "USD"
    
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self.amount + other.amount, self.currency)

m1 = Money(100, "USD")
m2 = Money(50, "USD")
m3 = m1 + m2  # Money(amount=150, currency='USD')

# Can be used in sets and as dict keys (hashable)
prices = {Money(100, "USD"), Money(200, "EUR")}
```

### With Validation

```python
from dataclasses import dataclass, field

@dataclass
class Email:
    address: str
    
    def __post_init__(self):
        if "@" not in self.address:
            raise ValueError(f"Invalid email: {self.address}")

@dataclass
class User:
    name: str
    email: Email
    age: int = field(default=0)
    
    def __post_init__(self):
        if isinstance(self.email, str):
            self.email = Email(self.email)  # Auto-convert
        if self.age < 0:
            raise ValueError("Age cannot be negative")
```

---

## Comparison with Alternatives

| Feature | dataclass | NamedTuple | Regular Class |
|---------|-----------|------------|---------------|
| Mutable | ✓ (default) | ✗ | ✓ |
| Type hints | Required | Optional | Optional |
| Inheritance | ✓ | Limited | ✓ |
| Default values | ✓ | ✓ | ✓ |
| Methods | ✓ | ✓ | ✓ |
| `__slots__` | ✓ (3.10+) | Automatic | Manual |
| Memory | Normal | Efficient | Normal |
| Boilerplate | Minimal | Minimal | High |

---

## Summary

| Feature | Syntax |
|---------|--------|
| Basic dataclass | `@dataclass` |
| Immutable | `@dataclass(frozen=True)` |
| Sortable | `@dataclass(order=True)` |
| With slots | `@dataclass(slots=True)` |
| Mutable default | `field(default_factory=list)` |
| Hidden from repr | `field(repr=False)` |
| Not in __init__ | `field(init=False)` |
| Post-init logic | `def __post_init__(self)` |
| To dict | `asdict(instance)` |
| To tuple | `astuple(instance)` |

**Key Takeaways**:

- Use `@dataclass` for classes that primarily store data
- Type hints are required for all fields
- Use `field(default_factory=...)` for mutable defaults (lists, dicts)
- Use `frozen=True` for immutable objects (hashable, safe)
- Use `__post_init__` for validation and computed fields
- Python 3.10+ adds `slots=True` for memory efficiency
- `asdict()` and `astuple()` for easy serialization
