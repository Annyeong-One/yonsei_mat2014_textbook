
# Mutable Default Arguments

## The Mental Model

When Python encounters a `def` statement, it does two things: it compiles the function body into a code object, and it **evaluates the default argument expressions exactly once**. The resulting objects are stored inside the function object itself and reused on every subsequent call. For immutable defaults like integers or strings, this is harmless---each call gets the same unchangeable value. But for mutable defaults like lists or dictionaries, every call that uses the default shares **the same object in memory**. Mutations accumulate silently across calls.

This is not a bug in Python. It is a direct consequence of the rule that default values are evaluated at **definition time**, not at **call time**.

## The Trap in Action

Consider a function that collects items into a list:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

A programmer might expect each call to start with a fresh empty list. Instead:

```python
print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['apple', 'banana']
print(add_item("cherry"))  # ['apple', 'banana', 'cherry']
```

The list `['apple']` from the first call is the **same object** that receives `'banana'` on the second call. The default `[]` was created once when `def` executed, and every call that omits `items` shares that single list.

## Why This Happens

Python functions are first-class objects. When the interpreter executes `def add_item(item, items=[]):`, it:

1. Evaluates the expression `[]`, producing a new empty list object.
2. Stores a reference to that list in `add_item.__defaults__`.
3. On each call where `items` is not provided, binds the parameter `items` to the object already stored in `__defaults__`.

You can inspect this directly:

```python
def add_item(item, items=[]):
    items.append(item)
    return items

add_item("apple")
add_item("banana")

print(add_item.__defaults__)  # (['apple', 'banana'],)
```

The tuple `__defaults__` holds a reference to the **same list** that the function body mutates. The default is not "regenerated" on each call---it is looked up.

## Verifying with id()

The built-in `id()` function returns the memory address of an object. Using it confirms that every call receives the same default list:

```python
def append_to(item, target=[]):
    print(f"id(target) = {id(target)}")
    target.append(item)
    return target

append_to(1)  # id(target) = 140234567890
append_to(2)  # id(target) = 140234567890  (same address)
append_to(3)  # id(target) = 140234567890  (same address)
```

All three calls print the same `id`, confirming they operate on a single shared list object.

When an explicit argument is passed, a **different** object is used:

```python
my_list = [10, 20]
append_to(30, my_list)  # id(target) = <different address>
```

## The None Sentinel Pattern

The standard fix replaces the mutable default with `None` and creates a fresh object inside the function body:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

Now each call that omits `items` gets a **new** empty list:

```python
print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['banana']
print(add_item("cherry"))  # ['cherry']
```

The test `items is None` uses identity comparison (`is`), not equality (`==`). This is both faster and more precise---it checks whether `items` is literally the `None` singleton, not merely something that happens to equal `None`.

The same pattern applies to dictionaries and sets:

```python
def register(name, registry=None):
    if registry is None:
        registry = {}
    registry[name] = True
    return registry

def collect_unique(value, seen=None):
    if seen is None:
        seen = set()
    seen.add(value)
    return seen
```

## When Mutable Defaults Are Intentional

In rare cases, a mutable default is used **on purpose** as a simple cache or memo:

```python
def fibonacci(n, cache={0: 0, 1: 1}):
    if n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]

print(fibonacci(10))  # 55
```

The shared dictionary `cache` persists between calls, which is exactly the desired behavior here. This technique is uncommon and should be documented clearly when used, because it violates the expectation that default arguments are "fresh" each time.

## Summary

| Concept | Detail |
|---|---|
| When defaults are evaluated | Once, at `def` execution time |
| Where defaults are stored | `function.__defaults__` tuple |
| Why mutable defaults cause bugs | All calls share the same mutable object |
| Standard fix | Use `None` as default, create fresh object in body |
| How to verify | `id()` shows same address across calls |

## Exercises

**Exercise 1.**
Without running the code, predict the output of the following program. Then explain **why** each call produces that result.

```python
def make_row(value, row=[]):
    row.append(value)
    return row

r1 = make_row(1)
r2 = make_row(2)
r3 = make_row(3, [10])

print(r1)
print(r2)
print(r3)
print(r1 is r2)
```

??? success "Solution to Exercise 1"
    Output:

    ```text
    [1, 2]
    [1, 2]
    [10, 3]
    True
    ```

    `r1 = make_row(1)`: The default list `[]` is used. After appending, the default list becomes `[1]`. `r1` is bound to this list.

    `r2 = make_row(2)`: The same default list (now `[1]`) is used again. After appending, it becomes `[1, 2]`. `r2` is bound to the **same** list object.

    Since `r1` and `r2` reference the same object, printing `r1` now also shows `[1, 2]`---the mutation from the second call is visible through `r1`.

    `r3 = make_row(3, [10])`: An explicit list `[10]` is passed, so the default is not used. After appending, `r3` is `[10, 3]`. This does not affect the default list.

    `r1 is r2` is `True` because both names point to the same default list object.

---

**Exercise 2.**
Rewrite the following function to fix the mutable default argument bug. Verify that your fix works by calling the function three times without providing the `log` argument and confirming that each call returns an independent list.

```python
def log_event(event, log=[]):
    log.append(event)
    return log
```

??? success "Solution to Exercise 2"
    Fixed version using the `None` sentinel pattern:

    ```python
    def log_event(event, log=None):
        if log is None:
            log = []
        log.append(event)
        return log
    ```

    Verification:

    ```python
    a = log_event("start")
    b = log_event("stop")
    c = log_event("restart")

    print(a)  # ['start']
    print(b)  # ['stop']
    print(c)  # ['restart']
    print(a is b)  # False
    ```

    Each call creates a new list because `log=None` is immutable, and `if log is None: log = []` executes a fresh list constructor on every call that does not supply an explicit `log` argument. The `id()` values of `a`, `b`, and `c` are all different.

---

**Exercise 3.**
A colleague writes a memoized function using an intentional mutable default:

```python
def square(n, cache={}):
    if n not in cache:
        print(f"Computing {n}^2")
        cache[n] = n * n
    return cache[n]
```

(a) Call `square(3)` twice. How many times does `"Computing 3^2"` print, and why?

(b) How can you inspect the cache after several calls without modifying the function?

(c) What is one risk of this pattern in a long-running application?

??? success "Solution to Exercise 3"
    **(a)** `"Computing 3^2"` prints **once**---on the first call. The second call finds `3` already in `cache` and returns the stored value without recomputing.

    ```python
    square(3)  # prints "Computing 3^2", returns 9
    square(3)  # prints nothing, returns 9
    ```

    The mutable default `cache={}` is shared across all calls. After the first call, `cache` contains `{3: 9}`, so the `if n not in cache` check fails on subsequent calls with `n=3`.

    **(b)** Inspect the cache through `__defaults__`:

    ```python
    square(3)
    square(4)
    square(5)
    print(square.__defaults__)  # ({3: 9, 4: 16, 5: 25},)
    ```

    **(c)** The cache grows without bound. In a long-running application, it will consume increasingly more memory because there is no eviction policy. For production use, `functools.lru_cache` provides a size-limited cache with automatic eviction.
