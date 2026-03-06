"""
Python Regular Expressions - Tutorial 01: Basics
=================================================

LEARNING OBJECTIVES:
-------------------
1. Understand what regular expressions are and why they're useful
2. Learn the basic re module functions: match(), search(), findall()
3. Create simple literal patterns
4. Work with match objects
5. Understand the difference between match() and search()

PREREQUISITES:
-------------
- Basic Python string operations
- Basic understanding of functions
- Familiarity with True/False boolean values

DIFFICULTY: BEGINNER
"""

import re  # Import the regular expressions module

# ==============================================================================
# SECTION 1: WHAT ARE REGULAR EXPRESSIONS?
# ==============================================================================

if __name__ == "__main__":

    """
    Regular expressions (regex) are powerful patterns used to match text.
    Think of them as a "search language" for strings.

    WHY USE REGEX?
    - Find patterns in text (e.g., all email addresses)
    - Validate input (e.g., check if a string is a valid phone number)
    - Extract information (e.g., get all dates from a document)
    - Replace text (e.g., format phone numbers consistently)
    - Split strings based on complex patterns

    WHEN NOT TO USE REGEX:
    - Simple string operations (use .startswith(), .endswith(), .find() instead)
    - When readability matters more than flexibility
    - When parsing complex structured data (use proper parsers)
    """

    # ==============================================================================
    # SECTION 2: BASIC PATTERN MATCHING WITH re.match()
    # ==============================================================================

    """
    re.match() checks if the BEGINNING of a string matches a pattern.
    If it matches, it returns a Match object; otherwise, it returns None.

    Syntax: re.match(pattern, string)
    """

    # Example 1: Simple literal matching
    # ----------------------------------
    # Let's search for the exact word "hello" at the start of a string

    text1 = "hello world"
    pattern1 = "hello"

    # Try to match the pattern at the beginning of the string
    match_result = re.match(pattern1, text1)

    # Check if we found a match
    if match_result:
        print(f"✓ Pattern '{pattern1}' found at the beginning!")
        print(f"  Matched text: '{match_result.group()}'")  # group() returns the matched text
    else:
        print(f"✗ Pattern '{pattern1}' not found at the beginning")

    print()

    # Example 2: re.match() only checks the BEGINNING
    # -----------------------------------------------
    text2 = "goodbye hello world"
    pattern2 = "hello"

    match_result2 = re.match(pattern2, text2)

    if match_result2:
        print(f"✓ Pattern '{pattern2}' found at the beginning!")
    else:
        # This will print because "hello" is NOT at the start
        print(f"✗ Pattern '{pattern2}' not found at the beginning")
        print(f"  (Note: '{pattern2}' exists in the string, but not at the start)")

    print()

    # ==============================================================================
    # SECTION 3: SEARCHING ANYWHERE WITH re.search()
    # ==============================================================================

    """
    re.search() finds the pattern ANYWHERE in the string (not just at the beginning).
    It returns the FIRST match found, or None if no match exists.

    Syntax: re.search(pattern, string)
    """

    # Example 3: Using re.search() to find patterns anywhere
    # ------------------------------------------------------
    text3 = "goodbye hello world"
    pattern3 = "hello"

    # Search for the pattern anywhere in the string
    search_result = re.search(pattern3, text3)

    if search_result:
        print(f"✓ Pattern '{pattern3}' found in the string!")
        print(f"  Matched text: '{search_result.group()}'")
        print(f"  Position: starts at index {search_result.start()}, ends at index {search_result.end()}")
    else:
        print(f"✗ Pattern '{pattern3}' not found")

    print()

    # Example 4: Comparing re.match() vs re.search()
    # ----------------------------------------------
    test_string = "The cat is on the mat"
    pattern = "cat"

    # Using re.match() - checks only the beginning
    match_obj = re.match(pattern, test_string)
    print(f"re.match() result: {match_obj}")  # Will be None

    # Using re.search() - checks entire string
    search_obj = re.search(pattern, test_string)
    print(f"re.search() result: {search_obj}")  # Will find "cat"

    if search_obj:
        print(f"Found '{pattern}' at position {search_obj.start()}")

    print()

    # ==============================================================================
    # SECTION 4: FINDING ALL MATCHES WITH re.findall()
    # ==============================================================================

    """
    re.findall() returns a LIST of all non-overlapping matches.
    Unlike match() and search() which return Match objects, findall() returns strings.

    Syntax: re.findall(pattern, string)
    """

    # Example 5: Finding all occurrences of a pattern
    # -----------------------------------------------
    text4 = "cat bat rat cat mat cat"
    pattern4 = "cat"

    # Find all occurrences of "cat"
    all_matches = re.findall(pattern4, text4)

    print(f"Pattern '{pattern4}' in text: '{text4}'")
    print(f"All matches: {all_matches}")
    print(f"Number of matches: {len(all_matches)}")

    print()

    # Example 6: Finding all occurrences of different words
    # -----------------------------------------------------
    text5 = "I love Python. Python is great. Everyone should learn Python!"
    pattern5 = "Python"

    python_count = re.findall(pattern5, text5)
    print(f"The word '{pattern5}' appears {len(python_count)} times")
    print(f"Matches: {python_count}")

    print()

    # ==============================================================================
    # SECTION 5: UNDERSTANDING MATCH OBJECTS
    # ==============================================================================

    """
    When re.match() or re.search() finds a match, they return a Match object.
    This object contains useful information about the match:

    - .group()    : Returns the matched text
    - .start()    : Returns the starting position of the match
    - .end()      : Returns the ending position of the match
    - .span()     : Returns a tuple (start, end)
    - .string     : Returns the original string that was searched
    """

    # Example 7: Exploring Match object properties
    # --------------------------------------------
    text6 = "Find the needle in the haystack"
    pattern6 = "needle"

    match = re.search(pattern6, text6)

    if match:
        print("Match object properties:")
        print(f"  Matched text: '{match.group()}'")
        print(f"  Start position: {match.start()}")
        print(f"  End position: {match.end()}")
        print(f"  Span (start, end): {match.span()}")
        print(f"  Original string: '{match.string}'")

        # We can also use slicing to verify
        start, end = match.span()
        print(f"  Verification: text[{start}:{end}] = '{text6[start:end]}'")

    print()

    # ==============================================================================
    # SECTION 6: CASE SENSITIVITY
    # ==============================================================================

    """
    By default, regular expressions are CASE-SENSITIVE.
    "Hello" and "hello" are treated as different patterns.
    """

    # Example 8: Case-sensitive matching
    # ----------------------------------
    text7 = "Hello World"

    # This will match
    match_lower = re.search("Hello", text7)
    print(f"Searching for 'Hello': {'Found' if match_lower else 'Not found'}")

    # This will NOT match (different case)
    match_upper = re.search("hello", text7)
    print(f"Searching for 'hello': {'Found' if match_upper else 'Not found'}")

    print()

    # We'll learn how to do case-insensitive matching in later tutorials
    # (Hint: use the re.IGNORECASE flag)

    # ==============================================================================
    # SECTION 7: SPECIAL CHARACTERS IN LITERALS
    # ==============================================================================

    """
    Some characters have special meaning in regex (like . * + ? etc.).
    To match them literally, we need to ESCAPE them with a backslash \.

    In Python, we use RAW STRINGS (r"pattern") to avoid double-escaping.
    """

    # Example 9: Matching special characters literally
    # ------------------------------------------------

    # Wrong way: Without raw string or proper escaping
    text8 = "My email is user@example.com"

    # To match a literal period '.', we need to escape it
    # Using raw string (recommended)
    pattern8 = r"\."  # Matches a literal period

    matches = re.findall(pattern8, text8)
    print(f"Periods found in '{text8}': {matches}")
    print(f"Number of periods: {len(matches)}")

    print()

    # Example 10: Why use raw strings?
    # --------------------------------
    # Without raw string: need double backslash
    pattern_without_raw = "\\."  # Need \\ to get one \

    # With raw string: single backslash (preferred)
    pattern_with_raw = r"\."  # More readable

    text9 = "3.14 is pi"
    print(f"Without raw string: {re.findall(pattern_without_raw, text9)}")
    print(f"With raw string: {re.findall(pattern_with_raw, text9)}")

    print()

    # ==============================================================================
    # SECTION 8: PRACTICAL EXAMPLES
    # ==============================================================================

    # Example 11: Simple email detection (simplified version)
    # ------------------------------------------------------
    email_text = "Contact us at support@company.com or sales@company.com"

    # For now, we'll just look for the @ symbol (we'll improve this later)
    at_symbols = re.findall("@", email_text)
    print(f"Potential email addresses (@ symbols found): {len(at_symbols)}")

    print()

    # Example 12: Finding specific words in a document
    # -----------------------------------------------
    document = """
    Python is a high-level programming language.
    Python is widely used in web development, data science, and automation.
    Learning Python is a great investment in your programming career.
    """

    # Count occurrences of "Python"
    python_matches = re.findall("Python", document)
    print(f"Word 'Python' appears {len(python_matches)} times in the document")

    # Find the first occurrence
    first_python = re.search("Python", document)
    if first_python:
        print(f"First occurrence at position: {first_python.start()}")

    print()

    # Example 13: Validating exact string match
    # -----------------------------------------
    def check_exact_match(text, pattern):
        """
        Check if the ENTIRE string exactly matches the pattern.
        This is useful for validation (e.g., checking if input is exactly "yes" or "no").
        """
        match = re.match(pattern, text)
        # For exact match, the match should span the entire string
        if match and match.group() == text:
            return True
        return False

    # Test the function
    print("Exact match tests:")
    print(f"  'hello' matches 'hello': {check_exact_match('hello', 'hello')}")
    print(f"  'hello world' matches 'hello': {check_exact_match('hello world', 'hello')}")
    print(f"  'hi' matches 'hello': {check_exact_match('hi', 'hello')}")

    print()

    # ==============================================================================
    # SECTION 9: COMMON PATTERNS TO REMEMBER
    # ==============================================================================

    print("="*70)
    print("SUMMARY: KEY POINTS TO REMEMBER")
    print("="*70)

    summary = """
    1. re.match(pattern, string)
       - Checks if pattern matches at the BEGINNING of string
       - Returns Match object or None

    2. re.search(pattern, string)
       - Finds pattern ANYWHERE in string
       - Returns first Match object or None

    3. re.findall(pattern, string)
       - Returns LIST of all matches
       - Returns strings, not Match objects

    4. Match Objects:
       - .group()  : Get matched text
       - .start()  : Get starting position
       - .end()    : Get ending position
       - .span()   : Get (start, end) tuple

    5. Best Practices:
       - Use raw strings: r"pattern"
       - Test patterns with simple examples first
       - Remember: regex is case-sensitive by default
       - Escape special characters with backslash: \.

    6. When to use what:
       - Use re.match() when checking if string STARTS with pattern
       - Use re.search() when looking for pattern ANYWHERE
       - Use re.findall() when you need ALL matches
    """

    print(summary)

    # ==============================================================================
    # PRACTICE EXERCISES
    # ==============================================================================

    print("="*70)
    print("PRACTICE CHALLENGES")
    print("="*70)

    """
    Try these exercises to test your understanding:

    1. Write code to check if a string starts with "Error:"
    2. Find all occurrences of the word "test" in a long string
    3. Check if the word "password" appears anywhere in a string
    4. Count how many times "the" appears in a paragraph
    5. Extract the position of the first occurrence of "Python" in a text

    Solutions can be found in exercises_01_basics.py
    """

    # ==============================================================================
    # END OF TUTORIAL 01
    # ==============================================================================

    print("\n" + "="*70)
    print("END OF TUTORIAL - You've learned the basics of regex in Python!")
    print("Next: Tutorial 02 - Character Classes")
    print("="*70)
