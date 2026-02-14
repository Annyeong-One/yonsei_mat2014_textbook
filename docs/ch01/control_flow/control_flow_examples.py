"""
Python Control Flow - Examples
Run this file to see conditional statements in action!
"""

print("=" * 60)
print("EXAMPLE 1: Simple if Statement")
print("=" * 60)

age = 25
print(f"Age: {age}")

if age >= 18:
    print("You are an adult")
    print("You can vote")

print("This always executes (outside if block)")
print()

print("=" * 60)
print("EXAMPLE 2: if-else Statement")
print("=" * 60)

temperature = 15
print(f"Temperature: {temperature}°C")

if temperature > 20:
    print("It's warm outside")
else:
    print("It's cool outside")
print()

print("=" * 60)
print("EXAMPLE 3: if-elif-else for Multiple Conditions")
print("=" * 60)

score = 85
print(f"Score: {score}")

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
print()

print("=" * 60)
print("EXAMPLE 4: Even or Odd Number")
print("=" * 60)

number = 17
print(f"Number: {number}")

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
print()

print("=" * 60)
print("EXAMPLE 5: Nested Conditionals")
print("=" * 60)

age = 22
has_license = True

print(f"Age: {age}")
print(f"Has license: {has_license}")

if age >= 18:
    print("Age requirement met")
    if has_license:
        print("✓ You can drive!")
    else:
        print("✗ You need to get a driver's license")
else:
    print("✗ You must be 18 or older to drive")
print()

print("=" * 60)
print("EXAMPLE 6: Membership Testing")
print("=" * 60)

allowed_users = ["alice", "bob", "charlie"]
username = "bob"

print(f"Username: {username}")
print(f"Allowed users: {allowed_users}")

if username in allowed_users:
    print(f"✓ Welcome, {username}!")
else:
    print(f"✗ Access denied for {username}")
print()

print("=" * 60)
print("EXAMPLE 7: Range Checking")
print("=" * 60)

temperature = 22
print(f"Temperature: {temperature}°C")

if temperature < 0:
    print("🥶 Freezing!")
elif 0 <= temperature < 10:
    print("❄️ Very cold")
elif 10 <= temperature < 20:
    print("🌡️ Cool")
elif 20 <= temperature < 30:
    print("😊 Comfortable")
else:
    print("🔥 Hot!")
print()

print("=" * 60)
print("EXAMPLE 8: Logical Operators in Conditions")
print("=" * 60)

is_weekend = True
is_sunny = True
has_money = False

print(f"Is weekend: {is_weekend}")
print(f"Is sunny: {is_sunny}")
print(f"Has money: {has_money}")

# AND operator
if is_weekend and is_sunny:
    print("✓ Perfect day for outdoor activities!")

# OR operator
if has_money or is_weekend:
    print("✓ You can enjoy some free time")

# NOT operator
if not has_money:
    print("✗ Budget day - enjoy free activities")
print()

print("=" * 60)
print("EXAMPLE 9: Ternary Operator")
print("=" * 60)

age = 16
# Ternary: value_if_true if condition else value_if_false
status = "adult" if age >= 18 else "minor"

print(f"Age: {age}")
print(f"Status: {status}")

# Another example
number = 7
parity = "even" if number % 2 == 0 else "odd"
print(f"Number {number} is {parity}")
print()

print("=" * 60)
print("EXAMPLE 10: Truthy and Falsy Values")
print("=" * 60)

# Empty string is falsy
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name is empty")

# Empty list is falsy
items = []
if items:
    print(f"Items: {items}")
else:
    print("No items in the list")

# Zero is falsy
count = 0
if count:
    print(f"Count: {count}")
else:
    print("Count is zero")

# None is falsy
result = None
if result:
    print(f"Result: {result}")
else:
    print("No result available")
print()

print("=" * 60)
print("EXAMPLE 11: Multiple Conditions with 'and'")
print("=" * 60)

username = "admin"
password = "secure123"

print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")

if username == "admin" and password == "secure123":
    print("✓ Login successful")
else:
    print("✗ Invalid credentials")
print()

print("=" * 60)
print("EXAMPLE 12: Multiple Conditions with 'or'")
print("=" * 60)

payment_method = "credit_card"

print(f"Payment method: {payment_method}")

if payment_method == "credit_card" or payment_method == "debit_card" or payment_method == "paypal":
    print("✓ Payment method accepted")
else:
    print("✗ Invalid payment method")

# Better way using 'in'
if payment_method in ["credit_card", "debit_card", "paypal"]:
    print("✓ Payment method accepted (using 'in')")
