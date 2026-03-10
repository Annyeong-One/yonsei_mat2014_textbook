# Configuration (dictConfig, fileConfig)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Configure logging using dictConfig for Python dicts or fileConfig for configuration files.

## dictConfig - Dictionary Configuration

Configure logging with a dictionary.

```python
import logging.config

config = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'INFO'
        }
    },
    'loggers': {
        'myapp': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}

logging.config.dictConfig(config)
logger = logging.getLogger('myapp')
logger.info("Application started")
```

```
2026-02-12 12:34:56,789 - myapp - INFO - Application started
```

## fileConfig - Configuration File

Configure logging from an INI file.

```python
import logging.config
import tempfile
import os

# Create temporary config file
config_content = '''[loggers]
keys=root,myapp

[handlers]
keys=console

[formatters]
keys=standard

[logger_root]
level=WARNING
handlers=console

[logger_myapp]
level=DEBUG
handlers=console
qualname=myapp

[handler_console]
class=StreamHandler
level=DEBUG
formatter=standard
args=(sys.stdout,)

[formatter_standard]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
'''

# Write config to temp file
with tempfile.NamedTemporaryFile(mode='w', suffix='.conf', delete=False) as f:
    f.write(config_content)
    config_path = f.name

try:
    logging.config.fileConfig(config_path)
    logger = logging.getLogger('myapp')
    logger.info("Configured from file")
finally:
    os.unlink(config_path)
```

```
2026-02-12 12:34:56,789 - myapp - INFO - Configured from file
```

