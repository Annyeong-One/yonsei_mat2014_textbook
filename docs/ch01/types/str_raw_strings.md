# `str`: Raw Strings

Raw strings ignore escape character interpretation, treating backslashes as literal characters.

---

## Syntax

### 1. Basic Raw String

Prefix a string with `r` to create a raw string:

```python
def main():
    # Raw string ignores escape sequences
    print(r"Hello, Bob.\tThis is Sungchul.\nHow are you")
    # Output: Hello, Bob.\tThis is Sungchul.\nHow are you

if __name__ == "__main__":
    main()
```

### 2. Comparison

Without the `r` prefix, escapes are interpreted:

```python
def main():
    # Normal string processes escape sequences
    print("Hello, Bob.\tThis is Sungchul.\nHow are you")
    # Output:
    # Hello, Bob.    This is Sungchul.
    # How are you

if __name__ == "__main__":
    main()
```

---

## Use Cases

### 1. File Paths

Windows paths use backslashes:

```python
# Without raw string (requires escaping)
path = "C:\\Users\\Documents\\file.txt"

# With raw string (cleaner)
path = r"C:\Users\Documents\file.txt"
```

### 2. Regular Expressions

Regex patterns often contain backslashes:

```python
import re

# Without raw string
pattern = "\\d+\\.\\d+"

# With raw string (more readable)
pattern = r"\d+\.\d+"

text = "Price: 19.99"
match = re.search(pattern, text)
print(match.group())  # 19.99
```

---

## Limitations

### 1. Trailing Backslash

Raw strings cannot end with an odd number of backslashes:

```python
# This causes a syntax error
# path = r"C:\Users\"

# Solutions
path = r"C:\Users" + "\\"
path = "C:\\Users\\"
```

---

## Key Takeaways

- Prefix `r` creates raw strings.
- Raw strings treat backslashes literally.
- Ideal for file paths and regex patterns.
- Cannot end with odd backslashes.
