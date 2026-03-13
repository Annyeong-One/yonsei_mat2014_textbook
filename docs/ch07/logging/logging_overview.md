# logging Overview

The `logging` module provides a flexible framework for emitting log messages from Python programs.

## Basic Logging

Start logging with minimal configuration.

```python
import logging

# Basic configuration
logging.basicConfig(level=logging.DEBUG)

# Log messages at different levels
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
```

```
DEBUG:root:Debug message
INFO:root:Info message
WARNING:root:Warning message
ERROR:root:Error message
CRITICAL:root:Critical message
```

## Logger Objects

Use named loggers for better organization.

```python
import logging

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handler
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Log messages
logger.info("Application started")
logger.warning("Low memory")
```

```
2026-02-12 12:34:56,789 - __main__ - INFO - Application started
2026-02-12 12:34:56,789 - __main__ - WARNING - Low memory
```

