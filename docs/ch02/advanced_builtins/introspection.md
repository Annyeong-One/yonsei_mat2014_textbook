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

---

## Exercises


**Exercise 1.**
Write a function `list_methods(obj)` that takes any object and returns a sorted list of its public method names (names that do not start with `_` and are callable). Test it with a list and a string.

??? success "Solution to Exercise 1"

        ```python
        def list_methods(obj):
            return sorted(
                name for name in dir(obj)
                if not name.startswith("_") and callable(getattr(obj, name))
            )

        print(list_methods([]))    # ['append', 'clear', 'copy', ...]
        print(list_methods(""))    # ['capitalize', 'casefold', 'center', ...]
        ```

    `dir(obj)` returns all attribute names. Filtering out names starting with `_` removes dunder methods and private attributes. Checking `callable(getattr(obj, name))` ensures only methods are included.

---

**Exercise 2.**
Given the class below, use `type()`, `isinstance()`, and `hasattr()` to answer the following questions in code: What is the type of `d`? Is `d` an instance of `Animal`? Does `d` have an attribute called `speak`?

```python
class Animal:
    pass

class Dog(Animal):
    def speak(self):
        return "Woof"

d = Dog()
```

??? success "Solution to Exercise 2"

        ```python
        class Animal:
            pass

        class Dog(Animal):
            def speak(self):
                return "Woof"

        d = Dog()

        print(type(d))                  # <class '__main__.Dog'>
        print(isinstance(d, Animal))    # True
        print(hasattr(d, "speak"))      # True
        ```

    `type(d)` returns `Dog`, but `isinstance(d, Animal)` returns `True` because `Dog` inherits from `Animal`. `hasattr` checks whether the attribute exists on the object or its class hierarchy.

---

**Exercise 3.**
Write a function `inspect_object(obj)` that prints the object's type, its `id`, the number of attributes returned by `dir()`, and whether it is callable. Test it with an integer, a string, and a lambda function.

??? success "Solution to Exercise 3"

        ```python
        def inspect_object(obj):
            print(f"Type: {type(obj)}")
            print(f"ID: {id(obj)}")
            print(f"Attributes: {len(dir(obj))}")
            print(f"Callable: {callable(obj)}")
            print()

        inspect_object(42)
        inspect_object("hello")
        inspect_object(lambda x: x)
        ```

    Integers and strings are not callable, so `callable` returns `False` for them. Lambda functions are callable, so it returns `True`.
