# Version Check

## Check Version

### 1. Using __version__

Check the installed NumPy version.

```python
import numpy as np

def main():
    print(f"NumPy version: {np.__version__}")

if __name__ == "__main__":
    main()
```

**Output:**

```
NumPy version: 1.26.0
```

### 2. Command Line

Check version from terminal.

```bash
python -c "import numpy; print(numpy.__version__)"
```

Or using pip:

```bash
pip show numpy
```

### 3. Detailed Info

Get comprehensive build information.

```python
import numpy as np

def main():
    print(np.show_config())

if __name__ == "__main__":
    main()
```

## Verify Install

### 1. Basic Test

Verify NumPy works correctly.

```python
import numpy as np

def main():
    # Create array
    a = np.array([1, 2, 3, 4, 5])
    
    # Basic operations
    print(f"Array: {a}")
    print(f"Sum: {a.sum()}")
    print(f"Mean: {a.mean()}")
    
    print("NumPy is working!")

if __name__ == "__main__":
    main()
```

### 2. Matrix Operations

Test linear algebra functionality.

```python
import numpy as np

def main():
    A = np.array([[1, 2], [3, 4]])
    b = np.array([5, 6])
    
    # Matrix multiplication
    result = A @ b
    print(f"Matrix multiply: {result}")
    
    # Determinant
    det = np.linalg.det(A)
    print(f"Determinant: {det}")
    
    print("Linear algebra working!")

if __name__ == "__main__":
    main()
```

### 3. Random Generation

Test random number generation.

```python
import numpy as np

def main():
    np.random.seed(42)
    
    samples = np.random.randn(5)
    print(f"Random samples: {samples}")
    
    print("Random generation working!")

if __name__ == "__main__":
    main()
```

## Troubleshooting

### 1. Import Error

If NumPy is not found:

```bash
# Check if installed
pip list | grep numpy

# Reinstall if needed
pip uninstall numpy
pip install numpy
```

### 2. Version Mismatch

If you need a different version:

```python
import numpy as np

def main():
    required = "1.24.0"
    installed = np.__version__
    
    print(f"Required: {required}")
    print(f"Installed: {installed}")
    
    # Compare versions
    from packaging import version
    if version.parse(installed) < version.parse(required):
        print("Upgrade needed!")

if __name__ == "__main__":
    main()
```

### 3. Multiple Pythons

Ensure correct Python environment:

```bash
# Check which Python
which python

# Check which pip
which pip

# They should match
python -c "import sys; print(sys.executable)"
```


---

## Exercises

**Exercise 1.** Write a script that prints the NumPy version and checks if it is at least version 1.20. Print a warning if the version is older.

??? success "Solution to Exercise 1"
    ```python
    import numpy as np

    version = np.__version__
    print(f"NumPy version: {version}")

    major, minor = [int(x) for x in version.split(".")[:2]]
    if (major, minor) < (1, 20):
        print("Warning: NumPy 1.20+ recommended")
    else:
        print("Version OK")
    ```

---

**Exercise 2.** Use `np.show_config()` to display the build configuration. What information does this provide?

??? success "Solution to Exercise 2"
    ```python
    import numpy as np
    np.show_config()
    ```

    This shows build details including the BLAS/LAPACK libraries used, compiler information, and optimization flags. It helps diagnose performance issues or verify that optimized linear algebra libraries are linked.

---

**Exercise 3.** Write a function `check_numpy_version(min_version: str) -> bool` that parses version strings and returns `True` if the installed version meets the requirement.

??? success "Solution to Exercise 3"
    ```python
    import numpy as np

    def check_numpy_version(min_version: str) -> bool:
        installed = tuple(int(x) for x in np.__version__.split(".")[:3])
        required = tuple(int(x) for x in min_version.split("."))
        return installed >= required

    print(check_numpy_version("1.20.0"))  # True or False
    ```

---

**Exercise 4.** Explain why checking the NumPy version matters when writing code that uses newer features like `np.random.default_rng()`.

??? success "Solution to Exercise 4"
    `np.random.default_rng()` was introduced in NumPy 1.17. Code using newer APIs will fail with `AttributeError` on older versions. Checking the version at startup lets you provide helpful error messages or fall back to older APIs.
