# Practical Patterns

클로저의 실용적인 활용 패턴과 디버깅 방법입니다.

## Factory Functions

### Basic Factory

```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

### Configuration Factory

```python
def make_formatter(prefix, suffix=""):
    def format(value):
        return f"{prefix}{value}{suffix}"
    return format

currency = make_formatter("$", " USD")
percent = make_formatter("", "%")

print(currency(100))  # \$100 USD
print(percent(75))    # 75%
```

### Validator Factory

```python
def make_validator(min_val, max_val):
    def validate(value):
        if min_val <= value <= max_val:
            return True
        raise ValueError(f"Value must be between {min_val} and {max_val}")
    return validate

validate_age = make_validator(0, 150)
validate_percent = make_validator(0, 100)
```

---

## Decorators with State

### Call Counter

```python
def count_calls(func):
    count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Call #{count}")
        return func(*args, **kwargs)
    
    wrapper.get_count = lambda: count
    return wrapper

@count_calls
def greet(name):
    return f"Hello, {name}!"

greet("Alice")  # Call #1
greet("Bob")    # Call #2
print(greet.get_count())  # 2
```

### Memoization

```python
def memoize(func):
    cache = {}
    
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    wrapper.cache = cache
    wrapper.clear = lambda: cache.clear()
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # Fast!
```

### Rate Limiter

```python
import time

def rate_limit(max_calls, period):
    calls = []
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove old calls
            while calls and calls[0] < now - period:
                calls.pop(0)
            
            if len(calls) >= max_calls:
                raise Exception("Rate limit exceeded")
            
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3, period=60)
def api_call():
    return "Response"
```

---

## functools.partial

기존 함수의 인자를 고정합니다:

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))    # 125
```

### partial vs Closure

```python
# Using closure
def make_power(exp):
    return lambda x: x ** exp

# Using partial
from functools import partial
def power(x, exp):
    return x ** exp

square_closure = make_power(2)
square_partial = partial(power, exp=2)

# Both work the same
print(square_closure(5))  # 25
print(square_partial(5))  # 25
```

| Approach | Pros | Cons |
|----------|------|------|
| Closure | Full control, custom logic | More verbose |
| `partial` | Concise, preserves metadata | Only fixes arguments |

---

## Callback Patterns

### Event Handler Factory

```python
def make_handler(event_name, callback):
    def handler(data):
        print(f"[{event_name}] Processing...")
        return callback(data)
    return handler

def process_click(data):
    return f"Clicked at {data['x']}, {data['y']}"

click_handler = make_handler("CLICK", process_click)
print(click_handler({'x': 100, 'y': 200}))
```

### Retry Logic

```python
import time

def with_retry(max_attempts, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@with_retry(max_attempts=3, delay=1)
def unstable_api_call():
    # Might fail
    pass
```

---

## Debugging Tools

### Inspect Closure Contents

```python
def outer():
    x = 10
    y = "hello"
    return lambda: (x, y)

f = outer()

# View closure
print(f.__closure__)  # (<cell ...>, <cell ...>)

# View free variable names
print(f.__code__.co_freevars)  # ('x', 'y')

# View cell contents
for var, cell in zip(f.__code__.co_freevars, f.__closure__):
    print(f"{var} = {cell.cell_contents}")
# x = 10
# y = hello
```

### Debug Helper Function

```python
def inspect_closure(func):
    """Print closure details for debugging."""
    print(f"Function: {func.__name__}")
    
    if func.__closure__ is None:
        print("  No closure")
        return
    
    freevars = func.__code__.co_freevars
    for var, cell in zip(freevars, func.__closure__):
        print(f"  {var} = {cell.cell_contents!r}")

# Usage
def make_adder(n):
    return lambda x: x + n

add5 = make_adder(5)
inspect_closure(add5)
# Function: <lambda>
#   n = 5
```

---

## Memory Considerations

### Problem: Large Captures

```python
# Bad: captures entire large_data
def make_handler():
    large_data = [0] * 1_000_000
    
    def handler():
        return len(large_data)  # Only needs length
    
    return handler  # Keeps 1M integers alive!
```

### Solution: Capture Only What's Needed

```python
# Good: captures only the length
def make_handler():
    large_data = [0] * 1_000_000
    data_len = len(large_data)
    
    def handler():
        return data_len
    
    return handler  # large_data can be garbage collected
```

### Avoid Circular References

```python
# Potential issue
def outer():
    x = []
    def inner():
        return x
    x.append(inner)  # Cycle: inner → x → inner
    return inner

# Better: use weakref if needed
import weakref

def outer():
    x = []
    def inner():
        return x
    # Don't create cycles, or use weak references
    return inner
```

---

## Summary

| Pattern | Use Case | Key Technique |
|---------|----------|---------------|
| Factory | Create configured functions | Return inner function |
| Decorator | Add behavior to functions | `nonlocal` for state |
| `partial` | Fix function arguments | `functools.partial` |
| Callback | Event handling | Capture context |
| Memoization | Cache results | Dict in closure |

**Debugging Checklist:**
1. `func.__closure__` — Cell objects
2. `func.__code__.co_freevars` — Variable names
3. `cell.cell_contents` — Actual values
