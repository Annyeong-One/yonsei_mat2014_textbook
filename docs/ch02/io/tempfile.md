# tempfile Module

The tempfile module creates temporary files and directories with automatic cleanup. It is essential for safe temporary storage without polluting the file system.

---

## Named Temporary Files

### Creating Temp Files

```python
import tempfile
import os

with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write("Temporary content")
    temp_name = f.name

print(f"File: {temp_name}")
print(f"Exists: {os.path.exists(temp_name)}")

os.unlink(temp_name)
```

Output:
```
File: /tmp/tmpXXXXXXXX
Exists: True
```

### Auto-Cleanup Context Manager

```python
import tempfile

with tempfile.NamedTemporaryFile(mode='w', delete=True) as f:
    f.write("Data")
    f.flush()
    print(f"Writing to {f.name}")

print(f"After context: file deleted")
```

Output:
```
Writing to /tmp/tmpXXXXXXXX
After context: file deleted
```

## Temporary Directories

### Creating Temp Directories

```python
import tempfile
import os

with tempfile.TemporaryDirectory() as tmpdir:
    filepath = os.path.join(tmpdir, "file.txt")
    with open(filepath, 'w') as f:
        f.write("Data")
    print(f"Created: {filepath}")

print(f"Directory cleaned up")
```

Output:
```
Created: /tmp/tmpXXXXXXXX/file.txt
Directory cleaned up
```

## SpooledTemporaryFile

### In-Memory Until Size Limit

```python
import tempfile

with tempfile.SpooledTemporaryFile(max_size=1024, mode='w+') as f:
    f.write("Small data")
    f.seek(0)
    print(f.read())
```

Output:
```
Small data
```

## Practical Usage

### Temporary Processing

```python
import tempfile
import os

data = ["line1\n", "line2\n", "line3\n"]

with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
    f.writelines(data)
    temp_file = f.name

with open(temp_file, 'r') as f:
    lines = f.readlines()
    print(f"Read {len(lines)} lines")

os.unlink(temp_file)
```

Output:
```
Read 3 lines
```
