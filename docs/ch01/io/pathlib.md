# Path Handling

The `pathlib` module provides object-oriented filesystem path operations. It offers cleaner syntax than `os.path` and works consistently across operating systems.

## Creating Paths

Construct `Path` objects to represent filesystem locations.

### 1. Basic Construction

Create paths from strings or path components.

```python
from pathlib import Path

# From string
p = Path("/home/user/docs")

# Current directory
cwd = Path(".")
cwd = Path.cwd()

# Home directory
home = Path.home()

# Relative path
rel = Path("data/file.txt")
```

### 2. Joining Paths

Use `/` operator to join path components.

```python
from pathlib import Path

base = Path("/home/user")

# Join with /
full = base / "docs" / "file.txt"
print(full)  # /home/user/docs/file.txt

# Join with variable
filename = "report.pdf"
path = base / "downloads" / filename
```

### 3. Platform Paths

Use platform-specific path classes when needed.

```python
from pathlib import Path, PurePosixPath, PureWindowsPath

# Automatic platform detection
p = Path("data/file.txt")

# Force POSIX style (Linux/Mac)
posix = PurePosixPath("data/file.txt")
print(posix)  # data/file.txt

# Force Windows style
win = PureWindowsPath("data/file.txt")
print(win)    # data\file.txt
```

## Path Components

Extract parts of a path.

### 1. Name and Suffix

Get filename and extension.

```python
from pathlib import Path

p = Path("/home/user/docs/report.tar.gz")

print(p.name)      # report.tar.gz
print(p.stem)      # report.tar
print(p.suffix)    # .gz
print(p.suffixes)  # ['.tar', '.gz']
```

### 2. Parent Directories

Access parent paths.

```python
from pathlib import Path

p = Path("/home/user/docs/report.txt")

print(p.parent)    # /home/user/docs
print(p.parents[0])  # /home/user/docs
print(p.parents[1])  # /home/user
print(p.parents[2])  # /home

# All parents
for parent in p.parents:
    print(parent)
```

### 3. Parts Tuple

Split path into components.

```python
from pathlib import Path

p = Path("/home/user/docs/file.txt")

print(p.parts)
# ('/', 'home', 'user', 'docs', 'file.txt')

print(p.anchor)    # /
print(p.root)      # /
```

## Path Operations

Modify and manipulate paths.

### 1. Change Extension

Create new path with different suffix.

```python
from pathlib import Path

p = Path("data/report.txt")

# Change extension
pdf = p.with_suffix(".pdf")
print(pdf)  # data/report.pdf

# Remove extension
no_ext = p.with_suffix("")
print(no_ext)  # data/report

# Add extension
backup = p.with_suffix(".txt.bak")
print(backup)  # data/report.txt.bak
```

### 2. Change Name

Create new path with different filename.

```python
from pathlib import Path

p = Path("/home/user/old_name.txt")

# Change entire name
new = p.with_name("new_name.txt")
print(new)  # /home/user/new_name.txt

# Change stem only
renamed = p.with_stem("renamed")
print(renamed)  # /home/user/renamed.txt
```

### 3. Resolve and Absolute

Get canonical absolute paths.

```python
from pathlib import Path

p = Path("./data/../data/file.txt")

# Resolve to absolute, normalized path
resolved = p.resolve()
print(resolved)  # /full/path/data/file.txt

# Check if absolute
print(p.is_absolute())         # False
print(resolved.is_absolute())  # True

# Make absolute without resolving
abs_path = p.absolute()
```

## File System Queries

Check path properties and existence.

### 1. Existence Checks

Test if paths exist and their types.

```python
from pathlib import Path

p = Path("some/path")

print(p.exists())      # True/False
print(p.is_file())     # True if regular file
print(p.is_dir())      # True if directory
print(p.is_symlink())  # True if symbolic link
```

### 2. File Properties

Get file metadata.

```python
from pathlib import Path
import datetime

p = Path("file.txt")

if p.exists():
    stat = p.stat()
    print(f"Size: {stat.st_size} bytes")
    print(f"Modified: {stat.st_mtime}")
    
    # Human-readable time
    mtime = datetime.datetime.fromtimestamp(stat.st_mtime)
    print(f"Modified: {mtime}")
```

### 3. Path Matching

Check if path matches a pattern.

```python
from pathlib import Path

p = Path("data/report_2025.csv")

# Simple pattern matching
print(p.match("*.csv"))           # True
print(p.match("report_*.csv"))    # True
print(p.match("data/*.csv"))      # True
print(p.match("**/*.csv"))        # True
```

## Directory Operations

Work with directories and their contents.

### 1. Listing Contents

Iterate over directory contents.

```python
from pathlib import Path

p = Path(".")

# All items (non-recursive)
for item in p.iterdir():
    print(item)

# Only files
files = [f for f in p.iterdir() if f.is_file()]

# Only directories
dirs = [d for d in p.iterdir() if d.is_dir()]
```

### 2. Glob Patterns

Find files matching patterns.

```python
from pathlib import Path

p = Path(".")

# All .py files in current dir
for py in p.glob("*.py"):
    print(py)

# Recursive search
for py in p.rglob("*.py"):
    print(py)

# Multiple patterns
for f in p.glob("*.{py,txt}"):
    print(f)
```

### 3. Create Directories

Make new directories.

```python
from pathlib import Path

# Create single directory
p = Path("new_folder")
p.mkdir()

# Create with parents
p = Path("path/to/new/folder")
p.mkdir(parents=True)

# Ignore if exists
p.mkdir(parents=True, exist_ok=True)
```

## File Operations

Read, write, and manipulate files.

### 1. Quick Read/Write

Convenience methods for simple file I/O.

```python
from pathlib import Path

p = Path("data.txt")

# Write text
p.write_text("Hello, World!")

# Read text
content = p.read_text()
print(content)  # Hello, World!

# Write bytes
p.write_bytes(b"\x00\x01\x02")

# Read bytes
data = p.read_bytes()
```

### 2. File Management

Delete, rename, and copy files.

```python
from pathlib import Path
import shutil

p = Path("file.txt")

# Delete file
p.unlink()

# Delete if exists
p.unlink(missing_ok=True)

# Rename/move
new_path = p.rename("new_name.txt")

# Copy (use shutil)
shutil.copy(p, Path("backup.txt"))
```

### 3. Touch and Create

Create empty files or update timestamps.

```python
from pathlib import Path

p = Path("new_file.txt")

# Create empty file (or update mtime)
p.touch()

# Create only if doesn't exist
p.touch(exist_ok=True)
```

## Common Patterns

Practical pathlib usage patterns.

### 1. Safe File Processing

Process files with existence checks.

```python
from pathlib import Path

def process_file(filepath):
    """Safely process a file."""
    p = Path(filepath)
    
    if not p.exists():
        raise FileNotFoundError(f"Not found: {p}")
    
    if not p.is_file():
        raise ValueError(f"Not a file: {p}")
    
    return p.read_text()
```

### 2. Output Directory

Ensure output directory exists.

```python
from pathlib import Path

def save_report(name, content):
    """Save report to output directory."""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    filepath = output_dir / f"{name}.txt"
    filepath.write_text(content)
    
    return filepath
```

### 3. Find Project Root

Locate project root by marker file.

```python
from pathlib import Path

def find_project_root(marker=".git"):
    """Find project root containing marker."""
    current = Path.cwd()
    
    for parent in [current] + list(current.parents):
        if (parent / marker).exists():
            return parent
    
    raise FileNotFoundError(f"No {marker} found")

root = find_project_root()
config = root / "config" / "settings.json"
```
