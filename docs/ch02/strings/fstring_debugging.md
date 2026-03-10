# F-String Debugging


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python 3.8 introduced the `=` specifier in f-strings, making it easy to print both variable names and their values. This simple feature dramatically improves debugging output.

---

## The `=` Specifier

Add `=` after an expression inside an f-string to print both the expression and its value:

```python
x = 42
print(f"{x=}")  # x=42

name = "Alice"
print(f"{name=}")  # name='Alice'
```

### Before and After

```python
# Before Python 3.8
x = 10
y = 20
print(f"x={x}, y={y}")  # x=10, y=20

# Python 3.8+
print(f"{x=}, {y=}")    # x=10, y=20
```

Less typing, less chance of mismatch between variable name and value.

---

## Basic Usage

### Variables

```python
count = 100
name = "Bob"
active = True

print(f"{count=}")   # count=100
print(f"{name=}")    # name='Bob'
print(f"{active=}")  # active=True
```

### Expressions

The `=` specifier works with any expression, not just variables:

```python
x = 5
print(f"{x + 10=}")      # x + 10=15
print(f"{x * 2=}")       # x * 2=10
print(f"{x ** 2=}")      # x ** 2=25

items = [1, 2, 3]
print(f"{len(items)=}")  # len(items)=3
print(f"{sum(items)=}")  # sum(items)=6
```

### Function Calls

```python
def get_status():
    return "OK"

print(f"{get_status()=}")  # get_status()='OK'

# With arguments
def add(a, b):
    return a + b

print(f"{add(2, 3)=}")  # add(2, 3)=5
```

### Object Attributes

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(f"{p.x=}, {p.y=}")  # p.x=3, p.y=4
```

---

## Combining with Format Specifiers

The `=` can be combined with format specifiers:

### Number Formatting

```python
value = 123.456789

print(f"{value=}")        # value=123.456789
print(f"{value=:.2f}")    # value=123.46
print(f"{value=:10.2f}")  # value=    123.46

large = 1234567
print(f"{large=:,}")      # large=1,234,567
print(f"{large=:_}")      # large=1_234_567
```

### Width and Alignment

```python
name = "Bob"

print(f"{name=:>10}")  # name=       Bob
print(f"{name=:<10}")  # name=Bob       
print(f"{name=:^10}")  # name=   Bob    
```

### Number Bases

```python
num = 255

print(f"{num=}")     # num=255
print(f"{num=:b}")   # num=11111111
print(f"{num=:x}")   # num=ff
print(f"{num=:o}")   # num=377
print(f"{num=:#x}")  # num=0xff
```

---

## Spaces Around `=`

Spaces in the f-string are preserved in the output:

```python
x = 42

print(f"{x=}")      # x=42
print(f"{x =}")     # x =42
print(f"{x= }")     # x= 42
print(f"{x = }")    # x = 42
```

This helps customize the output format:

```python
a, b, c = 1, 2, 3

# Compact
print(f"{a=},{b=},{c=}")     # a=1,b=2,c=3

# Readable
print(f"{a = }, {b = }, {c = }")  # a = 1, b = 2, c = 3
```

---

## Debugging Collections

### Lists and Tuples

```python
numbers = [1, 2, 3, 4, 5]
print(f"{numbers=}")        # numbers=[1, 2, 3, 4, 5]
print(f"{numbers[0]=}")     # numbers[0]=1
print(f"{numbers[-1]=}")    # numbers[-1]=5
print(f"{numbers[1:3]=}")   # numbers[1:3]=[2, 3]
```

### Dictionaries

```python
user = {"name": "Alice", "age": 30}
print(f"{user=}")           # user={'name': 'Alice', 'age': 30}
print(f"{user['name']=}")   # user['name']='Alice'
```

### Nested Structures

```python
data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}
print(f"{data['users'][0]['name']=}")  # data['users'][0]['name']='Alice'
```

---

## Debugging Comparisons

```python
x, y = 10, 20

print(f"{x < y=}")    # x < y=True
print(f"{x == y=}")   # x == y=False
print(f"{x + y=}")    # x + y=30

