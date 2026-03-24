
# Input and Output Utilities

Python provides the `open()` built-in function for reading from and writing to files. The `with` statement ensures that files are properly closed after use.

## Writing Files

```python
with open("data.txt","w") as f:
    f.write("Hello")
```

## Reading Files

```python
with open("data.txt") as f:
    text = f.read()
```

## File Modes

| Mode | Meaning |
| ---- | ------- |
| r    | read    |
| w    | write   |
| a    | append  |
