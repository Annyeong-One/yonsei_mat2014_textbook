# Custom Decoders (object_hook)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Use object_hook to transform JSON objects during deserialization.

## Basic object_hook Usage

Transform JSON objects with a custom function.

```python
import json
from datetime import datetime

def parse_date(obj):
    if 'date' in obj and isinstance(obj['date'], str):
        obj['date'] = datetime.fromisoformat(obj['date'])
    return obj

json_str = '{"event": "Meeting", "date": "2024-12-25T14:30:00"}'
data = json.loads(json_str, object_hook=parse_date)
print(data)
print(f"Date type: {type(data['date'])}")
```

```
{'event': 'Meeting', 'date': datetime.datetime(2024, 12, 25, 14, 30)}
Date type: <class 'datetime.datetime'>
```

## Creating Custom Classes from JSON

Convert JSON objects to custom Python classes.

```python
import json
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

def user_decoder(obj):
    if 'name' in obj and 'age' in obj:
        return User(obj['name'], obj['age'])
    return obj

json_str = '{"name": "Alice", "age": 30}'
user = json.loads(json_str, object_hook=user_decoder)
print(user)
print(f"Type: {type(user)}")
```

```
User(name='Alice', age=30)
Type: <class '__main__.User'>
```

