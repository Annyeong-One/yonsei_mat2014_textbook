# Polymorphism

Polymorphism allows objects of different types to be treated through a common interface, with each type implementing behavior in its own way.

---

## What is Polymorphism

### 1. Many Forms

"Polymorphism" means "many forms"—same interface, different implementations.

### 2. Common Interface

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

### 3. Uniform Treatment

```python
animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())
```

Don't care about the specific type—just call the method.

---

## Interface Definition

### 1. Placeholder Method

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass  # placeholder
```

Signals that all subclasses should implement `speak`.

### 2. Method Override

```python
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
```

Each subclass provides its own implementation.

### 3. Type Consistency

All `Animal` objects have a `speak` method.

---

## Duck Typing

### 1. No Type Declaration

```python
def make_speak(animal):
    print(animal.speak())
```

No need to declare `animal` is an `Animal`.

### 2. Interface Matters

```python
class Robot:
    def speak(self):
        return "Beep boop!"

make_speak(Robot())  # Works!
```

If it has `speak()`, it works.

### 3. Runtime Check

```python
if hasattr(obj, 'speak'):
    obj.speak()
```

---

## Method Overriding

### 1. Replace Behavior

```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"
```

### 2. Extend Behavior

```python
class Child(Parent):
    def greet(self):
        parent_msg = super().greet()
        return f"{parent_msg} and Child"
```

### 3. Selective Override

```python
class Parent:
    def method_a(self):
        return "A"
    
    def method_b(self):
        return "B"

class Child(Parent):
    def method_a(self):  # override only this
        return "A from Child"
    # method_b inherited
```

---

## Operator Overloading

### 1. Special Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

### 2. String Representation

```python
def __str__(self):
    return f"Vector({self.x}, {self.y})"

def __repr__(self):
    return f"Vector(x={self.x}, y={self.y})"
```

### 3. Comparison

```python
def __eq__(self, other):
    return self.x == other.x and self.y == other.y

def __lt__(self, other):
    return self.x < other.x
```

---

## Real-World Example

### 1. SciPy Distributions

```python
from scipy import stats

# Different distributions, same interface
obj = stats.norm()    # Normal
# obj = stats.uniform() # Uniform
# obj = stats.expon()  # Exponential

x = obj.rvs(10_000)  # All have rvs()
```

### 2. Common Methods

```python
samples = obj.rvs(n)     # random samples
density = obj.pdf(x)     # probability density
cumulative = obj.cdf(x)  # cumulative distribution
```

### 3. Interchangeable

Can swap distributions without changing code.

---

## Polymorphic Functions

### 1. Generic Processing

```python
def process_shapes(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area
```

### 2. Mixed Types

```python
shapes = [
    Rectangle(3, 4),
    Circle(5),
    Triangle(3, 4)
]
print(process_shapes(shapes))
```

### 3. No Type Checks

Don't need to check `isinstance()`—just call the method.

---

## Benefits

### 1. Code Reusability

Write once, works for many types.

### 2. Extensibility

Add new types without changing existing code.

### 3. Clean Design

No complex conditional logic based on type.

---

## Polymorphism vs Abstraction

### 1. Polymorphism (Informal)

```python
class Animal:
    def speak(self):
        pass  # no enforcement
```

Trust that subclasses implement correctly.

### 2. Abstraction (Formal)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # enforced!
```

Forces subclasses to implement.

### 3. Key Difference

Polymorphism = same interface, different behaviors.
Abstraction = enforced contract with ABC.

---

## Key Takeaways

- Polymorphism enables uniform interfaces.
- Different types implement methods differently.
- Duck typing: if it quacks, it's a duck.
- Method overriding enables custom behavior.
- Operator overloading uses special methods.
