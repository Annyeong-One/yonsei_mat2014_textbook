# Complex Fundamentals

Python has built-in support for complex numbers, representing values with real and imaginary parts. Complex numbers are essential for scientific computing, signal processing, and mathematical applications.

## Creating Complex

Multiple ways to create complex numbers in Python.

### 1. Literal Syntax

Use `j` or `J` suffix for the imaginary part.

```python
a = 1 + 2j
print(a)         # (1+2j)
print(type(a))   # <class 'complex'>

# Uppercase J also works
b = 1 + 2J
print(b)         # (1+2j)

# No space before j allowed
# c = 1 + 2 j   # SyntaxError: invalid syntax
```

### 2. The complex() Function

Use the constructor for explicit creation.

```python
# Two arguments: real, imaginary
a = complex(1, 2)
print(a)         # (1+2j)

# Single argument: real only
b = complex(3)
print(b)         # (3+0j)

# From string
c = complex("1+2j")
print(c)         # (1+2j)
```

### 3. Pure Imaginary

Create numbers with only imaginary part.

```python
# Pure imaginary
i = 1j
print(i)         # 1j

# Using complex()
i = complex(0, 1)
print(i)         # 1j

# Zero
zero = 0j
print(zero)      # 0j
```

## Accessing Parts

Extract real and imaginary components.

### 1. Attributes

Use `.real` and `.imag` attributes.

```python
a = 3 + 4j

print(a.real)    # 3.0
print(a.imag)    # 4.0

# Both are floats
print(type(a.real))  # <class 'float'>
print(type(a.imag))  # <class 'float'>
```

### 2. NumPy Functions

Use `np.real()` and `np.imag()` for arrays.

```python
import numpy as np

a = 1 + 2j

print(np.real(a))        # 1.0
print(np.imag(a))        # 2.0
print(type(np.real(a)))  # <class 'numpy.float64'>
```

### 3. Conjugate

Get the complex conjugate with `.conjugate()`.

```python
a = 3 + 4j

conj = a.conjugate()
print(conj)      # (3-4j)

# Product with conjugate gives real number
print(a * conj)  # (25+0j)
```

## Internal Storage

Complex numbers store both parts as floats.

### 1. Float Components

Integer literals become floats internally.

```python
import numpy as np

a = 1 + 2j
print(type(a.real))  # <class 'float'>
print(type(a.imag))  # <class 'float'>

# These are all equivalent
b = 1. + 2j
c = 1. + 2.j
d = 1.0 + 2.0j

print(a == b == c == d)  # True
```

### 2. Memory Layout

A complex is two floats (16 bytes total).

```python
import sys

a = 1 + 2j
print(sys.getsizeof(a))  # 32 (includes object overhead)

# Compare with float
f = 1.0
print(sys.getsizeof(f))  # 24
```

### 3. Precision Limits

Subject to same float precision issues.

```python
a = 0.1 + 0.2j
print(a)  # (0.1+0.2j)

b = (0.1 + 0.1 + 0.1) + 0j
print(b)  # (0.30000000000000004+0j)
```

## Arithmetic

Standard arithmetic operations on complex numbers.

### 1. Basic Operations

Addition, subtraction, multiplication, division.

```python
a = 1 + 2j
b = 3 + 4j

print(a + b)    # (4+6j)
print(a - b)    # (-2-2j)
print(a * b)    # (-5+10j)
print(a / b)    # (0.44+0.08j)
```

### 2. Imaginary Unit

Verify that i² = -1.

```python
i = 1j

result = i * i
print(result)        # (-1+0j)
print(result.real)   # -1.0

# Using complex()
i = complex(0, 1)
print(i * i)         # (-1+0j)
```

### 3. Power Operations

Exponentiation with complex numbers.

