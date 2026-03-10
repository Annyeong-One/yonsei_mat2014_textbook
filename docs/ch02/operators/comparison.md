# Comparison Operators


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Comparison operators compare values and return `True` or `False`.


## Operator Summary

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `==` | Equal to | `3 == 3` | `True` |
| `!=` | Not equal to | `3 != 2` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `3 > 5` | `False` |
| `<=` | Less than or equal | `3 <= 3` | `True` |
| `>=` | Greater than or equal | `5 >= 3` | `True` |


## Numeric Comparison

```python
print(5 > 3)    # True
print(5 < 3)    # False
print(5 >= 5)   # True
print(5 <= 4)   # False
print(5 == 5)   # True
print(5 != 5)   # False
```

### Integer and Float

Python handles mixed numeric types:

```python
print(1 == 1.0)   # True
print(1 < 1.0)    # False
print(1 <= 1.0)   # True
```


## Boolean Comparison

Booleans can be compared:

```python
print(True == True)    # True
print(True == False)   # False
print(True != False)   # True
```


## Chained Comparisons

Python allows chaining comparisons:

```python
print(1 < 2 < 3)           # True
print(1 < 2 < 3 < 4 < 5)   # True
print(1 < 5 > 3)           # True (1 < 5 and 5 > 3)
```

This is equivalent to:

```python
print(1 < 2 and 2 < 3)     # True
```

### Practical Example

```python
age = 25
if 18 <= age <= 65:
    print("Working age")
```


## Comparison Gotchas

### Floating-Point Precision

```python
print(0.1 + 0.2 == 0.3)   # False!
print(0.1 + 0.2)          # 0.30000000000000004
```

Use approximate comparison:

```python
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

### Comparison Order

```python
# These are equivalent
print(10 <= 20 == 30 > 40)
print((10 <= 20) and (20 == 30) and (30 > 40))  # False
```


## Equality vs Identity

| Operator | Compares | Example |
|----------|----------|---------|
| `==` | Values | `[1,2] == [1,2]` → `True` |
| `is` | Identity | `[1,2] is [1,2]` → `False` |

See [Identity Operators](identity.md) for details.


## Comparison with Different Types

### Numeric Types Mix

```python
print(1 == 1.0 == True)  # True (True is 1)
print(0 == False)         # True
```

### String vs Number

```python
# Python 3: Cannot compare
print("5" > 3)  # TypeError
```

### None Comparison

```python
print(None == None)  # True
print(None is None)  # True (preferred)
```


## Use in Control Flow

```python
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
```


## Summary

- `==` compares values, `is` compares identity
- Chained comparisons: `a < b < c` means `a < b and b < c`
- Be careful with float comparison (use `math.isclose`)
- Cannot compare incompatible types in Python 3
