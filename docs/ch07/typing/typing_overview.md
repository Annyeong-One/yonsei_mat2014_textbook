# typing Overview

Python is dynamically typed — variables can hold any type, and type errors only surface at runtime. As codebases grow, this flexibility becomes a liability: a function may receive an unexpected type and fail deep in its execution. The `typing` module lets you declare expected types so that tools like `mypy` can catch mismatches before the code runs, while Python itself remains dynamically typed.

## What is Type Hinting?

Type hints annotate the expected types of variables, function parameters, and return values. Python does not enforce these annotations at runtime — passing the wrong type will not raise a `TypeError` from the hint itself. Instead, type hints serve as machine-readable documentation that static analysis tools can verify.

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

```text
Alice is 30 years old
[1, 2, 3] {'host': 'localhost'}
```

## Benefits of Type Hints

Beyond documentation, type hints unlock three practical benefits. First, IDEs like VS Code and PyCharm use them for autocomplete and inline error detection. Second, static checkers like `mypy` can flag type mismatches before you run the code. Third, type-annotated code is easier for collaborators to read, since the function signature alone reveals the expected data shapes.

```python
# Clear intent for complex types using built-in generics (Python 3.9+)
def process_users(users: list[dict[str, str]]) -> int:
    return len(users)

data = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"}
]
print(f"Processed {process_users(data)} users")
```

```text
Processed 2 users
```
