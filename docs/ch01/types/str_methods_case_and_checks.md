

# str Methods: Case and Checks

Python strings provide many useful methods for:

- changing case
- testing properties

These methods help analyze and normalize text.

```mermaid
flowchart TD
    A[String methods]
    A --> B[case methods]
    A --> C[check methods]
````

---

## 1. Case Methods

Common case-related methods include:

| Method         | Purpose                    |
| -------------- | -------------------------- |
| `lower()`      | convert to lowercase       |
| `upper()`      | convert to uppercase       |
| `title()`      | title-case words           |
| `capitalize()` | capitalize first character |
| `swapcase()`   | swap upper and lower case  |

Example:

```python
text = "pYtHoN"

print(text.lower())
print(text.upper())
print(text.title())
print(text.swapcase())
```

---

## 2. Case Methods Return New Strings

Because strings are immutable, these methods do not modify the original string.

```python
text = "Python"
lowered = text.lower()

print(text)
print(lowered)
```

---

## 3. Check Methods

Check methods return Boolean values.

Common examples:

| Method      | Meaning                        |
| ----------- | ------------------------------ |
| `isalpha()` | all alphabetic characters      |
| `isdigit()` | all digits                     |
| `isalnum()` | alphanumeric only              |
| `islower()` | all cased characters lowercase |
| `isupper()` | all cased characters uppercase |
| `isspace()` | all whitespace                 |

Example:

```python
print("Python".isalpha())
print("123".isdigit())
print("abc123".isalnum())
```

Output:

```text
True
True
True
```

---

## 4. Validation Use Cases

These methods are often used for simple input validation.

```python
code = "12345"

if code.isdigit():
    print("numeric code")
```

Another example:

```python
name = "Alice"

if name.isalpha():
    print("letters only")
```

---

## 5. Worked Examples

### Example 1: normalize for comparison

```python
a = "HELLO"
b = "hello"

print(a.lower() == b.lower())
```

### Example 2: check digits

```python
text = "2025"
print(text.isdigit())
```

### Example 3: title case

```python
title = "python programming"
print(title.title())
```

Output:

```text
Python Programming
```

---

## 6. Common Pitfalls

### Assuming methods modify in place

They return new strings.

### Overtrusting simple checks

Methods such as `isdigit()` are useful, but real-world validation often needs additional rules.

---

## 7. Summary

Key ideas:

* case methods transform strings
* check methods test textual properties
* all string methods return new strings
* these methods are useful for normalization and validation

Case and check methods are among the most frequently used string tools in Python.