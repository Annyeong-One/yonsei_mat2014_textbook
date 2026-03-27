# Class Attributes

Class attributes are shared across all instances of a class, storing data that belongs to the class itself.

---

## What are Class Attributes

### 1. Shared Variables

```python
class Student:
    university = 'Yonsei'  # class attribute
    
    def __init__(self, name):
        self.name = name  # instance attribute

a = Student("Lee")
b = Student("Kim")
print(a.university)  # 'Yonsei'
print(b.university)  # 'Yonsei' - same value
```

### 2. Belong to Class

```python
print(Student.university)  # Access via class
```

### 3. Single Copy

Only one copy shared by all instances.

---

## Defining Class Attributes

### 1. At Class Level

```python
class Student:
    university = 'Yonsei'     # class attribute
    num_students = 0          # class attribute
    students_list = []        # class attribute
    mandatory = ['Chapel']    # class attribute
```

### 2. Not in `__init__`

```python
class Student:
    university = 'Yonsei'  # class level
    
    def __init__(self, name):
        self.name = name  # instance level
```

### 3. Outside Methods

Defined directly in class body.

---

## Correct Usage

### 1. Modify via Class

```python
class Student:
    num_students = 0
    
    def __init__(self, name):
        self.name = name
        Student.num_students += 1  # Correct!

a = Student("Lee")
b = Student("Kim")
print(Student.num_students)  # 2
```

### 2. Shared Lists

```python
class Student:
    students_list = []
    
    def __init__(self, name):
        self.name = name
        Student.students_list.append(self)
```

### 3. Constants

```python
class Math:
    PI = 3.14159
    E = 2.71828
```

---

## Wrong Usage

### 1. Modifying via `self`

```python
# WRONG
class Student:
    num_students = 0
    
    def __init__(self, name):
        self.num_students += 1  # Creates instance attribute!

a = Student("Lee")
b = Student("Kim")
print(Student.num_students)  # Still 0!
```

### 2. Creates Instance Attribute

```python
a = Student("Lee")
print(a.__dict__)  # {'name': 'Lee', 'num_students': 1}
print(Student.__dict__)  # num_students still 0
```

### 3. Shadowing

Instance attribute shadows class attribute.

---

## Class Attribute Use Cases

### 1. Counters

```python
class Student:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Student.count += 1
```

### 2. Shared Configuration

```python
class Logger:
    enable_debug = False  # Shared flag
    
    def log(self, msg):
        if Logger.enable_debug:
            print(msg)
```

### 3. Default Values

```python
class Connection:
    default_timeout = 30
    
    def __init__(self, timeout=None):
        self.timeout = timeout or Connection.default_timeout
```

---

## Logger Example

### 1. Wrong: Instance Flag

```python
# WRONG - each instance has own flag
class Logger:
    enable_debug = False
    
    def print(self, msg):
        if self.enable_debug:
            print(msg)
    
    def set_debug(self):
        self.enable_debug = True  # Instance attribute!

a = Logger()
b = Logger()
a.set_debug()
a.print("hello")  # Prints
b.print("hello")  # Doesn't print
```

### 2. Correct: Class Method

```python
# CORRECT - modify class attribute
class Logger:
    enable_debug = False
    
    def print(self, msg):
        if Logger.enable_debug:
            print(msg)
    
    @classmethod
    def set_debug(cls):
        cls.enable_debug = True  # Class attribute!

a = Logger()
b = Logger()
Logger.set_debug()
a.print("hello")  # Prints
b.print("hello")  # Prints
```

### 3. Affects All Instances

Class method modifies shared state.

---

## Class `__dict__`

### 1. Read-Only Mapping

```python
class Student:
    university = 'Yonsei'
    num_students = 0

print(Student.__dict__)
# mappingproxy({'university': 'Yonsei', 'num_students': 0, ...})
```

### 2. Access Attributes

```python
print(Student.__dict__['university'])  # 'Yonsei'
```

### 3. `vars()` on Class

```python
print(vars(Student))
# Same as Student.__dict__
```

---

## Special Class Attributes

### 1. `__doc__`

```python
class Car:
    """This is a Car class."""
    pass

print(Car.__doc__)
# "This is a Car class."
```

### 2. `__name__`

```python
print(Car.__name__)  # 'Car'
```

### 3. `__module__`

```python
print(Car.__module__)  # '__main__'
```

---

## Instance vs Class

### 1. Instance `__dict__`

```python
a = Student("Lee", "Math")
print(a.__dict__)
# {'name': 'Lee', 'major': 'Math'}
```

### 2. Class `__dict__`

```python
print(Student.__dict__)
# {'university': 'Yonsei', 'num_students': 0, ...}
```

### 3. Separate Namespaces

Instance and class have different dictionaries.

---

## Lookup Order

### 1. Instance First

```python
class A:
    x = 10

a = A()
print(a.x)  # 10 - found in class
```

### 2. Then Class

```python
a.x = 20  # Create instance attribute
print(a.x)  # 20 - found in instance
print(A.x)  # 10 - class unchanged
```

### 3. Instance Shadows Class

Instance attribute hides class attribute of same name.

---

## Best Practices

### 1. Use Class Name

```python
# Good
Student.num_students += 1

# Avoid
self.num_students += 1
```

### 2. Use `@classmethod`

```python
@classmethod
def increment_count(cls):
    cls.num_students += 1
```

### 3. Document Purpose

```python
class Config:
    """Global configuration settings."""
    DEBUG = False  # Class attribute for all instances
```

---

## Key Takeaways

- Class attributes are shared across instances.
- Modify via class name, not `self`.
- Using `self` creates instance attribute.
- Use `@classmethod` for class-level operations.
- Class `__dict__` is read-only mapping.

---

## Runnable Example: `instance_vs_class_tutorial.py`

```python
"""
03: Instance vs Class Attributes and Methods

Understanding the difference between instance-level and class-level members.
"""

# ============================================================================
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

if __name__ == "__main__":

    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Max", 5)

    print("Instance attributes (different for each object):")
    print(f"{dog1.name} is {dog1.age} years old")
    print(f"{dog2.name} is {dog2.age} years old")

    print("\nClass attribute (same for all objects):")
    print(f"{dog1.name} is a {dog1.species}")
    print(f"{dog2.name} is a {dog2.species}")
    print(f"Total dogs created: {Dog.total_dogs}")


    # ============================================================================
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


    # ============================================================================
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


    # ============================================================================
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


    # ============================================================================
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
```
