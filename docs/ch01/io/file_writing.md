

# Writing Files

Programs often need to write data to files.

Examples include:

- saving program output
- generating reports
- storing logs
- exporting processed data

```mermaid
flowchart TD
    A[Program data]
    A --> B[open file in write mode]
    B --> C[write()]
    C --> D[data stored on disk]
````

---

## 1. Opening Files for Writing

To write to a file, specify mode `"w"`.

```python
f = open("output.txt", "w")
```

This creates the file if it does not exist.

If the file exists, it is **overwritten**.

---

## 2. Writing Text

```python
f = open("output.txt", "w")

f.write("Hello\n")
f.write("Python\n")

f.close()
```

---

## 3. Appending to Files

Mode `"a"` appends to the end of a file.

```python
f = open("log.txt", "a")

f.write("New entry\n")

f.close()
```

---

## 4. Writing Multiple Lines

```python
lines = ["a\n", "b\n", "c\n"]

f = open("letters.txt", "w")
f.writelines(lines)
f.close()
```

---

## 5. File Modes

| Mode   | Meaning        |
| ------ | -------------- |
| `"r"`  | read           |
| `"w"`  | write          |
| `"a"`  | append         |
| `"r+"` | read and write |

Example:

```python
f = open("data.txt", "r")
```

---

## 6. Worked Example

```python
numbers = [1, 2, 3]

f = open("numbers.txt", "w")

for n in numbers:
    f.write(str(n) + "\n")

f.close()
```

---

## 7. Common Pitfalls

### Overwriting files accidentally

Using `"w"` replaces existing content.

### Writing non-string objects

`write()` expects strings.

Convert values first.

```python
f.write(str(x))
```

---


## 8. Summary

Key ideas:

* files can be opened in write or append mode
* `write()` stores text data
* `writelines()` writes multiple lines
* writing often requires converting values to strings

File writing allows programs to persist data beyond program execution.


## Exercises

**Exercise 1.**
`write()` does not add newlines automatically. Predict the content of the file:

```python
with open("test.txt", "w") as f:
    f.write("hello")
    f.write("world")
```

What does `test.txt` contain? How does this differ from `print("hello", file=f)`? Why does `write()` not add newlines while `print()` does?

??? success "Solution to Exercise 1"
    `test.txt` contains: `helloworld` (no newline between them, no trailing newline).

    Using `print("hello", file=f)` would write `hello\n` -- `print()` adds a newline by default (controlled by the `end` parameter, which defaults to `"\n"`).

    `write()` does not add newlines because it is a **low-level** method that writes exactly the bytes you give it. This gives you full control over the output format. `print()` is a **high-level** function designed for human-readable output, so it adds separators and newlines by default. The design principle: low-level tools should be precise; high-level tools should be convenient.

---

**Exercise 2.**
Mode `"w"` overwrites existing content, while mode `"a"` appends. Predict the final content of the file after running this code:

```python
with open("log.txt", "w") as f:
    f.write("first\n")

with open("log.txt", "w") as f:
    f.write("second\n")

with open("log.txt", "a") as f:
    f.write("third\n")
```

Why is accidental use of `"w"` a common source of data loss? What simple precaution can prevent it?

??? success "Solution to Exercise 2"
    Final content of `log.txt`:

    ```text
    second
    third
    ```

    The first `"w"` open creates the file with `"first\n"`. The second `"w"` open **overwrites** the entire file with `"second\n"` -- `"first\n"` is gone. The `"a"` open appends `"third\n"` to the existing content.

    Accidental use of `"w"` is a common source of data loss because it silently destroys the previous content without warning. Precautions:
    1. Check if the file exists before writing: `if Path(filename).exists(): raise FileExistsError(...)`.
    2. Use `"x"` mode (exclusive creation): `open("log.txt", "x")` raises `FileExistsError` if the file already exists.
    3. Always use `"a"` for log files.

---

**Exercise 3.**
`write()` only accepts strings. A programmer wants to write a list of numbers:

```python
numbers = [1, 2, 3, 4, 5]

with open("nums.txt", "w") as f:
    f.write(numbers)
```

This raises `TypeError`. Show two correct approaches: one using `write()` with explicit conversion, and one using `print()` with the `file` parameter. Which approach is more convenient for complex output?

??? success "Solution to Exercise 3"
    Using `write()` with explicit conversion:

    ```python
    numbers = [1, 2, 3, 4, 5]
    with open("nums.txt", "w") as f:
        for n in numbers:
            f.write(str(n) + "\n")
    ```

    Using `print()` with `file` parameter:

    ```python
    numbers = [1, 2, 3, 4, 5]
    with open("nums.txt", "w") as f:
        for n in numbers:
            print(n, file=f)
    ```

    `print()` is more convenient because it automatically converts values to strings (via `str()`) and adds newlines. For complex output with multiple values, `print(a, b, c, file=f)` handles spacing and conversion automatically, while `write()` would require `f.write(f"{a} {b} {c}\n")`.
