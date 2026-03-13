# calendar Module

The `calendar` module provides functions for calendar-related operations and generating formatted calendars.

## Basic Calendar Operations

Get calendar information for dates.

```python
import calendar
from datetime import date

# Day of week for a specific date
d = date(2024, 12, 25)
day_name = calendar.day_name[d.weekday()]
print(f"2024-12-25 is a {day_name}")

# Check if leap year
print(f"2024 is leap year: {calendar.isleap(2024)}")
print(f"2025 is leap year: {calendar.isleap(2025)}")

# Days in month
days = calendar.monthrange(2024, 2)
print(f"Feb 2024 has {days[1]} days")
```

```
2024-12-25 is a Wednesday
2024 is leap year: True
2025 is leap year: False
Feb 2024 has 29 days
```

## Print Calendars

Generate and display formatted calendars.

```python
import calendar

# Print a month
print("December 2024:")
print(calendar.month(2024, 12))

# Print a year (just first 3 months for brevity)
cal = calendar.TextCalendar()
for month in range(1, 4):
    print(calendar.month(2024, month))
```

```
December 2024:
   December 2024
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
```

