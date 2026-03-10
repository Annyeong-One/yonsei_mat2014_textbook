# Classes and Instances


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Classes

### 1. Definition

```python
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name):
        # Instance attribute
        self.name = name
    
    def bark(self):
        return f"{self.name} says woof!"
```

## Instances

### 1. Creating

```python
dog1 = Dog("Rex")
dog2 = Dog("Max")

print(dog1.name)   # Rex
print(dog2.name)   # Max
```

### 2. Independent

```python
print(dog1.bark())  # Rex says woof!
print(dog2.bark())  # Max says woof!

# Different objects
print(dog1 is dog2)  # False
```

## Class vs Instance

### 1. Attributes

```python
class MyClass:
    class_var = "shared"
    
    def __init__(self):
        self.instance_var = "unique"

obj1 = MyClass()
obj2 = MyClass()

print(obj1.class_var)      # shared
print(obj1.instance_var)   # unique
```

## Summary

- Class: blueprint
- Instance: object from class
- self refers to instance
- Each instance independent
