
# Input and Output Utilities

Python provides the `open()` built-in function for reading from and writing to files. The `with` statement ensures that files are properly closed after use, even if an exception occurs.

## Writing Files

```python
with open("data.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")
```

## Reading Files

```python
with open("data.txt") as f:
    text = f.read()
print(text)
```

You can also read line by line:

```python
with open("data.txt") as f:
    for line in f:
        print(line.strip())
```

## File Modes

| Mode | Meaning | Creates file? | Overwrites? |
|------|---------|---------------|-------------|
| `"r"` | Read (default) | No | No |
| `"w"` | Write | Yes | Yes |
| `"a"` | Append | Yes | No |
| `"x"` | Exclusive create | Yes | Raises error if exists |
| `"rb"` | Read binary | No | No |
| `"wb"` | Write binary | Yes | Yes |

!!! tip "Always Use `with`"
    The `with` statement guarantees that the file is closed when the block exits, even if an error occurs. Avoid calling `f.close()` manually.

---

## Exercises

**Exercise 1.**
File modes determine what operations are allowed. Predict which operations succeed and which raise errors:

```python
# Assume data.txt exists with content "hello"
with open("data.txt", "r") as f:
    f.write("world")   # Line A

with open("data.txt", "w") as f:
    content = f.read()  # Line B
```

Why does Line A fail? Why does Line B fail? What does the mode string control?

??? success "Solution to Exercise 1"
    Line A raises `io.UnsupportedOperation: not writable`. Line B raises `io.UnsupportedOperation: not readable`.

    The mode string controls which operations are permitted:
    - `"r"` (read): only `read()`, `readline()`, `readlines()` -- no writing
    - `"w"` (write): only `write()`, `writelines()` -- no reading, and it truncates the file to zero length on opening

    The mode acts as a contract: it tells both the OS and the Python runtime what you intend to do with the file. This prevents accidental data corruption (writing to a file you meant to read) and enables optimizations.

---

**Exercise 2.**
The `with` statement guarantees cleanup. Predict the output:

```python
f = open("test.txt", "w")
f.write("data")
# What if an exception occurs here?
f.close()

# vs

with open("test.txt", "w") as f:
    f.write("data")
    # What if an exception occurs here?
# f.close() called automatically
```

What happens to the file if an exception occurs between `f.write` and `f.close()` in the first pattern? Why is `with` safer?

??? success "Solution to Exercise 2"
    In the first pattern, if an exception occurs between `f.write("data")` and `f.close()`, the file is **never closed**. The data may not be flushed to disk, and the file handle leaks until the garbage collector eventually cleans it up (which is not guaranteed to happen promptly).

    With `with`, the file is **always closed** when the block exits, whether normally or via an exception. The `with` statement calls `f.__exit__()`, which calls `f.close()`, regardless of how the block terminates. This is equivalent to a `try/finally` block but cleaner.

    This is why "always use `with`" is a Python best practice for any resource that needs cleanup.

---

**Exercise 3.**
Reading a file line-by-line vs all at once has different memory implications. Predict the output:

```python
# Assume data.txt has 3 lines: "line1\nline2\nline3\n"

with open("data.txt") as f:
    text = f.read()
print(repr(text))

with open("data.txt") as f:
    lines = f.readlines()
print(lines)

with open("data.txt") as f:
    for line in f:
        print(repr(line))
```

Why does each line from `readlines()` and the `for` loop include `\n`? Which approach is most memory-efficient for large files?

??? success "Solution to Exercise 3"
    Output:

    ```text
    'line1\nline2\nline3\n'
    ['line1\n', 'line2\n', 'line3\n']
    'line1\n'
    'line2\n'
    'line3\n'
    ```

    `read()` returns the entire file as a single string, including newlines. `readlines()` returns a list of lines, each retaining its trailing `\n`. The `for` loop iterates line-by-line, also retaining `\n`.

    The `for line in f` approach is **most memory-efficient** for large files because it reads one line at a time (streaming). `read()` loads the entire file into memory. `readlines()` loads all lines into a list. For a 10 GB file, `read()` and `readlines()` would need 10 GB of RAM, while `for line in f` needs only enough for one line at a time.
