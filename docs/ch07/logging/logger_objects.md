# Logger Objects


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Create and configure logger objects for modular logging throughout your application.

## Creating Loggers

Create named loggers for different modules.

```python
import logging

# Get loggers for different modules
logger_app = logging.getLogger('app')
logger_db = logging.getLogger('app.database')
logger_api = logging.getLogger('app.api')

# Loggers have hierarchical names
print(f"App logger: {logger_app.name}")
print(f"DB logger: {logger_db.name}")
print(f"API logger: {logger_api.name}")
```

```
App logger: app
DB logger: app.database
API logger: app.api
```

## Logger Configuration

Configure individual loggers with handlers and formatters.

```python
import logging

# Create logger
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)

# Remove existing handlers
logger.handlers.clear()

# Create handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# Create formatter
fmt = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(fmt)

# Add handler to logger
logger.addHandler(handler)

# Log messages
logger.info("Starting application")
logger.debug("Debug info")
```

```
myapp - INFO - Starting application
myapp - DEBUG - Debug info
```

