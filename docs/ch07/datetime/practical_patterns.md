# Practical Patterns for datetime

Common patterns and best practices for working with dates and times in real-world applications.

## Human-Readable Relative Times

Display times relative to now (e.g., '2 hours ago').

```python
from datetime import datetime, timedelta

def time_ago(dt):
    now = datetime.now()
    delta = now - dt
    
    if delta.days > 0:
        return f"{delta.days} days ago"
    elif delta.seconds > 3600:
        return f"{delta.seconds // 3600} hours ago"
    elif delta.seconds > 60:
        return f"{delta.seconds // 60} minutes ago"
    else:
        return "just now"

past = datetime.now() - timedelta(hours=2)
print(time_ago(past))
```

```
2 hours ago
```

## Date Range Iteration

Iterate through a range of dates.

```python
from datetime import date, timedelta

def date_range(start: date, end: date):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)

start = date(2024, 12, 23)
end = date(2024, 12, 26)

for d in date_range(start, end):
    print(d)
```

```
2024-12-23
2024-12-24
2024-12-25
2024-12-26
```

## Scheduling and Cron-like Logic

Check if a task should run based on schedule.

```python
from datetime import datetime, timedelta

class Task:
    def __init__(self, name, interval_hours):
        self.name = name
        self.interval = timedelta(hours=interval_hours)
        self.last_run = None
    
    def should_run(self):
        if self.last_run is None:
            return True
        return datetime.now() >= self.last_run + self.interval
    
    def run(self):
        print(f"Running {self.name}")
        self.last_run = datetime.now()

task = Task("cleanup", 24)
print(f"Should run: {task.should_run()}")
task.run()
print(f"Should run again: {task.should_run()}")
```

```
Should run: True
Running cleanup
Should run again: False
```

