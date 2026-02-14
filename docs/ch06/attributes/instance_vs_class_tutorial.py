"""
03: Instance vs Class Attributes and Methods

Understanding the difference between instance-level and class-level members.
"""

# Example 1: Instance vs Class Attributes
class Dog:
    # Class attribute - shared by ALL dogs
    species = "Canis familiaris"
    total_dogs = 0
    
    def __init__(self, name, age):
        # Instance attributes - unique to each dog
        self.name = name
        self.age = age
        Dog.total_dogs += 1  # Increment class attribute

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print("Instance attributes (different for each object):")
print(f"{dog1.name} is {dog1.age} years old")
print(f"{dog2.name} is {dog2.age} years old")

print("\nClass attribute (same for all objects):")
print(f"{dog1.name} is a {dog1.species}")
print(f"{dog2.name} is a {dog2.species}")
print(f"Total dogs created: {Dog.total_dogs}")


# Example 2: Class Methods
class Employee:
    # Class attributes
    company_name = "TechCorp"
    employee_count = 0
    raise_percentage = 1.05
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    # Instance method (works with instance data)
    def apply_raise(self):
        self.salary = int(self.salary * Employee.raise_percentage)
        return f"{self.name}'s new salary: ${self.salary}"
    
    # Class method (works with class data)
    @classmethod
    def set_raise_percentage(cls, percentage):
        cls.raise_percentage = percentage
    
    @classmethod
    def get_employee_count(cls):
        return f"Total employees: {cls.employee_count}"
    
    @classmethod
    def from_string(cls, emp_string):
        # Alternative constructor
        name, salary = emp_string.split('-')
        return cls(name, int(salary))

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(f"\n{Employee.get_employee_count()}")
print(f"{emp1.apply_raise()}")

# Using class method to change class attribute
Employee.set_raise_percentage(1.10)
print(f"{emp2.apply_raise()}")

# Using alternative constructor (class method)
emp3 = Employee.from_string("Charlie-55000")
print(f"\nCreated employee: {emp3.name} with salary ${emp3.salary}")


# Example 3: Static Methods
class MathOperations:
    """A collection of mathematical operations"""
    
    # Static method - doesn't use instance or class data
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    
    @staticmethod
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

# Static methods can be called without creating an instance
print(f"\n10 + 5 = {MathOperations.add(10, 5)}")
print(f"10 × 5 = {MathOperations.multiply(10, 5)}")
print(f"Is 10 even? {MathOperations.is_even(10)}")
print(f"Is 17 prime? {MathOperations.is_prime(17)}")


# Example 4: When to use what
class Pizza:
    # Class attribute - shared information
    menu_prices = {"small": 8.99, "medium": 12.99, "large": 16.99}
    total_orders = 0
    
    def __init__(self, size, toppings):
        # Instance attributes - specific to this order
        self.size = size
        self.toppings = toppings
        self.price = self._calculate_price()
        Pizza.total_orders += 1
    
    # Instance method - uses instance data
    def _calculate_price(self):
        base_price = Pizza.menu_prices[self.size]
        topping_cost = len(self.toppings) * 1.50
        return base_price + topping_cost
    
    def get_description(self):
        toppings_str = ", ".join(self.toppings)
        return f"{self.size.capitalize()} pizza with {toppings_str} - ${self.price:.2f}"
    
    # Class method - works with class data
    @classmethod
    def update_price(cls, size, new_price):
        cls.menu_prices[size] = new_price
    
    @classmethod
    def get_total_orders(cls):
        return cls.total_orders
    
    # Static method - utility function, doesn't need instance or class
    @staticmethod
    def is_valid_size(size):
        return size in ["small", "medium", "large"]

order1 = Pizza("large", ["pepperoni", "mushrooms"])
order2 = Pizza("medium", ["cheese"])

print(f"\n{order1.get_description()}")
print(f"{order2.get_description()}")
print(f"Total orders: {Pizza.get_total_orders()}")

# Using static method
print(f"\nIs 'extra-large' a valid size? {Pizza.is_valid_size('extra-large')}")
print(f"Is 'medium' a valid size? {Pizza.is_valid_size('medium')}")


# Example 5: Comparison table
print("\n" + "="*70)
print("COMPARISON: Instance vs Class vs Static")
print("="*70)

class Example:
    class_var = "I am a class variable"
    
    def __init__(self, value):
        self.instance_var = value
    
    def instance_method(self):
        # Can access both instance and class variables
        return f"Instance: {self.instance_var}, Class: {Example.class_var}"
    
    @classmethod
    def class_method(cls):
        # Can only access class variables (no self)
        return f"Class method accessing: {cls.class_var}"
    
    @staticmethod
    def static_method():
        # Cannot access instance or class variables directly
        return "Static method - independent function"

obj = Example("my value")
print("\nInstance Method:", obj.instance_method())
print("Class Method:", Example.class_method())
print("Static Method:", Example.static_method())


# Key Takeaways:
# 1. INSTANCE ATTRIBUTES: Unique to each object, defined with self
# 2. CLASS ATTRIBUTES: Shared by all objects, defined at class level
# 3. INSTANCE METHODS: Use 'self', access instance data
# 4. CLASS METHODS: Use '@classmethod' and 'cls', access class data
# 5. STATIC METHODS: Use '@staticmethod', don't access instance or class data
# 6. Access class attributes with ClassName.attribute or self.attribute
# 7. Class methods often used as alternative constructors
# 8. Static methods are utility functions related to the class
