

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