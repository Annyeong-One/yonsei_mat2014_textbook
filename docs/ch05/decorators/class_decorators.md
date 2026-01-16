# Class Decorators

Decorators can be applied to classes, and classes can be used as decorators.

## Decorating Classes

A class decorator receives a class and returns a modified class.

### Adding Methods

```python
def add_repr(cls):
    """Add a __repr__ method to a class."""
    def __repr__(self):
        attrs = ', '.join(f'{k}={v!r}' for k, v in vars(self).items())
        return f"{cls.__name__}({attrs})"
    cls.__repr__ = __repr__
    return cls

@add_repr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p)  # Point(x=3, y=4)
```

### Adding Class Attributes

```python
def singleton(cls):
    """Make a class a singleton."""
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Connecting to database...")

db1 = Database()  # Prints message
db2 = Database()  # No message (same instance)
print(db1 is db2)  # True
```

### Registering Classes

```python
registry = {}

def register(cls):
    """Register a class in the global registry."""
    registry[cls.__name__] = cls
    return cls

@register
class Handler:
    pass

@register
class Processor:
    pass

print(registry)  # {'Handler': <class 'Handler'>, 'Processor': <class 'Processor'>}
```

---

## Classes as Decorators

A class can act as a decorator by implementing `__init__` and `__call__`.

### Basic Pattern

```python
class CountCalls:
    """Decorator class that counts function calls."""
    
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Call 1 of greet, Hello, Alice!
greet("Bob")    # Call 2 of greet, Hello, Bob!
print(greet.count)  # 2
```

### With Parameters (Factory Pattern)

```python
class Repeat:
    """Decorator class with parameters."""
    
    def __init__(self, times):
        self.times = times
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                result = func(*args, **kwargs)
            return result
        return wrapper

@Repeat(3)
def say_hello():
    print("Hello!")

say_hello()  # Prints "Hello!" 3 times
```

### Stateful Decorator Class

```python
class Memoize:
    """Caching decorator implemented as a class."""
    
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]
    
    def clear_cache(self):
        self.cache.clear()

@Memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))  # Fast due to caching
print(fibonacci.cache)  # View cached values
fibonacci.clear_cache()  # Clear the cache
```

---

## Preserving Method Behavior

When decorating methods, use `__get__` to handle the descriptor protocol:

```python
from functools import wraps

class Logger:
    """Decorator that works with both functions and methods."""
    
    def __init__(self, func):
        self.func = func
        wraps(func)(self)
    
    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__}")
        return self.func(*args, **kwargs)
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        # Return a bound method
        from functools import partial
        return partial(self.__call__, obj)

class MyClass:
    @Logger
    def method(self, x):
        return x * 2

obj = MyClass()
print(obj.method(5))  # Works correctly with self
```

---

## Comparison: Function vs Class Decorators

| Aspect | Function Decorator | Class Decorator |
|--------|-------------------|-----------------|
| State | Closure variables | Instance attributes |
| Methods | Not applicable | Can add helper methods |
| Readability | Simpler for basic cases | Better for complex state |
| Instance check | Not applicable | `isinstance(decorated, DecoratorClass)` |

### When to Use Class Decorators

- Need complex state management
- Want to expose additional methods
- Need to work with the descriptor protocol
- Want cleaner organization for complex decorators

### When to Use Function Decorators

- Simple transformations
- No complex state needed
- Prefer functional style
- Need to work with `functools.wraps` easily

---

## Practical Examples

### Timing Decorator Class

```python
import time

class Timer:
    """Time function execution with statistics."""
    
    def __init__(self, func):
        self.func = func
        self.times = []
    
    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        self.times.append(elapsed)
        return result
    
    @property
    def average_time(self):
        return sum(self.times) / len(self.times) if self.times else 0
    
    @property
    def total_time(self):
        return sum(self.times)

@Timer
def slow_function():
    time.sleep(0.1)

for _ in range(5):
    slow_function()

print(f"Average: {slow_function.average_time:.3f}s")
print(f"Total: {slow_function.total_time:.3f}s")
```

### Validation Decorator Class

```python
class ValidateArgs:
    """Validate function arguments against type specifications."""
    
    def __init__(self, **type_specs):
        self.type_specs = type_specs
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # Validate keyword arguments
            for name, expected_type in self.type_specs.items():
                if name in kwargs:
                    if not isinstance(kwargs[name], expected_type):
                        raise TypeError(
                            f"{name} must be {expected_type.__name__}"
                        )
            return func(*args, **kwargs)
        return wrapper

@ValidateArgs(name=str, age=int)
def create_user(name, age):
    return {'name': name, 'age': age}

create_user(name="Alice", age=30)  # Works
create_user(name="Bob", age="30")  # TypeError
```

---

## Summary

| Pattern | Description |
|---------|-------------|
| Class decorator | Decorator applied to a class |
| Decorator class | Class that acts as a decorator |
| `__init__` | Receives the function/parameters |
| `__call__` | Called when decorated function is invoked |
| `__get__` | For method decoration (descriptor protocol) |

**Key Points**:
- Class decorators modify or enhance classes
- Decorator classes provide stateful decorators
- Use `__get__` for method compatibility
- Choose based on complexity and state requirements
