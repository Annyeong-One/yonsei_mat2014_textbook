

# Opening and Reading Files

Programs often need to read data stored in files.

Python provides built-in tools for opening and reading files.

Typical tasks include:

- reading configuration files
- loading datasets
- processing logs
- reading user input stored in files

```mermaid2
flowchart TD
    A[File on disk]
    A --> B[open()]
    B --> C[file object]
    C --> D[read operations]
````

---

## 1. Opening a File

Files are opened using the `open()` function.

```python
f = open("data.txt")
```

This returns a **file object** representing the open file.

The default mode is **read mode**.

---

## 2. Reading the Entire File

```python
f = open("data.txt")

text = f.read()
print(text)

f.close()
```

`read()` loads the entire file contents into a string.

---

## 3. Reading Line by Line

Files can also be processed line by line.

```python
f = open("data.txt")

for line in f:
    print(line)

f.close()
```

This approach is useful for large files.

---

## 4. read(), readline(), readlines()

| Method        | Description   |
| ------------- | ------------- |
| `read()`      | entire file   |
| `readline()`  | one line      |
| `readlines()` | list of lines |

Example:

```python
f = open("data.txt")

print(f.readline())
print(f.readline())

f.close()
```

---

## 5. File Closing

Files should normally be closed after use.

```python
f.close()
```

Closing ensures resources are released and data is written properly.

Later sections introduce **automatic closing using context managers**.

---

## 6. Worked Example

```python
f = open("numbers.txt")

for line in f:
    print(int(line))

f.close()
```

This example reads numbers from a file and prints them.

---

## 7. Common Pitfalls

### Forgetting to close files

Unclosed files may cause resource problems.

### Reading extremely large files with `read()`

This loads the entire file into memory.

### Assuming files always exist

Attempting to open a missing file raises an exception.

---

## 8. Summary

Key ideas:

* files are opened with `open()`
* reading operations use file objects
* files can be read entirely or line by line
* files should normally be closed after use

File reading is the first step in processing external data sources.