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

---

## Exercises

**Exercise 1.**
Create a class `Point` without type hints. Show that you can add arbitrary attributes (like `color`, `label`) at runtime. Then create a `TypedPoint` with type hints and `__slots__`. Show the difference: `TypedPoint` prevents dynamic attribute addition while `Point` allows it.

??? success "Solution to Exercise 1"

        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        p = Point(1, 2)
        p.color = "red"   # Dynamic — works fine
        p.label = "A"     # Also fine
        print(vars(p))    # {'x': 1, 'y': 2, 'color': 'red', 'label': 'A'}

        class TypedPoint:
            __slots__ = ('x', 'y')

            def __init__(self, x: float, y: float):
                self.x = x
                self.y = y

        tp = TypedPoint(1, 2)
        try:
            tp.color = "red"
        except AttributeError as e:
            print(f"Error: {e}")
            # Error: 'TypedPoint' object has no attribute 'color'

---

**Exercise 2.**
Write a function that takes an object and a list of expected attribute names. It should check whether the object has all expected attributes using `hasattr()` and return a report dictionary mapping each name to `True`/`False`. Demonstrate with a duck-typing scenario where two different classes satisfy the same interface check.

??? success "Solution to Exercise 2"

        def check_interface(obj, expected):
            return {name: hasattr(obj, name) for name in expected}

        class Duck:
            def quack(self):
                return "Quack!"
            def swim(self):
                return "Swimming"

        class Person:
            def quack(self):
                return "I'm quacking!"
            def swim(self):
                return "I'm swimming!"

        expected = ["quack", "swim", "fly"]
        print(check_interface(Duck(), expected))
        # {'quack': True, 'swim': True, 'fly': False}
        print(check_interface(Person(), expected))
        # {'quack': True, 'swim': True, 'fly': False}

---

**Exercise 3.**
Demonstrate the "typo bug" problem in dynamic typing: create a class `Account` with a `balance` attribute. Accidentally write `self.balence = 100` (typo). Show that Python silently creates a new attribute. Then show how `__slots__` prevents this problem by raising `AttributeError` on the typo.

??? success "Solution to Exercise 3"

        # Dynamic typing — typo creates silent bug
        class Account:
            def __init__(self, balance):
                self.balance = balance

        acc = Account(1000)
        acc.balence = 500  # Typo! Creates new attribute silently
        print(acc.balance)   # 1000 — original unchanged
        print(acc.balence)   # 500 — typo attribute

        # Slots prevent this
        class SafeAccount:
            __slots__ = ('balance',)

            def __init__(self, balance):
                self.balance = balance

        safe = SafeAccount(1000)
        try:
            safe.balence = 500  # Typo caught!
        except AttributeError as e:
            print(f"Caught typo: {e}")
