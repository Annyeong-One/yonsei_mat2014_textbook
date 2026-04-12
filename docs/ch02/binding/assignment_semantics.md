

# Assignment Semantics

## The Mental Model

Many programmers coming from C or Java think of assignment as "putting a value
into a box." Python works differently. The statement `a = 10` does **not**
place the integer 10 inside a container called `a`. Instead, Python performs
three steps:

1. **Evaluate the right-hand side** to produce an object.
2. **Create or find** the resulting object in memory.
3. **Bind the name** on the left-hand side to that object.

A name in Python is a label attached to an object, not a storage location.
Grasping this distinction is the single most important step toward
understanding Python's runtime behavior.

---

## How Simple Assignment Works

Consider the following:

```python
x = 2 + 3
```

Python evaluates `2 + 3`, producing the integer object `5`. It then binds the
name `x` to that object. The name `x` now *refers to* (points at) the object
`5`.

```python
x = 2 + 3
y = x
print(x is y)  # True -- both names point to the same object
```

After `y = x`, the names `x` and `y` are **two labels attached to the same
object**. No copy is made. You can verify this with `id()`:

```python
x = [1, 2, 3]
y = x
print(id(x))  # e.g. 140234866203200
print(id(y))  # same number
```

---

## Chained Assignment

Python allows chaining assignments:

```python
a = b = c = 0
```

This evaluates the right-hand side once, producing a single `int` object `0`,
then binds the names `a`, `b`, and `c` to that same object. It is equivalent
to:

```python
temp = 0
a = temp
b = temp
c = temp
```

All three names share identity:

```python
a = b = c = []
print(a is b)  # True
print(b is c)  # True
a.append(1)
print(c)       # [1] -- same object
```

!!! warning "Chained assignment with mutable objects"
    Because chained assignment creates one object shared by multiple names,
    mutating through any name affects all of them. If you need independent
    lists, create separate literals: `a, b, c = [], [], []`.

---

## Simultaneous (Tuple-Unpacking) Assignment

Simultaneous assignment evaluates **all** right-hand side expressions before
any binding occurs:

```python
a, b = 1, 2
```

Python builds a tuple `(1, 2)`, then unpacks it, binding `a` to `1` and `b`
to `2`.

The classic swap idiom relies on this guarantee:

```python
x = "left"
y = "right"
x, y = y, x
print(x)  # right
print(y)  # left
```

No temporary variable is needed because the right-hand tuple `(y, x)` is fully
evaluated before the names `x` and `y` are rebound.

Simultaneous assignment also supports nested unpacking:

```python
(a, b), c = (1, 2), 3
print(a, b, c)  # 1 2 3
```

---

## Augmented Assignment

Augmented assignment operators (`+=`, `-=`, `*=`, etc.) combine an operation
with rebinding:

```python
count = 10
count += 5  # equivalent to count = count + 5
print(count)  # 15
```

### Immutable objects

For immutable types like `int`, `float`, and `str`, augmented assignment always
creates a **new object**:

```python
n = 100
original_id = id(n)
n += 1
print(id(n) == original_id)  # False -- n now refers to a new int object
```

### Mutable objects

For mutable types like `list`, augmented assignment may modify the object
**in place** by calling the `__iadd__` method:

```python
items = [1, 2, 3]
original_id = id(items)
items += [4, 5]
print(id(items) == original_id)  # True -- same list, modified in place
```

This matters when multiple names refer to the same object:

```python
a = [1, 2]
b = a
a += [3]
print(b)  # [1, 2, 3] -- b sees the mutation because a and b share the object
```

Compare with plain `+`, which always creates a new object:

```python
a = [1, 2]
b = a
a = a + [3]
print(b)  # [1, 2] -- b still refers to the original list
```

!!! note "The `+=` asymmetry"
    `a += b` and `a = a + b` are **not always equivalent**. For mutable types,
    `+=` mutates in place (and rebinds), while `a = a + b` creates a new object
    and rebinds. For immutable types, both create a new object.

### The tuple-with-list surprise

One of Python's most surprising behaviors involves `+=` on a mutable element inside an immutable container:

```python
t = ([1, 2],)

try:
    t[0] += [3]
except TypeError as e:
    print("Error:", e)

print(t)  # ([1, 2, 3],)
```

This both **raises an error** and **mutates the list**. Why? Because `+=` is a two-step operation:

1. `t[0].__iadd__([3])` --- mutates the list in place (succeeds)
2. `t[0] = result` --- tries to assign back into the tuple (fails)

Step 1 already changed the list before step 2 fails. This demonstrates that `+=` is not an atomic operation.

---

## The Right-Hand Side Is Always Evaluated First

This rule applies to every form of assignment. The right-hand side is fully
evaluated to produce an object (or tuple of objects) before any name binding
happens on the left:

