
# Input and Output Utilities

Python provides the `open()` built-in function for reading from and writing to files. The `with` statement ensures that files are properly closed after use, even if an exception occurs.

## Writing Files

```python
with open("data.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")
```

## Reading Files

```python
with open("data.txt") as f:
    text = f.read()
print(text)
```

You can also read line by line:

```python
with open("data.txt") as f:
    for line in f:
        print(line.strip())
```

## File Modes

| Mode | Meaning | Creates file? | Overwrites? |
|------|---------|---------------|-------------|
| `"r"` | Read (default) | No | No |
| `"w"` | Write | Yes | Yes |
| `"a"` | Append | Yes | No |
| `"x"` | Exclusive create | Yes | Raises error if exists |
| `"rb"` | Read binary | No | No |
| `"wb"` | Write binary | Yes | Yes |

!!! tip "Always Use `with`"
    The `with` statement guarantees that the file is closed when the block exits, even if an error occurs. Avoid calling `f.close()` manually.
