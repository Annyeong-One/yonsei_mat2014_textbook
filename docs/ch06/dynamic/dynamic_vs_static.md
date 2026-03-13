# Dynamic vs Static

## Dynamic Typing

### 1. Python

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

```java
// Java - static
class Dog {
    String name;  // Must declare
}
```

## Type Hints

### 1. Optional

```python
class Dog:
    def __init__(self, name: str):
        self.name: str = name

# Type hints don't enforce
```

## Summary

- Python: dynamic
- Add attributes anytime
- Type hints optional
- Flexible but risky
