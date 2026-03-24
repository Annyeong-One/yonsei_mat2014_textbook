# TYPE_CHECKING and Forward References

As projects grow, type hints sometimes create circular import chains — module A imports a type from module B, which imports a type from module A. Similarly, a class may need to reference itself in its own type annotations before the class definition is complete. Python's `TYPE_CHECKING` constant and forward references (string-quoted type names) solve both problems without sacrificing type safety.

## TYPE_CHECKING for Conditional Imports

The `TYPE_CHECKING` constant from the `typing` module is `False` at runtime but treated as `True` by static type checkers like `mypy`. Wrapping an import in `if TYPE_CHECKING:` means the import only executes during type analysis, breaking the circular dependency at runtime. The type annotation must then use a string (forward reference) so Python does not try to evaluate it.

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

```text
Code runs without importing SomeType at runtime
```

## Forward References with Quotes

A forward reference is a type annotation written as a string literal (e.g., `'Node'`) instead of the bare class name. Python evaluates annotations at class-definition time, so referencing a class that has not yet been fully defined raises a `NameError`. Quoting the name defers evaluation, letting the annotation resolve later.

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

```text
Node1: 1, Node2: 2
```
