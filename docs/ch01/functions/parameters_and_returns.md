

# Parameters and Returns

Functions become much more useful when they can **accept input** and **produce output**.

This section covers:

- parameters
- arguments
- return values
- default parameters
- keyword arguments

```mermaid2
flowchart LR
    A[Arguments] --> B[Function]
    B --> C[Return value]
````

---

## 1. Parameters and Arguments

A **parameter** is a variable listed in a function definition.

An **argument** is the actual value passed to the function when it is called.

```python
def greet(name):
    print("Hello,", name)

greet("Alice")
```

Here:

* `name` is the parameter
* `"Alice"` is the argument

---

## 2. Functions with Multiple Parameters

Functions may accept multiple parameters.

```python
def add(a, b):
    print(a + b)

add(3, 4)
```

Output:

```text
7
```

Parameters allow one function definition to work with many different values.

---

## 3. Return Values

A function can send a value back to the caller using `return`.

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
```

Output:

```text
7
```

The returned value can be stored, printed, or used in larger expressions.

```python
print(add(2, 5) * 2)
```

---

## 4. Returning Multiple Values

Python functions can return multiple values separated by commas.

```python
def min_max(a, b):
    if a < b:
        return a, b
    return b, a

small, large = min_max(10, 3)
print(small, large)
```

Output:

```text
3 10
```

Technically, Python returns a tuple.

---

## 5. Default Parameters

A parameter can have a default value.

```python
def greet(name="guest"):
    print("Hello,", name)

greet()
greet("Alice")
```

Output:

```text
Hello, guest
Hello, Alice
```

Default parameters make functions more flexible.

---

## 6. Keyword Arguments

Arguments can be passed by name.

```python
def describe(name, age):
    print(name, age)

describe(age=25, name="Alice")
```

Keyword arguments improve readability and allow arguments to be supplied out of order.

---

## 7. Positional vs Keyword Arguments

Most function calls use positional arguments:

```python
describe("Alice", 25)
```

But keyword arguments are often clearer when a function has many parameters.

---

## 8. Early Return

A function may return early depending on a condition.

```python
def reciprocal(x):
    if x == 0:
        return None
    return 1 / x
```

This pattern is useful for validation and guard clauses.

---

## 9. Worked Examples

### Example 1: area function

```python
def area(length, width):
    return length * width

print(area(3, 4))
```

Output:

```text
12
```

### Example 2: greeting with default

```python
def greet(name="friend"):
    return f"Hello, {name}"

print(greet())
print(greet("Sam"))
```

### Example 3: keyword arguments

```python
def power(base, exponent):
    return base ** exponent

print(power(exponent=3, base=2))
```

Output:

```text
8
```

---

## 10. Common Pitfalls

### Printing instead of returning

```python
def add(a, b):
    print(a + b)
```

This displays the result, but does not return it.

### Using mutable defaults

Default arguments should be chosen carefully. Mutable defaults are a later topic, but they can cause surprising behavior.

### Forgetting the returned value

A function may compute something useful, but that value is lost if it is ignored.

---

## 11. Summary

Key ideas:

* parameters receive inputs inside the function
* arguments provide values at call time
* `return` sends a value back to the caller
* functions can have default parameters
* keyword arguments improve readability
* returning is different from printing

Parameters and return values are what make functions truly useful as computational tools.