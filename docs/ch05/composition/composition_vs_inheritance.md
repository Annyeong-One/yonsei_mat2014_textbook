# Composition vs Inheritance

## Core Differences

### 1. Relationship Type

**Inheritance** models **"is-a"** relationships:
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):  # Dog IS-A Animal
    def speak(self):
        return "Woof"
```

**Composition** models **"has-a"** relationships:
```python
class Bark:
    def sound(self):
        return "Woof"

class Dog:
    def __init__(self):
        self.bark = Bark()  # Dog HAS-A Bark
    
    def speak(self):
        return self.bark.sound()
```

### 2. Coupling Strength

| Aspect | Inheritance | Composition |
|--------|-------------|-------------|
| Coupling | Tight | Loose |
| Dependency | Compile-time | Runtime |
| Flexibility | Low | High |
| Changes impact | Cascading | Isolated |

### 3. Code Reuse Mechanism

**Inheritance** reuses through extension:
```python
class Vehicle:
    def move(self):
        return "Moving"

class Car(Vehicle):
    pass  # Inherits move()
```

**Composition** reuses through delegation:
```python
class Movement:
    def move(self):
        return "Moving"

class Car:
    def __init__(self):
        self.movement = Movement()
    
    def move(self):
        return self.movement.move()
```

## When to Use Each

### 1. Use Inheritance When

**Clear hierarchies exist:**
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
```

**Polymorphism is needed:**
```python
def calculate_total_area(shapes: list[Shape]):
    return sum(shape.area() for shape in shapes)

shapes = [Circle(5), Rectangle(4, 6)]
print(calculate_total_area(shapes))
```

**Shared interface required:**
```python
class Drawable:
    def draw(self):
        pass

class Button(Drawable):
    def draw(self):
        return "Drawing button"

class Image(Drawable):
    def draw(self):
        return "Drawing image"
```

### 2. Use Composition When

**Building from parts:**
```python
class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def rotate(self):
        return "Wheels rotating"

class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()
    
    def drive(self):
        return f"{self.engine.start()}, {self.wheels.rotate()}"
```

**Runtime flexibility needed:**
```python
class FileLogger:
    def log(self, msg):
        return f"File: {msg}"

class ConsoleLogger:
    def log(self, msg):
        return f"Console: {msg}"

class Application:
    def __init__(self, logger):
        self.logger = logger  # Flexible at runtime
    
    def run(self):
        self.logger.log("App started")

# Switch logger at runtime
app = Application(FileLogger())
app.logger = ConsoleLogger()
```

**Avoiding deep hierarchies:**
```python
# ❌ BAD - Deep inheritance
class Entity:
    pass

class LivingEntity(Entity):
    pass

class Animal(LivingEntity):
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

# ✅ GOOD - Composition
class Entity:
    def __init__(self, behaviors):
        self.behaviors = behaviors

class Dog(Entity):
    def __init__(self):
        super().__init__([
            LivingBehavior(),
            AnimalBehavior(),
            MammalBehavior()
        ])
```

## Problems with Inheritance

### 1. Fragile Base Class

Changes to parent break children:

```python
class Animal:
    def move(self):
        return "Walking"

class Bird(Animal):
    def fly(self):
        return "Flying"

# Later, Animal changes
class Animal:
    def move(self, speed):  # Added parameter
        return f"Walking at {speed}"

# Bird breaks!
bird = Bird()
bird.move()  # ❌ TypeError: missing 1 required positional argument
```

With composition:
```python
class WalkingBehavior:
    def move(self):
        return "Walking"

class FlyingBehavior:
    def move(self):
        return "Flying"

class Bird:
    def __init__(self):
        self.movement = FlyingBehavior()
    
    def move(self):
        return self.movement.move()

# Isolated change
class WalkingBehavior:
    def move(self, speed=1):  # Bird unaffected
        return f"Walking at {speed}"
```

### 2. Inflexible Hierarchy

Can't change behavior after instantiation:

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

# Can't make dog meow
dog = Dog()
# Stuck with "Woof"
```

With composition:
```python
class Bark:
    def sound(self):
        return "Woof"

class Meow:
    def sound(self):
        return "Meow"

class Animal:
    def __init__(self, sound_maker):
        self.sound_maker = sound_maker
    
    def speak(self):
        return self.sound_maker.sound()

animal = Animal(Bark())
animal.speak()  # "Woof"

# Can change behavior
animal.sound_maker = Meow()
animal.speak()  # "Meow"
```

### 3. Multiple Inheritance Issues

Diamond problem:

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
d.method()  # Which method? Depends on MRO
```

Composition avoids this:
```python
class A:
    def method(self):
        return "A"

class B:
    def method(self):
        return "B"

class C:
    def method(self):
        return "C"

class D:
    def __init__(self):
        self.b = B()
        self.c = C()
    
    def b_method(self):
        return self.b.method()
    
    def c_method(self):
        return self.c.method()

# Clear and explicit
d = D()
d.b_method()  # "B"
d.c_method()  # "C"
```

## Advantages of Composition

### 1. Better Encapsulation

Hide implementation:

