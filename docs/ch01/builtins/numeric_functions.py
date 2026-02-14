"""
03_numeric_functions.py - Numeric Built-in Functions
abs(), round(), pow(), min(), max(), sum(), divmod()
"""

print("=" * 70)
print("NUMERIC BUILT-IN FUNCTIONS")
print("=" * 70)

# abs() - Absolute value
print("\n1. abs() - Absolute Value")
print(f"abs(-10) = {abs(-10)}")
print(f"abs(3.14) = {abs(3.14)}")
print(f"abs(-3.14) = {abs(-3.14)}")

# round() - Round to nearest integer or decimal places
print("\n2. round() - Rounding")
print(f"round(3.7) = {round(3.7)}")          # 4
print(f"round(3.14159, 2) = {round(3.14159, 2)}")  # 3.14
print(f"round(2.5) = {round(2.5)}")          # 2 (banker's rounding)

# pow() - Power (exponentiation)
print("\n3. pow() - Power")
print(f"pow(2, 3) = {pow(2, 3)}")        # 2^3 = 8
print(f"pow(5, 2) = {pow(5, 2)}")        # 5^2 = 25
print(f"2 ** 3 = {2 ** 3}")               # Equivalent to pow()

# min() - Minimum value
print("\n4. min() - Minimum")
print(f"min(5, 2, 8, 1) = {min(5, 2, 8, 1)}")
numbers = [10, 20, 5, 15]
print(f"min({numbers}) = {min(numbers)}")

# max() - Maximum value
print("\n5. max() - Maximum")
print(f"max(5, 2, 8, 1) = {max(5, 2, 8, 1)}")
print(f"max({numbers}) = {max(numbers)}")

# sum() - Sum of all elements
print("\n6. sum() - Sum")
numbers = [1, 2, 3, 4, 5]
print(f"sum({numbers}) = {sum(numbers)}")
print(f"sum({numbers}, 10) = {sum(numbers, 10)}")  # Start from 10

# divmod() - Division and remainder
print("\n7. divmod() - Quotient and Remainder")
result = divmod(17, 5)
print(f"divmod(17, 5) = {result}")  # (3, 2): 17/5 = 3 remainder 2
quotient, remainder = divmod(17, 5)
print(f"17 ÷ 5 = {quotient} remainder {remainder}")

print("\n" + "=" * 70)
print("PRACTICAL EXAMPLES")
print("=" * 70)

# Distance calculation
print("\nExample: Calculate distance from origin")
x, y = 3, 4
distance = pow(pow(x, 2) + pow(y, 2), 0.5)  # sqrt(x^2 + y^2)
print(f"Distance from (0,0) to ({x},{y}): {distance}")

# Grade calculation
print("\nExample: Calculate average grade")
grades = [85, 92, 78, 95, 88]
average = sum(grades) / len(grades)
print(f"Grades: {grades}")
print(f"Average: {round(average, 2)}")
print(f"Highest: {max(grades)}, Lowest: {min(grades)}")

print("\nSee exercises.py for practice!")