```python
x = 5
x = x * 2 + 1  # RHS evaluates to 11 using the current value of x, then x is rebound
print(x)  # 11
```

This principle guarantees that simultaneous swap works, that augmented
assignment reads the current value before writing, and that chained assignment
evaluates once.

---

## Visualizing Assignment with id()

The built-in `id()` function returns an object's unique identity (its memory
address in CPython). Use it to trace what assignment does:

```python
a = "hello"
print(f"a -> id {id(a)}")

b = a
print(f"b -> id {id(b)}")  # same as a

a = "world"
print(f"a -> id {id(a)}")  # different -- a now points to a new object
print(f"b -> id {id(b)}")  # unchanged -- b still points to "hello"
```

Example output:

```
a -> id 140539436498736
b -> id 140539436498736
a -> id 140539436498800
b -> id 140539436498736
```

Rebinding `a` does not affect `b`. The old object `"hello"` still exists as
long as `b` refers to it.

---

## Summary

| Concept | What happens |
| --- | --- |
| Simple assignment `x = expr` | Evaluate `expr`, bind `x` to the resulting object |
| Chained assignment `a = b = expr` | Evaluate `expr` once, bind both names to the same object |
| Simultaneous assignment `a, b = x, y` | Evaluate all RHS expressions, then bind all LHS names |
| Augmented assignment `x += expr` | Evaluate `expr`, call `__iadd__` (mutable) or `__add__` (immutable), rebind `x` |

The unifying principle: **assignment binds names to objects; it never copies
values into containers.**

---

## Exercises

**Exercise 1.**
Predict the output of the following code. Explain what happens at each
assignment step in terms of object creation and name binding.

```python
a = [10, 20]
b = a
c = a
a = a + [30]
print(a)
print(b)
print(a is b)
print(b is c)
```

??? success "Solution to Exercise 1"
    Output:

    ```text
    [10, 20, 30]
    [10, 20]
    False
    True
    ```

    Step-by-step:

    - `a = [10, 20]` creates a list object and binds `a` to it.
    - `b = a` binds `b` to the same list object. `c = a` binds `c` to the same
      object as well. At this point `a`, `b`, and `c` all share identity.
    - `a = a + [30]` evaluates the right-hand side: `a + [30]` concatenates the
      existing list with `[30]`, producing a **new** list `[10, 20, 30]`. The
      name `a` is then rebound to this new list. The names `b` and `c` still
      refer to the original list `[10, 20]`.
    - `a is b` is `False` because `a` now points to the new list.
    - `b is c` is `True` because both still point to the original list.

---

**Exercise 2.**
A colleague claims that `x += [4]` and `x = x + [4]` are interchangeable when
`x` is a list. Write a short program that demonstrates they are **not**
equivalent. Your program should use a second name that shares the same list
object and print results showing the difference.

??? success "Solution to Exercise 2"
    ```python
    # Demonstrating that += and + differ for lists

    # Case 1: augmented assignment (+=)
    a = [1, 2, 3]
    b = a
    a += [4]
    print("After a += [4]:")
    print(f"  a = {a}")       # [1, 2, 3, 4]
    print(f"  b = {b}")       # [1, 2, 3, 4]
    print(f"  a is b: {a is b}")  # True

    # Case 2: concatenation assignment (= ... +)
    a = [1, 2, 3]
    b = a
    a = a + [4]
    print("After a = a + [4]:")
    print(f"  a = {a}")       # [1, 2, 3, 4]
    print(f"  b = {b}")       # [1, 2, 3]
    print(f"  a is b: {a is b}")  # False
    ```

    In Case 1, `+=` calls `list.__iadd__`, which extends the list in place and
    rebinds `a` to the same object. Since `b` shares that object, `b` sees the
    change. In Case 2, `a + [4]` creates a brand-new list. The name `a` is
    rebound to the new list, leaving `b` still pointing at the original
    unchanged list.

---

**Exercise 3.**
Using simultaneous assignment, write a single line of code that rotates three
variables so that the value in `a` moves to `b`, the value in `b` moves to
`c`, and the value in `c` moves to `a`. Start with `a, b, c = 1, 2, 3` and
print the result. Explain why this works without a temporary variable.

??? success "Solution to Exercise 3"
    ```python
    a, b, c = 1, 2, 3
    a, b, c = c, a, b
    print(a, b, c)  # 3 1 2
    ```

    The right-hand side `c, a, b` is fully evaluated **before** any name
    binding occurs on the left. Python builds the tuple `(3, 1, 2)` using the
    current values of `c`, `a`, and `b`. Only then does it unpack this tuple,
    binding `a` to `3`, `b` to `1`, and `c` to `2`. Because evaluation and
    binding are separate phases, no temporary variable is needed and no value
    is lost during the rotation.
