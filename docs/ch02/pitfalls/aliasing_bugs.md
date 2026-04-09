
# Aliasing Bugs

## The Mental Model

In Python, variables are **names** that refer to objects, not containers that hold values. When you write `b = a`, you are not copying the data inside `a`---you are making `b` point to the **same object** that `a` already points to. Both names are now **aliases** for one underlying object.

For immutable objects (integers, strings, tuples), aliasing is invisible. You cannot change the object in place, so it does not matter how many names point to it. But for mutable objects (lists, dictionaries, sets), aliasing means that modifying the object through one name silently changes what every other alias sees. This is the root cause of an entire class of bugs.

## List Aliasing

The simplest aliasing bug occurs with a plain assignment:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
```

After `b = a`, both `a` and `b` refer to the same list object. The `append` through `b` mutates that shared object, and the change is visible through `a`. You can confirm the aliasing with `is` and `id()`:

```python
print(a is b)      # True
print(id(a) == id(b))  # True
```

## The Multiplication Trap

A common source of aliasing bugs is using `*` to create nested structures:

```python
grid = [[0]] * 3
print(grid)  # [[0], [0], [0]]

grid[0].append(1)
print(grid)  # [[0, 1], [0, 1], [0, 1]]
```

All three inner lists are the **same object**. The `*` operator does not create three independent copies---it replicates the **reference** three times. Mutating one "row" mutates all of them.

Verify with `id()`:

```python
grid = [[0]] * 3
print(id(grid[0]))  # 140234567890
print(id(grid[1]))  # 140234567890  (same)
print(id(grid[2]))  # 140234567890  (same)
```

The correct way to create independent rows is with a list comprehension:

```python
grid = [[0] for _ in range(3)]

grid[0].append(1)
print(grid)  # [[0, 1], [0], [0]]
```

Each iteration of the comprehension evaluates `[0]` fresh, producing a distinct list object.

## Dictionary and Set Aliasing

The same aliasing behavior applies to all mutable types:

```python
original = {"x": [1, 2]}
alias = original

alias["x"].append(3)
print(original)  # {'x': [1, 2, 3]}
```

And with sets:

```python
s1 = {1, 2, 3}
s2 = s1
s2.add(4)
print(s1)  # {1, 2, 3, 4}
```

In every case, assignment creates an alias, not a copy.

## Function Argument Aliasing

When you pass a mutable object to a function, the parameter becomes an alias for the caller's object. Any in-place mutation inside the function is visible to the caller:

```python
def remove_negatives(numbers):
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            numbers.pop(i)
        else:
            i += 1

data = [3, -1, 4, -2, 5]
remove_negatives(data)
print(data)  # [3, 4, 5]
```

The caller's `data` list is modified because `numbers` inside the function is an alias for the same object. If the caller did not expect this, it is a bug.

## Fixes Using Copying

### Shallow Copy

A **shallow copy** creates a new top-level container, but the elements inside still refer to the same objects:

```python
import copy

a = [1, 2, 3]
b = a.copy()       # or b = list(a) or b = a[:]
b.append(4)
print(a)  # [1, 2, 3]  -- unaffected
print(b)  # [1, 2, 3, 4]
```

For a flat list of immutable elements, a shallow copy is sufficient. But for nested structures, the inner objects are still shared:

```python
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)
print(a)  # [[1, 2, 99], [3, 4]]  -- inner list still aliased
```

### Deep Copy

A **deep copy** recursively copies every nested object, producing a fully independent structure:

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0].append(99)
print(a)  # [[1, 2], [3, 4]]  -- completely independent
print(b)  # [[1, 2, 99], [3, 4]]
```

### Protecting Function Arguments

To prevent a function from modifying the caller's data, copy the argument at the function boundary:

```python
def sorted_without_negatives(numbers):
    working = numbers.copy()  # Shallow copy -- caller's list is safe
    working = [x for x in working if x >= 0]
    working.sort()
    return working

data = [3, -1, 4, -2, 5]
result = sorted_without_negatives(data)
print(data)    # [3, -1, 4, -2, 5]  -- unchanged
print(result)  # [3, 4, 5]
```

## Summary of Copying Methods

