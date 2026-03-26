
# Parameters

Functions become much more useful when they can accept **inputs**.
Inputs allow the same function to work with different values each time it is called.

## The Problem

Consider this function from the previous page:

```python
def greet():
    print("=" * 30)
    print("  Welcome, Alice")
    print("=" * 30)

greet()
greet()
```

Output

```text
==============================
  Welcome, Alice
==============================
==============================
  Welcome, Alice
==============================
```

This function always welcomes **Alice**.
What if we want to welcome different people?

## The Solution

We can add a **parameter** so the function accepts a value.

```python
def greet(name):
    print("=" * 30)
    print("  Welcome,", name)
    print("=" * 30)

greet("Alice")
greet("Bob")
```

Output

```text
==============================
  Welcome, Alice
==============================
==============================
  Welcome, Bob
==============================
```

The function now accepts a value that can change each time it is called.
When we call `greet("Alice")`, Python assigns `"Alice"` to the parameter `name` inside the function body.

## Parameters and Arguments

A **parameter** is a variable listed in the function definition.

An **argument** is the value supplied when the function is called.

```python
def greet(name):
    print("Welcome,", name)

greet("Alice")
```

Here:

- `name` is the **parameter**
- `"Alice"` is the **argument**

## Multiple Parameters

Functions can accept more than one parameter.

```python
def describe(name, age):
    print(name, "is", age, "years old")

describe("Alice", 25)
describe("Bob", 30)
```

Output

```text
Alice is 25 years old
Bob is 30 years old
```

Each parameter receives its own value when the function is called.
The order of the arguments must match the order of the parameters.

## Default Parameters

Parameters can have **default values**.
This is a preview — we will see more uses of default values in later pages.

```python
def greet(name="guest"):
    print("Welcome,", name)

greet()
greet("Alice")
```

Output

```text
Welcome, guest
Welcome, Alice
```

When no argument is provided, the parameter uses its default value.
When an argument is provided, it overrides the default.

## Key Ideas

Parameters let a function accept different inputs each time it is called.
The parameter name appears in the `def` line; the argument value appears in the call.
When a function has multiple parameters, arguments are matched to parameters by position.

Next: [Return Values](return_values.md).
