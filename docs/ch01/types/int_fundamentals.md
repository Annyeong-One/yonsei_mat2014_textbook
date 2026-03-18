
# int Fundamentals

The `int` type represents **integers**, or whole numbers without fractional parts.

Examples of integers include:

```python
0
1
-5
42
1000000
````

Integers are one of the most fundamental data types in Python. They are used for:

* counting
* indexing
* loop control
* exact arithmetic
* representing discrete quantities

```mermaid
flowchart TD
    A[int]
    A --> B[positive]
    A --> C[zero]
    A --> D[negative]
```

---

## 1. Integers as Mathematical Objects

An integer represents a whole number on the number line.

```mermaid
flowchart LR
    A[-3] --> B[-2] --> C[-1] --> D[0] --> E[1] --> F[2] --> G[3]
```

Unlike floating-point numbers, integers have **no decimal point**.

```python
a = 5
b = -12
c = 0
```

---

## 2. Integer Arithmetic

Python supports the standard arithmetic operations on integers.

| Operation      | Symbol | Example  | Result |
| -------------- | ------ | -------- | ------ |
| addition       | `+`    | `3 + 2`  | `5`    |
| subtraction    | `-`    | `3 - 2`  | `1`    |
| multiplication | `*`    | `3 * 2`  | `6`    |
| division       | `/`    | `3 / 2`  | `1.5`  |
| floor division | `//`   | `3 // 2` | `1`    |
| remainder      | `%`    | `3 % 2`  | `1`    |
| exponentiation | `**`   | `3 ** 2` | `9`    |

Example:

```python
a = 7
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
```

---

## 3. Exactness of Integers

Python integers are **exact**.

For example:

```python
print(10 + 20)
print(2 * 100)
```

These results are represented precisely.

This differs from floating-point numbers, which may introduce rounding error.

---

## 4. Arbitrary Precision

Unlike many programming languages, Python integers are **arbitrary precision**.

That means Python integers can grow as large as memory allows.

```python
x = 10 ** 50
print(x)
```

Output:

```text
100000000000000000000000000000000000000000000000000
```

This is an important distinction from languages that restrict integers to fixed sizes such as 32-bit or 64-bit storage.

```mermaid
flowchart LR
    A[small int] --> B[larger int] --> C[very large int]
```

---

## 5. Integer Literals

Python supports several integer literal formats.

| Base        | Example  | Meaning |
| ----------- | -------- | ------- |
| decimal     | `42`     | base 10 |
| binary      | `0b1010` | base 2  |
| octal       | `0o52`   | base 8  |
| hexadecimal | `0x2A`   | base 16 |

Example:

```python
print(42)
print(0b101010)
print(0o52)
print(0x2A)
```

All of these represent the same value.

---

## 6. Underscores in Integer Literals

Python allows underscores in numeric literals to improve readability.

```python
population = 1_000_000
seconds = 86_400
```

These underscores do not affect the value.

```python
print(population)
print(seconds)
```

---

## 7. Integers in Boolean Contexts

Integers can appear in conditions.

* `0` behaves as `False`
* nonzero integers behave as `True`

Example:

```python
if 0:
    print("This will not print")

if 5:
    print("This will print")
```

---

## 8. Worked Examples

### Example 1: counting items

```python
apples = 5
oranges = 3
total = apples + oranges

print(total)
```

Output:

```text
8
```

### Example 2: even or odd

```python
n = 17

if n % 2 == 0:
    print("even")
else:
    print("odd")
```

Output:

```text
odd
```

### Example 3: power computation

```python
print(2 ** 10)
```

Output:

```text
1024
```

---

## 9. Common Pitfalls

### Using `/` when you want an integer result

```python
print(7 / 2)
```

This produces:

```text
3.5
```

Use `//` for floor division if an integer-style quotient is intended.

### Confusing `%` with percentage

The `%` operator computes the **remainder**, not a percentage.

---

## 10. Summary

Key ideas:

* `int` represents whole numbers
* integers support exact arithmetic
* Python integers have arbitrary precision
* integer literals can be written in multiple bases
* `0` is falsy and nonzero integers are truthy

The `int` type is the foundation for counting, indexing, and exact numeric computation.