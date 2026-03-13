# os Module Overview

The `os` module provides a portable way to interact with the operating system, including file operations, environment variables, and process management.

## os Module Basics

Access operating system functionality.

```python
import os

# Get current working directory
cwd = os.getcwd()
print(f"Current directory: {cwd}")

# Get environment variables
path = os.environ.get('PATH', 'Not set')
print(f"PATH exists: {bool(path)}")

# Get OS name
print(f"OS: {os.name}")

# Get system
import platform
print(f"System: {platform.system()}")
```

```
Current directory: /home/user
PATH exists: True
OS: posix
System: Linux
```

## File and Directory Information

Get information about files and directories.

```python
import os
import tempfile

# Create temp file for demo
with tempfile.NamedTemporaryFile(delete=False) as f:
    temp_path = f.name
    f.write(b"test content")

try:
    # Check file existence
    print(f"File exists: {os.path.exists(temp_path)}")
    
    # Check file type
    print(f"Is file: {os.path.isfile(temp_path)}")
    print(f"Is dir: {os.path.isdir(temp_path)}")
    
    # Get file size
    print(f"Size: {os.path.getsize(temp_path)} bytes")
finally:
    os.unlink(temp_path)
```

```
File exists: True
Is file: True
Is dir: False
Size: 12 bytes
```

