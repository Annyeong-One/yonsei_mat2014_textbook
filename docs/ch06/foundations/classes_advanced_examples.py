"""
Advanced Classes and Objects Examples
Demonstrating special methods, class methods, static methods, and design patterns
"""

# Example 1: Special Methods (Magic Methods)
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
