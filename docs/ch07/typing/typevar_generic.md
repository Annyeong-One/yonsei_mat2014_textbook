# TypeVar and Generic

`TypeVar` defines type variables for generic functions and classes, allowing flexible yet type-safe code.

## TypeVar - Generic Type Variables

Use TypeVar to write generic functions that work with any type.

```python
from typing import TypeVar

T = TypeVar('T')

def first(items: list[T]) -> T:
    return items[0]

def last(items: list[T]) -> T:
    return items[-1]

nums = [1, 2, 3]
strs = ['a', 'b', 'c']

print(first(nums))  # int
print(last(strs))   # str
```

```
1
c
```

## Constrained TypeVar

Restrict TypeVar to specific types.

```python
from typing import TypeVar

# Only int or str
T = TypeVar('T', int, str)

def process(value: T) -> T:
    if isinstance(value, int):
        return value * 2  # type: ignore
    else:
        return value.upper()  # type: ignore

print(process(5))
print(process("hello"))
```

```
10
HELLO
```

## Generic Classes

Create generic classes with type parameters.

```python
from typing import Generic, TypeVar

T = TypeVar('T')

class Container(Generic[T]):
    def __init__(self, item: T):
        self.item = item
    
    def get(self) -> T:
        return self.item

int_container = Container[int](42)
str_container = Container[str]("hello")

print(int_container.get())
print(str_container.get())
```

```
42
hello
```

