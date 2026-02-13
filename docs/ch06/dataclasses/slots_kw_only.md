# slots and kw_only

The `slots=True` parameter reduces memory usage by preventing `__dict__`. The `kw_only=True` parameter requires keyword-only arguments in `__init__()`.

---

## Using slots=True

```python
from dataclasses import dataclass

@dataclass(slots=True)
class Point:
    x: float
    y: float

point = Point(1.0, 2.0)
print(point)  # Point(x=1.0, y=2.0)

# Attempt to add arbitrary attributes fails
try:
    point.z = 3.0
except AttributeError as e:
    print(f"Cannot add attribute: {e}")

# Check memory usage
print(f"Point size: {point.__sizeof__()} bytes")
```

## Memory Efficiency with slots

```python
from dataclasses import dataclass
import sys

# Without slots (has __dict__)
@dataclass
class RegularPoint:
    x: float
    y: float

# With slots (no __dict__)
@dataclass(slots=True)
class SlotPoint:
    x: float
    y: float

regular = RegularPoint(1.0, 2.0)
slot = SlotPoint(1.0, 2.0)

print(f"Regular: {sys.getsizeof(regular.__dict__)} bytes for __dict__")
print(f"Slotted: no __dict__, saves memory")
```

## Using kw_only=True

```python
from dataclasses import dataclass

@dataclass(kw_only=True)
class Configuration:
    host: str
    port: int
    timeout: float = 30.0

# Must use keyword arguments
config = Configuration(host="localhost", port=8080)
print(config)  # Configuration(host='localhost', port=8080, timeout=30.0)

# Positional arguments fail
try:
    bad_config = Configuration("localhost", 8080)
except TypeError as e:
    print(f"Error: {e}")
```

## Combining slots and kw_only

```python
from dataclasses import dataclass

@dataclass(slots=True, kw_only=True)
class OptimizedConfig:
    name: str
    debug: bool = False
    workers: int = 4

config = OptimizedConfig(name="production", debug=False)
print(config)  # OptimizedConfig(name='production', debug=False, workers=4)

# Memory efficient and requires keyword arguments
```

## Per-Field kw_only

```python
from dataclasses import dataclass, field

@dataclass
class MixedArgs:
    # Positional argument
    name: str
    
    # Keyword-only arguments
    age: int = field(kw_only=True)
    email: str = field(kw_only=True)

obj = MixedArgs("Alice", age=30, email="alice@example.com")
print(obj)  # MixedArgs(name='Alice', age=30, email='alice@example.com')
```

## Performance with Slots

```python
from dataclasses import dataclass
import timeit

@dataclass
class Regular:
    x: int
    y: int

@dataclass(slots=True)
class Slotted:
    x: int
    y: int

# Attribute access is slightly faster with slots
regular = Regular(1, 2)
slotted = Slotted(1, 2)

time_regular = timeit.timeit(lambda: regular.x, number=1000000)
time_slotted = timeit.timeit(lambda: slotted.x, number=1000000)

print(f"Regular: {time_regular:.4f}s")
print(f"Slotted: {time_slotted:.4f}s")
```

## When to Use

- **slots=True**: Large number of instances, memory matters
- **kw_only=True**: Prevent positional argument confusion, improve code clarity
- **Both**: Performance-critical code with many objects
