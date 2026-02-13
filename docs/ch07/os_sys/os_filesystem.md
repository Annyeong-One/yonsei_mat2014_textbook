# File System Operations (os)

Perform file and directory operations like creating, removing, listing, and copying.

## Directory Operations

Create and navigate directories.

```python
import os
import tempfile
import shutil

# Create temporary directory
temp_dir = tempfile.mkdtemp()
print(f"Created: {temp_dir}")

try:
    # Create subdirectory
    subdir = os.path.join(temp_dir, 'subdir')
    os.makedirs(subdir, exist_ok=True)
    print(f"Created subdir: {subdir}")
    
    # List directory contents
    os.chdir(temp_dir)
    print(f"Contents: {os.listdir('.')}")
finally:
    shutil.rmtree(temp_dir)
```

```
Created: /tmp/tmpXXXXXX
Created subdir: /tmp/tmpXXXXXX/subdir
Contents: ['subdir']
```

## File Operations

Create, rename, and remove files.

```python
import os
import tempfile

temp_dir = tempfile.mkdtemp()
try:
    # Create file
    file1 = os.path.join(temp_dir, 'file1.txt')
    with open(file1, 'w') as f:
        f.write('content')
    print(f"Created: {os.path.basename(file1)}")
    
    # Rename file
    file2 = os.path.join(temp_dir, 'file2.txt')
    os.rename(file1, file2)
    print(f"Renamed to: {os.path.basename(file2)}")
    
    # Remove file
    os.remove(file2)
    print("Removed file")
finally:
    import shutil
    shutil.rmtree(temp_dir)
```

```
Created: file1.txt
Renamed to: file2.txt
Removed file
```

