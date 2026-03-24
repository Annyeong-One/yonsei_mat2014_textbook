# Dynamic vs Static

Programming languages differ fundamentally in when they check types. Statically typed languages like Java and C++ verify types at compile time and require every attribute to be declared before use. Python, by contrast, is dynamically typed: objects can receive new attributes at any point during execution without prior declaration. This flexibility is a core part of Python's design, but it requires discipline to avoid runtime errors from typos or unexpected attribute additions.

## Dynamic Typing

### 1. Python

In a dynamically typed language like Python, you can add attributes to an object at any time. There is no requirement to declare them in the class body or in `__init__` — the interpreter simply creates the attribute when you assign to it.

```python
class Dog:
    pass

# Can add attributes anytime
dog = Dog()
dog.name = "Rex"  # OK
dog.age = 5       # OK
```

## Static Typing

### 1. Other Languages

In statically typed languages, all attributes must be declared in the class definition. The compiler checks every attribute access at compile time and rejects any reference to an undeclared field.

```java
// Java - static
class Dog {
    String name;  // Must declare
}
```

Attempting to assign `dog.age` without declaring `age` in the class would cause a compilation error in Java, whereas Python would silently create the attribute.

## Type Hints

### 1. Optional

Python introduced type hints as an optional middle ground between full dynamic freedom and static enforcement. You can annotate parameter and attribute types for documentation and for use with static analysis tools like mypy, without sacrificing Python's runtime flexibility.

```python
class Dog:
    def __init__(self, name: str):
        self.name: str = name

# Type hints are not enforced at runtime
```

Type hints make code more readable and allow tools to catch type errors before the program runs, but the Python interpreter itself does not enforce them.

## Summary

- Python is dynamically typed, allowing attributes to be added to any object at any time without declaration.
- Statically typed languages require all attributes to be declared in advance and enforce this at compile time.
- Type hints provide an optional way to document expected types and enable static analysis without changing Python's dynamic runtime behavior.
- Dynamic typing offers flexibility but demands careful discipline, since typos in attribute names create new attributes silently rather than raising errors.
