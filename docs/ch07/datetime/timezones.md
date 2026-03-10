# Timezone Handling (timezone, zoneinfo)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Handle timezones with `timezone` for fixed offsets and `zoneinfo` for named timezones.

## Fixed Timezones with timezone

Create fixed timezone offsets.

```python
from datetime import datetime, timezone, timedelta

# UTC timezone
utc = timezone.utc
now_utc = datetime.now(utc)
print(f"UTC: {now_utc}")

# Custom offset (EST is UTC-5)
est = timezone(timedelta(hours=-5))
now_est = datetime.now(est)
print(f"EST: {now_est}")

# Convert between timezones
print(f"UTC: {now_utc}")
print(f"EST: {now_utc.astimezone(est)}")
```

```
UTC: 2026-02-12 20:00:00+00:00
EST: 2026-02-12 15:00:00-05:00
UTC: 2026-02-12 20:00:00+00:00
EST: 2026-02-12 15:00:00-05:00
```

## Named Timezones with zoneinfo

Use named timezone identifiers from the IANA database.

```python
from datetime import datetime
from zoneinfo import ZoneInfo

# Get current time in different timezones
timezones = ["UTC", "America/New_York", "Europe/London", "Asia/Tokyo"]

now = datetime.now()
for tz_name in timezones:
    tz = ZoneInfo(tz_name)
    local_time = now.astimezone(tz)
    print(f"{tz_name}: {local_time.strftime('%Y-%m-%d %H:%M:%S %Z')}
```

```
UTC: 2026-02-12 20:00:00 UTC
America/New_York: 2026-02-12 15:00:00 EST
Europe/London: 2026-02-12 20:00:00 GMT
Asia/Tokyo: 2026-02-13 05:00:00 JST
```

