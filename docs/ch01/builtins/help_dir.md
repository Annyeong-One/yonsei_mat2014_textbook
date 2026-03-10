# help() and dir()


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The help() function provides documentation about objects, modules, and functions, while dir() lists available attributes and methods. Both are essential introspection tools for exploring Python objects and understanding their capabilities.

---

## dir() Function

### Exploring Object Attributes

```python
text = "hello"
attributes = dir(text)
print([attr for attr in attributes if not attr.startswith('_')])
```

Output:
```
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

### List Methods

```python
lst = []
methods = [m for m in dir(lst) if not m.startswith('_')]
print(methods)
```

Output:
```
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

### Dictionary Methods

```python
d = {}
dict_methods = [m for m in dir(d) if not m.startswith('_')]
print(dict_methods[:5])
```

Output:
```
['clear', 'copy', 'fromkeys', 'get', 'items']
```

## help() Function

### Getting Function Documentation

```python
help(len)
```

Output:
```
Help on built-in function len in module builtins:

len(obj, /)
    Return the length of obj.
```

### String Method Help

```python
help(str.upper)
```

Output:
```
Help on method_descriptor:

upper(self, /)
    Return a copy of the string converted to uppercase.
```

## Practical Introspection

### Discovering Available Methods

```python
class Dog:
    def bark(self):
        return "Woof!"
    
    def sit(self):
        return "Dog sits"

dog = Dog()
public_methods = [m for m in dir(dog) if not m.startswith('_') and callable(getattr(dog, m))]
print(public_methods)
```

Output:
```
['bark', 'sit']
```

### Checking Object Types

```python
obj1 = 42
obj2 = "hello"
obj3 = [1, 2, 3]

for obj in [obj1, obj2, obj3]:
    print(f"Type: {type(obj).__name__}")
    attrs = [a for a in dir(obj) if not a.startswith('_')]
    print(f"Methods: {len(attrs)}
")
```

Output:
```
Type: int
Methods: 31

Type: str
Methods: 43

Type: list
Methods: 11
```
