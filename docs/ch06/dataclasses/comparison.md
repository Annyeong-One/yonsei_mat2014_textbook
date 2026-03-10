# Dataclass vs NamedTuple vs attrs


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python offers multiple ways to create simple classes. Understanding differences helps you choose the right tool.

---

## Dataclasses

```python
from dataclasses import dataclass

@dataclass
class PersonDataclass:
    name: str
    age: int
    city: str = "Unknown"

person = PersonDataclass("Alice", 30)
person.age = 31  # Mutable
print(person)    # PersonDataclass(name='Alice', age=31, city='Unknown')
```

## NamedTuple

```python
from typing import NamedTuple

class PersonNamedTuple(NamedTuple):
    name: str
    age: int
    city: str = "Unknown"

person = PersonNamedTuple("Bob", 25)
print(person)       # PersonNamedTuple(name='Bob', age=25, city='Unknown')
print(person[0])    # 'Bob' (tuple indexing works)
# person.age = 26   # Error: immutable
```

## attrs Library

```python
# pip install attrs
import attrs

@attrs.define
class PersonAttrs:
    name: str
    age: int
    city: str = "Unknown"

person = PersonAttrs("Charlie", 28)
person.age = 29  # Mutable
print(person)    # PersonAttrs(name='Charlie', age=29, city='Unknown')
```

## Comparison

```python
from dataclasses import dataclass
from typing import NamedTuple

@dataclass
class DataclassPerson:
    name: str
    age: int = 0

class NamedTuplePerson(NamedTuple):
    name: str
    age: int = 0

# Mutability
dc_person = DataclassPerson("Alice")
dc_person.age = 30  # Works

nt_person = NamedTuplePerson("Bob")
# nt_person.age = 30  # Error

# Tuple unpacking (NamedTuple only)
name, age = nt_person
print(f"{name}: {age}")

# Hashing
dc_frozen = DataclassPerson("Charlie")
dc_dict = {dc_frozen: "value"}  # Error without frozen=True

nt_dict = {nt_person: "value"}  # Works automatically
```

## Performance Comparison

```python
import timeit
from dataclasses import dataclass
from typing import NamedTuple

@dataclass
class DC:
    x: int
    y: int

class NT(NamedTuple):
    x: int
    y: int

# Creation time similar
# NamedTuple slightly faster for creation
# Dataclass more flexible

time_dc = timeit.timeit(lambda: DC(1, 2), number=100000)
time_nt = timeit.timeit(lambda: NT(1, 2), number=100000)

print(f"Dataclass: {time_dc:.4f}s")
print(f"NamedTuple: {time_nt:.4f}s")
```

## When to Use Each

**Dataclasses:**
- Mutable objects
- Complex initialization
- Need many methods
- Standard library preferred

**NamedTuple:**
- Immutable records
- Tuple unpacking needed
- Dictionary/set keys
- Lightweight
- Type hints integration

**attrs:**
- Complex validation
- Custom __init__ behavior
- Slots by default (memory efficient)
- Not in standard library
