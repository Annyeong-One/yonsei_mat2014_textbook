

# Code Structure and Readability

Readable code is easier to maintain and less likely to contain errors.
Python enforces readability through **indentation rules and simple syntax**.

This chapter explains:

* indentation and blocks
* comments
* the `pass` statement

---

## 1. Indentation and Blocks

Unlike many languages, Python uses **indentation to define code blocks**.

Example:

```python
if temperature > 30:
    print("Hot")
    print("Stay hydrated")
```

The colon `:` introduces a block, and all lines in the block must have the same indentation.

### Standard indentation

PEP 8 recommends **4 spaces per indentation level**.

### Block structure

```mermaid2
flowchart TD
    A[if statement]
    A --> B[indented block]
    B --> C[statement 1]
    B --> D[statement 2]
```

Mixing tabs and spaces can cause errors such as:

```
IndentationError
```

or

```
TabError
```

---

## 2. Nested Blocks

Blocks can be nested.

Example:

```python
for i in range(3):
    for j in range(3):
        if i == j:
            print(i, j)
```

Each nested level increases indentation.

---

## 3. Guard Clauses

Guard clauses help avoid deep nesting.

Example:

```python
def process(data):
    if data is None:
        return None

    if not validate(data):
        return None

    return transform(data)
```

This improves readability.

---

## 4. Comments

Comments are annotations ignored by the interpreter.

Example:

```python
# This is a comment
x = 5
```

The most important rule:

**comment why, not what**.

Example:

```python
x = 5  # server requires minimum timeout
```

Bad example:

```python
x = x + 1  # increment x by 1
```

Comments that repeat obvious code are not useful. 

---

## 5. Docstrings

Docstrings document functions, classes, and modules.

Example:

```python
def calculate_area(length, width):
    """Calculate rectangle area."""
    return length * width
```

Docstrings are accessible at runtime:

```python
print(calculate_area.__doc__)
```

---

## 6. Comment Markers

Common markers include:

```
TODO
FIXME
HACK
NOTE
```

Example:

```python
# TODO: optimize algorithm
# FIXME: handle empty list
```

---

## 7. The `pass` Statement

Python requires every block to contain at least one statement.

The `pass` statement acts as a **placeholder**.

Example:

```python
def future_feature():
    pass
```

Example class:

```python
class DatabaseConnection:
    pass
```

`pass` performs **no operation** but satisfies the syntax requirement. 

---

## 8. pass vs Ellipsis

Python also provides the **ellipsis literal**:

```python
...
```

Example:

```python
def parse():
    ...
```

Both serve as placeholders.

---

## 9. pass Does Not Exit a Function

Example:

```python
def demo():
    pass
    print("Still runs")

demo()
```

Output:

```
Still runs
```

Unlike `return`, `pass` does not stop execution.

---

## 10. Summary

Key ideas:

* indentation defines program structure
* blocks follow a colon `:`
* comments explain **intent**
* docstrings document functions and modules
* `pass` creates intentionally empty blocks

These conventions help Python code remain **clear and readable**.


