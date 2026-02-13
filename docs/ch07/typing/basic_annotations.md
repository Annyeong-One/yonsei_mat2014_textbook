# Basic Annotations (int, str, list)

Basic type annotations include primitive types and built-in collection types, forming the foundation of type hinting.

## Primitive Type Annotations

Annotate variables with primitive types like int, str, float, and bool.

```python
# Primitive types
name: str = "Alice"
age: int = 30
height: float = 5.8
is_active: bool = True

print(f"{name}, {age}, {height}, {is_active}")
```

```
Alice, 30, 5.8, True
```

## Collection Type Annotations

Annotate collections and specify their element types.

```python
# Collection types (Python 3.9+)
numbers: list[int] = [1, 2, 3]
tags: set[str] = {"python", "typing"}
coords: tuple[float, float] = (10.5, 20.3)

# Dictionaries with key-value types
config: dict[str, int] = {"port": 8080, "timeout": 30}

print(f"Numbers: {numbers}")
print(f"Config: {config}")
```

```
Numbers: [1, 2, 3]
Config: {'port': 8080, 'timeout': 30}
```

## Function Annotations

Annotate function parameters and return types.

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}"

result1 = add(5, 3)
result2 = greet("World")
print(result1, result2)
```

```
8 Hello, World
```

