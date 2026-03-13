# TypeGuard and Type Narrowing

`TypeGuard` helps type checkers narrow down types within function bodies, improving type safety.

## Type Narrowing with Isinstance

Use isinstance to narrow types within conditional blocks.

```python
from typing import Union

def process_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        # Type checker knows value is int here
        return f"Integer: {value * 2}"
    else:
        # Type checker knows value is str here
        return f"String: {value.upper()}"

print(process_value(5))
print(process_value("hello"))
```

```
Integer: 10
String: HELLO
```

## TypeGuard for Custom Type Checks

Create custom type guards for more complex type narrowing.

```python
from typing import TypeGuard

def is_list_of_ints(value: list) -> TypeGuard[list[int]]:
    return all(isinstance(item, int) for item in value)

def process_numbers(value: list) -> int:
    if is_list_of_ints(value):
        # Type checker narrows to list[int]
        return sum(value)
    else:
        return 0

print(process_numbers([1, 2, 3]))
print(process_numbers([1, "two", 3]))
```

```
6
0
```

