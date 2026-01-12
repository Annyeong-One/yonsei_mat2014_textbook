# `str`: Modification

Since strings are immutable, modification requires creating new string objects.

---

## Concatenation

### 1. Plus Operator

Join strings with `+`:

```python
string = "Hello"
new_string = string + " World"

print("Original:", string)      # Hello
print("Modified:", new_string)  # Hello World
```

### 2. With Slicing

Combine slicing and concatenation:

```python
a = "Hello Pi"
a = a[:1] + "E" + a[2:]
print(a)  # HEllo Pi
```

---

## Replace Method

### 1. Basic Replace

Substitute substrings:

```python
a = "Hello Pi"
a = a.replace("Pi", "World")
print(a)  # Hello World
```

### 2. Multiple Occurrences

Replace all matches:

```python
s = "hello hello hello"
s = s.replace("hello", "hi")
print(s)  # hi hi hi
```

### 3. Limited Replace

Specify maximum replacements:

```python
s = "hello hello hello"
s = s.replace("hello", "hi", 1)
print(s)  # hi hello hello
```

---

## Case Methods

### 1. Upper and Lower

```python
s = "Hello World"
print(s.upper())  # HELLO WORLD
print(s.lower())  # hello world
```

### 2. Title and Swap

```python
s = "hello world"
print(s.title())    # Hello World
print(s.swapcase()) # HELLO WORLD
```

### 3. Capitalize

```python
s = "hello world"
print(s.capitalize())  # Hello world
```

---

## String Formatting

### 1. format() Method

```python
a = "Hello {}"
a = a.format("World")
print(a)  # Hello World
```

### 2. F-Strings

```python
name = "World"
a = f"Hello {name}"
print(a)  # Hello World
```

### 3. Multiple Values

```python
first = "John"
last = "Doe"
full = f"{first} {last}"
print(full)  # John Doe
```

---

## Join Method

### 1. From List

```python
words = ["Hello", "World"]
result = " ".join(words)
print(result)  # Hello World
```

### 2. Custom Separator

```python
parts = ["2024", "01", "15"]
date = "-".join(parts)
print(date)  # 2024-01-15
```

---

## Strip Methods

### 1. Whitespace

```python
s = "  hello  "
print(s.strip())   # hello
print(s.lstrip())  # hello  (right space remains)
print(s.rstrip())  #   hello (left space remains)
```

### 2. Characters

```python
s = "...hello..."
print(s.strip("."))  # hello
```

---

## Key Takeaways

- Use `+` or slicing for concatenation.
- `replace()` substitutes substrings.
- Case methods: `upper()`, `lower()`, `title()`.
- F-strings provide modern formatting.
- `join()` builds strings from iterables.
