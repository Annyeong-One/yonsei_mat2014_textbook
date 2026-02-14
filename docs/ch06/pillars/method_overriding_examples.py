"""
Example 02: Method Overriding

Method overriding allows a child class to provide a specific implementation
of a method that is already defined in its parent class.
"""

class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        return 0  # Default implementation
    
    def perimeter(self):
        return 0  # Default implementation
    
    def describe(self):
        return f"This is a {self.name}"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    # Override area method
    def area(self):
        return self.width * self.height
    
    # Override perimeter method
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    # Override describe method
    def describe(self):
        # Call parent's describe and add more info
        parent_desc = super().describe()
        return f"{parent_desc} with width {self.width} and height {self.height}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    # Override area method
    def area(self):
        return 3.14159 * self.radius ** 2
    
    # Override perimeter method (circumference)
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
    # Override describe method
    def describe(self):
        return f"{super().describe()} with radius {self.radius}"


class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    # Override area method
    def area(self):
        return 0.5 * self.base * self.height
    
    # Override perimeter method
    def perimeter(self):
        return self.side1 + self.side2 + self.side3


# Testing method overriding
if __name__ == "__main__":
    print("=" * 60)
    print("METHOD OVERRIDING DEMO")
    print("=" * 60)
    
    # Create different shapes
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Triangle(6, 4, 5, 5, 6)
    ]
    
    # Process each shape
    for shape in shapes:
        print(f"\n{shape.describe()}")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")
    
    # Demonstrate that the same method name gives different results
    print("\n" + "=" * 60)
    print("SAME METHOD, DIFFERENT BEHAVIOR")
    print("=" * 60)
    
    rect = Rectangle(4, 5)
    circ = Circle(3)
    
    print(f"\nrect.area() = {rect.area()}")
    print(f"circ.area() = {circ.area():.2f}")
    print("\nSame method name 'area()', but different calculations!")

"""
KEY TAKEAWAYS:
1. Child classes can override parent methods to provide specific behavior
2. Use super() to call the parent's version of the method if needed
3. Method overriding is the foundation of polymorphism
4. The overridden method must have the same name as the parent's method
5. You can completely replace or extend the parent's functionality
"""
