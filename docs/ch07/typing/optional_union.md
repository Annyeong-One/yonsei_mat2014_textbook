# Optional and Union


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

`Optional` represents values that can be None, while `Union` represents a value that can be one of several types.

## Optional - Nullable Types

Use `Optional[T]` when a value can be of type T or None.

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

print(find_user(1))  # Alice
print(find_user(99))  # None
```

```
Alice
None
```

## Union - Multiple Possible Types

Use `Union[T1, T2]` when a value can be one of several types.

```python
from typing import Union

def process_id(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Integer ID: {value}"
    else:
        return f"String ID: {value}"

print(process_id(123))
print(process_id("ABC"))
```

```
Integer ID: 123
String ID: ABC
```

## Modern Syntax with |

Python 3.10+ allows using | instead of Union.

```python
# Python 3.10+ syntax
def process_data(value: int | str) -> str:
    return f"Got: {value}"

# Optional is equivalent to T | None
def find_item(item_id: int) -> str | None:
    items = {1: "Item A"}
    return items.get(item_id)

print(process_data(42))
print(find_item(1))
print(find_item(99))
```

```
Got: 42
Item A
None
```

