# Package Init Files

The `__init__.py` file marks a directory as a Python package and serves as the package's entry point.

---

## Historical Context

**Python < 3.3**: `__init__.py` was required for packages.

**Python ≥ 3.3** (PEP 420): Namespace packages allow packages without `__init__.py`.

However, `__init__.py` remains essential for:

- Exposing a public API
- Initialization logic
- Controlling imports


---

## Core Responsibilities

### 1. Exposing the Package Interface

Re-export internal modules for cleaner imports:

```python
# mylib/__init__.py
from .core import MyModel
from .utils import save, load

__all__ = ["MyModel", "save", "load"]
```

Users can now write:

```python
from mylib import MyModel  # Instead of: from mylib.core import MyModel
```

### 2. Controlling Wildcard Imports

`__all__` defines what `from mylib import *` exports:

```python
# mylib/__init__.py
__all__ = ["foo", "bar"]  # Only these are exported with *
```

Without `__all__`, all public names (not starting with `_`) are exported.

### 3. Runtime Initialization

`__init__.py` runs during import — use for setup:

```python
# mylib/__init__.py
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Register plugins, load configs, etc.
from .registry import register_all
register_all()
```


---

## Lazy Imports

Defer heavy imports to reduce startup time:

```python
# mylib/__init__.py
def get_model():
    from .models import MyModel  # Only loaded when called
    return MyModel()
```

Useful when submodules have large dependencies (e.g., PyTorch, TensorFlow).


---

## Dynamic API Composition

Build APIs based on runtime conditions:

```python
# mylib/__init__.py
import os

if os.getenv("USE_GPU"):
    from .acceleration.cuda_backend import MatrixOps
else:
    from .acceleration.cpu_backend import MatrixOps
```


---

## API Stability

Maintain stable imports despite internal refactoring:

```python
# v1 layout
from .optimizer import SGD, Adam

# v2: internal restructure (users unaffected)
from .optim.sgd import SGD
from .optim.adam import Adam
```

Users always write `from mylib import SGD` — internal changes are hidden.

### Name Conflicts

If you import the same name twice, **last assignment wins**:

```python
from .optimizer import SGD    # First binding
from .optim.sgd import SGD    # Overwrites first
```

To expose both versions, use aliases:

```python
from .optimizer import SGD as SGD_legacy
from .optim.sgd import SGD

__all__ = ['SGD', 'SGD_legacy']
```


---

## Practical Example

A simple package with inheritance:

```
mypackage/
├── __init__.py
├── polygon.py
├── rectangle.py
└── triangle.py
```

```python
# mypackage/polygon.py
class Polygon:
    def set_values(self, width, height):
        self._width = width
        self._height = height

# mypackage/rectangle.py
from .polygon import Polygon

class Rectangle(Polygon):
    def area(self):
        return self._width * self._height

# mypackage/triangle.py
from .polygon import Polygon

class Triangle(Polygon):
    def area(self):
        return self._width * self._height / 2

# mypackage/__init__.py
from .polygon import Polygon
from .rectangle import Rectangle
from .triangle import Triangle
```

Now users have three import options:

```python
# Option 1: Import from submodule
from mypackage.rectangle import Rectangle

# Option 2: Import module with alias
import mypackage.rectangle as r
r.Rectangle()

# Option 3: Import package (uses __init__.py)
import mypackage
mypackage.Rectangle()  # Works because of re-export
```

Without the `__init__.py` re-exports, Option 3 would raise `AttributeError`.


---

## Real-World Example

From scikit-learn's `__init__.py`:

```python
from ._config import get_config, set_config
from .utils import show_versions
from .base import clone

__all__ = [
    "get_config",
    "set_config", 
    "show_versions",
    "clone",
]
```

This allows `from sklearn import clone` while hiding internal structure.


---

## Pitfalls to Avoid

| Pitfall | Why It's Dangerous |
|---------|-------------------|
| Importing everything | Slow import time, high memory |
| Creating global state | Breaks thread safety |
| Overusing wildcards | Namespace pollution |
| Omitting `__all__` | Implicit, uncontrolled API |


---

## Summary

| Responsibility | Description |
|----------------|-------------|
| API Exposure | Re-export internal symbols |
| Import Control | Manage wildcard visibility via `__all__` |
| Initialization | Run package-level setup code |
| Lazy Loading | Defer expensive imports |
| Compatibility | Hide refactoring from users |
