# Indentation and Blocks

## Introduction

Unlike most programming languages that use braces `{}` or keywords like `begin`/`end` to define code blocks, Python uses **indentation**. This is one of Python's most distinctive features and enforces readable code formatting.

Understanding indentation is crucial because improper indentation doesn't just make code hard to read—it causes syntax errors or changes program logic. This chapter covers everything you need to know about Python's indentation rules and code blocks.

## Why Indentation Matters in Python

### The Philosophy

Python's creator, Guido van Rossum, believed that code is read more often than it's written. By making indentation mandatory, Python ensures that code structure is always visually clear.

```python
# Python - structure is obvious
if x > 0:
    print("Positive")
    print("Greater than zero")
else:
    print("Not positive")

# Compare to languages with braces (structure can be hidden)
# if (x > 0) { print("Positive"); print("Greater than zero"); }
# else { print("Not positive"); }
```

### Indentation as Syntax

In Python, indentation isn't just for readability—it's part of the syntax:

```python
# Correct - indentation defines the block
if True:
    print("This is inside the if block")
print("This is outside the if block")

# Error - inconsistent indentation
if True:
    print("This is inside")
  print("This will cause IndentationError")

# Error - missing indentation
if True:
print("This will cause IndentationError")
```

## Basic Indentation Rules

### Rule 1: Consistent Indentation

All statements in a block must be indented by the same amount:

```python
# Correct - consistent 4-space indentation
if x > 0:
    print("Line 1")
    print("Line 2")
    print("Line 3")

# Error - inconsistent indentation
if x > 0:
    print("Line 1")
  print("Line 2")  # IndentationError: unexpected indent
      print("Line 3")  # IndentationError
```

### Rule 2: Indentation After Colons

Colons (`:`) indicate the start of an indented block:

```python
# After if
if condition:
    statement

# After for
for i in range(10):
    statement

# After while
while condition:
    statement

# After function definition
def function():
    statement

# After class definition
class MyClass:
    statement

# After with statement
with open('file.txt') as f:
    statement

# After try-except
try:
    statement
except Exception:
    statement
```

### Rule 3: Spaces vs Tabs

**PEP 8 Recommendation**: Use **4 spaces per indentation level**

```python
# Recommended (4 spaces)
if True:
    print("4 spaces")
    if True:
        print("8 spaces")

# Also valid but not recommended (2 spaces)
if True:
  print("2 spaces")
  if True:
    print("4 spaces")

# Valid but NEVER mix with spaces (causes errors)
if True:
<tab>print("Tab character")  # Don't do this if you use spaces elsewhere
```

**Critical**: Never mix tabs and spaces in the same file. Python 3 treats this as an error:

```python
# Error - mixing tabs and spaces
if True:
    print("Spaces")
<tab>print("Tab")  # TabError: inconsistent use of tabs and spaces
```

### Rule 4: Blank Lines

Blank lines don't require indentation:

```python
if x > 0:
    print("Positive")
                    # <-- Blank line (no indentation needed)
    print("Still in the if block")

# But be consistent within blocks
def function():
    statement1
    
    statement2  # Blank line above is fine
    
    statement3
```

## Defining Code Blocks

### Single-Statement Blocks

For single-statement blocks, you can use the same line (though not always recommended):

```python
# Valid - single statement on same line
if x > 0: print("Positive")

# But better for readability
if x > 0:
    print("Positive")

# Multiple statements must be indented
if x > 0: print("Line 1"); print("Line 2")  # Valid but ugly

# Better
if x > 0:
    print("Line 1")
    print("Line 2")
```

### Multi-Statement Blocks

Multiple statements must be properly indented:

```python
if score >= 60:
    print("You passed!")
    grade = "Pass"
    total_passes += 1
    print(f"Grade: {grade}")
```

### Nested Blocks

Blocks can be nested inside other blocks:

```python
# Each nesting level adds one indentation level
if x > 0:                    # Level 0
    print("Positive")        # Level 1
    if x > 10:               # Level 1
        print("Greater than 10")  # Level 2
        if x > 100:          # Level 2
            print("Greater than 100")  # Level 3

# Another example
for i in range(5):           # Level 0
    print(f"i = {i}")        # Level 1
    for j in range(3):       # Level 1
        print(f"  j = {j}")  # Level 2
        if i == j:           # Level 2
            print("  Equal!")  # Level 3
```

## Indentation in Different Constructs

### Conditional Statements

```python
# if-elif-else
if temperature > 30:
    print("Hot")
    action = "Use AC"
elif temperature > 20:
    print("Warm")
    action = "Open windows"
elif temperature > 10:
    print("Cool")
    action = "Light jacket"
else:
    print("Cold")
    action = "Heavy coat"

# Nested conditionals
if logged_in:
    if is_admin:
        print("Admin access")
        show_admin_panel()
    else:
        print("User access")
        show_user_panel()
else:
    print("Please log in")
    show_login_page()
```

### Loops

```python
# for loop
for i in range(5):
    print(i)
    print(i * 2)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

### Functions

```python
# Function definition
def calculate_area(length, width):
    area = length * width
    return area

