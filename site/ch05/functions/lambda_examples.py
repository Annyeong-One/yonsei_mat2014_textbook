"""
Lambda Functions - Practical Examples
This file contains various practical examples of lambda functions in Python.
"""

if __name__ == "__main__":

    print("=" * 60)
    print("LAMBDA FUNCTIONS - EXAMPLES")
    print("=" * 60)

    # ============================================================================
    # EXAMPLE 1: Basic Lambda Functions
    # ============================================================================
    print("\n1. BASIC LAMBDA FUNCTIONS")
    print("-" * 60)

    # Simple lambda functions
    double = lambda x: x * 2
    print(f"Double of 5: {double(5)}")

    cube = lambda x: x ** 3
    print(f"Cube of 3: {cube(3)}")

    # Multiple parameters
    add = lambda a, b: a + b
    print(f"Sum of 10 and 15: {add(10, 15)}")

    max_of_two = lambda a, b: a if a > b else b
    print(f"Maximum of 7 and 12: {max_of_two(7, 12)}")

    # ============================================================================
    # EXAMPLE 2: Lambda with map()
    # ============================================================================
    print("\n2. LAMBDA WITH MAP()")
    print("-" * 60)

    numbers = [1, 2, 3, 4, 5]
    print(f"Original list: {numbers}")

    # Square all numbers
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"Squared: {squared}")

    # Convert Celsius to Fahrenheit
    celsius_temps = [0, 10, 20, 30, 40]
    fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
    print(f"Celsius: {celsius_temps}")
    print(f"Fahrenheit: {fahrenheit}")

    # String manipulation
    words = ["hello", "world", "python", "lambda"]
    uppercase = list(map(lambda s: s.upper(), words))
    print(f"Original: {words}")
    print(f"Uppercase: {uppercase}")

    # ============================================================================
    # EXAMPLE 3: Lambda with filter()
    # ============================================================================
    print("\n3. LAMBDA WITH FILTER()")
    print("-" * 60)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original list: {numbers}")

    # Filter even numbers
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")

    # Filter odd numbers
    odds = list(filter(lambda x: x % 2 != 0, numbers))
    print(f"Odd numbers: {odds}")

    # Filter numbers greater than 5
    greater_than_5 = list(filter(lambda x: x > 5, numbers))
    print(f"Greater than 5: {greater_than_5}")

    # Filter strings by length
    words = ["cat", "elephant", "dog", "hippopotamus", "bird"]
    long_words = list(filter(lambda w: len(w) > 5, words))
    print(f"\nWords: {words}")
    print(f"Words longer than 5 chars: {long_words}")

    # ============================================================================
    # EXAMPLE 4: Lambda with sorted()
    # ============================================================================
    print("\n4. LAMBDA WITH SORTED()")
    print("-" * 60)

    # Sort by string length
    words = ["python", "is", "awesome", "programming", "fun"]
    print(f"Original: {words}")
    sorted_by_length = sorted(words, key=lambda w: len(w))
    print(f"Sorted by length: {sorted_by_length}")

    # Sort list of tuples
    students = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 78),
        ("Diana", 95)
    ]
    print(f"\nStudents (name, grade): {students}")

    sorted_by_grade = sorted(students, key=lambda student: student[1])
    print(f"Sorted by grade: {sorted_by_grade}")

    sorted_by_name = sorted(students, key=lambda student: student[0])
    print(f"Sorted by name: {sorted_by_name}")

    # Sort dictionaries
    products = [
        {"name": "Laptop", "price": 999},
        {"name": "Mouse", "price": 25},
        {"name": "Keyboard", "price": 75},
        {"name": "Monitor", "price": 300}
    ]
    print(f"\nProducts: {products}")
    sorted_by_price = sorted(products, key=lambda p: p["price"])
    print(f"Sorted by price: {sorted_by_price}")

    # ============================================================================
    # EXAMPLE 5: Lambda with reduce()
    # ============================================================================
    print("\n5. LAMBDA WITH REDUCE()")
    print("-" * 60)

    from functools import reduce

    numbers = [1, 2, 3, 4, 5]
    print(f"Numbers: {numbers}")

    # Calculate product of all numbers
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product: {product}")

    # Calculate sum
    sum_result = reduce(lambda x, y: x + y, numbers)
    print(f"Sum: {sum_result}")

    # Find maximum
    max_value = reduce(lambda x, y: x if x > y else y, numbers)
    print(f"Maximum: {max_value}")

    # Concatenate strings
    words = ["Python", " is", " awesome", "!"]
    sentence = reduce(lambda x, y: x + y, words)
    print(f"\nWords: {words}")
    print(f"Concatenated: {sentence}")

    # ============================================================================
    # EXAMPLE 6: Nested Lambdas and Complex Operations
    # ============================================================================
    print("\n6. NESTED LAMBDAS AND COMPLEX OPERATIONS")
    print("-" * 60)

    # Lambda that returns another lambda
    multiply_by = lambda x: lambda y: x * y
    times_2 = multiply_by(2)
    times_5 = multiply_by(5)

    print(f"5 * 2 = {times_2(5)}")
    print(f"5 * 5 = {times_5(5)}")

    # Conditional lambda
    check_age = lambda age: "Adult" if age >= 18 else "Minor"
    print(f"\nAge 25: {check_age(25)}")
    print(f"Age 15: {check_age(15)}")

    # Multiple conditions
    grade_letter = lambda score: 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'
    print(f"\nScore 95: {grade_letter(95)}")
    print(f"Score 83: {grade_letter(83)}")
    print(f"Score 55: {grade_letter(55)}")

    # ============================================================================
    # EXAMPLE 7: Real-World Scenarios
    # ============================================================================
    print("\n7. REAL-WORLD SCENARIOS")
    print("-" * 60)

    # Data cleaning
    data = ["  hello  ", "  WORLD  ", "  Python  "]
    cleaned = list(map(lambda s: s.strip().lower(), data))
    print(f"Original data: {data}")
    print(f"Cleaned data: {cleaned}")

    # Extract specific fields
    users = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "London"},
        {"name": "Charlie", "age": 35, "city": "Paris"}
    ]
    names = list(map(lambda user: user["name"], users))
    print(f"\nUser names: {names}")

    # Filter valid emails (simple check)
    emails = ["user@example.com", "invalid-email", "another@test.com", "bad@", "good@mail.org"]
    valid_emails = list(filter(lambda email: "@" in email and "." in email, emails))
    print(f"\nEmails: {emails}")
    print(f"Valid emails: {valid_emails}")

    # Calculate discounted prices
    prices = [100, 250, 50, 399, 75]
    discount_rate = 0.20
    discounted = list(map(lambda price: price * (1 - discount_rate), prices))
    print(f"\nOriginal prices: {prices}")
    print(f"Discounted prices (20% off): {discounted}")

    print("\n" + "=" * 60)
    print("END OF EXAMPLES")
    print("=" * 60)
