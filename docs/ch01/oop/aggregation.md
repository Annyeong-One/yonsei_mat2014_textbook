# Aggregation Pattern

## Weak Has-a

### 1. Definition

**Aggregation** is a weak form of association where:

- One class **uses** instances of another class
- Components have **independent lifetimes**
- Components are **passed in**, not created internally
- Models **shared ownership** relationships

### 2. Ownership Model

The container **references but doesn't own** its components:

```python
class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, players):
        self.players = players  # Passed in, not created

# Players exist independently
alice = Player("Alice")
bob = Player("Bob")

# Team uses existing players
team = Team([alice, bob])

del team  # Team destroyed, but players still exist
print(alice.name)  # Alice (still accessible)
```

### 3. Key Principle

Components **can exist meaningfully** outside their container.

## Implementation

### 1. Basic Pattern

```python
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []  # Collection of references
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        return [book.title for book in self.books]

# Books exist independently
book1 = Book("Python Guide")
book2 = Book("Design Patterns")

# Library aggregates books
library = Library()
library.add_book(book1)
library.add_book(book2)

# Books survive library deletion
del library
print(book1.title)  # Python Guide (still exists)
```

### 2. Multiple Containers

Same objects can be shared across containers:

```python
class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def enroll(self, student):
        self.students.append(student)

# Student exists independently
alice = Student("Alice")

# Shared across multiple courses
math = Course("Mathematics")
physics = Course("Physics")

math.enroll(alice)
physics.enroll(alice)  # Same student in multiple courses
```

### 3. Dynamic Assembly

Components can be added/removed dynamically:

```python
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def remove_employee(self, employee):
        self.employees.remove(employee)

# Employees exist independently
alice = Employee("Alice")
bob = Employee("Bob")

# Dynamic team assembly
engineering = Department("Engineering")
engineering.add_employee(alice)
engineering.add_employee(bob)

# Move employee to different department
marketing = Department("Marketing")
engineering.remove_employee(alice)
marketing.add_employee(alice)
```

## Characteristics

### 1. Shared Ownership

Multiple containers can reference the same object:

```python
class Professor:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self):
        self.faculty = []

class ResearchLab:
    def __init__(self):
        self.researchers = []

# Professor shared between university and lab
prof = Professor("Dr. Smith")

university = University()
university.faculty.append(prof)

lab = ResearchLab()
lab.researchers.append(prof)  # Same professor, different contexts
```

### 2. Independent Lifecycle

```python
class Musician:
    def __init__(self, name):
        self.name = name

class Band:
    def __init__(self, musicians):
        self.musicians = musicians

# Musicians exist before band
guitar = Musician("Eric")
drums = Musician("Dave")

# Band formed
band = Band([guitar, drums])

# Band disbanded
del band

# Musicians continue their careers
print(guitar.name)  # Eric (still exists)
print(drums.name)   # Dave (still exists)
```

### 3. Plug-and-Play

Easy to swap components:

```python
class Driver:
    def __init__(self, name):
        self.name = name

class RaceCar:
    def __init__(self, driver=None):
        self.driver = driver
    
    def change_driver(self, new_driver):
        self.driver = new_driver

# Drivers independent
lewis = Driver("Lewis")
max = Driver("Max")

# Car with driver
car = RaceCar(lewis)

# Switch drivers
car.change_driver(max)
```

## vs Composition

### 1. Lifetime Comparison

```python
# COMPOSITION - Engine dies with Car
class Car:
    def __init__(self):
        self.engine = Engine()  # Created internally

car = Car()
del car  # Engine destroyed too

# AGGREGATION - Driver survives Team
class Team:
    def __init__(self, driver):
        self.driver = driver  # Passed in

driver = Driver("Lewis")
team = Team(driver)
del team  # Driver still exists
```

### 2. Creation Comparison

```python
# COMPOSITION - Container creates
class House:
    def __init__(self):
        self.rooms = [Room() for _ in range(5)]  # Created here

# AGGREGATION - Container receives
class Hotel:
    def __init__(self, rooms):
        self.rooms = rooms  # Passed in

rooms = [Room() for _ in range(100)]
hotel = Hotel(rooms)
```

### 3. Ownership Comparison

| Aspect | Composition | Aggregation |
|--------|-------------|-------------|
| Creation | Internal | External |
| Ownership | Exclusive | Shared |
| Lifetime | Dependent | Independent |
| Coupling | Strong | Weak |

## Design Patterns

### 1. Observer Pattern

```python
class Observer:
    def update(self, message):
        print(f"Received: {message}")

class Subject:
    def __init__(self):
        self.observers = []  # Aggregated
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def detach(self, observer):
        self.observers.remove(observer)
    
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

# Observers exist independently
obs1 = Observer()
obs2 = Observer()

# Subject aggregates observers
subject = Subject()
subject.attach(obs1)
subject.attach(obs2)
subject.notify("Event occurred")

# Observers can be detached and reused
subject.detach(obs1)
another_subject = Subject()
another_subject.attach(obs1)
```

### 2. Strategy Pattern

