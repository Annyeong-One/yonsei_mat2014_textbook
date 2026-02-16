"""
Unicode Normalization and Case Folding - String Comparison Strategies
This tutorial demonstrates how to use NFC normalization and case folding
to properly compare Unicode strings that may look the same but have
different internal representations.
Run this file to see Unicode normalization in action!
"""

from unicodedata import normalize

print("=" * 70)
print("UNICODE NORMALIZATION AND CASE FOLDING - EXAMPLES")
print("=" * 70)

# ============================================================================
# EXAMPLE 1: The Unicode Representation Problem
# ============================================================================
print("\n1. THE PROBLEM - VISUALLY IDENTICAL STRINGS THAT ARE DIFFERENT")
print("-" * 70)

# These two strings LOOK identical but are built differently
# é (single character) vs e + combining accent
str1 = 'café'  # e + acute accent (precomposed form NFC)
str2 = 'cafe\u0301'  # e + combining acute accent (decomposed form NFD)

print(f"\nString 1: {str1}")
print(f"String 2: {str2}")
print(f"\nThey look the same, but are they equal? {str1 == str2}")
print(f"\nLength of str1: {len(str1)} characters")
print(f"Length of str2: {len(str2)} characters")

print("\nWHY THEY'RE DIFFERENT:")
print("- str1 uses precomposed form: 'é' is ONE character (U+00E9)")
print("- str2 uses decomposed form: 'e' + combining accent (two chars)")
print("- Both are valid Unicode, but visually identical to humans")
print("- This causes problems when comparing strings!")

# ============================================================================
# EXAMPLE 2: Understanding Unicode Normalization Forms
# ============================================================================
print("\n2. UNICODE NORMALIZATION FORMS - NFC vs NFD")
print("-" * 70)

print("\nThere are several normalization forms:")
print("- NFC (Canonical Decomposition, followed by Canonical Composition)")
print("- NFD (Canonical Decomposition only)")
print("- NFKC (Compatibility Decomposition, followed by Composition)")
print("- NFKD (Compatibility Decomposition only)")

print("\nFor our purposes, NFC is the most useful.")
print("It combines characters into their precomposed form.\n")

# Normalize both strings to NFC form
nfc_str1 = normalize('NFC', str1)
nfc_str2 = normalize('NFC', str2)

print(f"normalize('NFC', str1) == normalize('NFC', str2): {nfc_str1 == nfc_str2}")
print(f"\nBoth are now: {nfc_str1}")
print(f"Length: {len(nfc_str1)} character(s)")

print("\nWHY THIS HELPS:")
print("- Both strings are now in the SAME form (NFC)")
print("- They can now be compared reliably")
print("- This solves the hidden character problem!")

# ============================================================================
# EXAMPLE 3: Creating a Unicode-Aware Comparison Function
# ============================================================================
print("\n3. NFC COMPARISON FUNCTION")
print("-" * 70)

def nfc_equal(str1, str2):
    """
    Compare two strings using NFC normalization.

    This function normalizes both strings to NFC form before comparison,
    ensuring that visually identical strings are considered equal.
    """
    return normalize('NFC', str1) == normalize('NFC', str2)

print("\nDefined: nfc_equal(str1, str2)")
print("This function normalizes both strings to NFC before comparing.\n")

# Test the function
test_strings = [
    ('café', 'cafe\u0301', 'café vs café (different representations)'),
    ('Café', 'CAFÉ', 'Café vs CAFÉ (different cases)'),
    ('naïve', 'naïve', 'naïve vs naïve (same form)'),
]

print("Testing nfc_equal():\n")
for s1, s2, description in test_strings:
    result = nfc_equal(s1, s2)
    print(f"  {description}")
    print(f"    nfc_equal({s1!r}, {s2!r}) = {result}\n")

print("NOTE: nfc_equal() still distinguishes case (Café != CAFÉ)")

# ============================================================================
# EXAMPLE 4: Case Folding - Making Comparison Case Insensitive
# ============================================================================
print("\n4. CASE FOLDING - COMBINING NFC WITH CASEFOLD()")
print("-" * 70)

