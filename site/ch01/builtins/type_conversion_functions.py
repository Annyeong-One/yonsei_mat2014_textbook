"""
02_type_conversion_functions.py

TOPIC: Type Conversion Built-in Functions
LEVEL: Basic
DURATION: 30-45 minutes

LEARNING OBJECTIVES:
1. Convert between basic data types
2. Understand type conversion rules
3. Handle conversion errors
4. Use type constructors for data structures

KEY FUNCTIONS:
- int(), float(), str(), bool()
- list(), tuple(), dict(), set()
- chr(), ord(), hex(), bin()
"""

# ============================================================================
# SECTION 1: Basic Type Conversions
# ============================================================================

if __name__ == "__main__":

    print("=" * 70)
    print("SECTION 1: Basic Type Conversions")
    print("=" * 70)

    # String to Integer
    print("\nString to Integer:")
    age_str = "25"
    age_int = int(age_str)
    print(f"String '{age_str}' -> Integer {age_int}")
    print(f"Type: {type(age_str)} -> {type(age_int)}")

    # String to Float
    print("\nString to Float:")
    price_str = "19.99"
    price_float = float(price_str)
    print(f"String '{price_str}' -> Float {price_float}")

    # Float to Integer (truncates decimal part)
    print("\nFloat to Integer:")
    pi = 3.14159
    pi_int = int(pi)
    print(f"Float {pi} -> Integer {pi_int} (truncated)")

    # Integer to String
    print("\nInteger to String:")
    age = 25
    age_str = str(age)
    print(f"Integer {age} -> String '{age_str}'")
    print(f"Can now concatenate: 'Age: ' + '{age_str}' = '{'Age: ' + age_str}'")

    # ============================================================================
    # SECTION 2: Boolean Conversions
    # ============================================================================

    print("\n" + "=" * 70)
    print("SECTION 2: Boolean Conversions")
    print("=" * 70)

    # Any value can be converted to bool
    print("\nConverting to Boolean:")

    # Numbers: 0 is False, everything else is True
    print(f"bool(0) = {bool(0)}")           # False
    print(f"bool(1) = {bool(1)}")           # True
    print(f"bool(-5) = {bool(-5)}")         # True
    print(f"bool(0.0) = {bool(0.0)}")       # False

    # Strings: empty string is False, any content is True
    print(f"\nbool('') = {bool('')}")       # False (empty string)
    print(f"bool('hello') = {bool('hello')}")  # True
    print(f"bool(' ') = {bool(' ')}")       # True (space is content!)

    # Containers: empty is False, with content is True
    print(f"\nbool([]) = {bool([])}")       # False (empty list)
    print(f"bool([1]) = {bool([1])}")       # True
    print(f"bool({{}}) = {bool({})}")       # False (empty dict)
    print(f"bool(None) = {bool(None)}")     # False

    print("""
    RULE: These are "falsy" (convert to False):
    - 0, 0.0
    - Empty string: ''
    - Empty containers: [], {}, ()
    - None
    Everything else is "truthy" (converts to True)
    """)

    # ============================================================================
    # SECTION 3: Advanced Number Conversions
    # ============================================================================

    print("\n" + "=" * 70)
    print("SECTION 3: Advanced Number Conversions")
    print("=" * 70)

    # Converting between number bases
    print("Number base conversions:")
    number = 42

    print(f"\nDecimal: {number}")
    print(f"Binary:  {bin(number)}")   # 0b prefix
    print(f"Octal:   {oct(number)}")   # 0o prefix
    print(f"Hex:     {hex(number)}")   # 0x prefix

    # Converting from string with base
    print("\nConverting from different bases:")
    binary_str = "101010"
    print(f"Binary string '101010' to int: {int(binary_str, 2)}")

    hex_str = "2A"
    print(f"Hex string '2A' to int: {int(hex_str, 16)}")

    # Character conversions
    print("\nCharacter <-> Number:")
    print(f"ord('A') = {ord('A')}")  # Character to ASCII value
    print(f"chr(65) = {chr(65)}")    # ASCII value to character
    print(f"ord('a') = {ord('a')}")
    print(f"chr(97) = {chr(97)}")

    # ============================================================================
    # SECTION 4: Container Conversions
    # ============================================================================

    print("\n" + "=" * 70)
    print("SECTION 4: Container Conversions")
    print("=" * 70)

    # List from various sources
    print("Creating lists:")
    string = "Python"
    print(f"list('{string}') = {list(string)}")  # Splits into characters

    numbers = (1, 2, 3, 4, 5)
    print(f"list({numbers}) = {list(numbers)}")  # Tuple to list

    # Tuple from various sources
    print("\nCreating tuples:")
    my_list = [1, 2, 3]
    print(f"tuple({my_list}) = {tuple(my_list)}")

    # Set from various sources (removes duplicates)
    print("\nCreating sets:")
    duplicates = [1, 2, 2, 3, 3, 3]
    print(f"set({duplicates}) = {set(duplicates)}")

    # Dictionary from list of tuples
    print("\nCreating dictionaries:")
    pairs = [('a', 1), ('b', 2), ('c', 3)]
    print(f"dict({pairs}) = {dict(pairs)}")

    # ============================================================================
    # SECTION 5: Error Handling
    # ============================================================================

    print("\n" + "=" * 70)
    print("SECTION 5: Conversion Errors")
    print("=" * 70)

    print("These conversions will FAIL:")
    print("""
    int("hello")        # ValueError: invalid literal
    int("12.5")         # ValueError: can't convert directly
    float("abc")        # ValueError: invalid literal
    int("12 34")        # ValueError: space in number
    """)

    # Safe conversion with try/except
    print("\nSafe conversion pattern:")
    def safe_int_conversion(value):
        try:
            return int(value)
        except ValueError:
            print(f"Cannot convert '{value}' to integer")
            return None

    print(safe_int_conversion("123"))    # Works
    print(safe_int_conversion("abc"))    # Fails gracefully

    # ============================================================================
    # SECTION 6: Practical Examples
    # ============================================================================

    print("\n" + "=" * 70)
    print("SECTION 6: Practical Examples")
    print("=" * 70)

    # Example 1: User input processing
    print("\nExample 1: Processing user input")
    print("Simulating: user_input = '25'")
    user_input = "25"
    age = int(user_input)
    is_adult = age >= 18
    print(f"Age: {age}, Is adult: {is_adult}")

    # Example 2: Formatting numbers
    print("\nExample 2: Number formatting")
    price = 1234.567
    price_str = f"${price:.2f}"
    print(f"Price as string: {price_str}")

    # Example 3: Removing duplicates from list
    print("\nExample 3: Remove duplicates")
    numbers_with_dupes = [1, 2, 3, 2, 1, 4, 3, 5]
    unique_numbers = list(set(numbers_with_dupes))
    print(f"Original: {numbers_with_dupes}")
    print(f"Unique:   {sorted(unique_numbers)}")  # Sort to restore order

    # Example 4: Splitting and converting
    print("\nExample 4: String to number list")
    number_string = "10 20 30 40 50"
    number_list = [int(x) for x in number_string.split()]
    print(f"String: '{number_string}'")
    print(f"List: {number_list}")

    # ============================================================================
    # SECTION 7: Key Takeaways
    # ============================================================================

    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS")
    print("=" * 70)

    print("""
    1. int() converts to integer (truncates floats)
    2. float() converts to floating point
    3. str() converts anything to string
    4. bool() converts to True/False (falsy vs truthy values)
    5. list(), tuple(), set(), dict() create containers
    6. ord() converts character to number, chr() does reverse
    7. bin(), oct(), hex() convert numbers to different bases
    8. int(string, base) converts from specific base
    9. Always handle ValueError for invalid conversions
    10. Empty containers/strings/0/None are "falsy"

    COMMON PATTERNS:
    - User input: int(input("Enter number: "))
    - Remove duplicates: list(set(my_list))
    - Check if value: if value: (uses bool conversion)
    - Format output: str(number) or f"{number}"
    """)

    print("\nSee exercises.py for practice problems!")
