"""
PYTHON SETS - COMPLETE TUTORIAL
================================

Sets are unordered collections of unique elements. They're perfect for 
membership testing, removing duplicates, and mathematical set operations.
"""

# =============================================================================
# 1. CREATING SETS
# =============================================================================

# Empty set (note: {} creates a dict, not a set!)
empty_set = set()
print(f"Empty set: {empty_set}, type: {type(empty_set)}")

# NOT a set!
not_a_set = {}
print(f"Empty dict: {not_a_set}, type: {type(not_a_set)}")

# Set with initial values
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}

# Using set() constructor
from_list = set([1, 2, 3, 2, 1])  # Duplicates removed!
from_string = set("hello")  # {'h', 'e', 'l', 'o'}
from_tuple = set((1, 2, 3, 4, 5))

# Duplicates are automatically removed
with_duplicates = {1, 2, 2, 3, 3, 3, 4, 5}
print(f"Duplicates removed: {with_duplicates}")

print("\nBasic sets created:")
print(f"Numbers: {numbers}")
print(f"From list: {from_list}")
print(f"From string: {from_string}")
print()

# =============================================================================
# 2. BASIC SET OPERATIONS
# =============================================================================

fruits = {"apple", "banana", "cherry"}

# Adding elements
fruits.add("date")
print(f"After add: {fruits}")

# Adding multiple elements
fruits.update(["elderberry", "fig"])
print(f"After update: {fruits}")

# Removing elements
fruits.remove("banana")  # Raises KeyError if not found
print(f"After remove: {fruits}")

fruits.discard("grape")  # Does NOT raise error if not found
print(f"After discard (grape not in set): {fruits}")

# Pop - removes and returns arbitrary element
popped = fruits.pop()
print(f"Popped: {popped}, Remaining: {fruits}")

# Clear - removes all elements
numbers = {1, 2, 3}
numbers.clear()
print(f"After clear: {numbers}")
print()

# =============================================================================
# 3. SET MEMBERSHIP TESTING
# =============================================================================

fruits = {"apple", "banana", "cherry"}

# Check if element exists (very fast - O(1))
print("Membership testing:")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# Length
print(f"Number of fruits: {len(fruits)}")
print()

# =============================================================================
# 4. SET MATHEMATICAL OPERATIONS
# =============================================================================

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("Set A:", a)
print("Set B:", b)
print()

# UNION - all elements from both sets
union1 = a | b
union2 = a.union(b)
print(f"Union (A | B): {union1}")
print(f"Union (A.union(B)): {union2}")

# INTERSECTION - elements in both sets
intersection1 = a & b
intersection2 = a.intersection(b)
print(f"Intersection (A & B): {intersection1}")
print(f"Intersection (A.intersection(B)): {intersection2}")

# DIFFERENCE - elements in A but not in B
difference1 = a - b
difference2 = a.difference(b)
print(f"Difference (A - B): {difference1}")
print(f"Difference (A.difference(B)): {difference2}")

# SYMMETRIC DIFFERENCE - elements in A or B, but not both
sym_diff1 = a ^ b
sym_diff2 = a.symmetric_difference(b)
print(f"Symmetric Difference (A ^ B): {sym_diff1}")
print(f"Symmetric Difference (A.symmetric_difference(B)): {sym_diff2}")
print()

# =============================================================================
# 5. SET COMPARISON OPERATIONS
# =============================================================================

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {1, 2, 3}
d = {4, 5, 6}

print("Set comparisons:")
print(f"A: {a}")
print(f"B: {b}")
print(f"C: {c}")
print(f"D: {d}")
print()

# SUBSET - all elements of A are in B
print(f"A is subset of B (A <= B): {a <= b}")
print(f"A is subset of B (A.issubset(B)): {a.issubset(b)}")

# PROPER SUBSET - subset but not equal
print(f"A is proper subset of B (A < B): {a < b}")

# SUPERSET - B contains all elements of A
print(f"B is superset of A (B >= A): {b >= a}")
print(f"B is superset of A (B.issuperset(A)): {b.issuperset(a)}")

# PROPER SUPERSET
print(f"B is proper superset of A (B > A): {b > a}")

# EQUALITY
print(f"A equals C (A == C): {a == c}")

# DISJOINT - no common elements
print(f"A and D are disjoint (A.isdisjoint(D)): {a.isdisjoint(d)}")
print()

