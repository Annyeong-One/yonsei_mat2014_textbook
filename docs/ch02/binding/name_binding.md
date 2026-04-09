

# Name Binding Model

## The Mental Model

Think of Python's runtime as a collection of **dictionaries**. Each dictionary
maps names (strings) to objects. When you write `x = 42`, Python adds the
entry `"x": 42` to whichever dictionary is currently active. When you read `x`,
Python searches through a specific chain of dictionaries until it finds the
key `"x"`.

These dictionaries are called **namespaces**, and the search order is called
the **scope resolution rule**. Understanding this model explains how Python
finds names, why some names shadow others, and what happens when you use
`global` or `nonlocal`.

---

## What Creates a Name Binding

Several Python statements create name bindings -- they add entries to a
namespace:

| Statement | Name created | Example |
| --- | --- | --- |
| Assignment | Left-hand side name | `x = 10` |
| `def` | Function name | `def greet(): ...` |
| `class` | Class name | `class Dog: ...` |
| `import` | Module or alias name | `import os` |
| `from ... import` | Imported name or alias | `from math import pi` |
| `for` loop | Loop variable | `for i in range(5):` |
| `with` statement | Target name | `with open(f) as fh:` |
| `except` clause | Exception name | `except ValueError as e:` |
| Function parameters | Parameter names | `def f(a, b):` |

Each of these statements binds a name in the **current** namespace.

### How def Creates a Name

A `def` statement does two things: it creates a **function object**, and it
binds the function's name in the enclosing namespace:

```python
def square(n):
    return n * n

print(type(square))  # <class 'function'>
print(square)        # <function square at 0x...>
```

The name `square` is an ordinary entry in the namespace. You can rebind it:

```python
def square(n):
    return n * n

old = square
square = 42
print(square)    # 42
print(old(5))    # 25 -- the function object still exists
```

### How import Creates a Name

An `import` statement creates a **module object** and binds a name to it:

```python
import math
print(type(math))  # <class 'module'>
print(math.pi)     # 3.141592653589793
```

With `from ... import`, specific attributes are copied into the current
namespace:

```python
from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)        # 3.141592653589793
```

Using an alias binds under a different name:

```python
import numpy as np  # binds the module object under the name "np"
```

---

## Namespaces as Dictionaries

Every namespace in Python is implemented as (or backed by) a dictionary. You
can inspect them directly:

### The global namespace

```python
x = 10
name = "Alice"

print(globals())
```

`globals()` returns the dictionary for the current module's namespace. You will
see `"x"` and `"name"` as keys among the built-in entries.

### The local namespace

Inside a function, `locals()` returns the local namespace:

```python
def example():
    a = 1
    b = 2
    print(locals())

example()  # {'a': 1, 'b': 2}
```

At module level, `locals()` and `globals()` return the same dictionary.

### Namespace manipulation

Because `globals()` returns a real dictionary, you can modify it directly
(though this is rarely advisable):

```python
globals()["dynamic_var"] = 99
print(dynamic_var)  # 99
```

This confirms the mental model: name binding is literally dictionary insertion.

---

## The LEGB Rule

When Python encounters a name, it searches four namespaces in order:

| Letter | Scope | Description |
| --- | --- | --- |
| **L** | Local | Names defined inside the current function |
| **E** | Enclosing | Names in any enclosing function (for nested functions) |
| **G** | Global | Names defined at the module level |
| **B** | Built-in | Names pre-defined by Python (`len`, `print`, `int`, etc.) |

Python searches from L to B and stops at the first match.

### LEGB in action

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # "local" -- found in L

    inner()
    print(x)  # "enclosing" -- found in L of outer

outer()
print(x)  # "global" -- found in G
```

### Falling through to built-in scope

```python
def demo():
    result = len([1, 2, 3])  # "len" not in L, E, or G -- found in B
    print(result)

demo()  # 3
```

### Shadowing

A local name can shadow a global or built-in name:

```python
len = 42  # shadows the built-in len

# print(len([1, 2, 3]))  # TypeError: 'int' object is not callable

del len  # remove the shadow, restoring access to the built-in
print(len([1, 2, 3]))  # 3
```

!!! warning "Avoid shadowing built-in names"
    Binding a name like `list`, `dict`, `str`, `len`, or `print` in your own
    code hides the built-in. This is a common source of confusing errors.

---

## Removing Names with del

The `del` statement removes a name from its namespace:

```python
x = 100
print(x)    # 100

