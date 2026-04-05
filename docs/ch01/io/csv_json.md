
# CSV and JSON Basics

Many programs exchange data using common text formats such as **CSV** and **JSON**.

These formats allow data to be stored and shared between systems.

```mermaid
flowchart LR
    A[Program] --> B[CSV]
    A --> C[JSON]
    B --> D[Spreadsheet tools]
    C --> E[Web APIs]
````

---

## 1. CSV Files

CSV stands for **Comma-Separated Values**.

Example file:

```text
name,age
Alice,25
Bob,30
```

---

## 2. Reading CSV

Python provides the `csv` module.

```python
import csv

with open("data.csv") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)
```

---

## 3. Writing CSV

```python
import csv

with open("out.csv", "w") as f:
    writer = csv.writer(f)

    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 25])
```

---

## 4. JSON Files

JSON (JavaScript Object Notation) is widely used for structured data.

Example JSON:

```json
{
  "name": "Alice",
  "age": 25
}
```

---

## 5. Reading JSON

```python
import json

with open("data.json") as f:
    data = json.load(f)

print(data)
```

---

## 6. Writing JSON

```python
import json

data = {"name": "Alice", "age": 25}

with open("data.json", "w") as f:
    json.dump(data, f)
```

---


## 7. Summary

Key ideas:

* CSV represents tabular data
* JSON represents structured data
* Python provides `csv` and `json` modules
* these formats are widely used for data exchange


## Exercises

**Exercise 1.**
`csv.reader` returns lists of strings, not typed values. Predict the output:

```python
import csv
import io

data = "name,age\nAlice,25\nBob,30"
reader = csv.reader(io.StringIO(data))
header = next(reader)
first_row = next(reader)
print(first_row)
print(type(first_row[1]))
print(first_row[1] + 5)
```

Why does the last line fail? What must you do to work with numeric CSV data? How does `csv.DictReader` improve upon `csv.reader`?

??? success "Solution to Exercise 1"
    Output:

    ```text
    ['Alice', '25']
    <class 'str'>
    ```

    Then `first_row[1] + 5` raises `TypeError: can only concatenate str (not "int") to str` because `first_row[1]` is the string `"25"`, not the integer `25`.

    CSV files are plain text -- the `csv` module reads all values as strings. To work with numeric data, you must convert explicitly: `int(first_row[1])` or `float(first_row[1])`.

    `csv.DictReader` improves upon `csv.reader` by using the header row as keys:

    ```python
    reader = csv.DictReader(io.StringIO(data))
    for row in reader:
        print(row["name"], int(row["age"]))
    ```

    Each row becomes a dictionary (`{"name": "Alice", "age": "25"}`), making field access clearer than numeric indices.

---

**Exercise 2.**
`json.loads()` converts JSON strings to Python objects. Predict the Python types:

```python
import json

data = json.loads('{"name": "Alice", "age": 25, "scores": [90, 85], "active": true, "address": null}')
print(type(data))
print(type(data["age"]))
print(type(data["scores"]))
print(type(data["active"]))
print(type(data["address"]))
```

How does JSON map to Python types? What JSON types have no direct Python equivalent, and vice versa?

??? success "Solution to Exercise 2"
    Output:

    ```text
    <class 'dict'>
    <class 'int'>
    <class 'list'>
    <class 'bool'>
    <class 'NoneType'>
    ```

    JSON to Python type mapping:

    | JSON | Python |
    |------|--------|
    | object `{}` | `dict` |
    | array `[]` | `list` |
    | string | `str` |
    | number (integer) | `int` |
    | number (decimal) | `float` |
    | `true`/`false` | `True`/`False` |
    | `null` | `None` |

    JSON types with no Python equivalent: none (all JSON types map to Python). Python types with no JSON equivalent: `tuple` (serialized as array), `set` (not serializable), `bytes`, `datetime`, `complex`, and custom objects. This asymmetry means you must handle these types specially when serializing.

---

**Exercise 3.**
A programmer tries to serialize a Python object to JSON:

```python
import json
from datetime import datetime

data = {"timestamp": datetime.now(), "values": {1, 2, 3}}
json.dumps(data)
```

This raises `TypeError`. Which values in the dictionary are not JSON-serializable? Why does JSON only support certain types? Show how to handle this by providing a custom serialization approach.

??? success "Solution to Exercise 3"
    Two values are not JSON-serializable: `datetime.now()` (a `datetime` object) and `{1, 2, 3}` (a `set`). JSON only supports strings, numbers, booleans, null, arrays, and objects.

    JSON supports only these types because it is a **data interchange format** designed for simplicity and cross-language compatibility. Every programming language can represent these basic types.

    Custom serialization approach:

    ```python
    import json
    from datetime import datetime

    def custom_serializer(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, set):
            return list(obj)
        raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

    data = {"timestamp": datetime.now(), "values": {1, 2, 3}}
    result = json.dumps(data, default=custom_serializer)
    print(result)
    ```

    The `default` parameter provides a function that converts non-serializable objects to serializable ones. This is the standard pattern for extending JSON serialization in Python.
