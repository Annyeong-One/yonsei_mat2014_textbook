# Attribute Lookup

When you access an attribute on a Python object, the interpreter does not simply retrieve a stored value. Instead, it follows a well-defined search chain that moves from the instance to its class and then up through the class hierarchy. Understanding this lookup mechanism is essential for working with inheritance, class design, and advanced features like descriptors.

## Lookup Order

### 1. Instance, Class, Parent

When you write `obj.attr`, Python searches in a specific order: it checks the instance's own namespace first, then the class that created the instance, and finally any parent classes following the method resolution order (MRO). The first match wins.

```python
class Parent:
    x = "parent"

class Child(Parent):
    y = "child"

obj = Child()
obj.z = "instance"

print(obj.z)  # instance (found in instance)
print(obj.y)  # child (found in class)
print(obj.x)  # parent (found in parent)
```

In this example, `obj.z` is found directly on the instance. The name `obj.y` is not on the instance, so Python checks `Child` and finds it there. Finally, `obj.x` is not on the instance or on `Child`, so Python continues up to `Parent` where it finds the match.

## The __dict__ Dictionary

Every object and class in Python maintains a `__dict__` dictionary that stores its attributes. This dictionary is the underlying data structure that powers the attribute lookup chain described above.

### 1. Instance Dict

Attributes set through `self.x = value` inside a method (or directly on the instance) are stored in the instance's `__dict__`. This is the first place Python looks during attribute resolution.

```python
class MyClass:
    def __init__(self, x):
        self.x = x

obj = MyClass(10)
print(obj.__dict__)  # {'x': 10}
```

### 2. Class Dict

Class-level attributes, methods, and other definitions live in the class's `__dict__`. Python searches here after checking the instance namespace.

```python
print(MyClass.__dict__)
# Contains methods and class attributes
```

## Summary

- Python resolves attribute access by searching the instance namespace first, then the class, and finally parent classes in MRO order.
- The `__dict__` dictionary on each object and class is the storage mechanism behind this lookup chain.
- This dynamic lookup process runs every time you access an attribute, which gives Python its flexibility for runtime modifications.
