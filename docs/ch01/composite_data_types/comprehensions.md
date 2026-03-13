
# Comprehensions

A **comprehension** is a compact way to build a new collection from an iterable.

Python supports comprehensions for:

- lists
- sets
- dictionaries

They provide a concise alternative to some loops.

```mermaid2
flowchart LR
    A[iterable] --> B[comprehension]
    B --> C[new collection]
````

---

## 1. List Comprehensions

A list comprehension creates a list.

```python
squares = [x * x for x in range(5)]
print(squares)
```

Output:

```text
[0, 1, 4, 9, 16]
```

Equivalent loop:

```python
squares = []
for x in range(5):
    squares.append(x * x)
```

---

## 2. Filtering in Comprehensions

A condition can be added.

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
```

Output:

```text
[0, 2, 4, 6, 8]
```

---

## 3. Set Comprehensions

A set comprehension creates a set.

```python
lengths = {len(word) for word in ["cat", "dog", "apple"]}
print(lengths)
```

Because sets keep unique values, duplicates are removed automatically.

---

## 4. Dictionary Comprehensions

A dictionary comprehension creates a mapping.

```python
squares = {x: x * x for x in range(5)}
print(squares)
```

Output:

```text
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## 5. When Comprehensions Are Helpful

Comprehensions are most helpful when:

* the transformation is simple
* the resulting collection is easy to understand
* the expression remains readable

When a comprehension becomes too complex, an ordinary loop may be clearer.

---

## 6. Worked Examples

### Example 1: uppercase words

```python
words = ["python", "is", "fun"]
upper_words = [w.upper() for w in words]
print(upper_words)
```

### Example 2: positive numbers only

```python
nums = [-2, -1, 0, 1, 2]
positive = [x for x in nums if x > 0]
print(positive)
```

### Example 3: word lengths

```python
length_map = {word: len(word) for word in ["cat", "horse"]}
print(length_map)
```

---

## 7. Common Pitfalls

### Making comprehensions too complex

Readability matters more than compactness.

### Forgetting collection type

Square brackets create lists, braces may create sets or dictionaries depending on syntax.

---

## 8. Summary

Key ideas:

* comprehensions create collections concisely
* list comprehensions build lists
* set comprehensions build sets
* dictionary comprehensions build mappings
* comprehensions should remain readable

Comprehensions are one of Python’s most expressive tools for transforming data.