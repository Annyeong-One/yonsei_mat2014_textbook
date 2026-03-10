# sys Runtime Information


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Access runtime information like memory usage, loaded modules, and recursion limits.

## Memory and Resource Information

Check memory and system resources.

```python
import sys
import gc

# Garbage collection
gc.collect()
print(f"GC stats: {gc.get_stats()}")

# Reference count
x = [1, 2, 3]
print(f"Reference count: {sys.getrefcount(x)}")

# Recursion limit
print(f"Recursion limit: {sys.getrecursionlimit()}")

# Stack info
import traceback
print(f"Call stack depth: {len(traceback.extract_stack())}")
```

```
GC stats: [{'collections': 123}]
Reference count: 2
Recursion limit: 1000
Call stack depth: 5
```

## Modules and Paths

Check loaded modules and search paths.

```python
import sys

# Module path
print(f"Python path: {sys.path[:3]}")

# Loaded modules
core_modules = [m for m in sys.modules if not '.' in m]
print(f"Core modules loaded: {len(core_modules)}")

# Module info
if 'json' in sys.modules:
    print("json module is loaded")

# Standard modules
import json
print(f"json module path: {json.__file__}")
```

```
Python path: ['', '/usr/lib/python3.12', '/usr/lib/python3.12/lib-dynload']
Core modules loaded: 25
json module is loaded
json module path: /usr/lib/python3.12/json/__init__.py
```

