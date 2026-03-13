# Frozen Dataclasses

The `frozen=True` parameter makes a dataclass immutable, preventing modifications after creation. Frozen dataclasses can be hashed and used in sets/dicts.

---

## Creating Frozen Dataclasses

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

point = Point(1.0, 2.0)
print(point)  # Point(x=1.0, y=2.0)

# Attempt to modify raises FrozenInstanceError
try:
    point.x = 5.0
except AttributeError as e:
    print(f"Error: {e}")
```

## Using Frozen Dataclasses as Dictionary Keys

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

# Frozen dataclasses are hashable
coords = {
    Coordinate(0, 0): "origin",
    Coordinate(1, 1): "diagonal",
    Coordinate(-1, 1): "northwest"
}

print(coords[Coordinate(0, 0)])    # "origin"
print(Coordinate(1, 1) in coords)  # True
```

## Using Frozen Dataclasses in Sets

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Color:
    red: int
    green: int
    blue: int

colors = {
    Color(255, 0, 0),     # Red
    Color(0, 255, 0),     # Green
    Color(0, 0, 255),     # Blue
    Color(255, 0, 0)      # Duplicate red (ignored)
}

print(len(colors))  # 3 (unique colors only)
print(Color(255, 0, 0) in colors)  # True
```

## Frozen vs Mutable

```python
from dataclasses import dataclass

# Mutable (default)
@dataclass
class MutablePoint:
    x: float
    y: float

# Frozen
@dataclass(frozen=True)
class FrozenPoint:
    x: float
    y: float

# Mutable can be modified
mut_point = MutablePoint(1, 2)
mut_point.x = 3

# Frozen cannot
frozen_point = FrozenPoint(1, 2)
try:
    frozen_point.x = 3
except AttributeError as e:
    print(f"Cannot modify frozen: {e}")

# Frozen can be hashed (used as dict key)
point_map = {frozen_point: "initial"}
print(point_map[frozen_point])  # "initial"
```

## Performance Implications

```python
from dataclasses import dataclass
import timeit

@dataclass
class Mutable:
    x: int
    y: int

@dataclass(frozen=True)
class Frozen:
    x: int
    y: int

# Frozen dataclasses have hash cached
frozen = Frozen(1, 2)
print(hash(frozen))

# Creation time is similar
# But hashing is faster for frozen (cached)
```

## When to Use Frozen

- Use when data should be immutable (coordinates, colors, etc.)
- Use when storing in sets or as dictionary keys
- Use for function parameters that shouldn't be modified
- Use for thread-safe data sharing
