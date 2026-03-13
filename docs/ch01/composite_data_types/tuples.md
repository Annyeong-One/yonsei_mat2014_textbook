
# Tuples

A `tuple` is an **ordered, immutable sequence**.

Tuples are useful when a collection of values should stay fixed after creation.

Examples:

```python
(1, 2, 3)
("a", "b", "c")
()
````

```mermaid2
flowchart TD
    A[tuple]
    A --> B[ordered]
    A --> C[immutable]
```

---

## 1. Creating Tuples

Tuples are usually written with parentheses.

```python
point = (3, 4)
colors = ("red", "green", "blue")
```

A one-element tuple requires a trailing comma.

```python
single = (5,)
```

Without the comma, Python interprets it as an ordinary grouped expression.

---

## 2. Indexing and Slicing

Tuples support indexing and slicing just like other sequences.

```python
t = ("a", "b", "c", "d")

print(t[0])
print(t[1:3])
```

Output:

```text
a
('b', 'c')
```

---

## 3. Immutability

Tuples cannot be changed after creation.

```python
t = (1, 2, 3)

# t[0] = 10   # TypeError
```

This immutability makes tuples useful for fixed records and safer data sharing.

---

## 4. Tuple Packing and Unpacking

Python supports packing multiple values into a tuple and unpacking them into variables.

```python
point = 3, 4
x, y = point

print(x)
print(y)
```

Output:

```text
3
4
```

This is one of the most elegant features of Python.

---

## 5. When Tuples Are Useful

Tuples are often used for:

* coordinates
* RGB color values
* return values from functions
* fixed configuration data

Because tuples are immutable, they communicate that the structure is intended to stay stable.

---

## 6. Worked Examples

### Example 1: coordinate pair

```python
point = (10, 20)
print(point[0], point[1])
```

### Example 2: unpacking

```python
person = ("Alice", 25)
name, age = person
print(name, age)
```

### Example 3: function returning two values

```python
def min_max(a, b):
    if a < b:
        return a, b
    return b, a

print(min_max(8, 3))
```

Output:

```text
(3, 8)
```

---

## 7. Common Pitfalls

### Forgetting the comma in a one-element tuple

```python
(5)
```

is not a tuple, but:

```python
(5,)
```

is.

### Assuming immutability means contents can never contain mutable objects

A tuple itself is immutable, but it may contain mutable elements such as lists.

---

## 8. Summary

Key ideas:

* tuples are ordered and immutable
* tuples support indexing, slicing, and iteration
* tuple packing and unpacking are very useful
* tuples are ideal for fixed collections of values

Tuples provide a compact and reliable way to represent stable structured data.