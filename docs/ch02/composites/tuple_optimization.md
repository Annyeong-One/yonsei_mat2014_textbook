# tuple Optimization


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Tuples are optimized in CPython through tuple interning and caching, making them faster for hashable collections and reducing memory usage. Understanding these optimizations explains why tuples are preferred for immutable sequences and dictionary keys.

---

## Tuple Interning

### Small Tuple Caching

```python
a = (1, 2, 3)
b = (1, 2, 3)
print(f"Same object: {a is b}")

c = tuple([1, 2, 3])
print(f"Constructed tuple same: {a is c}")
```

Output:
```
Same object: True
Constructed tuple same: False
```

### String Tuple Interning

```python
t1 = ("hello", "world")
t2 = ("hello", "world")
print(f"String tuples same: {t1 is t2}")
```

Output:
```
String tuples same: True
```

## Memory Efficiency

### Tuple vs List Comparison

```python
import sys

t = (1, 2, 3, 4, 5)
l = [1, 2, 3, 4, 5]

print(f"Tuple size: {sys.getsizeof(t)} bytes")
print(f"List size: {sys.getsizeof(l)} bytes")
```

Output:
```
Tuple size: 56 bytes
List size: 64 bytes
```

## Tuple Unpacking Optimization

### Fast Unpacking

```python
def swap(a, b):
    return b, a

x = 1
y = 2
x, y = swap(x, y)
print(f"Swapped: x={x}, y={y}")
```

Output:
```
Swapped: x=2, y=1
```

## Practical Advantages

### Hashable for Dictionaries

```python
# Tuples can be dict keys
coordinates = {
    (0, 0): "origin",
    (1, 0): "right",
    (0, 1): "up"
}

print(coordinates[(1, 0)])
```

Output:
```
right
```

### Function Return Optimization

```python
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(f"Coordinates: ({x}, {y})")
```

Output:
```
Coordinates: (10, 20)
```
