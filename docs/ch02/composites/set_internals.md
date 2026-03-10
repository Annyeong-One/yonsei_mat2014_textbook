# set Internals


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Sets are implemented similarly to dictionaries—as hash tables—enabling O(1) average membership testing and set operations. Understanding set internals explains their performance characteristics and implementation constraints.

---

## Hash-Based Implementation

### Membership Testing is Fast

```python
s = {i for i in range(100000)}

# O(1) average case
print(50000 in s)
print(99999 in s)
print(100000 in s)
```

Output:
```
True
True
False
```

### Elements Must Be Hashable

```python
s = {1, 2.5, "three", (4, 5)}
print(s)

# Unhashable types fail
try:
    s.add([6, 7])
except TypeError as e:
    print(f"Error: {e}")
```

Output:
```
{1, 2.5, 'three', (4, 5)}
Error: unhashable type: 'list'
```

## Set Operations as Hash Operations

### Union, Intersection, Difference

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"Union: {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference: {a - b}")
print(f"Symmetric difference: {a ^ b}")
```

Output:
```
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference: {1, 2}
Symmetric difference: {1, 2, 5, 6}
```

## Set vs List Performance

### Membership Testing

```python
import time

# Using list
lst = list(range(100000))
set_time = time.time()
for _ in range(1000):
    50000 in lst
list_duration = time.time() - set_time

# Using set
s = set(range(100000))
start = time.time()
for _ in range(1000):
    50000 in s
set_duration = time.time() - start

print(f"List: {list_duration:.4f}s")
print(f"Set: {set_duration:.6f}s")
```

Output:
```
List: 0.0234s
Set: 0.000024s
```

## Practical Uses

### Deduplication

```python
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = set(data)
print(unique)
```

Output:
```
{1, 2, 3, 4}
```

### Finding Common Elements

```python
students_morning = {'Alice', 'Bob', 'Charlie'}
students_afternoon = {'Bob', 'Charlie', 'David'}

both_shifts = students_morning & students_afternoon
print(f"Both shifts: {both_shifts}")
```

Output:
```
Both shifts: {'Charlie', 'Bob'}
```
