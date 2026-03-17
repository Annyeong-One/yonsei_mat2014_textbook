
# Conditional Statements

Conditional statements allow a program to **execute code only when certain conditions are satisfied**.

The primary conditional structure in Python is the `if` statement.

---

### Basic if Statement

```python
age = 25

if age >= 18:
    print("You are an adult")
````

If the condition evaluates to `True`, the indented block executes.

---

### if–else Statement

```python
temperature = 15

if temperature > 20:
    print("Warm")
else:
    print("Cool")
```

The `else` block executes when the condition is `False`.

---

### Multiple Conditions (if–elif–else)

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

Python evaluates conditions **top to bottom**, executing the first match.

---

### Logical Operators

Python allows combining conditions using logical operators.

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | both conditions must be true        |
| `or`     | at least one condition must be true |
| `not`    | reverses a condition                |

Example:

```python
age = 22
has_license = True

if age >= 18 and has_license:
    print("You can drive")
```

---

### Truthy and Falsy Values

Python treats some values as `False` automatically.

Falsy values include:

```
0
None
False
""
[]
{}
```

Everything else is considered **truthy**.

Example:

```python
name = ""

if name:
    print("Hello")
else:
    print("Name missing")
```

---

### Nested Conditionals

Conditional blocks can appear inside other conditional blocks.

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
```

However, excessive nesting can make programs harder to read.

````

---

# loops.md

```md
## Loops

Loops allow programs to **repeat a block of code multiple times**.

Python provides two primary looping constructs:

- `for` loops
- `while` loops

```mermaid2
flowchart TD
    A[Start Loop] --> B[Check Condition]
    B -->|True| C[Execute Block]
    C --> B
    B -->|False| D[Exit Loop]
````

---

### for Loop

The `for` loop iterates over an iterable object.

```python
for item in iterable:
    statement
```

Example:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

Output:

```
apple
banana
cherry
```

---

### range()

The `range()` function generates sequences of numbers.

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

Other forms:

```python
range(start, stop)
range(start, stop, step)
```

Example:

```python
for i in range(2,10,2):
    print(i)
```

---

### Nested Loops

Loops can be placed inside other loops.

```python
for i in range(3):
    for j in range(3):
        print(i,j)
```

Nested loops are often used in **matrix operations or grid computations**.

---

## while Loop

The `while` loop continues executing while a condition remains true.

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Output:

```
0
1
2
3
4
```

---

## Infinite Loops

A `while True` loop creates an infinite loop.

```python
while True:
    command = input("> ")

    if command == "quit":
        break
```

This pattern is common in **interactive programs and servers**.
