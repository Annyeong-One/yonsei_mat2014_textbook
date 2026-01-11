# CPython vs Language

## Language Guarantees

### 1. Semantic Behavior

Python's **language specification** defines guaranteed behavior that all implementations must follow:

- Variable assignment creates name-to-object bindings
- Object identity (`id()`) remains constant during object lifetime
- Immutable objects cannot be modified after creation
- Mutable objects can be modified in-place

```python
# Guaranteed: identity stability
x = [1, 2, 3]
original_id = id(x)
x.append(4)
assert id(x) == original_id  # Always True
```

### 2. Implementation Freedom

Language spec allows freedom in:

- Memory layout and allocation strategies
- Garbage collection algorithms
- Optimization techniques
- Internal data structures

## CPython Specifics

### 1. Reference Counting

⚙️ **CPython-specific**: Uses reference counting as primary memory management

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # CPython: shows refcount
# PyPy, Jython: may use different GC
```

### 2. Integer Caching

⚙️ **CPython-specific**: Caches integers in range `[-5, 256]`

```python
a = 42
b = 42
print(a is b)  # True in CPython (cached)

a = 257
b = 257
print(a is b)  # May be False (not guaranteed)
```

### 3. GIL Implementation

⚙️ **CPython-specific**: Single-threaded bytecode execution

```python
import threading

# CPython: threads don't run Python code in parallel
# PyPy/Jython: may have different threading models
```

## Key Distinctions

### 1. What's Guaranteed

| Aspect | Language Guarantee | Example |
|--------|-------------------|---------|
| Equality | `==` compares values | `[1,2] == [1,2]` → True |
| Identity | `is` checks object identity | Behavior defined |
| Mutability | Types have fixed mutability | `list` always mutable |
| Assignment | Creates name binding | Defined semantics |

### 2. What's Not

| Aspect | CPython Behavior | Other Implementations |
|--------|-----------------|---------------------|
| `id()` value | Memory address | May be different |
| Small int caching | `[-5, 256]` | May cache differently |
| String interning | Automatic for some | May vary |
| `is` for literals | Often True | Implementation-dependent |

## Practical Implications

### 1. Write Portable Code

```python
# Good: relies on language guarantees
if x == y:  # Value comparison
    pass

# Bad: relies on CPython specifics
if id(x) < id(y):  # Memory address comparison
    pass
```

### 2. Use `is` Correctly

```python
# Good: singleton comparison
if x is None:
    pass

# Bad: relying on implementation detail
if x is 42:  # Works in CPython, not guaranteed
    pass
```

### 3. Debug Carefully

```python
import sys

# CPython-specific debugging
def debug_refcount(obj):
    # Only works in CPython
    return sys.getrefcount(obj)
```

## Documentation Tags

When documenting behavior:

- **Language-level**: Guaranteed across all implementations
- **⚙️ CPython**: Specific to CPython implementation
- **Implementation-dependent**: May vary

```python
# Language-level: guaranteed
x = [1, 2]
x.append(3)  # Always works

# ⚙️ CPython: implementation detail
import sys
sys.getrefcount(x)  # CPython-specific

# Implementation-dependent
a = 1000
b = 1000
# a is b may be True or False
```
