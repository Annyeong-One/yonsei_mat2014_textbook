# __post_init__ Method


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The `__post_init__()` method is called after the generated `__init__()` completes, allowing you to perform additional initialization or validation.

---

## Basic __post_init__ Usage

```python
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Event:
    name: str
    date: str
    duration_minutes: int
    
    def __post_init__(self):
        # Convert string to datetime
        self.date = datetime.strptime(self.date, "%Y-%m-%d")
        # Calculate end time
        self.end_time = self.date + timedelta(minutes=self.duration_minutes)

event = Event("Meeting", "2024-02-15", 60)
print(f"{event.name} on {event.date.date()} until {event.end_time.time()}")
```

## Validation in __post_init__

```python
from dataclasses import dataclass

@dataclass
class Age:
    years: int
    
    def __post_init__(self):
        if self.years < 0 or self.years > 150:
            raise ValueError(f"Invalid age: {self.years}")

try:
    invalid = Age(-5)
except ValueError as e:
    print(f"Error: {e}")

valid = Age(25)
print(f"Valid age: {valid.years}")
```

## Derived Fields

```python
from dataclasses import dataclass, field

@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)
    perimeter: float = field(init=False)
    
    def __post_init__(self):
        # Calculate derived fields
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print(f"Area: {rect.area}, Perimeter: {rect.perimeter}")  # 50, 30
```

## Complex Initialization Logic

```python
from dataclasses import dataclass
from pathlib import Path

@dataclass
class FileConfig:
    path: str
    mode: str = "r"
    encoding: str = "utf-8"
    _file = None
    
    def __post_init__(self):
        # Validate path exists for read mode
        if self.mode == "r" and not Path(self.path).exists():
            raise FileNotFoundError(f"{self.path} not found")
        
        # Store as Path object
        self.path = Path(self.path)
        
        print(f"Initialized config for {self.path}")

try:
    config = FileConfig("/nonexistent/file.txt")
except FileNotFoundError as e:
    print(f"Error: {e}")
```

## __post_init__ with Field Modifications

```python
from dataclasses import dataclass, field

@dataclass
class Container:
    items: list = field(default_factory=list)
    
    def __post_init__(self):
        # Ensure items is always a list
        if not isinstance(self.items, list):
            self.items = list(self.items)
        
        # Sort items
        self.items.sort()

container = Container((3, 1, 2))
print(container.items)  # [1, 2, 3]
```

## Performance Notes

- `__post_init__()` adds overhead to object creation
- Keep it lightweight for frequently created objects
- Use for validation, derived fields, and conversions
- Alternative: Use custom `__init__` if complex logic needed