# =============================================================================
# 6. MODIFYING SETS IN-PLACE
# =============================================================================

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Update (union in-place)
a_copy = a.copy()
a_copy.update(b)
print(f"After update: {a_copy}")  # Same as a |= b

# Intersection update
a_copy = a.copy()
a_copy.intersection_update(b)
print(f"After intersection_update: {a_copy}")  # Same as a &= b

# Difference update
a_copy = a.copy()
a_copy.difference_update(b)
print(f"After difference_update: {a_copy}")  # Same as a -= b

# Symmetric difference update
a_copy = a.copy()
a_copy.symmetric_difference_update(b)
print(f"After symmetric_difference_update: {a_copy}")  # Same as a ^= b
print()

# =============================================================================
# 7. SET COMPREHENSIONS
# =============================================================================

# Basic set comprehension
squares = {x**2 for x in range(10)}
print(f"Squares: {squares}")

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From string (remove duplicates)
unique_chars = {char.lower() for char in "Hello World"}
print(f"Unique chars: {unique_chars}")

# Complex comprehension
words = ["apple", "banana", "cherry", "apricot", "blueberry"]
long_words = {word.upper() for word in words if len(word) > 5}
print(f"Long words (uppercase): {long_words}")
print()

# =============================================================================
# 8. FROZENSET (IMMUTABLE SETS)
# =============================================================================

# Frozensets are immutable - can't be modified after creation
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {frozen}")

# Can be used as dictionary keys or set elements
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set of frozensets: {set_of_sets}")

dict_with_set_keys = {frozenset([1, 2]): "value1", frozenset([3, 4]): "value2"}
print(f"Dict with frozenset keys: {dict_with_set_keys}")

# Frozensets support all set operations except modifications
frozen_a = frozenset([1, 2, 3])
frozen_b = frozenset([2, 3, 4])
print(f"Frozen union: {frozen_a | frozen_b}")
print(f"Frozen intersection: {frozen_a & frozen_b}")

# Cannot modify frozenset
try:
    frozen.add(6)
except AttributeError as e:
    print(f"Error: frozenset is immutable - {e}")
print()

# =============================================================================
# 9. ITERATING THROUGH SETS
# =============================================================================

fruits = {"apple", "banana", "cherry", "date"}

# Basic iteration (order is not guaranteed!)
print("Iterating through set:")
for fruit in fruits:
    print(f"  {fruit}")

# With enumerate (not very useful since sets are unordered)
print("\nWith enumerate:")
for i, fruit in enumerate(sorted(fruits)):
    print(f"  {i}: {fruit}")
print()

# =============================================================================
# 10. PRACTICAL USES OF SETS
# =============================================================================

# 1. REMOVING DUPLICATES
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers))
print(f"Remove duplicates: {unique_numbers}")

# 2. MEMBERSHIP TESTING (very fast!)
valid_users = {"alice", "bob", "charlie", "diana"}
user = "bob"
if user in valid_users:
    print(f"{user} is a valid user")

# 3. FINDING COMMON ELEMENTS
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"Common elements: {common}")

# 4. FINDING UNIQUE ELEMENTS
only_in_list1 = set(list1) - set(list2)
print(f"Only in list1: {only_in_list1}")

# 5. CHECKING IF LISTS HAVE ANY COMMON ELEMENTS
if not set(list1).isdisjoint(list2):
    print("Lists have common elements")

# 6. COMBINING UNIQUE ELEMENTS
all_elements = set(list1) | set(list2)
print(f"All unique elements: {all_elements}")
print()

# =============================================================================
# 11. COMMON PATTERNS AND TIPS
# =============================================================================

