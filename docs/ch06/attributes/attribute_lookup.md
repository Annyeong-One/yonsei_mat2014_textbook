# Attribute Lookup


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Lookup Order

### 1. Instance → Class → Parent

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

## __dict__

### 1. Instance Dict

```python
class MyClass:
    def __init__(self, x):
        self.x = x

obj = MyClass(10)
print(obj.__dict__)  # {'x': 10}
```

### 2. Class Dict

```python
print(MyClass.__dict__)
# Contains methods and class attributes
```

## Summary

- Search: instance → class → parents
- __dict__ stores attributes
- Dynamic lookup
