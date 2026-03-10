# json.dumps and json.loads


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

`dumps()` converts Python objects to JSON strings, while `loads()` parses JSON strings into Python objects.

## dumps - Python to JSON String

Convert Python objects to JSON strings.

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding"]
}

# Convert to JSON string
json_str = json.dumps(data)
print(json_str)
print(type(json_str))
```

```
{"name": "Alice", "age": 30, "hobbies": ["reading", "coding"]}
<class 'str'>
```

## loads - JSON String to Python

Parse JSON strings into Python objects.

```python
import json

json_str = '{"name": "Bob", "age": 25, "active": true}'

# Parse JSON string
data = json.loads(json_str)
print(data)
print(type(data))
print(f"Name: {data['name']}")
print(f"Active: {data['active']}")
```

```
{'name': 'Bob', 'age': 25, 'active': True}
<class 'dict'>
Name: Bob
Active: True
```

