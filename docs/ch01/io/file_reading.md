# Opening and Reading Files

File input/output (I/O) allows Python programs to read data from and write data to files on disk. Reading files is fundamental for data processing and analysis.

---

## Opening Files

Use the built-in `open()` function:

```python
f = open("data.txt", "r")
# ... work with file ...
f.close()
```

### File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read (default) — file must exist |
| `"w"` | Write — creates or truncates file |
| `"a"` | Append — creates or appends to file |
| `"x"` | Exclusive create — fails if file exists |
| `"b"` | Binary mode (combine: `"rb"`, `"wb"`) |
| `"t"` | Text mode (default, combine: `"rt"`) |
| `"+"` | Read and write (combine: `"r+"`, `"w+"`) |

```python
# Common combinations
f = open("data.txt", "r")      # Read text (default)
f = open("data.txt", "rt")     # Same as above
f = open("image.png", "rb")    # Read binary
f = open("log.txt", "a")       # Append text
f = open("data.txt", "r+")     # Read and write
```

### Encoding

Always specify encoding for text files:

```python
# Explicit encoding (recommended)
f = open("data.txt", "r", encoding="utf-8")

# Other encodings
f = open("legacy.txt", "r", encoding="latin-1")
f = open("korean.txt", "r", encoding="euc-kr")

# System default (not portable)
f = open("data.txt", "r")  # Uses locale.getpreferredencoding()
```

**Best practice**: Always use `encoding="utf-8"` for portability.

---

## Reading Methods

### read() — Entire File

Read the entire file into a single string:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

Read specific number of characters:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    first_100 = f.read(100)  # First 100 characters
    next_50 = f.read(50)     # Next 50 characters
```

### readline() — One Line

Read a single line (including newline character):

```python
with open("data.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()     # First line
    line2 = f.readline()     # Second line
    line3 = f.readline()     # Third line (empty string if EOF)
```

Loop until end of file:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    while line := f.readline():
        print(line.strip())
```

### readlines() — All Lines as List

Read all lines into a list:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    
print(lines)  # ['line1\n', 'line2\n', 'line3\n']
print(len(lines))  # Number of lines
```

**Note**: Each line includes the newline character `\n`.

### Iteration — Line by Line (Recommended)

Iterate directly over the file object:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

**Why preferred:**
- Memory efficient (doesn't load entire file)
- Clean, Pythonic syntax
- Works with very large files

---

## Comparison of Reading Methods

| Method | Returns | Memory | Use Case |
|--------|---------|--------|----------|
| `read()` | Single string | High | Small files |
| `read(n)` | n characters | Low | Chunked processing |
| `readline()` | One line | Low | Line-by-line with control |
| `readlines()` | List of lines | High | Need random access to lines |
| `for line in f` | One line at a time | Low | Large files (recommended) |

---

## Handling Newlines

### Strip Newlines

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()      # Remove leading/trailing whitespace
        # or
        line = line.rstrip('\n')  # Remove only trailing newline
        print(line)
```

### splitlines()

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    lines = content.splitlines()  # No newline characters
    
print(lines)  # ['line1', 'line2', 'line3']
```

---

## File Position

### tell() — Current Position

```python
with open("data.txt", "r", encoding="utf-8") as f:
    print(f.tell())      # 0 (start)
    f.read(10)
    print(f.tell())      # 10 (after reading 10 chars)
```

### seek() — Move Position

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    f.seek(0)            # Back to start
    content_again = f.read()
```

**Note**: In text mode, `seek()` only reliably works with positions from `tell()` or `seek(0)`.

---

## Error Handling

### File Not Found

```python
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist")
```

### Permission Denied

```python
try:
    with open("/etc/passwd", "r") as f:
        content = f.read()
except PermissionError:
    print("No permission to read file")
```

### Encoding Errors

```python
# Strict (default) — raises error
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    print("File contains invalid UTF-8")

# Replace invalid characters
with open("data.txt", "r", encoding="utf-8", errors="replace") as f:
    content = f.read()  # Invalid bytes become �

# Ignore invalid characters
with open("data.txt", "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()  # Invalid bytes are skipped
```

---

## Common Patterns

### Check File Exists Before Reading

```python
from pathlib import Path

filepath = Path("data.txt")
if filepath.exists():
    content = filepath.read_text(encoding="utf-8")
else:
    print("File not found")
```

### Read with Default Value

```python
from pathlib import Path

def read_file(path, default=""):
    """Read file or return default if not found."""
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return default

content = read_file("config.txt", default="{}")
```

### Count Lines Efficiently

```python
def count_lines(filepath):
    """Count lines without loading entire file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

num_lines = count_lines("large_file.txt")
```

---

## Key Takeaways

- Use `open()` with explicit `encoding="utf-8"`
- Prefer `for line in f` for large files (memory efficient)
- `read()` loads entire file — use for small files only
- `readline()` for line-by-line control
- `readlines()` when you need a list of all lines
- Always handle `FileNotFoundError` and encoding errors
- Use `with` statement for automatic file closing (see Context Managers)
