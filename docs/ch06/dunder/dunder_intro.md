# Introduction to Dunder

Python uses a special set of methods as hooks that let user-defined classes integrate seamlessly with built-in syntax. When you write `a + b`, Python calls `a.__add__(b)` behind the scenes. When you call `len(obj)`, Python calls `obj.__len__()`. These hooks are called dunder methods, and understanding them is key to writing classes that feel natural and Pythonic.

## What Are Dunder Methods?

### 1. Definition

Dunder methods — short for "double underscore" methods — are special methods whose names begin and end with two underscores, like `__init__` or `__add__`. They are sometimes called "magic methods" because Python calls them implicitly in response to operations like addition, comparison, or string conversion. You rarely call them directly; instead, you define them in your class and let Python invoke them at the right moment.

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

Dunder methods fall into several functional categories. The following sections provide an overview of the most commonly used groups.

### 1. Initialization

These methods control how instances are created, initialized, and destroyed.

- `__init__`: Initializer — sets up the instance's initial state after creation
- `__new__`: Instance creation — constructs and returns the new instance
- `__del__`: Finalizer — called when the instance is about to be garbage-collected

### 2. Representation

These methods control how an object is converted to a string for display or debugging.

- `__str__`: User-friendly string returned by `str()` and `print()`
- `__repr__`: Developer-friendly representation returned by `repr()` and the interactive console
- `__format__`: Custom formatting used by `format()` and f-strings

### 3. Operators

These methods let your class support built-in operators and container protocols.

- `__add__`, `__sub__`, `__mul__`, `__truediv__`: arithmetic operators
- `__eq__`, `__lt__`, `__gt__`: comparison operators
- `__len__`, `__getitem__`, `__setitem__`: container and indexing operations

## Summary

- Dunder methods are the mechanism Python uses to connect user-defined classes with built-in syntax and operations.
- You define them in your class, and Python calls them automatically when the corresponding operator or function is used.
- The most commonly overridden dunder methods cover initialization, string representation, arithmetic operators, and container behavior.
