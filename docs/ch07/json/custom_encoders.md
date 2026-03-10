# Custom Encoders (JSONEncoder)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Extend JSONEncoder to handle custom Python objects that aren't JSON serializable by default.

## Creating Custom Encoders

Subclass JSONEncoder to handle custom types.

```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {
    "event": "Conference",
    "date": datetime(2024, 12, 25, 14, 30)
}

json_str = json.dumps(data, cls=DateTimeEncoder)
print(json_str)
```

```
{"event": "Conference", "date": "2024-12-25T14:30:00"}
```

## Using default Parameter

Use the default parameter for simpler custom encoding.

```python
import json
from datetime import date

def encode_date(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

data = {
    "name": "Alice",
    "birth_date": date(1990, 5, 15)
}

json_str = json.dumps(data, default=encode_date)
print(json_str)
```

```
{"name": "Alice", "birth_date": "1990-05-15"}
```

