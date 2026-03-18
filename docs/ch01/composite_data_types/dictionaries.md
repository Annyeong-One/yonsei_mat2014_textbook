
# Dictionaries

A `dict` is a **mapping** from keys to values.

Unlike sequences, dictionaries are organized by keys rather than by numeric positions. Each key maps to a corresponding value.

```python
student = {
    "name": "Alice",
    "age": 25,
    "major": "math"
}
```

Since Python 3.7, dictionaries maintain insertion order.

```mermaid
flowchart TD
    A[dict]
    A --> B["key1 → value1"]
    A --> C["key2 → value2"]
    A --> D["key3 → value3"]
```

---

## 1. Accessing Values

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

Accessing a missing key raises `KeyError`.

```python
user = {"name": "Alice"}
user["email"]
```

Output:

```text
KeyError: 'email'
```

Use `get()` when absence is possible. The two-argument form provides a default value.

```python
user = {"name": "Alice"}

print(user.get("email"))
print(user.get("email", "not provided"))
```

Output:

```text
None
not provided
```

---

## 2. Adding and Updating Entries

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

The `update()` method merges entries from another dictionary.

```python
defaults = {"theme": "light", "volume": 50}
overrides = {"volume": 80, "lang": "en"}
defaults.update(overrides)

print(defaults)
```

Output:

```text
{'theme': 'light', 'volume': 80, 'lang': 'en'}
```

---

## 3. Dictionary Methods

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
print(data.values())
```

Output:

```text
dict_keys(['a', 'b'])
dict_values([1, 2])
```

Note that `keys()` and `values()` return view objects, not lists. Wrap with `list()` if a list is needed.

---

## 4. Key Hashability Requirement

Like [set](sets.md) members, dictionary keys must be hashable. Strings, integers, and tuples can be keys; lists cannot.

```python
d = {}
d[[1, 2]] = "value"
```

Output:

```text
TypeError: unhashable type: 'list'
```

See [Hashing and Hash Tables](../../ch02/composites/hashing_deep_dive.md) for a full explanation of how hashing works.

---

## 5. Why Dictionaries Are Fast: O(1) Lookup

Dictionaries are one of Python's most important data structures because they support
**O(1) key lookup** — finding a value takes the same time whether the dictionary has
10 entries or 10 million.

To understand why, it helps to compare three approaches to finding something by name.

### Approach 1: scanning a list — O(n)

The simplest approach is a list of pairs searched from the start:
```python
phonebook = [("Alice", "010-1234"), ("Bob", "010-5678"), ("Charlie", "010-9999")]

def find(phonebook, name):
    for entry in phonebook:
        if entry[0] == name:
            return entry[1]

print(find(phonebook, "Charlie"))
```

Output:
```text
010-9999
```

To find "Charlie", Python checks Alice, then Bob, then Charlie. With a million entries,
finding the last one requires a million comparisons. Cost grows linearly with size: **O(n)**.

### Approach 2: binary search on a sorted list — O(log n)

If the list is sorted, Python can use binary search — repeatedly cutting the search
space in half:
```
["Alice", "Bob", "Charlie", "Diana", "Eve"]
  search "Diana": check middle ("Charlie") → too early → check right half
                  check middle ("Diana") → found
```

Much faster, but still *searching* — cost grows with size, just slowly: **O(log n)**.
A list of one million entries requires at most 20 comparisons.

### Approach 3: direct addressing — O(1)

The fastest possible lookup requires no searching at all. Consider a simple array
where position *is* the address:
```python
data = [None] * 5
data[2] = "Alice"

print(data[2])   # instant — no search, goes directly to position 2
```

Output:
```text
Alice
```

Regardless of array size, `data[2]` is always one step. This is **O(1)** — constant time.

### How dictionaries achieve O(1)

A dictionary applies this direct-addressing idea to arbitrary keys like strings and
integers. Internally, Python converts each key into a position, then stores and retrieves
the value at that position directly — no scanning, no searching.
```python
phonebook = {"Alice": "010-1234", "Bob": "010-5678", "Charlie": "010-9999"}

print(phonebook["Charlie"])   # goes directly to Charlie's slot — no search
```

Output:
```text
010-9999
```

The conversion from key to position is fast and fixed-cost regardless of dictionary
size. This is why lookup stays O(1) whether the dictionary has 10 entries or 10 million.

| Structure     | Strategy              | Cost     |
| ------------- | --------------------- | -------- |
| list          | scan from start       | O(n)     |
| sorted list   | binary search         | O(log n) |
| dict          | direct addressing     | O(1)     |

How Python converts a key like `"Alice"` into a position is the job of the **hash
function** — covered in detail in
[Hashing and Hash Tables](../../ch02/composites/hashing_deep_dive.md).

---

## 6. Iterating Through Dictionaries

```python
person = {"name": "Alice", "age": 25}

for key, value in person.items():
    print(key, value)
```

Output:

```text
name Alice
age 25
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

Output:

```text
dark
```

### Example 2: safe lookup

```python
user = {"name": "Alice"}
print(user.get("email", "not provided"))
```

Output:

```text
not provided
```

### Example 3: update a value

```python
scores = {"math": 90}
scores["math"] = 95
print(scores)
```

Output:

```text
{'math': 95}
```

---

## 8. Common Pitfalls

### Accessing a missing key directly

As shown in Section 1, bracket access on a missing key raises `KeyError`. Use `get()` for safe access.

### Assuming numeric indexing works

Dictionaries are mappings, not position-based containers. `student[0]` does not return the first value — it looks for the key `0`.

```python
student = {"name": "Alice", "age": 25}
student[0]
```

Output:

```text
KeyError: 0
```

---

## 9. Summary

Key ideas:

- dictionaries map keys to values
- values are accessed by keys, not positions
- dictionaries are mutable and maintain insertion order
- keys must be hashable — lists cannot be keys
- dictionaries are designed for O(1) lookup

Dictionaries are one of Python's most powerful tools for representing structured information. Dictionary values can themselves be dictionaries — nested structures are covered in [Nested Data Structures](../../ch02/composites/nested_structures.md). Dictionaries can also be built concisely using comprehensions — see [Comprehensions](comprehensions.md). This page follows [Sets](sets.md) in the composite data types section.
