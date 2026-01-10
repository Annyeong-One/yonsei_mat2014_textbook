# Functions as Objects

In Python, **functions are first-class objects**. This means they can be assigned to variables, passed as arguments, and returned from other functions.

---

## 1. Functions as values

A function can be treated like any other object:

```python
def f(x):
    return x + 1

g = f
g(10)   # 11
```

Here, `g` is another reference to the same function object.

---

## 2. Passing functions as arguments

Functions are often passed to other functions:

```python
def apply(fn, x):
    return fn(x)

apply(f, 5)
```

This pattern underlies:
- callbacks,
- numerical methods,
- higher-order abstractions.

---

## 3. Returning functions

Functions can return other functions:

```python
def make_multiplier(a):
    def mul(x):
        return a * x
    return mul

double = make_multiplier(2)
double(10)
```

This uses **closures** to capture state.

---

## 4. Practical importance

Functions as objects enable:
- decorators,
- functional programming patterns,
- flexible APIs.

They are essential for modern Python design.

---

## Key takeaways

- Functions are objects.
- They can be passed, stored, and returned.
- Closures capture surrounding state.