# Function with multiple statements
def greet(name):
    message = f"Hello, {name}!"
    print(message)
    print("Welcome to Python!")
    return message

# Nested function
def outer():
    x = 10
    
    def inner():
        print(f"x = {x}")
    
    inner()
    return x
```

### Classes

```python
# Class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, I'm {self.name}")
        print(f"I'm {self.age} years old")
    
    def birthday(self):
        self.age += 1
        print(f"Happy birthday! Now {self.age}")

# Nested class
class Outer:
    class Inner:
        def method(self):
            print("Inner class method")
```

### Try-Except Blocks

```python
try:
    risky_operation()
    print("Success")
except ValueError:
    print("ValueError occurred")
    handle_value_error()
except TypeError:
    print("TypeError occurred")
    handle_type_error()
finally:
    print("Cleanup")
    cleanup()
```

### With Statements

```python
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
    process(content)

# Multiple context managers
with open('input.txt') as infile, open('output.txt', 'w') as outfile:
    data = infile.read()
    outfile.write(data.upper())
```

## Common Indentation Patterns

### Guarding Clauses

Return early to avoid deep nesting:

```python
# Poor - deep nesting
def process_data(data):
    if data is not None:
        if len(data) > 0:
            if validate(data):
                return transform(data)
    return None

# Better - guard clauses
def process_data(data):
    if data is None:
        return None
    if len(data) == 0:
        return None
    if not validate(data):
        return None
    return transform(data)
```

### Early Returns

```python
# Reduce nesting with early returns
def check_eligibility(age, license):
    if age < 18:
        return False
    if not license:
        return False
    return True

# Instead of
def check_eligibility(age, license):
    if age >= 18:
        if license:
            return True
    return False
```

### Loop Structures

```python
# Clean loop structure
for user in users:
    if not user.is_active:
        continue
    
    process_user(user)
    
    if user.needs_update:
        update_user(user)
```

## Continuation Lines

### Implicit Line Continuation

Python allows line continuation inside brackets, parentheses, and braces:

```python
# List spread across multiple lines
fruits = [
    'apple',
    'banana',
    'cherry',
    'date'
]

# Function call with many arguments
result = some_function(
    arg1,
    arg2,
    arg3,
    arg4
)

# Long condition
if (temperature > 30 and
    humidity > 70 and
    wind_speed < 10):
    print("Very hot and humid")

# Dictionary definition
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
```

### Explicit Line Continuation

Use backslash `\` for explicit continuation:

```python
# Arithmetic expression
total = 1 + 2 + 3 + \
        4 + 5 + 6 + \
        7 + 8 + 9

# String concatenation
message = "This is a very long message " \
          "that spans multiple lines " \
          "using backslash continuation"

# Note: Implicit continuation is preferred when possible
# Better:
total = (1 + 2 + 3 +
         4 + 5 + 6 +
         7 + 8 + 9)
```

### String Continuation

```python
# Triple quotes for multi-line strings
text = """
This is a multi-line string.
It preserves line breaks.
And indentation.
"""

# Implicit concatenation of string literals
message = ("This is "
           "a single "
           "string")

# Join method for dynamic strings
lines = [
    "Line 1",
    "Line 2",
    "Line 3"
]
text = "\n".join(lines)
```

## Handling Long Lines

PEP 8 recommends keeping lines under 79 characters. Here's how to break long lines:

### Function Calls

```python
# Method 1: Align with opening delimiter
result = some_function(arg1, arg2,
                       arg3, arg4)

# Method 2: Hanging indent (preferred)
result = some_function(
    arg1, arg2,
    arg3, arg4
)

# Method 3: One argument per line
result = some_function(
    arg1,
    arg2,
    arg3,
    arg4
)
```

### Function Definitions

```python
# Hanging indent
def long_function_name(
        param1, param2,
        param3, param4):
    print(param1)

# Or one per line
def long_function_name(
        param1,
        param2,
        param3,
        param4):
    print(param1)
```

### Conditional Statements

```python
# Use parentheses for multi-line conditions
if (condition1 and
    condition2 and
    condition3):
    do_something()

# Or break at logical operators
if (user.is_authenticated and
        user.has_permission('edit') and
        not user.is_suspended):
    allow_edit()
```

### Collections

```python
# Lists
my_list = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

# Dictionaries
config = {
    'host': 'localhost',
    'port': 8080,
    'debug': True,
    'timeout': 30
}

# Method chaining
result = (dataframe
          .filter(condition)
          .groupby('category')
          .agg({'value': 'sum'})
          .sort_values('value'))
```

## Indentation Best Practices

### 1. Use 4 Spaces

```python
# Good - 4 spaces
def function():
    statement1
    statement2

# Avoid - 2 spaces (valid but not PEP 8)
def function():
  statement1
  statement2

# Never - tabs mixed with spaces
def function():
    statement1
<tab>statement2  # TabError
```

### 2. Be Consistent

```python
# Good - consistent indentation throughout
if condition:
    statement1
    statement2
    if nested_condition:
        nested_statement

# Poor - varying indentation
if condition:
  statement1
    statement2
      if nested_condition:
        nested_statement
