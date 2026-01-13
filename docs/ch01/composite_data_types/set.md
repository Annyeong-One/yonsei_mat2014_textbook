# `set` and Membership

A **set** is an unordered collection of unique, hashable elements, implemented using a hash table.

---

## Creating Sets

```python
s = {1, 2, 3}
empty = set()       # NOT {} (that's an empty dict)
```

Duplicates are automatically removed:

```python
s = {1, 2, 2, 3, 3, 3}
print(s)            # {1, 2, 3}
```

### From Other Types

```python
set("hello")        # {'h', 'e', 'l', 'o'}
set([1, 2, 2, 3])   # {1, 2, 3}
set((1, 2, 3))      # {1, 2, 3}
```

### Set Comprehension

```python
{x**2 for x in range(5)}    # {0, 1, 4, 9, 16}
```

---

## Elements Must Be Hashable

Only immutable (hashable) objects can be set elements:

```python
{1, "hello", (1, 2)}    # ✓ int, str, tuple

{[1, 2]}                # ✗ TypeError: unhashable type: 'list'
{{"a": 1}}              # ✗ TypeError: unhashable type: 'dict'
```

### The Number Gotcha

```python
s = {1, 1.0}
print(s)        # {1}
```

Since `1 == 1.0` and `hash(1) == hash(1.0)`, they're the same element.

---

## Membership Testing

Sets excel at O(1) membership checks:

```python
s = {1, 2, 3}
2 in s          # True
5 in s          # False
5 not in s      # True
```

Much faster than lists for large collections.

---

## Set Operations

### Union (`|`)

Elements in either set:

```python
{1, 2, 3} | {3, 4, 5}           # {1, 2, 3, 4, 5}
{1, 2, 3}.union({3, 4, 5})      # Same
```

### Intersection (`&`)

Elements in both sets:

```python
{1, 2, 3} & {2, 3, 4}           # {2, 3}
{1, 2, 3}.intersection({2, 3, 4})
```

### Difference (`-`)

Elements in first but not second:

```python
{1, 2, 3} - {2, 3, 4}           # {1}
{1, 2, 3}.difference({2, 3, 4})
```

### Symmetric Difference (`^`)

Elements in either but not both:

```python
{1, 2, 3} ^ {2, 3, 4}           # {1, 4}
{1, 2, 3}.symmetric_difference({2, 3, 4})
```

### In-Place Operations

```python
s = {1, 2, 3}
s |= {4, 5}     # Union update
s &= {2, 3, 4}  # Intersection update
s -= {3}        # Difference update
s ^= {1, 5}     # Symmetric difference update
```

---

## Set Methods

### Adding Elements

```python
s = {1, 2}
s.add(3)            # {1, 2, 3}
s.add(2)            # {1, 2, 3} (no change, already exists)

s.update([4, 5])    # {1, 2, 3, 4, 5} (add multiple)
```

### Removing Elements

```python
s = {1, 2, 3, 4, 5}

s.remove(3)         # Removes 3, KeyError if missing
s.discard(10)       # No error if missing
s.pop()             # Remove and return arbitrary element
s.clear()           # Remove all elements
```

| Method | Missing Element |
|--------|-----------------|
| `remove(x)` | KeyError |
| `discard(x)` | No error |

---

## Set Comparisons

### Subset and Superset

```python
A = {1, 2}
B = {1, 2, 3, 4}

A <= B      # True (A is subset of B)
A < B       # True (A is proper subset)
B >= A      # True (B is superset of A)
B > A       # True (B is proper superset)

A.issubset(B)       # True
B.issuperset(A)     # True
```

### Disjoint

```python
{1, 2}.isdisjoint({3, 4})   # True (no common elements)
{1, 2}.isdisjoint({2, 3})   # False
```

---

## Frozenset

Immutable version of set:

```python
fs = frozenset([1, 2, 3])
fs.add(4)           # AttributeError: no add method
```

Can be used as dict key or set element:

```python
{frozenset([1, 2]): "value"}    # ✓
{{1, 2}: "value"}               # ✗ TypeError
```

---

## Set Internals

Sets use the same hash table as dictionaries, but without values:

| Aspect | `dict` | `set` |
|--------|--------|-------|
| Structure | Hash table | Hash table |
| Content | Key-value pairs | Keys only |
| Collision | Open addressing | Open addressing |

Conceptually: `{"a", "b"}` → `{"a": True, "b": True}`

---

## Time Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| `x in s` | O(1) | O(n) |
| `add(x)` | O(1) | O(n) |
| `remove(x)` | O(1) | O(n) |
| `union` | O(len(s)+len(t)) | — |
| `intersection` | O(min(len(s),len(t))) | — |

---

## Common Use Cases

### Remove Duplicates

```python
list(set([1, 2, 2, 3, 3, 3]))   # [1, 2, 3]
```

Note: Order not preserved. For order-preserving:

```python
list(dict.fromkeys([1, 2, 2, 3]))  # [1, 2, 3]
```

### Fast Lookup

```python
valid = {"apple", "banana", "cherry"}
if fruit in valid:
    process(fruit)
```

### Find Common/Different Elements

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

common = a & b          # {3, 4}
only_in_a = a - b       # {1, 2}
in_either = a | b       # {1, 2, 3, 4, 5, 6}
```

---

## Key Takeaways

- Sets store unique, hashable elements only
- O(1) membership testing (much faster than lists)
- `{}` is empty dict, use `set()` for empty set
- `1` and `1.0` are the same element
- Support mathematical set operations (`|`, `&`, `-`, `^`)
- Use `frozenset` for immutable sets (as dict keys)
- Internally same as dict, but keys only
