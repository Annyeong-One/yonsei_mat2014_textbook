# Initialization Patterns

## Parent __init__

### 1. Call super()

```python
class Parent:
    def __init__(self, x):
        self.x = x

class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

obj = Child(10, 20)
print(obj.x, obj.y)  # 10 20
```

## Multiple Inheritance

### 1. MRO Order

```python
class A:
    def __init__(self):
        print("A")
        super().__init__()

class B:
    def __init__(self):
        print("B")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("C")
        super().__init__()

obj = C()
# Prints: C, A, B
```

## Summary

- Use super() for parent init
- MRO determines order
- Call super() in each class
