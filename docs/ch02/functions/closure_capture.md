# Closure Capture

When a nested function references variables from its enclosing scope, Python creates a closure. Understanding how closures capture variables is essential for avoiding subtle bugs.


## What is a Closure?

A closure is a function that remembers values from its enclosing scope, even after that scope has finished executing.

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n  # n is captured from enclosing scope
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

The inner function `multiplier` "closes over" the variable `n`.


## How Capture Works

Python captures **variables by reference**, not by value. The closure stores a reference to the variable, not a copy of its value.

```python
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

c = make_counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

Each call modifies the same `count` variable.


## Inspecting Closures

You can examine captured variables through `__closure__`:

```python
def outer(x):
    def inner():
        return x
    return inner

f = outer(10)

print(f.__closure__)           # (<cell at 0x...>,)
print(f.__closure__[0].cell_contents)  # 10
```


## The Loop Variable Gotcha

The most common closure pitfall involves loops:

```python
def create_functions():
    functions = []
    for i in range(3):
        def f():
            return i
        functions.append(f)
    return functions

funcs = create_functions()
print(funcs[0]())  # 2 (expected 0)
print(funcs[1]())  # 2 (expected 1)
print(funcs[2]())  # 2 (expected 2)
```

**All functions return 2!** Why?


## Why the Loop Gotcha Happens

Each function captures a **reference to the same variable `i`**, not its current value. By the time the functions are called, the loop has finished and `i` equals 2.

```
During loop iteration 0:
  functions[0].closure -> i (currently 0)

During loop iteration 1:
  functions[0].closure -> i (currently 1)
  functions[1].closure -> i (currently 1)

During loop iteration 2:
  functions[0].closure -> i (currently 2)
  functions[1].closure -> i (currently 2)
  functions[2].closure -> i (currently 2)

After loop:
  All closures reference i, which equals 2
```


## Solution 1: Default Parameter

Capture the current value using a default parameter:

```python
def create_functions():
    functions = []
    for i in range(3):
        def f(i=i):  # i=i captures current value
            return i
        functions.append(f)
    return functions

funcs = create_functions()
print(funcs[0]())  # 0
print(funcs[1]())  # 1
print(funcs[2]())  # 2
```

Default parameters are evaluated at function definition time, capturing the current value of `i`.


## Solution 2: Factory Function

Create a separate scope for each iteration:

```python
def create_functions():
    def make_f(i):
        def f():
            return i
        return f
    
    functions = []
    for i in range(3):
        functions.append(make_f(i))
    return functions

funcs = create_functions()
print(funcs[0]())  # 0
print(funcs[1]())  # 1
print(funcs[2]())  # 2
```

Each call to `make_f` creates a new scope with its own `i`.


## Solution 3: functools.partial

Use `partial` to bind the current value:

```python
from functools import partial

def create_functions():
    def f(i):
        return i
    
    return [partial(f, i) for i in range(3)]

funcs = create_functions()
print(funcs[0]())  # 0
print(funcs[1]())  # 1
print(funcs[2]())  # 2
```


## Solution 4: Lambda with Default

Same principle as solution 1, using lambda:

```python
functions = [lambda i=i: i for i in range(3)]

print(functions[0]())  # 0
print(functions[1]())  # 1
print(functions[2]())  # 2
```


## Real-World Example: Event Handlers

This gotcha commonly appears with event handlers or callbacks:

```python
# Bug: All buttons do the same thing
buttons = []
for i in range(5):
    def on_click():
        print(f"Button {i} clicked")
    buttons.append(on_click)

# All print "Button 4 clicked"
```

**Fix**:

```python
buttons = []
for i in range(5):
    def on_click(i=i):  # Capture current i
        print(f"Button {i} clicked")
    buttons.append(on_click)
```


## Late Binding Explained

Python uses **late binding** for closures—the value is looked up when the function is called, not when it's defined.

```python
def outer():
    x = 10
    def inner():
        return x  # x is looked up when inner() is called
    x = 20  # Change x after defining inner
    return inner

f = outer()
print(f())  # 20 (not 10!)
```

The closure sees the final value of `x`.


## Early Binding with Defaults

Default parameters use **early binding**—the value is captured when the function is defined.

```python
def outer():
    x = 10
    def inner(x=x):  # x captured NOW (value 10)
        return x
    x = 20  # Too late, inner already captured x=10
    return inner

f = outer()
print(f())  # 10
```


## Nested Loops

The gotcha compounds with nested loops:

```python
# Bug
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(lambda: (i, j))
    matrix.append(row)

print(matrix[0][0]())  # (2, 2) - Wrong!

# Fix
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(lambda i=i, j=j: (i, j))
    matrix.append(row)

print(matrix[0][0]())  # (0, 0) - Correct!
```


## Summary

| Binding Type | When Value is Captured | Syntax |
|--------------|------------------------|--------|
| Late binding | When function is called | `def f(): return x` |
| Early binding | When function is defined | `def f(x=x): return x` |

**Key Takeaways**:

1. Closures capture **variables by reference**, not by value
2. Loop variables change, but all closures share the same reference
3. Use **default parameters** to capture the current value
4. Or use a **factory function** to create separate scopes
5. This applies to `def`, `lambda`, and comprehensions
