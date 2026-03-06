"""
Example 01: Basic Inheritance

This example demonstrates the fundamental concept of inheritance,
where a child class inherits attributes and methods from a parent class.
"""

# Parent Class (also called Base Class or Superclass)

# =============================================================================
# Definitions
# =============================================================================

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        return f"{self.name} is eating."
    
    def sleep(self):
        return f"{self.name} is sleeping."
    
    def info(self):
        return f"{self.name} is a {self.species}."


# Child Class (also called Derived Class or Subclass)
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Dog")
        self.breed = breed
    
    # Dog-specific method
    def bark(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    # Cat-specific method
    def meow(self):
        return f"{self.name} says Meow!"


# Testing the classes

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("BASIC INHERITANCE DEMO")
    print("=" * 50)
    
    # Create a Dog object
    dog = Dog("Buddy", "Golden Retriever")
    print(f"\nDog Name: {dog.name}")
    print(f"Breed: {dog.breed}")
    print(dog.info())  # Inherited method
    print(dog.eat())   # Inherited method
    print(dog.bark())  # Dog-specific method
    
    # Create a Cat object
    cat = Cat("Whiskers", "Orange")
    print(f"\nCat Name: {cat.name}")
    print(f"Color: {cat.color}")
    print(cat.info())  # Inherited method
    print(cat.sleep()) # Inherited method
    print(cat.meow())  # Cat-specific method
    
    # Check inheritance
    print("\n" + "=" * 50)
    print("INHERITANCE VERIFICATION")
    print("=" * 50)
    print(f"Is dog an Animal? {isinstance(dog, Animal)}")
    print(f"Is dog a Dog? {isinstance(dog, Dog)}")
    print(f"Is cat an Animal? {isinstance(cat, Animal)}")
    print(f"Is dog a Cat? {isinstance(dog, Cat)}")

"""
KEY TAKEAWAYS:
1. Child classes inherit all attributes and methods from parent class
2. Use super() to call parent class constructor
3. Child classes can have their own unique methods
4. isinstance() checks if an object is an instance of a class
5. A child class object is also an instance of its parent class
"""
