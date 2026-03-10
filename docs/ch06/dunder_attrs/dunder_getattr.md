# __getattr__


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Fundamentals

### 1. Definition

The `__getattr__` method is called **only when regular attribute lookup fails**:

```python
obj.missing_attr  # Triggers __getattr__ if 'missing_attr' not found
```

### 2. Method Signature

```python
def __getattr__(self, name):
    # Called only for missing attributes
    # Can return a value or raise AttributeError
    pass
```

### 3. Fallback Mechanism

```python
obj.attr
    ↓
__getattribute__('attr') called
    ↓
Attribute found? → Return it
    ↓
Not found? → AttributeError
    ↓
__getattr__('attr') called (if defined)
    ↓
Return value or raise AttributeError
```

## Basic Implementation

### 1. Simple Example

```python
class MyClass:
    def __init__(self):
        self.existing = "I exist"
    
    def __getattr__(self, name):
        return f"Default value for {name}"

obj = MyClass()
print(obj.existing)     # "I exist" (normal lookup)
print(obj.missing)      # "Default value for missing" (__getattr__)
print(obj.anything)     # "Default value for anything" (__getattr__)
```

### 2. Providing Defaults

```python
class Config:
    def __init__(self):
        self.host = "localhost"
    
    def __getattr__(self, name):
        defaults = {
            'port': 8080,
            'debug': False,
            'timeout': 30
        }
        if name in defaults:
            return defaults[name]
        raise AttributeError(f"No attribute: {name}")

config = Config()
print(config.host)    # "localhost" (exists)
print(config.port)    # 8080 (from __getattr__)
print(config.debug)   # False (from __getattr__)
```

### 3. Raising Errors

```python
def __getattr__(self, name):
    raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")
```

## Only for Missing Attributes

### 1. Comparison

```python
class Example:
    def __init__(self):
        self.exists = "value"
    
    def __getattr__(self, name):
        print(f"__getattr__ called for: {name}")
        return "default"

obj = Example()
print(obj.exists)   # "value" (__getattr__ NOT called)
print(obj.missing)  # "default" (__getattr__ IS called)
```

### 2. Not Called For

`__getattr__` is **not** called when:
- Attribute exists in `__dict__`
- Attribute is a descriptor in the class
- Attribute exists in parent classes
- Attribute is found through normal lookup

### 3. Only Called When

`__getattr__` **is** called when:
- Attribute doesn't exist anywhere
- `__getattribute__` raises `AttributeError`
- No other lookup mechanism found the attribute

## Practical Examples

### 1. Dynamic Attributes

```python
class DynamicObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __getattr__(self, name):
        return f"No attribute '{name}' - returning None"

obj = DynamicObject(name="Alice", age=30)
print(obj.name)     # "Alice"
print(obj.age)      # 30
print(obj.email)    # "No attribute 'email' - returning None"
```

### 2. Lazy Loading

```python
class LazyLoader:
    def __init__(self):
        self._cache = {}
    
    def __getattr__(self, name):
        if name.startswith('data_'):
            print(f"Loading {name}...")
            # Simulate expensive operation
            data = f"Loaded data for {name}"
            # Cache it
            self._cache[name] = data
            setattr(self, name, data)  # Store in __dict__
            return data
        raise AttributeError(f"No attribute: {name}")

loader = LazyLoader()
print(loader.data_users)      # Loading data_users... Loaded data for data_users
print(loader.data_users)      # Loaded data for data_users (from __dict__, __getattr__ not called)
```

### 3. Attribute Delegation

```python
class Wrapper:
    def __init__(self, wrapped_object):
        self._wrapped = wrapped_object
    
    def __getattr__(self, name):
        # Delegate to wrapped object
        return getattr(self._wrapped, name)

class Target:
    def __init__(self):
        self.value = 42
    
    def method(self):
        return "method called"

wrapper = Wrapper(Target())
print(wrapper.value)     # 42 (delegated)
print(wrapper.method())  # "method called" (delegated)
```

## vs __getattribute__

### 1. Key Differences

| Aspect | `__getattribute__` | `__getattr__` |
|--------|-------------------|---------------|
| When called | **Every** attribute access | **Only** missing attributes |
| Frequency | Always | Rarely (only on failure) |
| Use case | Universal interception | Graceful fallback |
| Complexity | High (easy to break) | Low (safer) |
| Performance | Slower (always runs) | Faster (rarely runs) |

### 2. Example

