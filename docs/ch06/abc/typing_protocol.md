# typing.Protocol — Structural Subtyping

`Protocol` (Python 3.8+) enables structural subtyping (static duck typing). Classes don't need to inherit from a Protocol—they just need to implement the required methods.

```python
from typing import Protocol
```

---

## Nominal vs Structural Typing

### Nominal Typing (ABC)

Classes must explicitly inherit:

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass

# Must inherit from Drawable
class Circle(Drawable):
    def draw(self) -> str:
        return "○"

# This class has draw() but ISN'T Drawable
class Square:
    def draw(self) -> str:
        return "□"

def render(shape: Drawable):
    print(shape.draw())

render(Circle())  # ✓ OK
render(Square())  # ✗ Type error (doesn't inherit Drawable)
```

### Structural Typing (Protocol)

Classes just need matching methods:

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:
        ...

# No inheritance needed!
class Circle:
    def draw(self) -> str:
        return "○"

class Square:
    def draw(self) -> str:
        return "□"

def render(shape: Drawable):
    print(shape.draw())

render(Circle())  # ✓ OK
render(Square())  # ✓ OK - has draw(), so it's Drawable!
```

---

## Defining Protocols

### Basic Protocol

```python
from typing import Protocol

class Greeter(Protocol):
    def greet(self, name: str) -> str:
        ...  # Use ... or pass

# Any class with greet(name: str) -> str works
class FormalGreeter:
    def greet(self, name: str) -> str:
        return f"Good day, {name}."

class CasualGreeter:
    def greet(self, name: str) -> str:
        return f"Hey {name}!"

def say_hello(greeter: Greeter, name: str):
    print(greeter.greet(name))

say_hello(FormalGreeter(), "Alice")  # "Good day, Alice."
say_hello(CasualGreeter(), "Bob")    # "Hey Bob!"
```

### Protocol with Multiple Methods

```python
from typing import Protocol

class Database(Protocol):
    def connect(self) -> None:
        ...
    
    def execute(self, query: str) -> list:
        ...
    
    def close(self) -> None:
        ...

# Must implement ALL methods to be compatible
class PostgresDB:
    def connect(self) -> None:
        print("Connecting to Postgres...")
    
    def execute(self, query: str) -> list:
        return [{"id": 1}]
    
    def close(self) -> None:
        print("Closing connection")

def run_query(db: Database, query: str) -> list:
    db.connect()
    result = db.execute(query)
    db.close()
    return result
```

### Protocol with Properties

```python
from typing import Protocol

class Named(Protocol):
    @property
    def name(self) -> str:
        ...

class Person:
    def __init__(self, name: str):
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name

class Company:
    name: str  # Class attribute also satisfies protocol
    
    def __init__(self, name: str):
        self.name = name

def display(obj: Named):
    print(f"Name: {obj.name}")

display(Person("Alice"))    # ✓
display(Company("Acme"))    # ✓
```

### Protocol with Class Variables

```python
from typing import Protocol, ClassVar

class Configurable(Protocol):
    config_key: ClassVar[str]
    
    def configure(self) -> None:
        ...

class DatabaseConfig:
    config_key: ClassVar[str] = "database"
    
    def configure(self) -> None:
        print(f"Configuring {self.config_key}")
```

---

## Runtime Checking

By default, Protocols only work for static type checking. For runtime `isinstance()` checks:

### @runtime_checkable

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Closeable(Protocol):
    def close(self) -> None:
        ...

class File:
    def close(self) -> None:
        print("File closed")

class Connection:
    def close(self) -> None:
        print("Connection closed")

f = File()
print(isinstance(f, Closeable))  # True

# Works with any object that has close()
import io
buffer = io.StringIO()
print(isinstance(buffer, Closeable))  # True
```

### Limitations of Runtime Checking

`@runtime_checkable` only checks method **existence**, not signatures:

```python
@runtime_checkable
class Adder(Protocol):
    def add(self, x: int, y: int) -> int:
        ...

class BadAdder:
    def add(self):  # Wrong signature!
        return 42

# Runtime check passes (only checks if 'add' exists)
print(isinstance(BadAdder(), Adder))  # True!

# But type checker would catch this
```

---

## Inheriting from Protocol

### Extending Protocols

```python
from typing import Protocol

class Reader(Protocol):
    def read(self) -> str:
        ...

class Writer(Protocol):
    def write(self, data: str) -> None:
        ...

class ReadWriter(Reader, Writer, Protocol):
    """Combines Reader and Writer."""
    pass

# Must implement both read() and write()
class File:
    def read(self) -> str:
        return "data"
    
    def write(self, data: str) -> None:
        print(f"Writing: {data}")

def process(rw: ReadWriter):
    data = rw.read()
    rw.write(data.upper())

