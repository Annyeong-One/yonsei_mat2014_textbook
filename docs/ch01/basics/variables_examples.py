"""
Python Variables - Examples
Run each section to see how variables work!
"""

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("EXAMPLE 1: Basic Variable Assignment")
    print("=" * 50)

    # Creating different types of variables
    name = "Alice"
    age = 25
    height = 5.6
    is_student = True

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height}")
    print(f"Is Student: {is_student}")
    print()

    print("=" * 50)
    print("EXAMPLE 2: Multiple Assignment")
    print("=" * 50)

    # Assign same value to multiple variables
    x = y = z = 100
    print(f"x = {x}, y = {y}, z = {z}")

    # Assign different values
    a, b, c = 1, 2, 3
    print(f"a = {a}, b = {b}, c = {c}")
    print()

    print("=" * 50)
    print("EXAMPLE 3: Variable Reassignment")
    print("=" * 50)

    counter = 0
    print(f"Initial counter: {counter}")

    counter = 10
    print(f"After reassignment: {counter}")

    counter = counter + 5
    print(f"After adding 5: {counter}")
    print()

    print("=" * 50)
    print("EXAMPLE 4: Swapping Variables")
    print("=" * 50)

    first = "Apple"
    second = "Banana"

    print(f"Before swap - First: {first}, Second: {second}")

    # Pythonic swap
    first, second = second, first

    print(f"After swap - First: {first}, Second: {second}")
    print()

    print("=" * 50)
    print("EXAMPLE 5: Type Checking")
    print("=" * 50)

    integer_var = 42
    float_var = 3.14
    string_var = "Hello"
    boolean_var = True
    list_var = [1, 2, 3]

    print(f"{integer_var} is of type: {type(integer_var)}")
    print(f"{float_var} is of type: {type(float_var)}")
    print(f"{string_var} is of type: {type(string_var)}")
    print(f"{boolean_var} is of type: {type(boolean_var)}")
    print(f"{list_var} is of type: {type(list_var)}")
    print()

    print("=" * 50)
    print("EXAMPLE 6: Variable Naming Conventions")
    print("=" * 50)

    # Snake case (Python standard)
    first_name = "John"
    last_name = "Doe"
    user_age = 30

    print(f"User: {first_name} {last_name}, Age: {user_age}")

    # Constants (uppercase)
    PI = 3.14159
    MAX_CONNECTIONS = 100

    print(f"PI value: {PI}")
    print(f"Max connections: {MAX_CONNECTIONS}")
    print()

    print("=" * 50)
    print("EXAMPLE 7: String Variables and Operations")
    print("=" * 50)

    greeting = "Hello"
    name = "World"

    # String concatenation
    message = greeting + " " + name + "!"
    print(message)

    # String formatting (f-strings)
    formatted_message = f"{greeting} {name}!"
    print(formatted_message)
    print()

    print("=" * 50)
    print("EXAMPLE 8: Numeric Variables and Operations")
    print("=" * 50)

    # Integer variables
    apples = 10
    oranges = 5
    total_fruits = apples + oranges

    print(f"Apples: {apples}")
    print(f"Oranges: {oranges}")
    print(f"Total fruits: {total_fruits}")

    # Float variables
    price = 19.99
    quantity = 3
    total_cost = price * quantity

    print(f"Price per item: ${price}")
    print(f"Quantity: {quantity}")
    print(f"Total cost: ${total_cost:.2f}")
    print()

    print("=" * 50)
    print("EXAMPLE 9: Boolean Variables")
    print("=" * 50)

    is_raining = False
    is_sunny = True
    has_umbrella = True

    print(f"Is it raining? {is_raining}")
    print(f"Is it sunny? {is_sunny}")
    print(f"Do I have an umbrella? {has_umbrella}")

    # Using booleans in conditions
    if is_sunny and not is_raining:
        print("Perfect day for a picnic!")
    print()

    print("=" * 50)
    print("EXAMPLE 10: Dynamic Typing")
    print("=" * 50)

    # Python allows changing variable types
    variable = 10
    print(f"Variable is: {variable}, Type: {type(variable)}")

    variable = "Now I'm a string"
    print(f"Variable is: {variable}, Type: {type(variable)}")

    variable = [1, 2, 3]
    print(f"Variable is: {variable}, Type: {type(variable)}")
    print()

    print("=" * 50)
    print("All examples completed!")
    print("=" * 50)
