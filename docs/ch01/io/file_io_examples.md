
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

## Exercises

**Exercise 1.**
Write a program that creates a file called `names.txt` containing five names (one per line), then reads the file back and prints each name in uppercase.

??? success "Solution to Exercise 1"
    ```python
    # Write names
    with open("names.txt", "w") as f:
        for name in ["Alice", "Bob", "Carol", "Dave", "Eve"]:
            f.write(name + "\n")

    # Read and print in uppercase
    with open("names.txt") as f:
        for line in f:
            print(line.strip().upper())
    ```

    Output:

    ```
    ALICE
    BOB
    CAROL
    DAVE
    EVE
    ```

    `strip()` removes the trailing newline from each line before calling `upper()`.

---

**Exercise 2.**
Predict the output of the following program. What does the `get` method do when the key is not found?

```python
counts = {}
words = ["the", "cat", "sat", "on", "the", "mat", "the"]

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
```

??? success "Solution to Exercise 2"
    Output:

    ```
    {'the': 3, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
    ```

    `counts.get(word, 0)` returns the current count for `word` if it exists, or `0` if the key is not yet in the dictionary. Adding 1 and assigning back increments the count. This is a standard word-counting pattern.

---

**Exercise 3.**
Write a program that reads a CSV string (not a file) and converts it into a list of dictionaries. Use the first row as headers.

```python
csv_text = """name,age,city
Alice,30,Paris
Bob,25,London
Carol,35,Tokyo"""
```

??? success "Solution to Exercise 3"
    ```python
    csv_text = """name,age,city
    Alice,30,Paris
    Bob,25,London
    Carol,35,Tokyo"""

    lines = csv_text.strip().split("\n")
    headers = lines[0].split(",")
    records = []

    for line in lines[1:]:
        values = line.strip().split(",")
        record = {}
        for h, v in zip(headers, values):
            record[h] = v
        records.append(record)

    print(records)
    ```

    Output:

    ```
    [{'name': 'Alice', 'age': '30', 'city': 'Paris'},
     {'name': 'Bob', 'age': '25', 'city': 'London'},
     {'name': 'Carol', 'age': '35', 'city': 'Tokyo'}]
    ```

    The first line provides the keys. Each subsequent line is split and zipped with the headers to form a dictionary.

---

**Exercise 4.**
Explain why the `with` statement is preferred over manually calling `f.close()`. Describe a scenario where forgetting to close a file could cause problems.

??? success "Solution to Exercise 4"
    The `with` statement is preferred because it guarantees the file is closed when the block exits, even if an exception occurs. For example:

    ```python
    with open("data.txt") as f:
        data = f.read()
        # If an error occurs here, the file is still closed
    ```

    Without `with`, you must call `f.close()` manually:

    ```python
    f = open("data.txt")
    data = f.read()
    f.close()  # Forgotten if an exception occurs above
    ```

    A scenario where this causes problems: if a program writes to a file without closing it, the data may remain in a memory buffer and never be flushed to disk. If the program crashes before `close()` is called, the file may be empty or incomplete. On some operating systems, an unclosed file also holds a lock that prevents other programs from accessing it.

---

**Exercise 5.**
Write a program that uses the `json` module to save a dictionary to a file and then load it back. Verify that the loaded data is equal to the original.

```python
import json

original = {"name": "Alice", "scores": [90, 85, 92], "active": True}
```

??? success "Solution to Exercise 5"
    ```python
    import json

    original = {"name": "Alice", "scores": [90, 85, 92], "active": True}

    # Save to file
    with open("data.json", "w") as f:
        json.dump(original, f)

    # Load from file
    with open("data.json") as f:
        loaded = json.load(f)

    print(loaded)
    print(original == loaded)
    ```

    Output:

    ```
    {'name': 'Alice', 'scores': [90, 85, 92], 'active': True}
    True
    ```

    `json.dump` serializes the dictionary to JSON format and writes it to the file. `json.load` reads the file and deserializes the JSON back into a Python dictionary. The `==` comparison confirms the round-trip preserves the data.
