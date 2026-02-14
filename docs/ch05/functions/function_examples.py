"""
Python Functions - Examples
"""

print("="*60)
print("EXAMPLE 1: Basic Function")
print("="*60)
def greet():
    print("Hello, World!")
greet()
print()

print("="*60)
print("EXAMPLE 2: Function with Parameter")
print("="*60)
def greet_person(name):
    print(f"Hello, {name}!")
greet_person("Alice")
print()

print("="*60)
print("EXAMPLE 3: Function with Return")
print("="*60)
def add(a, b):
    return a + b
result = add(5, 3)
print(f"5 + 3 = {result}")
print()

print("="*60)
print("EXAMPLE 4: Multiple Parameters")
print("="*60)
def rectangle_area(length, width):
    return length * width
area = rectangle_area(5, 3)
print(f"Area: {area}")
print()

print("="*60)
print("EXAMPLE 5: Multiple Return Values")
print("="*60)
def get_min_max(numbers):
    return min(numbers), max(numbers)
minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")
print()

print("="*60)
print("EXAMPLE 6: Default Parameters")
print("="*60)
def power(base, exponent=2):
    return base ** exponent
print(f"5^2 = {power(5)}")
print(f"5^3 = {power(5, 3)}")
print()

print("="*60)
print("EXAMPLE 7: Keyword Arguments")
print("="*60)
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")
describe_pet(animal="dog", name="Buddy")
describe_pet(name="Whiskers", animal="cat")
print()

print("="*60)
print("EXAMPLE 8: Local vs Global Scope")
print("="*60)
x = 10  # Global
def show_scope():
    y = 20  # Local
    print(f"Inside function - x: {x}, y: {y}")
show_scope()
print(f"Outside function - x: {x}")
print()

print("="*60)
print("EXAMPLE 9: Variable-Length Arguments (*args)")
print("="*60)
def sum_all(*numbers):
    return sum(numbers)
print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")
print()

print("="*60)
print("EXAMPLE 10: Keyword Variable Arguments (**kwargs)")
print("="*60)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="NYC")
print()

print("="*60)
print("EXAMPLE 11: Lambda Function")
print("="*60)
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")
add = lambda x, y: x + y
print(f"3 + 4 = {add(3, 4)}")
print()

print("="*60)
print("EXAMPLE 12: Function with Docstring")
print("="*60)
def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)"""
    return weight / (height ** 2)
print(f"BMI: {calculate_bmi(70, 1.75):.2f}")
print(f"Docstring: {calculate_bmi.__doc__}")
print()

print("="*60)
print("EXAMPLE 13: Factorial (Recursive)")
print("="*60)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(f"5! = {factorial(5)}")
print()

print("="*60)
print("EXAMPLE 14: Is Even (Boolean Return)")
print("="*60)
def is_even(num):
    return num % 2 == 0
print(f"4 is even: {is_even(4)}")
print(f"7 is even: {is_even(7)}")
print()

print("="*60)
print("EXAMPLE 15: Temperature Converter")
print("="*60)
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print()

print("All examples completed!")
