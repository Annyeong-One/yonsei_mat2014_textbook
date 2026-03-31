
# help() and dir()

Python provides `help()` and `dir()` as introspection tools: `help()` displays an object's documentation, while `dir()` lists its available attributes and methods.

## help()

Displays the built-in documentation for any Python object, including functions, modules, and classes.

```python
help(print)
```

## dir()

Lists all attributes and methods available on a given object or type.

```python
dir(str)
```

This returns a list of all string methods and attributes:

```
['capitalize', 'count', 'encode', 'find', 'lower', ...]
```

## Practical Example

```python
x = "Python"

print(dir(x))
```

These tools help developers **discover available functionality**.
