
# Type Conversions

Python supports conversions between numeric types.

The most common numeric conversions are:

- `int()` for integers
- `float()` for floating-point numbers
- `complex()` for complex numbers

These conversions allow programs to move values between different numeric representations.

```mermaid2
flowchart TD
    A[int]
    A --> B[float]
    A --> C[complex]
    B --> D[int]
    B --> C
````

---

## 1. Converting int to float

Converting an integer to a float preserves the numeric value while changing its representation.

```python
x = 5
y = float(x)

print(y)
print(type(y))
```

Output:

```text
5.0
<class 'float'>
```

---

## 2. Converting float to int

Converting a float to an integer truncates toward zero.

```python
x = 3.9
y = int(x)

print(y)
```

Output:

```text
3
```

For negative values:

```python
print(int(-3.9))
```

Output:

```text
-3
```

---

## 3. Converting int to complex

An integer can be converted directly to a complex number.

```python
x = 7
z = complex(x)

print(z)
```

Output:

```text
(7+0j)
```

---

## 4. Converting float to complex

A float can also be converted directly.

```python
x = 2.5
z = complex(x)

print(z)
```

Output:

```text
(2.5+0j)
```

---

## 5. Creating complex numbers from two parts

The `complex()` function can take two arguments:

```python
z = complex(2, 3)
print(z)
```

Output:

```text
(2+3j)
```

This means:

[
2 + 3j
]

---

## 6. Converting Strings

Strings can often be converted into numeric values.

```python
print(int("42"))
print(float("3.14"))
print(complex("2+3j"))
```

Output:

```text
42
3.14
(2+3j)
```

However, the string must be in valid format.

```python
# int("hello")      -> ValueError
# float("abc")      -> ValueError
```

---

## 7. Implicit Numeric Promotion

Python also performs automatic promotion during mixed arithmetic.

```python
print(type(3 + 2.5))
print(type(3 + 2j))
print(type(2.5 + 2j))
```

Output:

```text
<class 'float'>
<class 'complex'>
<class 'complex'>
```

This follows the general widening order:

```text
int -> float -> complex
```

```mermaid2
flowchart LR
    A[int] --> B[float] --> C[complex]
```

---

## 8. Worked Examples

### Example 1: integer to float

```python
x = 10
print(float(x))
```

### Example 2: float to integer

```python
y = 8.99
print(int(y))
```

### Example 3: integer to complex

```python
n = 4
print(complex(n))
```

---

## 9. Common Pitfalls

### Assuming float-to-int rounds

```python
print(int(4.9))
```

This produces `4`, not `5`.

### Forgetting complex string syntax

```python
complex("2+3j")
```

works, but malformed strings do not.

### Ignoring promotion

Mixed arithmetic can produce wider numeric types than expected.

---

## 10. Summary

Key ideas:

* Python supports explicit conversion with `int()`, `float()`, and `complex()`
* float-to-int conversion truncates toward zero
* integers and floats can be converted into complex numbers
* strings may be converted when properly formatted
* mixed numeric arithmetic promotes values from `int` to `float` to `complex`

Type conversion is essential for writing programs that combine different numeric representations safely and clearly.