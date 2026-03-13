

# Input and Output Utilities

Python programs frequently read from and write to files.

---

## Writing Files

```python
with open("data.txt","w") as f:
    f.write("Hello")
````

---

## Reading Files

```python
with open("data.txt") as f:
    text = f.read()
```

---

## File Modes

| Mode | Meaning |
| ---- | ------- |
| r    | read    |
| w    | write   |
| a    | append  |

````