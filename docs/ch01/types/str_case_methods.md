# Case Methods


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

String case methods return new strings with modified letter casing. The original string remains unchanged due to immutability.

## Basic Transforms

Convert entire strings to uniform case.

### 1. Lower and Upper

Convert all characters to lowercase or uppercase.

```python
s = "Hello World"

print(s.lower())  # hello world
print(s.upper())  # HELLO WORLD
print(s)          # Hello World (unchanged)
```

### 2. Method Call Syntax

Methods can be called on the class with string as argument.

```python
s = "Hello World"

# Instance method call
print(s.lower())         # hello world

# Equivalent class method call
print(str.lower(s))      # hello world
print(str.upper(s))      # HELLO WORLD
```

### 3. Chaining Methods

Chain multiple method calls together.

```python
s = "  HELLO  "

result = s.strip().lower()
print(result)  # hello

# Step by step
stripped = s.strip()    # "HELLO"
lowered = stripped.lower()  # "hello"
```

## Title Transforms

Transform casing based on word boundaries.

### 1. The title() Method

Capitalize the first letter of each word.

```python
s = "hello world"
print(s.title())  # Hello World

s = "HELLO WORLD"
print(s.title())  # Hello World
```

### 2. The capitalize() Method

Capitalize only the first character of the string.

```python
s = "hello world"
print(s.capitalize())  # Hello world

s = "HELLO WORLD"
print(s.capitalize())  # Hello world
```

### 3. Title Edge Cases

The `title()` method treats apostrophes as word boundaries.

```python
s = "it's a test"
print(s.title())  # It'S A Test (unexpected)

# For proper title case, use string.capwords
import string
print(string.capwords("it's a test"))  # It's A Test
```

## Swap and Fold

Additional case transformation methods.

### 1. The swapcase() Method

Swap uppercase to lowercase and vice versa.

```python
s = "Hello World"
print(s.swapcase())  # hELLO wORLD

s = "PyThOn"
print(s.swapcase())  # pYtHoN
```

### 2. The casefold() Method

Aggressive lowercase for case-insensitive comparison.

```python
s1 = "straße"
s2 = "STRASSE"

# lower() doesn't handle German ß
print(s1.lower())      # straße
print(s2.lower())      # strasse

# casefold() does
print(s1.casefold())   # strasse
print(s2.casefold())   # strasse
print(s1.casefold() == s2.casefold())  # True
```

### 3. When to Use Each

Choose the appropriate method for your use case.

```python
# Display formatting
title = "welcome message".title()  # Welcome Message

# User input normalization
email = "User@Example.COM".lower()  # user@example.com

# International comparison
match = "Ω".casefold() == "ω".casefold()  # True
```

## Unicode Behavior

Case methods work with Unicode characters.

### 1. Accented Characters

Accents are preserved during case conversion.

```python
s = "héllo wórld"
print(s.upper())  # HÉLLO WÓRLD
print(s.title())  # Héllo Wórld
```

### 2. Non-Latin Scripts

Some scripts don't have case distinctions.

```python
# Korean has no case
korean = "안녕하세요"
print(korean.upper())  # 안녕하세요 (unchanged)

# Greek has case
greek = "Ελληνικά"
print(greek.upper())   # ΕΛΛΗΝΙΚΆ
print(greek.lower())   # ελληνικά
```

### 3. Length Changes

Some case conversions change string length.

```python
# German sharp s expands
s = "ß"
print(s.upper())       # SS
print(len(s))          # 1
print(len(s.upper()))  # 2

# Turkish dotted i
s = "İ"  # Turkish capital I with dot
print(s.lower())       # i̇ (may vary by locale)
```

## Practical Patterns

Common use cases for case methods.

### 1. Input Normalization

Normalize user input for consistent processing.

```python
def normalize_email(email):
    """Normalize email to lowercase."""
    return email.strip().lower()

emails = ["User@Example.COM", "  admin@test.org  "]
normalized = [normalize_email(e) for e in emails]
print(normalized)  # ['user@example.com', 'admin@test.org']
```

### 2. Display Formatting

Format strings for user display.

```python
def format_name(first, last):
    """Format name with proper capitalization."""
    return f"{first.capitalize()} {last.upper()}"

print(format_name("john", "doe"))  # John DOE
```

### 3. Case-Insensitive Search

Search without case sensitivity.

```python
def search_insensitive(text, query):
    """Case-insensitive substring search."""
    return query.casefold() in text.casefold()

text = "Hello World"
print(search_insensitive(text, "WORLD"))  # True
print(search_insensitive(text, "earth"))  # False
```
