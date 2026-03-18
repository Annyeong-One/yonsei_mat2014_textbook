
# str Operators and Membership

Strings support several important operators:

- concatenation with `+`
- repetition with `*`
- membership tests with `in` and `not in`

These operations allow programs to combine, repeat, and inspect text.

```mermaid
flowchart TD
    A[String operations]
    A --> B[Concatenation]
    A --> C[Repetition]
    A --> D[Membership]
````

---

## 1. Concatenation

Concatenation joins strings together.

```python
a = "Hello"
b = "World"

print(a + " " + b)
```

Output:

```text
Hello World
```

The `+` operator creates a new string.

---

## 2. Repetition

The `*` operator repeats a string.

```python
print("ha" * 3)
```

Output:

```text
hahaha
```

This is useful for simple pattern generation.

```python
print("=" * 10)
```

Output:

```text
==========
```

---

## 3. Membership Testing

The `in` operator checks whether a substring appears inside a string.

```python
text = "Python programming"

print("Python" in text)
print("java" in text)
```

Output:

```text
True
False
```

The `not in` operator checks for absence.

```python
print("java" not in text)
```

Output:

```text
True
```

---

## 4. Membership Works on Characters and Substrings

Membership is not limited to single characters.

```python
word = "banana"

print("a" in word)
print("ana" in word)
```

Output:

```text
True
True
```

---

## 5. Operators Produce New Strings

Concatenation and repetition do not modify the original string.

```python
name = "Py"
new_name = name + "thon"

print(name)
print(new_name)
```

Output:

```text
Py
Python
```

---

## 6. Worked Examples

### Example 1: build a filename

```python
base = "report"
ext = ".txt"

filename = base + ext
print(filename)
```

### Example 2: repeated pattern

```python
print("-" * 20)
```

### Example 3: substring test

```python
email = "user@example.com"

if "@" in email:
    print("looks valid")
```

---

## 7. Common Pitfalls

### Concatenating strings and numbers directly

```python
# "Age: " + 25   # TypeError
```

Convert the number first.

```python
print("Age: " + str(25))
```

### Assuming `in` tests whole-word meaning

It checks substring presence, not linguistic word boundaries.

---

## 8. Summary

Key ideas:

* `+` joins strings
* `*` repeats strings
* `in` and `not in` test for substring presence
* string operators return new strings

These operations form the foundation of many basic text-processing tasks.