```

### 3. Avoid Deep Nesting

```python
# Poor - deeply nested
def process(data):
    if data:
        if validate(data):
            if transform(data):
                if save(data):
                    return True
    return False

# Better - early returns
def process(data):
    if not data:
        return False
    if not validate(data):
        return False
    if not transform(data):
        return False
    return save(data)
```

### 4. Use Blank Lines for Readability

```python
# Good - blank lines separate logical sections
def complex_function(x):
    # Validate input
    if x < 0:
        raise ValueError("x must be non-negative")
    
    # Calculate result
    result = 0
    for i in range(x):
        result += i ** 2
    
    # Return processed result
    return result / x
```

### 5. Align Continuation Lines

```python
# Good - aligned
result = some_function(argument1, argument2,
                       argument3, argument4)

# Good - hanging indent
result = some_function(
    argument1, argument2,
    argument3, argument4
)

# Poor - misaligned
result = some_function(argument1, argument2,
    argument3, argument4)
```

## Common Indentation Errors

### 1. IndentationError

Occurs when indentation is incorrect:

```python
# Error - missing indentation
if True:
print("No indentation")  # IndentationError: expected an indented block

# Error - unexpected indentation
x = 10
    y = 20  # IndentationError: unexpected indent
```

### 2. Inconsistent Indentation

```python
# Error - inconsistent spacing
if True:
    print("4 spaces")
  print("2 spaces")  # IndentationError: unindent does not match
```

### 3. TabError

```python
# Error - mixing tabs and spaces
if True:
    print("Spaces")
<tab>print("Tab")  # TabError: inconsistent use of tabs and spaces
```

### 4. Forgetting Colons

```python
# Error - missing colon
if condition  # SyntaxError: invalid syntax
    statement
```

### 5. Empty Blocks

```python
# Error - empty block
if condition:
# IndentationError: expected an indented block after 'if'

# Fix with pass
if condition:
    pass  # Placeholder
```

## IDE and Editor Support

### Configuring Your Editor

Most modern editors handle Python indentation automatically:

**VS Code**:
```json
{
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "python.formatting.provider": "black"
}
```

**PyCharm**:
- Settings → Editor → Code Style → Python → Tabs and Indents
- Set "Tab size" to 4
- Check "Use tab character" OFF

**Sublime Text**:
```json
{
    "tab_size": 4,
    "translate_tabs_to_spaces": true
}
```

### Automatic Formatting

Use formatters to ensure consistent indentation:

```bash
# Black - opinionated formatter
pip install black
black my_script.py

# autopep8 - PEP 8 compliant formatter
pip install autopep8
autopep8 --in-place my_script.py

# yapf - configurable formatter
pip install yapf
yapf --in-place my_script.py
```

## Special Cases

### Single-Line Blocks

```python
# Allowed but not always recommended
if x > 0: print("Positive")

# Better
if x > 0:
    print("Positive")

# Multiple statements (discouraged)
if x > 0: y = x; print(y)

# Much better
if x > 0:
    y = x
    print(y)
```

### Empty Blocks

```python
# Use pass for empty blocks
def not_implemented():
    pass

class EmptyClass:
    pass

# Or docstrings count as statements
def documented_but_empty():
    """This function does nothing yet."""
    pass  # Still good practice
```

### Comments and Indentation

```python
# Comments should align with code
if condition:
    # This comment is properly indented
    statement
    # Another comment
    another_statement

# Not this
if condition:
# Poorly indented comment
    statement
```

## Debugging Indentation Issues

### Check for Hidden Characters

```python
# Tabs might look like spaces but aren't
# Use editor's "Show whitespace" feature

# Run with Python's -tt flag for strict tab checking
# python -tt script.py
```

### Use Python's Indentation Checker

```python
# python -m tabnanny script.py
# Checks for ambiguous indentation
```

### Visual Indicators

Enable whitespace visualization in your editor:
- Dots for spaces
- Arrows for tabs
- Different colors for trailing spaces

## Quick Reference

### Valid Indentation Patterns
```python
# Basic block
if condition:
    statement

# Nested blocks
if outer:
    if inner:
        statement

# Multiple statements
if condition:
    statement1
    statement2
    statement3

# Continuation
result = function(
    arg1,
    arg2
)
```

### Common Errors
```python
# Missing indentation
if condition:
statement  # Error

# Inconsistent indentation
if condition:
    statement1
  statement2  # Error

# Mixing tabs and spaces
if condition:
    statement  # Spaces
<tab>statement  # Tab - Error!
```

## Summary

- Python uses **indentation to define code blocks** (not braces)
- **4 spaces** per indentation level is standard (PEP 8)
- **Never mix tabs and spaces**
- Colons (`:`) indicate the start of an indented block
- All statements in a block must have **consistent indentation**
- Use **blank lines** to separate logical sections (no indentation needed)
- Implicit continuation works inside `()`, `[]`, `{}`
- Explicit continuation uses backslash `\`
- Configure your editor to insert spaces instead of tabs
- Use formatting tools like **Black** or **autopep8** for consistency

Proper indentation is not just a stylistic choice in Python—it's a fundamental part of the language syntax. Master it early and your code will be both correct and readable.
