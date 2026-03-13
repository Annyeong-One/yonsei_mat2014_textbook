# Anti-Patterns and Pitfalls

Common mistakes and gotchas to avoid in Python.

## Scope Pitfalls

### Late Binding in Closures

One of the most common Python gotchas:

```python
# BUG: All functions return 2 (last value of i)
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])  # [2, 2, 2]

# FIX: Capture i as default argument
funcs = [lambda x=i: x for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]

# FIX: Use functools.partial
from functools import partial
funcs = [partial(lambda x: x, i) for i in range(3)]
```

**Why it happens**: The lambda captures `i` by reference, not by value. When called, it uses the current value of `i`, which is 2 after the loop completes.

### UnboundLocalError

```python
# BUG: UnboundLocalError
x = 10

def function():
    print(x)  # Error! Python sees assignment below
    x = 20    # This makes x local to entire function

# FIX 1: Use global
def function():
    global x
    print(x)
    x = 20

# FIX 2: Use different variable name
def function():
    print(x)
    y = 20
```

### Missing `nonlocal`

```python
# BUG: UnboundLocalError
def outer():
    count = 0
    def inner():
        count += 1  # Error! count is local
    inner()

# FIX: Declare nonlocal
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
    return count  # Returns 1
```

---

## Mutable Default Arguments

One of Python's most infamous gotchas:

```python
# BUG: Default list is shared between calls
def append_to(item, lst=[]):
    lst.append(item)
    return lst

print(append_to(1))  # [1]
print(append_to(2))  # [1, 2] - Unexpected!
print(append_to(3))  # [1, 2, 3] - Keeps growing!

# FIX: Use None as default
def append_to(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

**Why it happens**: Default arguments are evaluated once when the function is defined, not each time it's called.

---

## `locals()` Caveats

### Cannot Create Variables

```python
# BUG: This doesn't work
def function():
    locals()['x'] = 10
    print(x)  # NameError: name 'x' is not defined

# The locals() dict is a copy, not the actual namespace
```

### Read-Only in Functions

```python
def function():
    x = 10
    y = 20
    
    # Good: inspection/debugging
    print(locals())  # {'x': 10, 'y': 20}
    
    # Bad: trying to modify
    locals()['x'] = 100
    print(x)  # Still 10!
```

### Correct Usage

```python
# For inspection only
def debug_locals():
    a = 1
    b = 2
    for name, value in locals().items():
        print(f"{name} = {value}")

# Use normal assignment for variables
def function():
    x = 10  # Correct way to create local variable
```

---

## Common Anti-Patterns

### Wildcard Imports

```python
# BAD: Pollutes namespace, hides dependencies
from module import *

# GOOD: Explicit imports
from module import specific_function, SpecificClass
```

### Bare `except`

```python
# BAD: Catches everything including KeyboardInterrupt
try:
    risky_operation()
except:
    pass

# GOOD: Catch specific exceptions
try:
    risky_operation()
except ValueError as e:
    handle_error(e)
except (TypeError, KeyError):
    handle_other_error()
```

### Using `is` for Value Comparison

```python
# BAD: May fail for large numbers
if x is 1000:
    pass

# GOOD: Use == for values
if x == 1000:
    pass

# is is correct for: None, True, False
if x is None:
    pass
```

### Modifying List While Iterating

```python
# BUG: Skips elements
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)
print(items)  # [1, 3, 5] - Looks ok but is buggy

# FIX 1: Iterate over copy
for item in items[:]:
    if item % 2 == 0:
        items.remove(item)

# FIX 2: List comprehension
items = [item for item in items if item % 2 != 0]

# FIX 3: Filter
items = list(filter(lambda x: x % 2 != 0, items))
```

### String Concatenation in Loop

```python
# BAD: O(n²) complexity
result = ""
for s in strings:
    result += s

# GOOD: O(n) complexity
result = "".join(strings)
```

---

## Gotcha Summary

| Gotcha | Symptom | Fix |
|--------|---------|-----|
| Late binding | All closures return same value | Use default argument `x=i` |
| UnboundLocalError | Variable not found | Add `global` or `nonlocal` |
| Mutable default | Shared state between calls | Use `None` as default |
| `locals()` modification | Variable not created | Use normal assignment |
| Bare except | Catches too much | Specify exception types |
| List modification | Skipped elements | Iterate over copy |

---

## Best Practices

1. **Always use `None` for mutable defaults**
2. **Capture loop variables explicitly in closures**
3. **Declare `nonlocal` or `global` when needed**
4. **Use `locals()` only for inspection**
5. **Catch specific exceptions**
6. **Don't modify collections while iterating**
7. **Use `==` for value comparison, `is` for identity**
