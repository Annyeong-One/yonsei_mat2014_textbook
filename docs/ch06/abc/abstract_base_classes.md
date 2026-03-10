# Abstract Base Classes (ABC)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Abstract Base Classes define interfaces that subclasses must implement. They provide a way to enforce contracts and enable polymorphism with explicit structure.

```python
from abc import ABC, abstractmethod
```

---

## Why Use ABCs?

### The Problem: Duck Typing Limitations

Duck typing ("if it quacks like a duck...") is flexible but has issues:

```python
# Duck typing - no enforcement
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

# Both work, but Person isn't really a duck
def make_it_quack(thing):
    thing.quack()  # Works for both, but is Person valid?
```

### The Solution: ABCs

ABCs explicitly define what methods a class must have:

```python
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        """All birds must implement fly()"""
        pass
    
    @abstractmethod
    def make_sound(self):
        """All birds must implement make_sound()"""
        pass

# Cannot instantiate abstract class
# bird = Bird()  # TypeError!

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies short distances"
    
    def make_sound(self):
        return "Chirp!"

# Can instantiate concrete class
sparrow = Sparrow()  # ✓ OK
```

---

## Basic ABC Definition

### Using ABC Base Class

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        from math import pi
        return pi * self.radius ** 2
    
    def perimeter(self):
        from math import pi
        return 2 * pi * self.radius
```

### Using ABCMeta Metaclass

Alternative syntax (equivalent to inheriting from ABC):

```python
from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass
```

---

## Abstract Methods

### @abstractmethod

Must be implemented by all concrete subclasses:

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        """Establish connection to database."""
        pass
    
    @abstractmethod
    def execute(self, query):
        """Execute a query."""
        pass
    
    @abstractmethod
    def close(self):
        """Close the connection."""
        pass
```

### Abstract Properties

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @property
    @abstractmethod
    def max_speed(self):
        """Maximum speed in km/h."""
        pass
    
    @property
    @abstractmethod
    def fuel_type(self):
        """Type of fuel used."""
        pass

class Car(Vehicle):
    @property
    def max_speed(self):
        return 200
    
    @property
    def fuel_type(self):
        return "gasoline"
```

### Abstract Class Methods

```python
from abc import ABC, abstractmethod

class Serializable(ABC):
    @classmethod
    @abstractmethod
    def from_json(cls, json_str):
        """Create instance from JSON string."""
        pass
    
    @abstractmethod
    def to_json(self):
        """Convert instance to JSON string."""
        pass
```

### Abstract Static Methods

```python
from abc import ABC, abstractmethod

class Validator(ABC):
    @staticmethod
    @abstractmethod
    def validate(value):
        """Validate the given value."""
        pass
```

---

## Concrete Methods in ABCs

ABCs can have concrete (implemented) methods:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        """Must be implemented by subclass."""
        pass
    
    # Concrete method - inherited as-is
    def introduce(self):
        return f"I am {self.name} and I say: {self.speak()}"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.introduce())  # "I am Buddy and I say: Woof!"
```

---

## Default Implementation

Abstract methods can have default implementations:

```python
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        """Log a message. Subclasses should call super()."""
        print(f"[{self.__class__.__name__}] {message}")

class FileLogger(Logger):
    def log(self, message):
        super().log(message)  # Call default implementation
        # Additional file-specific logging
        with open("log.txt", "a") as f:
            f.write(message + "\n")
```

---

## Checking Implementation

### isinstance() and issubclass()

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def draw(self):
        return "Drawing circle"

circle = Circle()

print(isinstance(circle, Drawable))  # True
print(issubclass(Circle, Drawable))  # True
```

### __subclasshook__

Customize isinstance/issubclass behavior:

```python
from abc import ABC, abstractmethod

class Iterable(ABC):
    @abstractmethod
    def __iter__(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterable:
            if hasattr(C, '__iter__'):
                return True
        return NotImplemented

# Now any class with __iter__ is considered Iterable
class MyContainer:
    def __iter__(self):
        return iter([1, 2, 3])

print(isinstance(MyContainer(), Iterable))  # True
```

---

## Built-in ABCs

Python's `collections.abc` module provides many useful ABCs:

```python
from collections.abc import (
    Iterable,      # Has __iter__
    Iterator,      # Has __iter__ and __next__
    Sequence,      # Has __getitem__ and __len__
    MutableSequence,  # Sequence + __setitem__, __delitem__, insert
    Mapping,       # Has __getitem__, __iter__, __len__
    MutableMapping,   # Mapping + __setitem__, __delitem__
    Set,           # Has __contains__, __iter__, __len__
    Callable,      # Has __call__
    Hashable,      # Has __hash__
)

# Check if something is iterable
from collections.abc import Iterable
print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance(42, Iterable))          # False
```

### Implementing Collection ABCs

```python
from collections.abc import Sequence

