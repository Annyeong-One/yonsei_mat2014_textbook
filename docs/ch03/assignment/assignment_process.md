# Assignment Process

Understanding how Python executes assignment statements and binds names to objects.

## Assignment Steps

When Python executes an assignment statement, it follows these steps:

### Step 1: Evaluate the Right-Hand Side (RHS)

The expression on the right side is evaluated first:

```python
x = 2 + 3
# 1. Evaluate 2 + 3 → 5
# 2. Bind x to 5
```

```python
y = len([1, 2, 3]) * 2
# 1. Evaluate len([1, 2, 3]) → 3
# 2. Evaluate 3 * 2 → 6
# 3. Bind y to 6
```

### Step 2: Create/Update Binding

The name is bound to the resulting object in the appropriate namespace:

```python
x = 42  # Creates binding in local namespace
# Equivalent to: locals()['x'] = 42
```

## Binding Semantics

### Name Binding

Assignment creates a binding from a name to an object:

```python
x = 42
# Creates/updates binding
# x → 42 object (integer)
```

The name `x` is now a reference to the integer object `42`.

### Rebinding

Assigning to an existing name creates a new binding:

```python
x = 42
x = "hello"  # x now refers to a different object
```

The old object (`42`) is not modified—`x` simply points to a new object.

## Multiple Assignment

### Tuple Unpacking

```python
a, b = 1, 2
# Equivalent to:
# temp = (1, 2)
# a = temp[0]
# b = temp[1]
```

### Chained Assignment

```python
x = y = z = 0
# All three names bound to the same object
print(x is y is z)  # True
```

### Swap Values

```python
a, b = b, a
# RHS evaluated first: (b, a) tuple created
# Then unpacked to a, b
```

## Namespace Updates

Assignment modifies the appropriate namespace:

```python
# Global scope
x = 10  # Updates globals()

def func():
    y = 20  # Updates locals()
    global z
    z = 30  # Updates globals()
```

## Order of Operations

```python
# Complex example
x = (a := 5) + (b := 10)
# 1. Evaluate (a := 5) → assigns 5 to a, returns 5
# 2. Evaluate (b := 10) → assigns 10 to b, returns 10
# 3. Evaluate 5 + 10 → 15
# 4. Bind x to 15
```

## Summary

| Step | Description |
|------|-------------|
| 1 | Evaluate right-hand side expression |
| 2 | Create object (if needed) |
| 3 | Bind name to object in namespace |

Key points:
- RHS always evaluated first
- Assignment binds names, doesn't copy values
- Multiple assignment uses unpacking
- Namespace determines scope of binding
