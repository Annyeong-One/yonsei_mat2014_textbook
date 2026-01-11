# Introduction to Dunder

## What Are Dunder Methods?

### 1. Definition
Dunder methods (double underscore methods) are special methods in Python that enable operator overloading and customize object behavior. Also called "magic methods."

### 2. Naming Convention
- Start and end with double underscores: `__method__`
- Examples: `__init__`, `__str__`, `__add__`, `__len__`

### 3. Purpose
Enable objects to interact with Python's built-in operations:
- Arithmetic: `+`, `-`, `*`, `/`
- Comparisons: `==`, `<`, `>`
- Container operations: `len()`, `[]`, `in`
- String representations: `str()`, `repr()`

## Common Categories

### 1. Initialization
- `__init__`: Constructor
- `__new__`: Instance creation
- `__del__`: Destructor

### 2. Representation
- `__str__`: User-friendly string
- `__repr__`: Developer-friendly representation
- `__format__`: Format specification

### 3. Operators
- `__add__`, `__sub__`, `__mul__`, `__truediv__`
- `__eq__`, `__lt__`, `__gt__`
- `__len__`, `__getitem__`, `__setitem__`