```python
import numpy as np

a = 1 + 1j

# Square
print(a ** 2)        # 2j

# Square root
print(a ** 0.5)      # (1.0986...+0.4550...j)

# e^(i*pi) = -1 (Euler's identity)
result = np.exp(1j * np.pi)
print(result)        # (-1+0j) approximately
```

## Magnitude and Phase

Polar representation of complex numbers.

### 1. Absolute Value

Get magnitude with `abs()`.

```python
a = 3 + 4j

magnitude = abs(a)
print(magnitude)     # 5.0

# Same as sqrt(real² + imag²)
import math
manual = math.sqrt(a.real**2 + a.imag**2)
print(manual)        # 5.0
```

### 2. Phase Angle

Get angle with `cmath.phase()`.

```python
import cmath

a = 1 + 1j

phase = cmath.phase(a)
print(phase)             # 0.7853... (π/4 radians)
print(math.degrees(phase))  # 45.0 degrees
```

### 3. Polar Conversion

Convert between rectangular and polar forms.

```python
import cmath

a = 1 + 1j

# To polar (magnitude, phase)
r, phi = cmath.polar(a)
print(f"r={r:.4f}, φ={phi:.4f}")  # r=1.4142, φ=0.7854

# From polar back to rectangular
b = cmath.rect(r, phi)
print(b)  # (1+1j) approximately
```

## Math Functions

Complex-aware mathematical functions.

### 1. The cmath Module

Use `cmath` for complex math functions.

```python
import cmath

a = 1 + 2j

print(cmath.sqrt(a))    # (1.272...+0.786...j)
print(cmath.exp(a))     # (-1.131...+2.471...j)
print(cmath.log(a))     # (0.804...+1.107...j)
```

### 2. Trigonometric Functions

Complex trigonometry with `cmath`.

```python
import cmath

a = 1 + 1j

print(cmath.sin(a))     # (1.298...+0.634...j)
print(cmath.cos(a))     # (0.833...-0.988...j)
print(cmath.tan(a))     # (0.271...+1.083...j)
```

### 3. NumPy Integration

NumPy functions work with complex arrays.

```python
import numpy as np

# Array of complex numbers
arr = np.array([1+2j, 3+4j, 5+6j])

print(np.abs(arr))      # [2.236 5.    7.81 ]
print(np.angle(arr))    # [1.107 0.927 0.876]
print(np.real(arr))     # [1. 3. 5.]
print(np.imag(arr))     # [2. 4. 6.]
```

## Practical Examples

Common applications of complex numbers.

### 1. Unit Circle

Plot unit circle using Euler's formula.

```python
import numpy as np
import matplotlib.pyplot as plt

i = complex(0, 1)
theta = np.linspace(0, 2*np.pi, 100)

# e^(iθ) = cos(θ) + i·sin(θ)
z = np.exp(i * theta)

x = np.real(z)
y = np.imag(z)

fig, ax = plt.subplots(figsize=(4, 4))
ax.plot(x, y)
ax.set_aspect('equal')
ax.set_title('Unit Circle')
plt.show()
```

### 2. Roots of Unity

Calculate nth roots of unity.

```python
import numpy as np

def roots_of_unity(n):
    """Calculate n-th roots of unity."""
    k = np.arange(n)
    return np.exp(2j * np.pi * k / n)

# 4th roots of unity
roots = roots_of_unity(4)
print(roots)
# [ 1.+0.j  0.+1.j -1.+0.j -0.-1.j]
```

### 3. Quadratic Solutions

Solve quadratics with complex roots.

```python
import cmath

def solve_quadratic(a, b, c):
    """Solve ax² + bx + c = 0."""
    discriminant = b**2 - 4*a*c
    x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return x1, x2

# x² + 1 = 0 (no real solutions)
roots = solve_quadratic(1, 0, 1)
print(roots)  # (1j, -1j)

# x² - 2x + 1 = 0 (real solutions)
roots = solve_quadratic(1, -2, 1)
print(roots)  # ((1+0j), (1+0j))
```
