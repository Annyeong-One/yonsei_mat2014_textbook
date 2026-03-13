
# Sets

A `set` is an **unordered collection of unique elements**.

Sets are useful when the main concern is not order, but **membership and uniqueness**.

Examples:

```python
{1, 2, 3}
set()
````

```mermaid2
flowchart TD
    A[set]
    A --> B[unordered]
    A --> C[unique elements]
    A --> D[fast membership testing]
```

---

## 1. Uniqueness

Sets automatically remove duplicates.

```python
data = {1, 2, 2, 3, 3, 3}
print(data)
```

Output:

```text
{1, 2, 3}
```

This makes sets very useful for eliminating repeated values.

---

## 2. Membership Testing

Sets are especially good for membership checks.

```python
vowels = {"a", "e", "i", "o", "u"}

print("a" in vowels)
print("z" in vowels)
```

Output:

```text
True
False
```

---

## 3. Creating Sets

Sets can be written with braces.

```python
colors = {"red", "green", "blue"}
```

An empty set must be created with `set()`.

```python
empty = set()
```

Using `{}` creates an empty dictionary, not an empty set.

---

## 4. Set Operations

Sets support important mathematical operations.

| Operation    | Symbol | Meaning                      |              |
| ------------ | ------ | ---------------------------- | ------------ |
| union        | `      | `                            | all elements |
| intersection | `&`    | common elements              |              |
| difference   | `-`    | elements in first not second |              |

Example:

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
print(a - b)
```

---

## 5. Common Set Methods

| Method       | Purpose                  |
| ------------ | ------------------------ |
| `add(x)`     | add element              |
| `remove(x)`  | remove element           |
| `discard(x)` | remove if present        |
| `pop()`      | remove arbitrary element |
| `clear()`    | remove all elements      |

Example:

```python
s = {1, 2}
s.add(3)
print(s)
```

---

## 6. Worked Examples

### Example 1: remove duplicates

```python
nums = [1, 2, 2, 3, 3]
unique = set(nums)
print(unique)
```

### Example 2: membership test

```python
allowed = {"admin", "editor"}

if "admin" in allowed:
    print("granted")
```

### Example 3: intersection

```python
a = {"red", "green"}
b = {"green", "blue"}

print(a & b)
```

Output:

```text
{'green'}
```

---

## 7. Common Pitfalls

### Expecting order

Sets are unordered collections.

### Using `{}` for an empty set

`{}` creates a dictionary, not a set.

### Assuming all objects can be stored in a set

Set elements must be hashable.

---

## 8. Summary

Key ideas:

* sets store unique elements
* sets are unordered
* membership testing is a major strength of sets
* set operations reflect mathematical set ideas

Sets are especially useful for uniqueness, filtering, and fast membership logic.