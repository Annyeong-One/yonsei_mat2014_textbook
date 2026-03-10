# LEGB Resolution


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Four Scopes

### 1. Local (L)

```python
def function():
    x = 10  # Local
```

### 2. Enclosing (E)

```python
def outer():
    x = 10  # Enclosing for inner
    def inner():
        print(x)
```

### 3. Global (G)

```python
x = 10  # Global

def function():
    print(x)
```

### 4. Built-in (B)

```python
# Always available
print(len([1, 2, 3]))
```

## Lookup Order

Searches: L → E → G → B


## Accessing Namespaces

### 1. `globals()`

Returns the global namespace dictionary:

```python
x = 42
print(globals()['x'])  # 42
```

### 2. `locals()`

Returns the local namespace dictionary:

```python
def f():
    a = 10
    b = 20
    print(locals())  # {'a': 10, 'b': 20}
```

### 3. `__builtins__`

Contains built-in names:

```python
import builtins
print(dir(builtins))  # ['abs', 'all', 'any', ...]
```

### 4. No `enclosings()` Function

There is no built-in to access enclosing scope directly. Enclosing variables are captured in closures via `__closure__`:

```python
def outer():
    x = 10
    def inner():
        return x
    return inner

f = outer()
print(f.__closure__[0].cell_contents)  # 10
```


## Namespace Summary

| Namespace | Access Method | Modifiable? |
|-----------|---------------|-------------|
| Local | `locals()` | No (snapshot) |
| Enclosing | `__closure__` | Via `nonlocal` |
| Global | `globals()` | Yes |
| Built-in | `builtins` module | Not recommended |


## Summary

- Four scope levels
- Specific lookup order
- First match wins
