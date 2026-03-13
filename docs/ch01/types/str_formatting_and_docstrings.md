
# str Formatting and Docstrings

Strings are often used not just as data, but also as a way to present information and document programs.

This section covers:

- f-strings
- `format()`
- simple formatting ideas
- docstrings

```mermaid2
flowchart TD
    A[String formatting]
    A --> B[f-strings]
    A --> C[format()]
    A --> D[docstrings]
````

---

## 1. f-Strings

An f-string allows expressions to be embedded directly inside a string literal.

```python
name = "Alice"
age = 25

print(f"{name} is {age} years old.")
```

Output:

```text
Alice is 25 years old.
```

This is often the clearest modern formatting method.

---

## 2. Formatting Expressions

Expressions can appear inside braces.

```python
x = 5
y = 7

print(f"{x} + {y} = {x + y}")
```

Output:

```text
5 + 7 = 12
```

---

## 3. format()

Python also supports the `format()` method.

```python
name = "Bob"
score = 92

print("{} scored {}".format(name, score))
```

Output:

```text
Bob scored 92
```

Named fields are also possible.

```python
print("{name} scored {score}".format(name="Bob", score=92))
```

---

## 4. Simple Numeric Formatting

Formatting can control appearance.

```python
pi = 3.14159
print(f"{pi:.2f}")
```

Output:

```text
3.14
```

---

## 5. Docstrings

A docstring is a triple-quoted string placed immediately inside a module, function, class, or method definition.

```python
def area(length, width):
    """Return the area of a rectangle."""
    return length * width
```

Docstrings are used for documentation and are accessible at runtime.

```python
print(area.__doc__)
```

Output:

```text
Return the area of a rectangle.
```

---

## 6. Multiline Docstrings

Docstrings can span multiple lines.

```python
def greet(name):
    """
    Return a greeting message.

    Args:
        name: person's name
    """
    return f"Hello, {name}"
```

---

## 7. Worked Examples

### Example 1: f-string

```python
language = "Python"
version = 3.12

print(f"{language} {version}")
```

### Example 2: format method

```python
print("x = {}, y = {}".format(3, 4))
```

### Example 3: function docstring

```python
def square(x):
    """Return x squared."""
    return x * x

print(square.__doc__)
```

---

## 8. Common Pitfalls

### Forgetting the `f` in f-strings

```python
# "{name}"   # literal text, not formatted
```

### Confusing ordinary multiline strings with docstrings

A string becomes a docstring only when placed as the first statement in a module, function, class, or method body.

---

## 9. Summary

Key ideas:

* f-strings are a powerful formatting tool
* `format()` provides an older but still useful formatting style
* docstrings document code objects
* triple-quoted strings are often used for docstrings

Formatting and documentation make string usage much more practical and expressive.