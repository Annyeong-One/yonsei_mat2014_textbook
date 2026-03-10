# Python Decorators - Quick Reference Cheat Sheet


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Basic Syntax

### Simple Decorator
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper

@my_decorator
def my_function():
    pass
```

### With functools.wraps (ALWAYS USE THIS!)
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Decorator Patterns

### 1. Basic Decorator Template
```python
from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before function execution
        result = func(*args, **kwargs)
        # After function execution
        return result
    return wrapper
```

### 2. Decorator with Parameters
```python
def decorator_with_params(param1, param2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use param1, param2
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_params("value1", "value2")
def my_function():
    pass
```

### 3. Class-Based Decorator
```python
from functools import update_wrapper

class MyDecorator:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
    
    def __call__(self, *args, **kwargs):
        # Your logic here
        return self.func(*args, **kwargs)

@MyDecorator
def my_function():
    pass
```

## Common Use Cases

### Timing
```python
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper
```

### Logging
```python
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
```

### Debug
```python
def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper
```

### Caching/Memoization
```python
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

# Or use built-in:
from functools import lru_cache

@lru_cache(maxsize=128)
def my_function(n):
    pass
```

### Exception Handling
```python
def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return None
    return wrapper
```

### Retry Logic
```python
def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Retry {attempt + 1}/{max_attempts}")
        return wrapper
    return decorator
```

### Validation
```python
def validate_positive(func):
    @wraps(func)
    def wrapper(n):
        if n < 0:
            raise ValueError("Must be positive")
        return func(n)
    return wrapper

def validate_type(expected_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not isinstance(args[0], expected_type):
                raise TypeError(f"Expected {expected_type}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Rate Limiting
```python
import time

def rate_limit(max_calls, time_period):
    def decorator(func):
        calls = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            calls[:] = [t for t in calls if now - t < time_period]
            if len(calls) >= max_calls:
                return None
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Authentication
```python
def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_authenticated():
            raise PermissionError("Not authenticated")
        return func(*args, **kwargs)
    return wrapper

def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if user_role != role:
                raise PermissionError(f"Requires {role}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

## Stacking Decorators

```python
@decorator1
@decorator2
@decorator3
def my_function():
    pass

# Equivalent to:
# my_function = decorator1(decorator2(decorator3(my_function)))
```

**Important**: Decorators are applied bottom-to-top!

### Example
```python
def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def exclaim(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"
    return wrapper

@uppercase  # Applied SECOND
@exclaim    # Applied FIRST
def greet():
    return "hello"

greet()  # Returns "HELLO!"
```

## Built-in Decorators

### @property
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Negative radius")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.radius)  # Access like attribute
c.radius = 10    # Use setter
print(c.area)    # Computed property
```

### @staticmethod
```python
class MyClass:
    @staticmethod
    def static_method():
        # No access to self or cls
        return "Static!"

MyClass.static_method()  # Can call without instance
```

### @classmethod
```python
class MyClass:
    count = 0
    
    @classmethod
    def increment(cls):
        cls.count += 1

MyClass.increment()  # Access class variables
```

### @functools.lru_cache
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## Best Practices

### ✅ DO:
- Use `@wraps` to preserve function metadata
- Use `*args, **kwargs` for flexibility
- Keep decorators simple and focused
- Document what decorators do
- Consider using built-in decorators when available

### ❌ DON'T:
- Forget to return the wrapper function
- Modify the original function
- Make decorators too complex
- Use decorators for core business logic
- Stack too many decorators (hard to debug)

## Common Patterns Summary

| Pattern | Use Case | Complexity |
|---------|----------|------------|
| Simple wrapper | Add behavior before/after | Easy |
| With parameters | Configurable behavior | Medium |
| Class-based | Need state/attributes | Medium |
| Stacked | Multiple behaviors | Easy |
| Memoization | Cache expensive calls | Easy |
| Timing | Performance monitoring | Easy |
| Validation | Input checking | Easy |
| Retry | Handle transient failures | Medium |
| Rate limiting | Control call frequency | Hard |

## Quick Tips

1. **Debugging**: Decorated functions can be hard to debug - use simple decorators
2. **Performance**: Each decorator adds overhead - use sparingly
3. **Order matters**: When stacking, decorators apply bottom-to-top
4. **Testing**: Test both the decorator and decorated function
5. **Documentation**: Always document what your decorator does

## Common Mistakes

```python
# ❌ Forgetting to return wrapper
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    # Missing: return wrapper

# ❌ Not using *args, **kwargs
def bad_decorator(func):
    def wrapper():  # Won't work with arguments!
        return func()
    return wrapper

# ❌ Not using @wraps
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper  # Loses func.__name__, __doc__, etc.

# ✅ Correct pattern
from functools import wraps

def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Real-World Examples

```python
# Flask route decorator
@app.route('/users/<id>')
def get_user(id):
    pass

# Django login required
@login_required
def profile(request):
    pass

# pytest fixture
@pytest.fixture
def database():
    pass

# Click CLI command
@click.command()
def hello():
    pass
```

---

**Remember**: Decorators are syntactic sugar for function wrapping. Master the basics before creating complex decorators!
