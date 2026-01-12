# CSV and JSON

CSV and JSON are standard formats for data exchange. Python's standard library provides dedicated modules for parsing and generating both formats.

## CSV Reading

The `csv` module parses comma-separated value files.

### 1. Basic Reader

Read CSV rows as lists of strings.

```python
import csv

with open("data.csv", "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ['value1', 'value2', 'value3']
```

### 2. With Headers

Use `DictReader` to access columns by name.

```python
import csv

# data.csv:
# name,age,city
# Alice,30,Seoul
# Bob,25,Busan

with open("data.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
# Alice 30
# Bob 25
```

### 3. Custom Delimiters

Handle non-comma separators and quotes.

```python
import csv

# Tab-separated file
with open("data.tsv", "r", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)

# Custom quote character
with open("data.csv", "r", newline="") as f:
    reader = csv.reader(f, quotechar="'")
    for row in reader:
        print(row)
```

## CSV Writing

Write data to CSV format files.

### 1. Basic Writer

Write rows as lists.

```python
import csv

data = [
    ["name", "age", "city"],
    ["Alice", 30, "Seoul"],
    ["Bob", 25, "Busan"]
]

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

### 2. Dict Writer

Write rows from dictionaries.

```python
import csv

data = [
    {"name": "Alice", "age": 30, "city": "Seoul"},
    {"name": "Bob", "age": 25, "city": "Busan"}
]

with open("output.csv", "w", newline="") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(data)
```

### 3. Quoting Options

Control when values are quoted.

```python
import csv

data = [["Name", "Description"], ["Test", "Has, comma"]]

# Quote all fields
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(data)
# "Name","Description"
# "Test","Has, comma"

# Quote only when needed (default)
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(data)
# Name,Description
# Test,"Has, comma"
```

## JSON Reading

The `json` module parses JSON formatted data.

### 1. Load From File

Parse JSON file into Python objects.

```python
import json

# data.json:
# {"name": "Alice", "scores": [95, 87, 92]}

with open("data.json", "r") as f:
    data = json.load(f)

print(data["name"])       # Alice
print(data["scores"][0])  # 95
print(type(data))         # <class 'dict'>
```

### 2. Load From String

Parse JSON string directly.

```python
import json

json_str = '{"name": "Bob", "active": true, "count": null}'

data = json.loads(json_str)
print(data["name"])       # Bob
print(data["active"])     # True (bool)
print(data["count"])      # None
```

### 3. Type Mapping

JSON types map to Python types automatically.

```python
import json

json_str = '''
{
    "string": "hello",
    "number": 42,
    "float": 3.14,
    "boolean": true,
    "null": null,
    "array": [1, 2, 3],
    "object": {"nested": "value"}
}
'''

data = json.loads(json_str)
# string -> str
# number -> int
# float -> float
# boolean -> bool
# null -> None
# array -> list
# object -> dict
```

## JSON Writing

Serialize Python objects to JSON format.

### 1. Dump To File

Write Python data as JSON file.

```python
import json

data = {
    "name": "Alice",
    "scores": [95, 87, 92],
    "active": True
}

with open("output.json", "w") as f:
    json.dump(data, f)
```

### 2. Dump To String

Convert to JSON string.

```python
import json

data = {"name": "Bob", "age": 30}

json_str = json.dumps(data)
print(json_str)  # {"name": "Bob", "age": 30}
```

### 3. Formatting Options

Control output formatting for readability.

```python
import json

data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}

# Compact (default)
print(json.dumps(data))
# {"users": [{"name": "Alice"}, {"name": "Bob"}]}

# Pretty printed
print(json.dumps(data, indent=2))
# {
#   "users": [
#     {"name": "Alice"},
#     {"name": "Bob"}
#   ]
# }

# Sorted keys
print(json.dumps(data, sort_keys=True))
```

## Advanced JSON

Handle complex serialization scenarios.

### 1. Non-Serializable Types

Handle types JSON doesn't support natively.

```python
import json
from datetime import datetime

data = {"timestamp": datetime.now()}

# Fails: TypeError
# json.dumps(data)

# Solution 1: Custom default function
def json_default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Not serializable: {type(obj)}")

result = json.dumps(data, default=json_default)
print(result)  # {"timestamp": "2025-01-12T14:30:00"}
```

### 2. Custom Encoder

Create reusable encoder class.

```python
import json
from datetime import datetime, date
from decimal import Decimal

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)

data = {
    "date": date(2025, 1, 12),
    "price": Decimal("19.99"),
    "tags": {"python", "json"}
}

result = json.dumps(data, cls=CustomEncoder)
print(result)
```

### 3. Custom Decoder

Parse JSON with custom object creation.

```python
import json
from datetime import datetime

def decode_datetime(dct):
    """Convert ISO strings back to datetime."""
    for key, value in dct.items():
        if isinstance(value, str):
            try:
                dct[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return dct

json_str = '{"created": "2025-01-12T14:30:00"}'
data = json.loads(json_str, object_hook=decode_datetime)
print(type(data["created"]))  # <class 'datetime.datetime'>
```

## Error Handling

Handle parsing errors gracefully.

### 1. CSV Errors

Handle malformed CSV data.

```python
import csv

try:
    with open("data.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader, 1):
            if len(row) != 3:
                print(f"Line {i}: Expected 3 columns")
                continue
            process(row)
except csv.Error as e:
    print(f"CSV error: {e}")
except FileNotFoundError:
    print("File not found")
```

### 2. JSON Errors

Handle invalid JSON gracefully.

```python
import json

def safe_json_load(filepath):
    """Load JSON with error handling."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON at line {e.lineno}: {e.msg}")
        return None

data = safe_json_load("config.json")
```

### 3. Validation Pattern

Validate structure after parsing.

```python
import json

def load_config(filepath):
    """Load and validate configuration."""
    with open(filepath, "r") as f:
        config = json.load(f)
    
    # Validate required fields
    required = ["database", "port", "debug"]
    missing = [k for k in required if k not in config]
    
    if missing:
        raise ValueError(f"Missing config keys: {missing}")
    
    # Validate types
    if not isinstance(config["port"], int):
        raise TypeError("port must be integer")
    
    return config
```

## Practical Patterns

Common real-world usage patterns.

### 1. CSV to Dict List

Convert CSV to list of dictionaries.

```python
import csv

def csv_to_dicts(filepath):
    """Read CSV as list of dicts."""
    with open(filepath, "r", newline="") as f:
        return list(csv.DictReader(f))

records = csv_to_dicts("users.csv")
for r in records:
    print(r["name"])
```

### 2. JSON Config File

Load application configuration.

```python
import json
from pathlib import Path

def load_config(name="config.json"):
    """Load JSON config with defaults."""
    defaults = {
        "debug": False,
        "port": 8080,
        "host": "localhost"
    }
    
    path = Path(name)
    if path.exists():
        with open(path) as f:
            user_config = json.load(f)
        defaults.update(user_config)
    
    return defaults

config = load_config()
```

### 3. Data Conversion

Convert between CSV and JSON formats.

```python
import csv
import json

def csv_to_json(csv_path, json_path):
    """Convert CSV file to JSON."""
    with open(csv_path, "r", newline="") as f:
        data = list(csv.DictReader(f))
    
    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)

def json_to_csv(json_path, csv_path):
    """Convert JSON array to CSV."""
    with open(json_path, "r") as f:
        data = json.load(f)
    
    if not data:
        return
    
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
```
