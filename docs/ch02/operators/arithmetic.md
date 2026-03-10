# Arithmetic Operators


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Arithmetic operators perform mathematical operations on numeric values.


## Operator Summary

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `3 + 2` | `5` |
| `-` | Subtraction | `3 - 2` | `1` |
| `*` | Multiplication | `3 * 2` | `6` |
| `/` | Division | `7 / 2` | `3.5` |
| `//` | Floor Division | `7 // 2` | `3` |
| `%` | Modulo | `7 % 2` | `1` |
| `**` | Exponentiation | `3 ** 2` | `9` |


## Basic Operations

```python
a = 10
b = 3

print(a + b)   # 13 (addition)
print(a - b)   # 7  (subtraction)
print(a * b)   # 30 (multiplication)
print(a / b)   # 3.333... (true division)
print(a // b)  # 3  (floor division)
print(a % b)   # 1  (remainder)
print(a ** b)  # 1000 (10^3)
```


## Division Types

### True Division (`/`)

Always returns a float:

```python
print(10 / 2)   # 5.0
print(7 / 2)    # 3.5
print(1 / 3)    # 0.333...
```

### Floor Division (`//`)

Returns the largest integer less than or equal to the result:

```python
print(7 // 2)    # 3
print(10 // 3)   # 3
print(-7 // 2)   # -4 (rounds toward negative infinity)
```

### Modulo (`%`)

Returns the remainder after division:

```python
print(7 % 2)     # 1
print(10 % 3)    # 1
print(15 % 5)    # 0
```


## Unary Operators

```python
x = 5
print(+x)   # 5  (unary plus)
print(-x)   # -5 (unary minus)
```


## Exponentiation

```python
print(2 ** 3)    # 8
print(2 ** 0.5)  # 1.414... (square root)
print(10 ** -2)  # 0.01

# Right-to-left associativity
print(2 ** 3 ** 2)   # 512 (2^9, not 8^2)
```


## Assignment Operators

Combine assignment with arithmetic:

| Operator | Example | Equivalent To |
|----------|---------|---------------|
| `+=` | `x += 2` | `x = x + 2` |
| `-=` | `x -= 2` | `x = x - 2` |
| `*=` | `x *= 2` | `x = x * 2` |
| `/=` | `x /= 2` | `x = x / 2` |
| `//=` | `x //= 2` | `x = x // 2` |
| `%=` | `x %= 2` | `x = x % 2` |
| `**=` | `x **= 2` | `x = x ** 2` |

```python
x = 10
x += 5   # x = 15
x *= 2   # x = 30
x //= 4  # x = 7
```


## Type Behavior

### Integer Operations

```python
print(5 + 3)     # 8 (int)
print(5 * 3)     # 15 (int)
print(5 // 3)    # 1 (int)
print(5 / 3)     # 1.666... (float, always)
```

### Float Operations

```python
print(5.0 + 3)   # 8.0 (float)
print(5 * 3.0)   # 15.0 (float)
```

### Complex Operations

```python
print((1+2j) + (3+4j))  # (4+6j)
print((1+2j) * (3+4j))  # (-5+10j)
```


## Common Use Cases

### Check Even/Odd

```python
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Wrap Around (Circular)

```python
# Cycle through 0-9
index = (index + 1) % 10
```

### Integer Division with Remainder

```python
quotient, remainder = divmod(17, 5)
print(quotient, remainder)  # 3, 2
```


## Summary

- `/` always returns float
- `//` returns floor (rounds toward negative infinity)
- `%` returns remainder
- `**` is right-associative
- Use `divmod()` for both quotient and remainder
