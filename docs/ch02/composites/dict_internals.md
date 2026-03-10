# dict Internals (Hash Tables)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python dictionaries are implemented as hash tables, using hash functions to map keys to values with O(1) average lookup time. Understanding dict internals explains performance characteristics and behavioral quirks.

---

## Hash Functions

### How Hashing Works

```python
# Hash of objects
print(f"Hash of 'key': {hash('key')}")
print(f"Hash of 42: {hash(42)}")
print(f"Hash of (1,2): {hash((1, 2))}")

# Lists can't be hashed (mutable)
try:
    hash([1, 2, 3])
except TypeError as e:
    print(f"Error: {e}")
```

Output:
```
Hash of 'key': 4567822475321
Hash of 42: 42
Hash of (1,2): 3713081631934410656
Error: unhashable type: 'list'
```

### Hash Collisions

```python
# Multiple keys can hash to same bucket
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3

print(f"Dict size: {d}")
```

Output:
```
Dict size: {'a': 1, 'b': 2, 'c': 3}
```

## Dictionary Growth

### Dynamic Resizing

```python
d = {}
print(f"Initial capacity hint")

for i in range(10):
    d[f'key_{i}'] = i

print(f"Keys: {len(d)}")
print(f"Dict: {d}")
```

Output:
```
Initial capacity hint
Keys: 10
Dict: {'key_0': 0, 'key_1': 1, 'key_2': 2, 'key_3': 3, 'key_4': 4, 'key_5': 5, 'key_6': 6, 'key_7': 7, 'key_8': 8, 'key_9': 9}
```

## Performance Characteristics

### O(1) Lookup

```python
import time

d = {i: i**2 for i in range(100000)}

# Fast lookup
start = time.time()
for _ in range(1000):
    value = d[50000]
lookup_time = time.time() - start

print(f"Lookup time: {lookup_time:.6f}s")
```

Output:
```
Lookup time: 0.000045s
```

## Key Behavior

### Keys Must Be Hashable

```python
d = {(1, 2): "tuple_key"}
print(d[(1, 2)])

# This fails - lists aren't hashable
try:
    d[[1, 2]] = "list_key"
except TypeError:
    print("Lists cannot be dict keys")
```

Output:
```
tuple_key
Lists cannot be dict keys
```
