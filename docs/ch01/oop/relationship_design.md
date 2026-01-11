# Relationship Design

## Design Principles

### 1. Single Responsibility

Each class should have one reason to change:

```python
# ❌ BAD - Multiple responsibilities
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        # Database logic
        pass
    
    def send_email(self):
        # Email logic
        pass
    
    def validate(self):
        # Validation logic
        pass

# ✅ GOOD - Separated responsibilities
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        # Database logic
        pass

class EmailService:
    def send(self, user):
        # Email logic
        pass

class UserValidator:
    def validate(self, user):
        # Validation logic
        pass
```

### 2. Open-Closed Principle

Open for extension, closed for modification:

```python
# Using composition for extensibility
class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method
    
    def process(self, amount):
        return self.payment_method.charge(amount)

# Extend by adding new payment methods
class CreditCard:
    def charge(self, amount):
        return f"Charged ${amount} to card"

class PayPal:
    def charge(self, amount):
        return f"Charged ${amount} via PayPal"

# No modification to PaymentProcessor needed
processor = PaymentProcessor(CreditCard())
processor = PaymentProcessor(PayPal())
```

### 3. Liskov Substitution

Subclasses must be substitutable for their base classes:

```python
# ✅ GOOD - LSP respected
class Bird:
    def move(self):
        return "Moving"

class Sparrow(Bird):
    def move(self):
        return "Flying"  # Still moving

class Penguin(Bird):
    def move(self):
        return "Walking"  # Still moving

def make_bird_move(bird: Bird):
    return bird.move()  # Works for all birds

# ❌ BAD - LSP violated
class Rectangle:
    def set_width(self, w):
        self.width = w
    
    def set_height(self, h):
        self.height = h
    
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def set_width(self, w):
        self.width = w
        self.height = w  # Violates expectation
    
    def set_height(self, h):
        self.width = h
        self.height = h  # Violates expectation
```

## Choosing Relationships

### 1. Decision Framework

```
Question: What relationship do I need?

├─ Is B a specialized type of A?
│  ├─ Yes → Can B substitute for A everywhere?
│  │  ├─ Yes → Use INHERITANCE
│  │  └─ No → Use COMPOSITION
│  └─ No → Does B contain/use A?
│     ├─ B creates A → Use COMPOSITION
│     ├─ B receives A → Use AGGREGATION
│     └─ B delegates to A → Use COMPOSITION
```

### 2. Checklist Questions

**For Inheritance:**
- Is there a clear "is-a" relationship?
- Do I need polymorphic behavior?
- Will the hierarchy stay stable?
- Can I substitute subclass for superclass?

**For Composition:**
- Does the container own the component?
- Should the component's lifetime be tied to the container?
- Do I need to hide implementation details?

**For Aggregation:**
- Can the component exist independently?
- Might the component be shared?
- Should the container just reference the component?

### 3. Common Mistakes

**Inheritance abuse:**
```python
# ❌ BAD - Not a true is-a
class Stack(list):
    pass  # Stack is not really a list

# ✅ GOOD - Composition
class Stack:
    def __init__(self):
        self._items = []  # Has-a list
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()
```

## Design Patterns

### 1. Strategy Pattern

Composition for flexible algorithms:

```python
from abc import ABC, abstractmethod

class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self, data):
        pass

class ZipCompression(CompressionStrategy):
    def compress(self, data):
        return f"Zipped: {data}"

class RarCompression(CompressionStrategy):
    def compress(self, data):
        return f"Rarred: {data}"

class FileCompressor:
    def __init__(self, strategy: CompressionStrategy):
        self.strategy = strategy
    
    def compress_file(self, data):
        return self.strategy.compress(data)

# Flexible at runtime
compressor = FileCompressor(ZipCompression())
compressor.strategy = RarCompression()  # Switch strategy
```

### 2. Decorator Pattern

Composition for adding responsibilities:

```python
class Coffee:
    def cost(self):
        return 5
    
    def description(self):
        return "Coffee"

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 2
    
    def description(self):
        return f"{self.coffee.description()} + Milk"

class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 1
    
    def description(self):
        return f"{self.coffee.description()} + Sugar"

# Build up features
coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)
print(coffee.description())  # Coffee + Milk + Sugar
print(coffee.cost())  # 8
```

### 3. Observer Pattern

Aggregation for event handling:

```python
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class EmailObserver(Observer):
    def update(self, message):
        print(f"Email: {message}")

class SMSObserver(Observer):
    def update(self, message):
        print(f"SMS: {message}")

class NewsPublisher:
    def __init__(self):
        self.subscribers = []  # Aggregated observers
    
    def subscribe(self, observer: Observer):
        self.subscribers.append(observer)
    
    def unsubscribe(self, observer: Observer):
        self.subscribers.remove(observer)
    
    def notify(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)

publisher = NewsPublisher()
email_obs = EmailObserver()
sms_obs = SMSObserver()

publisher.subscribe(email_obs)
publisher.subscribe(sms_obs)
publisher.notify("Breaking news!")
```

## Refactoring Strategies

### 1. Extract Class

Break down god classes:

