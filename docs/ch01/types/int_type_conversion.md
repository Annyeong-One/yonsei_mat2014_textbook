
# int Type Conversion

Python provides the `int()` function to convert values into integers.

This is one of the most common type conversions in Python, especially when working with:

- user input
- strings containing digits
- floating-point values
- boolean values

```mermaid
flowchart TD
    A[value]
    A --> B[int()]
    B --> C[integer result]
````

---

## 1. Basic Syntax

```python
int(x)
```

The function attempts to convert `x` into an integer.

Example:

```python
print(int("42"))
print(int(3.9))
print(int(True))
```

Output:

```text
42
3
1
```

---

## 2. Converting from Strings

A string containing digits can be converted to an integer.

```python
x = "123"
y = int(x)

print(y)
print(type(y))
```

Output:

```text
123
<class 'int'>
```

### Negative numbers

```python
print(int("-25"))
```

Output:

```text
-25
```

---

## 3. Converting from Floats

When converting a float to an integer, Python **truncates toward zero**.

```python
print(int(3.9))
print(int(3.1))
print(int(-3.9))
```

Output:

```text
3
3
-3
```

This is not rounding. It is truncation.

```mermaid
flowchart LR
    A[3.9] --> B[int()] --> C[3]
    D[-3.9] --> E[int()] --> F[-3]
```

---

## 4. Converting from Booleans

Because `bool` is a subclass of `int`, Boolean values convert naturally.

```python
print(int(True))
print(int(False))
```

Output:

```text
1
0
```

---

## 5. Base Conversion from Strings

`int()` can also interpret strings written in different bases.

Syntax:

```python
int(string, base)
```

Example:

```python
print(int("1010", 2))
print(int("52", 8))
print(int("2A", 16))
```

Output:

```text
10
42
42
```

This is useful when reading binary, octal, or hexadecimal values.

---

## 6. Invalid Conversions

Some conversions fail and raise `ValueError`.

```python
int("hello")
int("3.14")
```

These fail because the strings do not represent valid integers in base 10.

Example:

```python
try:
    print(int("hello"))
except ValueError:
    print("Cannot convert")
```

---

## 7. User Input Pattern

A common pattern is converting input strings into integers.

```python
age = int(input("Enter your age: "))
print(age + 1)
```

This works because `input()` always returns a string.

---

## 8. Worked Examples

### Example 1: converting input

```python
text = "45"
number = int(text)

print(number * 2)
```

Output:

```text
90
```

### Example 2: converting a float

```python
price = 19.99
whole = int(price)

print(whole)
```

Output:

```text
19
```

### Example 3: binary string to integer

```python
bits = "1101"
value = int(bits, 2)

print(value)
```

Output:

```text
13
```

---

## 9. Common Pitfalls

### Assuming `int()` rounds

```python
print(int(3.9))
```

This gives `3`, not `4`.

### Forgetting base when needed

```python
int("1010")
```

This is interpreted as decimal `1010`, not binary `10`.

---

## 10. Summary

Key ideas:

* `int()` converts compatible values into integers
* float conversion truncates toward zero
* strings can be converted when they contain valid integer text
* `int(string, base)` supports other number bases
* invalid conversions raise `ValueError`

Understanding `int()` is essential for handling input and performing exact numeric operations.