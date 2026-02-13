# json.dump and json.load (File I/O)

`dump()` writes JSON to a file, while `load()` reads JSON from a file.

## dump - Write JSON to File

Write JSON data directly to a file.

```python
import json
import tempfile
import os

data = {
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
}

# Write to file
with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
    json.dump(data, f)
    temp_path = f.name

# Verify
with open(temp_path) as f:
    print(f.read())

os.unlink(temp_path)
```

```
{"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}
```

## load - Read JSON from File

Read JSON data directly from a file.

```python
import json
import tempfile
import os

# Create temporary JSON file
data = {"config": {"host": "localhost", "port": 8080}}
with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
    json.dump(data, f)
    temp_path = f.name

# Load from file
with open(temp_path) as f:
    loaded = json.load(f)
    print(loaded)
    print(f"Host: {loaded['config']['host']}")

os.unlink(temp_path)
```

```
{'config': {'host': 'localhost', 'port': 8080}}
Host: localhost
```

