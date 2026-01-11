# Attribute Access

Attribute access dunder methods control how object attributes are retrieved, set, and deleted.

---

## Attribute Lookup Methods

### 1. `__getattr__`

```python
class DynamicObject:
    def __getattr__(self, name):
        return f"No attribute '{name}'"

obj = DynamicObject()
print(obj.anything)  # "No attribute 'anything'"
print(obj.foo)       # "No attribute 'foo'"
```

Called when attribute not found normally.

### 2. `__getattribute__`

```python
class LoggedObject:
    def __getattribute__(self, name):
        print(f"Accessing: {name}")
        return super().__getattribute__(name)

obj = LoggedObject()
obj.value  # Prints: Accessing: value
```

Called for **every** attribute access.

### 3. Key Difference

```python
# __getattr__: fallback only
# __getattribute__: always called
```

---

## `__getattr__` Details

### 1. Fallback Mechanism

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def __getattr__(self, attr):
        return f"{attr} not found"

p = Person("Alice")
print(p.name)    # "Alice" - normal lookup
print(p.age)     # "age not found" - fallback
```

### 2. Dynamic Attributes

```python
class LazyLoader:
    def __getattr__(self, name):
        print(f"Loading {name}...")
        value = load_expensive_data(name)
        setattr(self, name, value)  # Cache it
        return value

obj = LazyLoader()
obj.data  # Loaded once, cached
obj.data  # Direct access (cached)
```

### 3. Proxy Pattern

```python
class Proxy:
    def __init__(self, obj):
        self._obj = obj
    
    def __getattr__(self, name):
        return getattr(self._obj, name)

p = Proxy([1, 2, 3])
print(p.append)  # Delegates to list
```

---

## `__getattribute__` Details

### 1. Universal Hook

```python
class Monitored:
    def __init__(self):
        self.x = 10
    
    def __getattribute__(self, name):
        print(f"Get: {name}")
        return super().__getattribute__(name)

m = Monitored()
m.x  # Prints: Get: x
```

### 2. Infinite Recursion Risk

```python
# WRONG - infinite recursion
class Bad:
    def __getattribute__(self, name):
        return self.value  # Calls __getattribute__ again!

# CORRECT - use super()
class Good:
    def __getattribute__(self, name):
        return super().__getattribute__(name)
```

### 3. Access `__dict__` Safely

```python
def __getattribute__(self, name):
    # Safe way to access instance dict
    d = super().__getattribute__('__dict__')
    if name in d:
        return d[name]
    return super().__getattribute__(name)
```

---

## `__setattr__` Method

### 1. Attribute Assignment

```python
class ValidatedObject:
    def __setattr__(self, name, value):
        if name == "age" and value < 0:
            raise ValueError("Age must be positive")
        super().__setattr__(name, value)

obj = ValidatedObject()
obj.age = 25   # OK
obj.age = -5   # ValueError
```

### 2. Called on Assignment

```python
obj.x = 10  # Calls obj.__setattr__('x', 10)
```

### 3. Initialization Gotcha

```python
class Person:
    def __init__(self, name):
        self.name = name  # Calls __setattr__
    
    def __setattr__(self, name, value):
        print(f"Setting {name} = {value}")
        super().__setattr__(name, value)
```

---

## `__delattr__` Method

### 1. Attribute Deletion

```python
class ProtectedObject:
    def __init__(self):
        self.x = 10
        self.id = "important"
    
    def __delattr__(self, name):
        if name == "id":
            raise AttributeError("Cannot delete ID")
        super().__delattr__(name)

obj = ProtectedObject()
del obj.x   # OK
del obj.id  # AttributeError
```

### 2. Called on `del`

```python
del obj.attr  # Calls obj.__delattr__('attr')
```

### 3. Logging Deletions

```python
def __delattr__(self, name):
    print(f"Deleting {name}")
    super().__delattr__(name)
```

---

## Comparison Table

### 1. Method Purposes

| Method | When Called | Purpose |
|--------|-------------|---------|
| `__getattr__` | Attribute not found | Fallback |
| `__getattribute__` | Every access | Universal hook |
| `__setattr__` | Assignment | Control setting |
| `__delattr__` | Deletion | Control deletion |

### 2. Call Order

```python
# Access: obj.x
# 1. __getattribute__('x')
# 2. If AttributeError → __getattr__('x')

# Set: obj.x = 10
# → __setattr__('x', 10)

# Delete: del obj.x
# → __delattr__('x')
```

### 3. Super() Required

```python
# Always use super() to avoid recursion
def __getattribute__(self, name):
    return super().__getattribute__(name)
