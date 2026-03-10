# Formatting (strftime) and Parsing (strptime)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

`strftime()` formats datetime objects as strings, while `strptime()` parses strings into datetime objects.

## strftime - Format Datetime to String

Use format codes to create human-readable date strings.

```python
from datetime import datetime

now = datetime(2024, 12, 25, 14, 30, 45)

# Common format codes
formats = {
    "%Y-%m-%d": now.strftime("%Y-%m-%d"),
    "%d/%m/%Y": now.strftime("%d/%m/%Y"),
    "%A, %B %d, %Y": now.strftime("%A, %B %d, %Y"),
    "%I:%M %p": now.strftime("%I:%M %p"),
    "%H:%M:%S": now.strftime("%H:%M:%S"),
}

for pattern, result in formats.items():
    print(f"{pattern}: {result}")
```

```
%Y-%m-%d: 2024-12-25
%d/%m/%Y: 25/12/2024
%A, %B %d, %Y: Wednesday, December 25, 2024
%I:%M %p: 02:30 PM
%H:%M:%S: 14:30:45
```

## strptime - Parse String to Datetime

Parse date strings using format codes.

```python
from datetime import datetime

# Parse various date formats
dates = [
    ("2024-12-25", "%Y-%m-%d"),
    ("25/12/2024", "%d/%m/%Y"),
    ("December 25, 2024", "%B %d, %Y"),
    ("02:30 PM", "%I:%M %p"),
]

for date_str, fmt in dates:
    parsed = datetime.strptime(date_str, fmt)
    print(f"'{date_str}' -> {parsed}")
```

```
'2024-12-25' -> 2024-12-25 00:00:00
'25/12/2024' -> 2024-12-25 00:00:00
'December 25, 2024' -> 2024-12-25 00:00:00
'02:30 PM' -> 1900-01-01 14:30:00
```

