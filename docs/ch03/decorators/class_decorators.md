# Class Decorators

## Decorating Classes

### 1. Class Decorator

```python
def add_repr(cls):
    def __repr__(self):
        return f"{cls.__name__}()"
    cls.__repr__ = __repr__
    return cls

@add_repr
class MyClass:
    pass

obj = MyClass()
print(obj)  # MyClass()
```

## Class as Decorator

### 1. Callable Class

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def greet():
    print("Hello")

greet()  # Call 1, Hello
greet()  # Call 2, Hello
```

## Summary

- Can decorate classes
- Classes can be decorators
- Use __call__ for callable
- Flexible pattern
