# Common Mistakes

## Mutable Defaults

### 1. The Problem

```python
def append_to(item, lst=[]):
    lst.append(item)
    return lst

print(append_to(1))  # [1]
print(append_to(2))  # [1, 2] - Bug!
```

### 2. The Fix

```python
def append_to(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

## Late Binding

### 1. The Problem

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print([f() for f in funcs])  # [2, 2, 2]
```

### 2. The Fix

```python
funcs = [lambda x=i: x for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]
```

## Shadowing Built-ins

### 1. The Problem

```python
list = [1, 2, 3]
# Later...
# new_list = list(range(5))  # TypeError!
```

### 2. The Fix

```python
# Don't shadow built-ins
items = [1, 2, 3]
```

## Expecting Mutation

### 1. The Problem

```python
x = [1, 2, 3]
x = x + [4, 5]  # New list, not mutation
```

### 2. Use Correct Operator

```python
x += [4, 5]  # Mutates in place
# or
x.extend([4, 5])  # Explicit mutation
```

## Summary

- Watch mutable defaults
- Fix late binding with defaults
- Don't shadow built-ins
- Know mutation vs assignment
