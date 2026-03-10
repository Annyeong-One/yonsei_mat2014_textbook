# sys.path and Module Search


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python searches for modules in a well-defined order stored in `sys.path`. Understanding this is crucial for managing imports in larger projects.

---

## The Module Search Path

```python
import sys

for path in sys.path:
    print(path)
```

Example output:
```
/home/user/project          # Script's directory
/usr/lib/python311.zip
/usr/lib/python3.11
/usr/lib/python3.11/lib-dynload
/home/user/.local/lib/python3.11/site-packages
/usr/lib/python3.11/site-packages
```

---

## Search Order

When you `import mymodule`, Python searches in this order:

| Priority | Location | Description |
|----------|----------|-------------|
| 1 | Script directory | Directory containing the running script |
| 2 | `PYTHONPATH` | Directories in this environment variable |
| 3 | Standard library | Built-in modules and standard lib |
| 4 | Site-packages | Installed third-party packages |

**First match wins** — Python stops searching after finding the module.

---

## sys.path[0]: The Script Directory

The first entry is always the script's directory (or empty string for interactive):

```python
# /home/user/project/main.py
import sys
print(sys.path[0])  # '/home/user/project'
```

This allows importing sibling modules:

```
project/
├── main.py
└── utils.py    # Can be imported as: import utils
```

---

## PYTHONPATH Environment Variable

Add custom directories to the search path:

```bash
# Linux/macOS
export PYTHONPATH="/home/user/mylibs:/home/user/shared"

# Windows
set PYTHONPATH=C:\mylibs;C:\shared
```

These directories are added after the script directory but before the standard library.

```python
import sys
print(sys.path)
# ['', '/home/user/mylibs', '/home/user/shared', ...]
```

---

## Modifying sys.path at Runtime

### Append (Lower Priority)

```python
import sys
sys.path.append('/path/to/my/modules')
```

### Insert (Higher Priority)

```python
import sys
sys.path.insert(0, '/priority/path')
```

### Example

```python
import sys
sys.path.insert(0, '/home/user/custom_libs')

import mymodule  # Now searches /home/user/custom_libs first
```

---

## PATH vs sys.path vs PYTHONPATH

| Variable | Purpose | Used By |
|----------|---------|---------|
| `PATH` | Find **executables** (`python`, `pip`) | Operating system shell |
| `sys.path` | Find **Python modules** | Python import system |
| `PYTHONPATH` | Add directories to `sys.path` | Python (environment variable) |

```python
import os
import sys

# PATH: for executables
print(os.environ.get('PATH'))

# sys.path: for modules
print(sys.path)

# PYTHONPATH: affects sys.path
print(os.environ.get('PYTHONPATH'))
```

---

## Finding Where a Module Lives

### Using __file__

```python
import numpy
print(numpy.__file__)
# /usr/lib/python3.11/site-packages/numpy/__init__.py
```

### Using inspect

```python
import inspect
import os

print(inspect.getfile(os))
# /usr/lib/python3.11/os.py
```

### Check if Already Imported

```python
import sys

'numpy' in sys.modules  # True if imported
sys.modules['numpy']    # The module object
```

---

## Common Pitfalls

### 1. Name Shadowing

**Problem:** Local file shadows standard library.

```
project/
├── main.py
└── math.py    # Shadows built-in math!
```

```python
# main.py
import math    # Imports YOUR math.py, not the standard library!
math.sqrt(16)  # AttributeError!
```

**Solution:** Don't name files after standard library modules.

### 2. Importing from Wrong Directory

**Problem:** Multiple versions of a module exist.

```python
import sys
sys.path.insert(0, '/old/version')
sys.path.insert(0, '/new/version')

import mymodule  # Gets /new/version (first in path)
```

**Solution:** Use virtual environments to isolate dependencies.

### 3. Relative Path Issues

**Problem:** Script works from one directory but not another.

```python
# Fragile
sys.path.append('../lib')

# Better: Use absolute paths
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_dir, '..', 'lib'))
```

---

## Built-in Modules

Some modules are built into the interpreter (no `.py` file):

```python
import sys
print(sys.builtin_module_names)
# ('_abc', '_ast', '_codecs', 'builtins', 'sys', ...)
```

These are always available and searched before `sys.path`.

---

## Site-Packages

Third-party packages installed via `pip` go to site-packages:

```python
import site
print(site.getsitepackages())
# ['/usr/lib/python3.11/site-packages']

print(site.getusersitepackages())
# '/home/user/.local/lib/python3.11/site-packages'
```

---

## Best Practices

| Practice | Reason |
|----------|--------|
| Use virtual environments | Isolate project dependencies |
| Avoid modifying `sys.path` in code | Makes code non-portable |
| Use `pip install -e .` for local packages | Proper package management |
| Don't shadow standard library names | Prevents confusing bugs |
| Use absolute imports | More explicit and reliable |

---

## Debugging Import Issues

```python
import sys

# Where is Python looking?
print('\n'.join(sys.path))

# Is module already loaded?
print('numpy' in sys.modules)

# Where did module come from?
import mymodule
print(mymodule.__file__)

# Verbose import debugging
python -v script.py  # Shows all import steps
```

---

## Key Takeaways

- `sys.path` is a list of directories Python searches for modules
- First match wins — order matters
- Script's directory is always first in `sys.path`
- `PYTHONPATH` adds directories to the search path
- Avoid name collisions with standard library modules
- Use virtual environments instead of modifying `sys.path`
- Use `module.__file__` to find where a module is located
