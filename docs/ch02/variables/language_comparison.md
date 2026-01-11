# Language Models

## Python Model

### 1. Reference Semantics

Names refer to objects:

```python
x = [1, 2, 3]
y = x  # Both refer to same object
```

| Characteristic | Behavior |
|---------------|----------|
| Assignment | Creates reference |
| Equality `==` | Compares values |
| Identity `is` | Compares references |
| Mutation | Affects all references |

### 2. Example

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]
```

## Java Model

### 1. Objects vs Primitives

**Objects**: Reference semantics

```java
List<Integer> x = new ArrayList<>();
List<Integer> y = x;  // Both refer to same
```

**Primitives**: Value semantics

```java
int a = 42;
int b = a;  // b gets copy
```

### 2. Key Differences

| Type | Assignment | Comparison |
|------|-----------|------------|
| Object | Reference | `.equals()` |
| Primitive | Copy | `==` |

## C Model

### 1. Direct Storage

Variables are memory locations:

```c
int x = 42;  // x is 4-byte container
```

### 2. Explicit Pointers

```c
int x = 42;
int* p = &x;   // Explicit pointer
int y = x;     // Copy value
```

| Aspect | Behavior |
|--------|----------|
| Variables | Direct storage |
| Pointers | Explicit `*` |
| Assignment | Copies value |
| Comparison | Value or pointer |

## C++ Model

### 1. Multiple Options

```cpp
int x = 42;        // Value
int* p = &x;       // Pointer
int& r = x;        // Reference
```

### 2. Choice Table

| Type | Storage | Assignment | Modification |
|------|---------|-----------|--------------|
| Value | Direct | Copy | Independent |
| Pointer | Address | Copy pointer | Through `*p` |
| Reference | Alias | Cannot reassign | Direct |

## Haskell Model

### 1. Immutable Bindings

```haskell
x = [1, 2, 3]  -- Immutable binding
-- x = [4, 5, 6]  -- Error: cannot rebind
```

### 2. Transparency

```haskell
-- Same expression always gives same result
f x = x + x
-- f 5 always returns 10
```

## Comparison Table

| Language | Variable Model | Memory Mgmt | Assignment |
|----------|---------------|-------------|------------|
| **Python** | Names → Objects | Auto (GC) | Ref binding |
| **Java** | Refs + Primitives | Auto (GC) | Ref/Copy |
| **C++** | Values/Ptrs/Refs | Manual | Value/Ptr |
| **C** | Direct values | Manual | Value copy |
| **Haskell** | Immutable | Auto (GC) | No reassign |

## Practical Examples

### 1. Aliasing

**Python**:
```python
x = [1, 2]
y = x  # Alias
y.append(3)
print(x)  # [1, 2, 3]
```

**C**:
```c
int x = 42;
int y = x;  // Copy
y = 100;
// x still 42
```

### 2. Parameter Passing

**Python**:
```python
def modify(lst):
    lst.append(4)  # Modifies original

x = [1, 2, 3]
modify(x)
print(x)  # [1, 2, 3, 4]
```

**C**:
```c
void modify(int val) {
    val = 100;  // Modifies copy only
}

int x = 42;
modify(x);
// x still 42
```

**C++ Reference**:
```cpp
void modify(int& val) {
    val = 100;  // Modifies original
}

int x = 42;
modify(x);
// x is now 100
```

## Key Insights

### 1. Python Advantages

- Simple mental model
- No pointer arithmetic
- Automatic memory management
- Flexible aliasing

### 2. Python Gotchas

- Unexpected sharing
- Mutable default arguments
- No explicit copy

### 3. Best Practices

```python
# Explicit copying when needed
import copy

original = [1, 2, [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

# Clear intent
def process(data):
    # Work with original
    data.append(5)
    
def process_copy(data):
    # Work with copy
    local_data = data.copy()
    local_data.append(5)
    return local_data
```