print("\nFor case-insensitive comparison, Python provides casefold():")
print("- casefold() is more aggressive than lower()")
print("- It handles language-specific lowercasing\n")

test_case = 'Café'
print(f"Original: {test_case}")
print(f"lower():  {test_case.lower()}")
print(f"casefold():  {test_case.casefold()}\n")

# For most English text they're the same, but for some Unicode:
special = 'ß'  # German sharp S
print(f"German 'ß' example:")
print(f"  'ß'.lower() = {'ß'.lower()!r}")
print(f"  'ß'.casefold() = {'ß'.casefold()!r}")
print(f"  Note: casefold() is more aggressive for Unicode!")

# ============================================================================
# EXAMPLE 5: Creating a Case-Insensitive Comparison Function
# ============================================================================
print("\n5. CASE-INSENSITIVE COMPARISON FUNCTION")
print("-" * 70)

def fold_equal(str1, str2):
    """
    Compare two strings using NFC normalization and case folding.

    This combines two techniques:
    1. NFC normalization to handle different representations
    2. casefold() to handle case-insensitive comparison

    This is the most robust way to compare strings that might differ
    in both representation and case.
    """
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())

print("\nDefined: fold_equal(str1, str2)")
print("This function combines NFC normalization and case folding.\n")

print("Testing fold_equal():\n")
for s1, s2, description in test_strings:
    result = fold_equal(s1, s2)
    print(f"  {description}")
    print(f"    fold_equal({s1!r}, {s2!r}) = {result}\n")

# Additional case-sensitive tests
print("Additional tests with case folding:\n")
case_tests = [
    ('Café', 'CAFÉ', 'Café vs CAFÉ'),
    ('naïve', 'NAÏVE', 'naïve vs NAÏVE'),
    ('ß', 'SS', 'ß vs SS (German sharp S)'),
]

for s1, s2, description in case_tests:
    result = fold_equal(s1, s2)
    print(f"  {description}")
    print(f"    fold_equal({s1!r}, {s2!r}) = {result}\n")

# ============================================================================
# EXAMPLE 6: Practical Example - User Search
# ============================================================================
print("\n6. PRACTICAL EXAMPLE - ROBUST NAME SEARCH")
print("-" * 70)

users = [
    {'name': 'José', 'email': 'jose@example.com'},
    {'name': 'Françoise', 'email': 'francoise@example.com'},
    {'name': 'Müller', 'email': 'muller@example.com'},
    {'name': 'Søren', 'email': 'soren@example.com'},
]

def search_users(query, users_list):
    """Search users by name, case and accent insensitive."""
    results = []
    for user in users_list:
        if fold_equal(user['name'], query):
            results.append(user)
    return results

print("\nUser database:")
for user in users:
    print(f"  {user['name']:15} - {user['email']}")

print("\n\nSearching for users (case and accent insensitive):\n")
searches = ['josé', 'JOSÉ', 'FRANCOISE', 'muller', 'MÜLLER', 'soren']

for search_term in searches:
    found = search_users(search_term, users)
    if found:
        print(f"  Search '{search_term}': Found {found[0]['name']}")
    else:
        print(f"  Search '{search_term}': Not found")

# ============================================================================
# SUMMARY: When to Use Each Approach
# ============================================================================
print("\n" + "=" * 70)
print("SUMMARY - WHICH APPROACH TO USE?")
print("=" * 70)

print("""
1. USE nfc_equal() when:
   - You need case-sensitive comparison
   - But want to handle different Unicode representations
   - Example: Comparing database keys, filenames

2. USE fold_equal() when:
   - You need case-insensitive comparison
   - You want to handle Unicode representation differences
   - You're comparing user input (usernames, search queries)
   - Example: User authentication, search functionality

3. USE simple == when:
   - You know both strings are in the same Unicode form
   - Case matters
   - Performance is critical (no normalization overhead)
   - You're working with ASCII-only strings

KEY INSIGHTS:
- Always normalize strings before comparing them
- Use casefold() for user-facing comparisons
- Unicode normalization prevents subtle bugs
- This is especially important with international names and text
""")
