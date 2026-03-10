# Dataclass Inheritance


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Dataclasses support inheritance with automatic handling of parent and child fields. Understanding field ordering rules is important.

---

## Basic Inheritance

```python
from dataclasses import dataclass

@dataclass
class Animal:
    name: str
    age: int

@dataclass
class Dog(Animal):
    breed: str

dog = Dog("Buddy", 3, "Golden Retriever")
print(dog)  # Dog(name='Buddy', age=3, breed='Golden Retriever')
```

## Field Ordering in Inheritance

```python
from dataclasses import dataclass, field

@dataclass
class Base:
    x: int
    y: int = 10

# Fields with defaults must come after fields without defaults
@dataclass
class Derived(Base):
    z: int = 20  # Must have default since parent has default field

derived = Derived(1)
print(derived)  # Derived(x=1, y=10, z=20)

# This would fail: fields without defaults after those with defaults
# @dataclass
# class BadDerived(Base):
#     z: int  # Error: non-default field after default field
```

## Overriding Parent Fields

```python
from dataclasses import dataclass, field

@dataclass
class Vehicle:
    wheels: int = 4
    color: str = "white"

@dataclass
class Car(Vehicle):
    # Override with different default
    wheels: int = 4  # Explicitly set
    color: str = "silver"  # Different default
    doors: int = 4

car = Car()
print(car)  # Car(wheels=4, color='silver', doors=4)
```

## Multiple Inheritance

```python
from dataclasses import dataclass

@dataclass
class TimestampMixin:
    created_at: str = "2024-01-01"

@dataclass
class NameMixin:
    name: str

@dataclass
class Document(NameMixin, TimestampMixin):
    content: str = ""

doc = Document(name="Report", content="Summary")
print(doc)  # Document(name='Report', created_at='2024-01-01', content='Summary')
```

## Initialization Behavior

```python
from dataclasses import dataclass

@dataclass
class Parent:
    x: int
    
    def __post_init__(self):
        print(f"Parent init: x={self.x}")

@dataclass
class Child(Parent):
    y: int = 0
    
    def __post_init__(self):
        super().__post_init__()  # Call parent
        print(f"Child init: y={self.y}")

child = Child(1, 2)
# Output:
# Parent init: x=1
# Child init: y=2
```

## Inheritance with Mutable Defaults

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class BaseCollection:
    items: List[str] = field(default_factory=list)

@dataclass
class ExtendedCollection(BaseCollection):
    metadata: dict = field(default_factory=dict)

col1 = ExtendedCollection()
col2 = ExtendedCollection()

col1.items.append("item1")
col1.metadata['type'] = 'test'

print(col1)  # ExtendedCollection(items=['item1'], metadata={'type': 'test'})
print(col2)  # ExtendedCollection(items=[], metadata={})  # Independent
```

## Best Practices

- Keep parent dataclasses simple
- Place required fields in parent, optional in child
- Call `super().__post_init__()` when overriding
- Consider composition over inheritance for complex cases
