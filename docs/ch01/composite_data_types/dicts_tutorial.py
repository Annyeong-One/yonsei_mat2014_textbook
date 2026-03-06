"""
PYTHON DICTIONARIES - COMPLETE TUTORIAL
========================================

Dictionaries are mutable, unordered collections of key-value pairs.
They provide fast lookup and are one of Python's most useful data structures.
"""

# =============================================================================
# 1. CREATING DICTIONARIES
# =============================================================================

# Empty dictionary

if __name__ == "__main__":
    empty_dict = {}
    also_empty = dict()

    # Dictionary with initial values
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }

    # Using dict() constructor
    from_pairs = dict([("a", 1), ("b", 2), ("c", 3)])
    from_kwargs = dict(name="Bob", age=25, city="Boston")

    # Dictionary with mixed types
    mixed = {
        "string_key": "value",
        42: "number key",
        (1, 2): "tuple key",
        "list_value": [1, 2, 3],
        "dict_value": {"nested": "dict"}
    }

    print("Basic dictionaries created:")
    print(f"Person: {person}")
    print(f"From pairs: {from_pairs}")
    print()

    # =============================================================================
    # 2. ACCESSING VALUES
    # =============================================================================

    person = {"name": "Alice", "age": 30, "city": "New York"}

    # Using square brackets (raises KeyError if key doesn't exist)
    print("Accessing values:")
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")

    # Using get() method (returns None or default if key doesn't exist)
    print(f"City: {person.get('city')}")
    print(f"Country (not found): {person.get('country')}")
    print(f"Country with default: {person.get('country', 'USA')}")

    # Handling missing keys
    try:
        print(person["country"])  # This will raise KeyError
    except KeyError as e:
        print(f"KeyError: {e}")
    print()

    # =============================================================================
    # 3. ADDING AND MODIFYING VALUES
    # =============================================================================

    person = {"name": "Alice", "age": 30}

    # Adding new key-value pair
    person["city"] = "New York"
    print(f"After adding city: {person}")

    # Modifying existing value
    person["age"] = 31
    print(f"After modifying age: {person}")

    # Adding multiple items with update()
    person.update({"job": "Engineer", "salary": 85000})
    print(f"After update: {person}")

    # Using update with keyword arguments
    person.update(department="IT", years_experience=5)
    print(f"After update with kwargs: {person}")
    print()

    # =============================================================================
    # 4. REMOVING ITEMS
    # =============================================================================

    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "job": "Engineer",
        "salary": 85000
    }

    # Using del statement
    del person["salary"]
    print(f"After del: {person}")

    # Using pop() - removes and returns value
    job = person.pop("job")
    print(f"Popped job: {job}")
    print(f"After pop: {person}")

    # pop() with default value (doesn't raise error if key missing)
    country = person.pop("country", "Unknown")
    print(f"Popped country (with default): {country}")

    # Using popitem() - removes and returns last inserted key-value pair
    last_item = person.popitem()
    print(f"Popped last item: {last_item}")
    print(f"After popitem: {person}")

    # clear() - removes all items
    person.clear()
    print(f"After clear: {person}")
    print()

    # =============================================================================
    # 5. CHECKING MEMBERSHIP
    # =============================================================================

    person = {"name": "Alice", "age": 30, "city": "New York"}

    # Check if key exists
    print("Membership testing:")
    print(f"'name' in person: {'name' in person}")
    print(f"'country' in person: {'country' in person}")
    print(f"'salary' not in person: {'salary' not in person}")

    # Check if value exists (less efficient)
    print(f"'Alice' in person.values(): {'Alice' in person.values()}")
    print()

    # =============================================================================
    # 6. DICTIONARY METHODS
    # =============================================================================

    person = {"name": "Alice", "age": 30, "city": "New York"}

    # keys() - returns view of all keys
    print("Keys:", person.keys())
    print("Keys as list:", list(person.keys()))

    # values() - returns view of all values
    print("Values:", person.values())
    print("Values as list:", list(person.values()))

    # items() - returns view of all key-value pairs
    print("Items:", person.items())
    print("Items as list:", list(person.items()))

    # copy() - creates shallow copy
    person_copy = person.copy()
    print(f"Copy: {person_copy}")

    # setdefault() - returns value if key exists, otherwise sets default and returns it
    person.setdefault("country", "USA")
    print(f"After setdefault: {person}")

    # fromkeys() - creates dict from sequence of keys with same value
    keys = ["a", "b", "c"]
    default_dict = dict.fromkeys(keys, 0)
    print(f"From keys: {default_dict}")
    print()

    # =============================================================================
    # 7. ITERATING THROUGH DICTIONARIES
    # =============================================================================

    person = {"name": "Alice", "age": 30, "city": "New York"}

    # Iterate over keys (default)
    print("Iterating over keys:")
    for key in person:
        print(f"  {key}")

    # Iterate over keys explicitly
    print("\nIterating over keys (explicit):")
    for key in person.keys():
        print(f"  {key}: {person[key]}")

    # Iterate over values
    print("\nIterating over values:")
    for value in person.values():
        print(f"  {value}")

    # Iterate over key-value pairs (most common)
    print("\nIterating over items:")
    for key, value in person.items():
        print(f"  {key}: {value}")
    print()

    # =============================================================================
    # 8. DICTIONARY COMPREHENSIONS
    # =============================================================================

    # Basic dictionary comprehension
    squares = {x: x**2 for x in range(1, 6)}
    print(f"Squares: {squares}")

    # With condition
    even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    print(f"Even squares: {even_squares}")

    # From two lists using zip
    keys = ["name", "age", "city"]
    values = ["Bob", 25, "Boston"]
    person = {k: v for k, v in zip(keys, values)}
    print(f"From zip: {person}")

    # Inverting a dictionary (swap keys and values)
    original = {"a": 1, "b": 2, "c": 3}
    inverted = {v: k for k, v in original.items()}
    print(f"Original: {original}")
    print(f"Inverted: {inverted}")

    # Transform values
    prices = {"apple": 1.50, "banana": 0.75, "cherry": 2.00}
    discounted = {item: price * 0.9 for item, price in prices.items()}
    print(f"Discounted prices: {discounted}")
    print()

    # =============================================================================
    # 9. NESTED DICTIONARIES
    # =============================================================================

    # Dictionary of dictionaries
    users = {
        "user1": {
            "name": "Alice",
            "age": 30,
            "email": "alice@email.com"
        },
        "user2": {
            "name": "Bob",
            "age": 25,
            "email": "bob@email.com"
        }
    }

    print("Nested dictionary:")
    print(f"User1 name: {users['user1']['name']}")
    print(f"User2 age: {users['user2']['age']}")

    # Iterating nested dictionaries
    print("\nAll users:")
    for user_id, user_data in users.items():
        print(f"  {user_id}:")
        for key, value in user_data.items():
            print(f"    {key}: {value}")
    print()

    # =============================================================================
    # 10. MERGING DICTIONARIES
    # =============================================================================

    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    dict3 = {"b": 20, "e": 5}

    # Using update() (modifies dict1)
    dict1_copy = dict1.copy()
    dict1_copy.update(dict2)
    print(f"Merged with update: {dict1_copy}")

    # Using {**dict1, **dict2} (Python 3.5+)
    merged = {**dict1, **dict2}
    print(f"Merged with **: {merged}")

    # Merge with conflict (later values win)
    merged_conflict = {**dict1, **dict3}
    print(f"Merged with conflict: {merged_conflict}")

    # Using | operator (Python 3.9+)
    try:
        merged_pipe = dict1 | dict2
        print(f"Merged with |: {merged_pipe}")
    except TypeError:
        print("| operator not available (Python < 3.9)")

    # Merging multiple dictionaries
    all_merged = {**dict1, **dict2, **dict3}
    print(f"All merged: {all_merged}")
    print()

    # =============================================================================
    # 11. DEFAULT DICTIONARIES
    # =============================================================================

    from collections import defaultdict

    # Regular dict - KeyError if key doesn't exist
    regular = {}
    try:
        regular["missing"] += 1
    except KeyError:
        print("KeyError with regular dict")

    # defaultdict with default value
    counts = defaultdict(int)  # default value is 0
    counts["apple"] += 1
    counts["banana"] += 1
    counts["apple"] += 1
    print(f"Counts (defaultdict): {dict(counts)}")

    # defaultdict with list
    groups = defaultdict(list)
    groups["fruits"].append("apple")
    groups["fruits"].append("banana")
    groups["vegetables"].append("carrot")
    print(f"Groups: {dict(groups)}")

    # defaultdict with custom default
    def default_value():
        return "Unknown"

    info = defaultdict(default_value)
    print(f"Missing key: {info['missing']}")
    print()

    # =============================================================================
    # 12. ORDERED DICTIONARIES
    # =============================================================================

    from collections import OrderedDict

    # In Python 3.7+, regular dicts maintain insertion order
    # OrderedDict is mainly for compatibility and explicit ordering

    regular_dict = {}
    regular_dict["b"] = 2
    regular_dict["a"] = 1
    regular_dict["c"] = 3
    print(f"Regular dict (3.7+): {regular_dict}")  # Maintains order

    # OrderedDict
    ordered = OrderedDict()
    ordered["b"] = 2
    ordered["a"] = 1
    ordered["c"] = 3
    print(f"OrderedDict: {ordered}")

    # Move to end
    ordered.move_to_end("b")
    print(f"After move_to_end: {ordered}")
    print()

    # =============================================================================
    # 13. COUNTER
    # =============================================================================

    from collections import Counter

    # Counting elements
    fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    fruit_counts = Counter(fruits)
    print(f"Fruit counts: {fruit_counts}")

    # Most common elements
    print(f"Most common (2): {fruit_counts.most_common(2)}")

    # Counter arithmetic
    counter1 = Counter(["a", "b", "c", "a"])
    counter2 = Counter(["a", "b", "d", "b"])
    print(f"Counter1: {counter1}")
    print(f"Counter2: {counter2}")
    print(f"Addition: {counter1 + counter2}")
    print(f"Subtraction: {counter1 - counter2}")
    print()

    # =============================================================================
    # 14. DICTIONARY VIEWS
    # =============================================================================

    person = {"name": "Alice", "age": 30, "city": "New York"}

    # Views are dynamic - they reflect changes
    keys_view = person.keys()
    values_view = person.values()
    items_view = person.items()

    print("Original views:")
    print(f"Keys: {keys_view}")
    print(f"Values: {values_view}")

    # Modify dictionary
    person["job"] = "Engineer"
    del person["age"]

    print("\nViews after modification:")
    print(f"Keys: {keys_view}")  # Updated!
    print(f"Values: {values_view}")  # Updated!
    print()

    # =============================================================================
    # 15. DICTIONARY UNPACKING
    # =============================================================================

    def greet(name, age, city):
        print(f"Hello {name}, age {age}, from {city}")

    person = {"name": "Alice", "age": 30, "city": "New York"}

    # Unpack dictionary as function arguments
    greet(**person)

    # Unpacking in dictionary literals
    defaults = {"theme": "dark", "language": "en"}
    custom = {"language": "es", "timezone": "UTC"}
    settings = {**defaults, **custom}
    print(f"Settings: {settings}")
    print()

    # =============================================================================
    # 16. COMMON PATTERNS AND TIPS
    # =============================================================================

    # Get value or set default if missing (idiomatic)
    cache = {}
    key = "expensive_computation"
    if key not in cache:
        cache[key] = "computed_value"
    value = cache[key]

    # Same thing using setdefault
    value = cache.setdefault(key, "computed_value")

    # Swap keys and values (be careful with duplicate values!)
    original = {"a": 1, "b": 2, "c": 3}
    swapped = {v: k for k, v in original.items()}
    print(f"Swapped: {swapped}")

    # Filter dictionary
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
    high_scores = {name: score for name, score in scores.items() if score >= 90}
    print(f"High scores: {high_scores}")

    # Group by property
    students = [
        {"name": "Alice", "grade": "A"},
        {"name": "Bob", "grade": "B"},
        {"name": "Charlie", "grade": "A"},
        {"name": "Diana", "grade": "C"}
    ]
    by_grade = {}
    for student in students:
        grade = student["grade"]
        if grade not in by_grade:
            by_grade[grade] = []
        by_grade[grade].append(student["name"])
    print(f"Students by grade: {by_grade}")

    # Using defaultdict for grouping
    from collections import defaultdict
    by_grade_dd = defaultdict(list)
    for student in students:
        by_grade_dd[student["grade"]].append(student["name"])
    print(f"Using defaultdict: {dict(by_grade_dd)}")
    print()

    # =============================================================================
    # 17. PERFORMANCE NOTES
    # =============================================================================

    """
    Operation               | Average | Worst Case
    ------------------------|---------|------------
    Access by key           | O(1)    | O(n)
    Insert item             | O(1)    | O(n)
    Delete item             | O(1)    | O(n)
    Search for key          | O(1)    | O(n)
    Search for value        | O(n)    | O(n)
    Iterate                 | O(n)    | O(n)

    Key Points:
    - Dictionaries use hash tables internally
    - Keys must be hashable (immutable types)
    - Average O(1) for most operations makes dicts very fast
    - Space overhead compared to lists
    - Order preserved in Python 3.7+
    """

    # =============================================================================
    # 18. WHEN TO USE DICTIONARIES
    # =============================================================================

    """
    Use DICTIONARIES when:
    - You need key-value associations
    - You need fast lookups by key
    - Keys are meaningful (not just indices)
    - You're counting/grouping items
    - You need to map between different data types
    - Order of insertion matters (Python 3.7+)

    Use LISTS when:
    - You need ordered sequences
    - You need to access by numeric index
    - You need to sort easily
    - Keys would just be 0, 1, 2, 3...

    Use SETS when:
    - You only need keys (no values)
    - You need set operations (union, intersection)
    - You need to remove duplicates
    - Order doesn't matter
    """

    print("=" * 60)
    print("TUTORIAL COMPLETE!")
    print("Dictionaries are powerful - practice with the exercises!")
    print("=" * 60)
