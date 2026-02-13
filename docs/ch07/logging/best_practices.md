# Logging Best Practices

Guidelines for effective logging in production applications.

## Use Named Loggers

Create loggers for each module using __name__.

```python
import logging

# In each module, use __name__ for the logger
logger = logging.getLogger(__name__)

def process_data(data):
    logger.debug(f"Processing data: {data}")
    try:
        result = sum(data)
        logger.info(f"Processed successfully: {result}")
        return result
    except Exception as e:
        logger.error(f"Error processing: {e}")
        raise

logging.basicConfig(level=logging.DEBUG)
process_data([1, 2, 3])
```

```
DEBUG:__main__:Processing data: [1, 2, 3]
INFO:__main__:Processed successfully: 6
```

## Structured Logging

Include context in log messages.

```python
import logging
import json

logger = logging.getLogger(__name__)

class StructuredFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage(),
            'logger': record.name
        }
        return json.dumps(log_obj)

handler = logging.StreamHandler()
handler.setFormatter(StructuredFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("User login", extra={'user_id': 123})
```

```
{"timestamp": "2026-02-12 12:34:56,789", "level": "INFO", "message": "User login", "logger": "__main__"}
```

