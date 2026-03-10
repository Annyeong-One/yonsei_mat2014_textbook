# Post-Mortem Debugging


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Debug a program after it crashes using post-mortem debugging.

## Post-Mortem Debugging with pdb

Debug exceptions after they occur.

```python
import pdb
import traceback

def buggy_function():
    x = 10
    y = 0
    return x / y  # This will raise ZeroDivisionError

try:
    result = buggy_function()
except Exception:
    # Start debugging at the point of exception
    traceback.print_exc()
    pdb.post_mortem()
    # Now you can inspect the call stack and variables
```

```
Traceback (most recent call last):
  File "script.py", line 9, in <module>
    result = buggy_function()
  File "script.py", line 5, in buggy_function
    return x / y
ZeroDivisionError: division by zero
```

## Debugging Exceptions

Inspect exceptions and their context.

```python
import sys
import pdb

def analyze_error():
    items = [1, 2, 3]
    try:
        result = items[10]  # IndexError
    except IndexError:
        # Get exception info
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(f"Exception: {exc_type.__name__}")
        print(f"Message: {exc_value}")
        print(f"Traceback present: {exc_tb is not None}")
        
        # Use traceback to understand the error
        import traceback
        traceback.print_tb(exc_tb)

analyze_error()
```

```
Exception: IndexError
Message: list index out of range
Traceback present: True
```