process(File())  # ✓
```

### Adding Methods to Extended Protocol

```python
from typing import Protocol

class Identifiable(Protocol):
    @property
    def id(self) -> int:
        ...

class Timestamped(Protocol):
    @property
    def created_at(self) -> str:
        ...

class Entity(Identifiable, Timestamped, Protocol):
    @property
    def updated_at(self) -> str:
        ...
```

---

## Generic Protocols

```python
from typing import Protocol, TypeVar

T = TypeVar('T')

class Container(Protocol[T]):
    def get(self) -> T:
        ...
    
    def set(self, value: T) -> None:
        ...

class Box:
    def __init__(self, value: int):
        self._value = value
    
    def get(self) -> int:
        return self._value
    
    def set(self, value: int) -> None:
        self._value = value

def double_value(container: Container[int]) -> None:
    container.set(container.get() * 2)

box = Box(5)
double_value(box)
print(box.get())  # 10
```

### Covariant and Contravariant

```python
from typing import Protocol, TypeVar

T_co = TypeVar('T_co', covariant=True)
T_contra = TypeVar('T_contra', contravariant=True)

class Readable(Protocol[T_co]):
    def read(self) -> T_co:
        ...

class Writable(Protocol[T_contra]):
    def write(self, value: T_contra) -> None:
        ...
```

---

## Practical Examples

### Callback Protocol

```python
from typing import Protocol

class EventHandler(Protocol):
    def __call__(self, event: str, data: dict) -> None:
        ...

def on_click(event: str, data: dict) -> None:
    print(f"Clicked: {event}, {data}")

class ClickLogger:
    def __call__(self, event: str, data: dict) -> None:
        print(f"[LOG] {event}: {data}")

def register_handler(handler: EventHandler):
    handler("click", {"x": 10, "y": 20})

register_handler(on_click)      # Function ✓
register_handler(ClickLogger()) # Callable object ✓
```

### Iterator Protocol

```python
from typing import Protocol, TypeVar, Iterator

T = TypeVar('T')

class SupportsIter(Protocol[T]):
    def __iter__(self) -> Iterator[T]:
        ...

def first_item(items: SupportsIter[T]) -> T:
    return next(iter(items))

# Works with any iterable
print(first_item([1, 2, 3]))        # 1
print(first_item({4, 5, 6}))        # 4 (or 5 or 6)
print(first_item("hello"))          # 'h'
```

### Comparable Protocol

```python
from typing import Protocol, TypeVar

T = TypeVar('T')

class Comparable(Protocol):
    def __lt__(self, other: 'Comparable') -> bool:
        ...
    
    def __eq__(self, other: object) -> bool:
        ...

def min_value(a: Comparable, b: Comparable) -> Comparable:
    return a if a < b else b

# Works with any comparable
print(min_value(3, 7))          # 3
print(min_value("apple", "banana"))  # "apple"
```

### Context Manager Protocol

```python
from typing import Protocol, TypeVar

T = TypeVar('T')

class ContextManager(Protocol[T]):
    def __enter__(self) -> T:
        ...
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        ...

class Timer:
    def __enter__(self) -> 'Timer':
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, *args) -> bool:
        import time
        self.elapsed = time.time() - self.start
        return False

def timed_operation(cm: ContextManager[Timer]):
    with cm as timer:
        pass
    return timer.elapsed
```

---

## Protocol vs ABC Comparison

| Feature | Protocol | ABC |
|---------|----------|-----|
| Inheritance required | No | Yes |
| Static type checking | ✓ | ✓ |
| Runtime isinstance() | With `@runtime_checkable` | Always |
| Method implementation | Not enforced | Enforced |
| Signature checking (runtime) | No | No |
| Use case | Duck typing, interfaces | Contracts, mixins |

### When to Use Each

**Use Protocol when:**
- You want duck typing with type hints
- Working with external code you can't modify
- Defining interfaces for callbacks
- Type checking without requiring inheritance

**Use ABC when:**
- You need runtime enforcement
- You want to share implementation (concrete methods)
- Building class hierarchies
- Need `isinstance()` checks without decorator

---

## Summary

| Feature | Syntax |
|---------|--------|
| Define Protocol | `class MyProtocol(Protocol):` |
| Runtime checkable | `@runtime_checkable` |
| Method stub | `def method(self) -> None: ...` |
| Property | `@property` + `...` |
| Extend Protocol | `class Extended(Proto1, Proto2, Protocol):` |
| Generic Protocol | `class Container(Protocol[T]):` |

**Key Takeaways**:

- Protocols enable structural subtyping (static duck typing)
- No inheritance required—just implement the methods
- Use `@runtime_checkable` for `isinstance()` support
- Runtime checks only verify method existence, not signatures
- Protocols are ideal for type hints without tight coupling
- Prefer Protocol for interfaces, ABC for enforced contracts
