# Callable and TypeAlias

`Callable` annotates functions or callable objects, while `TypeAlias` creates named type aliases for complex type annotations.

## Callable - Function Type Hints

Use `Callable` to annotate functions and callbacks.

```python
from typing import Callable

# Function that takes a Callable
def apply_operation(a: int, b: int, op: Callable[[int, int], int]) -> int:
    return op(a, b)

# Callable with different signatures
def transform(data: list[str], processor: Callable[[str], int]) -> list[int]:
    return [processor(item) for item in data]

result1 = apply_operation(5, 3, lambda x, y: x + y)
result2 = transform(["hello", "world"], len)

print(result1)
print(result2)
```

```
8
[5, 5]
```

## TypeAlias - Named Type Aliases

Create reusable type definitions with TypeAlias.

```python
from typing import TypeAlias

# Create named aliases for complex types
UserId: TypeAlias = int
UserName: TypeAlias = str
UserData: TypeAlias = dict[UserId, UserName]

def get_user_name(users: UserData, user_id: UserId) -> UserName | None:
    return users.get(user_id)

users: UserData = {1: "Alice", 2: "Bob"}
print(get_user_name(users, 1))
print(get_user_name(users, 99))
```

```
Alice
None
```

