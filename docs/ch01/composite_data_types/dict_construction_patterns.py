"""
Dictionary Construction Patterns - Building Dicts from Tuples and Sorting Keys
This tutorial demonstrates different ways to construct dictionaries from
sequences and how to control the order of keys through sorting.
Run this file to see dict construction patterns in action!
"""

print("=" * 70)
print("DICTIONARY CONSTRUCTION PATTERNS - EXAMPLES")
print("=" * 70)

# ============================================================================
# EXAMPLE 1: Basic Data - Dial Codes by Country
# ============================================================================
print("\n1. OUR DATA - DIAL CODES FOR MOST POPULOUS COUNTRIES")
print("-" * 70)

# List of tuples: (country_dial_code, country_name)
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

print("\nRaw data structure - list of (code, country) tuples:")
for code, country in DIAL_CODES:
    print(f"  {code:4} -> {country}")

print("\nNOTE: The data is in its original, unsorted order")

# ============================================================================
# EXAMPLE 2: Simple Dict Construction - Order Preserved (Python 3.7+)
# ============================================================================
print("\n2. SIMPLE DICT CONSTRUCTION - dict()")
print("-" * 70)

d1 = dict(DIAL_CODES)

print(f"\nCreated: d1 = dict(DIAL_CODES)")
print(f"\nDictionary d1 - keys in ORIGINAL order:")
for key in d1.keys():
    print(f"  {key:4} -> {d1[key]}")

print("\nWHY THIS MATTERS:")
print("- dict() constructor accepts an iterable of (key, value) pairs")
print("- Python 3.7+ preserves insertion order in dictionaries")
print("- d1 has keys in the same order as the input list")

# ============================================================================
# EXAMPLE 3: Sorted Dict - Sorting by Keys (numeric)
# ============================================================================
print("\n3. SORTED DICT - SORTING BY DIAL CODE (NUMERIC)")
print("-" * 70)

d2 = dict(sorted(DIAL_CODES))

print(f"\nCreated: d2 = dict(sorted(DIAL_CODES))")
print(f"\nDictionary d2 - keys in NUMERIC order:")
for key in d2.keys():
    print(f"  {key:4} -> {d2[key]}")

print("\nWHY THIS MATTERS:")
print("- sorted() on a list of tuples sorts by the FIRST element")
print("- So our tuples are sorted by dial code (86, 1, 7, ...)")
print("- Then dict() is called on the sorted list")
print("- Result: dictionary with keys in numeric order")

# ============================================================================
# EXAMPLE 4: Custom Sort - Sorting by Country Name (alphabetic)
# ============================================================================
print("\n4. SORTED DICT - SORTING BY COUNTRY NAME (CUSTOM)")
print("-" * 70)

# Using key parameter to sort by second element (country name)
d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))

print(f"\nCreated: d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))")
print(f"\nDictionary d3 - keys in ALPHABETIC ORDER by country:")
for key in d3.keys():
    print(f"  {key:4} -> {d3[key]}")

print("\nWHY THIS MATTERS:")
print("- key=lambda x: x[1] tells sorted() to use the 2nd element (country)")
print("- The tuples are reordered by country name (Bangladesh, Brazil, ...)")
print("- But the resulting dict still has the dial CODE as key (not country!)")
print("- This is useful for alphabetically organizing data by values")

# ============================================================================
# EXAMPLE 5: Comparing the Dictionaries
# ============================================================================
print("\n5. COMPARING THE THREE DICTIONARIES")
print("-" * 70)

print(f"\nd1 == d2: {d1 == d2}")
print(f"d2 == d3: {d2 == d3}")
print(f"d1 == d3: {d1 == d3}")

print("\nWHY THEY'RE EQUAL:")
print("- All three dictionaries have the SAME KEY-VALUE PAIRS")
print("- They only differ in the order of keys")
print("- In Python 3.7+, order is preserved but doesn't affect equality")
print("- {1: 'USA', 86: 'China'} == {86: 'China', 1: 'USA'} is True")

# ============================================================================
# EXAMPLE 6: Practical Example - Building a Lookup Table
# ============================================================================
print("\n6. PRACTICAL EXAMPLE - PHONE NUMBER LOOKUP")
print("-" * 70)

# Using d2 (sorted by dial code) for faster lookup of similar codes
def lookup_country(dial_code, codes_dict):
    """Look up country by dial code."""
    return codes_dict.get(dial_code, "Unknown country")

test_codes = [1, 86, 555, 91]

print(f"\nUsing d2 (sorted by dial code) to look up countries:")
for code in test_codes:
    country = lookup_country(code, d2)
    print(f"  Dial code {code:4} -> {country}")

print("\nKEY INSIGHTS ABOUT DICT CONSTRUCTION:")
print("- Use dict(iterable) for simple key-value pair conversion")
print("- Use sorted() before dict() to control key order")
print("- Use key parameter with sorted() for custom ordering")
print("- Dictionary equality doesn't depend on key order")
print("- Insertion order is preserved since Python 3.7")
print("- Choose ordering based on your use case (lookup speed, readability)")
