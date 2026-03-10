# Import Mechanics


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python's `import` system allows code to be organized into reusable **modules**. Understanding how imports work is essential for structuring larger projects.

---

## Import Forms

### Basic Import

```python
import math

math.sqrt(16)       # 4.0
math.pi             # 3.14159...
```

The module object is bound to the name `math`.

### Import with Alias

```python
import numpy as np

np.array([1, 2, 3])
```

Useful for long module names.

### Import Specific Names

```python
from math import sqrt, pi

sqrt(16)            # 4.0 (no prefix needed)
pi                  # 3.14159...
```

Only the specified names are bound.

### Import with Alias (from)

```python
from math import sqrt as s

s(16)               # 4.0
```

### Wildcard Import (Discouraged)

```python
from math import *

sin(0)              # Works, but origin unclear
```

Pollutes namespace and breaks static analysis. Avoid in production code.

---

## What Happens During Import

When Python executes `import mymodule`:

### Step 1: Check Cache

```python
import sys
'mymodule' in sys.modules  # Already imported?
```

If cached, return the cached module object immediately.

### Step 2: Search for Module

Python searches directories in `sys.path`:
1. Current script's directory
2. `PYTHONPATH` directories
3. Standard library
4. Site-packages

### Step 3: Execute Module Code

The module's top-level code runs **once**:

```python
# mymodule.py
print("Module is being loaded!")  # Runs on first import

def greet():
    return "Hello"
```

### Step 4: Create Module Object

Python creates a `module` object containing all definitions.

### Step 5: Cache in sys.modules

```python
import sys
import mymodule

sys.modules['mymodule']  # <module 'mymodule' from '...'>
```

### Step 6: Bind Name

The module object is bound to the name in your namespace.

---

## Import Caching: sys.modules

Modules are imported **once** per session:

```python
import mymodule     # Executes module code
import mymodule     # Uses cached version (no re-execution)
import mymodule     # Still cached
```

### Viewing the Cache

```python
import sys

# All loaded modules
print(list(sys.modules.keys()))

# Check specific module
print(sys.modules.get('os'))
```

### Why Caching Matters

- Avoids duplicate side effects
- Improves performance
- Ensures consistent state across imports

---

## Reloading Modules

To force re-execution (useful in development):

```python
import importlib
import mymodule

# Edit mymodule.py...

importlib.reload(mymodule)  # Re-executes the module
```

**Caveats:**
- Doesn't reload submodules automatically
- Existing references to old objects persist
- Use sparingly; restart interpreter for clean state

---

## Module Objects

Modules are objects with attributes:

```python
import math

type(math)              # <class 'module'>
math.__name__           # 'math'
math.__file__           # '/usr/lib/python3.11/lib-dynload/math.cpython-311-...'
math.__dict__.keys()    # All names defined in module
dir(math)               # List of attributes
```

### The Module Namespace

A module's namespace is its `__dict__`:

```python
import mymodule

# These are equivalent:
mymodule.some_function
mymodule.__dict__['some_function']
```

---

## Import Syntax Comparison

| Syntax | What It Imports | How to Access |
|--------|-----------------|---------------|
| `import math` | Module object | `math.sqrt()` |
| `import math as m` | Module with alias | `m.sqrt()` |
| `from math import sqrt` | Function directly | `sqrt()` |
| `from math import sqrt as s` | Function with alias | `s()` |
| `from math import *` | All public names | `sqrt()`, `sin()`, etc. |

---

## What Can Be Imported

### `import X` — Only Modules/Packages

```python
import os           # ✅ Module
import numpy        # ✅ Package
import math.sqrt    # ❌ sqrt is a function, not module
```

### `from X import Y` — Anything

```python
from math import sqrt       # ✅ Function
from datetime import date   # ✅ Class
from os.path import join    # ✅ Function from submodule
from numpy import array     # ✅ Function
from mypackage import submodule  # ✅ Module
```

---

## Circular Imports

When two modules import each other:

```python
# a.py
from b import func_b

def func_a():
    return "A"

# b.py
from a import func_a  # ImportError or AttributeError

def func_b():
    return "B"
```

### Solutions

**1. Move import inside function:**

```python
# b.py
def func_b():
    from a import func_a  # Deferred import
    return func_a()
```

**2. Import module, not name:**

```python
# b.py
import a

def func_b():
    return a.func_a()
```

**3. Restructure code:**

Move shared code to a third module.

---

## Import Best Practices

### Do

```python
# Group imports at top of file
import os
import sys

import numpy as np
import pandas as pd

from mypackage import mymodule
```

### Don't

```python
from module import *              # Namespace pollution
import sys, os, math              # Multiple imports on one line
from package import a, b, c, d, e  # Too many names
```

### PEP 8 Import Order

1. Standard library (`os`, `sys`, `math`)
2. Third-party packages (`numpy`, `pandas`)
3. Local packages (`mypackage`)

Separate groups with blank lines.

---

## Key Takeaways

- Imports bind names to module objects or their contents
- Module code executes **once** on first import
- Imports are cached in `sys.modules`
- Use `importlib.reload()` to re-execute during development
- Avoid circular imports through restructuring or deferred imports
- Follow PEP 8 import ordering conventions
