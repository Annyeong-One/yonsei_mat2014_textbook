# Opening and Reading Files

File input/output (I/O) allows Python programs to read data from and write data to files on disk. Reading files is fundamental for data analysis and quantitative work.

---

## 1. Opening a file

Use the built-in `open()` function:

```python
f = open("data.txt", "r")
```

Common modes:
- `"r"`: read (default)
- `"w"`: write (truncate)
- `"a"`: append
- `"b"`: binary mode

---

## 2. Reading the entire file

```python
text = f.read()
```

This reads the entire file into a single string.

---

## 3. Reading line by line

```python
for line in f:
    print(line.strip())
```

This is memory-efficient and preferred for large files.

---

## 4. Reading into a list

```python
lines = f.readlines()
```

Each element is one line (including newline characters).

---

## 5. Closing files

Always close files when done:

```python
f.close()
```

Failing to close files can lead to resource leaks.

---

## Key takeaways

- Use `open()` to access files.
- Prefer line-by-line reading for large files.
- Always close files when finished.
