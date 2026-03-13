
# CSV and JSON Basics

Many programs exchange data using common text formats such as **CSV** and **JSON**.

These formats allow data to be stored and shared between systems.

```mermaid2
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