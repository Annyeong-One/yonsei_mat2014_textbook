# Python vs C Memory


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Memory Model

### 1. Python

Everything on heap:

```python
x = 42              # Heap
s = "hello"         # Heap
lst = [1, 2, 3]     # Heap
```

### 2. C

Variables on stack:

```c
int x = 42;         // Stack
char s[] = "hello"; // Stack
```

## Allocation

### 1. Python Auto

```python
# Automatic allocation
x = [1, 2, 3]

# Automatic deallocation
del x
# GC handles it
```

### 2. C Manual

```c
// Manual allocation
int *x = malloc(sizeof(int) * 3);

// Manual deallocation
free(x);  // Must remember!
```

## References

### 1. Python

All names are references:

```python
a = [1, 2, 3]
b = a           # Both point to same

b.append(4)
print(a)        # [1, 2, 3, 4]
```

### 2. C

Explicit pointers:

```c
int x = 42;
int *p = &x;    // Explicit pointer
int y = x;      // Copy value
```

## Type Safety

### 1. Python Dynamic

```python
x = 42
x = "hello"     # OK
x = [1, 2, 3]   # OK
```

### 2. C Static

```c
int x = 42;
x = "hello";    // Error!
```

## Memory Overhead

### 1. Python

Every object has overhead:

```python
import sys

x = 1
print(sys.getsizeof(x))  # ~28 bytes!
```

### 2. C

Minimal overhead:

```c
int x = 1;  // 4 bytes only
```

## Performance

### 1. Python

- Auto management
- More overhead
- Slower allocation

### 2. C

- Manual control
- Less overhead
- Faster allocation
- More error-prone

## Summary

| Aspect | Python | C |
|--------|--------|---|
| Location | Heap | Stack/Heap |
| Management | Auto | Manual |
| References | All refs | Explicit |
| Overhead | High | Low |
| Safety | Safe | Unsafe |
