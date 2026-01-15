# Parameter Mechanisms

Python provides flexible mechanisms for defining and passing function parameters. Understanding these mechanisms helps write more expressive and maintainable code.


## Parameter Categories

Python has five categories of parameters:

1. **Positional-or-keyword** - Can be passed either way
2. **Positional-only** - Must be passed by position (before `/`)
3. **Keyword-only** - Must be passed by name (after `*`)
4. **`*args`** - Captures extra positional arguments
5. **`**kwargs`** - Captures extra keyword arguments


## Basic Positional and Keyword Arguments

By default, parameters can be passed positionally or by keyword.

```python
def greet(name, greeting):
    return f"{greeting}, {name}!"

# All equivalent
greet("Alice", "Hello")           # Positional
greet(name="Alice", greeting="Hello")  # Keyword
greet("Alice", greeting="Hello")  # Mixed
```


## Default Values

Parameters can have default values, making them optional.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")           # "Hello, Alice!"
greet("Alice", "Hi")     # "Hi, Alice!"
```

**Rule**: Parameters with defaults must come after parameters without defaults.

```python
# Valid
def func(a, b, c=10, d=20):
    pass

# Invalid - SyntaxError
def func(a, b=10, c):  # Non-default after default
    pass
```


## Positional-Only Parameters (/)

Parameters before `/` must be passed positionally.

```python
def divide(x, y, /):
    return x / y

divide(10, 2)      # OK: 5.0
divide(x=10, y=2)  # TypeError: positional-only argument
```

**Use cases**:
- When parameter names are meaningless (`x`, `y`)
- To allow future parameter name changes without breaking API
- For performance in C-implemented functions

```python
# Real-world example: len() is positional-only
len([1, 2, 3])     # OK
len(obj=[1, 2, 3]) # TypeError
```


## Keyword-Only Parameters (*)

Parameters after `*` must be passed by keyword.

```python
def connect(host, port, *, timeout=30, retries=3):
    print(f"Connecting to {host}:{port}")
    print(f"timeout={timeout}, retries={retries}")

connect("localhost", 8080)                    # OK
connect("localhost", 8080, timeout=60)        # OK
connect("localhost", 8080, 60)                # TypeError
```

**Use cases**:
- Forcing explicit, self-documenting calls
- Preventing accidental positional matches
- Boolean flags that would be unclear positionally

```python
# Without keyword-only: What does True mean?
process_file("data.txt", True, False)

# With keyword-only: Clear intent
def process_file(path, *, verbose=False, overwrite=False):
    pass

process_file("data.txt", verbose=True, overwrite=False)
```


## Combined Syntax

You can combine `/` and `*` in the same function.

```python
def func(pos_only, /, standard, *, kw_only):
    print(f"{pos_only}, {standard}, {kw_only}")

func(1, 2, kw_only=3)           # OK
func(1, standard=2, kw_only=3)  # OK
func(pos_only=1, standard=2, kw_only=3)  # TypeError
func(1, 2, 3)                   # TypeError
```

**Full parameter order**:
```python
def func(pos_only, /, pos_or_kw, *args, kw_only, **kwargs):
    pass
```


## *args: Variable Positional Arguments

`*args` captures any extra positional arguments as a tuple.

```python
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2)           # 3
sum_all(1, 2, 3, 4, 5)  # 15
sum_all()               # 0

# args is a tuple
def show_args(*args):
    print(type(args))   # <class 'tuple'>
    print(args)

show_args(1, "hello", [1, 2])  # (1, 'hello', [1, 2])
```


## **kwargs: Variable Keyword Arguments

`**kwargs` captures any extra keyword arguments as a dictionary.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
```

Output:
```
name: Alice
age: 30
city: NYC
```


## Combining *args and **kwargs

A function can accept any arguments with `*args` and `**kwargs`.

```python
def flexible(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

flexible(1, 2, 3, name="Alice", age=30)
```

Output:
```
Positional: (1, 2, 3)
Keyword: {'name': 'Alice', 'age': 30}
```

**Common use**: Wrapper functions and decorators.

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```


## Unpacking Arguments

Use `*` and `**` when calling functions to unpack iterables and dictionaries.

```python
def add(a, b, c):
    return a + b + c

# Unpack list/tuple
numbers = [1, 2, 3]
add(*numbers)  # 6

# Unpack dictionary
params = {"a": 1, "b": 2, "c": 3}
add(**params)  # 6

# Combined
add(*[1, 2], **{"c": 3})  # 6
```


## Parameter Order Rules

When defining functions, parameters must appear in this order:

```python
def func(
    positional_only,      # 1. Positional-only
    /,                    # 2. Separator
    positional_or_keyword,# 3. Standard
    *args,                # 4. *args (also makes following kw-only)
    keyword_only,         # 5. Keyword-only
    **kwargs              # 6. **kwargs (must be last)
):
    pass
```


## Real-World Examples

### print() signature

```python
# Simplified signature of print()
def print(*values, sep=' ', end='\n', file=None):
    pass

print(1, 2, 3)              # 1 2 3
print(1, 2, 3, sep='-')     # 1-2-3
print(1, 2, 3, end='!\n')   # 1 2 3!
```

### sorted() signature

```python
# sorted(iterable, /, *, key=None, reverse=False)
sorted([3, 1, 2])                    # [1, 2, 3]
sorted([3, 1, 2], reverse=True)      # [3, 2, 1]
sorted(["b", "A"], key=str.lower)    # ['A', 'b']
```


## Quick Reference

| Syntax | Meaning |
|--------|---------|
| `def f(a, b)` | Standard parameters |
| `def f(a, b=10)` | Default value |
| `def f(a, /)` | Positional-only |
| `def f(*, a)` | Keyword-only |
| `def f(*args)` | Variable positional |
| `def f(**kwargs)` | Variable keyword |
| `f(*list)` | Unpack iterable |
| `f(**dict)` | Unpack dictionary |
