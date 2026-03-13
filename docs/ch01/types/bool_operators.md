
# bool Operators

Python provides logical operators for combining and transforming Boolean expressions.

The three Boolean operators are:

- `and`
- `or`
- `not`

These operators are essential for building compound conditions.

```mermaid2
flowchart TD
    A[Boolean expressions]
    A --> B[and]
    A --> C[or]
    A --> D[not]
````

---

## 1. The `and` Operator

`and` returns `True` only if **both operands are true**.

```python
print(True and True)
print(True and False)
```

Output:

```text
True
False
```

Truth table:

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

Example:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
```

---

## 2. The `or` Operator

`or` returns `True` if **at least one operand is true**.

```python
print(True or False)
print(False or False)
```

Output:

```text
True
False
```

Truth table:

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

Example:

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today")
```

---

## 3. The `not` Operator

`not` reverses a Boolean value.

```python
print(not True)
print(not False)
```

Output:

```text
False
True
```

Truth table:

| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |

Example:

```python
logged_in = False

if not logged_in:
    print("Please sign in")
```

---

## 4. Short-Circuit Evaluation

Python’s Boolean operators use **short-circuit evaluation**.

This means evaluation stops as soon as the result is known.

### `and`

If the left side is false, Python does not need to evaluate the right side.

```python
False and print("hello")
```

The `print()` call is never executed.

### `or`

If the left side is true, Python does not need to evaluate the right side.

```python
True or print("hello")
```

Again, `print()` is not executed.

```mermaid2
flowchart LR
    A[left operand] --> B{result already known?}
    B -->|yes| C[stop]
    B -->|no| D[evaluate right operand]
```

Short-circuiting is useful for guard conditions.

```python
x = None

if x is not None and x > 0:
    print("positive")
```

---

## 5. Operators Return Values

In Python, `and` and `or` return one of their operands, not necessarily `True` or `False`.

```python
print(0 or 5)
print("" or "default")
print(3 and 7)
```

Output:

```text
5
default
7
```

This behavior is often used for fallback values.

```python
name = user_input or "Guest"
```

---

## 6. Worked Examples

### Example 1: combined condition

```python
age = 25
has_ticket = True

print(age >= 18 and has_ticket)
```

### Example 2: fallback value

```python
username = ""
display_name = username or "Anonymous"

print(display_name)
```

Output:

```text
Anonymous
```

### Example 3: negation

```python
is_busy = False
print(not is_busy)
```

Output:

```text
True
```

---

## 7. Common Pitfalls

### Assuming `and` and `or` always return `bool`

They often return one of the original operands.

### Forgetting precedence

`not` has higher precedence than `and`, which has higher precedence than `or`.

Use parentheses when clarity matters.

---

## 8. Summary

Key ideas:

* `and` requires both conditions to be true
* `or` requires at least one condition to be true
* `not` reverses truth value
* Python uses short-circuit evaluation
* `and` and `or` may return operands, not just Booleans

Boolean operators let programs express complex logic clearly and efficiently.