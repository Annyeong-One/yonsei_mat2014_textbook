"""
Python Regular Expressions - Tutorial 06: Lookahead and Lookbehind
==================================================================

LEARNING OBJECTIVES:
-------------------
1. Understand lookahead assertions (?=...) and (?!...)
2. Master lookbehind assertions (?<=...) and (?<!...)
3. Combine lookarounds with other patterns
4. Apply lookarounds to complex validation scenarios
5. Understand zero-width assertions

PREREQUISITES:
-------------
- Tutorials 01-05 (all previous tutorials)

DIFFICULTY: ADVANCED
"""

import re

# ==============================================================================
# SECTION 1: INTRODUCTION TO LOOKAROUNDS
# ==============================================================================

"""
LOOKAROUNDS are zero-width assertions - they match a position, not characters.
They CHECK if a pattern exists ahead or behind, without consuming characters.

Types:
  (?=...)   Positive lookahead: must be followed by ...
  (?!...)   Negative lookahead: must NOT be followed by ...
  (?<=...)  Positive lookbehind: must be preceded by ...
  (?<!...)  Negative lookbehind: must NOT be preceded by ...

Key concept: They don't capture or consume characters!
"""

print("="*70)
print("SECTION 1: POSITIVE LOOKAHEAD (?=...)")
print("="*70)

# Example 1: Basic positive lookahead
# -----------------------------------
"""
Match a pattern only if it's followed by another pattern.
"""

text1 = "read reading reader"

# Match "read" only if followed by "ing"
pattern1 = r"read(?=ing)"
matches1 = re.findall(pattern1, text1)

print(f"Text: '{text1}'")
print(f"Pattern: 'read(?=ing)' (read followed by ing)")
print(f"Matches: {matches1}")
print("(Note: 'ing' is not included in the match)")

print()

# Example 2: Lookahead for validation
# -----------------------------------
"""
Check if a number is followed by a specific unit.
"""

text2 = "100kg 200g 300ml"

# Match numbers followed by "kg"
pattern2 = r"\d+(?=kg)"
matches2 = re.findall(pattern2, text2)

print(f"Text: '{text2}'")
print(f"Pattern: '\\d+(?=kg)' (numbers before kg)")
print(f"Matches: {matches2}")

print()

# ==============================================================================
# SECTION 2: NEGATIVE LOOKAHEAD (?!...)
# ==============================================================================

"""
Match only if NOT followed by a pattern.
"""

print("="*70)
print("SECTION 2: NEGATIVE LOOKAHEAD (?!...)")
print("="*70)

# Example 3: Negative lookahead
# -----------------------------
text3 = "cat cats dog dogs"

# Match "cat" not followed by "s"
pattern3 = r"cat(?!s)"
matches3 = re.findall(pattern3, text3)

print(f"Text: '{text3}'")
print(f"Pattern: 'cat(?!s)' (cat not followed by s)")
print(f"Matches: {matches3}")

print()

# Example 4: Excluding specific suffixes
# --------------------------------------
text4 = "test.txt test.py test.md readme.txt"

# Match filenames not ending with .txt
pattern4 = r"\w+(?!\.txt)\.\w+"
matches4 = re.findall(pattern4, text4)

print(f"Text: '{text4}'")
print(f"Non-.txt files: {matches4}")

print()

# ==============================================================================
# SECTION 3: POSITIVE LOOKBEHIND (?<=...)
# ==============================================================================

"""
Match only if preceded by a pattern.
"""

print("="*70)
print("SECTION 3: POSITIVE LOOKBEHIND (?<=...)")
print("="*70)

# Example 5: Basic lookbehind
# ---------------------------
text5 = "$100 €200 £300"

# Match numbers preceded by $
pattern5 = r"(?<=\$)\d+"
matches5 = re.findall(pattern5, text5)

print(f"Text: '{text5}'")
print(f"Pattern: '(?<=\\$)\\d+' (numbers after $)")
print(f"Matches: {matches5}")

print()

# Example 6: Extracting values after labels
# -----------------------------------------
text6 = "Price: $50 Tax: $10 Total: $60"

# Match numbers that come after "Total: $"
pattern6 = r"(?<=Total: \$)\d+"
total = re.search(pattern6, text6)

print(f"Text: '{text6}'")
if total:
    print(f"Total amount: ${total.group()}")

print()

# ==============================================================================
# SECTION 4: NEGATIVE LOOKBEHIND (?<!...)
# ==============================================================================

"""
Match only if NOT preceded by a pattern.
"""

print("="*70)
print("SECTION 4: NEGATIVE LOOKBEHIND (?<!...)")
print("="*70)

# Example 7: Negative lookbehind
# ------------------------------
text7 = "123 456 789 012"

# Match 3-digit numbers NOT preceded by "0"
pattern7 = r"(?<!0)\d{3}"
matches7 = re.findall(pattern7, text7)

print(f"Text: '{text7}'")
print(f"Pattern: '(?<!0)\\d{{3}}' (3 digits not after 0)")
print(f"Matches: {matches7}")

print()

# ==============================================================================
# SECTION 5: COMBINING LOOKAROUNDS
# ==============================================================================