print()

print("=" * 60)
print("EXAMPLE 13: Guard Clauses Pattern")
print("=" * 60)

def validate_age(age):
    """Validate age with guard clauses"""
    
    # Guard clause 1
    if age < 0:
        return "Invalid: Age cannot be negative"
    
    # Guard clause 2
    if age > 150:
        return "Invalid: Age too high"
    
    # Main logic
    if age < 18:
        return "Minor"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

test_ages = [-5, 15, 25, 70, 200]
for age in test_ages:
    result = validate_age(age)
    print(f"Age {age}: {result}")
print()

print("=" * 60)
print("EXAMPLE 14: Comparing None")
print("=" * 60)

value = None

# Recommended way
if value is None:
    print("Value is None (using 'is')")

# Also works but not recommended
if value == None:
    print("Value is None (using '==')")

# Check if NOT None
value = 42
if value is not None:
    print(f"Value is not None: {value}")
print()

print("=" * 60)
print("EXAMPLE 15: Practical - BMI Calculator")
print("=" * 60)

weight = 70  # kg
height = 1.75  # meters
bmi = weight / (height ** 2)

print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")
print()

print("=" * 60)
print("EXAMPLE 16: Practical - Discount Calculator")
print("=" * 60)

price = 100
is_member = True
quantity = 5

print(f"Original price: ${price}")
print(f"Is member: {is_member}")
print(f"Quantity: {quantity}")

discount = 0

if is_member:
    discount += 10  # 10% member discount
    print("Applied 10% member discount")

if quantity >= 5:
    discount += 5  # 5% bulk discount
    print("Applied 5% bulk discount")

final_price = price * (1 - discount / 100)
print(f"Total discount: {discount}%")
print(f"Final price: ${final_price:.2f}")
print()

print("=" * 60)
print("EXAMPLE 17: Practical - Grade with Feedback")
print("=" * 60)

score = 88
print(f"Score: {score}")

if score >= 90:
    grade = "A"
    feedback = "Excellent work!"
elif score >= 80:
    grade = "B"
    feedback = "Good job!"
elif score >= 70:
    grade = "C"
    feedback = "Satisfactory"
elif score >= 60:
    grade = "D"
    feedback = "Needs improvement"
else:
    grade = "F"
    feedback = "Please see instructor"

print(f"Grade: {grade}")
print(f"Feedback: {feedback}")
print()

print("=" * 60)
print("EXAMPLE 18: Practical - Time-based Greeting")
print("=" * 60)

import datetime
hour = datetime.datetime.now().hour

print(f"Current hour: {hour}")

if hour < 6:
    greeting = "Good night"
elif hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
elif hour < 22:
    greeting = "Good evening"
else:
    greeting = "Good night"

print(greeting)
print()

print("=" * 60)
print("EXAMPLE 19: Practical - Password Strength Checker")
print("=" * 60)

password = "Secure123!"

print(f"Password: {'*' * len(password)}")

has_length = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)

print(f"Length >= 8: {has_length}")
print(f"Has uppercase: {has_upper}")
print(f"Has lowercase: {has_lower}")
print(f"Has digit: {has_digit}")
print(f"Has special char: {has_special}")

if has_length and has_upper and has_lower and has_digit and has_special:
    strength = "Strong"
elif has_length and (has_upper or has_lower) and has_digit:
    strength = "Medium"
else:
    strength = "Weak"

print(f"Password strength: {strength}")
print()

print("=" * 60)
print("EXAMPLE 20: Practical - Shipping Cost Calculator")
print("=" * 60)

weight = 2.5  # kg
distance = 150  # km
is_express = False

print(f"Weight: {weight} kg")
print(f"Distance: {distance} km")
print(f"Express shipping: {is_express}")

# Base cost
if weight <= 1:
    cost = 5
elif weight <= 5:
    cost = 10
elif weight <= 10:
    cost = 15
else:
    cost = 20

# Distance surcharge
if distance > 100:
    cost += 5
    print("Added distance surcharge: $5")

# Express surcharge
if is_express:
    cost *= 1.5
    print("Applied express multiplier: 1.5x")

print(f"Total shipping cost: ${cost:.2f}")
print()

print("=" * 60)
print("All examples completed!")
print("=" * 60)
print()
print("Key Insights:")
print("• if statements execute code conditionally")
print("• elif allows multiple conditions")
print("• else provides a default path")
print("• Nesting is possible but keep it simple")
print("• Use 'and', 'or', 'not' for complex conditions")
print("• Ternary operator for simple one-liners")
print("• Truthy/falsy values simplify checks")
