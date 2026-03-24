# Initialization Patterns

When a child class defines its own `__init__`, Python does not automatically call the parent's initializer. If the parent sets up important attributes or performs setup logic, those steps are silently skipped unless the child explicitly invokes them. The `super()` function provides a clean, MRO-aware way to call parent initializers, and using it correctly is essential for both single and multiple inheritance.

## Parent __init__

### 1. Call super()

A child class should call `super().__init__()` to ensure the parent's initialization logic runs. Any arguments the parent expects must be passed through explicitly.

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

Without the `super().__init__(x)` call, `obj.x` would never be set, and accessing it would raise an `AttributeError`.

## Multiple Inheritance

### 1. MRO Order

With multiple inheritance, `super()` follows the Method Resolution Order (MRO). Python uses an algorithm called C3 linearization to determine a consistent order in which classes are visited. Each `super()` call passes control to the next class in the MRO chain, not necessarily the direct parent.

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

The MRO for `C` is `[C, A, B, object]`. When `C.__init__` calls `super().__init__()`, control passes to `A`. When `A` calls `super().__init__()`, control passes to `B` (the next in the MRO), not to `object`. Finally, `B` calls `super().__init__()`, which reaches `object.__init__()` and the chain completes.

## Summary

- Always call `super().__init__()` in a child class to ensure the parent's initialization logic executes.
- The Method Resolution Order (MRO) determines the sequence in which `super()` dispatches calls through the class hierarchy.
- In multiple inheritance, every class in the chain should call `super().__init__()` so that all initializers run in the correct MRO order.
