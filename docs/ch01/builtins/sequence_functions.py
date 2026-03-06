"""
04_sequence_functions.py - Sequence Built-in Functions
len(), range(), sorted(), reversed(), all(), any()
"""

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    print("=" * 70)
    print("SEQUENCE BUILT-IN FUNCTIONS")
    print("=" * 70)

    # len() - Length of sequence
    print("\n1. len() - Length")
    my_list = [1, 2, 3, 4, 5]
    my_string = "Python"
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    print(f"len({my_list}) = {len(my_list)}")
    print(f"len('{my_string}') = {len(my_string)}")
    print(f"len({my_dict}) = {len(my_dict)}")

    # range() - Generate sequence of numbers
    print("\n2. range() - Number Sequence")
    print(f"range(5): {list(range(5))}")              # 0 to 4
    print(f"range(1, 6): {list(range(1, 6))}")        # 1 to 5
    print(f"range(0, 10, 2): {list(range(0, 10, 2))}")  # Even numbers

    # sorted() - Return sorted copy
    print("\n3. sorted() - Sort (returns new list)")
    numbers = [3, 1, 4, 1, 5, 9, 2]
    print(f"Original: {numbers}")
    print(f"sorted(): {sorted(numbers)}")
    print(f"Original unchanged: {numbers}")
    print(f"Reverse sorted: {sorted(numbers, reverse=True)}")

    # reversed() - Reverse sequence
    print("\n4. reversed() - Reverse")
    numbers = [1, 2, 3, 4, 5]
    print(f"reversed({numbers}): {list(reversed(numbers))}")
    print(f"reversed('Python'): {list(reversed('Python'))}")

    # all() - Check if all elements are True
    print("\n5. all() - All True?")
    print(f"all([True, True, True]) = {all([True, True, True])}")
    print(f"all([True, False, True]) = {all([True, False, True])}")
    print(f"all([1, 2, 3]) = {all([1, 2, 3])}")  # Non-zero = True
    print(f"all([1, 0, 3]) = {all([1, 0, 3])}")  # 0 = False

    # any() - Check if any element is True
    print("\n6. any() - Any True?")
    print(f"any([False, False, False]) = {any([False, False, False])}")
    print(f"any([False, True, False]) = {any([False, True, False])}")
    print(f"any([0, 0, 1]) = {any([0, 0, 1])}")

    print("\n" + "=" * 70)
    print("PRACTICAL EXAMPLES")
    print("=" * 70)

    # Check password strength
    print("\nExample: Validate password")
    password = "MyPass123"
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    long_enough = len(password) >= 8

    print(f"Password: {password}")
    print(f"Has uppercase: {has_upper}")
    print(f"Has lowercase: {has_lower}")
    print(f"Has digits: {has_digit}")
    print(f"Long enough: {long_enough}")
    print(f"Valid: {all([has_upper, has_lower, has_digit, long_enough])}")

    # Process scores
    print("\nExample: Process test scores")
    scores = [85, 92, 78, 95, 88]
    print(f"Scores: {scores}")
    print(f"Count: {len(scores)}")
    print(f"Sorted: {sorted(scores)}")
    print(f"All passed (>=60): {all(score >= 60 for score in scores)}")
    print(f"Any excellent (>=90): {any(score >= 90 for score in scores)}")

    print("\nSee exercises.py for practice!")