# Pattern 1: Remove duplicates while preserving some order
def remove_duplicates_ordered(items):
    """Remove duplicates while preserving first occurrence order"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"Ordered unique: {remove_duplicates_ordered(nums)}")

# Pattern 2: Find elements that appear in all lists
lists = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
common_to_all = set(lists[0])
for lst in lists[1:]:
    common_to_all &= set(lst)
print(f"Common to all lists: {common_to_all}")

# Pattern 3: Count unique elements
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
unique_count = len(set(words))
print(f"Unique word count: {unique_count}")

# Pattern 4: Check if list has duplicates
def has_duplicates(items):
    return len(items) != len(set(items))

print(f"Has duplicates: {has_duplicates([1, 2, 3, 2])}")
print(f"No duplicates: {has_duplicates([1, 2, 3, 4])}")

# Pattern 5: Venn diagram data
group_a = {"Alice", "Bob", "Charlie", "Diana"}
group_b = {"Charlie", "Diana", "Eve", "Frank"}
only_a = group_a - group_b
only_b = group_b - group_a
both = group_a & group_b
print(f"Only in A: {only_a}")
print(f"Only in B: {only_b}")
print(f"In both: {both}")
print()

# =============================================================================
# 12. SET METHODS SUMMARY
# =============================================================================

print("=" * 60)
print("SET METHODS SUMMARY")
print("=" * 60)

methods_summary = """
ADDING/REMOVING:
  add(item)              - Add single element
  update(items)          - Add multiple elements
  remove(item)           - Remove element (raises KeyError if not found)
  discard(item)          - Remove element (no error if not found)
  pop()                  - Remove and return arbitrary element
  clear()                - Remove all elements

SET OPERATIONS (return new set):
  union(other)                    - A | B
  intersection(other)             - A & B
  difference(other)               - A - B
  symmetric_difference(other)     - A ^ B

IN-PLACE OPERATIONS (modify set):
  update(other)                      - A |= B
  intersection_update(other)         - A &= B
  difference_update(other)           - A -= B
  symmetric_difference_update(other) - A ^= B

COMPARISONS:
  issubset(other)        - A <= B
  issuperset(other)      - A >= B
  isdisjoint(other)      - No common elements

OTHER:
  copy()                 - Shallow copy
  len(s)                 - Number of elements
  item in s              - Membership test
"""

print(methods_summary)

# =============================================================================
# 13. PERFORMANCE NOTES
# =============================================================================

print("=" * 60)
print("PERFORMANCE CHARACTERISTICS")
print("=" * 60)

performance_notes = """
Operation               | Average | Worst Case
------------------------|---------|------------
Add element             | O(1)    | O(n)
Remove element          | O(1)    | O(n)
Check membership        | O(1)    | O(n)
Union (|)               | O(len(A) + len(B))
Intersection (&)        | O(min(len(A), len(B)))
Difference (-)          | O(len(A))
Symmetric difference    | O(len(A) + len(B))

Key Points:
- Sets use hash tables internally
- Elements must be hashable (immutable)
- Much faster than lists for membership testing
- No indexing or slicing (unordered)
- Great for mathematical set operations
"""

print(performance_notes)

# =============================================================================
# 14. WHEN TO USE SETS
# =============================================================================

print("=" * 60)
print("WHEN TO USE SETS")
print("=" * 60)

when_to_use = """
Use SETS when:
- You need to eliminate duplicates
- You need fast membership testing (item in set)
- You need to perform mathematical set operations
- Order doesn't matter
- You're tracking unique items
- You need to find common/different elements between collections

Use LISTS when:
- Order matters
- You need indexing/slicing
- You need to store duplicates
- You need to sort easily

Use DICTIONARIES when:
- You need key-value associations
- You need to map between data

Don't use SETS for:
- Storing mutable objects (lists, dicts, other sets)
- When you need to maintain order (use list or OrderedDict)
- When you need to access by index
"""

print(when_to_use)

# =============================================================================
# 15. COMMON MISTAKES
# =============================================================================

print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)

# Mistake 1: Creating empty set
wrong = {}  # This is a dict!
right = set()  # This is a set!
print(f"Type of {{}}: {type(wrong)}")
print(f"Type of set(): {type(right)}")

# Mistake 2: Trying to add unhashable items
try:
    my_set = {1, 2, 3}
    my_set.add([4, 5])  # Lists are not hashable!
except TypeError as e:
    print(f"Error: {e}")

# Mistake 3: Assuming sets maintain order (though Python 3.7+ dicts do)
# Sets are still unordered by design
s = {3, 1, 4, 1, 5, 9}
print(f"Set (order not guaranteed): {s}")

# Mistake 4: Using remove instead of discard
try:
    my_set = {1, 2, 3}
    my_set.remove(4)  # Raises KeyError
except KeyError:
    print("KeyError: use discard() if you're not sure element exists")

# Correct way
my_set.discard(4)  # No error
print()

print("=" * 60)
print("TUTORIAL COMPLETE!")
print("Sets are powerful for unique collections and set operations!")
print("=" * 60)
