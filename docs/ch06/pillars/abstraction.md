# Abstraction


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Abstraction hides complex implementation details and shows only the necessary features, reducing complexity for users.

---

## What is Abstraction

### 1. Hide Complexity

Show only essential features while hiding implementation details.

### 2. High-Level Interface

Users interact with objects at a high level without understanding internals.

### 3. Essential Features

Focus on **what** an object does, not **how** it does it.

---

## Abstract Base Classes

### 1. Using ABC Module

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

Defines a contract that subclasses must follow.

### 2. Cannot Instantiate

```python
shape = Shape()  # TypeError!
```

Abstract classes cannot be instantiated directly.

### 3. Must Implement

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):  # Must implement
        return self.width * self.height
```

---

## `@abstractmethod`

### 1. Required Methods

```python
class MyBase(ABC):
    @abstractmethod
    def must_override(self):
        pass
```

Subclasses **must** implement this method.

### 2. Enforcement

```python
class Incomplete(MyBase):
    pass

obj = Incomplete()  # TypeError!
```

Python prevents instantiation if abstract methods aren't implemented.

### 3. Complete Implementation

```python
class Complete(MyBase):
    def must_override(self):
        return "Implemented!"

obj = Complete()  # Works
```

---

## Abstract vs Optional

### 1. Required Methods

```python
class Dataset(ABC):
    @abstractmethod
    def __getitem__(self, index):
        pass  # Must override
    
    @abstractmethod
    def __len__(self):
        pass  # Must override
```

### 2. Optional Methods

```python
def __add__(self, other):
    return ConcatDataset([self, other])
```

No `@abstractmethod` = optional to override.

### 3. Mixed Approach

```python
class MyDataset(Dataset):
    def __getitem__(self, index):  # Required
        return self.data[index]
    
    def __len__(self):  # Required
        return len(self.data)
    
    # __add__ inherited - optional
```

---

## Abstract Decorators

### 1. Abstract Class Method

```python
class MyBase(ABC):
    @classmethod
    @abstractmethod
    def create(cls):
        pass
```

### 2. Abstract Static Method

```python
class MyBase(ABC):
    @staticmethod
    @abstractmethod
    def validate(data):
        pass
```

### 3. Abstract Property

```python
class MyBase(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
```

---

## Real-World Example

### 1. Shape Hierarchy

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
```

### 2. Concrete Shapes

```python
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
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
```

### 3. Polymorphic Use

```python
shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print(f"Area: {shape.area()}")
```

---

## Benefits

### 1. Contract Enforcement

Guarantees subclasses implement required methods.

### 2. Clear Interface

Defines what operations are available.

### 3. Design Consistency

All implementations follow the same structure.

---

## Common Patterns

### 1. Template Method

```python
class Algorithm(ABC):
    @abstractmethod
    def step_one(self):
        pass
    
    @abstractmethod
    def step_two(self):
        pass
    
    def execute(self):  # Template
        self.step_one()
        self.step_two()
```

### 2. Strategy Pattern

```python
class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass
```

### 3. Factory Pattern

```python
class Creator(ABC):
    @abstractmethod
    def create_product(self):
        pass
```

---

## Key Takeaways

- Abstraction hides implementation details.
- ABC module enforces contracts.
- `@abstractmethod` marks required methods.
- Cannot instantiate abstract classes.
- Enables polymorphic designs.