```python
class EmailValidator:
    def validate(self, email):
        return "@" in email

class UserService:
    def __init__(self):
        self._validator = EmailValidator()  # Private
    
    def create_user(self, email):
        if self._validator.validate(email):
            return f"User created: {email}"
        return "Invalid email"

# Client doesn't know about validator
service = UserService()
service.create_user("alice@example.com")
```

### 2. Runtime Flexibility

Change behavior dynamically:

```python
class SortStrategy:
    def sort(self, data):
        pass

class QuickSort(SortStrategy):
    def sort(self, data):
        return sorted(data)

class BubbleSort(SortStrategy):
    def sort(self, data):
        return sorted(data)

class Sorter:
    def __init__(self):
        self.strategy = QuickSort()
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def sort(self, data):
        return self.strategy.sort(data)

sorter = Sorter()
sorter.sort([3, 1, 2])

# Switch at runtime
sorter.set_strategy(BubbleSort())
```

### 3. Easier Testing

Inject mock objects:

```python
class MockDatabase:
    def query(self, sql):
        return [{"id": 1, "name": "Test"}]

class UserRepository:
    def __init__(self, database):
        self.database = database
    
    def get_users(self):
        return self.database.query("SELECT * FROM users")

# Easy testing
repo = UserRepository(MockDatabase())
users = repo.get_users()
assert len(users) == 1
```

## Combining Both

### 1. Interface Inheritance + Composition

Best of both worlds:

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCardGateway:
    def charge(self, amount):
        return f"Charged ${amount} to credit card"

class CreditCardPayment(PaymentMethod):
    def __init__(self):
        self.gateway = CreditCardGateway()  # Composition
    
    def process(self, amount):
        return self.gateway.charge(amount)

class PayPalGateway:
    def send_payment(self, amount):
        return f"Sent ${amount} via PayPal"

class PayPalPayment(PaymentMethod):
    def __init__(self):
        self.gateway = PayPalGateway()  # Composition
    
    def process(self, amount):
        return self.gateway.send_payment(amount)

# Polymorphism through inheritance
# Implementation through composition
def process_payment(method: PaymentMethod, amount):
    return method.process(amount)

process_payment(CreditCardPayment(), 100)
process_payment(PayPalPayment(), 50)
```

### 2. Template Method Pattern

```python
class Algorithm(ABC):
    def execute(self):
        self.step1()
        self.step2()
        self.step3()
    
    @abstractmethod
    def step1(self):
        pass
    
    @abstractmethod
    def step2(self):
        pass
    
    @abstractmethod
    def step3(self):
        pass

class ConcreteAlgorithm(Algorithm):
    def __init__(self, helper):
        self.helper = helper  # Composition
    
    def step1(self):
        return self.helper.do_something()
    
    def step2(self):
        return "Step 2"
    
    def step3(self):
        return "Step 3"
```

### 3. Strategy with Inheritance

```python
class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        return "Strategy A"

class ConcreteStrategyB(Strategy):
    def execute(self):
        return "Strategy B"

class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy  # Composition
    
    def do_work(self):
        return self.strategy.execute()
```

## Design Guidelines

### 1. Prefer Composition

Modern best practice:

> "Favor composition over inheritance"

```python
# Instead of:
class FlyingAnimal(Animal):
    pass

class SwimmingAnimal(Animal):
    pass

class FlyingSwimmingAnimal(FlyingAnimal, SwimmingAnimal):
    pass

# Use:
class Animal:
    def __init__(self, abilities):
        self.abilities = abilities
    
    def perform(self):
        for ability in self.abilities:
            ability.execute()

duck = Animal([FlyAbility(), SwimAbility()])
```

### 2. When Inheritance is OK

Use for:
- True **is-a** relationships
- **Abstract base classes** (interfaces)
- **Framework extension points**
- **Polymorphic collections**

```python
# Good inheritance use
class Plugin(ABC):
    @abstractmethod
    def run(self):
        pass

class DataPlugin(Plugin):
    def run(self):
        return "Processing data"

class FilePlugin(Plugin):
    def run(self):
        return "Processing files"

def run_all(plugins: list[Plugin]):
    for plugin in plugins:
        plugin.run()
```

### 3. Refactoring Inheritance

Convert to composition:

```python
# Before - Inheritance
class Logger:
    def log(self, msg):
        print(msg)

class TimestampLogger(Logger):
    def log(self, msg):
        from datetime import datetime
        super().log(f"{datetime.now()}: {msg}")

# After - Composition
class Logger:
    def log(self, msg):
        print(msg)

class TimestampDecorator:
    def __init__(self, logger):
        self.logger = logger
    
    def log(self, msg):
        from datetime import datetime
        self.logger.log(f"{datetime.now()}: {msg}")

logger = TimestampDecorator(Logger())
```

## Summary Table

| Criterion | Inheritance | Composition |
|-----------|-------------|-------------|
| Relationship | is-a | has-a |
| Coupling | Tight | Loose |
| Flexibility | Low | High |
| Reusability | Limited | High |
| Testing | Harder | Easier |
| Changes | Cascading | Isolated |
| Use for | Type hierarchies | Building systems |