| Method | Creates new top-level? | Copies nested objects? | Use when |
|---|---|---|---|
| `b = a` | No (alias) | No | You want both names to share the object |
| `a.copy()` / `list(a)` / `a[:]` | Yes | No (shallow) | Flat structures with immutable elements |
| `copy.deepcopy(a)` | Yes | Yes (recursive) | Nested mutable structures |

## Exercises

**Exercise 1.**
Predict the output of the following code. Explain which names are aliases and which are independent.

```python
x = [10, 20, 30]
y = x
z = x.copy()

y.append(40)
z.append(50)

print(x)
print(y)
print(z)
print(x is y)
print(x is z)
```

??? success "Solution to Exercise 1"
    Output:

    ```text
    [10, 20, 30, 40]
    [10, 20, 30, 40]
    [10, 20, 30, 50]
    True
    False
    ```

    `y = x` makes `y` an alias for the same list as `x`. When `y.append(40)` executes, the shared list becomes `[10, 20, 30, 40]`, visible through both `x` and `y`.

    `z = x.copy()` creates a new, independent list containing the same elements. `z.append(50)` modifies only `z`, producing `[10, 20, 30, 50]`. The original list (referenced by `x` and `y`) is unaffected.

    `x is y` is `True` because they reference the same object. `x is z` is `False` because `z` is a separate object created by `copy()`.

---

**Exercise 2.**
A programmer wants to create a 3x3 grid initialized with zeros. They write:

```python
grid = [[0, 0, 0]] * 3
grid[1][1] = 5
print(grid)
```

(a) What does `print(grid)` output?

(b) Why is the result surprising?

(c) Rewrite the grid creation so that modifying one row does not affect the others.

??? success "Solution to Exercise 2"
    **(a)** Output:

    ```text
    [[0, 5, 0], [0, 5, 0], [0, 5, 0]]
    ```

    **(b)** The `*` operator creates three references to the **same** inner list `[0, 0, 0]`. Setting `grid[1][1] = 5` modifies that single shared list, so the change appears in all three "rows". All three elements of `grid` have the same `id()`.

    **(c)** Use a list comprehension to create independent lists:

    ```python
    grid = [[0, 0, 0] for _ in range(3)]
    grid[1][1] = 5
    print(grid)  # [[0, 0, 0], [0, 5, 0], [0, 0, 0]]
    ```

    Each iteration of the comprehension evaluates `[0, 0, 0]` as a fresh list expression, producing three distinct list objects.

---

**Exercise 3.**
Consider the following code involving nested aliasing:

```python
import copy

original = {"name": "Alice", "scores": [85, 90, 78]}
shallow = original.copy()
deep = copy.deepcopy(original)

shallow["scores"].append(95)
deep["scores"].append(100)
shallow["name"] = "Bob"

print(original["name"])
print(original["scores"])
print(shallow["scores"])
print(deep["scores"])
```

Predict all four lines of output. Explain why `original["name"]` is not changed to `"Bob"` even though `shallow["name"]` was reassigned, but `original["scores"]` **is** affected by the append through `shallow`.

??? success "Solution to Exercise 3"
    Output:

    ```text
    Alice
    [85, 90, 78, 95]
    [85, 90, 78, 95]
    [85, 90, 78, 100]
    ```

    `shallow = original.copy()` creates a new dictionary whose keys map to the **same objects** as `original`. The string `"Alice"` and the list `[85, 90, 78]` are shared.

    `shallow["name"] = "Bob"` is a **rebinding** operation: it changes which object the key `"name"` maps to in `shallow`. It does not mutate the string `"Alice"` (strings are immutable). Since `original` still maps `"name"` to the original string, `original["name"]` remains `"Alice"`.

    `shallow["scores"].append(95)` is a **mutation**: it modifies the list that both `original["scores"]` and `shallow["scores"]` reference. Since both dictionaries share the same list object, the append is visible through both.

    `deep = copy.deepcopy(original)` created a fully independent copy. The list inside `deep` is a separate object, so `deep["scores"].append(100)` only affects `deep`'s copy, producing `[85, 90, 78, 100]` (the original list before the shallow copy's append, plus `100`). Note that `deepcopy` was called before the `append(95)`, so `deep["scores"]` started as `[85, 90, 78]`.
