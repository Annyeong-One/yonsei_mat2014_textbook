
# Parameters

Functions become much more useful when they can accept **inputs**.
Inputs allow the same function to work with different values.

---

## The Problem

Consider this function:

```python
def greet():
    print("Hello Alice")

greet()
greet()
greet()
```

Output

```text
Hello Alice
Hello Alice
Hello Alice
```

This function always greets **Alice**.
What if we want to greet different people?

---

## The Solution

We can add a **parameter** so the function accepts a value.

```python
def greet(name):
    print("Hello", name)

greet("Alice")
greet("Bob")
greet("Charlie")
```

Output

```text
Hello Alice
Hello Bob
Hello Charlie
```

The function now accepts a value that can change each time it is called.
The value passed to the function replaces the parameter inside the function body.
Each time the function is called, a new value is assigned to the parameter.

```mermaid
flowchart LR
    A["Alice"] --> B["greet(name)"]
    B --> C["print(Hello Alice)"]
```

---

## Parameters and Arguments

A **parameter** is a variable listed in the function definition.

An **argument** is the value supplied when the function is called.

```python
def greet(name):
    print("Hello", name)

greet("Alice")
```

Here:

- `name` is the **parameter**
- `"Alice"` is the **argument**

---

## Multiple Parameters

Functions can accept multiple parameters.

```python
def add(a, b):
    return a + b

print(add(3, 4))
```

Output

```text
7
```

Each parameter receives its own value when the function is called.

---

## Default Parameters

Parameters can have **default values**.

```python
def greet(name="guest"):
    print("Hello", name)

greet()
greet("Alice")
```

Output

```text
Hello guest
Hello Alice
```

Default parameters make functions easier to call.

---

## Keyword Arguments

Arguments can be supplied using the parameter name.

```python
def describe(name, age):
    print(name, age)

describe(age=25, name="Alice")
```

Keyword arguments:

- improve readability
- allow arguments to appear in any order

---

## Positional vs Keyword Arguments

Most calls use **positional arguments**.

```python
describe("Alice", 25)
```

Keyword arguments are helpful when a function has many parameters.

---

## Summary

Key ideas:

- parameters define inputs for a function
- arguments provide values when calling the function
- functions can have multiple parameters
- parameters can have default values
- keyword arguments improve readability
