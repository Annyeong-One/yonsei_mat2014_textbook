# Identity Stability


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Object Identity

### 1. Constant ID

```python
x = [1, 2, 3]
original_id = id(x)

# Modify object
x.append(4)
x.extend([5, 6])
x[0] = 100

# ID unchanged
print(id(x) == original_id)  # True
```

### 2. New Object

```python
x = [1, 2, 3]
original_id = id(x)

# Create new object
x = [1, 2, 3]

# Different ID
print(id(x) != original_id)  # True
```

## Mutation

### 1. Preserves Identity

```python
lst = [1, 2, 3]
id1 = id(lst)

# All preserve identity
lst.append(4)
lst.extend([5, 6])
lst.insert(0, 0)
lst.remove(2)
lst.pop()
lst.sort()
lst.reverse()

print(id(lst) == id1)  # True
```

### 2. Immutables

```python
x = "hello"
id1 = id(x)

# Must create new
x = x + " world"

print(id(x) != id1)  # True
```

## References

### 1. Shared Identity

```python
a = [1, 2, 3]
b = a
c = a

# All same ID
print(id(a) == id(b) == id(c))  # True
```

### 2. Independent IDs

```python
a = [1, 2, 3]
b = [1, 2, 3]

# Different IDs
print(id(a) != id(b))  # True
```

## Guarantees

### 1. Language Level

```python
# Guaranteed: identity stable
x = [1, 2, 3]
x.append(4)
# Same object

# Guaranteed: mutation visible
y = x
x.append(5)
# y sees change
```

## Summary

### 1. Identity

- Unique per object
- Never changes
- Check with `is`

### 2. Operations

- Mutation: same ID
- Assignment: new ID
- Immutables: always new
