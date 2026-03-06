#!/usr/bin/env python3
"""
Python Strings - Practical Examples
====================================

This file contains 20 practical examples demonstrating Python string operations.
Run this file to see all examples in action.

Usage: python 02_strings_examples.py
"""

if __name__ == "__main__":

    print("=" * 70)
    print("PYTHON STRINGS - 20 PRACTICAL EXAMPLES")
    print("=" * 70)
    print()

    # ============================================================================
    # EXAMPLE 1: Creating Strings
    # ============================================================================

    print("Example 1: Creating Strings")
    print("-" * 70)

    single = 'Single quotes'
    double = "Double quotes"
    triple = '''Triple
    quotes
    for multiline'''

    print(f"Single: {single}")
    print(f"Double: {double}")
    print(f"Triple: {triple}")
    print(f"Empty string: '{''}'")
    print(f"String from number: {str(42)}")

    print("\nExplanation:")
    print("• Single/double quotes: for regular strings")
    print("• Triple quotes: for multiline strings or docstrings")
    print("• str(): converts other types to strings")
    print()

    # ============================================================================
    # EXAMPLE 2: String Indexing
    # ============================================================================

    print("=" * 70)
    print("Example 2: String Indexing")
    print("-" * 70)

    text = "Python"
    print(f"String: '{text}'")
    print(f"Indices:  0 1 2 3 4 5")
    print(f"         -6-5-4-3-2-1\n")

    print(f"text[0]  = '{text[0]}'   (first character)")
    print(f"text[5]  = '{text[5]}'   (last character)")
    print(f"text[-1] = '{text[-1]}'   (last character, negative index)")
    print(f"text[-6] = '{text[-6]}'   (first character, negative index)")

    print("\nExplanation:")
    print("• Positive indices start from 0 (left to right)")
    print("• Negative indices start from -1 (right to left)")
    print("• Useful for accessing first/last characters easily")
    print()

    # ============================================================================
    # EXAMPLE 3: String Slicing
    # ============================================================================

    print("=" * 70)
    print("Example 3: String Slicing")
    print("-" * 70)

    text = "Python Programming"
    print(f"Original: '{text}'")
    print(f"Length: {len(text)}\n")

    print(f"text[:6]      = '{text[:6]}'      (first 6 characters)")
    print(f"text[7:]      = '{text[7:]}'      (from index 7 to end)")
    print(f"text[7:11]    = '{text[7:11]}'    (characters 7-10)")
    print(f"text[-11:]    = '{text[-11:]}'    (last 11 characters)")
    print(f"text[::2]     = '{text[::2]}'     (every 2nd character)")
    print(f"text[::-1]    = '{text[::-1]}'    (reverse string)")

    print("\nExplanation:")
    print("• Syntax: string[start:stop:step]")
    print("• start: inclusive, stop: exclusive")
    print("• Omit start: begins at 0")
    print("• Omit stop: goes to end")
    print("• Negative step: reverses direction")
    print()

    # ============================================================================
    # EXAMPLE 4: String Concatenation and Repetition
    # ============================================================================

    print("=" * 70)
    print("Example 4: Concatenation and Repetition")
    print("-" * 70)

    first = "Hello"
    last = "World"

    # Concatenation
    combined = first + " " + last
    print(f"'{first}' + ' ' + '{last}' = '{combined}'")

    # Repetition
    repeated = "Python" * 3
    print(f"'Python' * 3 = '{repeated}'")

    # Practical uses
    separator = "=" * 40
    print(f"\nSeparator: {separator}")

    greeting = "Hi! " * 5
    print(f"Greeting: {greeting}")

    print("\nExplanation:")
    print("• + operator: joins strings together")
    print("• * operator: repeats string n times")
    print("• Useful for creating separators, padding, etc.")
    print()

    # ============================================================================
    # EXAMPLE 5: String Methods - Case Conversion
    # ============================================================================

    print("=" * 70)
    print("Example 5: Case Conversion Methods")
    print("-" * 70)

    text = "python programming"
    print(f"Original: '{text}'\n")

    print(f".upper()      → '{text.upper()}'")
    print(f".lower()      → '{text.lower()}'")
    print(f".capitalize() → '{text.capitalize()}'")
    print(f".title()      → '{text.title()}'")

    mixed = "PyThOn"
    print(f"\n'{mixed}'.swapcase() → '{mixed.swapcase()}'")

    print("\nExplanation:")
    print("• .upper(): all uppercase")
    print("• .lower(): all lowercase")
    print("• .capitalize(): first letter only")
    print("• .title(): first letter of each word")
    print("• .swapcase(): swap case of all letters")
    print()

    # ============================================================================
    # EXAMPLE 6: String Methods - Trimming
    # ============================================================================

    print("=" * 70)
    print("Example 6: Trimming Whitespace")
    print("-" * 70)

    text = "   Hello, World!   "
    print(f"Original: '{text}' (length: {len(text)})\n")

    print(f".strip()  → '{text.strip()}'  (both ends)")
    print(f".lstrip() → '{text.lstrip()}' (left only)")
    print(f".rstrip() → '{text.rstrip()}' (right only)")

    # Strip specific characters
    dirty = "###Hello###"
    clean = dirty.strip('#')
    print(f"\n'{dirty}'.strip('#') → '{clean}'")

    print("\nExplanation:")
    print("• .strip(): removes whitespace from both ends")
    print("• .lstrip(): removes from left (start)")
    print("• .rstrip(): removes from right (end)")
    print("• Can specify characters to strip")
    print()

    # ============================================================================
    # EXAMPLE 7: String Methods - Splitting and Joining
    # ============================================================================

    print("=" * 70)
    print("Example 7: Splitting and Joining")
    print("-" * 70)

    # Splitting
    csv = "apple,banana,cherry,date"
    fruits = csv.split(',')
    print(f"CSV: '{csv}'")
    print(f"Split: {fruits}\n")

    sentence = "Python is awesome"
    words = sentence.split()
    print(f"Sentence: '{sentence}'")
    print(f"Words: {words}\n")

    # Joining
    joined = " | ".join(fruits)
    print(f"Join with ' | ': '{joined}'")

    path = "/".join(["home", "user", "documents"])
    print(f"Path: '{path}'")

    print("\nExplanation:")
    print("• .split(delimiter): converts string to list")
    print("• .split() with no argument: splits on whitespace")
    print("• .join(list): converts list to string")
    print("• join is called on the delimiter string")
    print()

    # ============================================================================
    # EXAMPLE 8: String Methods - Searching
    # ============================================================================

    print("=" * 70)
    print("Example 8: Searching in Strings")
    print("-" * 70)

    text = "Python Programming in Python"
    print(f"Text: '{text}'\n")

    print(f".find('Python')       → {text.find('Python')} (first occurrence)")
    print(f".find('Java')         → {text.find('Java')} (not found)")
    print(f".count('Python')      → {text.count('Python')} (occurrences)")
    print(f".count('o')           → {text.count('o')}")
    print(f".startswith('Python') → {text.startswith('Python')}")
    print(f".endswith('Python')   → {text.endswith('Python')}")
    print(f".startswith('Java')   → {text.startswith('Java')}")

    print("\nExplanation:")
    print("• .find(): returns index or -1 if not found")
    print("• .count(): counts occurrences")
    print("• .startswith()/.endswith(): returns boolean")
    print("• All are case-sensitive")
    print()

    # ============================================================================
    # EXAMPLE 9: String Methods - Replacing
    # ============================================================================

    print("=" * 70)
    print("Example 9: Replacing Text")
    print("-" * 70)

    text = "Hello World"
    print(f"Original: '{text}'\n")

    print(f".replace('World', 'Python')  → '{text.replace('World', 'Python')}'")
    print(f".replace('o', '0')           → '{text.replace('o', '0')}'")
    print(f".replace('l', 'L', 1)        → '{text.replace('l', 'L', 1)}' (first only)")

    # Chaining replacements
    result = text.replace('o', '0').replace('l', '1')
    print(f"\nChained: .replace('o','0').replace('l','1') → '{result}'")

    print("\nExplanation:")
    print("• .replace(old, new): replaces all occurrences")
    print("• .replace(old, new, count): limits replacements")
    print("• Returns new string (original unchanged)")
    print("• Can chain multiple replacements")
    print()

    # ============================================================================
    # EXAMPLE 10: String Validation Methods
    # ============================================================================

    print("=" * 70)
    print("Example 10: Validation Methods")
    print("-" * 70)

    tests = [
        ("Hello", "isalpha"),
        ("Hello123", "isalpha"),
        ("12345", "isdigit"),
        ("123.45", "isdigit"),
        ("Hello123", "isalnum"),
        ("Hello 123", "isalnum"),
        ("hello", "islower"),
        ("HELLO", "isupper"),
        ("   ", "isspace"),
    ]

    for text, method in tests:
        result = getattr(text, method)()
        print(f"'{text}'.{method}() = {result}")

    print("\nExplanation:")
    print("• .isalpha(): only letters")
    print("• .isdigit(): only digits")
    print("• .isalnum(): letters and/or digits")
    print("• .islower()/.isupper(): case check")
    print("• .isspace(): only whitespace")
    print()

    # ============================================================================
    # EXAMPLE 11: f-strings (Modern Formatting)
    # ============================================================================

    print("=" * 70)
    print("Example 11: f-strings (Python 3.6+)")
    print("-" * 70)

    name = "Alice"
    age = 30
    height = 5.6

    # Basic f-strings
    print(f"Name: {name}")
    print(f"Age: {age}")

    # Expressions
    print(f"Next year: {age + 1}")
    print(f"Uppercase: {name.upper()}")

    # Multiple variables
    print(f"{name} is {age} years old")

    # Number formatting
    price = 19.99
    print(f"Price: ${price:.2f}")

    # Padding and alignment
    print(f"Left:   |{name:<10}|")
    print(f"Right:  |{name:>10}|")
    print(f"Center: |{name:^10}|")

    print("\nExplanation:")
    print("• Most modern and readable formatting")
    print("• Can include expressions and method calls")
    print("• :.2f means 2 decimal places")
    print("• < left, > right, ^ center alignment")
    print()

    # ============================================================================
    # EXAMPLE 12: .format() Method
    # ============================================================================

    print("=" * 70)
    print("Example 12: .format() Method")
    print("-" * 70)

    name = "Bob"
    age = 25

    # Positional
    print("Name: {}, Age: {}".format(name, age))

    # Indexed
    print("{0} is {1} years old. {0} likes Python.".format(name, age))

    # Named
    print("{n} is {a} years old".format(n=name, a=age))

    # Formatting
    print("Pi: {:.2f}".format(3.14159))
    print("Padded: {:0>5}".format(42))

    print("\nExplanation:")
    print("• Flexible formatting method")
    print("• Positional, indexed, or named arguments")
    print("• Same formatting options as f-strings")
    print()

    # ============================================================================
    # EXAMPLE 13: String Membership
    # ============================================================================

    print("=" * 70)
    print("Example 13: Membership Testing")
    print("-" * 70)

    text = "Python Programming Language"
    print(f"Text: '{text}'\n")

    searches = ["Python", "Java", "Programming", "python", "gram"]

    for word in searches:
        result = word in text
        print(f"'{word}' in text: {result}")

    print(f"\n'Java' not in text: {'Java' not in text}")

    print("\nExplanation:")
    print("• 'in' operator: checks if substring exists")
    print("• Returns True or False")
    print("• Case-sensitive")
    print("• 'not in': checks if substring doesn't exist")
    print()

    # ============================================================================
    # EXAMPLE 14: Escape Sequences
    # ============================================================================

    print("=" * 70)
    print("Example 14: Escape Sequences")
    print("-" * 70)

    print("Newline:")
    print("Line 1\nLine 2\nLine 3")

    print("\nTab:")
    print("Name:\tAlice\nAge:\t30")

    print("\nQuotes:")
    print("She said \"Hello\"")
    print('It\'s a nice day')

    print("\nBackslash:")
    print("Path: C:\\Users\\Alice\\Documents")

    print("\nRaw string (no escape processing):")
    print(r"Path: C:\Users\Alice\Documents")

    print("\nExplanation:")
    print("• \\n: newline")
    print("• \\t: tab")
    print("• \\': single quote")
    print("• \\\": double quote")
    print("• \\\\: backslash")
    print("• r'...': raw string (literal backslashes)")
    print()

    # ============================================================================
    # EXAMPLE 15: Multiline Strings
    # ============================================================================

    print("=" * 70)
    print("Example 15: Multiline Strings")
    print("-" * 70)

    # Triple quotes
    poem = """Roses are red,
    Violets are blue,
    Python is awesome,
    And so are you!"""

    print(poem)

    # Indented multiline (with dedent)
    import textwrap

    code = """
        def hello():
            print("Hello")
            return True
    """

    # Remove common leading whitespace
    clean_code = textwrap.dedent(code).strip()
    print("\nCode (dedented):")
    print(clean_code)

    print("\nExplanation:")
    print("• Triple quotes: preserve formatting and newlines")
    print("• Great for docstrings, poems, SQL, etc.")
    print("• textwrap.dedent(): removes common indentation")
    print()

    # ============================================================================
    # EXAMPLE 16: String Comparison
    # ============================================================================

    print("=" * 70)
    print("Example 16: String Comparison")
    print("-" * 70)

    print("Equality:")
    print(f"'apple' == 'apple': {'apple' == 'apple'}")
    print(f"'Apple' == 'apple': {'Apple' == 'apple'}")

    print("\nLexicographic order:")
    print(f"'apple' < 'banana': {'apple' < 'banana'}")
    print(f"'abc' < 'abd': {'abc' < 'abd'}")
    print(f"'Apple' < 'apple': {'Apple' < 'apple'}")

    print("\nString vs numeric:")
    print(f"'2' < '10': {'2' < '10'} (string comparison!)")
    print(f"2 < 10: {2 < 10} (numeric comparison)")

    print("\nExplanation:")
    print("• Comparison is case-sensitive")
    print("• Lexicographic: like dictionary order")
    print("• Compares character by character")
    print("• String '10' < '2' (compares '1' vs '2')")
    print()

    # ============================================================================
    # EXAMPLE 17: String Immutability
    # ============================================================================

    print("=" * 70)
    print("Example 17: String Immutability")
    print("-" * 70)

    text = "Hello"
    print(f"Original: '{text}'")
    print(f"ID: {id(text)}")

    # Methods return NEW strings
    upper = text.upper()
    print(f"\nAfter .upper(): '{upper}'")
    print(f"Original: '{text}' (unchanged)")
    print(f"Original ID: {id(text)}")
    print(f"New ID: {id(upper)} (different object)")

    # Cannot modify in place
    print("\nAttempting text[0] = 'h'...")
    try:
        text[0] = 'h'
    except TypeError as e:
        print(f"TypeError: {e}")

    # Create new string instead
    modified = 'h' + text[1:]
    print(f"\nSolution: 'h' + text[1:] = '{modified}'")

    print("\nExplanation:")
    print("• Strings cannot be changed after creation")
    print("• Methods return new strings")
    print("• Must create new string for modifications")
    print()

    # ============================================================================
    # EXAMPLE 18: Practical Use - Email Validation
    # ============================================================================

    print("=" * 70)
    print("Example 18: Practical - Email Validation")
    print("-" * 70)

    def is_valid_email(email):
        """Simple email validation"""
        email = email.strip()  # Remove whitespace

        if '@' not in email:
            return False

        if email.count('@') != 1:
            return False

        local, domain = email.split('@')

        if not local or not domain:
            return False

        if '.' not in domain:
            return False

        return True

    # Test cases
    emails = [
        "alice@example.com",
        "invalid.email",
        "no@domain",
        "  bob@test.com  ",
        "multiple@@at.com",
    ]

    for email in emails:
        valid = is_valid_email(email)
        print(f"'{email}' → {valid}")

    print("\nExplanation:")
    print("• Real-world string validation example")
    print("• Uses: .strip(), in, .count(), .split()")
    print("• Demonstrates practical string methods")
    print()

    # ============================================================================
    # EXAMPLE 19: Practical Use - Text Processing
    # ============================================================================

    print("=" * 70)
    print("Example 19: Practical - Text Processing")
    print("-" * 70)

    text = "  Python PROGRAMMING is FUN!  "
    print(f"Original: '{text}'\n")

    # Clean and normalize
    cleaned = text.strip()
    normalized = cleaned.lower()
    words = normalized.split()

    print(f"Cleaned: '{cleaned}'")
    print(f"Normalized: '{normalized}'")
    print(f"Words: {words}")

    # Word count
    word_count = len(words)
    print(f"\nWord count: {word_count}")

    # Most common character (excluding spaces)
    chars = [c for c in normalized if c.isalpha()]
    most_common = max(set(chars), key=chars.count)
    print(f"Most common letter: '{most_common}' ({chars.count(most_common)} times)")

    print("\nExplanation:")
    print("• Typical text processing workflow")
    print("• Clean → Normalize → Split → Analyze")
    print("• Combines multiple string methods")
    print()

    # ============================================================================
    # EXAMPLE 20: Practical Use - Building Dynamic SQL (Safe Way)
    # ============================================================================

    print("=" * 70)
    print("Example 20: Practical - Building Formatted Output")
    print("-" * 70)

    # Create a formatted table
    print("Student Report Card")
    print("=" * 50)

    students = [
        {"name": "Alice", "grade": 95, "status": "Excellent"},
        {"name": "Bob", "grade": 87, "status": "Good"},
        {"name": "Charlie", "grade": 72, "status": "Average"},
    ]

    # Header
    header = f"{'Name':<15} {'Grade':>10} {'Status':<15}"
    print(header)
    print("-" * 50)

    # Rows
    for student in students:
        row = f"{student['name']:<15} {student['grade']:>10} {student['status']:<15}"
        print(row)

    print("\nGPA Calculation:")
    total = sum(s['grade'] for s in students)
    average = total / len(students)
    print(f"Average Grade: {average:.2f}")

    print("\nExplanation:")
    print("• Formatted string output for tables")
    print("• < left-align, > right-align")
    print("• Number formatting with precision")
    print("• Practical report generation")
    print()

    # ============================================================================
    # SUMMARY
    # ============================================================================

    print("=" * 70)
    print("SUMMARY - PYTHON STRINGS")
    print("=" * 70)
    print("""
    Key Takeaways:

    1. Creation: Single, double, or triple quotes
    2. Indexing: Positive (0, 1, 2...) and negative (-1, -2, -3...)
    3. Slicing: [start:stop:step] for extracting substrings
    4. Operations: + (concatenate), * (repeat), in (membership)
    5. Methods: 40+ built-in methods for manipulation
    6. Formatting: f-strings (modern), .format(), % (legacy)
    7. Immutability: Strings cannot be modified in place
    8. Validation: isalpha(), isdigit(), isalnum(), etc.

    Essential Methods to Remember:
    • .upper(), .lower(), .title()
    • .strip(), .lstrip(), .rstrip()
    • .split(), .join()
    • .replace()
    • .startswith(), .endswith()
    • .find(), .count()

    Best Practices:
    ✓ Use f-strings for formatting
    ✓ Strip user input
    ✓ Use raw strings for paths/regex
    ✓ Join lists, don't concatenate in loops
    ✓ Validate before processing
    """)

    print("=" * 70)
    print("Next: Practice with exercises in 03_strings_exercises.py")
    print("=" * 70)
