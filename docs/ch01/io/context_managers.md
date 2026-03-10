# Context Managers


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Context managers ensure that resources are properly acquired and released. For file I/O, they guarantee files are closed even when errors occur.

---

## The Problem Without Context Managers

If an exception occurs, cleanup code may never run:

```python
f = open("data.txt", "r")
data = f.read()
result = process(data)  # What if this raises an exception?
f.close()               # Never reached!
```

The file handle leaks, potentially causing:
- Resource exhaustion (too many open files)
- Data loss (unflushed write buffers)
- Locked files (on Windows)

### try/finally Solution

```python
f = open("data.txt", "r")
try:
    data = f.read()
    result = process(data)
finally:
    f.close()  # Always runs, even if exception occurs
```

This works but is verbose and error-prone.

---

## The `with` Statement

The `with` statement provides clean, automatic resource management:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    data = f.read()
    result = process(data)
# File is automatically closed here, even if exception occurred
```

### Multiple Resources

```python
with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
    for line in fin:
        fout.write(line.upper())

# Or across multiple lines (Python 3.10+)
with (
    open("input.txt", "r") as fin,
    open("output.txt", "w") as fout,
):
    for line in fin:
        fout.write(line.upper())
```

### Nested `with` Statements

```python
with open("config.txt", "r") as config_file:
    config = config_file.read()
    
    with open("output.txt", "w") as output_file:
        output_file.write(f"Config: {config}")
```

---

## How Context Managers Work

A context manager is any object with `__enter__` and `__exit__` methods:

```python
with expression as variable:
    # block
```

Translates to:

```python
manager = expression
variable = manager.__enter__()
try:
    # block
finally:
    manager.__exit__(exc_type, exc_val, exc_tb)
```

### The Protocol

| Method | Called When | Returns |
|--------|-------------|---------|
| `__enter__()` | Entering `with` block | Value bound to `as` variable |
| `__exit__(exc_type, exc_val, exc_tb)` | Exiting `with` block | `True` to suppress exception |

---

## Creating Custom Context Managers

### Class-Based

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False  # Don't suppress exceptions

# Usage
with FileManager("data.txt", "r") as f:
    content = f.read()
```

### Practical Example: Timer

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f} seconds")
        return False

# Usage
with Timer():
    # Code to time
    sum(range(1_000_000))
# Output: Elapsed: 0.0234 seconds
```

### Practical Example: Database Transaction

```python
class Transaction:
    def __init__(self, connection):
        self.conn = connection
    
    def __enter__(self):
        return self.conn.cursor()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        return False

# Usage
with Transaction(db_connection) as cursor:
    cursor.execute("INSERT INTO users VALUES (?)", ("Alice",))
    cursor.execute("INSERT INTO logs VALUES (?)", ("User added",))
# Commits if no exception, rolls back otherwise
```

---

## contextlib Module

The `contextlib` module provides utilities for creating context managers.

### @contextmanager Decorator

Create context managers using a generator function:

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    f = open(filename, mode)
    try:
        yield f          # Value yielded is bound to 'as' variable
    finally:
        f.close()

# Usage
with file_manager("data.txt", "r") as f:
    content = f.read()
```

### @contextmanager Pattern

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    # Setup (like __enter__)
    print("Acquiring resource")
    resource = acquire_resource()
    
    try:
        yield resource   # Pause here, run with block
    finally:
        # Cleanup (like __exit__)
        print("Releasing resource")
        release_resource(resource)
```

### Practical Example: Temporary Directory Change

```python
import os
from contextlib import contextmanager

@contextmanager
def change_directory(path):
    """Temporarily change working directory."""
    original = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(original)

# Usage
with change_directory("/tmp"):
    print(os.getcwd())  # /tmp
print(os.getcwd())      # Back to original
```

### Practical Example: Redirect stdout

```python
import sys
from contextlib import contextmanager
from io import StringIO

@contextmanager
def capture_output():
    """Capture stdout to a string."""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = old_stdout

# Usage
with capture_output() as output:
    print("Hello")
    print("World")

captured = output.getvalue()
print(f"Captured: {captured!r}")  # 'Hello\nWorld\n'
```

---

## contextlib Utilities

### closing()

Wrap objects that have `.close()` but aren't context managers:

```python
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen("https://example.com")) as page:
    content = page.read()
# page.close() called automatically
```

### suppress()

Suppress specific exceptions:

```python
from contextlib import suppress

# Without suppress
try:
    os.remove("file.txt")
except FileNotFoundError:
    pass

# With suppress
with suppress(FileNotFoundError):
    os.remove("file.txt")
```

### redirect_stdout / redirect_stderr

Redirect output streams:

```python
from contextlib import redirect_stdout
from io import StringIO

f = StringIO()
with redirect_stdout(f):
    print("Hello")
    help(len)

output = f.getvalue()
```

### nullcontext()

A no-op context manager (useful for conditional context managers):

```python
from contextlib import nullcontext

def process(filepath, use_lock=False):
    lock = threading.Lock() if use_lock else nullcontext()
    
    with lock:
        with open(filepath) as f:
            return f.read()
```

### ExitStack

Manage a dynamic number of context managers:

```python
from contextlib import ExitStack

filenames = ["file1.txt", "file2.txt", "file3.txt"]

with ExitStack() as stack:
    files = [stack.enter_context(open(fn)) for fn in filenames]
    
    # All files are open here
    for f in files:
        print(f.readline())
# All files closed here
```

---

## Exception Handling in __exit__

The `__exit__` method receives exception info:

```python
class LoggingContext:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Exception: {exc_type.__name__}: {exc_val}")
        return False  # Re-raise exception

with LoggingContext():
    raise ValueError("Something went wrong")
# Prints: Exception: ValueError: Something went wrong
# Then re-raises the exception
```

### Suppressing Exceptions

Return `True` from `__exit__` to suppress the exception:

```python
class SuppressErrors:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Suppressed: {exc_val}")
            return True  # Suppress exception
        return False

with SuppressErrors():
    raise ValueError("This won't propagate")
print("Continues normally")
```

---

## Common Built-in Context Managers

| Context Manager | Purpose |
|-----------------|---------|
| `open()` | File I/O |
| `threading.Lock()` | Thread synchronization |
| `decimal.localcontext()` | Temporary decimal settings |
| `warnings.catch_warnings()` | Temporarily modify warnings |
| `unittest.mock.patch()` | Mocking in tests |
| `tempfile.TemporaryFile()` | Auto-deleted temp files |
| `tempfile.TemporaryDirectory()` | Auto-deleted temp directories |

---

## Key Takeaways

- Always use `with` for file I/O — guarantees cleanup
- Context managers handle setup and teardown automatically
- `__enter__` returns the resource, `__exit__` cleans up
- Use `@contextmanager` decorator for simple cases
- `contextlib` provides utilities: `closing`, `suppress`, `ExitStack`
- Return `True` from `__exit__` to suppress exceptions
- Essential for: files, locks, database connections, temporary resources
