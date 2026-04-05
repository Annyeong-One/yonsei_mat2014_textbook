

# Opening and Reading Files

Programs often need to read data stored in files.

Python provides built-in tools for opening and reading files.

Typical tasks include:

- reading configuration files
- loading datasets
- processing logs
- reading user input stored in files

```mermaid
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


## Exercises

**Exercise 1.**
Explain why `f.read()` should be avoided for very large files. What happens in memory when you call `read()` on a 10 GB file with only 8 GB of RAM? What is the preferred alternative for processing large files line by line, and why is it memory-efficient?

??? success "Solution to Exercise 1"
    `f.read()` loads the **entire file contents** into a single string in memory. For a 10 GB file on a machine with 8 GB of RAM, this would exhaust memory, causing either a `MemoryError` or severe swapping (the OS moves data between RAM and disk), making the program extremely slow.

    The preferred alternative:

    ```python
    with open("data.txt") as f:
        for line in f:
            process(line)
    ```

    Iterating over the file object reads **one line at a time**. Each line is loaded into memory, processed, and then the previous line can be garbage-collected. Memory usage stays roughly constant regardless of file size. This works because file objects are **iterators** -- they lazily produce lines on demand rather than loading everything at once.

---

**Exercise 2.**
After reading a file with `f.read()`, calling `f.read()` again returns an empty string `""`. Explain why. What is the "file position cursor," and how does it explain this behavior? How would you read the file contents a second time without reopening the file?

??? success "Solution to Exercise 2"
    Every open file object has a **position cursor** (or "file pointer") that tracks where the next read will start. When you first open a file, the cursor is at position 0 (the beginning).

    `f.read()` reads from the cursor to the end of the file, advancing the cursor to the end. A second `f.read()` tries to read from the end of the file -- there is nothing left, so it returns `""`.

    To read again without reopening: use `f.seek(0)` to move the cursor back to the beginning:

    ```python
    data1 = f.read()   # Reads everything, cursor at end
    f.seek(0)           # Move cursor back to start
    data2 = f.read()   # Reads everything again
    ```

    The cursor model explains why `for line in f` processes each line once -- each iteration advances the cursor past the line just read.

---

**Exercise 3.**
A programmer writes:

```python
f = open("data.txt")
data = f.read()
# ... process data ...
# forgot to call f.close()
```

Explain the potential problems of not closing a file. Then explain why the `with` statement is the correct solution and how it guarantees the file is closed even if an exception occurs.

??? success "Solution to Exercise 3"
    Not closing a file can cause:

    1. **Resource leaks**: The OS has a limited number of file handles. Opening many files without closing them can exhaust this limit, causing `OSError: Too many open files`.
    2. **Data loss**: For files opened for writing, data may be buffered in memory and not flushed to disk until the file is closed. If the program crashes, buffered data is lost.
    3. **Locking**: On some systems (especially Windows), an open file may be locked, preventing other programs from accessing it.

    The `with` statement guarantees cleanup:

    ```python
    with open("data.txt") as f:
        data = f.read()
    # f.close() is called automatically here, even if an exception occurred
    ```

    `with` calls `f.__exit__()` (which calls `f.close()`) when the block exits, whether normally or due to an exception. This is called a **context manager** pattern and is the only reliable way to ensure resources are properly released.
