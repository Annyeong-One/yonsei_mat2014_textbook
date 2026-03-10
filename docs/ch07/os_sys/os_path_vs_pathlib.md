# os.path vs pathlib


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Compare the traditional os.path module with the modern pathlib module for path operations.

## os.path Approach

Traditional string-based path manipulation.

```python
import os

# Build path with os.path.join
parts = ['home', 'user', 'documents', 'file.txt']
path = os.path.join(*parts)
print(f"os.path: {path}")

# Extract components
print(f"dirname: {os.path.dirname(path)}")
print(f"basename: {os.path.basename(path)}")
print(f"split: {os.path.splitext(path)}")

# Check file
import tempfile
with tempfile.NamedTemporaryFile() as f:
    print(f"exists: {os.path.exists(f.name)}")
```

```
os.path: home/user/documents/file.txt
dirname: home/user/documents
basename: file.txt
split: ('home/user/documents/file', '.txt')
exists: True
```

## pathlib Approach

Modern object-oriented path manipulation.

```python
from pathlib import Path
import tempfile

# Create Path object
path = Path('home') / 'user' / 'documents' / 'file.txt'
print(f"pathlib: {path}")

# Access components
print(f"parent: {path.parent}")
print(f"name: {path.name}")
print(f"suffix: {path.suffix}")
print(f"stem: {path.stem}")

# Check file
with tempfile.NamedTemporaryFile() as f:
    p = Path(f.name)
    print(f"exists: {p.exists()}")
    print(f"is_file: {p.is_file()}")
```

```
pathlib: home/user/documents/file.txt
parent: home/user/documents
name: file.txt
suffix: .txt
stem: file
exists: True
is_file: True
```

