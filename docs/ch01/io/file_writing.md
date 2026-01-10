# Writing Files

Writing files allows programs to persist results, logs, and data.

---

## 1. Opening a file for writing

```python
f = open("output.txt", "w")
```

Warning:
- `"w"` overwrites existing files.
- `"a"` appends instead.

---

## 2. Writing text

```python
f.write("Hello\n")
f.write("World\n")
```

`write()` returns the number of characters written.

---

## 3. Writing multiple lines

```python
lines = ["a\n", "b\n", "c\n"]
f.writelines(lines)
```

No automatic newlines are added.

---

## 4. Flushing output

```python
f.flush()
```

Forces buffered data to disk without closing the file.

---

## Key takeaways

- Use `"w"` to overwrite, `"a"` to append.
- `write()` does not add newlines automatically.
- Flush or close to ensure data is written.
