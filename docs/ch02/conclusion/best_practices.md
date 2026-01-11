# Best Practices

## Variable Naming

### 1. Descriptive Names

```python
# Good
user_count = len(users)
total_price = sum(prices)

# Bad
n = len(users)
x = sum(prices)
```

### 2. Follow PEP 8

```python
# Functions and variables
def my_function():
    local_var = 10

# Classes
class MyClass:
    pass

# Constants
MAX_SIZE = 100
```

## Function Design

### 1. Small and Focused

```python
def process_user(user):
    validate(user)
    save(user)
    notify(user)
```

### 2. Clear Returns

```python
def calculate(x, y):
    return x + y  # Clear what's returned
```

## Memory Management

### 1. Let Python Handle

```python
# Normal code
def function():
    data = load_data()
    result = process(data)
    return result
```

### 2. Break Cycles

```python
# Clear references when done
obj.parent = None
```

## Closures

### 1. Capture Value

```python
# Use defaults
for i in range(3):
    funcs.append(lambda x=i: x)
```

### 2. Minimize Capture

```python
# Only capture what's needed
def outer():
    config = load_config()
    key = config['key']
    
    def inner():
        return key  # Not entire config
    
    return inner
```

## Testing

### 1. Write Tests

```python
def test_counter():
    inc, get = make_counter()
    inc()
    assert get() == 1
```

## Summary

- Descriptive names
- Small functions
- Trust auto memory management
- Capture values in closures
- Write tests
