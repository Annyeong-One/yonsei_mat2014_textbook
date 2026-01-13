# Type Promotion

Type promotion is the automatic elevation of a value from a smaller or less precise data type to a larger or more precise data type during operations. Python performs this implicitly to prevent data loss.


## Promotion Hierarchy

Python follows a type promotion hierarchy for numeric types.

```
bool → int → float → complex
```

In mixed-type operations, the result assumes the type of the most general operand.

```python
print(1 + 1)      # 2 (int + int → int)
print(1. + 1.)    # 2.0 (float + float → float)
print(1 + 1.)     # 2.0 (int + float → float)
print(1. + 1)     # 2.0 (float + int → float)
```


## Promotion with Arithmetic Operators

Type promotion occurs with all arithmetic operators.

### Addition and Subtraction

```python
print(1 + 2.)     # 3.0 (int promoted to float)
print(5 - 1.5)    # 3.5 (int promoted to float)
```

### Multiplication

```python
print(2 * 3.)     # 6.0 (int promoted to float)
print(3 * (1+2j)) # (3+6j) (int promoted to complex)
```

### Division

True division always returns a float, even with integer operands.

```python
print(4 / 2)      # 2.0 (always float)
print(5 / 2)      # 2.5
```

Floor division preserves the more general type.

```python
print(7 // 2)     # 3 (int // int → int)
print(7 // 2.)    # 3.0 (int // float → float)
```


## Boolean in Numeric Context

Boolean values are promoted to integers in arithmetic operations.

```python
print(True + 2)   # 3 (True → 1)
print(False + 5)  # 5 (False → 0)
print(True * 10)  # 10
```

This enables useful patterns like counting True values.

```python
values = [True, False, True, True, False]
print(sum(values))  # 3
```


## Boolean in Conditional Context

In `if` statements, values are evaluated for truthiness without type conversion.

```python
if True:
    print("Executes")

if 1:
    print("Also executes")  # 1 is truthy

if 0:
    print("Does not execute")  # 0 is falsy
```


## Type Promotion vs Type Coercion

| Feature | Type Promotion | Type Coercion |
|---------|----------------|---------------|
| Direction | Implicit (automatic) | Explicit (manual) |
| Data Loss | No data loss | Possible data loss |
| Example | `1 + 2.0 → 3.0` | `int(3.7) → 3` |
| Purpose | Preserve precision | Format adjustment |

```python
# Type Promotion (implicit)
result = 1 + 1.
print(result, type(result))  # 2.0 <class 'float'>

# Type Coercion (explicit)
result = 1 + int(1.)
print(result, type(result))  # 2 <class 'int'>
```


## Why Type Promotion Matters

Type promotion ensures:

- **Consistency**: Mixed-type operations produce predictable results
- **Precision**: No accidental loss of decimal places
- **Safety**: Prevents overflow by promoting to larger types

```python
# Without promotion, this would lose precision
x = 5      # int
y = 3.2    # float
result = x + y
print(result)        # 8.2
print(type(result))  # <class 'float'>
```
