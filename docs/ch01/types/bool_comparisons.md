

# bool Comparisons

Comparisons test relationships between values and produce Boolean results.

These results are central to decision making in Python.

Common comparison operators include:

| Operator | Meaning |
|---|---|
| `==` | equal to |
| `!=` | not equal to |
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |

```mermaid2
flowchart TD
    A[Two values] --> B[comparison operator]
    B --> C[Boolean result]
````

---

## 1. Equality and Inequality

Equality checks whether two values are the same.

```python
print(5 == 5)
print(5 != 3)
```

Output:

```text
True
True
```

These comparisons work across many types.

```python
print("a" == "a")
print([1, 2] == [1, 2])
```

---

## 2. Ordering Comparisons

Ordering operators compare relative size.

```python
print(3 < 5)
print(10 > 7)
print(4 <= 4)
print(8 >= 10)
```

Output:

```text
True
True
True
False
```

These are especially common in loops and conditions.

---

## 3. Chained Comparisons

Python supports chained comparisons.

```python
x = 7
print(0 < x < 10)
```

Output:

```text
True
```

This is equivalent to:

```python
print(0 < x and x < 10)
```

but is often more readable.

---

## 4. Comparing Different Types

Some comparisons between unlike types are allowed, while others are not.

```python
print(3 == 3.0)
```

Output:

```text
True
```

But ordering unrelated types may fail.

```python
# "3" < 4   # TypeError
```

Python does not impose arbitrary ordering across unrelated types.

---

## 5. Identity vs Equality

Python distinguishes equality from identity.

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

* `==` checks whether values are equal
* `is` checks whether two names refer to the same object

This distinction is especially important with `None`.

---

## 6. Membership Comparisons

Python also provides membership tests.

| Operator | Meaning          |
| -------- | ---------------- |
| `in`     | value is present |
| `not in` | value is absent  |

Example:

```python
print("a" in "cat")
print(5 in [1, 2, 5])
```

Output:

```text
True
True
```

---

## 7. Worked Examples

### Example 1: password check

```python
password = "secret"

print(password == "secret")
```

Output:

```text
True
```

### Example 2: numeric range

```python
score = 82

if 80 <= score < 90:
    print("B range")
```

### Example 3: membership

```python
colors = ["red", "green", "blue"]

if "green" in colors:
    print("found")
```

---

## 8. Common Pitfalls

### Using `is` instead of `==`

For value comparison, use `==`, not `is`.

### Comparing unrelated types with ordering operators

Expressions like `"10" < 20` are invalid.

---

## 9. Summary

Key ideas:

* comparisons produce Boolean results
* equality and ordering comparisons are fundamental to control flow
* chained comparisons improve readability
* `==` and `is` have different meanings
* membership tests also produce Boolean values

Comparison operators allow Python programs to reason about relationships between values.