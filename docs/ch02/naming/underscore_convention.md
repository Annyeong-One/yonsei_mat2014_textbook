# Underscore Convention


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Single Leading

### 1. Throwaway Variable

```python
# Loop without using variable
for _ in range(5):
    print("Hello")

# Unpacking ignored values
_, status_code, _ = ("HTTP", 200, "OK")

# With star
first, *_, last = range(10)
```

### 2. Weak Private

Suggests internal use:

```python
# Module-level
_internal_cache = {}
_helper = lambda x: x * 2

# Class attribute  
class MyClass:
    def __init__(self):
        self._internal = 42
```

## Double Leading

### 1. Name Mangling

Triggers name mangling in classes:

```python
class MyClass:
    def __init__(self):
        self.__private = 42  # Mangled

obj = MyClass()
# obj.__private  # AttributeError
print(obj._MyClass__private)  # 42
```

### 2. Prevents Override

```python
class Base:
    def __init__(self):
        self.__setup()  # Calls Base.__setup
    
    def __setup(self):
        print("Base setup")

class Derived(Base):
    def __setup(self):  # Different method
        print("Derived setup")

obj = Derived()  # Prints: Base setup
```

## Dunder Methods

### 1. Magic Methods

Double leading AND trailing:

```python
class MyClass:
    def __init__(self):
        pass
    
    def __str__(self):
        return "MyClass instance"
    
    def __len__(self):
        return 42
```

### 2. Don't Create Own

```python
# Don't do this!
# def __my_method__(self):
#     pass

# Reserved for Python
```

## Trailing Underscore

### 1. Avoid Keywords

```python
# Avoid keyword collision
class_ = "MyClass"
type_ = "custom"
from_ = "source"

def process(type_=None):
    if type_ is None:
        type_ = "default"
    return type_
```

## Summary Table

| Pattern | Use Case | Example |
|---------|----------|---------|
| `_var` | Internal/throwaway | `_cache`, `_` |
| `__var` | Strong private | `__password` |
| `__method__` | Magic | `__init__` |
| `var_` | Avoid keyword | `class_` |
