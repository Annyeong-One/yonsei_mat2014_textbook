# `__name__ == "__main__"`

The `__name__` variable distinguishes between running a file as a script and importing it as a module. The "main guard" pattern prevents code from running on import.

---

## The `__name__` Variable

Every Python module has a `__name__` attribute:

| How Module is Used | Value of `__name__` |
|--------------------|---------------------|
| Run directly (`python script.py`) | `"__main__"` |
| Imported (`import script`) | `"script"` (module name) |

```python
# mymodule.py
print(f"__name__ is: {__name__}")
```

```bash
$ python mymodule.py
__name__ is: __main__
```

```python
>>> import mymodule
__name__ is: mymodule
```

---

## The Main Guard Pattern

```python
def main():
    print("This runs only when executed directly")

if __name__ == "__main__":
    main()
```

### How It Works

- **Run directly**: `__name__` is `"__main__"` → condition is `True` → `main()` executes
- **Imported**: `__name__` is `"mymodule"` → condition is `False` → `main()` doesn't execute

---

## Why It Matters

### Without Main Guard

```python
# greet.py
def greet(name):
    return f"Hello, {name}!"

# This runs on import!
print(greet("World"))
```

```python
>>> import greet
Hello, World!  # Unwanted side effect!
```

### With Main Guard

```python
# greet.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
```

```python
>>> import greet
# Nothing printed — safe import!

>>> greet.greet("Alice")
'Hello, Alice!'
```

---

## Practical Example

```python
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """Demo the calculator functions."""
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")

if __name__ == "__main__":
    main()
```

**As script:**
```bash
$ python calculator.py
2 + 3 = 5
5 - 2 = 3
4 * 3 = 12
10 / 2 = 5.0
```

**As module:**
```python
>>> from calculator import add, multiply
>>> add(10, 20)
30
>>> multiply(5, 6)
30
# No demo output printed
```

---

## Use Cases

### 1. Testing During Development

```python
# utils.py
def process_data(data):
    return [x * 2 for x in data]

if __name__ == "__main__":
    # Quick test
    test_data = [1, 2, 3, 4, 5]
    result = process_data(test_data)
    print(f"Input: {test_data}")
    print(f"Output: {result}")
    assert result == [2, 4, 6, 8, 10], "Test failed!"
    print("All tests passed!")
```

### 2. Command-Line Entry Point

```python
# cli.py
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Your name")
    args = parser.parse_args()
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
```

### 3. Demo / Example Usage

```python
# mylib.py
class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    def transform(self):
        return [x ** 2 for x in self.data]

if __name__ == "__main__":
    # Show how to use the class
    processor = DataProcessor([1, 2, 3, 4, 5])
    print("Squared:", processor.transform())
```

---

## The `__package__` Variable

Related to `__name__`, the `__package__` variable indicates the package context:

| Execution Method | `__name__` | `__package__` |
|------------------|------------|---------------|
| `python script.py` | `"__main__"` | `None` |
| `python -m package.script` | `"__main__"` | `"package"` |
| `import package.script` | `"package.script"` | `"package"` |

This is why relative imports work with `-m` but not direct execution.

---

## Common Patterns

### Pattern 1: Simple Entry Point

```python
if __name__ == "__main__":
    main()
```

### Pattern 2: With Error Handling

```python
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
```

### Pattern 3: With Exit Code

```python
import sys

if __name__ == "__main__":
    sys.exit(main())  # main() returns 0 on success, non-zero on failure
```

### Pattern 4: Async Entry Point

```python
import asyncio

async def main():
    await some_async_operation()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Anti-Patterns to Avoid

### Don't: Execute Code at Module Level

```python
# Bad: runs on import
data = load_expensive_data()  # Always runs!
```

### Do: Defer Execution

```python
# Good: only runs when needed
def get_data():
    return load_expensive_data()

if __name__ == "__main__":
    data = get_data()
```

### Don't: Put Everything in Main Guard

```python
# Bad: can't reuse anything
if __name__ == "__main__":
    def helper():
        pass
    helper()  # Not importable!
```

### Do: Define Functions Outside, Call Inside

```python
# Good: functions are importable
def helper():
    pass

if __name__ == "__main__":
    helper()
```

---

## Key Takeaways

- `__name__` is `"__main__"` when run directly, module name when imported
- The main guard `if __name__ == "__main__":` prevents code from running on import
- Use it for:
  - Entry points
  - Testing
  - Demo code
- Always define functions/classes **outside** the main guard for reusability
- Essential for writing code that works both as script and module
