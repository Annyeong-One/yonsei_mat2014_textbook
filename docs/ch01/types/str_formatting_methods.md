# Formatting Methods


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python provides three distinct string formatting approaches. Understanding all three is essential for reading legacy code and writing modern Python.

## Percent Formatting

The `%` operator is Python's oldest formatting method, borrowed from C's `printf` function.

### 1. Basic Syntax

The modulo operator takes a format string on the left and values on the right.

```python
name = "Alice"
age = 30

# Single value
greeting = "Hello, %s" % name
print(greeting)  # Hello, Alice

# Multiple values (tuple)
info = "Name: %s, Age: %d" % (name, age)
print(info)  # Name: Alice, Age: 30
```

### 2. Type Specifiers

Different specifiers control value conversion: `%s` for strings, `%d` for integers, `%f` for floats.

```python
pi = 3.14159

print("String: %s" % pi)      # String: 3.14159
print("Integer: %d" % 42)     # Integer: 42
print("Float: %f" % pi)       # Float: 3.141590
print("Float: %.2f" % pi)     # Float: 3.14
```

### 3. Named Placeholders

Use a dictionary with named placeholders for clearer formatting.

```python
data = {"name": "Bob", "city": "Seoul"}
message = "%(name)s lives in %(city)s" % data
print(message)  # Bob lives in Seoul
```

## The format() Method

The `str.format()` method uses curly braces `{}` as placeholders and supports positional and keyword arguments.

### 1. Basic Syntax

Empty braces are filled in order by positional arguments.

```python
name = "Carol"
age = 25

# Positional
print("Hello, {}!".format(name))
# Hello, Carol!

print("{} is {} years old".format(name, age))
# Carol is 25 years old
```

### 2. Indexed Arguments

Numeric indices allow reusing or reordering arguments.

```python
# Reordering
print("{1} before {0}".format("A", "B"))
# B before A

# Reusing
print("{0}{0}{0}".format("ha"))
# hahaha
```

### 3. Keyword Arguments

Named placeholders make templates self-documenting.

```python
template = "{name} scored {score} points"
print(template.format(name="Dave", score=95))
# Dave scored 95 points

# Mix positional and keyword
print("{0} lives in {city}".format("Eve", city="Seoul"))
# Eve lives in Seoul
```

## F-String Literals

F-strings embed expressions directly inside string literals using `{expression}` syntax. Introduced in Python 3.6.

### 1. Basic Syntax

Prefix with `f` or `F` before the opening quote.

```python
name = "Frank"
age = 28

print(f"Name: {name}, Age: {age}")
# Name: Frank, Age: 28

# Expressions are evaluated
print(f"Next year: {age + 1}")
# Next year: 29
```

### 2. Method Calls

Methods can be called directly within expressions.

```python
text = "hello"
print(f"Upper: {text.upper()}")
# Upper: HELLO

items = [1, 2, 3]
print(f"Count: {len(items)}")
# Count: 3
```

### 3. Debug Specifier

Python 3.8 added `=` for self-documenting debug output.

```python
x = 10
y = 20

print(f"{x=}, {y=}")
# x=10, y=20

print(f"{x + y=}")
# x + y=30
```

## Method Comparison

Each method has distinct advantages for different situations.

### 1. Readability

F-strings embed variables directly, making them immediately readable.

```python
name = "Grace"
score = 95.5

# %-formatting (verbose)
print("Student %s scored %.1f%%" % (name, score))

# str.format() (clearer)
print("Student {} scored {:.1f}%".format(name, score))

# f-string (most readable)
print(f"Student {name} scored {score:.1f}%")
```

### 2. Dynamic Templates

Use `str.format()` when format strings come from external sources.

```python
# Template from configuration
templates = {
    "en": "Hello, {name}!",
    "ko": "안녕하세요, {name}님!"
}

lang = "ko"
print(templates[lang].format(name="민수"))
# 안녕하세요, 민수님!
```

### 3. When to Use Each

F-strings for new code, `str.format()` for dynamic templates, `%` for legacy compatibility.

```python
# Modern code: f-strings
result = f"Value: {value:.2f}"

# External templates: str.format()
template = load_config("message.txt")
result = template.format(**data)

# Logging (traditional): %-formatting
import logging
logging.info("User %s logged in", username)
```
