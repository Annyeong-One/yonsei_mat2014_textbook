

# float Fundamentals

The `float` type represents **floating-point numbers**, which are numbers with fractional parts.

Examples:

```python
3.14
0.5
-2.75
1.0
````

Floats are used to represent:

* measurements
* scientific values
* real-number approximations
* division results

```mermaid2
flowchart TD
    A[float]
    A --> B[whole part]
    A --> C[fractional part]
```

---

## 1. Floating-Point Numbers

A floating-point number usually includes a decimal point.

```python
x = 3.14
y = -0.25
z = 2.0
```

Unlike integers, floats can represent values between whole numbers.

---

## 2. Float Arithmetic

Floats support the same main arithmetic operators as integers.

```python
a = 5.5
b = 2.0

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Output:

```text
7.5
3.5
11.0
2.75
```

---

## 3. Division Produces Floats

In Python, the `/` operator returns a float even when the mathematical result is a whole number.

```python
print(6 / 2)
```

Output:

```text
3.0
```

This behavior distinguishes `/` from floor division `//`.

---

## 4. Scientific Notation

Python supports scientific notation for floats.

```python
a = 1.5e3
b = 2.0e-2

print(a)
print(b)
```

Output:

```text
1500.0
0.02
```

This notation is useful in science and engineering.

---

## 5. Floating-Point Approximation

Floats are **approximations**, not exact representations of most decimal fractions.

For example:

```python
print(0.1 + 0.2)
```

Output may be:

```text
0.30000000000000004
```

This happens because many decimal values cannot be represented exactly in binary floating-point form.

```mermaid2
flowchart LR
    A[decimal value] --> B[binary approximation] --> C[stored float]
```

---

## 6. Comparing Floats Carefully

Because floats are approximate, direct equality comparisons can be misleading.

```python
print(0.1 + 0.2 == 0.3)
```

Output:

```text
False
```

A safer approach is to compare with tolerance.

```python
x = 0.1 + 0.2
print(abs(x - 0.3) < 1e-9)
```

Output:

```text
True
```

---

## 7. Converting to Float

The `float()` function converts compatible values to floats.

```python
print(float(5))
print(float("3.14"))
```

Output:

```text
5.0
3.14
```

---

## 8. Worked Examples

### Example 1: average

```python
total = 7
count = 2
average = total / count

print(average)
```

Output:

```text
3.5
```

### Example 2: measurement

```python
length = 2.5
width = 4.0
area = length * width

print(area)
```

Output:

```text
10.0
```

### Example 3: approximation issue

```python
x = 0.1 + 0.2
print(x)
```

---

## 9. Common Pitfalls

### Expecting exact decimal behavior

Floats are not ideal when exact decimal arithmetic is required, such as in financial calculations.

### Comparing with `==`

Direct equality is often unsafe for computed float values.

---

## 10. Summary

Key ideas:

* `float` represents numbers with fractional parts
* floats support ordinary arithmetic
* division with `/` produces floats
* floating-point values are approximations
* float comparisons often require tolerance

The `float` type is essential for measurements, ratios, and scientific computation.