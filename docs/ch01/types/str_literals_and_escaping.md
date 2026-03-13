
# str Literals and Escaping

Python provides several ways to write string literals.

This section covers:

- single-quoted strings
- double-quoted strings
- escape characters
- multiline strings
- raw strings

```mermaid2
flowchart TD
    A[String literals]
    A --> B[single quotes]
    A --> C[double quotes]
    A --> D[triple quotes]
    A --> E[raw strings]
    A --> F[escape sequences]
````

---

## 1. Single and Double Quotes

Strings can be written with either single quotes or double quotes.

```python
'a'
"hello"
```

These are equivalent in meaning.

```python
print('Python')
print("Python")
```

Use whichever form improves readability.

For example, double quotes are convenient when the string contains an apostrophe:

```python
print("Don't panic")
```

---

## 2. Escape Characters

Some characters cannot be written directly inside a string literal without special syntax.

Python uses **escape sequences** beginning with `\`.

| Escape | Meaning      |
| ------ | ------------ |
| `\'`   | single quote |
| `\"`   | double quote |
| `\\`   | backslash    |
| `\n`   | newline      |
| `\t`   | tab          |

Example:

```python
print("Line 1\nLine 2")
print("A\tB\tC")
print("He said: \"hello\"")
```

Output:

```text
Line 1
Line 2
A	B	C
He said: "hello"
```

---

## 3. Multiline Strings

Triple quotes allow strings to span multiple lines.

```python
text = """This is
a multiline
string."""
print(text)
```

Triple single quotes also work:

```python
text = '''another
multiline
string'''
```

Multiline strings are useful for:

* long text
* embedded examples
* templates
* docstrings

---

## 4. Raw Strings

A raw string treats backslashes literally.

```python
path = r"C:\new_folder\test.txt"
print(path)
```

Output:

```text
C:\new_folder\test.txt
```

Without the `r` prefix, sequences like `\n` would be interpreted as escapes.

Raw strings are especially useful for:

* file paths
* regular expressions
* Windows path examples

---

## 5. Choosing a Literal Style

Common guideline:

* use single or double quotes for ordinary strings
* use triple quotes for multiline text
* use raw strings when backslashes should remain literal

---

## 6. Worked Examples

### Example 1: newline

```python
print("Hello\nWorld")
```

### Example 2: quote inside string

```python
quote = "She said, \"Python is fun\"."
print(quote)
```

### Example 3: raw path

```python
path = r"C:\Users\name\Documents"
print(path)
```

---

## 7. Common Pitfalls

### Forgetting escapes

```python
# "C:\new"   # contains \n
```

This may produce an unintended newline.

### Confusing raw strings with ordinary strings

Raw strings still have syntax rules and are not magical text containers.

---

## 8. Summary

Key ideas:

* Python supports multiple string literal forms
* escape sequences represent special characters
* triple quotes allow multiline strings
* raw strings preserve backslashes literally

Understanding string literals is the first step toward working with text correctly.