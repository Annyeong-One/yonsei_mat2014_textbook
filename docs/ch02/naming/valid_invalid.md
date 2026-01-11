# Valid & Invalid

## Valid Identifiers

### 1. Letter Start

```python
# Uppercase
Name = "Alice"
UserData = [1, 2, 3]
MAX_SIZE = 100

# Lowercase  
name = "Bob"
user_data = [4, 5, 6]
count = 0
```

### 2. Underscore Start

```python
_private = 42
_internal = "data"
__very_private = True
```

### 3. With Numbers

```python
# After first char
user1 = "Alice"
data2024 = [1, 2, 3]
var_123 = True
```

### 4. Mixed Case

```python
# CamelCase
UserName = "Alice"
MyClassName = "Example"

# snake_case
user_name = "Bob"
my_variable = 42
```

## Invalid

### 1. Start with Digit

```python
# All invalid
# 2speed = 60      # SyntaxError
# 123var = "data"  # SyntaxError
# 1st_place = True # SyntaxError
```

### 2. Special Chars

```python
# All invalid
# user-name = "Alice"  # SyntaxError
# user@host = "data"   # SyntaxError
# price$ = 100         # SyntaxError
# user#1 = "Bob"       # SyntaxError
```

### 3. Spaces

```python
# All invalid
# user name = "Alice"  # SyntaxError
# my var = 42          # SyntaxError
# first name = "Bob"   # SyntaxError
```

### 4. Reserved Keywords

```python
# All invalid
# class = "MyClass"   # SyntaxError
# def = 42            # SyntaxError
# for = [1, 2, 3]     # SyntaxError
# if = True           # SyntaxError
```

## Edge Cases

### 1. Looks Invalid

But valid:

```python
# Valid (underscore start)
_ = 42
__ = "data"
___ = [1, 2, 3]

# Valid (all underscores)
___private___ = True
```

### 2. Looks Valid

But reserved:

```python
# These are keywords!
# None = 10    # SyntaxError
# True = False # SyntaxError
# pass = 42    # SyntaxError
```

## Testing Validity

### 1. Built-in Method

```python
# Check if valid
print("valid_name".isidentifier())   # True
print("2invalid".isidentifier())     # False
print("class".isidentifier())        # True (reserved!)
print("user-name".isidentifier())    # False
```

### 2. Keyword Check

```python
import keyword

name = "class"
if keyword.iskeyword(name):
    print(f"{name} is keyword!")
```

### 3. Safe Check

```python
import keyword

def is_safe(name):
    return (
        name.isidentifier() and
        not keyword.iskeyword(name)
    )

# Test
print(is_safe("valid_name"))  # True
print(is_safe("class"))       # False
print(is_safe("2bad"))        # False
```

## Common Patterns

### 1. Constants

```python
# All caps with underscores
MAX_SIZE = 100
DEFAULT_TIMEOUT = 30
PI = 3.14159
```

### 2. Private Convention

```python
# Leading underscore
_internal = 42
_helper = lambda x: x * 2
```

### 3. Name Mangling

```python
# Double underscore (in classes)
class MyClass:
    __private_var = 42
```

### 4. Magic Methods

```python
# Dunder methods
__init__ = lambda self: None
__str__ = lambda self: "obj"
__len__ = lambda self: 0
```

## Quick Reference

| Example | Valid? | Reason |
|---------|--------|--------|
| `name` | ✅ | Standard |
| `_name` | ✅ | Private |
| `__name` | ✅ | Mangling |
| `__name__` | ✅ | Dunder |
| `Name` | ✅ | Capitalized |
| `NAME` | ✅ | Constant |
| `name123` | ✅ | With digits |
| `2name` | ❌ | Digit start |
| `name-var` | ❌ | Hyphen |
| `name var` | ❌ | Space |
| `class` | ❌ | Reserved |
| `None` | ❌ | Reserved |

## Test All

```python
import keyword

tests = [
    "valid_name",
    "_private",
    "2invalid",
    "user-name",
    "class",
    "None",
    "my_var_123",
]

for name in tests:
    valid = name.isidentifier()
    kw = keyword.iskeyword(name)
    
    if kw:
        status = "❌ Keyword"
    elif valid:
        status = "✅ Valid"
    else:
        status = "❌ Invalid"
    
    print(f"{name:15} {status}")
```
