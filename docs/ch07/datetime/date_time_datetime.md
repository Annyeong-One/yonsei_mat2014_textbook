# date, time, datetime Objects

These three classes represent dates, times, and the combination of both, forming the foundation of datetime operations.

## date Class

The date class represents a calendar date (year, month, day).

```python
from datetime import date

# Today's date
today = date.today()
print(f"Today: {today}")

# Create specific date
d = date(2024, 12, 25)
print(f"Date: {d}")

# Access components
print(f"Year: {d.year}, Month: {d.month}, Day: {d.day}")

# Day of week (0=Monday)
print(f"Weekday: {d.weekday()}")
print(f"ISO Weekday: {d.isoweekday()}")
```

```
Today: 2026-02-12
Date: 2024-12-25
Year: 2024, Month: 12, Day: 25
Weekday: 2
ISO Weekday: 3
```

## time Class

The time class represents time (hour, minute, second, microsecond).

```python
from datetime import time

# Create time
t = time(14, 30, 45)
print(f"Time: {t}")

# Access components
print(f"Hour: {t.hour}, Minute: {t.minute}, Second: {t.second}")

# Midnight, noon
midnight = time(0, 0, 0)
noon = time(12, 0, 0)
print(f"Midnight: {midnight}, Noon: {noon}")
```

```
Time: 14:30:45
Hour: 14, Minute: 30, Second: 45
Midnight: 00:00:00, Noon: 12:00:00
```

## datetime Class

The datetime class combines date and time.

```python
from datetime import datetime

# Current datetime
now = datetime.now()
print(f"Now: {now}")

# Create specific datetime
dt = datetime(2024, 12, 25, 14, 30, 0)
print(f"DateTime: {dt}")

# Combine date and time
from datetime import date, time
d = date(2024, 12, 25)
t = time(14, 30)
combined = datetime.combine(d, t)
print(f"Combined: {combined}")
```

```
Now: 2026-02-12 14:30:45.123456
DateTime: 2024-12-25 14:30:00
Combined: 2024-12-25 14:30:00
```

