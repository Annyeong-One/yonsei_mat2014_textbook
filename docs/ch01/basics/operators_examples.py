"""
Python Operators - Examples
Run this file to see all operators in action!
"""

print("=" * 50)
print("EXAMPLE 1: Arithmetic Operators")
print("=" * 50)

a = 15
b = 4

print(f"a = {a}, b = {b}\n")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")
print()

print("=" * 50)
print("EXAMPLE 2: Division Types")
print("=" * 50)

print(f"10 / 3 = {10 / 3} (Regular division - always float)")
print(f"10 // 3 = {10 // 3} (Floor division - rounds down)")
print(f"10 % 3 = {10 % 3} (Modulus - remainder)")
print()

print(f"9 / 3 = {9 / 3} (Still returns float)")
print(f"9 // 3 = {9 // 3}")
print(f"9 % 3 = {9 % 3} (No remainder)")
print()

print("=" * 50)
print("EXAMPLE 3: Assignment Operators")
print("=" * 50)

x = 10
print(f"Initial value: x = {x}")

x += 5
print(f"After x += 5: x = {x}")

x -= 3
print(f"After x -= 3: x = {x}")

x *= 2
print(f"After x *= 2: x = {x}")

x /= 4
print(f"After x /= 4: x = {x}")

x **= 2
print(f"After x **= 2: x = {x}")
print()

print("=" * 50)
print("EXAMPLE 4: Comparison Operators")
print("=" * 50)

x = 10
y = 20

print(f"x = {x}, y = {y}\n")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= 10: {x >= 10}")
print(f"y <= 20: {y <= 20}")
print()

# Chaining comparisons
z = 15
print(f"z = {z}")
print(f"10 < z < 20: {10 < z < 20}")
print(f"10 < z < 15: {10 < z < 15}")
print()

print("=" * 50)
print("EXAMPLE 5: Logical Operators")
print("=" * 50)

age = 25
has_license = True
has_insurance = False

print(f"age = {age}")
print(f"has_license = {has_license}")
print(f"has_insurance = {has_insurance}\n")

# AND operator
can_drive = age >= 18 and has_license
print(f"Can drive (age >= 18 AND has_license): {can_drive}")

# OR operator
needs_requirements = not has_license or not has_insurance
print(f"Needs requirements (NOT has_license OR NOT has_insurance): {needs_requirements}")

# Complex condition
is_legal_driver = age >= 18 and has_license and has_insurance
print(f"Is legal driver (all conditions): {is_legal_driver}")
print()

print("=" * 50)
print("EXAMPLE 6: Logical Operator Truth Tables")
print("=" * 50)

print("AND Truth Table:")
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"False and False = {False and False}")
print()

print("OR Truth Table:")
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")
print()

print("NOT Truth Table:")
print(f"not True = {not True}")
print(f"not False = {not False}")
print()

print("=" * 50)
print("EXAMPLE 7: Membership Operators")
print("=" * 50)

# String membership
text = "Python Programming"
print(f"Text: '{text}'")
print(f"'Python' in text: {'Python' in text}")
print(f"'Java' in text: {'Java' in text}")
print(f"'Java' not in text: {'Java' not in text}")
print()

# List membership
fruits = ['apple', 'banana', 'orange', 'grape']
print(f"Fruits: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")
print(f"'mango' not in fruits: {'mango' not in fruits}")
print()

# Dictionary membership
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(f"Person: {person}")
print(f"'name' in person: {'name' in person}")
print(f"'Alice' in person: {'Alice' in person} (checks keys)")
print(f"'Alice' in person.values(): {'Alice' in person.values()}")
print()

print("=" * 50)
print("EXAMPLE 8: Identity Operators")
print("=" * 50)

# Lists
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x = {x}")
print(f"y = {y}")
print(f"z = x (z points to same object as x)")
print()

print(f"x == y: {x == y} (same values)")
print(f"x is y: {x is y} (different objects)")
print(f"x is z: {x is z} (same object)")
print(f"x is not y: {x is not y}")
print()

