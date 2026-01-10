# Import Mechanics

Python’s `import` system allows code to be organized into reusable **modules**. Understanding how imports work is essential for structuring larger projects.

---

## Basic import forms

```python
import math
import math as m
from math import sqrt
from math import sqrt as s
```

Each form binds names differently in the current namespace.

---

## What happens during

When Python executes `import module`:
1. It searches for the module.
2. It executes the module’s top-level code.
3. It creates a module object.
4. It binds the module name.

Imports are cached in `sys.modules`.

---

## Import is executed

A module is initialized only once per session:

```python
import mymodule
import mymodule   # no re-execution
```

This avoids duplicate side effects.

---

## Key takeaways

- Imports bind names, not copies of code.
- Module code runs at first import.
- Imports are cached.