```python
class SortStrategy:
    def sort(self, data):
        pass

class QuickSort(SortStrategy):
    def sort(self, data):
        return sorted(data)  # Simplified

class BubbleSort(SortStrategy):
    def sort(self, data):
        return sorted(data)  # Simplified

class DataProcessor:
    def __init__(self, strategy=None):
        self.strategy = strategy  # Aggregated
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def process(self, data):
        return self.strategy.sort(data)

# Strategies exist independently
quick = QuickSort()
bubble = BubbleSort()

# Processor aggregates strategy
processor = DataProcessor(quick)
processor.process([3, 1, 2])

# Switch strategy at runtime
processor.set_strategy(bubble)
```

### 3. Repository Pattern

```python
class Entity:
    def __init__(self, id, data):
        self.id = id
        self.data = data

class Repository:
    def __init__(self):
        self.entities = {}  # Aggregated entities
    
    def add(self, entity):
        self.entities[entity.id] = entity
    
    def get(self, id):
        return self.entities.get(id)
    
    def remove(self, id):
        if id in self.entities:
            del self.entities[id]

# Entities exist independently
user1 = Entity(1, {"name": "Alice"})
user2 = Entity(2, {"name": "Bob"})

# Repository aggregates entities
repo = Repository()
repo.add(user1)
repo.add(user2)

# Entities can be removed from repo but still exist
repo.remove(1)
print(user1.data)  # Still accessible
```

## Common Use Cases

### 1. Collections

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add(self, product):
        self.items.append(product)
    
    def remove(self, product):
        self.items.remove(product)
    
    def total(self):
        return sum(item.price for item in self.items)

# Products exist independently
laptop = Product("Laptop", 1000)
mouse = Product("Mouse", 50)

# Cart aggregates products
cart = ShoppingCart()
cart.add(laptop)
cart.add(mouse)

# Products can move between carts
cart2 = ShoppingCart()
cart.remove(laptop)
cart2.add(laptop)
```

### 2. Membership

```python
class Member:
    def __init__(self, name):
        self.name = name

class Club:
    def __init__(self, name):
        self.name = name
        self.members = []
    
    def join(self, member):
        self.members.append(member)
    
    def leave(self, member):
        self.members.remove(member)

# Members exist independently
alice = Member("Alice")

# Can join multiple clubs
chess_club = Club("Chess")
book_club = Club("Books")

chess_club.join(alice)
book_club.join(alice)

# Can leave clubs
chess_club.leave(alice)
```

### 3. Associations

```python
class Doctor:
    def __init__(self, name):
        self.name = name

class Patient:
    def __init__(self, name):
        self.name = name

class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []
    
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
    
    def add_patient(self, patient):
        self.patients.append(patient)

# Both exist independently
dr_smith = Doctor("Dr. Smith")
patient_john = Patient("John")

# Hospital aggregates both
hospital = Hospital()
hospital.add_doctor(dr_smith)
hospital.add_patient(patient_john)

# Doctor can work at multiple hospitals
hospital2 = Hospital()
hospital2.add_doctor(dr_smith)
```

## Benefits

### 1. Flexibility

Easy to reconfigure:

```python
class Component:
    def __init__(self, name):
        self.name = name

class System:
    def __init__(self, components):
        self.components = components
    
    def reconfigure(self, new_components):
        self.components = new_components

# Flexible assembly
comp1 = Component("A")
comp2 = Component("B")
comp3 = Component("C")

system = System([comp1, comp2])
system.reconfigure([comp2, comp3])  # Easy change
```

### 2. Reusability

Share objects across systems:

```python
class Sensor:
    def __init__(self, type):
        self.type = type
    
    def read(self):
        return f"Reading from {self.type}"

class MonitoringSystem:
    def __init__(self, sensors):
        self.sensors = sensors

class AlertSystem:
    def __init__(self, sensors):
        self.sensors = sensors

# Shared sensors
temp_sensor = Sensor("Temperature")
pressure_sensor = Sensor("Pressure")

# Used by multiple systems
monitor = MonitoringSystem([temp_sensor, pressure_sensor])
alerts = AlertSystem([temp_sensor])  # Reused
```

### 3. Testability

Easy to inject test doubles:

```python
class MockPlayer:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, players):
        self.players = players

# Easy testing with mocks
mock_players = [MockPlayer(f"Player{i}") for i in range(5)]
team = Team(mock_players)
```

## Best Practices

### 1. Clear Interfaces

Define how aggregated objects interact:

```python
from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def execute(self):
        pass

class Application:
    def __init__(self):
        self.plugins = []
    
    def register(self, plugin: Plugin):
        self.plugins.append(plugin)
    
    def run(self):
        for plugin in self.plugins:
            plugin.execute()
```

### 2. Null Handling

Handle missing aggregated objects:

```python
class Team:
    def __init__(self, coach=None):
        self.coach = coach
    
    def get_coach_name(self):
        return self.coach.name if self.coach else "No coach"
```

### 3. Defensive Copying

Prevent external modification:

```python
class Playlist:
    def __init__(self, songs):
        self.songs = list(songs)  # Defensive copy
    
    def get_songs(self):
        return list(self.songs)  # Return copy
```