# None comparison
value = None
print(f"value = {value}")
print(f"value is None: {value is None} (recommended)")
print(f"value == None: {value == None} (works but use 'is')")
print()

print("=" * 50)
print("EXAMPLE 9: Bitwise Operators")
print("=" * 50)

a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(f"a = {a} (Binary: {bin(a)})")
print(f"b = {b} (Binary: {bin(b)})")
print()

print(f"a & b (AND): {a & b} (Binary: {bin(a & b)})")
print(f"a | b (OR): {a | b} (Binary: {bin(a | b)})")
print(f"a ^ b (XOR): {a ^ b} (Binary: {bin(a ^ b)})")
print(f"~a (NOT): {~a}")
print(f"a << 1 (Left shift): {a << 1} (Binary: {bin(a << 1)})")
print(f"a >> 1 (Right shift): {a >> 1} (Binary: {bin(a >> 1)})")
print()

print("=" * 50)
print("EXAMPLE 10: Operator Precedence")
print("=" * 50)

# Without parentheses
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result} (multiplication first)")

# With parentheses
result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result} (addition first)")
print()

# Complex expression
result = 10 + 5 * 2 ** 3
print(f"10 + 5 * 2 ** 3 = {result}")
print("Evaluation order: 2**3=8, then 5*8=40, then 10+40=50")
print()

# With parentheses for clarity
result = 10 + (5 * (2 ** 3))
print(f"10 + (5 * (2 ** 3)) = {result} (same result, clearer)")
print()

print("=" * 50)
print("EXAMPLE 11: Practical - Calculate Discount")
print("=" * 50)

original_price = 100
discount_percent = 25

discount_amount = original_price * (discount_percent / 100)
final_price = original_price - discount_amount

print(f"Original Price: ${original_price}")
print(f"Discount: {discount_percent}%")
print(f"Discount Amount: ${discount_amount}")
print(f"Final Price: ${final_price}")
print()

print("=" * 50)
print("EXAMPLE 12: Practical - Loan Eligibility")
print("=" * 50)

age = 25
annual_income = 50000
credit_score = 720
has_existing_loan = False

# Multiple conditions
is_age_eligible = age >= 21 and age <= 65
is_income_sufficient = annual_income >= 30000
is_credit_good = credit_score >= 650
no_existing_loans = not has_existing_loan

is_eligible = (is_age_eligible and is_income_sufficient and 
               is_credit_good and no_existing_loans)

print(f"Applicant Details:")
print(f"  Age: {age}")
print(f"  Annual Income: ${annual_income}")
print(f"  Credit Score: {credit_score}")
print(f"  Has Existing Loan: {has_existing_loan}")
print()

print(f"Eligibility Checks:")
print(f"  Age Eligible (21-65): {is_age_eligible}")
print(f"  Income Sufficient (>= $30,000): {is_income_sufficient}")
print(f"  Credit Score Good (>= 650): {is_credit_good}")
print(f"  No Existing Loans: {no_existing_loans}")
print()

print(f"Final Decision: {'APPROVED' if is_eligible else 'DENIED'}")
print()

print("=" * 50)
print("EXAMPLE 13: Practical - Temperature Conversion")
print("=" * 50)

celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")

# Reverse
fahrenheit_input = 77
celsius_result = (fahrenheit_input - 32) * 5/9

print(f"{fahrenheit_input}°F = {celsius_result:.1f}°C")
print()

print("=" * 50)
print("EXAMPLE 14: Practical - Even/Odd Checker")
print("=" * 50)

numbers = [12, 7, 18, 23, 30, 15]
print(f"Numbers: {numbers}\n")

for num in numbers:
    is_even = num % 2 == 0
    result = "even" if is_even else "odd"
    print(f"{num} is {result}")
print()

print("=" * 50)
print("EXAMPLE 15: Practical - Grade Calculator")
print("=" * 50)

score = 85

grade = (
    'A' if score >= 90 else
    'B' if score >= 80 else
    'C' if score >= 70 else
    'D' if score >= 60 else
    'F'
)

passed = score >= 60

print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Passed: {passed}")
print()

print("=" * 50)
print("All examples completed!")
print("=" * 50)
