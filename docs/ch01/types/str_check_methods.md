# Check Methods

String check methods return boolean values indicating whether all characters satisfy a specific condition.

## Digit Checks

Methods for checking numeric characters.

### 1. The isdigit() Method

Returns `True` if all characters are ASCII digits (0-9).

```python
print("12345".isdigit())    # True
print("12345a".isdigit())   # False
print("".isdigit())         # False (empty string)
print("123.45".isdigit())   # False (dot is not digit)
```

### 2. The isnumeric() Method

Returns `True` for broader numeric characters including Unicode.

```python
print("12345".isnumeric())     # True
print("½".isnumeric())         # True (fraction)
print("²".isnumeric())         # True (superscript)
print("١٢٣".isnumeric())       # True (Arabic numerals)
```

### 3. Digit vs Numeric

Choose based on what characters you need to accept.

```python
test_strings = ["123", "½", "²", "٤٥٦"]

for s in test_strings:
    print(f"{s}: isdigit={s.isdigit()}, isnumeric={s.isnumeric()}")
# 123: isdigit=True, isnumeric=True
# ½: isdigit=False, isnumeric=True
# ²: isdigit=False, isnumeric=True
# ٤٥٦: isdigit=True, isnumeric=True
```

## Alpha Checks

Methods for checking alphabetic characters.

### 1. The isalpha() Method

Returns `True` if all characters are alphabetic.

```python
print("Hello".isalpha())       # True
print("Hello World".isalpha()) # False (space)
print("Hello123".isalpha())    # False (digits)
print("Héllo".isalpha())       # True (accented)
```

### 2. The isalnum() Method

Returns `True` if all characters are alphanumeric.

```python
print("Hello123".isalnum())    # True
print("Hello 123".isalnum())   # False (space)
print("Hello_123".isalnum())   # False (underscore)
```

### 3. Identifier Check

Use `isidentifier()` for valid Python variable names.

```python
print("variable".isidentifier())    # True
print("_private".isidentifier())    # True
print("123abc".isidentifier())      # False
print("my-var".isidentifier())      # False
print("class".isidentifier())       # True (but it's reserved)

# Check if valid and not reserved
import keyword
name = "class"
valid = name.isidentifier() and not keyword.iskeyword(name)
print(valid)  # False
```

## Case Checks

Methods for checking letter case.

### 1. The islower() Method

Returns `True` if all cased characters are lowercase.

```python
print("hello".islower())       # True
print("Hello".islower())       # False
print("hello123".islower())    # True (digits ignored)
print("hello!".islower())      # True (punctuation ignored)
print("123".islower())         # False (no cased chars)
```

### 2. The isupper() Method

Returns `True` if all cased characters are uppercase.

```python
print("HELLO".isupper())       # True
print("Hello".isupper())       # False
print("HELLO123".isupper())    # True
print("123".isupper())         # False (no cased chars)
```

### 3. The istitle() Method

Returns `True` if string is titlecased.

```python
print("Hello World".istitle())    # True
print("Hello world".istitle())    # False
print("HELLO WORLD".istitle())    # False
print("Hello".istitle())          # True
```

## Space Checks

Methods for checking whitespace.

### 1. The isspace() Method

Returns `True` if all characters are whitespace.

```python
print("   ".isspace())         # True
print("\t\n".isspace())        # True
print("".isspace())            # False (empty)
print("  a  ".isspace())       # False
```

### 2. Whitespace Characters

Various whitespace characters are recognized.

```python
whitespace_chars = [" ", "\t", "\n", "\r", "\v", "\f"]

for ws in whitespace_chars:
    print(f"{repr(ws)}: {ws.isspace()}")
# ' ': True
# '\t': True
# '\n': True
# '\r': True
# '\v': True
# '\f': True
```

### 3. Practical Validation

Check for blank or whitespace-only strings.

```python
def is_blank(s):
    """Check if string is empty or whitespace only."""
    return len(s) == 0 or s.isspace()

print(is_blank(""))        # True
print(is_blank("   "))     # True
print(is_blank("  a  "))   # False
```

## Printable Check

Check if string contains printable characters.

### 1. The isprintable() Method

Returns `True` if all characters are printable.

```python
print("Hello World".isprintable())    # True
print("Hello\nWorld".isprintable())   # False (newline)
print("Hello\tWorld".isprintable())   # False (tab)
print("".isprintable())               # True (empty)
```

### 2. Control Characters

Non-printable control characters return `False`.

```python
# ASCII control characters
print("\x00".isprintable())   # False (null)
print("\x07".isprintable())   # False (bell)
print("\x1b".isprintable())   # False (escape)
```

### 3. Sanitize Input

Filter non-printable characters from input.

```python
def sanitize(s):
    """Remove non-printable characters."""
    return "".join(c for c in s if c.isprintable())

dirty = "Hello\x00World\x07!"
clean = sanitize(dirty)
print(clean)  # HelloWorld!
```

## Combined Checks

Combine checks for validation patterns.

### 1. Username Validation

Validate username format.

```python
def valid_username(name):
    """Check valid username: alnum, starts with letter."""
    if not name:
        return False
    if not name[0].isalpha():
        return False
    return name.isalnum()

print(valid_username("john123"))   # True
print(valid_username("123john"))   # False
print(valid_username("john_doe"))  # False
```

### 2. Password Strength

Check password character requirements.

```python
def check_password(pw):
    """Check password has upper, lower, digit."""
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    return has_upper and has_lower and has_digit

print(check_password("Hello123"))   # True
print(check_password("hello123"))   # False (no upper)
print(check_password("HELLO123"))   # False (no lower)
```

### 3. Token Classification

Classify tokens by character type.

```python
def classify(token):
    """Classify token type."""
    if token.isdigit():
        return "number"
    if token.isalpha():
        return "word"
    if token.isspace():
        return "whitespace"
    return "mixed"

tokens = ["hello", "123", "  ", "abc123"]
for t in tokens:
    print(f"{t!r}: {classify(t)}")
```
