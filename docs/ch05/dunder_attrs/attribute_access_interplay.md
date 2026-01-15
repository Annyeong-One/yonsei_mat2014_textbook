# Access Interplay

## The Complete Picture

### 1. All Four Methods

Python provides four attribute access hooks that work together:

- `__getattribute__` - **Every** attribute read
- `__getattr__` - **Missing** attribute fallback
- `__setattr__` - **Every** attribute write
- `__delattr__` - **Every** attribute deletion

### 2. Relationship Diagram

```
Attribute Access:
    obj.x
        ↓
    __getattribute__('x')
        ↓
    Found? → Return value
        ↓
    Not found? → AttributeError
        ↓
    __getattr__('x') if defined
        ↓
    Return value or raise AttributeError

Attribute Assignment:
    obj.x = value
        ↓
    __setattr__('x', value)
        ↓
    Store in __dict__ or descriptor

Attribute Deletion:
    del obj.x
        ↓
    __delattr__('x')
        ↓
    Remove from __dict__ or descriptor
```

### 3. Priority Order

| Operation | Primary Hook | Fallback | Descriptor Interaction |
|-----------|--------------|----------|----------------------|
| Read | `__getattribute__` | `__getattr__` | Yes (via `__get__`) |
| Write | `__setattr__` | None | Yes (via `__set__`) |
| Delete | `__delattr__` | None | Yes (via `__delete__`) |

## Combined Implementation

### 1. All Methods Together

```python
class FullControl:
    def __init__(self, value):
        # Careful: __setattr__ is active here!
        super().__setattr__('_data', {})
        self.value = value  # Uses __setattr__
    
    def __getattribute__(self, name):
        print(f"[GET] {name}")
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        print(f"[MISSING] {name}")
        return f"Default for {name}"
    
    def __setattr__(self, name, value):
        print(f"[SET] {name} = {value}")
        super().__setattr__(name, value)
    
    def __delattr__(self, name):
        print(f"[DEL] {name}")
        super().__delattr__(name)

obj = FullControl(42)
# [SET] value = 42

print(obj.value)
# [GET] value
# 42

print(obj.missing)
# [GET] missing
# [MISSING] missing
# Default for missing

obj.new_attr = 100
# [SET] new_attr = 100

del obj.new_attr
# [DEL] new_attr
```

### 2. Execution Flow

```python
# Reading existing attribute
obj.value
    ↓
__getattribute__('value')  # Always runs first
    ↓
super().__getattribute__('value')
    ↓
Found in __dict__
    ↓
Return value

# Reading missing attribute
obj.missing
    ↓
__getattribute__('missing')  # Always runs first
    ↓
super().__getattribute__('missing')
    ↓
Not found → AttributeError
    ↓
__getattr__('missing')  # Fallback runs
    ↓
Return default value
```

### 3. With Properties

```python
class WithProperties:
    def __init__(self):
        self._value = 0
    
    @property
    def value(self):
        print("[PROPERTY GET]")
        return self._value
    
    @value.setter
    def value(self, val):
        print("[PROPERTY SET]")
        self._value = val
    
    @value.deleter
    def value(self):
        print("[PROPERTY DEL]")
        del self._value
    
    def __getattribute__(self, name):
        print(f"[__getattribute__] {name}")
        return super().__getattribute__(name)
    
    def __setattr__(self, name, value):
        print(f"[__setattr__] {name}")
        super().__setattr__(name, value)
    
    def __delattr__(self, name):
        print(f"[__delattr__] {name}")
        super().__delattr__(name)

obj = WithProperties()
# [__setattr__] _value

obj.value = 42
# [__setattr__] value
# [PROPERTY SET]
# [__setattr__] _value

print(obj.value)
# [__getattribute__] value
# [PROPERTY GET]
# [__getattribute__] _value
# 42

del obj.value
# [__delattr__] value
# [PROPERTY DEL]
# [__delattr__] _value
```

