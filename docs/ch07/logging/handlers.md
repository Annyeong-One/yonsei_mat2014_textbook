# Handlers (Stream, File, Rotating)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Handlers determine where log messages go: console, files, or rotating files.

## Stream Handler (Console)

Log to console with StreamHandler.

```python
import logging

logger = logging.getLogger('console_demo')
logger.setLevel(logging.DEBUG)

# StreamHandler outputs to console
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Message to console")
logger.warning("Warning to console")
```

```
INFO - Message to console
WARNING - Warning to console
```

## File Handler

Log to file with FileHandler.

```python
import logging
import tempfile
import os

# Create temporary file
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.log')
log_path = temp_file.name
temp_file.close()

try:
    logger = logging.getLogger('file_demo')
    logger.setLevel(logging.DEBUG)
    
    handler = logging.FileHandler(log_path)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    logger.info("Message to file")
    
    # Read the log file
    with open(log_path) as f:
        print(f.read())
finally:
    os.unlink(log_path)
```

```
2026-02-12 12:34:56,789 - INFO - Message to file
```

## RotatingFileHandler

Automatically rotate log files by size or time.

```python
import logging
from logging.handlers import RotatingFileHandler
import tempfile
import os

temp_dir = tempfile.mkdtemp()
log_path = os.path.join(temp_dir, 'app.log')

try:
    logger = logging.getLogger('rotating_demo')
    logger.setLevel(logging.DEBUG)
    
    # Max 1KB per file, keep 3 backups
    handler = RotatingFileHandler(
        log_path,
        maxBytes=1024,
        backupCount=3
    )
    
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    for i in range(5):
        logger.info(f"Log message {i}")
    
    print("Rotating file handler created successfully")
finally:
    import shutil
    shutil.rmtree(temp_dir, ignore_errors=True)
```

```
Rotating file handler created successfully
```

