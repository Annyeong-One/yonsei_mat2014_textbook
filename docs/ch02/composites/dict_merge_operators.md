# dict Merge Operators

Python 3.9+ introduced the | and |= operators for merging dictionaries, providing a cleaner syntax than update() and providing merge semantics. This is part of PEP 584 and improves dict manipulation.

---

## The | Operator (Merge)

### Basic Dict Merging

```python
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

merged = d1 | d2
print(merged)
```

Output:
```
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### Right Side Overwrites

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 3}

merged = d1 | d2
print(merged)
```

Output:
```
{'a': 1, 'b': 20, 'c': 3}
```

## The |= Operator (In-Place Merge)

### Updating a Dictionary

```python
d = {'a': 1, 'b': 2}
d |= {'c': 3, 'd': 4}
print(d)
```

Output:
```
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### Overwriting Values

```python
d = {'a': 1, 'b': 2}
d |= {'b': 20, 'c': 3}
print(d)
```

Output:
```
{'a': 1, 'b': 20, 'c': 3}
```

## Practical Applications

### Configuration Merging

```python
defaults = {'host': 'localhost', 'port': 8000, 'debug': False}
custom = {'port': 5000, 'debug': True}

config = defaults | custom
print(config)
```

Output:
```
{'host': 'localhost', 'port': 5000, 'debug': True}
```

### Layered Configuration

```python
system = {'theme': 'dark', 'language': 'en'}
user = {'theme': 'light'}
session = {'theme': 'auto'}

final = system | user | session
print(final)
```

Output:
```
{'theme': 'auto', 'language': 'en'}
```

## Comparison with update()

### | Creates New Dict

```python
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3}

d3 = d1 | d2
print(f"d1: {d1}")
print(f"d3: {d3}")
print(f"d1 unchanged: {d1 is not d3}")
```

Output:
```
d1: {'a': 1, 'b': 2}
d3: {'a': 1, 'b': 2, 'c': 3}
d1 unchanged: True
```
