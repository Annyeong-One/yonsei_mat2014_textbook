# Time Complexity of Operations


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python data structures have different time complexity characteristics for common operations. Understanding these complexities is crucial for writing efficient code and choosing the right data structure.

---

## List Operations

### Common Operations

```python
lst = [1, 2, 3, 4, 5]

# O(1) - Index access
print(lst[2])

# O(n) - Search
print(3 in lst)

# O(1) amortized - Append
lst.append(6)

# O(n) - Insert at beginning
lst.insert(0, 0)
```

Output:
```
3
True
```

## Dictionary Operations

### Hash Table Performance

```python
d = {'a': 1, 'b': 2, 'c': 3}

# O(1) - Key lookup
print(d['a'])

# O(1) - Insert/Update
d['d'] = 4

# O(1) - Delete
del d['a']

print(d)
```

Output:
```
1
{'b': 2, 'c': 3, 'd': 4}
```

## Set Operations

### Hash Set Performance

```python
s = {1, 2, 3, 4, 5}

# O(1) - Membership test
print(2 in s)

# O(1) - Add
s.add(6)

# O(n) - Union
s2 = {4, 5, 6, 7}
union = s | s2
print(union)
```

Output:
```
True
{1, 2, 3, 4, 5, 6, 7}
```

## Comparison Table

### Big-O Complexity Summary

```python
import sys

# Complexity examples
operations = {
    'list': {
        'index': 'O(1)',
        'search': 'O(n)',
        'append': 'O(1)',
        'insert': 'O(n)',
        'delete': 'O(n)'
    },
    'dict': {
        'lookup': 'O(1)',
        'insert': 'O(1)',
        'delete': 'O(1)'
    },
    'set': {
        'search': 'O(1)',
        'add': 'O(1)',
        'delete': 'O(1)'
    }
}

for ds, ops in operations.items():
    print(f"\n{ds.upper()}:")
    for op, complexity in ops.items():
        print(f"  {op}: {complexity}")
```

Output:
```
LIST:
  index: O(1)
  search: O(n)
  append: O(1)
  insert: O(n)
  delete: O(n)

DICT:
  lookup: O(1)
  insert: O(1)
  delete: O(1)

SET:
  search: O(1)
  add: O(1)
  delete: O(1)
```
