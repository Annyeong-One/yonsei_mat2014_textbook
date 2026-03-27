# First-Class Functions

In Python, functions are **first-class objects**. This means functions can be treated like any other value — assigned to variables, passed as arguments, returned from other functions, and stored in data structures.


## Functions Are Objects

Every function in Python is an instance of the `function` type. The name `f` without parentheses refers to the function object itself; `f()` *calls* it:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(type(greet))               # <class 'function'>
print(isinstance(greet, object)) # True

print(greet)          # <function greet at 0x...>
print(greet("Alice")) # Hello, Alice!
```

Like integers and strings, a function has a type, an identity (`id`), and attributes:

```python
print(greet.__name__)   # 'greet'
print(greet.__doc__)    # None (no docstring here)
```


## Assigning Functions to Variables

A function name is just a variable that references a function object. You can bind another name to the same object:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

say_hello = greet  # No parentheses — assigns the object, not the result

print(say_hello("Alice"))  # Hello, Alice!
print(say_hello is greet)  # True — same object
```


## Passing Functions as Arguments

Functions that accept other functions as arguments are called **higher-order functions**:

```python
def apply(func, value: int) -> int:  # func is any callable
    return func(value)

def square(x: int) -> int:
    return x ** 2

result = apply(square, 5)  # 25
```

### Applying Multiple Times

```python
def apply_twice(func, value: int) -> int:  # func is any callable
    return func(func(value))

def add_ten(x: int) -> int:
    return x + 10

result = apply_twice(add_ten, 5)
print(result)  # 25 (5 + 10 + 10)
```

### Built-in Higher-Order Functions

Python's `sorted`, `map`, and `filter` all accept a function argument:

```python
numbers = [3, 1, 4, 1, 5]

def negate(x: int) -> int:
    return -x

sorted(numbers, key=negate)  # [5, 4, 3, 1, 1]

list(map(str, numbers))      # ['3', '1', '4', '1', '5']

def greater_than_two(x: int) -> bool:
    return x > 2

list(filter(greater_than_two, numbers))  # [3, 4, 5]
```

Writing a named function for every small operation gets verbose. Python provides `lambda` for short, anonymous functions — covered in its own page. For now, notice that `key=negate` is the same idea as writing `key=lambda x: -x`.


## Returning Functions

A function can create and return another function. The inner function remembers the value of `n` even after `make_multiplier` has finished — this mechanism is called a **closure**, covered in detail in a later chapter:

```python
def make_multiplier(n: int):
    def multiply(x: int) -> int:
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```


## Storing Functions in Data Structures

Functions can be stored in lists, dictionaries, or any container.

### Lists

```python
def increment(x: int) -> int:
    return x + 1

def double(x: int) -> int:
    return x * 2

def square(x: int) -> int:
    return x ** 2

operations = [increment, double, square]

for op in operations:
    print(op(5))  # 6, 10, 25
```

### Dispatch Table

A dictionary that maps names to handler functions replaces long `if/elif` chains:

```python
def handle_get(request: dict) -> str:
    return "GET response"

def handle_post(request: dict) -> str:
    return "POST response"

def handle_delete(request: dict) -> str:
    return "DELETE response"

handlers = {
    "GET": handle_get,
    "POST": handle_post,
    "DELETE": handle_delete,
}

def dispatch(method: str, request: dict) -> str:
    handler = handlers.get(method)
    if handler:
        return handler(request)
    return "Unknown method"

print(dispatch("GET", {}))    # GET response
print(dispatch("POST", {}))   # POST response
print(dispatch("PATCH", {}))  # Unknown method
```

Because functions are values, the dictionary stores the function objects directly — no special syntax required.

First-class functions also enable closures, decorators, and callable objects, each of which builds on the ideas introduced here and is covered in its own chapter.