## Practical Patterns

### 1. Complete Validation System

```python
class ValidatedObject:
    def __init__(self):
        super().__setattr__('_validators', {})
        super().__setattr__('_values', {})
    
    def add_validator(self, attr, validator):
        self._validators[attr] = validator
    
    def __setattr__(self, name, value):
        if name not in ('_validators', '_values'):
            validators = super().__getattribute__('_validators')
            if name in validators:
                if not validators[name](value):
                    raise ValueError(f"Validation failed for {name}")
            values = super().__getattribute__('_values')
            values[name] = value
        else:
            super().__setattr__(name, value)
    
    def __getattribute__(self, name):
        if name not in ('_validators', '_values', 'add_validator'):
            try:
                values = super().__getattribute__('_values')
                return values[name]
            except KeyError:
                raise AttributeError(f"No attribute: {name}")
        return super().__getattribute__(name)
    
    def __delattr__(self, name):
        values = super().__getattribute__('_values')
        if name in values:
            del values[name]
        else:
            raise AttributeError(f"No attribute: {name}")

obj = ValidatedObject()
obj.add_validator('age', lambda x: 0 <= x <= 150)
obj.age = 30   # ✅ OK
# obj.age = 200  # ❌ ValidationError
```

### 2. Lazy Loading with Caching

```python
class LazyCache:
    def __init__(self):
        super().__setattr__('_cache', {})
        super().__setattr__('_loaders', {})
    
    def register_loader(self, attr, loader_func):
        self._loaders[attr] = loader_func
    
    def __getattribute__(self, name):
        if name in ('_cache', '_loaders', 'register_loader'):
            return super().__getattribute__(name)
        
        cache = super().__getattribute__('_cache')
        loaders = super().__getattribute__('_loaders')
        
        # Check cache first
        if name in cache:
            print(f"[CACHE HIT] {name}")
            return cache[name]
        
        # Check if loader exists
        if name in loaders:
            print(f"[LOADING] {name}")
            value = loaders[name]()
            cache[name] = value
            return value
        
        # Normal attribute access
        return super().__getattribute__(name)
    
    def __setattr__(self, name, value):
        if name not in ('_cache', '_loaders'):
            cache = super().__getattribute__('_cache')
            cache[name] = value
        else:
            super().__setattr__(name, value)
    
    def __delattr__(self, name):
        cache = super().__getattribute__('_cache')
        if name in cache:
            del cache[name]

obj = LazyCache()
obj.register_loader('data', lambda: [1, 2, 3, 4, 5])

print(obj.data)  # [LOADING] data → [1, 2, 3, 4, 5]
print(obj.data)  # [CACHE HIT] data → [1, 2, 3, 4, 5]
```

### 3. Access Control System

```python
class AccessControlled:
    def __init__(self):
        super().__setattr__('_permissions', {})
        super().__setattr__('_data', {})
    
    def set_permission(self, attr, read=True, write=True, delete=True):
        self._permissions[attr] = {
            'read': read,
            'write': write,
            'delete': delete
        }
    
    def _check_permission(self, attr, operation):
        perms = super().__getattribute__('_permissions')
        if attr in perms and not perms[attr].get(operation, True):
            raise PermissionError(
                f"No {operation} permission for '{attr}'"
            )
    
    def __getattribute__(self, name):
        if name in ('_permissions', '_data', 'set_permission', '_check_permission'):
            return super().__getattribute__(name)
        
        self._check_permission(name, 'read')
        data = super().__getattribute__('_data')
        if name in data:
            return data[name]
        return super().__getattribute__(name)
    
    def __setattr__(self, name, value):
        if name not in ('_permissions', '_data'):
            self._check_permission(name, 'write')
            data = super().__getattribute__('_data')
            data[name] = value
        else:
            super().__setattr__(name, value)
    
    def __delattr__(self, name):
        self._check_permission(name, 'delete')
        data = super().__getattribute__('_data')
        if name in data:
            del data[name]

obj = AccessControlled()
obj.set_permission('secret', read=False, write=True, delete=False)
obj.secret = "password"  # ✅ OK (write allowed)
# print(obj.secret)      # ❌ PermissionError (read denied)
# del obj.secret         # ❌ PermissionError (delete denied)
```

