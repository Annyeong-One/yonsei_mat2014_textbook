# `list` and Dynamic Arrays

A **list** is an ordered, mutable collection backed by a dynamic array. Lists are the most commonly used data structure in Python.

---

## Creating Lists

```python
xs = [1, 2, 3]
empty = []
mixed = [1, "two", 3.0]  # Heterogeneous (discouraged)
```

### From Other Types

```python
list("hello")       # ['h', 'e', 'l', 'l', 'o']
list((1, 2, 3))     # [1, 2, 3]
list(range(5))      # [0, 1, 2, 3, 4]
```

---

## Indexing and Slicing

```python
a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#    0  1  2  3  4  5  6  7  8   (positive)
#   -9 -8 -7 -6 -5 -4 -3 -2 -1   (negative)

a[0]      # 0 (first)
a[-1]     # 8 (last)
a[2:5]    # [2, 3, 4]
a[::2]    # [0, 2, 4, 6, 8] (every 2nd)
a[::-1]   # [8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
```

**Note**: `a[3]` returns an element; `a[3:4]` returns a list.

---

## Mutability

Lists can be modified in place:

```python
xs = [1, 2, 3]
xs[0] = 10        # [10, 2, 3]
xs.append(4)      # [10, 2, 3, 4]
xs[1:3] = [20]    # [10, 20, 4]
```

---

## Dynamic Array Internals

Python lists use **over-allocation**:

```python
import sys
a = []
for i in range(10):
    a.append(i)
    print(len(a), sys.getsizeof(a))
```

- Allocates extra capacity beyond current size
- Resizes occasionally (amortized O(1) append)
- Reallocation copies all elements (O(n))

---

## Concatenation and Repetition

### Concatenation

```python
x = [1, 2, 3]
y = x + [4, 5]    # New list: [1, 2, 3, 4, 5]

# In-place (same object)
x += [4, 5]       # Modifies x
```

**ID behavior**:

```python
x = [1, 2, 3]
print(id(x))
x = x + [4]       # New object (different id)
print(id(x))

x = [1, 2, 3]
print(id(x))
x += [4]          # Same object (same id)
print(id(x))
```

### Repetition

```python
[0] * 5           # [0, 0, 0, 0, 0]
[1, 2] * 3        # [1, 2, 1, 2, 1, 2]
```

---

## Aliasing and References

```python
a = [1, 2, 3]
b = a             # Same object
a.append(4)
print(b)          # [1, 2, 3, 4]
```

```
a ─┬──► [1, 2, 3, 4]
   │
b ─┘
```

To create an independent copy, see [list Copying](../../ch02/composites/list_copying.md).

---

## Built-in Functions

```python
nums = [3, 1, 4, 1, 5]

len(nums)         # 5
sum(nums)         # 14
min(nums)         # 1
max(nums)         # 5
sorted(nums)      # [1, 1, 3, 4, 5] (new list)
```

---

## Performance

| Operation | Time Complexity |
|-----------|-----------------|
| Index `a[i]` | O(1) |
| Append | O(1) amortized |
| Pop (end) | O(1) |
| Pop (front) | O(n) |
| Insert | O(n) |
| Remove | O(n) |
| Search `in` | O(n) |

---

## Key Takeaways

- Lists are mutable dynamic arrays
- Fast indexing and end operations
- `+=` modifies in place; `+` creates new list
- Multiple names can reference the same list (aliasing)
- Avoid frequent middle insertions for performance
