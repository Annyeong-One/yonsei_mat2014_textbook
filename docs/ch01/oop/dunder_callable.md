# Callable Objects

The `__call__` method makes instances behave like functions, enabling stateful callables and function-like objects.

---

## Making Objects Callable

### 1. `__call__` Method

```python
class Adder:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, x):
        return self.n + x

add10 = Adder(10)
print(add10(5))  # 15
```

### 2. Function-Like Syntax

```python
# Instance behaves like a function
result = add10(5)  # Calls add10.__call__(5)
```

### 3. Stateful Functions

Objects can maintain state between calls.

---

## Why Callable Objects

### 1. State + Behavior

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        return self.count

c = Counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

### 2. vs Regular Functions

```python
# Function: no state
def counter():
    return 1  # Always 1

# Callable object: has state
c = Counter()
c()  # Remembers previous calls
```

### 3. Extensibility

```python
class SmartCounter(Counter):
    def reset(self):
        self.count = 0
    
    def get_count(self):
        return self.count
```

---

## Comparison to Closures

### 1. Closure Version

```python
def make_adder(n):
    def add(x):
        return n + x
    return add

add10 = make_adder(10)
print(add10(5))  # 15
```

### 2. Class Version

```python
class Adder:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, x):
        return self.n + x

add10 = Adder(10)
print(add10(5))  # 15
```

### 3. When to Use Classes

- Need inheritance
- Want multiple methods
- State is complex
- Need introspection

---

## Stateful Multiplier

### 1. Track Usage

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        self.count = 0
    
    def __call__(self, x):
        self.count += 1
        return self.factor * x
    
    def get_stats(self):
        return f"Used {self.count} times"

m = Multiplier(3)
print(m(10))  # 30
print(m(5))   # 15
print(m.get_stats())  # Used 2 times
```

### 2. Mutable State

```python
class Accumulator:
    def __init__(self):
        self.total = 0
    
    def __call__(self, value):
        self.total += value
        return self.total

acc = Accumulator()
print(acc(5))   # 5
print(acc(10))  # 15
print(acc(3))   # 18
```

### 3. Configuration

```python
class Formatter:
    def __init__(self, prefix="", suffix=""):
        self.prefix = prefix
        self.suffix = suffix
    
    def __call__(self, text):
        return f"{self.prefix}{text}{self.suffix}

quote = Formatter('"', '"')
print(quote("Hello"))  # "Hello"
```

---

## Numerical Derivative

### 1. Function Operator

```python
class NumericalDerivative:
    def __init__(self, func, h=1e-5):
        self.func = func
        self.h = h
    
    def __call__(self, x):
        h = self.h
        return (self.func(x + h) - self.func(x - h)) / (2 * h)

import math
f = math.sin
df = NumericalDerivative(f)

print(df(math.pi / 2))  # ≈ 0 (cos(π/2))
print(df(0))            # ≈ 1 (cos(0))
```

### 2. Transforms Functions

Takes a function, returns derivative function.

### 3. Composition

```python
# Second derivative
d2f = NumericalDerivative(df)
```

---

## Neural Network Layer

### 1. PyTorch Pattern

```python
class LinearLayer:
    def __init__(self, in_features, out_features):
        self.weight = random_matrix(out_features, in_features)
        self.bias = random_vector(out_features)
    
    def __call__(self, x):
        return x @ self.weight.T + self.bias

layer = LinearLayer(10, 5)
output = layer(input_data)  # Clean syntax
```

### 2. Chaining Layers

```python
layer1 = LinearLayer(784, 128)
layer2 = LinearLayer(128, 10)

x = input_data
x = layer1(x)
x = relu(x)
x = layer2(x)
```

### 3. Framework Integration

All PyTorch/TensorFlow layers are callable.

---

## Command Pattern

### 1. Function Registry

```python
class Command:
    def __init__(self):
        self.registry = {}
    
    def register(self, name, func):
        self.registry[name] = func
    
    def __call__(self, name, *args, **kwargs):
        if name not in self.registry:
            raise ValueError(f"Unknown: {name}")
        return self.registry[name](*args, **kwargs)

cmd = Command()
cmd.register("add", lambda x, y: x + y)
cmd.register("mul", lambda x, y: x * y)

print(cmd("add", 2, 3))  # 5
print(cmd("mul", 4, 5))  # 20
```

### 2. Dynamic Dispatch

```python
class Calculator:
    def __init__(self):
        self.operations = {
            "add": self._add,
            "sub": self._sub,
        }
    
    def _add(self, a, b): return a + b
    def _sub(self, a, b): return a - b
    
    def __call__(self, op, a, b):
        return self.operations[op](a, b)

calc = Calculator()
print(calc("add", 5, 3))  # 8
```

### 3. Strategy Pattern

Callable objects as interchangeable strategies.

---

## Decorator Pattern

### 1. Callable Decorator

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))
print(greet.count)  # 2
```

### 2. With Configuration

```python
class Retry:
    def __init__(self, max_attempts):
        self.max_attempts = max_attempts
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for attempt in range(self.max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == self.max_attempts - 1:
                        raise
        return wrapper

@Retry(3)
def unstable_operation():
    pass
```

### 3. State Preservation

Decorators can maintain state across calls.

---

## Caching/Memoization

### 1. Cache Results

```python
class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # Fast with caching
```

### 2. LRU Cache

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(n):
    # Cached automatically
    pass
```

### 3. Clear Cache

```python
class Memoize:
    def clear_cache(self):
        self.cache.clear()
```

---

## Partial Application

### 1. Bind Arguments

```python
class Partial:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    
    def __call__(self, *more_args, **more_kwargs):
        all_args = self.args + more_args
        all_kwargs = {**self.kwargs, **more_kwargs}
        return self.func(*all_args, **all_kwargs)

def power(base, exponent):
    return base ** exponent

square = Partial(power, exponent=2)
print(square(5))  # 25
```

### 2. `functools.partial`

```python
from functools import partial

square = partial(power, exponent=2)
print(square(5))  # 25
```

### 3. Use Cases

Configuration, default arguments, callback binding.

---

## Callable Check

### 1. Test Callability

```python
def is_callable(obj):
    return callable(obj)

print(callable(Adder(5)))      # True
print(callable(lambda x: x))   # True
print(callable(42))            # False
```

### 2. `callable()` Built-in

```python
class NotCallable:
    pass

class IsCallable:
    def __call__(self):
        pass

print(callable(NotCallable()))  # False
print(callable(IsCallable()))   # True
```

### 3. Duck Typing

```python
if callable(obj):
    result = obj(args)
```

---

## Best Practices

### 1. Document Signature

```python
class Processor:
    """
    Callable that processes data.
    
    Args:
        data: Input data
    Returns:
        Processed result
    """
    def __call__(self, data):
        pass
```

### 2. Clear Purpose

Use when state + function behavior needed.

### 3. Alternative Methods

```python
class Calculator:
    def __call__(self, op, a, b):
        # Primary interface
        pass
    
    def add(self, a, b):
        # Alternative explicit method
        pass
```

---

## Key Takeaways

- `__call__` makes objects callable like functions.
- Enables stateful functions.
- Useful for decorators, strategies, commands.
- Provides extensibility via inheritance.
- Check with `callable()` built-in.
- Common in ML frameworks (PyTorch, TensorFlow).
