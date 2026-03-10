# Log Levels


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Understanding log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) and when to use each.

## Log Level Hierarchy

Log levels control which messages are recorded.

```python
import logging

logging.basicConfig(
    level=logging.WARNING,
    format='%(levelname)s: %(message)s'
)

logging.debug("Debug: detailed info")
logging.info("Info: confirmation")
logging.warning("Warning: something unexpected")
logging.error("Error: something failed")
logging.critical("Critical: serious problem")
```

```
WARNING: something unexpected
ERROR: something failed
CRITICAL: serious problem
```

## Level Values

Each level has a numeric value controlling filtering.

```python
import logging

levels = [
    (logging.DEBUG, "DEBUG"),
    (logging.INFO, "INFO"),
    (logging.WARNING, "WARNING"),
    (logging.ERROR, "ERROR"),
    (logging.CRITICAL, "CRITICAL")
]

for value, name in levels:
    print(f"{name}: {value}")
```

```
DEBUG: 10
INFO: 20
WARNING: 30
ERROR: 40
CRITICAL: 50
```

