
# print() and input()

Python provides two fundamental built-in functions for interacting with users:

| Function | Purpose |
|---|---|
| `print()` | display output |
| `input()` | receive user input |

These functions enable simple **input/output interaction** in programs.

```mermaid2
flowchart LR
    A[Program] --> B[input()]
    B --> C[User]
    C --> D[print()]
    D --> A
````

---

## print()

`print()` displays information to the console.

### Example

```python
print("Hello Python")
```

Output

```
Hello Python
```

---

## Multiple Values

```python
name = "Alice"
age = 25

print(name, age)
```

Output

```
Alice 25
```

---

## Separator and End

```python
print("A","B","C",sep="-")
```

Output

```
A-B-C
```

Example

```python
print("Hello", end=" ")
print("World")
```

Output

```
Hello World
```

---

## input()

`input()` reads user input from the keyboard.

Example

```python
name = input("Enter your name: ")
print("Hello", name)
```

---

## Important Note

`input()` always returns a **string**.

Example

```python
age = input("Enter age: ")
print(type(age))
```

Output

```
<class 'str'>
```

Convert values if needed:

```python
age = int(input("Enter age: "))
```