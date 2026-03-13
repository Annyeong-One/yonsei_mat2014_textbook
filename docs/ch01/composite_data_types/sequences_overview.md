

# Sequences Overview

Python includes several data types that store **multiple values inside a single object**.

These are called **composite data types**.

Some of the most important composite types are:

- `tuple`
- `list`
- `dict`
- `set`

Among these, tuples and lists are both **sequences**, meaning they store elements in order.

```mermaid2
flowchart TD
    A[Composite Data Types]
    A --> B[Sequences]
    A --> C[Mappings]
    A --> D[Sets]

    B --> E[tuple]
    B --> F[list]
    C --> G[dict]
    D --> H[set]
````

---

## 1. What Is a Sequence?

A sequence is an ordered collection of elements.

This means:

* elements have positions
* indexing is possible
* slicing is possible
* iteration follows a fixed order

Examples:

```python
numbers = [10, 20, 30]
letters = ("a", "b", "c")
text = "Python"
```

All three of these are sequences.

---

## 2. Common Sequence Operations

Sequences often support these operations:

| Operation  | Example        | Meaning            |
| ---------- | -------------- | ------------------ |
| indexing   | `seq[0]`       | first element      |
| slicing    | `seq[1:3]`     | subsequence        |
| length     | `len(seq)`     | number of elements |
| membership | `x in seq`     | containment test   |
| iteration  | `for x in seq` | visit elements     |

Example:

```python
data = [10, 20, 30, 40]

print(data[0])
print(data[1:3])
print(len(data))
print(20 in data)
```

---

## 3. Mutable vs Immutable Sequences

Not all sequences behave the same way.

| Type    | Ordered | Mutable |
| ------- | ------- | ------- |
| `tuple` | yes     | no      |
| `list`  | yes     | yes     |
| `str`   | yes     | no      |

A mutable sequence can be changed after creation.
An immutable sequence cannot.

This distinction is one of the most important ideas in Python’s data model.

---

## 4. Why Composite Types Matter

Composite types allow programs to represent structured information.

Examples:

* a list of scores
* a tuple of coordinates
* a dictionary of settings
* a set of unique tags

Without composite data types, programs would struggle to organize real-world data effectively.

---

## 5. Worked Examples

### Example 1: sequence indexing

```python
values = [5, 10, 15]
print(values[1])
```

Output:

```text
10
```

### Example 2: membership

```python
letters = ("a", "b", "c")
print("b" in letters)
```

Output:

```text
True
```

### Example 3: slicing

```python
numbers = [1, 2, 3, 4]
print(numbers[1:3])
```

Output:

```text
[2, 3]
```

---

## 6. Summary

Key ideas:

* composite data types store multiple values
* tuples and lists are sequences
* sequences are ordered
* some sequences are mutable, others are immutable
* composite types are essential for structured programming

Composite data types make Python programs capable of representing collections, relationships, and structured data.