```python
# Before - God class
class Employee:
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary
        self.tax_rate = 0.2
    
    def calculate_tax(self):
        return self.salary * self.tax_rate
    
    def send_email(self, message):
        print(f"Email to {self.email}: {message}")

# After - Extracted classes
class Contact:
    def __init__(self, email):
        self.email = email

class Salary:
    def __init__(self, amount, tax_rate):
        self.amount = amount
        self.tax_rate = tax_rate
    
    def calculate_tax(self):
        return self.amount * self.tax_rate

class Employee:
    def __init__(self, name, contact, salary):
        self.name = name
        self.contact = contact    # Composition
        self.salary = salary      # Composition
```

### 2. Replace Inheritance with Delegation

```python
# Before - Inheritance
class ArrayList:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)

class Stack(ArrayList):
    def push(self, item):
        self.add(item)
    
    def pop(self):
        return self.items.pop()

# After - Delegation
class Stack:
    def __init__(self):
        self._storage = []  # Composition
    
    def push(self, item):
        self._storage.append(item)
    
    def pop(self):
        return self._storage.pop()
```

### 3. Introduce Parameter Object

```python
# Before - Many parameters
class Order:
    def calculate_shipping(self, weight, distance, urgency):
        # Complex calculation
        pass

# After - Parameter object
class ShippingInfo:
    def __init__(self, weight, distance, urgency):
        self.weight = weight
        self.distance = distance
        self.urgency = urgency

class Order:
    def __init__(self):
        self.shipping_info = None
    
    def calculate_shipping(self):
        return self.shipping_info.weight * self.shipping_info.distance
```

## Testing Implications

### 1. Testability with Composition

```python
# Easy to mock
class MockEmailService:
    def send(self, to, message):
        return f"Mock sent to {to}"

class UserService:
    def __init__(self, email_service):
        self.email_service = email_service
    
    def register_user(self, user):
        self.email_service.send(user.email, "Welcome!")

# Test with mock
service = UserService(MockEmailService())
```

### 2. Testing Inheritance

```python
# Harder to test - must test whole hierarchy
class Animal:
    def __init__(self):
        self.energy = 100
    
    def move(self):
        self.energy -= 10

class Dog(Animal):
    def bark(self):
        return "Woof"

# Must ensure parent behavior works
def test_dog():
    dog = Dog()
    dog.move()  # Testing inherited behavior
    assert dog.energy == 90
```

### 3. Isolation with Composition

```python
# Test components independently
class Engine:
    def start(self):
        return "Started"

class Car:
    def __init__(self, engine):
        self.engine = engine
    
    def start(self):
        return self.engine.start()

# Test Engine alone
def test_engine():
    engine = Engine()
    assert engine.start() == "Started"

# Test Car with mock
def test_car():
    mock_engine = MockEngine()
    car = Car(mock_engine)
    assert car.start() == "Mock started"
```

## Real-World Guidelines

### 1. Domain Modeling

Model business entities properly:

```python
# E-commerce domain
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class CartItem:
    def __init__(self, product, quantity):
        self.product = product  # Aggregation
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []  # Composition of CartItems
    
    def add_item(self, product, quantity):
        self.items.append(CartItem(product, quantity))
```

### 2. Layered Architecture

Organize by responsibility:

```python
# Presentation Layer
class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

# Business Layer
class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

# Data Layer
class UserRepository:
    def __init__(self, database):
        self.database = database
```

### 3. Plugin Architecture

Use composition for extensibility:

```python
class Plugin(ABC):
    @abstractmethod
    def execute(self):
        pass

class Application:
    def __init__(self):
        self.plugins = []  # Aggregation
    
    def register_plugin(self, plugin: Plugin):
        self.plugins.append(plugin)
    
    def run(self):
        for plugin in self.plugins:
            plugin.execute()

# Easy to extend
app = Application()
app.register_plugin(DataPlugin())
app.register_plugin(UIPlugin())
```

## Best Practices

### 1. Minimize Coupling

```python
# ✅ GOOD - Low coupling
class Logger:
    def log(self, message):
        print(message)

class UserService:
    def __init__(self, logger):
        self.logger = logger  # Depends on interface
```

### 2. Program to Interfaces

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def query(self, sql):
        pass

class MySQLDatabase(Database):
    def query(self, sql):
        return "MySQL result"

class Repository:
    def __init__(self, db: Database):
        self.db = db  # Depends on abstraction
```

### 3. Keep It Simple

```python
# Don't over-engineer
# If inheritance works and is simple, use it
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

# Don't force composition when not needed
# This is overkill:
class SpeechBehavior:
    def speak(self):
        return "Woof"

class Dog:
    def __init__(self):
        self.speech = SpeechBehavior()
```

## Summary

### 1. Quick Reference

| Use Case | Recommended Approach |
|----------|---------------------|
| Type hierarchy | Inheritance |
| Building from parts | Composition |
| Shared objects | Aggregation |
| Runtime flexibility | Composition |
| Polymorphism | Inheritance + Composition |
| Testing | Composition |

### 2. Golden Rules

1. **Favor composition over inheritance**
2. **Use inheritance for is-a, composition for has-a**
3. **Keep hierarchies shallow**
4. **Program to interfaces**
5. **Inject dependencies**

### 3. Design Checklist

- [ ] Is the relationship truly is-a?
- [ ] Will the hierarchy stay stable?
- [ ] Do I need runtime flexibility?
- [ ] Can I test easily?
- [ ] Is coupling minimized?
- [ ] Are responsibilities clear?
