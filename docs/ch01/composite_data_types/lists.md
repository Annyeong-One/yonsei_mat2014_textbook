
# Lists

A `list` is an **ordered, mutable sequence**.

Lists are one of the most widely used data structures in Python because they are flexible and easy to modify.

Examples:

```python
[1, 2, 3]
["a", "b", "c"]
[]
````

```mermaid2
flowchart TD
    A[list]
    A --> B[ordered]
    A --> C[mutable]
    A --> D[dynamic size]
```

---

## 1. Creating Lists

Lists are written with square brackets.

```python
numbers = [10, 20, 30]
names = ["Alice", "Bob", "Charlie"]
empty = []
```

A list may contain values of mixed types, although in practice lists often hold related elements.

---

## 2. Indexing and Slicing

Lists support indexing and slicing.

```python
values = [10, 20, 30, 40]

print(values[0])
print(values[1:3])
```

Output:

```text
10
[20, 30]
```

---

## 3. Mutability

Unlike tuples, lists can be modified.

```python
values = [10, 20, 30]
values[1] = 99

print(values)
```

Output:

```text
[10, 99, 30]
```

This mutability is one of the defining features of lists.

---

## 4. Common List Methods

Lists provide many useful methods.

| Method             | Purpose                       |
| ------------------ | ----------------------------- |
| `append(x)`        | add element at end            |
| `extend(iterable)` | add multiple elements         |
| `insert(i, x)`     | insert at position            |
| `remove(x)`        | remove first matching element |
| `pop()`            | remove and return element     |
| `sort()`           | sort in place                 |
| `reverse()`        | reverse in place              |

Example:

```python
numbers = [3, 1, 2]
numbers.append(4)
numbers.sort()

print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

---

## 5. Lists as Dynamic Arrays

Conceptually, a Python list behaves like a dynamic array.

This means:

* it stores elements in order
* it can grow and shrink
* indexing is efficient
* appending is common and practical

At an introductory level, it is enough to understand that lists are designed to support flexible ordered collections.

---

## 6. Iteration

Lists are often used with loops.

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

---

## 7. Worked Examples

### Example 1: append values

```python
items = []
items.append("pen")
items.append("paper")
print(items)
```

Output:

```text
['pen', 'paper']
```

### Example 2: modify an element

```python
scores = [80, 90, 70]
scores[2] = 75
print(scores)
```

### Example 3: remove last value

```python
data = [1, 2, 3]
x = data.pop()
print(x)
print(data)
```

Output:

```text
3
[1, 2]
```

---

## 8. Common Pitfalls

### Confusing `append()` with `extend()`

`append()` adds one object.
`extend()` adds multiple elements from an iterable.

### Modifying a list while iterating over it

This can lead to confusing behavior and should be done carefully.

---

## 9. Summary

Key ideas:

* lists are ordered and mutable
* lists support indexing, slicing, and iteration
* lists can grow and shrink dynamically
* list methods make modification convenient

Lists are the standard tool for storing ordered collections that need to change over time.