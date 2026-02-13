# dict Ordering Guarantees

Since Python 3.7, dictionaries guarantee insertion order preservation as a language feature (not just implementation detail). This makes dicts suitable for ordered key-value collections and simplifies many programming patterns.

---

## Insertion Order Preservation

### Order is Guaranteed

```python
d = {}
d['z'] = 1
d['a'] = 2
d['m'] = 3

for key in d:
    print(key)
```

Output:
```
z
a
m
```

### Items Maintain Order

```python
d = {'zebra': 1, 'apple': 2, 'mango': 3}

print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
print("Items:", list(d.items()))
```

Output:
```
Keys: ['zebra', 'apple', 'mango']
Values: [1, 2, 3]
Items: [('zebra', 1), ('apple', 2), ('mango', 3)]
```

## Practical Benefits

### Iteration Order is Predictable

```python
config = {
    'host': 'localhost',
    'port': 8000,
    'debug': True,
    'timeout': 30
}

for setting, value in config.items():
    print(f"{setting}: {value}")
```

Output:
```
host: localhost
port: 8000
debug: True
timeout: 30
```

### First/Last Access

```python
d = {'first': 1, 'second': 2, 'third': 3}

first_key = next(iter(d))
last_key = next(reversed(d))

print(f"First: {first_key}")
print(f"Last: {last_key}")
```

Output:
```
First: first
Last: third
```

## Update Behavior

### Order After Updates

```python
d = {'a': 1, 'b': 2}
d['c'] = 3
d['a'] = 10  # Update doesn't change position

print(list(d.keys()))
```

Output:
```
['a', 'b', 'c']
```

### Deletion and Reinsertion

```python
d = {'a': 1, 'b': 2, 'c': 3}
del d['b']
d['b'] = 20

print(list(d.keys()))
```

Output:
```
['a', 'c', 'b']
```
