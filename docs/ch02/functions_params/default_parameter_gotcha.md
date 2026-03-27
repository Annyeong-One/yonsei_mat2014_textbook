# Default Parameter Gotcha

One of Python's most common pitfalls is using a mutable object as a default parameter value.

## The Problem

```python
def append_to(item, target=[]):
    target.append(item)
    return target

print(append_to(1))  # [1]
print(append_to(2))  # [1, 2]  — wait, what?
print(append_to(3))  # [1, 2, 3]  — it keeps growing!
```

Expected: each call returns a fresh list with one item.
Actual: the same list is reused and accumulates items across every call.

## Why This Happens

**Default values are evaluated once, at function definition time — not at each call.**

When Python executes the `def` statement it creates the function object, evaluates `[]` to produce a list, and stores that list as the default. Every call that omits `target` reuses that same list object.

```python
def append_to(item, target=[]):
    target.append(item)
    return target

print(append_to.__defaults__)   # ([],)
append_to(1)
print(append_to.__defaults__)   # ([1],)
append_to(2)
print(append_to.__defaults__)   # ([1, 2],)
```

### What happens in memory

When Python executes the `def` statement it performs three steps:

1. Creates a function object at a fixed address in virtual memory
2. Evaluates each default expression — `[]` produces a list object at its own fixed address
3. Stores that address inside the function object as part of `__defaults__`

That address is **fixed for the entire lifetime of the function**. Every call that omits the argument receives the object at that same address — not a fresh one.

```python
def append_to(item, target=[]):
    target.append(item)
    return target

# The function object lives at a fixed address
print(hex(id(append_to)))                      # e.g. 0x7f3a1c2b4d30

# The default list lives at a fixed address inside it
print(hex(id(append_to.__defaults__[0])))      # e.g. 0x7f3a1c2b4e50

append_to(1)
append_to(2)

# Same address — same object — now contains [1, 2]
print(hex(id(append_to.__defaults__[0])))      # 0x7f3a1c2b4e50 — unchanged
print(append_to.__defaults__)                  # ([1, 2],)
```

With `None` as the default, `None` is an immutable singleton — its address never changes and it can never accumulate state. The new list created inside the function body gets a **fresh address on every call**:

```python
def append_to(item, target=None):
    if target is None:
        target = []    # New object, new address, created on this call only
    target.append(item)
    return target

# Each call with no argument creates a brand-new list
r1 = append_to(1)
r2 = append_to(2)
print(hex(id(r1)), hex(id(r2)))   # Different addresses — different objects
print(r1)  # [1]
print(r2)  # [2]
```

Visualized:

```
After function definition:
  append_to object (0x...F)
    __defaults__ ──────► list object (0x...L) = []

After append_to(1):
  append_to object (0x...F)          ← same function, same address
    __defaults__ ──────► list object (0x...L) = [1]   ← same list, mutated

After append_to(2):
  append_to object (0x...F)          ← same function, same address
    __defaults__ ──────► list object (0x...L) = [1, 2] ← same list, mutated again

With None sentinel — each call:
  append_to object (0x...F)
    __defaults__ ──────► None (0x...N)    ← fixed, immutable singleton
  inside the call:
    target ──────► new list (0x...X)      ← fresh address every time
```

## The Fix: Use None as Default

The standard pattern is to use `None` as the sentinel and create the mutable object inside the function body.

```python
def append_to(item, target=None):
    if target is None:
        target = []       # New list created on each call
    target.append(item)
    return target

print(append_to(1))  # [1]
print(append_to(2))  # [2]  — correct
print(append_to(3))  # [3]  — correct
```

This pattern appeared in [Parameter Passing](parameter_passing.md) (Pattern 3). Now you know why `output=[]` is never written directly.

The rule applies to all mutable defaults — lists, dicts, and sets:

```python
# Bad
def record(event, log={}): ...
def tag(item, tags=set()): ...

# Good
def record(event, log=None):
    if log is None:
        log = {}
    ...

def tag(item, tags=None):
    if tags is None:
        tags = set()
    ...
```

## Augmented Assignment Gotcha

`+=` behaves differently for mutable and immutable types, which interacts with this topic.

For immutable types, `+=` creates a new object and rebinds the name — the default is not affected:

```python
def add_to_tuple(t=()):
    t += (4,)   # Creates a NEW tuple, rebinds local t
    return t

print(add_to_tuple())   # (4,)
print(add_to_tuple())   # (4,)  — correct, fresh each time
```

For mutable types, `+=` calls `__iadd__` which mutates the object in place — the default accumulates:

```python
def add_to_list(lst=[]):
    lst += [4]   # Mutates the SAME list (equivalent to lst.extend([4]))
    return lst

print(add_to_list())   # [4]
print(add_to_list())   # [4, 4]  — accumulating again
```

The fix is the same: use `None` as the default.

## Aliasing Confusion

Passing the same mutable object as two separate arguments can cause surprising results:

```python
def process(a, b):
    a.append(1)
    b.append(2)

x = [0]
process(x, x)   # Both a and b point to the same list
print(x)        # [0, 1, 2]
```

Both parameters reference `x`, so both mutations affect the same object. This is rarely intentional — always pass distinct objects when a function expects independent arguments.

## Intentional Use: Caching

Mutable defaults are occasionally used deliberately for simple caching:

```python
def fibonacci(n, cache={0: 0, 1: 1}):
    if n not in cache:
        cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]
```

The cache persists across calls by design. However this pattern is hard to test and reset. The idiomatic replacement is `@functools.lru_cache`:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

The `@` syntax is a *decorator* — covered in a later chapter. For now, read it as a way to attach caching behavior to a function.

## Class Method Gotcha

!!! note "Requires knowledge of classes"
    This section uses `class` and `__init__`, which are introduced in a later chapter. Feel free to skip and return here once classes are familiar.

The same issue occurs in `__init__`:

```python
class Logger:
    def __init__(self, messages=[]):   # Shared across ALL instances
        self.messages = messages

log1 = Logger()
log2 = Logger()
log1.messages.append("hello")
print(log2.messages)   # ["hello"]  — unintended sharing
```

Fix:

```python
class Logger:
    def __init__(self, messages=None):
        self.messages = messages if messages is not None else []
```

## Key Ideas

Default parameter values are evaluated once when the `def` statement runs, not each time the function is called.
Any mutable default — list, dict, set, or custom object — will be shared and mutated across all calls that omit that argument.
The fix is always the same: default to `None` and create the mutable object inside the function body.
