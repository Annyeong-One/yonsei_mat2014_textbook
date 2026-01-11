# Practical Examples

## Counter

### 1. Simple Counter

```python
def make_counter(start=0):
    count = start
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

### 2. Full Counter

```python
def make_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def reset():
        nonlocal count
        count = 0
    
    def get():
        return count
    
    return increment, decrement, reset, get

inc, dec, reset, get = make_counter()
```

## Caching

### 1. Memoization

```python
def memoize(f):
    cache = {}
    
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### 2. LRU Cache

```python
def lru_cache(maxsize):
    def decorator(f):
        cache = {}
        order = []
        
        def wrapper(*args):
            if args in cache:
                order.remove(args)
                order.append(args)
                return cache[args]
            
            result = f(*args)
            cache[args] = result
            order.append(args)
            
            if len(cache) > maxsize:
                oldest = order.pop(0)
                del cache[oldest]
            
            return result
        
        return wrapper
    return decorator
```

## Event Handlers

### 1. Button Callbacks

```python
def make_button_handler(button_id):
    def handler(event):
        print(f"Button {button_id} clicked")
    
    return handler

buttons = {}
for i in range(5):
    buttons[i] = make_button_handler(i)
```

### 2. Validators

```python
def make_validator(min_val, max_val):
    def validate(value):
        if not isinstance(value, (int, float)):
            return False, "Must be number"
        if value < min_val:
            return False, f"Must be >= {min_val}"
        if value > max_val:
            return False, f"Must be <= {max_val}"
        return True, "Valid"
    
    return validate

age_validator = make_validator(0, 120)
percent_validator = make_validator(0, 100)
```

## State Machines

### 1. Toggle

```python
def make_toggle(initial=False):
    state = initial
    
    def toggle():
        nonlocal state
        state = not state
        return state
    
    def get():
        return state
    
    def set(value):
        nonlocal state
        state = bool(value)
    
    return toggle, get, set
```

### 2. Accumulator

```python
def make_accumulator(initial=0):
    total = initial
    
    def add(value):
        nonlocal total
        total += value
        return total
    
    def subtract(value):
        nonlocal total
        total -= value
        return total
    
    def reset():
        nonlocal total
        total = initial
    
    return add, subtract, reset
```

## Configuration

### 1. Settings

```python
def create_formatter(prefix="", suffix=""):
    def format(text):
        return f"{prefix}{text}{suffix}"
    
    return format

bold = create_formatter("<b>", "</b>")
italic = create_formatter("<i>", "</i>")
```

### 2. API Client

```python
def make_api_client(base_url, api_key):
    def get(endpoint):
        url = f"{base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {api_key}"}
        # Make request
        return response
    
    def post(endpoint, data):
        url = f"{base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {api_key}"}
        # Make request
        return response
    
    return get, post

get, post = make_api_client("https://api.example.com", "key123")
```

## Summary

Closures useful for:
- State preservation
- Configuration
- Event handlers
- Caching
- Factories
