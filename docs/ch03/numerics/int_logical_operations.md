# Logical Operations

Python's logical operators `or`, `and`, and `not` can work with integers because non-zero integers are **truthy** and `0` is **falsy**.

---

## Truthiness

Integers are treated as Boolean values in logical operations.

### 1. Truthy vs Falsy

- **Non-zero integer** = truthy (True)
- **Zero (0)** = falsy (False)

This allows logical operators to manipulate integer values directly.

---

## The or Operator

The `or` operator returns the first truthy value or the last value if all are falsy.

### 1. Evaluation Rules

$$\begin{array}{clccccccccccccccc}
\text{a}&&&\text{a or b}\\
\text{True}&\text{(a or b) is True due to a}&\Rightarrow&\text{returns a}\\
\text{False}&\text{(a or b) depends on b}&\Rightarrow&\text{returns b}\\
\end{array}$$

### 2. Non-zero First

```python
def main():
    a = 156
    b = 52
    c = a or b
    print(c)  # Output: 156

if __name__ == "__main__":
    main()
```

### 3. Zero First

```python
def main():
    a = 0
    b = 52
    c = a or b
    print(c)  # Output: 52

if __name__ == "__main__":
    main()
```

### 4. Basic Example

Since `a` is non-zero (truthy), the `or` operator immediately returns `a`:

```python
a = 5  # Non-zero, evaluates to True
b = 0  # Zero, evaluates to False

result = a or b  # Since 'a' is truthy, 'a' is returned
print(result)  # Output: 5
```

If both operands are zero:

```python
a = 0  # Falsy
b = 0  # Falsy

result = a or b  # Both falsy, so returns 'b'
print(result)  # Output: 0
```

**Key Takeaway:** The `or` operator returns the first non-zero value, or the last value if all are zero.

---

## The and Operator

The `and` operator returns the second operand if both are truthy, otherwise returns the first falsy operand.

### 1. Evaluation Rules

$$\begin{array}{clccccccccccccccc}
\text{a}&&&\text{a and b}\\
\text{True}&\text{(a and b) depends on b}&\Rightarrow&\text{returns b}\\
\text{False}&\text{(a and b) is False due to a}&\Rightarrow&\text{returns a}\\
\end{array}$$

### 2. Both Non-zero

```python
def main():
    a = 156
    b = 52
    print(a and b)  # Output: 52

if __name__ == "__main__":
    main()
```

### 3. First Zero

```python
def main():
    a = 0
    b = 52
    print(a and b)  # Output: 0

if __name__ == "__main__":
    main()
```

### 4. Basic Example

Both `a` and `b` are truthy, so `b` is returned:

```python
a = 5  # Non-zero, evaluates to True
b = 3  # Non-zero, evaluates to True

result = a and b  # Both truthy, so 'b' is returned
print(result)  # Output: 3
```

If the first operand is zero:

```python
a = 0  # Falsy
b = 10  # Non-zero, evaluates to True

result = a and b  # Since 'a' is falsy, result is 'a' (0)
print(result)  # Output: 0
```

**Key Takeaway:** The `and` operator returns the second operand if both are non-zero; otherwise, it returns the first operand.

---

## The not Operator

The `not` operator inverts the truthiness of a value.

### 1. Evaluation Rules

$$\begin{array}{clccccccccccccccc}
\text{a}&&&\text{not a}\\
\text{True}&\text{(not a) is False}&\Rightarrow&\text{returns False}\\
\text{False}&\text{(not a) is True}&\Rightarrow&\text{returns True}\\
\end{array}$$

### 2. Non-zero Input

```python
def main():
    a = 3
    print(not a)  # Output: False

if __name__ == "__main__":
    main()
```

### 3. Zero Input

```python
def main():
    a = 0
    print(not a)  # Output: True

if __name__ == "__main__":
    main()
```

### 4. Basic Example

```python
a = 5  # Non-zero, evaluates to True

result = not a  # Inverts truthiness
print(result)  # Output: False
```

For zero:

```python
b = 0  # Falsy

result = not b  # Inverts truthiness
print(result)  # Output: True
```

**Key Takeaway:** `not` inverts the truthiness—non-zero integers become `False`, and zero becomes `True`.

---

## Combined Operations

Logical operators can be combined for complex expressions.

### 1. or and and

```python
a = 0
b = 3
c = 5

result = a or (b and c)  # 'b and c' returns 5, then 'a or 5' returns 5
print(result)  # Output: 5
```

### 2. not and and

```python
a = 0
b = 5

result = not (a and b)  # 'a and b' is 0, so 'not 0' is True
print(result)  # Output: True
```

### 3. Nested Logic

```python
x = 5
y = 0
z = 10

result = not x and (y or z)  # 'not x' is False, 'y or z' is 10, False and 10 is False
print(result)  # Output: False
```

---

## Short-Circuit

Python uses short-circuit evaluation for efficiency.

### 1. Short-Circuit or

The `or` operator stops evaluating once it finds a truthy value.

```python
a = 5
b = expensive_function()  # Not called if a is truthy

result = a or b  # b is never evaluated because a is truthy
```

### 2. Short-Circuit and

The `and` operator stops evaluating once it finds a falsy value.

```python
a = 0
b = expensive_function()  # Not called if a is falsy

result = a and b  # b is never evaluated because a is falsy
```

---

## Conclusion

In Python, logical operations with integers leverage implicit truthiness conversion. The `or` operator returns the first truthy value, `and` checks if both are truthy, and `not` inverts truthiness. These operations are essential for making decisions and controlling logic flow, all while using Python's treatment of integers as Boolean values.
