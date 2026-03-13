
# Ternary Expressions

A ternary expression provides a concise way to choose between two values.

Syntax:

````

value_if_true if condition else value_if_false

````

---

## Example

```python
age = 20

status = "adult" if age >= 18 else "minor"

print(status)
````

Output:

```
adult
```

---

## Numeric Example

```python
x = 10
y = 20

maximum = x if x > y else y
```

---

## List Comprehension Example

```python
numbers = [1,2,3,4]

labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
```

Ternary expressions are best used for **simple conditions**.

