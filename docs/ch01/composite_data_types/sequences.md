# Sequences Overview

A **sequence** is an ordered collection that supports indexing, slicing, and iteration. Python has three built-in sequence types: `str`, `list`, and `tuple`.

---

## Sequence Types

| Type | Mutable | Example |
|------|---------|---------|
| `str` | No | `"hello"` |
| `list` | Yes | `[1, 2, 3]` |
| `tuple` | No | `(1, 2, 3)` |

All sequences share common operations.

---

## Common Operations

### Indexing

Access individual elements by position:

```python
s = "Hello"
lst = [0, 1, 2, 3, 4]
t = (10, 20, 30, 40, 50)

# Positive index (from start)
s[0]        # 'H'
lst[2]      # 2
t[4]        # 50

# Negative index (from end)
s[-1]       # 'o'
lst[-2]     # 3
t[-3]       # 30
```

### Slicing

Extract a subsequence:

```python
s = "Hello World"
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
t = (0, 1, 2, 3, 4, 5, 6, 7, 8)

# [start:stop] (stop exclusive)
s[0:5]      # 'Hello'
lst[2:5]    # [2, 3, 4]
t[3:6]      # (3, 4, 5)

# [start:stop:step]
s[::2]      # 'HloWrd' (every 2nd)
lst[1:7:2]  # [1, 3, 5]
t[::-1]     # (8, 7, 6, 5, 4, 3, 2, 1, 0) (reversed)
```

Slicing always returns the **same type** as the original.

### Concatenation (`+`)

Join sequences of the same type:

```python
"Hello" + " World"          # 'Hello World'
[1, 2] + [3, 4]             # [1, 2, 3, 4]
(1, 2) + (3, 4)             # (1, 2, 3, 4)
```

Cannot mix types:

```python
[1, 2] + (3, 4)             # TypeError
```

### Repetition (`*`)

Repeat a sequence:

```python
"ab" * 3                    # 'ababab'
[0] * 5                     # [0, 0, 0, 0, 0]
(1, 2) * 2                  # (1, 2, 1, 2)
```

### Length (`len`)

```python
len("Hello")                # 5
len([1, 2, 3])              # 3
len((1, 2, 3, 4))           # 4
```

### Membership (`in`)

```python
'e' in "Hello"              # True
3 in [1, 2, 3]              # True
5 in (1, 2, 3)              # False
```

### Iteration

```python
for char in "abc":
    print(char)             # a, b, c

for item in [1, 2, 3]:
    print(item)             # 1, 2, 3

for val in (10, 20):
    print(val)              # 10, 20
```

---

## Comparison

Sequences compare lexicographically (element by element):

```python
[1, 2, 3] < [1, 2, 4]       # True (3 < 4)
"apple" < "banana"          # True ('a' < 'b')
(1, 2) < (1, 2, 3)          # True (shorter is "less")
```

---

## Built-in Functions

These work on all sequences:

| Function | Description |
|----------|-------------|
| `len(seq)` | Number of elements |
| `min(seq)` | Smallest element |
| `max(seq)` | Largest element |
| `sum(seq)` | Sum (numeric only) |
| `sorted(seq)` | New sorted list |
| `reversed(seq)` | Reverse iterator |
| `enumerate(seq)` | Index-value pairs |

```python
nums = [3, 1, 4, 1, 5]

len(nums)           # 5
min(nums)           # 1
max(nums)           # 5
sum(nums)           # 14
sorted(nums)        # [1, 1, 3, 4, 5]
list(reversed(nums)) # [5, 1, 4, 1, 3]
```

---

## Mutable vs Immutable

| Operation | `list` (mutable) | `str`/`tuple` (immutable) |
|-----------|------------------|---------------------------|
| `seq[i] = x` | ✅ Modifies | ❌ TypeError |
| `seq.append(x)` | ✅ Modifies | ❌ No method |
| Concatenation | New object (or `+=` in-place) | Always new object |

```python
# List: can modify
lst = [1, 2, 3]
lst[0] = 10         # [10, 2, 3]

# String: cannot modify
s = "hello"
s[0] = "H"          # TypeError

# Tuple: cannot modify
t = (1, 2, 3)
t[0] = 10           # TypeError
```

---

## When to Use Which

| Type | Use When |
|------|----------|
| `str` | Text data |
| `list` | Collection that changes |
| `tuple` | Fixed collection, dict keys, function returns |

---

## Summary

All sequences support:
- **Indexing**: `seq[i]`, `seq[-i]`
- **Slicing**: `seq[start:stop:step]`
- **Concatenation**: `seq1 + seq2`
- **Repetition**: `seq * n`
- **Length**: `len(seq)`
- **Membership**: `x in seq`
- **Iteration**: `for x in seq`

Choose `list` for mutable needs, `tuple` for immutable/hashable needs, `str` for text.
