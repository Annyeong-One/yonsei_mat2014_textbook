# Scripts vs Modules


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python files can act as **scripts**, **modules**, or both. Understanding the difference is essential for organizing code properly.

---

## Scripts

A **script** is a Python file designed to be **executed directly**.

### Characteristics

- Run with `python script.py`
- Performs a specific task
- Often has side effects (I/O, printing, file operations)
- Entry point for a program

### Example Script

```python
# backup.py - A simple backup script
import shutil
import datetime

source = "/home/user/documents"
dest = f"/backup/documents_{datetime.date.today()}"

shutil.copytree(source, dest)
print(f"Backup created: {dest}")
```

Run:
```bash
python backup.py
```

---

## Modules

A **module** is a Python file designed to be **imported** by other code.

### Characteristics

- Imported with `import module`
- Provides reusable functions, classes, constants
- Avoids side effects at import time
- No execution when imported

### Example Module

```python
# mathutils.py - A reusable math module
PI = 3.14159

def circle_area(radius):
    """Calculate the area of a circle."""
    return PI * radius ** 2

def circle_circumference(radius):
    """Calculate the circumference of a circle."""
    return 2 * PI * radius
```

Use:
```python
>>> from mathutils import circle_area
>>> circle_area(5)
78.53975
```

---

## The Problem: Script That Can't Be Imported

```python
# bad_example.py
def process_data(data):
    return [x * 2 for x in data]

# This runs on import!
data = [1, 2, 3, 4, 5]
result = process_data(data)
print(f"Result: {result}")
```

```python
>>> import bad_example
Result: [2, 4, 6, 8, 10]  # Unwanted!
```

---

## Combining Both Roles

Use the **main guard** to create files that work as both:

```python
# good_example.py
def process_data(data):
    """Double each element in the data."""
    return [x * 2 for x in data]

def main():
    """Entry point when run as script."""
    data = [1, 2, 3, 4, 5]
    result = process_data(data)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```

**As script:**
```bash
$ python good_example.py
Result: [2, 4, 6, 8, 10]
```

**As module:**
```python
>>> from good_example import process_data
>>> process_data([10, 20, 30])
[20, 40, 60]
# No output printed
```

---

## Running as Script vs Module

| Method | Command | `__name__` | Relative Imports |
|--------|---------|------------|------------------|
| Script | `python file.py` | `"__main__"` | ❌ Don't work |
| Module | `python -m package.file` | `"__main__"` | ✅ Work |
| Import | `import file` | `"file"` | ✅ Work |

### Script Mode

```bash
python mypackage/main.py
```

- Runs file directly
- No package context
- Relative imports fail
- `sys.path[0]` = script's directory

### Module Mode

```bash
python -m mypackage.main
```

- Runs through import system
- Has package context
- Relative imports work
- `sys.path[0]` = current directory

---

## Project Structure

### Small Project (Single File)

Both script and module in one file:

```
project/
└── calculator.py
```

```python
# calculator.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))
```

### Medium Project (Separate Entry Point)

```
project/
├── main.py           # Script (entry point)
└── calculator.py     # Module (library code)
```

```python
# calculator.py (module - no main guard needed)
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

```python
# main.py (script)
from calculator import add, multiply

def main():
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")

if __name__ == "__main__":
    main()
```

### Large Project (Package Structure)

```
project/
├── setup.py
├── mypackage/
│   ├── __init__.py
│   ├── __main__.py    # Entry point for `python -m mypackage`
│   ├── core.py        # Module
│   ├── utils.py       # Module
│   └── cli.py         # Module with CLI logic
└── scripts/
    └── run_analysis.py  # Standalone script
```

---

## The `__main__.py` File

For packages, `__main__.py` enables running with `-m`:

```python
# mypackage/__main__.py
from .cli import main

if __name__ == "__main__":
    main()
```

```bash
python -m mypackage  # Runs __main__.py
```

---

## Best Practices

### For Scripts

```python
#!/usr/bin/env python3
"""Script to process data files."""

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Process data")
    parser.add_argument("input", help="Input file")
    parser.add_argument("-o", "--output", help="Output file")
    args = parser.parse_args()
    
    # Do processing...
    print(f"Processing {args.input}")

if __name__ == "__main__":
    sys.exit(main() or 0)
```

### For Modules

```python
"""Utility functions for data processing.

This module provides functions for transforming and analyzing data.

Example:
    >>> from mymodule import transform
    >>> transform([1, 2, 3])
    [2, 4, 6]
"""

def transform(data):
    """Double each element."""
    return [x * 2 for x in data]

def analyze(data):
    """Return basic statistics."""
    return {
        'min': min(data),
        'max': max(data),
        'mean': sum(data) / len(data)
    }

# No main guard needed for pure modules
# But you can add one for testing:
if __name__ == "__main__":
    # Quick test
    test_data = [1, 2, 3, 4, 5]
    print(f"Transform: {transform(test_data)}")
    print(f"Analyze: {analyze(test_data)}")
```

---

## Summary

| Aspect | Script | Module |
|--------|--------|--------|
| Purpose | Execute task | Provide reusable code |
| How to use | `python file.py` | `import file` |
| Side effects | Expected | Avoid |
| Entry point | Yes | No (unless main guard) |
| Main guard | Required if also module | Optional |

---

## Key Takeaways

- **Scripts** are entry points; **modules** are libraries
- Use **main guard** to support both roles
- Use `python -m package.module` for proper package context
- Separate entry points from library code in larger projects
- Add `__main__.py` to make packages directly executable
