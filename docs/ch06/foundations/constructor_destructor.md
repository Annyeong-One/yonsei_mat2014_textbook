# Constructor & Destructor

Constructor (`__init__`) and destructor (`__del__`) manage object lifecycle in Python.

---

## Constructor: `__init__`

### 1. Purpose

Initializes new objects immediately after creation.

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

alice = Student("Alice", "Math")
```

### 2. Automatic Call

Python automatically calls `__init__` during instantiation.

```python
# These are equivalent:
a = Student("Lee", "Math")
# Student.__init__(a, "Lee", "Math")
```

### 3. Not Optional

Every class should define `__init__` for clarity.

---

## Bad Practice: No Constructor

### 1. Dynamic Assignment

```python
class Student:
    pass

a = Student()
a.name = "Lee"
a.major = "Math"
```

### 2. Problems

- No enforcement of required fields
- Runtime errors from typos
- Unclear object requirements
- Violates encapsulation

### 3. Fragile Code

```python
b = Student()
b.name = "Kim"
# Forgot to set major!
print(b.major)  # AttributeError
```

---

## Good Practice: With Constructor

### 1. Structured Initialization

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

a = Student("Lee", "Math")
```

### 2. Benefits

- Parameters are explicit
- Required fields enforced
- Self-documenting code
- Enables validation

### 3. With Validation

```python
class Student:
    def __init__(self, name, major):
        if not name:
            raise ValueError("Name required")
        self.name = name
        self.major = major
```

---

## Introspection with `vars()`

### 1. View Attributes

```python
alice = Student("Alice", "Statistics")
print(vars(alice))
# {'name': 'Alice', 'major': 'Statistics'}
```

### 2. Same as `__dict__`

```python
print(alice.__dict__)
# Same output as vars(alice)
```

### 3. Debugging Aid

Useful for inspecting object state.

---

## Constructor Patterns

### 1. Simple Assignment

```python
class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
```

### 2. With Defaults

```python
class Car:
    def __init__(self, speed=0, color="black"):
        self.speed = speed
        self.color = color
```

### 3. With Computation

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height  # computed
```

---

## Destructor: `__del__`

### 1. Purpose

Called when object is about to be destroyed.

```python
class IceCream:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"{self.name} created")
    
    def __del__(self):
        print(f"{self.name} destroyed")
```

### 2. Non-Deterministic

Timing is unpredictable—depends on garbage collection.

```python
obj = IceCream("Cone", 1500)
del obj
# Destructor may or may not run immediately
```

### 3. Reference Counting

```python
obj1 = IceCream("Cone", 1500)
obj2 = obj1  # Two references
del obj1     # __del__ NOT called yet
del obj2     # Now __del__ is called
```

---

## Destructor Limitations

### 1. Unreliable Timing

```python
def create_objects():
    obj = IceCream("Cone", 1500)
    # When is __del__ called? Unknown!

create_objects()
```

### 2. Circular References

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
a.next = b
b.next = a  # Circular reference
# Destructors may never run!
```

### 3. No Guarantees

Python doesn't guarantee `__del__` will be called.

---

## Better Alternatives

### 1. Context Managers

```python
class FileHandler:
    def __enter__(self):
        self.file = open("data.txt", "w")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileHandler() as f:
    f.write("data")
# Guaranteed cleanup
```

### 2. Explicit Methods

```python
class Resource:
    def __init__(self):
        self.resource = acquire_resource()
    
    def close(self):
        release_resource(self.resource)

r = Resource()
try:
    # Use resource
    pass
finally:
    r.close()
```

### 3. `contextlib`

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    resource = acquire_resource()
    try:
        yield resource
    finally:
        release_resource(resource)
```

---

## Constructor Best Practices

### 1. Keep Simple

```python
# Good
def __init__(self, name):
    self.name = name

# Bad - too much logic
def __init__(self, name):
    self.name = name
    self.connect_to_database()
    self.load_all_data()
```

### 2. Validate Input

```python
def __init__(self, age):
    if age < 0:
        raise ValueError("Age must be positive")
    self.age = age
