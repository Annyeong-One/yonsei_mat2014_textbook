# `id()`, `type()`, `isinstance()`

These built-ins support **introspection**, allowing programs to examine objects at runtime.

---

## `id()`

Returns a unique identifier for an object during its lifetime:

```python
x = []
id(x)
```

Conceptually corresponds to a memory address.

---

## `type()`

Returns the type of an object:

```python
type(3)        # <class 'int'>
type([1, 2])   # <class 'list'>
```

---

## `isinstance()`

Checks whether an object is an instance of a type:

```python
isinstance(3, int)
isinstance(True, int)   # True
```

Supports tuples of types:

```python
isinstance(x, (int, float))
```

---

## `dir()`

Returns a list of names (attributes and methods) of an object:

```python
name = "hello"
print(dir(name))  # List of string methods
```

Without arguments, returns names in current scope:

```python
x = 10
print(dir())  # Includes 'x'
```

Useful for exploration and debugging.


---

## `help()`

Displays documentation for an object:

```python
help(str.lower)
help(len)
```

Shows the docstring and signature. In interactive sessions, provides paginated output.


---

## `del`

Deletes references to objects:

```python
# Delete a variable
x = 10
del x
# x is no longer defined

# Delete from a list
my_list = [1, 2, 3]
del my_list[1]  # [1, 3]

# Delete from a dict
my_dict = {'a': 1, 'b': 2}
del my_dict['a']  # {'b': 2}

# Delete an attribute
del obj.attribute
```

Memory is freed by the garbage collector when no references remain.


---

## Best practices

- Use `isinstance()` instead of `type(x) == T`.
- Avoid excessive type checking; prefer polymorphism.

---

## Key takeaways

- `id()` returns object identity (memory address)
- `type()` returns object type
- `isinstance()` is the correct type-checking tool
- `dir()` lists available attributes and methods
- `help()` displays documentation
- `del` removes references (not the object itself)
