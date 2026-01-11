# Bad Practices

## Shadowing Built-ins

### 1. Common Mistakes

```python
# Really bad!
print(sorted([3, 1, 2]))
sorted = 1  # Shadows built-in!

# Later...
# sorted([3, 1, 2])  # TypeError!
```

### 2. Recovery

```python
# Once shadowed
list = [1, 2, 3]

# Recover
del list
new_list = list(range(5))  # Works
```

### 3. Don't Shadow

```python
# Never shadow:
# list, dict, set, tuple
# str, int, float
# print, input
# len, range
# sum, min, max
# sorted, filter, map
# type, id
```

## Function Shadowing

### 1. Example

```python
def f():
    return 1

f = 100  # Shadows function!
# f()  # TypeError!
```

### 2. Namespace Pollution

```python
# Bad
def count():
    return 42

count = count()  # Now int!
# count()  # TypeError!
```

## Misleading Names

### 1. Wrong Convention

```python
# Bad: looks constant
MAX_SIZE = [1, 2, 3]  # Mutable!

# Better
max_size = [1, 2, 3]
MAX_SIZE = 100  # Constant
```

### 2. Name vs Content

```python
# Bad
count = "not a count"
total = [1, 2, 3]

# Better  
label = "not a count"
numbers = [1, 2, 3]
```

## Single Letter Issues

### 1. Avoid Confusion

```python
# Bad: l looks like 1
l = 1          # Don't use
O = 0          # Don't use
I = 1          # Don't use

# Better
length = 1
offset = 0
index = 1
```

## Prevention

### 1. Check First

```python
import keyword
import builtins

def is_safe_name(name):
    if keyword.iskeyword(name):
        return False
    if hasattr(builtins, name):
        return False
    return name.isidentifier()

print(is_safe_name("user"))   # True
print(is_safe_name("list"))   # False
```

### 2. Use Linters

Tools that catch shadowing:
- pylint
- flake8
- pycodestyle