```

### 3. Document Parameters

```python
def __init__(self, name, age):
    """
    Initialize a Person.
    
    Args:
        name (str): Person's name
        age (int): Person's age
    """
    self.name = name
    self.age = age
```

---

## Key Takeaways

- `__init__` initializes objects—always define it.
- Use constructors to enforce required fields.
- `vars()` and `__dict__` inspect object state.
- `__del__` is unreliable—avoid for cleanup.
- Use context managers for resource management.

---

## Runnable Example: `classes_advanced_examples.py`

```python
"""
Advanced Classes and Objects Examples
Demonstrating special methods, class methods, static methods, and design patterns
"""

# ============================================================================
# Example 1: Special Methods (Magic Methods)

if __name__ == "__main__":
    print("=" * 50)
    print("Example 1: Special Methods - Vector Class")
    print("=" * 50)

    class Vector2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"Vector({self.x}, {self.y})"

        def __repr__(self):
            return f"Vector2D(x={self.x}, y={self.y})"

        def __add__(self, other):
            return Vector2D(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            return Vector2D(self.x - other.x, self.y - other.y)

        def __mul__(self, scalar):
            return Vector2D(self.x * scalar, self.y * scalar)

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        def __abs__(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5

        def __len__(self):
            return 2

        def __getitem__(self, index):
            if index == 0:
                return self.x
            elif index == 1:
                return self.y
            raise IndexError("Vector index out of range")

    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"v1 + v2: {v1 + v2}")
    print(f"v1 - v2: {v1 - v2}")
    print(f"v1 * 3: {v1 * 3}")
    print(f"v1 == v2: {v1 == v2}")
    print(f"|v1|: {abs(v1)}")
    print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")
    print()

    # ============================================================================
    # Example 2: Class Methods and Static Methods
    print("=" * 50)
    print("Example 2: Class Methods and Static Methods")
    print("=" * 50)

    class Employee:
        company = "TechCorp"
        num_employees = 0
        raise_amount = 1.04

        def __init__(self, name, salary):
            self.name = name
            self.salary = salary
            Employee.num_employees += 1

        def apply_raise(self):
            self.salary = int(self.salary * self.raise_amount)

        @classmethod
        def set_raise_amount(cls, amount):
            cls.raise_amount = amount

        @classmethod
        def from_string(cls, emp_string):
            """Alternative constructor"""
            name, salary = emp_string.split('-')
            return cls(name, int(salary))

        @staticmethod
        def is_workday(day):
            """Utility method that doesn't need instance or class"""
            return day.weekday() < 5

        def __str__(self):
            return f"{self.name}: ${self.salary}"

    # Regular instantiation
    emp1 = Employee("John", 50000)
    emp2 = Employee("Jane", 60000)

    print(f"Company: {Employee.company}")
    print(f"Employees: {Employee.num_employees}")
    print(emp1)
    print(emp2)

    # Using class method to change class variable
    Employee.set_raise_amount(1.05)
    emp1.apply_raise()
    print(f"After raise: {emp1}")

    # Using alternative constructor
    emp3 = Employee.from_string("Bob-55000")
    print(f"Created from string: {emp3}")

    # Using static method
    from datetime import date
    today = date.today()
    print(f"Is today a workday? {Employee.is_workday(today)}")
    print()

    # ============================================================================
    # Example 3: Properties and Validation
    print("=" * 50)
    print("Example 3: Properties with Validation")
    print("=" * 50)

    class Person:
        def __init__(self, name, age):
            self._name = name
            self.age = age  # Uses setter

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            if not value or not isinstance(value, str):
                raise ValueError("Name must be a non-empty string")
            self._name = value

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self, value):
            if not isinstance(value, int) or value < 0 or value > 150:
                raise ValueError("Age must be between 0 and 150")
            self._age = value

        @property
        def is_adult(self):
            return self._age >= 18

        def __str__(self):
            return f"{self._name}, {self._age} years old"

    person = Person("Alice", 25)
    print(person)
    print(f"Is adult? {person.is_adult}")

    person.age = 30
    print(f"After birthday: {person}")

    try:
        person.age = -5  # Will raise error
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # ============================================================================
    # Example 4: Composition Pattern
    print("=" * 50)
    print("Example 4: Composition - Building Complex Objects")
    print("=" * 50)

    class Engine:
        def __init__(self, horsepower, type):
            self.horsepower = horsepower
            self.type = type
            self.running = False

        def start(self):
            self.running = True
            return f"{self.horsepower}HP {self.type} engine started"

        def stop(self):
            self.running = False
            return "Engine stopped"

    class GPS:
        def __init__(self):
            self.current_location = "Unknown"

        def set_location(self, location):
            self.current_location = location

        def navigate_to(self, destination):
            return f"Navigating from {self.current_location} to {destination}"

    class Car:
        def __init__(self, model, horsepower, engine_type):
            self.model = model
            self.engine = Engine(horsepower, engine_type)
            self.gps = GPS()
            self.speed = 0

        def start(self):
            return f"{self.model}: {self.engine.start()}"

        def accelerate(self, amount):
            if self.engine.running:
                self.speed += amount
                return f"Speed: {self.speed} mph"
            return "Start engine first!"

        def navigate(self, destination):
            return self.gps.navigate_to(destination)

    car = Car("Tesla Model S", 670, "Electric")
    print(car.start())
    print(car.accelerate(30))
    print(car.accelerate(20))
    car.gps.set_location("San Francisco")
    print(car.navigate("Los Angeles"))
    print()

    # ============================================================================
    # Example 5: Context Manager (with statement)
    print("=" * 50)
    print("Example 5: Context Manager")
    print("=" * 50)

    class FileManager:
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None

        def __enter__(self):
            self.file = open(self.filename, self.mode)
            return self.file

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()
            return False

    # Using the context manager
    with FileManager('test.txt', 'w') as f:
        f.write("Hello from context manager!\n")
        f.write("File will be closed automatically.\n")

    print("File written and closed automatically")

    # Read back
    with FileManager('test.txt', 'r') as f:
        content = f.read()
        print(f"File content:\n{content}")
    print()

    # ============================================================================
    # Example 6: Callable Objects
    print("=" * 50)
    print("Example 6: Callable Objects")
    print("=" * 50)

    class Multiplier:
        def __init__(self, factor):
            self.factor = factor

        def __call__(self, x):
            return x * self.factor

    double = Multiplier(2)
    triple = Multiplier(3)

    print(f"Double 5: {double(5)}")
    print(f"Triple 5: {triple(5)}")
    print(f"Double 10: {double(10)}")
    print()

    # ============================================================================
    # Example 7: Descriptors (Advanced)
    print("=" * 50)
    print("Example 7: Descriptors for Validation")
    print("=" * 50)

    class PositiveNumber:
        def __init__(self, name):
            self.name = name

        def __get__(self, obj, objtype=None):
            return obj.__dict__.get(self.name, 0)

        def __set__(self, obj, value):
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f"{self.name} must be a positive number")
            obj.__dict__[self.name] = value

    class Product:
        price = PositiveNumber("price")
        quantity = PositiveNumber("quantity")

        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        @property
        def total_value(self):
            return self.price * self.quantity

    product = Product("Laptop", 999.99, 5)
    print(f"{product.name}: ${product.price} x {product.quantity}")
    print(f"Total value: ${product.total_value}")

    try:
        product.price = -10  # Will raise error
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # ============================================================================
    # Example 8: Iterator Pattern
    print("=" * 50)
    print("Example 8: Custom Iterator")
    print("=" * 50)

    class Countdown:
        def __init__(self, start):
            self.current = start

        def __iter__(self):
            return self

        def __next__(self):
            if self.current <= 0:
                raise StopIteration
            self.current -= 1
            return self.current + 1

    print("Countdown from 5:")
    for num in Countdown(5):
        print(num, end=" ")
    print("\n")

    # Clean up test file
    import os
    if os.path.exists('test.txt'):
        os.remove('test.txt')
        print("Cleaned up test file")
```
