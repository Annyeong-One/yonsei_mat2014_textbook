# Common Patterns

## Factory Functions

### 1. Object Creation

```python
def create_user(name, email):
    return {
        'name': name,
        'email': email
    }
```

## Builder Pattern

### 1. Fluent Interface

```python
class QueryBuilder:
    def __init__(self):
        self._table = None
    
    def table(self, name):
        self._table = name
        return self
    
    def build(self):
        return f"SELECT * FROM {self._table}"
```

## Registry Pattern

### 1. Plugin System

```python
_handlers = {}

def register(name):
    def decorator(func):
        _handlers[name] = func
        return func
    return decorator

@register('csv')
def process_csv(data):
    pass
```

## Summary

- Factory functions for creation
- Builder for complex objects
- Registry for plugins
