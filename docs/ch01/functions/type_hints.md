# Type Hints

Type hints (or type annotations) provide optional static typing information for function parameters and return values. They improve code readability and enable static analysis tools.


## Basic Syntax

```python
def add_this(a: int, b: int) -> int:
    return a + b

result = add_this(2, 3)
print(result)  # 5
```

- `a: int` — parameter `a` should be an `int`
- `b: int` — parameter `b` should be an `int`
- `-> int` — function returns an `int`


## Type Hints Are Not Enforced

Python does **not** enforce type hints at runtime. They are for documentation and static analysis only.

```python
def add_this(a: int, b: int) -> int:
    return a + b

# Works despite wrong types
result = add_this("2", "3")
print(result)  # "23" (string concatenation)
```

The code runs without error, but a type checker like `mypy` would flag this.


## Without Type Hints

```python
def add_this(a, b):
    return a + b

print(add_this(2, 3))      # 5
print(add_this("2", "3"))  # "23"
```

Without hints, readers can't tell what types are expected.


## Common Type Hints

### Basic Types

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def is_adult(age: int) -> bool:
    return age >= 18

def calculate_area(radius: float) -> float:
    return 3.14159 * radius ** 2
```

### None Return

```python
def print_message(msg: str) -> None:
    print(msg)
```

### Optional Parameters

```python
from typing import Optional

def greet(name: str, greeting: Optional[str] = None) -> str:
    if greeting is None:
        greeting = "Hello"
    return f"{greeting}, {name}!"
```

### Collections

```python
from typing import List, Dict, Tuple, Set

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def get_user(users: Dict[str, int]) -> int:
    return users.get("age", 0)

def get_point() -> Tuple[int, int]:
    return (10, 20)

def unique_items(items: Set[str]) -> int:
    return len(items)
```

### Python 3.9+ Simplified Syntax

```python
# Python 3.9+
def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)

def get_ages(users: dict[str, int]) -> list[int]:
    return list(users.values())
```


## Function Type Hints

```python
from typing import Callable

def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

def double(x: int) -> int:
    return x * 2

result = apply_twice(double, 5)  # 20
```


## Type Checking with mypy

Install and run mypy to check types:

```bash
pip install mypy
mypy script.py
```

Example error:

```python
def add(a: int, b: int) -> int:
    return a + b

add("hello", "world")  # mypy error: Argument 1 has incompatible type "str"
```


## Benefits of Type Hints

1. **Documentation** — Clear function signatures
2. **IDE Support** — Better autocomplete and error detection
3. **Static Analysis** — Catch bugs before runtime
4. **Refactoring** — Safer code changes
5. **Team Communication** — Explicit contracts


## When to Use Type Hints

**Use type hints for:**
- Public APIs and library functions
- Complex functions with multiple parameters
- Functions where types aren't obvious
- Team projects and production code

**Optional for:**
- Simple scripts
- Obvious functions like `def add(a, b): return a + b`
- Rapid prototyping


## Summary

- Type hints use `: type` for parameters and `-> type` for returns
- Python does **not enforce** type hints at runtime
- Use `mypy` or similar tools for static checking
- Import from `typing` module for complex types
- Python 3.9+ allows `list[int]` instead of `List[int]`
