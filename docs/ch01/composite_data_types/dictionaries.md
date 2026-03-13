
# Dictionaries

A `dict` is a **mapping** from keys to values.

Unlike sequences, dictionaries are organized by keys rather than by numeric positions.

Examples:

```python
{"name": "Alice", "age": 25}
{}
````

```mermaid2
flowchart LR
    A[key] --> B[value]
    C[key] --> D[value]
    E[key] --> F[value]
```

---

## 1. What a Dictionary Represents

A dictionary stores associations.

For example:

```python
student = {
    "name": "Alice",
    "age": 25,
    "major": "math"
}
```

This structure maps each key to its corresponding value.

---

## 2. Accessing Values

Dictionary values are accessed by key.

```python
student = {"name": "Alice", "age": 25}

print(student["name"])
print(student["age"])
```

Output:

```text
Alice
25
```

---

## 3. Adding and Updating Entries

Dictionaries are mutable.

```python
student = {"name": "Alice"}
student["age"] = 25
student["name"] = "Bob"

print(student)
```

Output:

```text
{'name': 'Bob', 'age': 25}
```

---

## 4. Dictionary Methods

Common dictionary methods include:

| Method          | Purpose                 |
| --------------- | ----------------------- |
| `keys()`        | view keys               |
| `values()`      | view values             |
| `items()`       | view key-value pairs    |
| `get(key)`      | safe lookup             |
| `pop(key)`      | remove and return value |
| `update(other)` | merge entries           |

Example:

```python
data = {"a": 1, "b": 2}

print(data.keys())
print(data.get("c"))
```

---

## 5. Dictionaries and Hash Tables

At a conceptual level, Python dictionaries are implemented using **hash tables**.

This allows fast lookup by key.

For an introductory course, the most important practical idea is:

> dictionaries are designed for efficient key-based access.

---

## 6. Iterating Through Dictionaries

```python
person = {"name": "Alice", "age": 25}

for key, value in person.items():
    print(key, value)
```

This is one of the most common ways to traverse dictionary contents.

---

## 7. Worked Examples

### Example 1: store settings

```python
settings = {
    "theme": "dark",
    "volume": 80
}
print(settings["theme"])
```

### Example 2: safe lookup

```python
user = {"name": "Alice"}
print(user.get("email"))
```

Output:

```text
None
```

### Example 3: update a value

```python
scores = {"math": 90}
scores["math"] = 95
print(scores)
```

---

## 8. Common Pitfalls

### Accessing a missing key directly

```python
# user["email"]   # KeyError
```

Use `get()` when absence is possible.

### Assuming dictionary order is about numeric indexing

Dictionaries are mappings, not position-based containers.

---

## 9. Summary

Key ideas:

* dictionaries map keys to values
* values are accessed by keys, not indexes
* dictionaries are mutable
* dictionary methods support inspection and update
* dictionaries are designed for efficient lookup

Dictionaries are one of Python’s most powerful tools for representing structured information.