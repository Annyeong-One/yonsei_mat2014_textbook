
# Path Handling (pathlib)

Python provides the **pathlib** module for working with file system paths.

It offers a modern and object-oriented interface for path manipulation.

```mermaid
flowchart TD
    A[pathlib.Path]
    A --> B[file path operations]
    A --> C[filesystem queries]
````

---

## 1. Creating Paths

```python
from pathlib import Path

p = Path("data.txt")
```

---

## 2. Checking File Existence

```python
p.exists()
p.is_file()
p.is_dir()
```

---

## 3. Joining Paths

```python
p = Path("data") / "file.txt"
```

This avoids manual string concatenation.

---

## 4. Reading and Writing

```python
p = Path("hello.txt")

p.write_text("Hello")
print(p.read_text())
```

---

## 5. Iterating Through Directories

```python
p = Path("data")

for item in p.iterdir():
    print(item)
```

---

## 6. Advantages of pathlib

* clearer code
* platform independence
* easier path manipulation

---


## 7. Summary

Key ideas:

* `pathlib.Path` represents filesystem paths
* paths can be joined using `/`
* methods support reading, writing, and inspection
* pathlib simplifies file system interactions


## Exercises

**Exercise 1.**
`pathlib.Path` uses the `/` operator for path joining. Explain why this works:

```python
from pathlib import Path

p = Path("data") / "subfolder" / "file.txt"
print(p)
print(type(p))
```

What Python mechanism allows `/` to join paths? Why is this preferred over string concatenation (`"data" + "/" + "subfolder" + "/" + "file.txt"`)?

??? success "Solution to Exercise 1"
    Output (on a Unix-like system):

    ```text
    data/subfolder/file.txt
    <class 'PosixPath'>
    ```

    The `/` operator works because `Path` defines the `__truediv__` method, which Python calls when `/` is used. This is **operator overloading** -- the same mechanism that lets `+` mean addition for numbers and concatenation for strings.

    `Path("/")` is preferred over string concatenation because:
    1. **Platform independence**: `Path` uses the correct separator (`/` on Unix, `\` on Windows) automatically.
    2. **Type safety**: the result is a `Path` object with path-specific methods, not a raw string.
    3. **Readability**: `Path("data") / "file.txt"` is cleaner than `os.path.join("data", "file.txt")`.
    4. **Validation**: `Path` understands path semantics (e.g., resolving `.` and `..`).

---

**Exercise 2.**
`Path` objects provide methods that combine multiple `os` module calls. Compare:

```python
import os
from pathlib import Path

# os module approach
if os.path.exists("data.txt") and os.path.isfile("data.txt"):
    size = os.path.getsize("data.txt")

# pathlib approach
p = Path("data.txt")
if p.exists() and p.is_file():
    size = p.stat().st_size
```

What advantage does the object-oriented `pathlib` approach have? Why does `Path` have methods like `.read_text()` and `.write_text()` when `open()` already exists?

??? success "Solution to Exercise 2"
    The object-oriented approach groups all path-related operations on a single object. Instead of calling free functions from `os.path` and passing the path string each time, you call methods on the `Path` object.

    Advantages:
    1. **Discoverability**: all path operations are methods on the `Path` object, so IDE autocompletion shows available operations.
    2. **Chaining**: `Path("dir").mkdir(parents=True, exist_ok=True)` reads naturally.
    3. **Consistency**: one object carries the path state, reducing the chance of passing the wrong string to a function.

    `.read_text()` and `.write_text()` exist for convenience:

    ```python
    # Instead of three lines:
    with open("data.txt") as f:
        content = f.read()

    # One line:
    content = Path("data.txt").read_text()
    ```

    They are shorthand for the common pattern of "open, read/write, close" when you want the entire file content. For line-by-line processing or binary data, `open()` with `with` is still needed.

---

**Exercise 3.**
A programmer writes platform-specific path code:

```python
path = "C:\\Users\\alice\\data\\file.txt"  # Windows only
```

Explain why this fails on macOS/Linux. Show how `pathlib.Path` solves the cross-platform problem. What does `Path.home()` return, and why is it useful for writing portable code?

??? success "Solution to Exercise 3"
    `"C:\\Users\\alice\\data\\file.txt"` is a Windows-specific path. On macOS/Linux, this is treated as a single directory name containing backslashes, not as a directory hierarchy. The file would not be found.

    `pathlib.Path` solves this:

    ```python
    from pathlib import Path
    p = Path.home() / "data" / "file.txt"
    ```

    `Path.home()` returns the current user's home directory as a `Path` object:
    - Windows: `C:\Users\alice`
    - macOS: `/Users/alice`
    - Linux: `/home/alice`

    The `/` operator joins paths using the platform-appropriate separator. This code works identically on all platforms, eliminating hardcoded paths and OS-specific separators.
