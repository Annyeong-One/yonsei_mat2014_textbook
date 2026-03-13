
# Composite Data Type Examples

This section gathers practical examples showing how tuples, lists, dictionaries, sets, and comprehensions work together.

---

## 1. List Example

```python
scores = [80, 90, 75]
scores.append(88)

print(scores)
print(scores[1])
````

Output:

```text
[80, 90, 75, 88]
90
```

---

## 2. Tuple Example

```python
point = (3, 4)
x, y = point

print(x)
print(y)
```

Output:

```text
3
4
```

---

## 3. Dictionary Example

```python
student = {
    "name": "Alice",
    "age": 20
}

print(student["name"])
student["age"] = 21
print(student)
```

---

## 4. Set Example

```python
tags = {"python", "math", "python"}
print(tags)
print("math" in tags)
```

Output:

```text
{'python', 'math'}
True
```

---

## 5. List Comprehension Example

```python
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

## 6. Dictionary Comprehension Example

```python
lengths = {word: len(word) for word in ["cat", "tiger", "lion"]}
print(lengths)
```

---

## 7. Set Comprehension Example

```python
remainders = {x % 3 for x in range(10)}
print(remainders)
```

Output:

```text
{0, 1, 2}
```

---

## 8. Practical Example: Count Characters

```python
text = "banana"
counts = {}

for ch in text:
    counts[ch] = counts.get(ch, 0) + 1

print(counts)
```

Output:

```text
{'b': 1, 'a': 3, 'n': 2}
```

---

## 9. Practical Example: Unique Sorted Words

```python
words = ["apple", "banana", "apple", "cherry"]
unique_words = sorted(set(words))

print(unique_words)
```

Output:

```text
['apple', 'banana', 'cherry']
```

---

## 10. Summary

These examples show that composite data types allow programs to:

* store collections of values
* represent fixed records
* model key-value relationships
* eliminate duplicates
* transform data concisely

Composite data types are essential tools for almost every nontrivial Python program.

