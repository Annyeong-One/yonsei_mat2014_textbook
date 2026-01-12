# String Built-ins

Python provides built-in functions that work with strings for measuring, converting, sorting, and character encoding operations.

## Length and Type

Functions for measuring strings and type conversion.

### 1. The len() Function

Returns the number of characters in a string.

```python
message = "Hello World!"
print(len(message))  # 12

# Empty string
print(len(""))       # 0

# Unicode characters count as one
print(len("안녕"))    # 2
print(len("café"))   # 4
```

### 2. The str() Function

Converts any value to its string representation.

```python
# From numbers
print(str(3.14))        # '3.14'
print(str(42))          # '42'
print(type(str(42)))    # <class 'str'>

# From other types
print(str(True))        # 'True'
print(str(None))        # 'None'
print(str([1, 2, 3]))   # '[1, 2, 3]'
```

### 3. String Concatenation

Use `str()` to concatenate non-strings.

```python
x = 10
y = 20
total = x + y

# Wrong: cannot concatenate str and int
# print("Total: " + total)  # TypeError

# Correct: convert to string first
print("Total: " + str(total))  # Total: 30

# Or use f-string (preferred)
print(f"Total: {total}")       # Total: 30
```

## Input Function

The `input()` function reads user input as a string.

### 1. Basic Input

Always returns a string, regardless of what user types.

```python
name = input("What is your name? ")
print(name, type(name))
# User types: Alice
# Output: Alice <class 'str'>

age = input("How old are you? ")
print(age, type(age))
# User types: 25
# Output: 25 <class 'str'>  (still string!)
```

### 2. Converting Input

Convert input to other types as needed.

```python
# Convert to integer
age = int(input("Enter your age: "))
print(age, type(age))  # 25 <class 'int'>

# Convert to float
price = float(input("Enter price: "))
print(price, type(price))  # 19.99 <class 'float'>

# One-liner pattern
n = int(input("Enter a number: "))
```

### 3. Input Validation

Handle invalid input gracefully.

```python
def get_integer(prompt):
    """Get integer input with validation."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

age = get_integer("Enter your age: ")
print(f"You are {age} years old.")
```

## Sorting Strings

Functions for ordering string characters.

### 1. The sorted() Function

Returns a sorted list of characters.

```python
s = "python"
result = sorted(s)
print(result)  # ['h', 'n', 'o', 'p', 't', 'y']
print(type(result))  # <class 'list'>

# Convert back to string
sorted_str = "".join(sorted(s))
print(sorted_str)  # hnopty
```

### 2. Reverse Sorting

Use `reverse=True` for descending order.

```python
s = "python"

# Ascending (default)
print(sorted(s))
# ['h', 'n', 'o', 'p', 't', 'y']

# Descending
print(sorted(s, reverse=True))
# ['y', 't', 'p', 'o', 'n', 'h']

# As string
print("".join(sorted(s, reverse=True)))
# ytponh
```

### 3. Case-Insensitive Sort

Use `key` parameter for custom sorting.

```python
chars = "PyThOn"

# Default: uppercase first (lower ASCII)
print(sorted(chars))
# ['O', 'P', 'T', 'h', 'n', 'y']

# Case-insensitive
print(sorted(chars, key=str.lower))
# ['h', 'n', 'O', 'P', 'T', 'y']
```

## Reversing Strings

Functions for reversing character order.

### 1. The reversed() Function

Returns an iterator over characters in reverse.

```python
s = "hello"

# reversed() returns iterator, not string
rev = reversed(s)
print(rev)  # <reversed object at 0x...>

# Iterate over it
for char in reversed(s):
    print(char, end="")
# olleh
```

### 2. Convert to String

Join the reversed iterator to get a string.

```python
s = "hello"

# Using join
reversed_str = "".join(reversed(s))
print(reversed_str)  # olleh

# Alternative: slicing (more common)
reversed_str = s[::-1]
print(reversed_str)  # olleh
```

### 3. Reversed vs Slicing

Both achieve reversal but differ in mechanism.

```python
s = "hello"

# reversed(): returns iterator (lazy)
rev_iter = reversed(s)

# Slicing: returns new string (eager)
rev_slice = s[::-1]

# For simple reversal, slicing is more Pythonic
palindrome = "radar"
is_palindrome = palindrome == palindrome[::-1]
print(is_palindrome)  # True
```

## Character Encoding

Functions for converting between characters and code points.

### 1. The ord() Function

Returns the Unicode code point of a character.

```python
# ASCII letters
print(ord("A"))  # 65
print(ord("Z"))  # 90
print(ord("a"))  # 97
print(ord("z"))  # 122

# Digits
print(ord("0"))  # 48
print(ord("9"))  # 57
```

### 2. The chr() Function

Returns the character for a Unicode code point.

```python
# From ASCII values
print(chr(65))   # A
print(chr(97))   # a
print(chr(48))   # 0

# Unicode characters
print(chr(8364))   # € (Euro sign)
print(chr(127775)) # 🌟 (Star emoji)
```

### 3. Alphabet Generation

Use `ord()` and `chr()` to generate sequences.

```python
import string

# Generate uppercase letters
for code in range(ord("A"), ord("Z") + 1):
    print(chr(code), end=" ")
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

# Or use string module
print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
```

## Practical Patterns

Common patterns using string built-ins.

### 1. Character Shifting

Implement simple cipher using `ord()` and `chr()`.

```python
def caesar_shift(text, shift):
    """Shift letters by given amount."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)

print(caesar_shift("Hello", 3))   # Khoor
print(caesar_shift("Khoor", -3))  # Hello
```

### 2. Anagram Check

Check if two strings are anagrams.

```python
def is_anagram(s1, s2):
    """Check if two strings are anagrams."""
    # Remove spaces and lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Compare sorted characters
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
```

### 3. Input Processing

Process multiple inputs from user.

```python
def get_numbers():
    """Get list of numbers from user."""
    line = input("Enter numbers (space-separated): ")
    return [int(x) for x in line.split()]

# Usage:
# Enter numbers (space-separated): 10 20 30
# Returns: [10, 20, 30]

def get_name_age():
    """Get name and age from user."""
    name = input("Name: ").strip()
    age = int(input("Age: "))
    return name, age
```
