# typing Overview

The `typing` module provides tools for annotating Python code with type hints, improving code clarity and enabling static type checking.

## What is Type Hinting?

Type hints document the expected types of variables and function parameters without enforcing them at runtime.

```python
# Type hints for function parameters and return types
def greet(name: str, age: int) -> str:
    return f"{name} is {age} years old"

result = greet("Alice", 30)
print(result)

# Type hints work with any types
numbers: list[int] = [1, 2, 3]
config: dict[str, str] = {"host": "localhost"}
print(numbers, config)
```

```
Alice is 30 years old
[1, 2, 3] {'host': 'localhost'}
```

## Benefits of Type Hints

Type hints enable better IDE support, catch errors early with tools like mypy, and improve code readability.

```python
from typing import List, Dict

# Clear intent for complex types
def process_users(users: List[Dict[str, str]]) -> int:
    return len(users)

data = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"}
]
print(f"Processed {process_users(data)} users")
```

```
Processed 2 users
```