## Design Patterns

### 1. When to Use Each

| Method | Use When |
|--------|----------|
| `__getattribute__` | Need to intercept **all** reads |
| `__getattr__` | Need **default values** for missing attributes |
| `__setattr__` | Need to **validate** or **transform** all writes |
| `__delattr__` | Need to **protect** or **cleanup** on deletion |

### 2. Combination Strategies

**Read-only after init:**
```python
class ReadOnlyAfterInit:
    def __init__(self):
        super().__setattr__('_locked', False)
        self.value = 42
        super().__setattr__('_locked', True)
    
    def __setattr__(self, name, value):
        if super().__getattribute__('_locked'):
            raise AttributeError("Read-only")
        super().__setattr__(name, value)
    
    def __delattr__(self, name):
        if super().__getattribute__('_locked'):
            raise AttributeError("Read-only")
        super().__delattr__(name)
```

**Computed with caching:**
```python
class ComputedCached:
    def __getattr__(self, name):
        if name.startswith('computed_'):
            value = self._compute(name)
            setattr(self, name, value)  # Cache it
            return value
        raise AttributeError(f"No attribute: {name}")
    
    def __delattr__(self, name):
        # Clear cache when dependency changes
        for attr in list(self.__dict__.keys()):
            if attr.startswith('computed_'):
                super().__delattr__(attr)
        super().__delattr__(name)
```

### 3. Best Practices

✅ **Use the minimum necessary** - Don't override all four if you don't need to

✅ **Call super()** - Always delegate to parent implementation

✅ **Avoid recursion** - Never access `self.x` inside `__getattribute__`

✅ **Document behavior** - Make it clear which attributes are special

✅ **Consider properties first** - They're simpler for specific attributes

## Common Pitfalls

### 1. Forgetting super()

```python
# ❌ BAD - doesn't actually store/retrieve/delete
def __setattr__(self, name, value):
    print(f"Setting {name}")
    # Forgot super().__setattr__!

# ✅ GOOD
def __setattr__(self, name, value):
    print(f"Setting {name}")
    super().__setattr__(name, value)
```

### 2. Infinite Recursion

```python
# ❌ BAD
def __getattribute__(self, name):
    if self.ready:  # Calls __getattribute__ again!
        return self.value  # And again!

# ✅ GOOD
def __getattribute__(self, name):
    if name == 'ready':
        return super().__getattribute__(name)
    ready = super().__getattribute__('ready')
    if ready:
        return super().__getattribute__('value')
```

### 3. Inconsistent Behavior

```python
# ❌ BAD - set but can't read
def __setattr__(self, name, value):
    self.__dict__[name] = value

def __getattribute__(self, name):
    return "always this"  # Ignores __dict__!

# ✅ GOOD - consistent get/set
def __setattr__(self, name, value):
    super().__setattr__(name, value)

def __getattribute__(self, name):
    return super().__getattribute__(name)
```

## Performance Considerations

### 1. Overhead

Each method adds overhead:

```python
# Fastest - direct access
obj.x

# Slower - goes through __getattribute__
class Logged:
    def __getattribute__(self, name):
        log(name)
        return super().__getattribute__(name)
```

### 2. Optimization Tips

- Use properties for specific attributes instead of `__getattribute__` for all
- Cache results in `__getattr__` by storing in `__dict__`
- Minimize logic in hot paths
- Consider `__slots__` for better performance

### 3. When Performance Matters

**Use normal attributes** for:
- Frequently accessed data
- Performance-critical code paths

**Use dunder methods** for:
- Framework/library code
- Debugging and development
- Special behaviors needed
