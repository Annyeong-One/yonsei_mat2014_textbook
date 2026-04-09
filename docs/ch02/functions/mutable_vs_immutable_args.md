
# Mutable vs Immutable Arguments

## The Mental Model

When you pass an argument to a function, the function receives a reference to the same object. Whether the function can change that object depends on a single property: **is the object mutable or immutable?**

Think of it as handing someone a document. If the document is written in wet ink on a whiteboard (mutable), they can erase and rewrite parts of it, and you will see the changes when you look at the board. If the document is a printed page (immutable), they cannot alter it. They can write a new page, but your original page remains unchanged.

This distinction is the most practical consequence of Python's call-by-object-reference convention.

## Passing Immutable Arguments

Immutable types include `int`, `float`, `str`, `tuple`, `bool`, `frozenset`, and `None`. When you pass an immutable object to a function, the function **cannot** modify the caller's data. Any operation that appears to change the value actually creates a new object and rebinds the local parameter name.

```python
def double(n):
    print(f"Before: id={id(n)}")
    n = n * 2  # creates a new int, rebinds local name
    print(f"After:  id={id(n)}")
    return n

x = 5
print(f"Caller: id={id(x)}")
result = double(x)
print(f"x = {x}")        # 5 -- unchanged
print(f"result = {result}")  # 10 -- new object
```

Output:

```
Caller: id=140456789
Before: id=140456789
After:  id=140456821
x = 5
result = 10
```

The id changes after `n = n * 2` because a new integer object was created. The caller's `x` still refers to the original object.

### Strings are Immutable

A common surprise for programmers coming from languages where strings are mutable:

```python
def shout(text):
    text = text.upper()  # creates a new string
    text = text + "!!!"  # creates yet another new string
    return text

greeting = "hello"
result = shout(greeting)
print(greeting)  # "hello" -- unchanged
print(result)    # "HELLO!!!"
```

Every string operation returns a **new** string. The original is never modified.

### Tuples are Immutable

```python
def try_modify_tuple(t):
    # t[0] = 99  # would raise TypeError: 'tuple' does not support item assignment
    t = (99, 88, 77)  # rebinds the local name
    return t

coords = (1, 2, 3)
new_coords = try_modify_tuple(coords)
print(coords)      # (1, 2, 3) -- unchanged
print(new_coords)  # (99, 88, 77)
```

## Passing Mutable Arguments

Mutable types include `list`, `dict`, `set`, and most user-defined objects. When you pass a mutable object to a function, the function **can** modify the caller's data through in-place operations.

### Lists

```python
def remove_negatives(numbers):
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            numbers.pop(i)
        else:
            i += 1

data = [3, -1, 4, -5, 9]
remove_negatives(data)
print(data)  # [3, 4, 9] -- modified in place
```

The function directly modifies the list that `data` refers to. No return value is needed because the caller's object has been changed.

### Dictionaries

```python
def add_defaults(config):
    config.setdefault("timeout", 30)
    config.setdefault("retries", 3)
    config.setdefault("verbose", False)

settings = {"timeout": 60}
add_defaults(settings)
print(settings)
# {'timeout': 60, 'retries': 3, 'verbose': False}
```

The function modifies the caller's dictionary. Note that `"timeout"` keeps its original value of `60` because `setdefault` only sets a key if it is not already present.

### Sets

```python
def add_vowels(s):
    s.update("aeiou")

letters = {"x", "y", "z"}
add_vowels(letters)
print(letters)  # {'a', 'e', 'i', 'o', 'u', 'x', 'y', 'z'}
```

## Common Surprises

### Surprise 1: Augmented Assignment on Immutable Types

```python
def increment(n):
    n += 1  # equivalent to n = n + 1 for int (immutable)

counter = 10
increment(counter)
print(counter)  # 10 -- unchanged!
```

For immutable types, `+=` creates a new object and rebinds the local name. The caller's variable is unaffected.

### Surprise 2: Augmented Assignment on Mutable Types

```python
def extend_list(lst):
    lst += [4, 5, 6]  # equivalent to lst.__iadd__([4, 5, 6]) -- in-place!

data = [1, 2, 3]
extend_list(data)
print(data)  # [1, 2, 3, 4, 5, 6] -- changed!
```

For lists, `+=` calls `__iadd__`, which modifies the list in place **and** rebinds the name. The mutation is visible to the caller.

This asymmetry is a frequent source of bugs:

| Type | `x += value` equivalent | Mutates in place? |
| --- | --- | --- |
| `int` | `x = x + value` | No (creates new int) |
| `str` | `x = x + value` | No (creates new str) |
| `list` | `x.__iadd__(value)` | Yes |
| `dict` | `x.update(value)` (via `\|=`) | Yes |

### Surprise 3: Rebinding Looks Like Mutation But Is Not

```python
def clear_wrong(lst):
    lst = []  # rebinds local name to a new empty list

def clear_right(lst):
    lst.clear()  # mutates the existing list

data = [1, 2, 3]
clear_wrong(data)
print(data)  # [1, 2, 3] -- NOT cleared

data = [1, 2, 3]
clear_right(data)
print(data)  # [] -- cleared
```

`lst = []` creates a new list and makes the local name point to it. The caller's list is untouched. `lst.clear()` modifies the existing object.

### Surprise 4: Mutable Objects Inside Immutable Containers

A tuple is immutable, but if it contains a mutable object (like a list), the mutable object can still be changed:

```python
def modify_inner(t):
    t[1].append(99)  # the list inside the tuple is mutable

data = (1, [2, 3], 4)
modify_inner(data)
print(data)  # (1, [2, 3, 99], 4) -- the list inside was mutated
```

