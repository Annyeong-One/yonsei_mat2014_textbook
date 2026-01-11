# Maintainability

## Clear Names

### 1. Descriptive

```python
# Good
user_count = len(users)

# Bad
n = len(users)
```

## Small Functions

### 1. Single Responsibility

```python
def process_user(user):
    validate(user)
    save(user)
    notify(user)
```

## Documentation

### 1. Docstrings

```python
def function(x):
    # Explain purpose
    return x * 2
```

## Summary

- Clear names
- Small functions
- Good documentation
