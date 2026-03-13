# TYPE_CHECKING and Forward References

`TYPE_CHECKING` allows including type hints only during static analysis, while forward references handle circular imports.

## TYPE_CHECKING for Conditional Imports

Use TYPE_CHECKING to avoid circular imports and runtime overhead.

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # These imports only happen during type checking
    from some_module import SomeType

def process(value: 'SomeType') -> str:
    # Quotes make it a forward reference
    return str(value)

print("Code runs without importing SomeType at runtime")
```

```
Code runs without importing SomeType at runtime
```

## Forward References with Quotes

Use string quotes for forward references before a class is defined.

```python
from typing import Optional

class Node:
    def __init__(self, value: int, next: Optional['Node'] = None):
        self.value = value
        self.next = next

# Create linked list
node1 = Node(1)
node2 = Node(2)
node1.next = node2

print(f"Node1: {node1.value}, Node2: {node1.next.value}")
```

```
Node1: 1, Node2: 2
```

