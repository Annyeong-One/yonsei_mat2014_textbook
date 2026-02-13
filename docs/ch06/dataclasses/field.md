# field() Function

The `field()` function provides fine-grained control over how individual fields are handled in dataclasses, including default values, factory functions, and metadata.

---

## Basic field() Usage

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
    name: str
    age: int = field(default=0)  # With default
    hobbies: List[str] = field(default_factory=list)  # Mutable default

person1 = Person("Alice")
person2 = Person("Bob", age=30)
person3 = Person("Charlie", age=25, hobbies=["reading"])

print(person1)  # Person(name='Alice', age=0, hobbies=[])
print(person2)  # Person(name='Bob', age=30, hobbies=[])
```

## default_factory for Mutable Objects

```python
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Config:
    name: str
    options: Dict[str, int] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)

config1 = Config("api")
config2 = Config("database")

# Each gets its own dictionary and list
config1.options['timeout'] = 30
config1.tags.append('important')

print(config1)  # Config(name='api', options={'timeout': 30}, tags=['important'])
print(config2)  # Config(name='database', options={}, tags=[])
```

## Field Metadata and Exclusion

```python
from dataclasses import dataclass, field, asdict

@dataclass
class User:
    name: str
    password: str = field(repr=False)  # Don't show in repr
    email: str = field(compare=False)  # Don't use in comparisons

user1 = User("alice", "secret123", "alice@example.com")
user2 = User("alice", "different", "alice@different.com")

print(user1)           # User(name='alice', email='alice@example.com')
print(user1 == user2)  # True (email not compared, password excluded)
```

## Custom Metadata

```python
from dataclasses import dataclass, field, fields

@dataclass
class Product:
    name: str = field(metadata={'description': 'Product name'})
    price: float = field(metadata={'currency': 'USD', 'min': 0.0})
    quantity: int = field(default=0, metadata={'unit': 'items'})

# Access metadata
for f in fields(Product):
    print(f"{f.name}: {f.metadata}")
```

## Initialization Order and Init

```python
from dataclasses import dataclass, field

@dataclass
class Example:
    required: str
    optional: str = field(default="default_value")
    # Fields with init=False aren't included in __init__
    computed: str = field(init=False)
    
    def __post_init__(self):
        self.computed = f"{self.required}_{self.optional}"

example = Example("test")
print(example)  # Example(required='test', optional='default_value', computed='test_default_value')
```

## Compare and Hash Control

```python
from dataclasses import dataclass, field

@dataclass
class Item:
    id: int
    name: str = field(compare=True)
    internal_state: dict = field(compare=False, repr=False)

item1 = Item(1, "widget", {})
item2 = Item(1, "widget", {'processed': True})

print(item1 == item2)  # True (internal_state not compared)
print(hash(item1))     # Works with hashable fields
```
