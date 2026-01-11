# Mutation vs Assignment

## Core Difference

### 1. Assignment

Creates new binding:

```python
x = [1, 2, 3]
x = [4, 5, 6]       # New object
```

### 2. Mutation

Modifies existing:

```python
x = [1, 2, 3]
x.append(4)         # Same object
```

## With Immutables

### 1. No Mutation

```python
x = "hello"
# x[0] = "H"        # TypeError

x = "H" + x[1:]     # Must assign
```

## With Mutables

### 1. Mutation Methods

```python
lst = [1, 2, 3]
lst.append(4)
lst.extend([5, 6])
lst.insert(0, 0)
```

### 2. Assignment

```python
lst = [1, 2, 3]
lst = lst + [4, 5]  # New object
```

## Operators

### 1. += Different

```python
# Immutable: new
x = "hello"
x += " world"

# Mutable: in-place
lst = [1, 2]
lst += [3, 4]       # Same object
```

### 2. + Always New

```python
lst = [1, 2]
lst = lst + [3, 4]  # New object
```

## Shared References

### 1. Assignment Safe

```python
a = [1, 2, 3]
b = a
a = [4, 5, 6]

print(b)            # [1, 2, 3]
```

### 2. Mutation Affects All

```python
a = [1, 2, 3]
b = a
a.append(4)

print(b)            # [1, 2, 3, 4]
```

## Function Parameters

### 1. Reassignment

```python
def reassign(lst):
    lst = [4, 5, 6]

original = [1, 2, 3]
reassign(original)
print(original)     # [1, 2, 3]
```

### 2. Mutation

```python
def mutate(lst):
    lst.append(4)

original = [1, 2, 3]
mutate(original)
print(original)     # [1, 2, 3, 4]
```

## Comparison

| Operation | Mutation? | New Object? |
|-----------|-----------|-------------|
| `x = y` | No | No |
| `x.append(3)` | Yes | No |
| `x += [3]` | Yes | No |
| `x = x + [3]` | No | Yes |

## Summary

### 1. Assignment

- Binds name to object
- Changes reference
- Original unaffected

### 2. Mutation

- Modifies in place
- Same identity
- Affects all refs
