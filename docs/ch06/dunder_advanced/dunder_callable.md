# Callable Objects

In Python, any object with a `__call__` method is considered callable — you can invoke it with parentheses just like a function. This is a powerful pattern because, unlike plain functions, callable objects can carry state between invocations. Whenever you need a function that remembers configuration or accumulates results, a callable object is a natural fit.

## Making Objects Callable

### 1. The __call__ Method

When you define `__call__` on a class, instances of that class become callable. Writing `obj(args)` is translated by Python into `obj.__call__(args)`. This means the instance behaves like a function while retaining all the benefits of being an object, including mutable internal state and inheritance.

### 2. Use Cases

Callable objects are useful in several common scenarios:

- **Function-like objects**: create reusable operations that carry configuration state, such as a multiplier with a fixed factor.
- **Decorators**: implement decorators as classes when you need to maintain state across decorated function calls.
- **State machines**: encode transitions and current state inside the object, and trigger transitions by calling it.

### 3. Example

The following class creates a callable that multiplies its argument by a fixed factor set at initialization.

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
print(double(5))   # 10
print(double(12))  # 24
```

The `double` object carries the factor `2` as internal state. Each call to `double(x)` multiplies `x` by that stored factor, producing the same behavior as a function but with the flexibility to change the factor or add methods later.

## Summary

- Defining `__call__` on a class makes its instances callable with the same syntax as a regular function.
- Callable objects combine the convenience of function call syntax with the ability to store and update internal state.
- Common applications include configurable operations, stateful decorators, and state machines.
