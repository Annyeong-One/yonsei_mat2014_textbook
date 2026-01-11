# Naming Constraints

## Basic Rules

### 1. Must Start With

Valid first characters:
- Letters: `A-Z`, `a-z`
- Underscore: `_`

```python
# Valid
name = "Alice"
_private = 42
userName = "Bob"
```

### 2. Cannot Start

Invalid first characters:
- Digits: `0-9`

```python
# Invalid
# 2speed = 60  # SyntaxError
```

## Subsequent Chars

### 1. Allowed

After first character:
- Letters: `A-Z`, `a-z`
- Digits: `0-9`
- Underscore: `_`

```python
# Valid
user123 = "Alice"
data_2024 = [1, 2, 3]
__private__ = True
```

### 2. Not Allowed

- Spaces
- Hyphens: `-`
- Special: `@`, `#`, `$`, etc.

```python
# Invalid
# user-name = "Alice"  # SyntaxError
# user name = "Bob"    # SyntaxError
# user@host = "data"   # SyntaxError
```

## Case Sensitivity

### 1. Different Vars

```python
Data = 100
data = 200
DATA = 300

print(f"{Data = }")  # Data = 100
print(f"{data = }")  # data = 200
print(f"{DATA = }")  # DATA = 300
```

### 2. Common Mistakes

```python
name = "Alice"
# Later...
print(Name)  # NameError
```

## Length Limits

### 1. Practical Limit

No hard limit, but:
- Keep under 30 characters
- Readability matters

```python
# Too long
this_is_an_extremely_long_name = 42

# Better
max_timeout = 30
```

## Reserved Words

### 1. Cannot Use

Python keywords reserved:

```python
import keyword
print(keyword.kwlist)
```

Common keywords:
- `if`, `else`, `elif`
- `for`, `while`, `break`
- `def`, `class`, `return`
- `import`, `from`, `as`
- `True`, `False`, `None`
- `and`, `or`, `not`
- `in`, `is`
- `try`, `except`, `finally`
- `with`, `lambda`, `yield`

### 2. Examples

```python
# Invalid
# class = "MyClass"  # SyntaxError
# for = 5           # SyntaxError
# None = 10         # SyntaxError
```

## Special Patterns

### 1. Single Underscore

```python
# "don't care" variable
for _ in range(5):
    print("Hello")

# Throwaway
_, status, _ = ("GET", 200, "OK")
```

### 2. Double Underscore

```python
# Name mangling
class MyClass:
    def __init__(self):
        self.__private = 42
```

### 3. Dunder Magic

```python
# Special methods
class MyClass:
    def __init__(self):
        pass
    
    def __str__(self):
        return "MyClass"
```

## Quick Reference

| Pattern | Valid | Example |
|---------|-------|---------|
| Letter start | ✅ | `name` |
| Underscore start | ✅ | `_private` |
| Digit start | ❌ | `2name` |
| Contains digits | ✅ | `var123` |
| Contains underscore | ✅ | `user_name` |
| Contains hyphen | ❌ | `user-name` |
| Contains space | ❌ | `user name` |
| Reserved word | ❌ | `class` |
| Case sensitive | ✅ | `Name` ≠ `name` |

## Validation

```python
def is_valid(name):
    return name.isidentifier()

# Test
print(is_valid("valid_name"))   # True
print(is_valid("2invalid"))     # False
print(is_valid("class"))        # True (but reserved!)
print(is_valid("user-name"))    # False
```
