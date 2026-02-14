"""
05: Properties and Decorators (@property)

Properties provide a way to customize access to instance attributes.
They allow you to use getter/setter methods while maintaining simple attribute syntax.
"""

# Example 1: Problem without properties
class TemperatureBasic:
    def __init__(self, celsius):
        self.celsius = celsius

temp = TemperatureBasic(25)
print("WITHOUT PROPERTIES:")
print(f"Temperature: {temp.celsius}°C")

# Problem: No validation
temp.celsius = -500  # Unrealistic temperature!
print(f"After invalid assignment: {temp.celsius}°C (This shouldn't be allowed!)")


# Example 2: Using properties with @property decorator
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Protected attribute
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:  # Absolute zero
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Calculated property"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit"""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Another calculated property"""
        return self._celsius + 273.15

print("\n" + "="*50)
print("WITH PROPERTIES:")
temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C")
print(f"In Fahrenheit: {temp.fahrenheit}°F")
print(f"In Kelvin: {temp.kelvin}K")

# Now validation happens automatically
try:
    temp.celsius = -500
except ValueError as e:
    print(f"Validation works! Error: {e}")

# Can set using different units
temp.fahrenheit = 86
print(f"\nSet to 86°F = {temp.celsius}°C")


# Example 3: Read-only properties
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def diameter(self):
        """Read-only property (no setter)"""
        return self._radius * 2
    
    @property
    def area(self):
        """Read-only calculated property"""
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        """Read-only calculated property"""
        return 2 * 3.14159 * self._radius

print("\n" + "="*50)
print("READ-ONLY PROPERTIES:")
circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Diameter: {circle.diameter}")
print(f"Area: {circle.area:.2f}")
print(f"Circumference: {circle.circumference:.2f}")

# Can change radius
circle.radius = 10
print(f"\nAfter changing radius to 10:")
print(f"Diameter: {circle.diameter}")
print(f"Area: {circle.area:.2f}")

# Cannot change diameter directly (no setter)
try:
    circle.diameter = 50
except AttributeError as e:
    print(f"\nCannot set diameter: {e}")


# Example 4: Properties with validation logic
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._email = None
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if value and '@' not in value:
            raise ValueError("Invalid email format")
        self._email = value
    
    @property
    def is_adult(self):
        """Computed property"""
        return self._age >= 18

print("\n" + "="*50)
print("VALIDATION WITH PROPERTIES:")
person = Person("Alice", 25)
print(f"{person.name} is {person.age} years old")
print(f"Is adult: {person.is_adult}")

# Validation in action
try:
    person.age = -5
except ValueError as e:
    print(f"Validation error: {e}")

try:
    person.email = "invalid-email"
except ValueError as e:
    print(f"Email validation error: {e}")

person.email = "alice@example.com"
print(f"Valid email set: {person.email}")


# Example 5: Properties with lazy loading
class DataProcessor:
    def __init__(self, filename):
        self._filename = filename
        self._data = None  # Not loaded yet
        self._processed = None
    
    @property
    def data(self):
        """Lazy loading - only load when accessed"""
        if self._data is None:
            print(f"Loading data from {self._filename}...")
            # Simulate loading data
            self._data = [1, 2, 3, 4, 5]
        return self._data
    
    @property
    def processed_data(self):
        """Process data only when needed"""
        if self._processed is None:
            print("Processing data...")
            self._processed = [x * 2 for x in self.data]
        return self._processed

print("\n" + "="*50)
print("LAZY LOADING WITH PROPERTIES:")
processor = DataProcessor("data.txt")
print("DataProcessor created (data not loaded yet)")
print(f"Accessing data: {processor.data}")  # Loads here
print(f"Accessing again: {processor.data}")  # Uses cached version
print(f"Processed: {processor.processed_data}")


# Example 6: Using properties for data transformation
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price
        self._discount = 0
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self._discount = value
    
    @property
    def final_price(self):
        """Calculated property with discount"""
        return self._price * (1 - self._discount / 100)
    
    @property
    def savings(self):
        """How much money is saved"""
        return self._price - self.final_price

print("\n" + "="*50)
print("DATA TRANSFORMATION:")
product = Product("Laptop", 1000)
print(f"Original price: ${product.price}")
product.discount = 20
print(f"With 20% discount: ${product.final_price:.2f}")
print(f"You save: ${product.savings:.2f}")


# Example 7: Properties vs regular methods comparison
class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    # Using property
    @property
    def area(self):
        return self._length * self._width
    
    # Using method
    def calculate_area(self):
        return self._length * self._width

print("\n" + "="*50)
print("PROPERTY VS METHOD:")
rect = Rectangle(5, 3)

# Property: accessed like an attribute
print(f"Using property: {rect.area}")

# Method: needs parentheses
print(f"Using method: {rect.calculate_area()}")

# Property is more intuitive for calculated values


# Key Takeaways:
# 1. @property makes methods accessible like attributes
# 2. Provides encapsulation - hide implementation details
# 3. Allows validation when setting values
# 4. Can create read-only properties (no setter)
# 5. Good for computed/derived values
# 6. Maintains clean syntax while adding functionality
# 7. Can implement lazy loading
# 8. Use properties when value needs computation or validation
# 9. Use regular methods when action/operation is being performed
