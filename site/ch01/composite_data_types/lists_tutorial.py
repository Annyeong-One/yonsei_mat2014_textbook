"""
PYTHON LISTS - COMPLETE TUTORIAL
==================================

Lists are ordered, mutable collections that can contain elements of different types.
They are one of the most versatile and commonly used data structures in Python.
"""

# =============================================================================
# 1. CREATING LISTS
# =============================================================================

# Empty list

if __name__ == "__main__":
    empty_list = []
    also_empty = list()

    # List with initial values
    numbers = [1, 2, 3, 4, 5]
    fruits = ["apple", "banana", "cherry"]
    mixed = [1, "hello", 3.14, True, [1, 2, 3]]  # Can contain different types

    # Using list() constructor
    from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
    from_range = list(range(5))  # [0, 1, 2, 3, 4]
    from_tuple = list((1, 2, 3, 4, 5))

    print("Basic lists created:")
    print(f"Numbers: {numbers}")
    print(f"Fruits: {fruits}")
    print(f"Mixed: {mixed}")
    print()

    # =============================================================================
    # 2. ACCESSING ELEMENTS (INDEXING)
    # =============================================================================

    letters = ['a', 'b', 'c', 'd', 'e']

    # Positive indexing (starts at 0)
    print("Indexing:")
    print(f"First element: {letters[0]}")    # 'a'
    print(f"Third element: {letters[2]}")    # 'c'

    # Negative indexing (starts from end)
    print(f"Last element: {letters[-1]}")    # 'e'
    print(f"Second to last: {letters[-2]}")  # 'd'
    print()

    # =============================================================================
    # 3. SLICING
    # =============================================================================

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("Slicing [start:stop:step]:")
    print(f"First 5: {numbers[:5]}")          # [0, 1, 2, 3, 4]
    print(f"Last 5: {numbers[-5:]}")          # [5, 6, 7, 8, 9]
    print(f"Middle: {numbers[3:7]}")          # [3, 4, 5, 6]
    print(f"Every 2nd: {numbers[::2]}")       # [0, 2, 4, 6, 8]
    print(f"Reverse: {numbers[::-1]}")        # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print()

    # =============================================================================
    # 4. MODIFYING LISTS (MUTABILITY)
    # =============================================================================

    fruits = ["apple", "banana", "cherry"]

    # Changing an element
    fruits[1] = "blueberry"
    print(f"After modification: {fruits}")

    # Changing multiple elements
    numbers = [1, 2, 3, 4, 5]
    numbers[1:4] = [20, 30, 40]
    print(f"Multiple changes: {numbers}")
    print()

    # =============================================================================
    # 5. ADDING ELEMENTS
    # =============================================================================

    fruits = ["apple", "banana"]

    # append() - adds single element to end
    fruits.append("cherry")
    print(f"After append: {fruits}")

    # insert() - adds element at specific position
    fruits.insert(1, "blueberry")
    print(f"After insert: {fruits}")

    # extend() - adds multiple elements to end
    fruits.extend(["date", "elderberry"])
    print(f"After extend: {fruits}")

    # Using + operator
    more_fruits = fruits + ["fig", "grape"]
    print(f"Using + operator: {more_fruits}")

    # Using * operator for repetition
    repeated = [1, 2, 3] * 3
    print(f"Repeated list: {repeated}")
    print()

    # =============================================================================
    # 6. REMOVING ELEMENTS
    # =============================================================================

    numbers = [1, 2, 3, 4, 5, 3, 6, 3]

    # remove() - removes first occurrence of value
    numbers_copy = numbers.copy()
    numbers_copy.remove(3)
    print(f"After remove(3): {numbers_copy}")  # First 3 is removed

    # pop() - removes and returns element at index (default: last)
    numbers_copy = numbers.copy()
    last = numbers_copy.pop()
    print(f"Popped: {last}, Remaining: {numbers_copy}")

    second = numbers_copy.pop(1)
    print(f"Popped index 1: {second}, Remaining: {numbers_copy}")

    # del statement - removes by index or slice
    numbers_copy = numbers.copy()
    del numbers_copy[0]
    print(f"After del [0]: {numbers_copy}")

    del numbers_copy[1:3]
    print(f"After del [1:3]: {numbers_copy}")

    # clear() - removes all elements
    numbers_copy = numbers.copy()
    numbers_copy.clear()
    print(f"After clear(): {numbers_copy}")
    print()

    # =============================================================================
    # 7. LIST METHODS
    # =============================================================================

    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    # count() - counts occurrences
    print(f"Count of 5: {numbers.count(5)}")

    # index() - finds first index of value
    print(f"Index of 9: {numbers.index(9)}")

    # You can also specify start and end for index()
    print(f"Index of 5 after position 4: {numbers.index(5, 4)}")

    # sort() - sorts in place
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    print(f"After sort(): {numbers_copy}")

    numbers_copy.sort(reverse=True)
    print(f"Reverse sort: {numbers_copy}")

    # Custom sorting with key
    words = ["banana", "pie", "Washington", "book"]
    words.sort(key=len)
    print(f"Sorted by length: {words}")

    # reverse() - reverses in place
    numbers_copy = numbers.copy()
    numbers_copy.reverse()
    print(f"After reverse(): {numbers_copy}")

    # copy() - creates shallow copy
    numbers_copy = numbers.copy()
    print(f"Copy created: {numbers_copy}")
    print()

    # =============================================================================
    # 8. SEARCHING AND CHECKING
    # =============================================================================

    fruits = ["apple", "banana", "cherry", "date"]

    # Checking membership
    print(f"'banana' in fruits: {'banana' in fruits}")
    print(f"'grape' not in fruits: {'grape' not in fruits}")

    # Length
    print(f"Length of fruits: {len(fruits)}")

    # Min, Max, Sum (for comparable/numeric elements)
    numbers = [45, 23, 67, 12, 89, 34]
    print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")

    # Finding index of max/min
    print(f"Index of max: {numbers.index(max(numbers))}")
    print()

    # =============================================================================
    # 9. ITERATING THROUGH LISTS
    # =============================================================================

    fruits = ["apple", "banana", "cherry"]

    # Basic iteration
    print("Basic iteration:")
    for fruit in fruits:
        print(f"  {fruit}")

    # With index using enumerate()
    print("\nWith index:")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")

    # With custom start index
    print("\nCustom start index:")
    for index, fruit in enumerate(fruits, start=1):
        print(f"  {index}. {fruit}")

    # Iterating backwards
    print("\nBackwards:")
    for fruit in reversed(fruits):
        print(f"  {fruit}")
    print()

    # =============================================================================
    # 10. LIST COMPREHENSIONS
    # =============================================================================

    # Basic list comprehension
    squares = [x**2 for x in range(10)]
    print(f"Squares: {squares}")

    # With condition
    evens = [x for x in range(20) if x % 2 == 0]
    print(f"Evens: {evens}")

    # With if-else
    labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
    print(f"Labels: {labels}")

    # Nested comprehension
    matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
    print(f"Matrix:\n{matrix}")

    # From string
    chars = [char.upper() for char in "hello"]
    print(f"Uppercase chars: {chars}")

    # Multiple conditions
    numbers = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
    print(f"Divisible by 2 and 5: {numbers}")
    print()

    # =============================================================================
    # 11. NESTED LISTS
    # =============================================================================

    # 2D list (matrix)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Nested list access:")
    print(f"Element at [0][0]: {matrix[0][0]}")  # 1
    print(f"Element at [1][2]: {matrix[1][2]}")  # 6
    print(f"Second row: {matrix[1]}")            # [4, 5, 6]

    print("\nIterating nested list:")
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

    # More complex nested structure
    nested = [[1, 2], [3, 4, 5], [6]]
    print(f"\nIrregular nested list: {nested}")
    print()

    # =============================================================================
    # 12. UNPACKING LISTS
    # =============================================================================

    numbers = [1, 2, 3]
    a, b, c = numbers
    print(f"Unpacked: a={a}, b={b}, c={c}")

    # With * operator (Python 3+)
    first, *middle, last = [1, 2, 3, 4, 5]
    print(f"first={first}, middle={middle}, last={last}")

    # Swapping values
    x, y = 10, 20
    x, y = y, x
    print(f"Swapped: x={x}, y={y}")
    print()

    # =============================================================================
    # 13. COMMON PATTERNS AND TIPS
    # =============================================================================

    # Creating a list of n identical elements
    zeros = [0] * 5
    print(f"Five zeros: {zeros}")

    # Creating a 2D list (be careful!)
    # Wrong way (creates shallow copy)
    wrong_matrix = [[0] * 3] * 3  # All rows point to same list!
    wrong_matrix[0][0] = 1
    print(f"Wrong matrix: {wrong_matrix}")  # All rows changed!

    # Right way
    right_matrix = [[0] * 3 for _ in range(3)]
    right_matrix[0][0] = 1
    print(f"Right matrix: {right_matrix}")  # Only first row changed

    # Flattening a list of lists
    nested = [[1, 2], [3, 4], [5, 6]]
    flattened = [item for sublist in nested for item in sublist]
    print(f"Flattened: {flattened}")

    # Removing duplicates (preserving order)
    numbers = [1, 2, 3, 2, 4, 3, 5]
    unique = list(dict.fromkeys(numbers))
    print(f"Unique (ordered): {unique}")

    # Finding common elements
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common = [x for x in list1 if x in list2]
    print(f"Common elements: {common}")

    # Splitting a list into chunks
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Chunks of 3: {list(chunks(numbers, 3))}")

    # Zipping lists together
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    combined = list(zip(names, ages))
    print(f"Zipped: {combined}")

    # Filtering with filter()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Filtered evens: {evens}")

    # Mapping with map()
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(f"Mapped squares: {squared}")
    print()

    # =============================================================================
    # 14. COPYING LISTS
    # =============================================================================

    original = [1, 2, 3, 4, 5]

    # Reference (NOT a copy!)
    reference = original
    reference[0] = 99
    print(f"Original after reference change: {original}")  # Changed!

    # Shallow copy (copy top level)
    original = [1, 2, 3, 4, 5]
    shallow = original.copy()  # or original[:] or list(original)
    shallow[0] = 99
    print(f"Original after shallow copy change: {original}")  # Not changed

    # Deep copy (for nested structures)
    import copy
    nested_original = [[1, 2], [3, 4]]
    deep = copy.deepcopy(nested_original)
    deep[0][0] = 99
    print(f"Original nested after deep copy change: {nested_original}")  # Not changed
    print()

    # =============================================================================
    # 15. PERFORMANCE NOTES
    # =============================================================================

    """
    Operation           | Time Complexity
    --------------------|----------------
    Access by index     | O(1)
    Append to end       | O(1) amortized
    Insert at beginning | O(n)
    Insert at middle    | O(n)
    Remove from end     | O(1)
    Remove from middle  | O(n)
    Search for element  | O(n)
    Slice               | O(k) where k is slice length
    Copy                | O(n)
    Sort                | O(n log n)
    Reverse             | O(n)

    Tips for Performance:
    - Use list comprehensions instead of loops when possible (faster)
    - Append to end instead of inserting at beginning
    - Use collections.deque for frequent insertions/removals at both ends
    - Pre-allocate list size if known
    """

    # =============================================================================
    # 16. WHEN TO USE LISTS
    # =============================================================================

    """
    Use LISTS when:
    - You need ordered sequences
    - You need to access by numeric index
    - You need to sort or reverse easily
    - You need to store duplicates
    - You need to modify elements
    - You need dynamic resizing

    Don't use LISTS for:
    - Fast membership testing (use sets)
    - Key-value associations (use dictionaries)
    - Immutable sequences (use tuples)
    - Large datasets where memory matters (use arrays or numpy)
    """

    print("=" * 60)
    print("TUTORIAL COMPLETE!")
    print("Lists are fundamental - practice with the exercises!")
    print("=" * 60)
