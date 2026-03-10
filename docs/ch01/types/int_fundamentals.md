# Integer Basics


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python integers are one of the fundamental numeric types for whole numbers. Unlike many languages, Python's `int` has arbitrary precision.

---

## Arbitrary Precision

Python integers can grow as large as memory allows without overflowing.

### 1. No Size Limit

Python integers are not limited to a fixed size like 32-bit or 64-bit.

```python
x = 10**100  # A very large integer
print(x)
```

### 2. Auto Float Convert

If an operation involves an integer and a float, Python automatically converts the integer to a float.

```python
x = 5
y = 2.0
result = x / y  # result is a float (2.5)
```

---

## Basic Operations

Python supports standard arithmetic operations with integers.

### 1. Arithmetic Table

![Arithmetic Operations](https://cdn.codegym.cc/images/article/80cd9ae0-2a36-464e-9e63-690c1feb1c62/512.webp)

[Image Source](https://codegym.cc/groups/posts/integer-division-java)

```python
a = 14
b = 4
print(a + b)   # Addition: 18
print(a - b)   # Subtraction: 10
print(a * b)   # Multiplication: 56
print(a / b)   # Division (float result): 3.5
print(a // b)  # Floor division: 3
print(a % b)   # Modulus: 2
print(a ** b)  # Exponentiation: 38416
```

### 2. Python vs C Division

Integer division behaves differently in Python and C.

**Python 3.x:**

```python
result = 10 / 3
print(result)  # Output: 3.3333333333333335 (floating-point)
```

For integer division in Python, use `//`:

```python
result = 10 // 3
print(result)  # Output: 3 (integer result)
```

**C:**

```c
#include <stdio.h>

int main() {
    int result = 10 / 3;
    printf("%d\n", result);  // Output: 3 (integer result)
    return 0;
}
```

For floating-point division in C:

```c
double result = 10.0 / 3;
printf("%lf\n", result);  // Output: 3.333333
```

**Summary:**
- Python 3.x: `/` gives float, `//` gives integer division
- C: `/` with integers gives integer division automatically

[ChatGPT](https://openai.com/blog/chatgpt)

### 3. Unary Operators

```python
a = 9
b = + a
c = - a
print(f"{a = }, {b = }, {c = }")

a = - 9
b = + a
c = - a
print(f"{a = }, {b = }, {c = }")
```

### 4. Dunder Methods

Basic math operations work through special methods.

```python
def main():
    a = 9
    b = 2

    # __add__
    print(a + b)
    print(a.__add__(b))
    print(int.__add__(a,b),end="\n\n")

    # __sub__
    print(a - b)
    print(a.__sub__(b))
    print(int.__sub__(a,b),end="\n\n")

    # __mul__
    print(a * b)
    print(a.__mul__(b))
    print(int.__mul__(a,b),end="\n\n")

    # __truediv__
    print(a / b)
    print(a.__truediv__(b))
    print(int.__truediv__(a,b),end="\n\n")

    # __floordiv__
    print(a // b)
    print(a.__floordiv__(b))
    print(int.__floordiv__(a,b),end="\n\n")

    # __mod__
    print(a % b)
    print(a.__mod__(b))
    print(int.__mod__(a,b),end="\n\n")

    # __pow__
    print(a ** b)
    print(a.__pow__(b))
    print(int.__pow__(a,b),end="\n\n")

if __name__ == "__main__":
    main()
```

### 5. n * n vs n**2

Both `n * n` and `n**2` square a number, but there are subtle differences.

**Reasons to use `n * n`:**

1. **Readability**: More immediately understandable
2. **Performance**: Slightly faster (direct multiplication)
3. **Historical**: Taught earlier in education

**Example:**

```python
n = 5
square_with_multiplication = n * n
square_with_exponentiation = n**2

print(square_with_multiplication)  # Output: 25
print(square_with_exponentiation)  # Output: 25
```

**Performance Comparison:**

```python
import timeit

n = 1000

# Timing n * n
multiplication_time = timeit.timeit('n * n', setup='n = 1000', number=1000000)

# Timing n**2
exponentiation_time = timeit.timeit('n**2', setup='n = 1000', number=1000000)

print(f"n * n time: {multiplication_time}")
print(f"n**2 time: {exponentiation_time}")
```

**Conclusion:** Both are correct; the choice depends on preference and context.

---

## Operator Precedence

Python follows standard mathematical order of operations.

### 1. Precedence Rules

1. Parentheses
2. Exponents
3. Unary + and -
4. Multiplication and Division (*, /, //, %) from left to right
5. Addition and Subtraction (+, -) from left to right

[Order of operations](https://en.wikipedia.org/wiki/Order_of_operations)

```python
def main():
    print(2 * 3 + 1)
    print(1 + 2 * 3)
    print(1 + 2 * 3 / 5)
    print(1 + 2 * 3 / 5 ** 2)

if __name__ == "__main__":
    main()
```

### 2. Practice Example

What is the output of the below code?

```python
print(10 + 5 ** 2 // 5)
```

**Solution:**

```python
print(10 + 5 ** 2 // 5)
```

equals to:

```python
print( 10 + ( ( 5 ** 2 ) // 5) )
```

```python
def main():
    print(10 + 5 ** 2 // 5)

if __name__ == "__main__":
    main()
```

---

## Built-in Functions

Python provides several built-in functions for integers.

### 1. Common Functions

```python
abs_val = abs(-10) # Absolute value: 10
abs_val = int.__abs__(-10)
print(abs_val)

power = pow(2, 3)    # Equivalent to 2 ** 3: 8
print(power)

max_val = max(10, 20, 30)  # Maximum value: 30
print(max_val)

min_val = min(10, 20, 30)  # Minimum value: 10
print(min_val)

rounded = round(5.678)  # Rounds to nearest integer: 6
print(rounded)

print(dir(int))
```

### 2. Math Module

```python
import math

def main():
    print( f"{math.floor(3.14) = }" )
    print( f"{math.floor(4.99) = }" )
    print( f"{math.ceil(3.14) = }" )
    print( f"{math.ceil(4.99) = }" )
    print( f"{math.sqrt(4.99) = }" )

if __name__ == "__main__":
    main()
```

---

## Integer Interning

Python optimizes memory by *interning* small integers.

### 1. Interning Range

Small integers (typically `-5` to `256`) are preallocated and reused.

```python
a = 100
b = 100
print(a is b)  # True, both refer to the same object in memory

x = 300
y = 300
print(x is y)  # False, different objects in memory
```

This optimization improves performance when working with small numbers.
