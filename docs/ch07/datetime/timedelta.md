# timedelta Arithmetic


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

`timedelta` represents a duration and enables arithmetic operations on dates and times.

## Creating and Using timedelta

Create timedelta objects to represent durations.

```python
from datetime import datetime, timedelta

# Create timedelta
delta = timedelta(days=5, hours=2, minutes=30)
print(f"Delta: {delta}")

# Access components
print(f"Days: {delta.days}, Seconds: {delta.seconds}")

# Arithmetic with dates
today = datetime.now()
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)

print(f"Today: {today.date()}")
print(f"Tomorrow: {tomorrow.date()}")
print(f"Next week: {next_week.date()}")
```

```
Delta: 5 days, 2:30:00
Days: 5, Seconds: 9000
Today: 2026-02-12
Tomorrow: 2026-02-13
Next week: 2026-02-19
```

## Date Differences

Calculate the duration between two dates.

```python
from datetime import date

start = date(2024, 1, 1)
end = date(2024, 12, 31)

difference = end - start
print(f"Days between: {difference.days}")

# Calculate age
from datetime import date
birth_date = date(1990, 5, 15)
today = date.today()
age_delta = today - birth_date
age_years = age_delta.days // 365
print(f"Age (approximate): {age_years} years")
```

```
Days between: 364
Age (approximate): 35 years
```