# Chain comparisons
a = 15
print(f"{10 < a < 20=}")  # 10 < a < 20=True
```

---

## Practical Debugging Patterns

### Quick Variable Inspection

```python
def calculate(a, b, c):
    result = (a + b) * c
    print(f"{a=}, {b=}, {c=}, {result=}")  # Debug line
    return result

calculate(2, 3, 4)  # a=2, b=3, c=4, result=20
```

### Loop Debugging

```python
items = ["apple", "banana", "cherry"]
for i, item in enumerate(items):
    print(f"{i=}, {item=}")
# i=0, item='apple'
# i=1, item='banana'
# i=2, item='cherry'
```

### Conditional Debugging

```python
def process(value):
    print(f"Input: {value=}")
    
    if value > 100:
        result = "high"
    elif value > 50:
        result = "medium"
    else:
        result = "low"
    
    print(f"Output: {result=}")
    return result
```

### Function Entry/Exit

```python
def complex_function(x, y):
    print(f"ENTER: {x=}, {y=}")
    
    intermediate = x * y
    print(f"  {intermediate=}")
    
    result = intermediate ** 2
    print(f"EXIT: {result=}")
    
    return result
```

---

## Combining with repr()

By default, strings show quotes (using `repr()`). Use `!s` for `str()`:

```python
name = "Alice"

print(f"{name=}")    # name='Alice' (repr)
print(f"{name=!s}")  # name=Alice (str)
print(f"{name=!r}")  # name='Alice' (explicit repr)
```

### Custom Objects

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(f"{p=}")    # p=Point(3, 4) (uses __repr__)
print(f"{p=!s}")  # p=(3, 4) (uses __str__)
```

---

## Advanced: ASCII Representation

Use `!a` for ASCII-safe representation:

```python
text = "Héllo"

print(f"{text=}")    # text='Héllo'
print(f"{text=!a}")  # text='H\xe9llo'
```

---

## Debugging with Walrus Operator

Combine `=` specifier with walrus operator (`:=`) for inline assignment:

```python
# Traditional
data = fetch_data()
print(f"Fetched: {data}")

# With walrus + f-string debugging
print(f"{(data := fetch_data())=}")

# Practical example
if (n := len(items)) > 10:
    print(f"Too many items: {n=}")
```

---

## Limitations

### Cannot Use with Format String Variables

```python
# This doesn't work
fmt = "{x=}"
x = 42
# print(fmt.format(x=x))  # Won't include the "x=" prefix

# The = specifier only works in f-strings
print(f"{x=}")  # x=42
```

### Python Version Requirement

```python
import sys
print(f"Python {sys.version_info.major}.{sys.version_info.minor}")

# f"{x=}" requires Python 3.8+
# Earlier versions will raise SyntaxError
```

---

## Comparison with Other Debug Methods

```python
x = 42
y = "hello"

# Method 1: Manual (verbose)
print(f"x={x}, y={y}")

# Method 2: f-string debug (Python 3.8+)
print(f"{x=}, {y=}")

# Method 3: Using locals()
print(locals())  # Shows all local variables

# Method 4: Using __debug__ and assert
assert x > 0, f"{x=} should be positive"

# Method 5: logging module
import logging
logging.debug(f"{x=}, {y=}")
```

---

## Summary

| Syntax | Output |
|--------|--------|
| `f"{x=}"` | `x=42` |
| `f"{x = }"` | `x = 42` |
| `f"{x=:.2f}"` | `x=3.14` |
| `f"{x=!s}"` | `x=value` (str) |
| `f"{x=!r}"` | `x='value'` (repr) |
| `f"{len(items)=}"` | `len(items)=5` |
| `f"{a + b=}"` | `a + b=15` |

**Key Points**:

- Add `=` after any expression in an f-string to see name and value
- Works with variables, expressions, function calls, and attributes
- Combine with format specifiers (`:` after `=`)
- Control spacing by adding spaces around `=`
- Use `!s` or `!r` to control string representation
- Requires Python 3.8 or later
- Great for quick debugging without writing verbose print statements
