"""
Python Data Types - Examples
Run this file to see all data types in action!
"""

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("EXAMPLE 1: Integer (int)")
    print("=" * 50)

    age = 25
    year = 2024
    temperature = -15
    big_number = 1_000_000

    print(f"Age: {age}, Type: {type(age)}")
    print(f"Year: {year}, Type: {type(year)}")
    print(f"Temperature: {temperature}")
    print(f"Big number: {big_number:,}")
    print()

    print("=" * 50)
    print("EXAMPLE 2: Float (float)")
    print("=" * 50)

    price = 19.99
    pi = 3.14159
    scientific = 1.5e3
    small_number = 1.5e-3

    print(f"Price: ${price}")
    print(f"Pi: {pi}")
    print(f"Scientific notation (1.5e3): {scientific}")
    print(f"Small number (1.5e-3): {small_number}")
    print()

    # Float precision example
    result = 0.1 + 0.2
    print(f"0.1 + 0.2 = {result} (precision issue)")
    print(f"Rounded: {round(result, 1)}")
    print()

    print("=" * 50)
    print("EXAMPLE 3: String (str)")
    print("=" * 50)

    name = "Alice"
    greeting = 'Hello'
    multiline = """This is a
    multiline
    string"""

    print(f"Name: {name}")
    print(f"Greeting: {greeting}")
    print(f"Multiline:\n{multiline}")
    print()

    # String operations
    text = "Python Programming"
    print(f"Original: {text}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"Replace: {text.replace('Python', 'Java')}")
    print(f"Split: {text.split()}")
    print(f"Length: {len(text)}")
    print()

    # String slicing
    print(f"First 6 chars: {text[:6]}")
    print(f"Last 11 chars: {text[-11:]}")
    print(f"Every 2nd char: {text[::2]}")
    print()

    print("=" * 50)
    print("EXAMPLE 4: Boolean (bool)")
    print("=" * 50)

    is_python_fun = True
    is_difficult = False

    print(f"Is Python fun? {is_python_fun}")
    print(f"Is it difficult? {is_difficult}")
    print()

    # Boolean operations
    print(f"True AND False: {True and False}")
    print(f"True OR False: {True or False}")
    print(f"NOT True: {not True}")
    print()

    # Comparison operations return booleans
    x = 10
    y = 20
    print(f"{x} > {y}: {x > y}")
    print(f"{x} < {y}: {x < y}")
    print(f"{x} == {y}: {x == y}")
    print(f"{x} != {y}: {x != y}")
    print()

    # Truthy and Falsy
    print(f"bool(0): {bool(0)}")
    print(f"bool(''): {bool('')}")
    print(f"bool([]): {bool([])}")
    print(f"bool(42): {bool(42)}")
    print(f"bool('text'): {bool('text')}")
    print()

    print("=" * 50)
    print("EXAMPLE 5: List (list)")
    print("=" * 50)

    fruits = ["apple", "banana", "orange"]
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]

    print(f"Fruits: {fruits}")
    print(f"Numbers: {numbers}")
    print(f"Mixed types: {mixed}")
    print()

    # List operations
    fruits.append("grape")
    print(f"After append: {fruits}")

    fruits.insert(1, "mango")
    print(f"After insert: {fruits}")

    fruits.remove("banana")
    print(f"After remove: {fruits}")

    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    print(f"First 2 fruits: {fruits[:2]}")
    print()

    print("=" * 50)
    print("EXAMPLE 6: Tuple (tuple)")
    print("=" * 50)

    coordinates = (10, 20)
    colors = ("red", "green", "blue")
    single = (42,)

    print(f"Coordinates: {coordinates}")
    print(f"Colors: {colors}")
    print(f"Single item tuple: {single}")
    print()

    # Tuple unpacking
    x, y = coordinates
    print(f"x = {x}, y = {y}")
    print()

    # Tuples are immutable
    print("Trying to modify a tuple would cause an error:")
    print("# coordinates[0] = 15  # TypeError!")
    print()

    print("=" * 50)
    print("EXAMPLE 7: Dictionary (dict)")
    print("=" * 50)

    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "email": "alice@email.com"
    }

    print(f"Person dictionary: {person}")
    print(f"Name: {person['name']}")
    print(f"Age: {person.get('age')}")
    print()

    # Modifying dictionary
    person["age"] = 31
    person["country"] = "USA"
    print(f"After modifications: {person}")
    print()

    # Dictionary methods
    print(f"Keys: {list(person.keys())}")
    print(f"Values: {list(person.values())}")
    print(f"Items: {list(person.items())}")
    print()

    print("=" * 50)
    print("EXAMPLE 8: Set (set)")
    print("=" * 50)

    numbers = {1, 2, 3, 4, 5}
    letters = {"a", "b", "c"}

    print(f"Numbers set: {numbers}")
    print(f"Letters set: {letters}")
    print()

    # Sets automatically remove duplicates
    duplicates = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
    print(f"Set with duplicates removed: {duplicates}")
    print()

    # Set operations
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union (|): {set1 | set2}")
    print(f"Intersection (&): {set1 & set2}")
    print(f"Difference (-): {set1 - set2}")
    print()

    print("=" * 50)
    print("EXAMPLE 9: None Type")
    print("=" * 50)

    result = None
    print(f"Result: {result}")
    print(f"Type: {type(result)}")
    print(f"Is None? {result is None}")
    print()

    # Common use case
    def find_user(user_id):
        # Simulate database lookup
        if user_id == 1:
            return {"name": "Alice", "age": 30}
        else:
            return None

    user = find_user(1)
    print(f"User found: {user}")

    user = find_user(999)
    print(f"User not found: {user}")
    print()

    print("=" * 50)
    print("EXAMPLE 10: Type Conversion")
    print("=" * 50)

    # String to number
    str_num = "42"
    int_num = int(str_num)
    float_num = float(str_num)

    print(f"String '{str_num}' to int: {int_num}")
    print(f"String '{str_num}' to float: {float_num}")
    print()

    # Number to string
    num = 100
    str_from_num = str(num)
    print(f"Number {num} to string: '{str_from_num}'")
    print()

    # List conversions
    text = "hello"
    text_list = list(text)
    print(f"String to list: {text_list}")

    tuple_data = (1, 2, 3)
    list_data = list(tuple_data)
    print(f"Tuple to list: {list_data}")
    print()

    # Boolean conversions
    print(f"int(True): {int(True)}")
    print(f"int(False): {int(False)}")
    print(f"bool(1): {bool(1)}")
    print(f"bool(0): {bool(0)}")
    print()

    print("=" * 50)
    print("EXAMPLE 11: Type Checking")
    print("=" * 50)

    variables = [
        42,
        3.14,
        "hello",
        True,
        [1, 2, 3],
        (1, 2, 3),
        {"key": "value"},
        {1, 2, 3},
        None
    ]

    print("Type checking with type():")
    for var in variables:
        print(f"{str(var):20} -> {type(var)}")
    print()

    print("Type checking with isinstance():")
    x = 42
    print(f"isinstance({x}, int): {isinstance(x, int)}")
    print(f"isinstance({x}, float): {isinstance(x, float)}")
    print(f"isinstance({x}, (int, float)): {isinstance(x, (int, float))}")
    print()

    print("=" * 50)
    print("EXAMPLE 12: Practical Examples")
    print("=" * 50)

    # Shopping cart example using different data types
    cart = {
        "items": [
            {"name": "Apple", "price": 1.50, "quantity": 4},
            {"name": "Bread", "price": 2.99, "quantity": 2},
            {"name": "Milk", "price": 3.49, "quantity": 1}
        ],
        "customer": "John Doe",
        "is_member": True
    }

    print("Shopping Cart:")
    print(f"Customer: {cart['customer']}")
    print(f"Member: {cart['is_member']}")
    print("\nItems:")

    total = 0.0
    for item in cart["items"]:
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(f"  {item['name']}: ${item['price']} x {item['quantity']} = ${item_total:.2f}")

    discount = 0.10 if cart["is_member"] else 0.0
    final_total = total * (1 - discount)

    print(f"\nSubtotal: ${total:.2f}")
    if discount > 0:
        print(f"Member discount: {discount * 100}%")
    print(f"Total: ${final_total:.2f}")
    print()

    print("=" * 50)
    print("All examples completed!")
    print("=" * 50)
