"""
PYTHON TUPLES - COMPLETE TUTORIAL
==================================

Tuples are immutable, ordered sequences in Python. Once created, their elements
cannot be modified, making them useful for data that shouldn't change.
"""

# =============================================================================
# 1. CREATING TUPLES
# =============================================================================

# Empty tuple

if __name__ == "__main__":
    empty_tuple = ()
    also_empty = tuple()

    # Tuple with parentheses
    numbers = (1, 2, 3, 4, 5)
    fruits = ("apple", "banana", "cherry")

    # Tuple without parentheses (tuple packing)
    coordinates = 10, 20, 30
    print(f"Coordinates: {coordinates}, type: {type(coordinates)}")

    # Single element tuple (note the comma!)
    single = (5,)      # This is a tuple
    not_tuple = (5)    # This is just an integer in parentheses
    print(f"Single tuple: {single}, type: {type(single)}")
    print(f"Not a tuple: {not_tuple}, type: {type(not_tuple)}")

    # Mixed types
    mixed = (1, "hello", 3.14, True, [1, 2, 3])

    # Using tuple() constructor
    from_list = tuple([1, 2, 3, 4, 5])
    from_string = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')
    from_range = tuple(range(5))  # (0, 1, 2, 3, 4)

    print(f"\nBasic tuples created:")
    print(f"Numbers: {numbers}")
    print(f"Fruits: {fruits}")
    print()

    # =============================================================================
    # 2. ACCESSING ELEMENTS (INDEXING)
    # =============================================================================

    letters = ('a', 'b', 'c', 'd', 'e')

    # Positive indexing
    print("Indexing:")
    print(f"First element: {letters[0]}")    # 'a'
    print(f"Third element: {letters[2]}")    # 'c'

    # Negative indexing
    print(f"Last element: {letters[-1]}")    # 'e'
    print(f"Second to last: {letters[-2]}")  # 'd'
    print()

    # =============================================================================
    # 3. SLICING
    # =============================================================================

    numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    print("Slicing [start:stop:step]:")
    print(f"First 5: {numbers[:5]}")          # (0, 1, 2, 3, 4)
    print(f"Last 5: {numbers[-5:]}")          # (5, 6, 7, 8, 9)
    print(f"Middle: {numbers[3:7]}")          # (3, 4, 5, 6)
    print(f"Every 2nd: {numbers[::2]}")       # (0, 2, 4, 6, 8)
    print(f"Reverse: {numbers[::-1]}")        # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
    print()

    # =============================================================================
    # 4. IMMUTABILITY
    # =============================================================================

    numbers = (1, 2, 3, 4, 5)

    print("Tuples are immutable:")
    try:
        numbers[0] = 10  # This will raise an error
    except TypeError as e:
        print(f"Error: {e}")

    try:
        numbers.append(6)  # Tuples don't have append method
    except AttributeError as e:
        print(f"Error: {e}")

    print()

    # However, if a tuple contains mutable objects, those can be modified
    mutable_content = ([1, 2, 3], [4, 5, 6])
    mutable_content[0].append(4)  # This works!
    print(f"Modified mutable content: {mutable_content}")
    print()

    # =============================================================================
    # 5. TUPLE METHODS
    # =============================================================================

    numbers = (1, 2, 3, 2, 4, 2, 5)

    # count() - counts occurrences
    print(f"Count of 2: {numbers.count(2)}")  # 3

    # index() - finds first index of value
    print(f"First index of 3: {numbers.index(3)}")  # 2

    # You can specify start and end for index
    print(f"Index of 2 after position 2: {numbers.index(2, 2)}")

    # That's it! Tuples only have 2 methods (due to immutability)
    print(f"\nTuple methods: count() and index()")
    print()

    # =============================================================================
    # 6. TUPLE OPERATIONS
    # =============================================================================

    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)

    # Concatenation
    combined = tuple1 + tuple2
    print(f"Concatenation: {combined}")

    # Repetition
    repeated = tuple1 * 3
    print(f"Repetition: {repeated}")

    # Membership testing
    print(f"2 in tuple1: {2 in tuple1}")
    print(f"7 not in tuple1: {7 not in tuple1}")

    # Length
    print(f"Length: {len(tuple1)}")

    # Min, Max, Sum (for numeric tuples)
    numbers = (45, 23, 67, 12, 89, 34)
    print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")

    # Comparing tuples (lexicographic order)
    print(f"(1, 2, 3) < (1, 2, 4): {(1, 2, 3) < (1, 2, 4)}")
    print()

    # =============================================================================
    # 7. TUPLE UNPACKING
    # =============================================================================

    # Basic unpacking
    point = (10, 20)
    x, y = point
    print(f"Unpacked point: x={x}, y={y}")

    # Multiple assignment
    a, b, c = (1, 2, 3)
    print(f"Multiple assignment: a={a}, b={b}, c={c}")

    # Swapping variables (very common use!)
    x, y = 5, 10
    print(f"Before swap: x={x}, y={y}")
    x, y = y, x  # Swap using tuple unpacking
    print(f"After swap: x={x}, y={y}")

    # Extended unpacking with * (Python 3+)
    first, *middle, last = (1, 2, 3, 4, 5)
    print(f"Extended unpacking: first={first}, middle={middle}, last={last}")

    # Unpacking in function returns
    def get_min_max(numbers):
        return min(numbers), max(numbers)  # Returns tuple

    minimum, maximum = get_min_max([1, 2, 3, 4, 5])
    print(f"Function return unpacking: min={minimum}, max={maximum}")

    # Ignoring values with underscore
    name, _, age = ("Alice", "dummy", 30)
    print(f"Ignoring middle value: name={name}, age={age}")
    print()

    # =============================================================================
    # 8. ITERATING THROUGH TUPLES
    # =============================================================================

    fruits = ("apple", "banana", "cherry")

    # Basic iteration
    print("Basic iteration:")
    for fruit in fruits:
        print(f"  {fruit}")

    # With index using enumerate()
    print("\nWith index:")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")

    # Iterating backwards
    print("\nBackwards:")
    for fruit in reversed(fruits):
        print(f"  {fruit}")
    print()

    # =============================================================================
    # 9. NESTED TUPLES
    # =============================================================================

    matrix = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )

    print("Nested tuple access:")
    print(f"Element at [0][0]: {matrix[0][0]}")  # 1
    print(f"Element at [1][2]: {matrix[1][2]}")  # 6
    print(f"Second row: {matrix[1]}")            # (4, 5, 6)

    print("\nIterating nested tuple:")
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()
    print()

    # =============================================================================
    # 10. TUPLES AS DICTIONARY KEYS
    # =============================================================================

    # Tuples can be used as dictionary keys (because they're immutable)
    locations = {}
    locations[(0, 0)] = "Origin"
    locations[(1, 2)] = "Point A"
    locations[(3, 4)] = "Point B"

    print("Tuples as dictionary keys:")
    for coords, name in locations.items():
        print(f"  {coords}: {name}")
    print()

    # Lists cannot be used as keys (they're mutable)
    try:
        bad_dict = {[1, 2]: "value"}  # This will raise an error
    except TypeError as e:
        print(f"Lists as keys error: {e}")
    print()

    # =============================================================================
    # 11. NAMED TUPLES
    # =============================================================================

    from collections import namedtuple

    # Define a named tuple type
    Point = namedtuple('Point', ['x', 'y'])
    Person = namedtuple('Person', ['name', 'age', 'city'])

    # Create instances
    p = Point(11, 22)
    person = Person('Alice', 30, 'New York')

    # Access by index (like regular tuple)
    print(f"Point by index: x={p[0]}, y={p[1]}")

    # Access by name (more readable!)
    print(f"Point by name: x={p.x}, y={p.y}")
    print(f"Person: {person.name}, {person.age}, {person.city}")

    # Named tuples are still tuples
    print(f"Is Point a tuple? {isinstance(p, tuple)}")

    # Named tuples are immutable
    try:
        p.x = 100
    except AttributeError as e:
        print(f"Cannot modify: {e}")

    # Convert to dict
    print(f"As dict: {person._asdict()}")

    # Replace (creates new tuple)
    new_person = person._replace(age=31)
    print(f"Replaced: {new_person}")
    print()

    # =============================================================================
    # 12. CONVERTING BETWEEN LISTS AND TUPLES
    # =============================================================================

    # List to tuple
    my_list = [1, 2, 3, 4, 5]
    my_tuple = tuple(my_list)
    print(f"List to tuple: {my_tuple}")

    # Tuple to list
    my_tuple = (1, 2, 3, 4, 5)
    my_list = list(my_tuple)
    print(f"Tuple to list: {my_list}")

    # When to convert:
    # - Convert to list when you need to modify elements
    # - Convert back to tuple when you're done modifying
    numbers = (1, 2, 3, 4, 5)
    temp_list = list(numbers)
    temp_list.append(6)
    numbers = tuple(temp_list)
    print(f"After conversion and modification: {numbers}")
    print()

    # =============================================================================
    # 13. WHEN TO USE TUPLES VS LISTS
    # =============================================================================

    """
    Use TUPLES when:
    - Data should not change (e.g., coordinates, RGB colors, dates)
    - You need a hashable collection (for dict keys or set elements)
    - You want to signal that data is read-only
    - You need slightly better performance (tuples are faster)
    - You're returning multiple values from a function
    - Representing fixed structure (database records, config)

    Use LISTS when:
    - Data needs to be modified
    - You need to add/remove elements
    - Order matters and changes frequently
    - You need list-specific methods (append, remove, sort, etc.)
    """

    # Examples of good tuple use cases
    RGB_RED = (255, 0, 0)
    DATE_OF_BIRTH = (1990, 5, 15)  # year, month, day
    COORDINATES = (40.7128, -74.0060)  # latitude, longitude
    DIMENSIONS = (1920, 1080)  # width, height

    # Examples of good list use cases
    shopping_list = ["milk", "eggs", "bread"]  # Will add/remove items
    scores = [85, 92, 78, 95]  # May need to add more scores
    todo_items = ["task1", "task2"]  # Will be modified

    print("Tuple vs List use cases demonstrated above")
    print()

    # =============================================================================
    # 14. TUPLE COMPREHENSIONS (ACTUALLY GENERATOR EXPRESSIONS)
    # =============================================================================

    # Note: (x for x in ...) creates a generator, not a tuple!
    gen = (x**2 for x in range(5))
    print(f"Generator: {gen}")
    print(f"Generator type: {type(gen)}")

    # To create a tuple from comprehension, use tuple()
    squares_tuple = tuple(x**2 for x in range(5))
    print(f"Tuple from generator: {squares_tuple}")
    print()

    # =============================================================================
    # 15. PERFORMANCE AND MEMORY
    # =============================================================================

    import sys

    # Memory comparison
    list_example = [1, 2, 3, 4, 5]
    tuple_example = (1, 2, 3, 4, 5)

    print("Memory usage:")
    print(f"List size: {sys.getsizeof(list_example)} bytes")
    print(f"Tuple size: {sys.getsizeof(tuple_example)} bytes")
    print(f"Tuples use less memory!")
    print()

    # =============================================================================
    # 16. COMMON TUPLE PATTERNS
    # =============================================================================

    # Pattern 1: Returning multiple values
    def divide_with_remainder(a, b):
        quotient = a // b
        remainder = a % b
        return quotient, remainder  # Returns tuple

    q, r = divide_with_remainder(17, 5)
    print(f"17 ÷ 5 = {q} remainder {r}")

    # Pattern 2: Parallel iteration with zip
    names = ("Alice", "Bob", "Charlie")
    ages = (25, 30, 35)
    for name, age in zip(names, ages):
        print(f"  {name} is {age} years old")

    # Pattern 3: Constants/Configuration
    CONFIG = (
        ("host", "localhost"),
        ("port", 8080),
        ("debug", True)
    )

    # Pattern 4: Function arguments unpacking
    def greet(name, age, city):
        print(f"Hello {name}, age {age}, from {city}")

    person_data = ("Alice", 30, "NYC")
    greet(*person_data)  # Unpacks tuple as arguments

    # Pattern 5: Multiple return values with named tuples
    from collections import namedtuple
    Stats = namedtuple('Stats', ['min', 'max', 'avg'])

    def calculate_stats(numbers):
        return Stats(
            min=min(numbers),
            max=max(numbers),
            avg=sum(numbers) / len(numbers)
        )

    stats = calculate_stats([1, 2, 3, 4, 5])
    print(f"\nStats: min={stats.min}, max={stats.max}, avg={stats.avg:.1f}")
    print()

    # =============================================================================
    # 17. PERFORMANCE NOTES
    # =============================================================================

    """
    Operation           | Tuple | List
    --------------------|-------|------
    Creation            | Faster| Fast
    Access by index     | O(1)  | O(1)
    Iteration           | Faster| Fast
    Modification        | No    | Yes
    Memory usage        | Less  | More
    Can be dict key     | Yes   | No
    Can be in set       | Yes   | No

    Performance characteristics:
    - Tuples are generally faster than lists for iteration
    - Tuples have a smaller memory footprint
    - Tuples are immutable, so they can be hashed (used in sets/dicts)
    - Lists are more flexible but slightly slower

    Choose tuples for:
    - Performance (slightly faster)
    - Memory efficiency
    - Immutability guarantee
    - Use as dictionary keys

    Choose lists for:
    - Need to modify data
    - Need list methods
    - Dynamic collections
    """

    print("=" * 60)
    print("TUTORIAL COMPLETE!")
    print("Tuples are simple but powerful - know when to use them!")
    print("=" * 60)
