# Formatting and Pretty Printing

Control JSON output formatting with indentation, sorting, and separators.

## Pretty Printing with Indentation

Format JSON for readability with indentation.

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding"],
    "address": {"city": "NYC", "zip": "10001"}
}

# Compact (default)
compact = json.dumps(data)
print("Compact:")
print(compact)

# Pretty-printed with indent
pretty = json.dumps(data, indent=2)
print("\nPretty:")
print(pretty)
```

```
Compact:
{"name": "Alice", "age": 30, "hobbies": ["reading", "coding"], "address": {"city": "NYC", "zip": "10001"}}

Pretty:
{
  "name": "Alice",
  "age": 30,
  "hobbies": [
    "reading",
    "coding"
  ],
  "address": {
    "city": "NYC",
    "zip": "10001"
  }
}
```

## Sorting and Separators

Control key order and output formatting.

```python
import json

data = {"zebra": 1, "apple": 2, "monkey": 3}

# Sorted keys
sorted_json = json.dumps(data, sort_keys=True, indent=2)
print("Sorted:")
print(sorted_json)

# Custom separators
compact_sep = json.dumps(data, separators=(',', ':'))
print("\nCompact separators:")
print(compact_sep)
```

```
Sorted:
{
  "apple": 2,
  "monkey": 3,
  "zebra": 1
}

Compact separators:
{"zebra":1,"apple":2,"monkey":3}
```

