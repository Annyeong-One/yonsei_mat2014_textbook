# List[int] vs list[int] - Generic Types

Generic types can be specified using either typing module classes (List[int]) or built-in types (list[int], available in Python 3.9+).

## Legacy Typing Module Syntax

Before Python 3.9, use types from the typing module for generic annotations.

```python
from typing import List, Dict, Set, Tuple

# Pre-3.9 style using typing module
numbers: List[int] = [1, 2, 3]
mapping: Dict[str, int] = {"a": 1, "b": 2}
unique: Set[str] = {"x", "y", "z"}
pair: Tuple[int, str] = (1, "one")

print(numbers, mapping, unique, pair)
```

```
[1, 2, 3] {'a': 1, 'b': 2} {'x', 'y', 'z'} (1, 'one')
```

## Modern Built-in Syntax (Python 3.9+)

Starting with Python 3.9, use built-in types directly for generics.

```python
# Python 3.9+ style using built-in types
numbers: list[int] = [1, 2, 3]
mapping: dict[str, int] = {"a": 1, "b": 2}
unique: set[str] = {"x", "y", "z"}
pair: tuple[int, str] = (1, "one")

print(numbers, mapping, unique, pair)
```

```
[1, 2, 3] {'a': 1, 'b': 2} {'x', 'y', 'z'} (1, 'one')
```

## When to Use Each Style

Choose based on your Python version and codebase consistency.

```python
# New code with Python 3.9+: prefer built-in syntax
def process(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

result = process(["cat", "elephant", "dog"])
print(result)

# Use typing module for complex types
from typing import Callable
callback: Callable[[int], str] = str
print(callback(42))
```

```
{'cat': 3, 'elephant': 8, 'dog': 3}
42
```

