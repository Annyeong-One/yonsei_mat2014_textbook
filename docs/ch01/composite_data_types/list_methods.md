# list Methods


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python lists provide many built-in methods for manipulation.

---

## Adding Elements

### `append(x)`

Add element to end (in-place, returns `None`):

```python
a = [1, 2, 3]
a.append(4)       # [1, 2, 3, 4]

# Common mistake
a = a.append(5)   # a is now None!
```

### `extend(iterable)`

Add all elements from iterable:

```python
a = [1, 2, 3]
a.extend([4, 5])  # [1, 2, 3, 4, 5]
a.extend("ab")    # [1, 2, 3, 4, 5, 'a', 'b']
```

### `insert(i, x)`

Insert element at index:

```python
a = [1, 2, 3]
a.insert(0, 'start')  # ['start', 1, 2, 3]
a.insert(2, 'mid')    # ['start', 1, 'mid', 2, 3]
```

---

## Removing Elements

### `pop([i])`

Remove and return element (default: last):

```python
a = [1, 2, 3, 4]
a.pop()       # Returns 4, a = [1, 2, 3]
a.pop(0)      # Returns 1, a = [2, 3]
```

### `remove(x)`

Remove first occurrence by value:

```python
a = [1, 2, 3, 2]
a.remove(2)   # [1, 3, 2]
a.remove(5)   # ValueError: not in list
```

### `clear()`

Remove all elements:

```python
a = [1, 2, 3]
a.clear()     # []
```

---

## Searching

### `index(x[, start[, end]])`

Find index of first occurrence:

```python
a = [1, 2, 3, 2, 3]
a.index(3)        # 2
a.index(3, 3)     # 4 (search from index 3)
a.index(5)        # ValueError: not in list
```

### `count(x)`

Count occurrences:

```python
a = [1, 2, 2, 3, 2]
a.count(2)        # 3
a.count(5)        # 0
```

---

## Ordering

### `sort(*, key=None, reverse=False)`

Sort in-place:

```python
a = [3, 1, 4, 1, 5]
a.sort()              # [1, 1, 3, 4, 5]

a = [3, 1, 4, 1, 5]
a.sort(reverse=True)  # [5, 4, 3, 1, 1]

a = [-3, 1, -4, 2]
a.sort(key=abs)       # [1, 2, -3, -4]
```

### `reverse()`

Reverse in-place:

```python
a = [1, 2, 3]
a.reverse()           # [3, 2, 1]
```

---

## Copying

### `copy()`

Shallow copy:

```python
a = [1, 2, 3]
b = a.copy()
a.append(4)
print(b)      # [1, 2, 3] (unchanged)
```

See [list Copying](../../ch02/composites/list_copying.md) for shallow vs deep copy.

---

## Sorting vs sorted()

| Method | In-place | Returns |
|--------|----------|---------|
| `a.sort()` | Yes | `None` |
| `sorted(a)` | No | New list |

```python
a = [3, 1, 2]
b = sorted(a)     # b = [1, 2, 3], a unchanged
a.sort()          # a = [1, 2, 3], returns None
```

---

## Reversing Comparison

| Method | Type | Returns |
|--------|------|---------|
| `a.reverse()` | In-place | `None` |
| `a[::-1]` | Copy | New list |
| `reversed(a)` | Iterator | Generator |

```python
a = [1, 2, 3]

a.reverse()       # a = [3, 2, 1]

b = a[::-1]       # New list

for x in reversed(a):  # Iterator (memory efficient)
    print(x)
```

---

## Summary

| Method | Action | Returns |
|--------|--------|---------|
| `append(x)` | Add to end | `None` |
| `extend(iter)` | Add all from iterable | `None` |
| `insert(i, x)` | Insert at index | `None` |
| `pop([i])` | Remove at index | Element |
| `remove(x)` | Remove by value | `None` |
| `clear()` | Remove all | `None` |
| `index(x)` | Find index | Integer |
| `count(x)` | Count occurrences | Integer |
| `sort()` | Sort in-place | `None` |
| `reverse()` | Reverse in-place | `None` |
| `copy()` | Shallow copy | New list |
