
# File I/O Examples

This section collects practical examples combining file reading, writing, and structured formats.

---

## 1. Copying a File

```python
with open("input.txt") as f1, open("output.txt", "w") as f2:
    for line in f1:
        f2.write(line)
````

---

## 2. Counting Lines

```python
count = 0

with open("data.txt") as f:
    for line in f:
        count += 1

print(count)
```

---

## 3. Writing Numbers

```python
with open("numbers.txt", "w") as f:
    for i in range(5):
        f.write(str(i) + "\n")
```

---

## 4. JSON Configuration

```python
import json

config = {"debug": True}

with open("config.json", "w") as f:
    json.dump(config, f)
```

---

## 5. CSV Processing

```python
import csv

with open("data.csv") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)
```

---

## 6. Practical Example: Word Count

```python
counts = {}

with open("text.txt") as f:
    for word in f.read().split():
        counts[word] = counts.get(word, 0) + 1

print(counts)
```

---

## 7. Summary

These examples demonstrate:

* reading files
* writing files
* copying data
* processing structured formats
* practical file-based workflows

File I/O connects Python programs to external data and persistent storage.

