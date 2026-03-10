# json Overview


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The `json` module provides tools for encoding and decoding JSON (JavaScript Object Notation) data.

## What is JSON?

JSON is a lightweight data format for exchanging structured data.

```python
import json

# JSON basics
json_str = '{"name": "Alice", "age": 30, "city": "NYC"}'
print(f"JSON string: {json_str}")

# Parse JSON
data = json.loads(json_str)
print(f"Parsed data: {data}")
print(f"Name: {data['name']}
```

```
JSON string: {"name": "Alice", "age": 30, "city": "NYC"}
Parsed data: {'name': 'Alice', 'age': 30, 'city': 'NYC'}
Name: Alice
```

## JSON to Python Type Mapping

Understand how JSON types map to Python.

```python
import json

json_str = '''
{
    "string": "hello",
    "number": 42,
    "float": 3.14,
    "bool": true,
    "null": null,
    "array": [1, 2, 3],
    "object": {"key": "value"}
}
'''

data = json.loads(json_str)
for key, value in data.items():
    print(f"{key}: {value} ({type(value).__name__)}")
```

```
string: hello (str)
number: 42 (int)
float: 3.14 (float)
bool: True (bool)
null: None (NoneType)
array: [1, 2, 3] (list)
object: {'key': 'value'} (dict)
```