The tuple itself was not modified (its references are the same), but the list it contains was.

## Defensive Patterns

When you want to prevent a function from modifying the caller's data, pass a copy:

```python
def process(items):
    items.sort()  # sorts in place
    return items[0]

original = [3, 1, 4, 1, 5]
smallest = process(original[:])  # pass a shallow copy
print(original)  # [3, 1, 4, 1, 5] -- preserved
print(smallest)  # 1
```

Common copying techniques:

```python
# Lists
copy_list = original_list[:]
copy_list = list(original_list)

# Dictionaries
copy_dict = original_dict.copy()
copy_dict = dict(original_dict)

# General (shallow copy)
import copy
shallow = copy.copy(original)

# General (deep copy -- for nested structures)
deep = copy.deepcopy(original)
```

---

## Exercises

**Exercise 1.**
Predict the output of the following code. Explain each result in terms of mutability and rebinding.

```python
def process(a, b, c):
    a = a + [4]
    b += [4]
    c.append(4)

x = [1, 2, 3]
y = [1, 2, 3]
z = [1, 2, 3]
process(x, y, z)
print(x)
print(y)
print(z)
```

Why do `x`, `y`, and `z` end up with different values despite all three starting as `[1, 2, 3]`?

??? success "Solution to Exercise 1"
    Output:

    ```text
    [1, 2, 3]
    [1, 2, 3, 4]
    [1, 2, 3, 4]
    ```

    - `a = a + [4]`: The `+` operator on lists creates a **new** list. The local name `a` is rebound to this new list. The caller's `x` is unaffected. Result: `x = [1, 2, 3]`.
    - `b += [4]`: For lists, `+=` calls `__iadd__`, which extends the list **in place** and then rebinds the name. The in-place modification is visible to the caller. Result: `y = [1, 2, 3, 4]`.
    - `c.append(4)`: This is a direct mutation of the shared object. The caller's `z` sees the change. Result: `z = [1, 2, 3, 4]`.

    The difference between `a + [4]` (creates new list) and `a += [4]` (modifies in place) is one of the most common sources of confusion in Python.

---

**Exercise 2.**
A junior developer writes this function to "safely" remove duplicates from a list:

```python
def remove_duplicates(items):
    items = list(set(items))

data = [1, 2, 2, 3, 3, 3]
remove_duplicates(data)
print(data)
```

The output is `[1, 2, 2, 3, 3, 3]` -- the duplicates are still there. Explain why this does not work and provide two different ways to fix it: one that modifies the list in place and one that returns a new list.

??? success "Solution to Exercise 2"
    The function fails because `items = list(set(items))` is a **rebinding** operation. It creates a new list from the set and assigns it to the local name `items`. The caller's `data` still refers to the original list.

    **Fix 1: Modify in place**

    ```python
    def remove_duplicates(items):
        seen = set()
        i = 0
        while i < len(items):
            if items[i] in seen:
                items.pop(i)
            else:
                seen.add(items[i])
                i += 1

    data = [1, 2, 2, 3, 3, 3]
    remove_duplicates(data)
    print(data)  # [1, 2, 3]
    ```

    Or more concisely using slice assignment:

    ```python
    def remove_duplicates(items):
        items[:] = list(dict.fromkeys(items))  # preserves order, modifies in place

    data = [1, 2, 2, 3, 3, 3]
    remove_duplicates(data)
    print(data)  # [1, 2, 3]
    ```

    **Fix 2: Return a new list**

    ```python
    def remove_duplicates(items):
        return list(dict.fromkeys(items))

    data = [1, 2, 2, 3, 3, 3]
    data = remove_duplicates(data)
    print(data)  # [1, 2, 3]
    ```

    The second approach is generally preferred because it makes data flow explicit through the return value.

---

**Exercise 3.**
Consider this code where a tuple contains a mutable list:

```python
def modify(data):
    data[0] += 1
    data[1].append(99)

t = (10, [20, 30])
modify(t)
```

Predict what happens. Does the function succeed, raise an error, or partially succeed? What is the final value of `t`? Explain why a tuple can "seem to change" even though tuples are immutable.

??? success "Solution to Exercise 3"
    This code raises a `TypeError`, but **partially succeeds**. The final value of `t` is `(10, [20, 30, 99])`.

    Step-by-step:

    - `data[0] += 1`: This attempts `data[0] = data[0] + 1`, which tries to assign `11` to index 0 of the tuple. Tuples do not support item assignment, so this raises `TypeError`. But wait -- this is actually the first line and it does raise an error. So `data[1].append(99)` never executes.

    Let us reconsider. The line `data[0] += 1` is equivalent to `data[0] = data[0] + 1`. Since `data` is a tuple, `data[0] = ...` raises `TypeError`. The second line never runs.

    The final value of `t` is `(10, [20, 30])` -- unchanged.

    Now consider if the lines were reversed:

    ```python
    def modify(data):
        data[1].append(99)  # succeeds -- mutates the list inside the tuple
        data[0] += 1        # raises TypeError

    t = (10, [20, 30])
    try:
        modify(t)
    except TypeError:
        pass
    print(t)  # (10, [20, 30, 99])
    ```

    Here the list mutation succeeds (because we are modifying the list object, not the tuple), and then the tuple assignment fails. The tuple "appears to change" because the list **inside** it was mutated. The tuple's references did not change -- index 1 still refers to the same list object -- but that object's contents changed.

    This demonstrates that immutability of a container only means its references cannot change. The objects those references point to can still be mutable and can still be modified.
