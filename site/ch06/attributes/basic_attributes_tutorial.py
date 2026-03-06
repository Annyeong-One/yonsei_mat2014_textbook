"""
01: Basic Attributes in Python

Attributes are variables that belong to a class or object.
They store the state/data of an object.
"""

# ============================================================================
# Example 1: Creating a class with attributes
class Dog:
    def __init__(self, name, age, breed):
        # Instance attributes - unique to each Dog object
        self.name = name
        self.age = age
        self.breed = breed

# Creating objects (instances) of the Dog class

if __name__ == "__main__":
    dog1 = Dog("Buddy", 3, "Golden Retriever")
    dog2 = Dog("Max", 5, "German Shepherd")

    # Accessing attributes
    print(f"{dog1.name} is a {dog1.age}-year-old {dog1.breed}")
    print(f"{dog2.name} is a {dog2.age}-year-old {dog2.breed}")

    # Modifying attributes
    dog1.age = 4
    print(f"\n{dog1.name} just had a birthday! Now {dog1.age} years old")


    # ============================================================================
    # Example 2: Adding attributes after object creation
    class Person:
        def __init__(self, name):
            self.name = name

    person = Person("Alice")
    print(f"\nPerson name: {person.name}")

    # You can add new attributes dynamically (though not recommended)
    person.age = 30
    person.city = "New York"
    print(f"{person.name} is {person.age} years old and lives in {person.city}")


    # ============================================================================
    # Example 3: Default attribute values
    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance  # Default value is 0
            self.account_number = self._generate_account_number()

        def _generate_account_number(self):
            import random
            return random.randint(10000000, 99999999)

    account1 = BankAccount("John Doe", 1000)
    account2 = BankAccount("Jane Smith")  # Uses default balance of 0

    print(f"\n{account1.owner}'s account #{account1.account_number}: ${account1.balance}")
    print(f"{account2.owner}'s account #{account2.account_number}: ${account2.balance}")


    # ============================================================================
    # Example 4: Multiple types of attributes
    class Student:
        def __init__(self, name, student_id):
            self.name = name              # String
            self.student_id = student_id  # Integer
            self.grades = []              # List (mutable)
            self.enrolled = True          # Boolean
            self.gpa = 0.0                # Float

    student = Student("Emma Wilson", 12345)
    student.grades = [95, 88, 92, 90]
    print(f"\n{student.name} (ID: {student.student_id})")
    print(f"Grades: {student.grades}")
    print(f"Enrolled: {student.enrolled}")


    # Key Takeaways:
    # 1. Attributes are defined in __init__ method using self.attribute_name
    # 2. Each object has its own copy of instance attributes
    # 3. Attributes can be any data type (string, int, list, etc.)
    # 4. You can access and modify attributes using dot notation
    # 5. Default values can be provided in __init__ parameters
