# Chained Assignment

## Basic Chaining

### 1. Simple Case

```python
a = b = c = 1
print(f"{a = }, {b = }, {c = }")
# a = 1, b = 1, c = 1
```

### 2. Single Object

All names refer to **same object**:

```python
a = b = c = [1, 2, 3]
print(f"{a is b is c = }")  # True
print(f"{id(a) == id(b) == id(c) = }")  # True
```

## Evaluation Order

### 1. Right-to-Left

Expression evaluated right-to-left:

```python
a = b = c = 1 + 2 + 3
# 1. Compute: 1 + 2 + 3 = 6
# 2. Create object: 6
# 3. Assign: c, then b, then a
```

### 2. Bytecode Evidence

```python
import dis

def f():
    a = b = c = 1

dis.dis(f)
```

Shows:
- `LOAD_CONST 1`
- `DUP_TOP` (duplicate)
- `DUP_TOP` (duplicate)
- `STORE_NAME` (c, b, a)

## Shared Mutability

### 1. Lists

```python
x = y = z = [1, 2, 3]

# Modify through one
x.append(4)

# All see change
print(f"{x = }")  # [1, 2, 3, 4]
print(f"{y = }")  # [1, 2, 3, 4]
print(f"{z = }")  # [1, 2, 3, 4]
```

### 2. Dictionaries

```python
a = b = c = {'key': 'value'}

a['new'] = 'data'

print(b)  # {'key': 'value', 'new': 'data'}
print(c)  # {'key': 'value', 'new': 'data'}
```

## Immutable Objects

### 1. No Issue

```python
x = y = z = 42

x = 100  # Rebinds x only

print(f"{x = }")  # x = 100
print(f"{y = }")  # y = 42
print(f"{z = }")  # z = 42
```

### 2. String Example

```python
a = b = c = "hello"

a = "world"  # Rebinds a

print(f"{a = }")  # a = 'world'
print(f"{b = }")  # b = 'hello'
print(f"{c = }")  # c = 'hello'
```

## Best Practices

### 1. Use for Immutables

```python
# Safe: immutable
MAX = DEFAULT = LIMIT = 100
```

### 2. Avoid for Mutables

```python
# Dangerous
x = y = z = []  # Same list!

# Better
x = []
y = []
z = []  # Three lists
```

### 3. Default Arguments

```python
# Don't do this!
def bad(element, target=x=y=[]):
    target.append(element)
    return target

# Better
def good(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target
```

## Identity Checks

### 1. Verify Sharing

```python
a = b = c = [1, 2, 3]

print(f"a is b: {a is b}")
print(f"b is c: {b is c}")
print(f"a is c: {a is c}")
# All True

print(f"IDs: {id(a)}, {id(b)}, {id(c)}")
# All same
```

### 2. Break Sharing

```python
a = b = c = [1, 2, 3]

# Rebind one name
a = [1, 2, 3]  # New object

print(f"a is b: {a is b}")  # False
print(f"b is c: {b is c}")  # True
```

## Use Cases

### 1. Constants

```python
# Good use case
ZERO = NULL = EMPTY = 0
```

### 2. Counters

```python
# Acceptable
wins = losses = draws = 0

wins += 1  # Only affects wins
```

### 3. Coordinates

```python
# OK for numbers
x = y = z = 0.0

# Dangerous for lists
# positions = velocities = [0, 0, 0]
```
