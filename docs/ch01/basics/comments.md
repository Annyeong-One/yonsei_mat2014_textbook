# Comments

Comments are notes in your code that Python ignores. They explain what the code does, why it exists, or provide context for future readers.

---

## Single-Line Comments

Use `#` for single-line comments:

```python
# This is a comment
x = 10  # This is an inline comment

# Calculate the area
area = length * width  # length and width are in meters
```

Everything after `#` on that line is ignored.

---

## Multi-Line Comments

Python doesn't have true multi-line comments like `/* */` in C. Instead, use:

### Option 1: Multiple `#` Lines

```python
# This is a longer comment
# that spans multiple lines
# explaining something complex
x = calculate_value()
```

### Option 2: Triple-Quoted Strings

```python
"""
This is a multi-line string.
It can be used as a comment if not assigned to anything.
Python will create the string but then discard it.
"""

'''
Single quotes work too.
This is also a multi-line comment.
'''
```

**Note**: Triple-quoted strings are technically string literals, not comments. They're ignored only if not assigned or used. Use `#` for true comments.

---

## Docstrings (Documentation Strings)

Triple-quoted strings immediately after a function, class, or module definition are **docstrings**:

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.
    
    Returns:
        The area as a float.
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)
help(calculate_area)
```

### Class Docstring

```python
class Rectangle:
    """A class representing a rectangle shape."""
    
    def __init__(self, length, width):
        """Initialize with length and width."""
        self.length = length
        self.width = width
```

### Module Docstring

```python
"""
mymodule.py

This module provides utility functions for geometric calculations.
"""

def area(l, w):
    return l * w
```

---

## Comments in Other Languages

| Language | Single-Line | Multi-Line |
|----------|-------------|------------|
| Python | `#` | `"""` or `'''` |
| C / C++ / Java | `//` | `/* */` |
| JavaScript | `//` | `/* */` |
| MATLAB | `%` | `%{ %}` |
| LaTeX | `%` | N/A |
| Bash / Shell | `#` | N/A |
| SQL | `--` | `/* */` |
| HTML | N/A | `<!-- -->` |

---

## When to Comment

### Good Comments

```python
# Convert temperature from Celsius to Fahrenheit
fahrenheit = celsius * 9/5 + 32

# Workaround for bug in library v2.3 (see issue #123)
result = data.copy()

# TODO: Optimize this loop for large datasets
for item in items:
    process(item)

# FIXME: Handle edge case when list is empty
```

### Bad Comments (Avoid)

```python
# Increment x by 1
x = x + 1  # Too obvious

# This is a variable
name = "Alice"  # Doesn't add value

# Loop through items
for item in items:  # Already clear from code
    print(item)
```

---

## Comment Best Practices

### 1. Explain Why, Not What

```python
# Bad: Set x to 5
x = 5

# Good: Default timeout in seconds (server requires minimum of 5)
x = 5
```

### 2. Keep Comments Updated

```python
# Bad: Outdated comment
# Calculate sum of first 10 numbers
total = sum(range(20))  # Code changed, comment didn't

# Good: Accurate comment
# Calculate sum of first 20 numbers
total = sum(range(20))
```

### 3. Use Consistent Style

```python
# Preferred: Space after #
# This is a comment

#Avoid: No space
#This looks cramped
```

### 4. Comment Markers

```python
# TODO: Implement caching
# FIXME: Handle None input
# HACK: Temporary workaround
# NOTE: This assumes sorted input
# XXX: This needs attention
```

---

## Commenting Out Code

Use `#` to temporarily disable code:

```python
# result = slow_function()  # Disabled for testing
result = fast_function()

# Debugging
# print(f"Debug: x = {x}")
# print(f"Debug: y = {y}")
```

**Tip**: Don't leave commented-out code in production. Use version control instead.

---

## Key Takeaways

- `#` for single-line comments
- `"""` or `'''` for multi-line (technically strings)
- Docstrings document functions, classes, modules
- Comment **why**, not **what**
- Keep comments accurate and updated
- Use TODO, FIXME markers for action items
