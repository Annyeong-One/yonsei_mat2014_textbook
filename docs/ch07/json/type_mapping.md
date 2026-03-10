# JSON and Python Type Mapping


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Understanding the mapping between JSON data types and Python data types.

## JSON to Python Mapping

How JSON types convert to Python types.

```python
import json

mapping = {
    '"string"': str,
    '42': int,
    '3.14': float,
    'true': bool,
    'false': bool,
    'null': type(None),
    '[]': list,
    '{}': dict
}

for json_val, py_type in mapping.items():
    obj = json.loads(json_val)
    print(f"{json_val:15} -> {type(obj).__name__:10} (expected: {py_type.__name__})")
```

```
"string"         -> str        (expected: str)
42              -> int        (expected: int)
3.14            -> float      (expected: float)
true            -> bool       (expected: bool)
false           -> bool       (expected: bool)
null            -> NoneType   (expected: NoneType)
[]              -> list       (expected: list)
{}              -> dict       (expected: dict)
```

## Python to JSON Mapping

How Python types convert to JSON.

```python
import json

data = {
    "string": "hello",
    "int": 42,
    "float": 3.14,
    "bool": True,
    "none": None,
    "list": [1, 2, 3],
    "dict": {"nested": "value"}
}

json_str = json.dumps(data)
print(json_str)

# Parse back to see types
parsed = json.loads(json_str)
for key, val in parsed.items():
    print(f"{key}: {type(val).__name__}")
```

```
{"string": "hello", "int": 42, "float": 3.14, "bool": true, "none": null, "list": [1, 2, 3], "dict": {"nested": "value"}}
string: str
int: int
float: float
bool: bool
none: NoneType
list: list
dict: dict
```

