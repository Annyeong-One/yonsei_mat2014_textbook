# datetime Overview


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The `datetime` module provides classes for manipulating dates and times, including date, time, datetime, timedelta, and timezone support.

## Core Classes

The datetime module provides several core classes for date and time manipulation.

```python
from datetime import date, time, datetime, timedelta

# Current date
today = date.today()
print(f"Today: {today}")

# Create specific date
birthday = date(1990, 5, 15)
print(f"Birthday: {birthday}")

# Current time
now = datetime.now()
print(f"Now: {now}")
```

```
Today: 2026-02-12
Birthday: 1990-05-15
Now: 2026-02-12 12:34:56.789123
```

## Parsing and Formatting

Convert between datetime objects and strings.

```python
from datetime import datetime

# Parse string to datetime
date_str = "2024-12-25"
parsed = datetime.strptime(date_str, "%Y-%m-%d")
print(f"Parsed: {parsed}")

# Format datetime to string
formatted = parsed.strftime("%A, %B %d, %Y")
print(f"Formatted: {formatted}")
```

```
Parsed: 2024-12-25 00:00:00
Formatted: Wednesday, December 25, 2024
```

