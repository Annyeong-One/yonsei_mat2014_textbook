# Methods and Attributes


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

In Python, an **attribute** is a property or value linked to an object, while a **method** is a callable function bound to an object. Since everything in Python is an object, even primitive types like `int`, `float`, and `str` have methods and attributes.

---

## Discovering Methods and Attributes

Use `dir()` to see all methods and attributes of any object:

```python
print(dir(float))
print(dir(int))
print(dir(str))
```

Use `help()` for documentation:

```python
help(str.upper)
```

---

## `float` Type

### Storage: IEEE 754

Python floats are 64-bit double-precision (IEEE 754):

| Component | Bits |
|-----------|------|
| Sign | 1 |
| Exponent | 11 |
| Mantissa | 52 |
| **Total** | **64** |

```python
mantissa_bits = 52
exponent_bits = 11
sign_bit = 1
total = mantissa_bits + exponent_bits + sign_bit
print(f"Float size: {total} bits")  # 64 bits
```

### Precision Limitations

Floats have finite precision:

```python
print(0.1 + 0.2)        # 0.30000000000000004 (not 0.3!)
print(0.1 + 0.2 == 0.3) # False
```

For exact decimals, use `decimal.Decimal`:

```python
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3
```

### Float Methods

```python
x = 3.14

x.is_integer()          # False (not a whole number)
(4.0).is_integer()      # True

x.as_integer_ratio()    # (7070651414971679, 2251799813685248)

x.hex()                 # '0x1.91eb851eb851fp+1'
```

### Float Attributes

```python
x = 3.14
print(x.real)           # 3.14 (real part)
print(x.imag)           # 0.0 (imaginary part)
```

### Comparing Floats

Use tolerance for comparison:

```python
a = 0.1 + 0.2
b = 0.3

# Wrong
print(a == b)                   # False

# Correct
print(abs(a - b) < 1e-9)        # True

# Or use math.isclose
import math
print(math.isclose(a, b))       # True
```

---

## `int` Type

### Storage: Arbitrary Precision

Python integers have **no size limit** — they grow as needed:

```python
big = 31415926535897932384626433832795028841971693993751058209749445923078164062
print(big)
print(type(big))        # <class 'int'>
```

No overflow errors like in C/Java.

### Integer Methods

```python
n = 42

n.bit_length()          # 6 (bits needed to represent 42)
n.bit_count()           # 3 (number of 1s in binary: 101010)

(255).to_bytes(2, 'big')    # b'\x00\xff'
int.from_bytes(b'\x00\xff', 'big')  # 255
```

### Integer Attributes

```python
n = 42
print(n.real)           # 42
print(n.imag)           # 0
print(n.numerator)      # 42
print(n.denominator)    # 1
```

### Integer Operations

```python
print(10 // 3)          # 3 (floor division)
print(10 % 3)           # 1 (modulus)
print(divmod(10, 3))    # (3, 1) (quotient, remainder)
print(2 ** 10)          # 1024 (exponentiation)
```

---

## `str` Type

### Storage: UTF-8 Encoding

Python strings are Unicode, encoded as UTF-8:

| Character Type | Bytes | Example |
|----------------|-------|---------|
| ASCII | 1 | `A`, `9`, `!` |
| Latin Extended | 2 | `é`, `ß`, `ø` |
| CJK (Korean, Chinese, Japanese) | 3 | `안`, `你`, `日` |
| Emoji | 4 | `😊`, `🚀` |

```python
# ASCII string
a = "Hello"
print(len(a))                       # 5 characters
print(len(a.encode('utf-8')))       # 5 bytes

# Korean string
b = "안녕"
print(len(b))                       # 2 characters
print(len(b.encode('utf-8')))       # 6 bytes (3 per character)

# Emoji
c = "😊"
print(len(c))                       # 1 character
print(len(c.encode('utf-8')))       # 4 bytes
```

### String Methods (Selection)

```python
s = "Hello World"

# Case methods
s.upper()               # 'HELLO WORLD'
s.lower()               # 'hello world'
s.title()               # 'Hello World'
s.capitalize()          # 'Hello world'

# Search methods
s.find('World')         # 6 (index)
s.count('l')            # 3
s.startswith('Hello')   # True
s.endswith('World')     # True

# Modify methods
s.replace('World', 'Python')  # 'Hello Python'
s.strip()               # Remove whitespace
s.split()               # ['Hello', 'World']

# Check methods
'hello'.isalpha()       # True
'123'.isdigit()         # True
'hello123'.isalnum()    # True
```

### String Formatting

```python
name = "Alice"
age = 30

# f-string (recommended)
f"Name: {name}, Age: {age}"

# format method
"Name: {}, Age: {}".format(name, age)

# % formatting (old style)
"Name: %s, Age: %d" % (name, age)
```

---

## Summary: How Types are Stored

| Type | Storage Format | Size | Precision |
|------|----------------|------|-----------|
| `float` | IEEE 754 double | 64 bits | ~15-17 decimal digits |
| `int` | Variable-length binary | Dynamic | Unlimited |
| `str` | UTF-8 Unicode | 1-4 bytes/char | N/A |

---

## Method Types in Classes

Python distinguishes three method types:

### Instance Methods

Operate on specific instances:

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):             # Instance method
        return f"{self.name} says woof!"

dog = Dog("Buddy")
dog.bark()                      # "Buddy says woof!"
```

### Class Methods

Operate on the class itself:

```python
class Dog:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Dog.count += 1
    
    @classmethod
    def get_count(cls):         # Class method
        return cls.count

Dog("Buddy")
Dog("Max")
Dog.get_count()                 # 2
```

### Static Methods

Don't depend on instance or class:

```python
class Math:
    @staticmethod
    def add(a, b):              # Static method
        return a + b

Math.add(2, 3)                  # 5
```

---

## Key Takeaways

- **Attributes**: Properties/values (`x.real`, `x.imag`)
- **Methods**: Callable functions (`x.is_integer()`, `s.upper()`)
- `dir(obj)` shows all methods and attributes
- `float`: 64-bit IEEE 754, finite precision, use `Decimal` for exactness
- `int`: Arbitrary precision, no overflow
- `str`: UTF-8 encoded, 1-4 bytes per character
- Python has instance methods, class methods (`@classmethod`), and static methods (`@staticmethod`)
