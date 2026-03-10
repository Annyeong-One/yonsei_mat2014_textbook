# pass Statement

The `pass` statement is Python's explicit no-op. It lets you create syntactically valid but intentionally empty code blocks.

## Definition

**`pass`** is a null statement that does nothing when executed. Python requires every block (after `:`) to contain at least one statement; `pass` satisfies this requirement as a placeholder. The **Ellipsis literal** (`...`) serves the same purpose and is conventionally preferred in type stubs and abstract method signatures.

## Explanation

Common uses: (1) **Stub functions/classes** during top-down design -- define the interface first, implement later. (2) **Custom exception classes** that add no behavior beyond their name: `class NotFoundError(Exception): pass`. (3) **Intentionally empty `except` blocks** when an exception is expected and safe to ignore (always catch a specific exception, never bare `except: pass`). (4) **Empty branches** in `if`/`elif`/`else` chains where one case requires no action.

`pass` does not exit the function. Code after `pass` continues to execute, unlike `return None` which exits immediately.

## Examples

```python
# Function and class stubs
def calculate_tax(income):
    pass  # TODO: implement tax logic

class DatabaseConnection:
    pass  # attributes and methods to be added
```

```python
# Custom exception with no extra behavior
class ValidationError(Exception):
    pass

# Intentionally ignoring a specific, expected exception
try:
    os.remove("temp.txt")
except FileNotFoundError:
    pass  # file already gone -- that's fine
```

```python
# pass vs Ellipsis: both are valid placeholders
def method_a():
    pass

def method_b():
    ...

# Ellipsis is conventional in type stubs (.pyi files)
def parse(data: bytes) -> dict[str, int]: ...
```

```python
# pass does NOT exit the function
def demo():
    pass
    print("This still runs")  # prints

demo()  # Output: This still runs
```
