# Writing Files

Writing files allows programs to persist results, logs, configurations, and data for later use.

---

## Opening Files for Writing

### Write Mode (`"w"`)

Creates new file or **truncates** (empties) existing file:

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!")
```

⚠️ **Warning**: `"w"` mode destroys existing content!

### Append Mode (`"a"`)

Creates new file or appends to existing file:

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry\n")
```

### Exclusive Create (`"x"`)

Creates new file, fails if file already exists:

```python
try:
    with open("new_file.txt", "x", encoding="utf-8") as f:
        f.write("Fresh content")
except FileExistsError:
    print("File already exists!")
```

### Read and Write (`"r+"`, `"w+"`)

```python
# Read and write (file must exist)
with open("data.txt", "r+", encoding="utf-8") as f:
    content = f.read()
    f.write("Appended text")

# Write and read (truncates first)
with open("data.txt", "w+", encoding="utf-8") as f:
    f.write("New content")
    f.seek(0)
    content = f.read()
```

---

## Writing Methods

### write() — Write String

Write a string to file, returns number of characters written:

```python
with open("output.txt", "w", encoding="utf-8") as f:
    chars_written = f.write("Hello\n")
    print(chars_written)  # 6
    
    f.write("World\n")
```

**Note**: `write()` does **not** add newlines automatically.

### writelines() — Write Multiple Strings

Write an iterable of strings:

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
```

**Note**: `writelines()` does **not** add newlines between items.

```python
# This produces "abc" (no newlines)
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(["a", "b", "c"])

# Add newlines yourself
items = ["a", "b", "c"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(item + "\n" for item in items)
```

---

## print() to File

Use `print()` with `file=` parameter:

```python
with open("output.txt", "w", encoding="utf-8") as f:
    print("Line 1", file=f)
    print("Line 2", file=f)
    print("Value:", 42, file=f)
```

**Advantages over write():**
- Automatically adds newline
- Handles multiple arguments
- Automatic string conversion

```python
with open("output.txt", "w", encoding="utf-8") as f:
    # Multiple values with separator
    print("a", "b", "c", sep=", ", file=f)  # a, b, c
    
    # Custom line ending
    print("no newline", end="", file=f)
    
    # Mix types
    print("Count:", 100, "items", file=f)
```

---

## Newline Handling

### Platform Differences

| Platform | Line Ending |
|----------|-------------|
| Unix/Linux/macOS | `\n` (LF) |
| Windows | `\r\n` (CRLF) |
| Old Mac (pre-OS X) | `\r` (CR) |

### The `newline` Parameter

```python
# Default: translate \n to platform-specific ending
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("line\n")  # Windows: writes \r\n, Unix: writes \n

# Force Unix-style (LF only)
with open("output.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write("line\n")  # Always writes \n

# Force Windows-style (CRLF)
with open("output.txt", "w", encoding="utf-8", newline="\r\n") as f:
    f.write("line\n")  # Always writes \r\n

# No translation (write exactly what you specify)
with open("output.txt", "w", encoding="utf-8", newline="") as f:
    f.write("line\n")  # Writes exactly \n
```

**Best practice for CSV**: Use `newline=""` to let the csv module handle line endings.

---

## Encoding

### Always Specify Encoding

```python
# Explicit UTF-8 (recommended)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, 世界! 🌍")

# UTF-8 with BOM (for Excel compatibility)
with open("output.txt", "w", encoding="utf-8-sig") as f:
    f.write("Data for Excel")
```

### Handling Unencodable Characters

```python
# Strict (default) — raises error
with open("output.txt", "w", encoding="ascii") as f:
    f.write("café")  # UnicodeEncodeError

# Replace with ?
with open("output.txt", "w", encoding="ascii", errors="replace") as f:
    f.write("café")  # Writes "caf?"

# Ignore unencodable
with open("output.txt", "w", encoding="ascii", errors="ignore") as f:
    f.write("café")  # Writes "caf"

# XML character reference
with open("output.txt", "w", encoding="ascii", errors="xmlcharrefreplace") as f:
    f.write("café")  # Writes "caf&#233;"
```

---

## Buffering and Flushing

### Buffering Modes

```python
# Default buffering (system-dependent, usually 4KB-8KB)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("buffered")

# Line buffered (flush on newline)
with open("output.txt", "w", encoding="utf-8", buffering=1) as f:
    f.write("line buffered\n")  # Flushed immediately

# Unbuffered (not allowed for text mode)
# buffering=0 only works with binary mode

# Custom buffer size
with open("output.txt", "w", encoding="utf-8", buffering=8192) as f:
    f.write("8KB buffer")
```

### Manual Flushing

```python
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("Important event")
    f.flush()  # Force write to disk now
    
    # More writes...
    f.write("Another event")
    # Automatically flushed when file closes
```

**Use `flush()` when:**
- Writing logs that need immediate visibility
- Long-running processes
- Before potentially crashing operations

---

## Error Handling

### Permission Denied

```python
try:
    with open("/root/file.txt", "w") as f:
        f.write("data")
except PermissionError:
    print("Cannot write to this location")
```

### Disk Full

```python
try:
    with open("huge_file.txt", "w", encoding="utf-8") as f:
        f.write("x" * 10_000_000_000)
except OSError as e:
    print(f"Write failed: {e}")
```

### Safe Write Pattern

Write to temp file, then rename (atomic on most systems):

```python
import os
from pathlib import Path

def safe_write(filepath, content):
    """Write atomically to avoid partial writes."""
    path = Path(filepath)
    temp_path = path.with_suffix(".tmp")
    
    try:
        temp_path.write_text(content, encoding="utf-8")
        temp_path.rename(path)  # Atomic on same filesystem
    except:
        temp_path.unlink(missing_ok=True)  # Clean up temp
        raise

safe_write("config.json", '{"key": "value"}')
```

---

## Common Patterns

### Write List to File

```python
items = ["apple", "banana", "cherry"]

# One item per line
with open("items.txt", "w", encoding="utf-8") as f:
    for item in items:
        f.write(item + "\n")

# Using print
with open("items.txt", "w", encoding="utf-8") as f:
    for item in items:
        print(item, file=f)

# Using writelines with newlines
with open("items.txt", "w", encoding="utf-8") as f:
    f.writelines(item + "\n" for item in items)

# Join then write
with open("items.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(items))
```

### Append with Timestamp

```python
from datetime import datetime

def log(message, filepath="app.log"):
    """Append timestamped message to log file."""
    timestamp = datetime.now().isoformat()
    with open(filepath, "a", encoding="utf-8") as f:
        print(f"[{timestamp}] {message}", file=f)

log("Application started")
log("User logged in")
```

### Create Parent Directories

```python
from pathlib import Path

def write_file(filepath, content):
    """Write file, creating parent directories if needed."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

write_file("output/reports/2025/january.txt", "Report content")
```

---

## Key Takeaways

- `"w"` truncates existing files — use `"a"` to append
- `write()` does **not** add newlines — add them yourself
- `writelines()` does **not** add newlines between items
- Use `print(..., file=f)` for convenient formatted output
- Always specify `encoding="utf-8"` for portability
- Use `newline=""` for CSV files
- Use `flush()` for immediate writes (logs, real-time data)
- Consider atomic writes for critical files