class MyList(Sequence):
    def __init__(self, data):
        self._data = list(data)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __len__(self):
        return len(self._data)
    
    # Sequence provides: __contains__, __iter__, __reversed__,
    # index(), count() for free!

ml = MyList([1, 2, 3, 4, 5])
print(3 in ml)      # True (uses inherited __contains__)
print(ml.count(3))  # 1 (uses inherited count())
```

---

## Practical Examples

### Plugin System

```python
from abc import ABC, abstractmethod

class Plugin(ABC):
    @property
    @abstractmethod
    def name(self):
        """Plugin name."""
        pass
    
    @abstractmethod
    def execute(self, data):
        """Process data."""
        pass
    
    def __repr__(self):
        return f"<Plugin: {self.name}>"

class UppercasePlugin(Plugin):
    @property
    def name(self):
        return "uppercase"
    
    def execute(self, data):
        return data.upper()

class ReversePlugin(Plugin):
    @property
    def name(self):
        return "reverse"
    
    def execute(self, data):
        return data[::-1]

# Plugin manager
class PluginManager:
    def __init__(self):
        self.plugins = {}
    
    def register(self, plugin: Plugin):
        self.plugins[plugin.name] = plugin
    
    def process(self, name, data):
        return self.plugins[name].execute(data)
```

### Repository Pattern

```python
from abc import ABC, abstractmethod
from typing import List, Optional

class Repository(ABC):
    @abstractmethod
    def get(self, id: int) -> Optional[dict]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[dict]:
        pass
    
    @abstractmethod
    def add(self, entity: dict) -> int:
        pass
    
    @abstractmethod
    def update(self, id: int, entity: dict) -> bool:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass

class InMemoryRepository(Repository):
    def __init__(self):
        self._data = {}
        self._next_id = 1
    
    def get(self, id: int) -> Optional[dict]:
        return self._data.get(id)
    
    def get_all(self) -> List[dict]:
        return list(self._data.values())
    
    def add(self, entity: dict) -> int:
        id = self._next_id
        self._data[id] = {**entity, 'id': id}
        self._next_id += 1
        return id
    
    def update(self, id: int, entity: dict) -> bool:
        if id in self._data:
            self._data[id] = {**entity, 'id': id}
            return True
        return False
    
    def delete(self, id: int) -> bool:
        if id in self._data:
            del self._data[id]
            return True
        return False
```

### Strategy Pattern

```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number
    
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} with credit card {self.card_number[-4:]}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} via PayPal ({self.email})"

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy: PaymentStrategy = None
    
    def set_payment(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy
    
    def checkout(self):
        total = sum(item['price'] for item in self.items)
        return self.payment_strategy.pay(total)
```

---

## ABC vs Protocol

| Feature | ABC | Protocol (typing) |
|---------|-----|-------------------|
| Type | Nominal (explicit inheritance) | Structural (implicit) |
| Runtime check | `isinstance()` works | Requires `@runtime_checkable` |
| Inheritance | Required | Not required |
| Use case | Enforce implementation | Type hints, duck typing |

```python
from abc import ABC, abstractmethod
from typing import Protocol

# ABC - must inherit
class DrawableABC(ABC):
    @abstractmethod
    def draw(self): pass

class Circle(DrawableABC):  # Must inherit
    def draw(self): return "circle"

# Protocol - just implement method
class DrawableProtocol(Protocol):
    def draw(self) -> str: ...

class Square:  # No inheritance needed
    def draw(self): return "square"

# Square is compatible with DrawableProtocol
def render(shape: DrawableProtocol):
    print(shape.draw())

render(Square())  # Works!
```

---

## Summary

| Feature | Syntax |
|---------|--------|
| Define ABC | `class MyABC(ABC):` |
| Abstract method | `@abstractmethod` |
| Abstract property | `@property` + `@abstractmethod` |
| Abstract classmethod | `@classmethod` + `@abstractmethod` |
| Concrete method | Regular method in ABC |
| Check instance | `isinstance(obj, MyABC)` |

**Key Takeaways**:

- ABCs define interfaces that subclasses must implement
- Cannot instantiate a class with unimplemented abstract methods
- Use `@abstractmethod` decorator for required methods
- ABCs can have concrete methods with shared implementation
- `collections.abc` provides useful built-in ABCs
- Choose ABC for strict contracts, Protocol for structural typing
