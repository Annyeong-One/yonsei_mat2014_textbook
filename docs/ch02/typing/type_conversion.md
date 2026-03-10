# Type Conversion


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Built-in Converters

### 1. To Integer

```python
x = int("42")       # From string
y = int(3.7)        # From float (truncates)
z = int(True)       # From bool
print(x, y, z)      # 42 3 1
```

### 2. To Float

```python
x = float("3.14")
y = float(42)
z = float(True)
print(x, y, z)      # 3.14 42.0 1.0
```

### 3. To String

```python
x = str(42)
y = str(3.14)
z = str([1, 2, 3])
print(x, y, z)      # "42" "3.14" "[1, 2, 3]"
```

## Collection Conversion

### 1. To List

```python
x = list((1, 2, 3))        # From tuple
y = list("hello")          # From string  
z = list(range(5))         # From range
print(x, y, z)
```

### 2. To Tuple/Set

```python
x = tuple([1, 2, 3])
y = set([1, 2, 2, 3])      # Removes duplicates
print(x, y)                # (1, 2, 3) {1, 2, 3}
```

### 3. To Dict

```python
x = dict([('a', 1), ('b', 2)])
keys = ['x', 'y']
values = [1, 2]
y = dict(zip(keys, values))
print(x, y)
```

## Numeric Conversion

### 1. Base Conversion

```python
x = int('1010', 2)         # Binary to int
y = int('FF', 16)          # Hex to int
print(x, y)                # 10 255
```

### 2. Int to Base

```python
print(bin(10))             # '0b1010'
print(hex(255))            # '0xff'
print(oct(63))             # '0o77'
```

## Error Handling

### 1. Safe Conversion

```python
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(safe_int("42"))      # 42
print(safe_int("bad"))     # 0
```

## Boolean Conversion

### 1. Truthy/Falsy

```python
print(bool(1))             # True
print(bool(0))             # False
print(bool(""))            # False
print(bool([]))            # False
print(bool(None))          # False
```

## Conversion Table

| From | To | Function |
|------|-----|----------|
| str | int | `int()` |
| str | float | `float()` |
| int | str | `str()` |
| list | tuple | `tuple()` |
| list | set | `set()` |
