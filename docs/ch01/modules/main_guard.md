
# __name__ == "__main__"

Python modules can be executed in two different ways:

1. run directly as a script
2. imported as a module

The variable `__name__` helps distinguish these cases.

```mermaid
flowchart TD
    A[Python file]
    A --> B{run directly?}
    B -->|yes| C[__name__ = "__main__"]
    B -->|no| D[__name__ = module name]
````

---

## 1. The **name** Variable

Every Python module has a special variable called `__name__`.

When a file is run directly:

```python
print(__name__)
```

Output:

```text
__main__
```

When the file is imported, `__name__` becomes the module name.

---

## 2. The Main Guard Pattern

The most common pattern is:

```python
if __name__ == "__main__":
    main()
```

Example:

```python
def main():
    print("Running program")

if __name__ == "__main__":
    main()
```

---

## 3. Why This Is Useful

The main guard prevents code from running during import.

Example:

```python
# tools.py

print("module loaded")
```

If imported, the print statement runs immediately.

The main guard avoids this problem.

---

## 4. Typical Program Structure

```python
def main():
    print("program logic")

if __name__ == "__main__":
    main()
```

This pattern separates:

* reusable code
* script execution

---

## 5. Example

File `math_tools.py`

```python
def square(x):
    return x * x

def main():
    print(square(5))

if __name__ == "__main__":
    main()
```

Running the file:

```text
25
```

Importing it:

```python
import math_tools
```

No output occurs.

---

## 6. Summary

Key ideas:

* `__name__` identifies how a module is executed
* `__name__ == "__main__"` is true when a file runs directly
* the main guard prevents unintended execution during import
* this pattern is common in Python programs

The main guard makes modules reusable while still allowing standalone execution.