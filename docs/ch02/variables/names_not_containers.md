# Names vs Containers


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Fundamental Model

### 1. Python Approach

Variables are **names** that refer to objects:

```python
x = [1, 2, 3]
```

**Memory Layout**:
```
Stack (Names)         Heap (Objects)
┌─────────┐          ┌──────────────────┐
│ x   ────┼─────────▶│ Identity: 140... │
└─────────┘          │ Type: <list>     │
                     │ Value: [1,2,3]   │
                     │ Refcount: 1      │
                     └──────────────────┘
```

### 2. C Approach

Variables are **containers** holding values:

```c
int x = 42;
```

**Memory Layout**:
```
Stack
┌─────────┬────────┐
│ x (int) │   42   │  # Value stored directly
└─────────┴────────┘
```

## Assignment Behavior

### 1. Python Binding

Creates new name-to-object association:

```python
x = [1, 2, 3]
y = x          # y points to same object
y.append(4)
print(x)       # [1, 2, 3, 4] - same object
```

### 2. C Copying

Copies value to new container:

```c
int x = 42;
int y = x;     // Copies value
y = 100;
// x still 42 - independent
```

## Multiple References

### 1. Python Sharing

Multiple names → same object:

```python
a = [1, 2, 3]
b = a
c = a

# All point to same object
print(a is b is c)  # True
print(id(a) == id(b) == id(c))  # True
```

### 2. C Independence

Each variable is separate:

```c
int a = 42;
int b = a;  // Copy
int c = a;  // Copy
// Three independent values
```

## Reassignment

### 1. Python Rebinding

Creates new binding:

```python
x = [1, 2, 3]
original_id = id(x)
x = [4, 5, 6]  # New object, new binding
print(id(x) != original_id)  # True
```

### 2. C Overwriting

Overwrites value in place:

```c
int x = 42;
x = 100;  // Same container, new value
```

## Function Parameters

### 1. Modification

```python
def modify_list(lst):
    lst.append(4)  # Modifies original

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4]
```

### 2. Reassignment

```python
def reassign_list(lst):
    lst = [5, 6]   # New local binding only

my_list = [1, 2, 3]
reassign_list(my_list)
print(my_list)  # [1, 2, 3] - unchanged
```

## Memory Efficiency

### 1. Python Sharing

```python
# Multiple names → one object
huge_list = list(range(1000000))
refs = [huge_list] * 1000  # 1000 names → 1 object
# Minimal extra memory
```

### 2. C Copying

```c
// Would create 1000 copies
// int arrays[1000][1000000];  // Huge memory!
```

## Mental Model

**Think of variables as**:
- Post-it notes with names
- Stuck on objects in heap
- Can move to different objects
- Multiple notes on same object

**Not as**:
- Boxes containing values
- Fixed storage locations
- Independent containers

```python
# Post-it note analogy
# Object exists in heap
actual_object = [1, 2, 3]

# Attach labels
x = actual_object  # "x" note on object
y = actual_object  # "y" note on object
z = actual_object  # "z" note on object

# Remove label
del y  # Remove "y" note

# Move label
x = [4, 5, 6]  # Move "x" to new object
```
