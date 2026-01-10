# Writing Files

Writing files allows programs to persist results, logs, and data.

---

## Opening a file for

```python
f = open("output.txt", "w")
```

Warning:
- `"w"` overwrites existing files.
- `"a"` appends instead.

---

## Writing text

```python
f.write("Hello\n")
f.write("World\n")
```

`write()` returns the number of characters written.

---

## Writing multiple

```python
lines = ["a\n", "b\n", "c\n"]
f.writelines(lines)
```

No automatic newlines are added.

---

## Flushing output

```python
f.flush()
```

Forces buffered data to disk without closing the file.

---

## Key takeaways

- Use `"w"` to overwrite, `"a"` to append.
- `write()` does not add newlines automatically.
- Flush or close to ensure data is written.
