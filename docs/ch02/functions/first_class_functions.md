# First-Class Functions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

In Python, functions are **first-class objects**. This means functions can be treated like any other value—assigned to variables, passed as arguments, returned from other functions, and stored in data structures.

---

## Functions Are Objects

Every function in Python is an instance of the `function` type:

```python
def greet(name):
    return f"Hello, {name}!"

print(type(greet))        # <class 'function'>
print(isinstance(greet, object))  # True
```

---

## Assigning Functions to Variables

A function name is just a variable that references a function object:

```python
def greet(name):
    return f"Hello, {name}!"

say_hello = greet  # Assign function to new variable

print(say_hello("Alice"))  # "Hello, Alice!"
print(greet("Alice"))      # "Hello, Alice!"
print(say_hello is greet)  # True (same object)
```

---

## Passing Functions as Arguments

Functions can be passed to other functions (higher-order functions):

```python
def apply(func, value):
    return func(value)

def square(x):
    return x ** 2

result = apply(square, 5)  # 25
```

### Applying Multiple Times

```python
def apply_twice(func, value):
    return func(func(value))

def add_ten(x):
    return x + 10

result = apply_twice(add_ten, 5)
print(result)  # 25 (5 + 10 + 10)
```

### Built-in Examples

```python
numbers = [3, 1, 4, 1, 5]

# sorted() takes a key function
sorted(numbers, key=lambda x: -x)  # [5, 4, 3, 1, 1]

# map() applies a function to each element
list(map(str, numbers))  # ['3', '1', '4', '1', '5']

# filter() keeps elements where function returns True
list(filter(lambda x: x > 2, numbers))  # [3, 4, 5]
```

---

## Returning Functions

Functions can create and return other functions:

```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

---

## Storing Functions in Data Structures

Functions can be stored in lists, dictionaries, etc.

### Lists

```python
operations = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2
]

# Apply each operation
for op in operations:
    print(op(5))  # 6, 10, 25

# Chain operations
value = 3
for op in operations:
    value = op(value)
print(value)  # ((3 + 1) * 2) ** 2 = 64
```

### Dictionaries

```python
commands = {
    'add': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mul': lambda a, b: a * b,
}

print(commands['add'](10, 5))  # 15
print(commands['mul'](5, 3))   # 15
```

---

## Function Dispatch Table

A common pattern using functions in dictionaries:

```python
def handle_get(request):
    return "GET response"

def handle_post(request):
    return "POST response"

def handle_delete(request):
    return "DELETE response"

handlers = {
    'GET': handle_get,
    'POST': handle_post,
    'DELETE': handle_delete,
}

def dispatch(method, request):
    handler = handlers.get(method)
    if handler:
        return handler(request)
    return "Unknown method"

print(dispatch('GET', {}))     # "GET response"
print(dispatch('POST', {}))    # "POST response"
print(dispatch('PATCH', {}))   # "Unknown method"
```

---

## Function Attributes

Functions have attributes like any other object:

```python
def greet(name):
    """Return a greeting."""
    return f"Hello, {name}!"

print(greet.__name__)      # 'greet'
print(greet.__doc__)       # 'Return a greeting.'
print(greet.__module__)    # '__main__'
print(greet.__code__)      # <code object greet at ...>
```

### Custom Attributes

You can even add custom attributes:

```python
def counter():
    counter.calls += 1
    return counter.calls

counter.calls = 0

print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

---

## Introspection

You can inspect function properties using the `inspect` module:

```python
def example(a, b, c=10, *args, **kwargs):
    """An example function."""
    pass

import inspect

# Get signature
sig = inspect.signature(example)
print(sig)  # (a, b, c=10, *args, **kwargs)

# Get parameters
for name, param in sig.parameters.items():
    print(f"{name}: {param.kind.name}, default={param.default}")
```

Output:
```
a: POSITIONAL_OR_KEYWORD, default=<class 'inspect._empty'>
b: POSITIONAL_OR_KEYWORD, default=<class 'inspect._empty'>
c: POSITIONAL_OR_KEYWORD, default=10
args: VAR_POSITIONAL, default=<class 'inspect._empty'>
kwargs: VAR_KEYWORD, default=<class 'inspect._empty'>
```

---

## Callable Objects

Any object with a `__call__` method behaves like a function:

```python
class Adder:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, x):
        return x + self.n

add_five = Adder(5)
print(add_five(10))  # 15
print(callable(add_five))  # True
```

### Checking Callability

Use `callable()` to check if something can be called:

```python
def func():
    pass

class MyClass:
    pass

class CallableClass:
    def __call__(self):
        pass

print(callable(func))           # True
print(callable(MyClass))        # True (classes are callable)
print(callable(CallableClass()))# True (has __call__)
print(callable(42))             # False
print(callable("hello"))        # False
```

---

## Practical Applications

### Strategy Pattern

```python
def process_data(data, strategy):
    return strategy(data)

def uppercase(text):
    return text.upper()

def reverse(text):
    return text[::-1]

text = "hello"
print(process_data(text, uppercase))  # "HELLO"
print(process_data(text, reverse))    # "olleh"
```

### Callback Functions

```python
def fetch_data(url, on_success, on_error):
    try:
        # Simulate fetching
        result = f"Data from {url}"
        on_success(result)
    except Exception as e:
        on_error(e)

fetch_data(
    "example.com",
    on_success=lambda data: print(f"Got: {data}"),
    on_error=lambda err: print(f"Error: {err}")
)
```

### Decorators (Preview)

First-class functions enable decorators:

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(2, 3)
```

Output:
```
Calling add
Returned 5
```

---

## Summary

| Capability | Example |
|------------|---------|
| Assign to variable | `f = my_func` |
| Pass as argument | `map(func, items)` |
| Return from function | `return inner_func` |
| Store in data structure | `funcs = [f1, f2]` |
| Access attributes | `func.__name__` |
| Check callability | `callable(obj)` |

**Key Takeaway**: In Python, functions are values. Anything you can do with a number or string, you can do with a function.
