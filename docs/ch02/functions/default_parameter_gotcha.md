# Default Parameter Gotcha

One of Python's most infamous pitfalls is using mutable objects as default parameter values. This section explains why it happens and how to avoid it.


## The Problem

```python
def append_to(item, target=[]):
    target.append(item)
    return target

print(append_to(1))  # [1]
print(append_to(2))  # [1, 2] - Wait, what?
print(append_to(3))  # [1, 2, 3] - It keeps growing!
```

Expected: Each call returns a new list with one item.
Actual: The same list is reused and accumulates items.


## Why This Happens

**Default values are evaluated once, at function definition time, not at call time.**

```python
def append_to(item, target=[]):
    target.append(item)
    return target
```

When Python executes this `def` statement:
1. It creates the function object
2. It evaluates `[]` to create a list object
3. It stores that list object as the default value

Every call that doesn't provide `target` uses that same list object.

```python
# Proof: default value has a persistent identity
def show_default(x=[]):
    print(f"id of default: {id(x)}")
    return x

show_default()  # id: 140234567890
show_default()  # id: 140234567890 (same!)
show_default()  # id: 140234567890 (same!)
```


## Visualizing the Problem

```python
def append_to(item, target=[]):
    target.append(item)
    return target
```

```
After function definition:
┌─────────────────────────────────┐
│ append_to function object       │
│   defaults: ([ ],)  ───────────►│ list object []
└─────────────────────────────────┘

After append_to(1):
┌─────────────────────────────────┐
│ append_to function object       │
│   defaults: ([ ],)  ───────────►│ list object [1]
└─────────────────────────────────┘

After append_to(2):
┌─────────────────────────────────┐
│ append_to function object       │
│   defaults: ([ ],)  ───────────►│ list object [1, 2]
└─────────────────────────────────┘
```


## Inspecting Default Values

You can see default values stored in `__defaults__`:

```python
def append_to(item, target=[]):
    target.append(item)
    return target

print(append_to.__defaults__)  # ([],)

append_to(1)
print(append_to.__defaults__)  # ([1],)

append_to(2)
print(append_to.__defaults__)  # ([1, 2],)
```


## The Solution: Use None as Default

The standard pattern is to use `None` as the default and create the mutable object inside the function.

```python
def append_to(item, target=None):
    if target is None:
        target = []  # Create new list each time
    target.append(item)
    return target

print(append_to(1))  # [1]
print(append_to(2))  # [2] - Correct!
print(append_to(3))  # [3] - Correct!
```

Each call creates a fresh list when `target` is not provided.


## Other Mutable Defaults to Avoid

The issue applies to all mutable objects:

### Lists

```python
# Bad
def add_user(user, users=[]):
    users.append(user)
    return users

# Good
def add_user(user, users=None):
    if users is None:
        users = []
    users.append(user)
    return users
```

### Dictionaries

```python
# Bad
def record_event(event, log={}):
    log[event] = True
    return log

# Good
def record_event(event, log=None):
    if log is None:
        log = {}
    log[event] = True
    return log
```

### Sets

```python
# Bad
def add_tag(tag, tags=set()):
    tags.add(tag)
    return tags

# Good
def add_tag(tag, tags=None):
    if tags is None:
        tags = set()
    tags.add(tag)
    return tags
```


## When Explicit Argument is Passed

When you explicitly pass an argument, it works correctly:

```python
def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target

my_list = [1, 2, 3]
result = append_to(4, my_list)
print(result)    # [1, 2, 3, 4]
print(my_list)   # [1, 2, 3, 4] - Same object, mutated
```


## Intentional Use of Mutable Defaults

Sometimes mutable defaults are used intentionally for caching:

```python
def fibonacci(n, cache={0: 0, 1: 1}):
    if n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]

print(fibonacci(10))  # 55
print(fibonacci(50))  # Fast! Uses cached values
```

This works because the cache persists between calls. However, this pattern:
- Is confusing to readers
- Makes testing difficult
- Is better replaced with `@functools.lru_cache`

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```


## Class Method Gotcha

The same issue occurs with class methods:

```python
class Logger:
    # Bad: shared across all instances!
    def __init__(self, messages=[]):
        self.messages = messages
    
    def log(self, msg):
        self.messages.append(msg)

log1 = Logger()
log2 = Logger()

log1.log("From log1")
print(log2.messages)  # ["From log1"] - Oops!
```

**Fix**:

```python
class Logger:
    def __init__(self, messages=None):
        if messages is None:
            messages = []
        self.messages = messages
```


## Instance-Dependent Default Values

Another related gotcha: using `self` in default parameter values.

```python
class Simulator:
    def __init__(self, duration):
        self.duration = duration
    
    # ERROR: self doesn't exist at definition time
    def run(self, steps=self.duration * 10):  # NameError
        pass
```

**Fix**: Use `None` and resolve inside the method.

```python
class Simulator:
    def __init__(self, duration):
        self.duration = duration
    
    def run(self, steps=None):
        if steps is None:
            steps = self.duration * 10
        # ... rest of method
```


## Quick Reference

| Default Type | Safe? | Example |
|--------------|-------|---------|
| `None` | ✅ | `def f(x=None)` |
| `int`, `float` | ✅ | `def f(x=0)` |
| `str` | ✅ | `def f(x="")` |
| `tuple` | ✅ | `def f(x=())` |
| `bool` | ✅ | `def f(x=False)` |
| `list` | ❌ | `def f(x=[])` |
| `dict` | ❌ | `def f(x={})` |
| `set` | ❌ | `def f(x=set())` |
| Custom objects | ❌ | `def f(x=MyClass())` |


## Summary

1. **Default values are evaluated once** at function definition, not at each call
2. **Mutable defaults persist** and are shared across all calls
3. **Use `None` as default** for mutable arguments
4. **Create the mutable object inside** the function body
5. **This applies to** lists, dicts, sets, and custom objects