del x
# print(x)  # NameError: name 'x' is not defined
```

`del` does **not** destroy the object. It removes the name-to-object binding.
The object is only destroyed when no references remain (garbage collection):

```python
a = [1, 2, 3]
b = a
del a
print(b)  # [1, 2, 3] -- the list object still exists because b refers to it
```

You can also delete attributes and dictionary entries with `del`:

```python
d = {"key": "value"}
del d["key"]
print(d)  # {}
```

---

## Scope Determined at Compile Time

Python determines the scope of each name **at compile time** (when the
function is defined), not at runtime. This has an important consequence:

```python
x = 10

def broken():
    print(x)   # UnboundLocalError!
    x = 20

# broken()
```

Python sees the assignment `x = 20` inside `broken` and classifies `x` as a
**local** variable for the entire function body. When `print(x)` executes, the
local `x` has not yet been assigned, causing an `UnboundLocalError`.

This is not a bug -- it is a direct consequence of compile-time scope analysis.
If you intend to read and write a global variable inside a function, use the
`global` declaration:

```python
x = 10

def fixed():
    global x
    print(x)  # 10
    x = 20

fixed()
print(x)  # 20
```

---

## Summary

| Concept | Key idea |
| --- | --- |
| Namespace | A dictionary mapping names to objects |
| Name binding | Adding an entry to a namespace (`x = ...`, `def`, `import`, etc.) |
| LEGB rule | Search order: Local, Enclosing, Global, Built-in |
| `del` | Removes a name from a namespace (not the object) |
| Scope analysis | Python determines scope at compile time, not runtime |

Names are not magic -- they are dictionary keys. Every operation on names
reduces to dictionary lookups and insertions, governed by the LEGB search
order.

---

## Exercises

**Exercise 1.**
Predict the output of the following code. For each `print` call, state which
scope (Local, Enclosing, Global, or Built-in) provides the value and why.

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        print(x)

    inner()

outer()
print(x)
```

??? success "Solution to Exercise 1"
    Output:

    ```text
    enclosing
    global
    ```

    - The first `print(x)` is inside `inner()`. Python searches the local
      scope of `inner` and finds no `x`. It then searches the **enclosing**
      scope (`outer`), where `x = "enclosing"` exists. It prints `"enclosing"`.
    - The second `print(x)` is at module level. Python searches the **global**
      scope, where `x = "global"` exists. It prints `"global"`.

    The key point is that `inner` does not have its own `x`, so LEGB resolution
    falls through from L to E. The module-level `print` resolves `x` directly
    at the G level.

---

**Exercise 2.**
Explain why the following function raises an error, even though `total` is
defined before the `print` call at module level. Fix the function in two
different ways: once using the `global` keyword, and once by redesigning the
function to avoid `global`.

```python
total = 0

def add_to_total(n):
    print(total)
    total = total + n

add_to_total(5)
```

??? success "Solution to Exercise 2"
    The function raises `UnboundLocalError: cannot access local variable
    'total' before assignment`. Python's compiler sees the assignment
    `total = total + n` and classifies `total` as a **local** variable for
    the entire function body. When `print(total)` executes, the local `total`
    has not yet been assigned.

    **Fix 1 -- using `global`:**

    ```python
    total = 0

    def add_to_total(n):
        global total
        print(total)
        total = total + n

    add_to_total(5)  # prints 0, then total becomes 5
    ```

    The `global` declaration tells Python that `total` inside this function
    refers to the module-level name.

    **Fix 2 -- redesign without `global`:**

    ```python
    def add_to_total(current_total, n):
        print(current_total)
        return current_total + n

    total = 0
    total = add_to_total(total, 5)  # prints 0, total becomes 5
    ```

    This approach passes `total` as an argument and returns the new value,
    avoiding shared mutable state entirely. This is generally preferred because
    it makes data flow explicit and the function easier to test.

---

**Exercise 3.**
Write a short program that demonstrates that `del` removes a name but not the
underlying object. Your program should:

1. Create a list and bind two names to it.
2. Delete one name.
3. Show that the other name still accesses the list.
4. Show that the deleted name raises `NameError`.

Include the expected output as comments.

??? success "Solution to Exercise 3"
    ```python
    data = [10, 20, 30]
    backup = data          # both names refer to the same list object

    print(id(data) == id(backup))  # True -- same object

    del data               # remove the name "data" from the namespace

    print(backup)          # [10, 20, 30] -- object still exists
    print(type(backup))    # <class 'list'>

    try:
        print(data)
    except NameError as e:
        print(e)           # name 'data' is not defined
    ```

    Expected output:

    ```text
    True
    [10, 20, 30]
    <class 'list'>
    name 'data' is not defined
    ```

    `del data` removes the entry `"data"` from the namespace dictionary. The
    list object itself is unaffected because `backup` still holds a reference
    to it. The object would only be garbage-collected when its reference count
    drops to zero (i.e., when no name or container refers to it).
