"""
01_map_filter_functions.py

TOPIC: map() and filter() Functions
LEVEL: Advanced
DURATION: 45-60 minutes

LEARNING OBJECTIVES:
1. Use map() to transform sequences
2. Use filter() to select elements
3. Combine map/filter with lambda functions
4. Compare to list comprehensions

KEY FUNCTIONS:
- map(function, iterable) - Apply function to each element
- filter(function, iterable) - Keep elements where function returns True
"""

# ============================================================================
# SECTION 1: Understanding map()
# ============================================================================

if __name__ == "__main__":

    print("=" * 70)
    print("SECTION 1: The map() Function")
    print("=" * 70)

    # map() applies a function to every item in an iterable
    # Returns a map object (iterator) - convert to list to see results

    # Example 1: Square all numbers
    numbers = [1, 2, 3, 4, 5]

    def square(x):
        return x ** 2

    squared = map(square, numbers)
    print(f"\nOriginal: {numbers}")
    print(f"map(square, numbers): {list(squared)}")

    # Example 2: Using lambda with map
    numbers = [1, 2, 3, 4, 5]
    squared = map(lambda x: x ** 2, numbers)
    print(f"\nWith lambda: {list(squared)}")

    # Example 3: Multiple iterables
    numbers1 = [1, 2, 3]
    numbers2 = [10, 20, 30]
    sums = map(lambda x, y: x + y, numbers1, numbers2)
    print(f"\nmap with 2 lists: {list(sums)}")

    # Example 4: String operations
    words = ["hello", "world", "python"]
    uppercase = map(str.upper, words)
    print(f"\nUppercase: {list(uppercase)}")

    print("""
    KEY POINTS:
    - map() returns an iterator (lazy evaluation)
    - Converts to list when needed: list(map(...))
    - Can use with lambda or named functions
    - Can take multiple iterables
    """)

    # ============================================================================
    # SECTION 2: Understanding filter()
    # ============================================================================

    print("\n" + "=" * 70)
    print("SECTION 2: The filter() Function")
    print("=" * 70)

    # filter() keeps only elements where function returns True

    # Example 1: Filter even numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def is_even(x):
        return x % 2 == 0

    evens = filter(is_even, numbers)
    print(f"\nOriginal: {numbers}")
    print(f"filter(is_even): {list(evens)}")

    # Example 2: Using lambda with filter
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = filter(lambda x: x % 2 == 0, numbers)
    print(f"\nWith lambda: {list(evens)}")

    # Example 3: Filter strings
    words = ["apple", "banana", "apricot", "cherry", "avocado"]
    a_words = filter(lambda w: w.startswith('a'), words)
    print(f"\nWords starting with 'a': {list(a_words)}")

    # Example 4: Filter None and falsy values
    values = [0, 1, False, True, "", "hello", None, [], [1, 2]]
    truthy = filter(None, values)  # None means "keep truthy values"
    print(f"\nTruthy values: {list(truthy)}")

    print("""
    KEY POINTS:
    - filter() returns an iterator
    - Keeps elements where function returns True
    - filter(None, iterable) keeps truthy values
    - Use lambda for simple conditions
    """)

    # ============================================================================
    # SECTION 3: Combining map() and filter()
    # ============================================================================

    print("\n" + "=" * 70)
    print("SECTION 3: Combining map() and filter()")
    print("=" * 70)

    # Chain operations: filter then map
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Get squares of even numbers
    evens = filter(lambda x: x % 2 == 0, numbers)
    squared_evens = map(lambda x: x ** 2, evens)
    result = list(squared_evens)
    print(f"Squares of even numbers: {result}")

    # Or in one line:
    result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
    print(f"One-liner version: {result}")

    # ============================================================================
    # SECTION 4: map/filter vs List Comprehensions
    # ============================================================================

    print("\n" + "=" * 70)
    print("SECTION 4: map/filter vs List Comprehensions")
    print("=" * 70)

    numbers = [1, 2, 3, 4, 5]

    # Using map
    print("\nUsing map():")
    squared_map = list(map(lambda x: x ** 2, numbers))
    print(f"  {squared_map}")

    # Using list comprehension
    print("\nUsing list comprehension:")
    squared_comp = [x ** 2 for x in numbers]
    print(f"  {squared_comp}")

    # Using filter
    print("\nUsing filter():")
    evens_filter = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"  {evens_filter}")

    # Using list comprehension
    print("\nUsing list comprehension:")
    evens_comp = [x for x in numbers if x % 2 == 0]
    print(f"  {evens_comp}")

    # Combined: squares of evens
    print("\nSquares of evens - map/filter:")
    result1 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
    print(f"  {result1}")

    print("\nSquares of evens - comprehension:")
    result2 = [x**2 for x in numbers if x % 2 == 0]
    print(f"  {result2}")

    print("""
    WHEN TO USE WHAT:
    - List comprehensions: More Pythonic, easier to read
    - map(): When you have existing function to apply
    - filter(): When you have existing predicate function
    - Both give same results, choose for readability
    """)

    # ============================================================================
    # SECTION 5: Practical Examples
    # ============================================================================

    print("\n" + "=" * 70)
    print("SECTION 5: Practical Examples")
    print("=" * 70)

    # Example 1: Process user data
    print("\nExample 1: Clean and format names")
    names = ["  alice  ", "BOB", "  Charlie"]
    cleaned = list(map(lambda s: s.strip().title(), names))
    print(f"Original: {names}")
    print(f"Cleaned: {cleaned}")

    # Example 2: Temperature conversion
    print("\nExample 2: Celsius to Fahrenheit")
    celsius = [0, 10, 20, 30, 100]
    fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
    for c, f in zip(celsius, fahrenheit):
        print(f"  {c}°C = {f}°F")

    # Example 3: Grade filtering
    print("\nExample 3: Filter passing grades")
    grades = [45, 78, 92, 55, 67, 88, 34, 91]
    passing = list(filter(lambda g: g >= 60, grades))
    print(f"All grades: {grades}")
    print(f"Passing (>=60): {passing}")
    print(f"Pass rate: {len(passing)/len(grades)*100:.1f}%")

    # Example 4: Data validation
    print("\nExample 4: Validate email addresses")
    emails = ["user@example.com", "invalid", "test@test.org", "no-at-sign"]
    valid_emails = list(filter(lambda e: '@' in e and '.' in e, emails))
    print(f"Valid emails: {valid_emails}")

    print("\nSee exercises.py for practice!")
