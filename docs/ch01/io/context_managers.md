
# Context Managers (with)

Python provides a safer and more convenient way to manage files using **context managers**.

The `with` statement automatically handles opening and closing files.

```mermaid2
flowchart TD
    A[with open()]
    A --> B[file operations]
    B --> C[file automatically closed]
````

---

## 1. Basic Syntax

```python
with open("data.txt") as f:
    text = f.read()
    print(text)
```

After the block finishes, the file is automatically closed.

---

## 2. Why Context Managers Are Useful

They ensure resources are released even if errors occur.

```mermaid2
flowchart TD
    A[open file]
    A --> B[process file]
    B --> C{error?}
    C -->|yes| D[file still closed]
    C -->|no| D
```

This makes programs more robust.

---

## 3. Writing Files with with

```python
with open("output.txt", "w") as f:
    f.write("Hello\n")
```

No explicit `close()` call is required.

---

## 4. Nested File Operations

Multiple files can be opened.

```python
with open("input.txt") as f1, open("output.txt", "w") as f2:
    for line in f1:
        f2.write(line)
```

---

## 5. Conceptual Model

A context manager defines two phases:

* entering the context
* exiting the context

The `with` statement guarantees that cleanup occurs.

---

## 6. Worked Example

```python
with open("numbers.txt") as f:
    total = 0
    for line in f:
        total += int(line)

print(total)
```

---

## 7. Summary

Key ideas:

* context managers simplify resource handling
* `with` automatically closes files
* they prevent resource leaks
* they are the recommended approach for file I/O

Using `with` is considered best practice when working with files.