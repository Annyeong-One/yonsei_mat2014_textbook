


# Type Conversion Functions

Python includes several built-in functions for converting values between types.

These functions are essential when working with input data or performing numeric operations.

| Function | Description |
|---|---|
| int() | convert to integer |
| float() | convert to floating point |
| str() | convert to string |
| bool() | convert to boolean |
| list() | convert to list |
| tuple() | convert to tuple |
| set() | convert to set |

---

## int()

```python
x = int("10")
print(x)
````

Output

```
10
```

---

## float()

```python
y = float("3.14")
print(y)
```

---

## str()

```python
value = 100
text = str(value)

print(text)
```

---

## bool()

Falsy values include:

```
0
None
False
""
[]
{}
```

Example

```python
print(bool(0))
print(bool(42))
```

---

## Exercises

**Exercise 1.**
Type conversion functions are also constructors for their types. Predict the output:

```python
print(int())
print(float())
print(str())
print(bool())
print(list())
print(tuple())
print(set())
```

What is the "zero value" or "empty value" for each type? Why does calling these constructors with no arguments produce these defaults?

??? success "Solution to Exercise 1"
    Output:

    ```text
    0
    0.0

    False
    []
    ()
    set()
    ```

    Each type has a natural "zero" or "empty" value: `0` for `int`, `0.0` for `float`, `""` (empty string) for `str`, `False` for `bool`, `[]` for `list`, `()` for `tuple`, `set()` for `set`.

    These are the defaults because each type's constructor, when called with no arguments, returns the **identity element** or **empty container** for that type. This is a consistent design: every type has a well-defined "nothing" value.

---

**Exercise 2.**
`bool()` applies truthiness rules. Predict the output:

```python
print(bool(0), bool(1), bool(-1))
print(bool(""), bool(" "), bool("False"))
print(bool([]), bool([0]), bool([[]]))
```

Why is `bool("False")` `True`? Why is `bool([0])` `True`? What is the general rule Python uses to determine truthiness?

??? success "Solution to Exercise 2"
    Output:

    ```text
    False True True
    False True True
    False True True
    ```

    `bool("False")` is `True` because `"False"` is a **non-empty string**. Python does not parse the string content -- it only checks whether the string is empty. Any non-empty string is truthy, regardless of what it says.

    `bool([0])` is `True` because the list is **non-empty** (it contains one element). The truthiness of containers depends on their length, not their contents.

    The general rule: a value is falsy if it is a "zero" or "empty" value: `0`, `0.0`, `""`, `None`, `False`, `[]`, `()`, `{}`, `set()`. Everything else is truthy. Custom classes can define `__bool__()` or `__len__()` to customize this behavior.

---

**Exercise 3.**
Some type conversions lose information. For each conversion, state whether information is preserved or lost:

```python
print(int(3.9))
print(float(3))
print(str(42))
print(int("42"))
print(list("abc"))
print(tuple([1, 2, 3]))
print(set([1, 2, 2, 3]))
```

Which conversions are **reversible** (you can convert back and get the original value)? Which are **lossy** (information is permanently lost)?

??? success "Solution to Exercise 3"
    | Conversion | Reversible? | Notes |
    |-----------|------------|-------|
    | `int(3.9)` = `3` | **Lossy** | The fractional part `.9` is permanently lost |
    | `float(3)` = `3.0` | Reversible | `int(3.0)` gives `3` |
    | `str(42)` = `"42"` | Reversible | `int("42")` gives `42` |
    | `int("42")` = `42` | Reversible | `str(42)` gives `"42"` |
    | `list("abc")` = `["a", "b", "c"]` | Reversible | `"".join(["a", "b", "c"])` gives `"abc"` |
    | `tuple([1, 2, 3])` = `(1, 2, 3)` | Reversible | `list((1, 2, 3))` gives `[1, 2, 3]` |
    | `set([1, 2, 2, 3])` = `{1, 2, 3}` | **Lossy** | Duplicates and order are permanently lost |

    The lossy conversions are `int(float)` (truncation loses fractional part) and `set(list)` (deduplication loses duplicates and ordering). These are one-way operations -- you cannot recover the original value.