```

---

## Lazy Attributes

### 1. Compute on Demand

```python
class LazyProperty:
    def __init__(self):
        pass
    
    def __getattr__(self, name):
        if name == "expensive":
            print("Computing expensive...")
            value = compute_expensive()
            self.expensive = value  # Cache
            return value
        raise AttributeError(f"No attribute {name}")

obj = LazyProperty()
obj.expensive  # Computed once
obj.expensive  # Cached
```

### 2. Database Lazy Loading

```python
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def __getattr__(self, name):
        if name == "profile":
            self.profile = fetch_profile(self.user_id)
            return self.profile
        raise AttributeError(name)
```

### 3. Avoid Repeated Computation

Cache expensive attributes on first access.

---

## Read-Only Attributes

### 1. Block Assignment

```python
class ReadOnly:
    def __init__(self):
        super().__setattr__('_value', 42)
    
    def __setattr__(self, name, value):
        raise AttributeError("Read-only object")
    
    def __getattr__(self, name):
        if name == 'value':
            return super().__getattribute__('_value')
        raise AttributeError(name)

obj = ReadOnly()
print(obj.value)  # 42
obj.value = 10    # AttributeError
```

### 2. Selective Protection

```python
class PartialReadOnly:
    PROTECTED = {'id', 'created_at'}
    
    def __setattr__(self, name, value):
        if name in self.PROTECTED:
            raise AttributeError(f"{name} is read-only")
        super().__setattr__(name, value)
```

### 3. Property Alternative

```python
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    # No setter - read-only
```

---

## Attribute Validation

### 1. Type Checking

```python
class TypedObject:
    def __setattr__(self, name, value):
        if name == "count" and not isinstance(value, int):
            raise TypeError("count must be int")
        super().__setattr__(name, value)

obj = TypedObject()
obj.count = 5    # OK
obj.count = "5"  # TypeError
```

### 2. Range Validation

```python
class Bounded:
    def __setattr__(self, name, value):
        if name == "percentage":
            if not 0 <= value <= 100:
                raise ValueError("Must be 0-100")
        super().__setattr__(name, value)
```

### 3. Complex Validation

```python
class Validated:
    VALIDATORS = {
        'email': lambda x: '@' in x,
        'age': lambda x: 0 < x < 120,
    }
    
    def __setattr__(self, name, value):
        if name in self.VALIDATORS:
            if not self.VALIDATORS[name](value):
                raise ValueError(f"Invalid {name}")
        super().__setattr__(name, value)
```

---

## Proxy Objects

### 1. Transparent Proxy

```python
class Proxy:
    def __init__(self, obj):
        # Use super() to avoid __setattr__
        super().__setattr__('_obj', obj)
    
    def __getattr__(self, name):
        return getattr(self._obj, name)
    
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)

p = Proxy([1, 2, 3])
p.append(4)  # Delegates to list
```

### 2. Logging Proxy

```python
class LoggingProxy:
    def __init__(self, obj):
        super().__setattr__('_obj', obj)
    
    def __getattribute__(self, name):
        obj = super().__getattribute__('_obj')
        attr = getattr(obj, name)
        print(f"Accessed: {name}")
        return attr
```

### 3. Remote Proxy

```python
class RemoteProxy:
    def __getattr__(self, name):
        return self._call_remote('get', name)
    
    def __setattr__(self, name, value):
        self._call_remote('set', name, value)
```

---

## Descriptor Protocol

### 1. `__get__` Method

```python
class Descriptor:
    def __get__(self, obj, objtype=None):
        print("Getting attribute")
        return 42

class MyClass:
    attr = Descriptor()

obj = MyClass()
print(obj.attr)  # Getting attribute\n42
```

### 2. `__set__` Method

```python
class Descriptor:
    def __set__(self, obj, value):
        print(f"Setting to {value}")
        obj._value = value

class MyClass:
    attr = Descriptor()

obj = MyClass()
obj.attr = 10  # Setting to 10
```

### 3. Data Descriptors

Descriptors with `__set__` take priority over instance `__dict__`.

---

## Best Practices

### 1. Use `super()`

```python
def __getattribute__(self, name):
    return super().__getattribute__(name)
```

### 2. Avoid in `__init__`

```python
# Careful - __setattr__ called here
def __init__(self):
    self.x = 10  # May need super().__setattr__
```

### 3. Performance Impact

```python
# __getattribute__ called on EVERY access
# Use sparingly for performance-critical code
```

---

## Key Takeaways

- `__getattr__`: fallback for missing attributes.
- `__getattribute__`: called for every access.
- `__setattr__`: controls assignment.
- `__delattr__`: controls deletion.
- Always use `super()` to avoid recursion.
- Useful for proxies, validation, lazy loading.
