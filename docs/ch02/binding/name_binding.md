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

---

## Namespaces as Dictionaries

Every namespace in Python is implemented as (or backed by) a dictionary. You can inspect them directly:

```python
x = 10

def greet():
    name = "Alice"
    print(locals())   # {'name': 'Alice'}

greet()
print("x" in globals())  # True
```

`globals()` returns the module-level namespace as a dictionary. `locals()` returns the current function's namespace. This is not a metaphor---namespaces literally are dictionaries.

---

## The LEGB Rule

When Python encounters a name, it searches four namespaces in order:

| Letter | Scope | Description |
| --- | --- | --- |
| **L** | Local | Names defined inside the current function |
| **E** | Enclosing | Names in any enclosing function |
| **G** | Global | Names defined at the module level |
| **B** | Built-in | Predefined names |

---

## Scope Determined at Compile Time

Python determines the scope of each name **at compile time**, not at runtime.

```python
x = 10

def broken():
    print(x)   # UnboundLocalError!
    x = 20
```

Python sees `x = 20` and classifies `x` as **local** for the entire function.

---

## Advanced Note: Assignment Changes Scope (and Evaluation)

Assignment does more than bind a name — it also determines **where that name lives**.

Consider:

```python
n = 10

def f():
    n = n + 1
    return n
```

This raises:

```
UnboundLocalError: local variable 'n' referenced before assignment
```

### What actually happens

Before execution, Python analyzes the function:

- It sees `n = ...`
- Therefore, `n` is **local to the function**

This decision is made **before any line runs**.

Now when evaluating:

```python
n + 1
```

Python does:

1. Look up `n` in the **local scope**
2. Not find a value (not assigned yet)
3. Raise an error

### Key insight

> Assignment affects *all* uses of the name in the function

Even earlier lines.

---

## Refined Mental Model

Combine name binding and scope:

> **scope → evaluate RHS → bind to LHS**

- Scope is determined first (compile time)
- RHS is evaluated using that scope
- LHS binding updates the namespace

---

## Comparison

### No assignment → global lookup

```python
def f():
    return n + 1
```

- `n` not assigned → not local
- → Python searches global scope
- → works

---

### With assignment → local shadowing

```python
def f():
    n = n + 1
```

- `n` assigned → local
- → shadows global `n`
- → RHS uses uninitialized local → error

---

## Summary

| Situation | Result |
|----------|--------|
| Name assigned in function | Local variable |
| RHS uses that name | Uses local scope |
| Local not initialized | UnboundLocalError |
| No assignment | Falls back to LEGB |

---

## Key Takeaway

> Names are dictionary keys — but **which dictionary** is decided *before execution*.

Assignment doesn't just insert into a dictionary --- it determines **which dictionary will be used everywhere in the function**.

---

## Exercises

**Exercise 1.**
Predict the output and explain which namespace each name lives in:

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        print(x)

    inner()

outer()
```

Which scope does `inner` find `x` in? What would change if `inner` also had `x = "local"` before the `print`?

??? success "Solution to Exercise 1"
    Output:

    ```text
    enclosing
    ```

    `inner` does not assign `x`, so it is not local. Python searches LEGB: Local (no `x`) -> Enclosing (`x = "enclosing"` found). It prints `"enclosing"`.

    If `inner` had `x = "local"` before the `print`, Python would classify `x` as local to `inner` at compile time. The `print(x)` would use the local value `"local"`.

---

**Exercise 2.**
Explain why this code raises an error, and provide two different fixes:

```python
total = 0

def add(n):
    total = total + n
    return total

add(5)
```

??? success "Solution to Exercise 2"
    `UnboundLocalError: local variable 'total' referenced before assignment`.

    Python sees `total = ...` inside `add` and marks `total` as local at compile time. When evaluating `total + n`, it looks for the local `total`, which has not been assigned yet.

    **Fix 1 --- use `global`** (generally discouraged):

    ```python
    def add(n):
        global total
        total = total + n
        return total
    ```

    **Fix 2 --- pass and return** (preferred):

    ```python
    total = 0

    def add(total, n):
        return total + n

    total = add(total, 5)
    ```

    Fix 2 makes data flow explicit through parameters and return values, avoiding hidden state dependencies.

---

**Exercise 3.**
`del` removes a name from its namespace. Predict the output:

```python
x = 10
y = x
del x

print(y)
print(x)
```

What happens to the object `10` after `del x`? Is it destroyed?

??? success "Solution to Exercise 3"
    Output:

    ```text
    10
    ```

    Then `print(x)` raises `NameError: name 'x' is not defined`.

    `del x` removes the name `x` from the namespace dictionary. It does NOT destroy the object `10`. The object still exists because `y` still references it. An object is only garbage-collected when no names (or other references) point to it. `del` removes the dictionary entry, not the object.