print("="*70)
print("SECTION 5: COMBINING LOOKAROUNDS")
print("="*70)

# Example 8: Password validation
# ------------------------------
"""
Validate password:
- At least 8 characters
- Contains at least one digit
- Contains at least one letter
- Contains at least one special character
"""

def validate_password(password):
    # Check minimum length
    if len(password) < 8:
        return False, "Too short"
    
    # Use lookaheads to check all requirements
    pattern = r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$"
    
    if re.match(pattern, password):
        return True, "Valid password"
    return False, "Missing required characters"

passwords = [
    "password",      # No digit or special char
    "pass123",       # No special char
    "Pass@123",      # Valid!
    "12345678",      # No letters or special
    "P@ss1"          # Too short
]

print("Password validation:")
for pwd in passwords:
    valid, msg = validate_password(pwd)
    status = "✓" if valid else "✗"
    print(f"  {status} '{pwd}': {msg}")

print()

# Example 9: Finding words between specific patterns
# --------------------------------------------------
text9 = "start apple banana end start cherry date end"

# Match words that are after "start" and before "end"
pattern9 = r"(?<=start )\w+(?= \w* end)"
matches9 = re.findall(pattern9, text9)

print(f"Text: '{text9}'")
print(f"Words after 'start': {matches9}")

print()

# ==============================================================================
# SECTION 6: PRACTICAL APPLICATIONS
# ==============================================================================

print("="*70)
print("SECTION 6: PRACTICAL APPLICATIONS")
print("="*70)

# Example 10: Currency conversion validation
# ------------------------------------------
text10 = "$100.00 €200.50 £300.75 ¥400"

# Extract amounts in dollars only
dollar_pattern = r"(?<=\$)\d+\.\d{2}"
dollar_amounts = re.findall(dollar_pattern, text10)

print(f"Text: '{text10}'")
print(f"Dollar amounts: {['$' + amt for amt in dollar_amounts]}")

print()

# Example 11: Extracting @mentions (not in emails)
# ------------------------------------------------
text11 = "Hi @john! Email: user@example.com, @alice says hi"

# Match @username but not when it's part of an email
pattern11 = r"(?<!\w)@\w+(?![\w.])"
mentions = re.findall(pattern11, text11)

print(f"Text: '{text11}'")
print(f"Mentions: {mentions}")
print("(Excludes @example.com because it's part of email)")

print()

# Example 12: Matching numbers not in equations
# ---------------------------------------------
text12 = "Age: 25, Score: 3+7=10, Price: 30"

# Match standalone numbers (not part of equations)
pattern12 = r"(?<![+=])\d+(?![+=])"
standalone = re.findall(pattern12, text12)

print(f"Text: '{text12}'")
print(f"Standalone numbers: {standalone}")

print()

# ==============================================================================
# SECTION 7: ADVANCED PATTERNS
# ==============================================================================

print("="*70)
print("SECTION 7: ADVANCED LOOKAROUND PATTERNS")
print("="*70)

# Example 13: Remove duplicate words but keep one
# -----------------------------------------------
text13 = "the the cat sat sat on the mat mat"

# Remove only the second occurrence of duplicates
pattern13 = r"\b(\w+)\s+(?=\1\b)"
result13 = re.sub(pattern13, "", text13)

print(f"Original: '{text13}'")
print(f"Deduplicated: '{result13}'")

print()

# Example 14: Validate hex color codes
# ------------------------------------
"""
Valid: #FFF, #FFFFFF
Invalid: #FF, #FFFFFFF
"""

colors = ["#FFF", "#FFFFFF", "#123ABC", "#GG", "#12345"]

pattern14 = r"^#(?:[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$"

print("Hex color validation:")
for color in colors:
    valid = bool(re.match(pattern14, color))
    status = "✓" if valid else "✗"
    print(f"  {status} {color}")

print()

# ==============================================================================
# SECTION 8: SUMMARY
# ==============================================================================

print("="*70)
print("LOOKAROUND CHEAT SHEET")
print("="*70)

cheat_sheet = """
LOOKAHEAD (looks forward):
  (?=...)     Positive: must be followed by ...
  (?!...)     Negative: must NOT be followed by ...

LOOKBEHIND (looks backward):
  (?<=...)    Positive: must be preceded by ...
  (?<!...)    Negative: must NOT be preceded by ...

KEY FEATURES:
  - Zero-width: don't consume characters
  - Don't capture: not included in match
  - Multiple lookarounds can be combined
  - Lookbehind must be fixed-width in Python

COMMON PATTERNS:
  (?=.*\d)               Contains at least one digit
  (?!.*admin)            Doesn't contain "admin"
  (?<=\$)\d+             Number after $
  (?<!@)\w+              Word not preceded by @
  
PASSWORD VALIDATION:
  ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$
  - At least 8 chars
  - Has lowercase, uppercase, and digit

CAUTION:
  - Lookbehind must have fixed width
  - Can impact performance
  - Sometimes simpler alternatives exist
"""

print(cheat_sheet)

print("\n" + "="*70)
print("END OF TUTORIAL - Lookahead and Lookbehind mastered!")
print("Next: Tutorial 07 - Practical Applications")
print("="*70)
