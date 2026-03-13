
# Path Handling (pathlib)

Python provides the **pathlib** module for working with file system paths.

It offers a modern and object-oriented interface for path manipulation.

```mermaid2
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