
# Common Runtime Errors

Programs may encounter various runtime errors during execution.

Understanding the most common errors helps programmers debug code quickly.

```mermaid2
flowchart TD
    A[Runtime Errors]
    A --> B[TypeError]
    A --> C[ValueError]
    A --> D[IndexError]
    A --> E[KeyError]
    A --> F[ZeroDivisionError]
````

---

## 1. TypeError

Occurs when an operation is applied to incompatible types.

Example:

```python
"hello" + 5
```

Output:

```text
TypeError: can only concatenate str (not "int") to str
```

---

## 2. ValueError

Occurs when a function receives a value of the correct type but an inappropriate value.

Example:

```python
int("hello")
```

Output:

```text
ValueError: invalid literal for int()
```

---

## 3. IndexError

Occurs when accessing an invalid index in a sequence.

```python
numbers = [1, 2, 3]
print(numbers[10])
```

Output:

```text
IndexError: list index out of range
```

---

## 4. KeyError

Occurs when accessing a missing dictionary key.

```python
data = {"a": 1}
print(data["b"])
```

Output:

```text
KeyError: 'b'
```

---

## 5. ZeroDivisionError

Occurs when dividing by zero.

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError
```

---

## 6. NameError

Occurs when a variable name is not defined.

```python
print(x)
```

Output:

```text
NameError: name 'x' is not defined
```

---

## 7. AttributeError

Occurs when accessing a nonexistent attribute.

```python
x = 5
x.append(3)
```

Output:

```text
AttributeError: 'int' object has no attribute 'append'
```

---

## 8. Worked Examples

### Example 1: safe dictionary access

```python
data = {"a": 1}

print(data.get("b"))
```

Output:

```text
None
```

### Example 2: checking length before indexing

```python
values = [1, 2]

if len(values) > 3:
    print(values[3])
```

---

## 9. Summary

Key ideas:

* runtime errors occur during execution
* different exception types describe different problems
* recognizing common exceptions helps with debugging
* careful checks can prevent some errors