```python
class Comparison:
    def __init__(self):
        self.exists = "value"
    
    def __getattribute__(self, name):
        print(f"__getattribute__: {name}")
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        print(f"__getattr__: {name}")
        return "default"

obj = Comparison()
print("=" * 40)
print(obj.exists)
# __getattribute__: exists
# value

print("=" * 40)
print(obj.missing)
# __getattribute__: missing
# __getattr__: missing
# default
```

### 3. When to Choose

**Use `__getattr__`:**
- Providing default values
- Delegating to another object
- Lazy loading attributes
- Backward compatibility (old attribute names)

**Use `__getattribute__`:**
- Logging all access
- Proxying everything
- Universal access control
- Complete attribute control

## Advanced Patterns

### 1. Database-Backed Attributes

```python
class DatabaseModel:
    def __init__(self, record_id):
        self.id = record_id
        self._cache = {}
    
    def __getattr__(self, name):
        # Check cache first
        if name in self._cache:
            return self._cache[name]
        
        # Query database
        print(f"Querying database for {name}...")
        value = f"DB value for {name}"
        
        # Cache result
        self._cache[name] = value
        return value

model = DatabaseModel(123)
print(model.name)      # Querying database for name... DB value for name
print(model.name)      # DB value for name (from cache)
print(model.email)     # Querying database for email... DB value for email
```

### 2. Method Generation

```python
class DynamicMethods:
    def __getattr__(self, name):
        if name.startswith('get_'):
            field = name[4:]  # Remove 'get_' prefix
            return lambda: f"Getting {field}"
        elif name.startswith('set_'):
            field = name[4:]  # Remove 'set_' prefix
            return lambda value: f"Setting {field} to {value}"
        raise AttributeError(f"No attribute: {name}")

obj = DynamicMethods()
print(obj.get_name())         # "Getting name"
print(obj.set_age(30))        # "Setting age to 30"
```

### 3. Nested Attribute Access

```python
class NestedAccess:
    def __init__(self, data):
        self._data = data
    
    def __getattr__(self, name):
        if '.' in name:
            # Handle nested access like 'user.profile.email'
            parts = name.split('.')
            value = self._data
            for part in parts:
                value = value.get(part)
                if value is None:
                    raise AttributeError(f"No nested attribute: {name}")
            return value
        
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"No attribute: {name}")

data = {
    'user': {
        'profile': {
            'email': 'alice@example.com'
        }
    }
}
obj = NestedAccess(data)
print(obj.user)  # {'profile': {'email': 'alice@example.com'}}
```

## Common Pitfalls

### 1. Forgetting to Raise

```python
# ❌ BAD - returns None for everything missing
def __getattr__(self, name):
    if name in self.valid_attrs:
        return self.valid_attrs[name]
    # Forgot to raise AttributeError!

# ✅ GOOD
def __getattr__(self, name):
    if name in self.valid_attrs:
        return self.valid_attrs[name]
    raise AttributeError(f"No attribute: {name}")
```

### 2. Infinite Recursion

```python
# ❌ BAD
def __getattr__(self, name):
    return self.default_value  # If 'default_value' missing, infinite loop!

# ✅ GOOD
def __getattr__(self, name):
    return object.__getattribute__(self, 'default_value')
```

### 3. Not Storing Loaded Values

```python
# ❌ BAD - reloads every time
def __getattr__(self, name):
    return self._load_from_db(name)  # Always hits database!

# ✅ GOOD - cache after loading
def __getattr__(self, name):
    value = self._load_from_db(name)
    setattr(self, name, value)  # Store in __dict__
    return value
```

## Best Practices

### 1. Clear Error Messages

```python
def __getattr__(self, name):
    valid = ', '.join(self._valid_attributes)
    raise AttributeError(
        f"'{type(self).__name__}' has no attribute '{name}'. "
        f"Valid attributes: {valid}"
    )
```

### 2. Document Behavior

```python
class DynamicAPI:
    """
    Provides dynamic attribute access.
    
    Any attribute access will query the API endpoint
    with the same name. Results are cached.
    
    Example:
        api.users  # Calls /api/users
        api.posts  # Calls /api/posts
    """
    def __getattr__(self, name):
        return self._fetch_endpoint(name)
```

### 3. Limit Scope

```python
def __getattr__(self, name):
    # Only handle specific pattern
    if not name.startswith('dynamic_'):
        raise AttributeError(f"No attribute: {name}")
    
    # Handle dynamic attributes
    return self._handle_dynamic(name)
```
