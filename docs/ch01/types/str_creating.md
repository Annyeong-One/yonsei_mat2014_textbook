# `str`: Creating Strings

Python provides multiple ways to create string literals, offering flexibility for different use cases.

---

## Quote Styles

### 1. Single Quotes

Single quotes create strings in Python:

```python
a = 'Hello World'
print(a, type(a))  # Hello World <class 'str'>
```

### 2. Double Quotes

Double quotes work identically:

```python
a = "Hello World"
print(a, type(a))  # Hello World <class 'str'>
```

### 3. No Difference

Unlike C, where single quotes create characters and double quotes create strings, Python treats both identically:

```python
def main():
    a = 'Hello World'
    print(f'{a = }')

    a = "Hello World"
    print(f'{a = }')

if __name__ == "__main__":
    main()
```

---

## Embedded Quotes

### 1. Alternate Quotes

Use the opposite quote style to embed quotations:

```python
# Double quotes inside single quotes
a = 'He called the Gettysburg Address a "monumental act."'
print(a)

# Single quotes inside double quotes
a = "He called the Gettysburg Address a 'monumental act.'"
print(a)
```

### 2. Escape Characters

Use backslash to escape same-style quotes:

```python
# Escaping double quotes
a = "He called the Gettysburg Address a \"monumental act.\""
print(a)

# Escaping single quotes
a = 'He called the Gettysburg Address a \'monumental act.\''
print(a)
```

---

## Key Takeaways

- Single and double quotes are interchangeable in Python.
- Embed quotes using alternate styles or escape characters.
- Choose quote style based on content for readability.
