# Practical Type Hint Patterns

Common patterns and best practices for applying type hints effectively in real-world Python code.

## API Response Typing

Type hint API responses and data structures clearly.

```python
from typing import TypeAlias
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str

ApiResponse: TypeAlias = dict[str, User]

def get_users() -> ApiResponse:
    return {
        "1": User(1, "Alice", "alice@example.com"),
        "2": User(2, "Bob", "bob@example.com")
    }

users = get_users()
print(users["1"])
```

```
User(id=1, name='Alice', email='alice@example.com')
```

## Variadic Arguments

Type hint functions with variable arguments.

```python
from typing import overload

@overload
def concat(sep: str) -> Callable[[str, ...], str]: ...

def concat(*items: str) -> str:
    return ",".join(items)

result = concat("apple", "banana", "cherry")
print(result)
```

```
apple,banana,cherry
```

## Decorators with Generics

Type hint decorators using generics.

```python
from typing import Callable, TypeVar, cast

F = TypeVar('F', bound=Callable)

def log_calls(func: F) -> F:
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return cast(F, wrapper)

@log_calls
def greet(name: str) -> str:
    return f"Hello {name}"

print(greet("Alice"))
```

```
Calling greet
Hello Alice
```

