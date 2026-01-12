# `str`: Methods

Python strings provide methods for transformation, substitution, and formatting.

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
print(s.title())     # Hello World
print(s.swapcase())  # HELLO WORLD
```

### 3. Capitalize

```python
s = "hello world"
print(s.capitalize())  # Hello world
```

---

## Replace Method

### 1. Basic Replace

```python
a = "Hello Pi"
a = a.replace("Pi", "World")
print(a)  # Hello World
```

### 2. All Occurrences

```python
s = "hello hello hello"
s = s.replace("hello", "hi")
print(s)  # hi hi hi
```

### 3. Limited Replace

```python
s = "hello hello hello"
s = s.replace("hello", "hi", 1)
print(s)  # hi hello hello
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

## Formatting

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

## Key Takeaways

- Case: `upper()`, `lower()`, `title()`.
- `replace()` substitutes substrings.
- `strip()` removes leading/trailing chars.
- `join()` builds strings from iterables.
- F-strings provide modern formatting.
