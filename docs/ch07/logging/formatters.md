# Formatters


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Formatters control the output format of log messages with customizable fields and styles.

## Common Format Codes

Use format codes to customize log output.

```python
import logging

# Create logger with different formatters
logger = logging.getLogger('format_demo')
logger.setLevel(logging.DEBUG)
logger.handlers.clear()

handler = logging.StreamHandler()

# Format with various codes
formats = [
    '%(message)s',
    '%(levelname)s - %(message)s',
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    '[%(filename)s:%(lineno)d] %(levelname)s: %(message)s'
]

for fmt_str in formats:
    formatter = logging.Formatter(fmt_str)
    handler.setFormatter(formatter)
    logger.handlers = [handler]
    logger.info("Test message")
    print()
```

```
Test message

INFO - Test message

2026-02-12 12:34:56,789 - format_demo - INFO - Test message

[logging_demo.py:15] INFO: Test message
```

## Custom Attributes

Add custom attributes to log records.

```python
import logging

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.user_id = 123
        record.request_id = 'req-456'
        return True

logger = logging.getLogger('context_demo')
logger.setLevel(logging.DEBUG)
logger.handlers.clear()

handler = logging.StreamHandler()
formatter = logging.Formatter(
    '[%(user_id)s:%(request_id)s] %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)
handler.addFilter(ContextFilter())
logger.addHandler(handler)

logger.info("Processing request")
```

```
[123:req-456] INFO - Processing request
```

