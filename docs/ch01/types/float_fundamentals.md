# Float Fundamentals

Python uses floating-point numbers to represent real numbers with decimal values. Floats are essential for scientific computing, financial calculations, and mathematical operations.

## Creating Floats

Multiple ways to create floating-point numbers.

### 1. Decimal Notation

Standard decimal point syntax.

```python
a = 3.14
print(a, type(a))  # 3.14 <class 'float'>

b = -0.001
print(b)           # -0.001

# Trailing decimal makes it a float
c = 3    # int
d = 3.   # float
print(type(c), type(d))  # <class 'int'> <class 'float'>

# Leading decimal is valid
e = .314
print(e)           # 0.314
```

### 2. Scientific Notation

Use `e` or `E` for powers of ten.

```python
# 1.23 × 10^4 = 12300.0
a = 1.23e4
print(a)           # 12300.0

# 5.67 × 10^-3 = 0.00567
b = 5.67E-3
print(b)           # 0.00567

# Equivalent representations
print(.314e1)      # 3.14
print(31.4e-1)     # 3.14
print(314e-2)      # 3.14
```

### 3. Type Conversion

Convert other types to float.

```python
# From integer
a = float(10)
print(a)           # 10.0

# From string
b = float("45.67")
print(b)           # 45.67

# Whitespace is automatically stripped
print(float("   3.14   "))  # 3.14

# Leading zeros are ignored
print(float("007.5"))       # 7.5

# From scientific notation string
c = float("1.5e2")
print(c)           # 150.0

# From boolean
print(float(True))   # 1.0
print(float(False))  # 0.0
```

## Basic Operations

Standard arithmetic with floats.

### 1. Arithmetic Operators

All standard operations work with floats.

```python
x = 10.5
y = 2.3

print(x + y)   # 12.8    Addition
print(x - y)   # 8.2     Subtraction
print(x * y)   # 24.15   Multiplication
print(x / y)   # 4.565...Division
print(x ** y)  # 42.43...Exponentiation
```

### 2. Division Operations

Different division behaviors.

```python
a = 7.5
b = 2.0

# True division (always float)
print(a / b)    # 3.75

# Floor division (rounds down)
print(a // b)   # 3.0

# Modulus (remainder)
print(a % b)    # 1.5

# divmod returns both
print(divmod(a, b))  # (3.0, 1.5)
```

### 3. Augmented Assignment

Shorthand operators modify in place.

```python
x = 10.0

x += 2.5   # x = x + 2.5
print(x)   # 12.5

x *= 2     # x = x * 2
print(x)   # 25.0

x /= 5     # x = x / 5
print(x)   # 5.0
```

## Math Module

Built-in mathematical functions.

### 1. Basic Functions

Common math operations.

```python
import math

x = 2.0

print(math.sqrt(x))    # 1.414...  Square root
print(math.pow(x, 3))  # 8.0       Power
print(math.exp(x))     # 7.389...  e^x
print(math.log(x))     # 0.693...  Natural log
print(math.log10(x))   # 0.301...  Base-10 log
```

### 2. Trigonometric Functions

Angles in radians.

```python
import math

x = math.pi / 4  # 45 degrees

print(math.sin(x))   # 0.707...
print(math.cos(x))   # 0.707...
print(math.tan(x))   # 1.0

# Inverse functions
print(math.asin(0.5))  # 0.523... radians
print(math.degrees(math.asin(0.5)))  # 30.0 degrees
```

### 3. Rounding Functions

Multiple rounding options.

```python
import math

x = 3.7
y = -3.7

print(math.floor(x))   # 3   Round down
print(math.floor(y))   # -4  Round down (toward -∞)

print(math.ceil(x))    # 4   Round up
print(math.ceil(y))    # -3  Round up (toward +∞)

print(math.trunc(x))   # 3   Truncate toward zero
print(math.trunc(y))   # -3  Truncate toward zero
```

## NumPy Operations

Efficient numerical computing with NumPy.

### 1. Basic Functions

NumPy provides similar functions.

```python
import numpy as np

x = 2.0

print(np.sqrt(x))   # 1.414...
print(np.log(x))    # 0.693...
print(np.exp(x))    # 7.389...
print(np.sin(x))    # 0.909...
print(np.cos(x))    # -0.416...
```

### 2. Array Operations

Vectorized operations on arrays.

```python
import numpy as np

a = np.array([1.2, 2.5, 3.7])
b = np.array([0.8, 1.5, 2.3])

print(a + b)    # [2.  4.  6. ]
print(a * b)    # [0.96 3.75 8.51]
print(np.sqrt(a))  # [1.095 1.581 1.924]
```

### 3. Float Data Types

Control precision with dtype.

```python
import numpy as np

# Different float precisions
a = np.array([1.0, 2.0], dtype=np.float32)  # 32-bit
b = np.array([1.0, 2.0], dtype=np.float64)  # 64-bit (default)

print(a.dtype)  # float32
print(b.dtype)  # float64
```

## Built-in Functions

Python's built-in float functions.

### 1. abs() Function

Absolute value.

```python
print(abs(-3.14))   # 3.14
print(abs(3.14))    # 3.14
```

### 2. round() Function

Round to specified decimals.

```python
x = 3.14159

print(round(x))      # 3
print(round(x, 2))   # 3.14
print(round(x, 4))   # 3.1416

# Banker's rounding (round half to even)
print(round(2.5))    # 2
print(round(3.5))    # 4
```

### 3. min() and max()

Find extremes in sequences.

```python
values = [1.5, 3.2, 0.8, 2.1]

print(min(values))   # 0.8
print(max(values))   # 3.2
print(sum(values))   # 7.6
```
