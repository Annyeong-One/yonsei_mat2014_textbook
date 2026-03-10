# __getattribute__


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Fundamentals

### 1. Definition

The `__getattribute__` method is automatically called by Python **for every attribute access** on an object:

```python
obj.attr  # Triggers obj.__getattribute__('attr')
getattr(obj, 'attr')  # Also triggers obj.__getattribute__('attr')
```

### 2. Method Signature

```python
def __getattribute__(self, name):
    # name is a string
    # Must return a value or raise AttributeError
    pass
```

### 3. Universal Hook

**Key characteristic**: `__getattribute__` is called for **every** attribute access, even:
- Instance attributes
- Class attributes
- Methods
- Properties
- Dunder methods (like `__dict__`)

## Basic Implementation

### 1. Simple Override

```python
class MyClass:
    def __init__(self):
        self.value = 42
    
    def __getattribute__(self, name):
        print(f"Accessing attribute: {name}")
        return super().__getattribute__(name)

obj = MyClass()
x = obj.value
# Output: Accessing attribute: value
# Returns: 42
```

### 2. Without super()

```python
class MyClass:
    def __getattribute__(self, name):
        print(f"Getting: {name}")
        return object.__getattribute__(self, name)
```

### 3. Must Return or Raise

```python
def __getattribute__(self, name):
    if name == 'secret':
        raise AttributeError("Access denied")
    return super().__getattribute__(name)
```

## Avoiding Recursion

### 1. The Problem

```python
class Broken:
    def __getattribute__(self, name):
        # ❌ INFINITE RECURSION!
        return self.name  # Calls __getattribute__ again!
```

### 2. Correct Approaches

**Use `super()`:**
```python
class Correct:
    def __getattribute__(self, name):
        return super().__getattribute__(name)
```

**Use `object.__getattribute__`:**
```python
class Correct:
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
```

**Direct dict access:**
```python
class Correct:
    def __getattribute__(self, name):
        return object.__getattribute__(self, '__dict__')[name]
```

### 3. Why Recursion Happens

```python
def __getattribute__(self, name):
    value = self.something  # Calls __getattribute__('something')
    # Which calls __getattribute__('something')
    # Which calls __getattribute__('something')
    # ... forever!
```

## Practical Examples

### 1. Logging Access

```python
class LoggedAccess:
    def __init__(self):
        self.data = {'x': 1, 'y': 2}
    
    def __getattribute__(self, name):
        print(f"[LOG] Accessing: {name}")
        return super().__getattribute__(name)

obj = LoggedAccess()
print(obj.data)
# [LOG] Accessing: data
# {'x': 1, 'y': 2}
```

### 2. Access Control

```python
class Restricted:
    def __init__(self):
        self._private = "secret"
        self.public = "visible"
    
    def __getattribute__(self, name):
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f"Cannot access private attribute: {name}")
        return super().__getattribute__(name)

obj = Restricted()
print(obj.public)   # ✅ "visible"
# print(obj._private)  # ❌ AttributeError
```

### 3. Lazy Loading

```python
class LazyLoader:
    def __init__(self):
        self._loaded = False
        self._data = None
    
    def __getattribute__(self, name):
        if name == 'data':
            loaded = super().__getattribute__('_loaded')
            if not loaded:
                print("Loading data...")
                object.__setattr__(self, '_data', [1, 2, 3, 4, 5])
                object.__setattr__(self, '_loaded', True)
            return super().__getattribute__('_data')
        return super().__getattribute__(name)

obj = LazyLoader()
print(obj.data)  # Loading data... [1, 2, 3, 4, 5]
print(obj.data)  # [1, 2, 3, 4, 5] (no loading)
```

## Interaction with Properties

### 1. Properties Still Work

```python
class Example:
    def __init__(self):
        self._value = 42
    
    @property
    def value(self):
        return self._value * 2
    
    def __getattribute__(self, name):
        print(f"Intercepting: {name}")
        return super().__getattribute__(name)

obj = Example()
print(obj.value)
# Intercepting: value
# 84 (property getter was called)
```

### 2. Order of Operations

```python
obj.value
    ↓
__getattribute__('value') called
    ↓
super().__getattribute__('value')
    ↓
Finds property descriptor in class
    ↓
Calls property's __get__ method
    ↓
Returns result
```

### 3. Blocking Properties

```python
class BlockProperty:
    @property
    def value(self):
        return 42
    
    def __getattribute__(self, name):
        if name == 'value':
            return 100  # Bypass property!
        return super().__getattribute__(name)

obj = BlockProperty()
print(obj.value)  # 100 (property never called)
```

## Advanced Patterns

### 1. Attribute Proxy

```python
class Proxy:
    def __init__(self, obj):
        object.__setattr__(self, '_obj', obj)
    
    def __getattribute__(self, name):
        if name == '_obj':
            return object.__getattribute__(self, name)
        obj = object.__getattribute__(self, '_obj')
        return getattr(obj, name)

class Target:
    def __init__(self):
        self.value = 42

proxy = Proxy(Target())
print(proxy.value)  # 42
```

### 2. Attribute Mapping

```python
class AttributeMapper:
    def __init__(self):
        self._mapping = {
            'old_name': 'new_name',
            'deprecated': 'current'
        }
        self.new_name = "value"
        self.current = "data"
    
    def __getattribute__(self, name):
        mapping = super().__getattribute__('_mapping')
        if name in mapping:
            name = mapping[name]
        return super().__getattribute__(name)

obj = AttributeMapper()
print(obj.old_name)    # "value"
print(obj.deprecated)  # "data"
```

### 3. Counting Access

```python
class AccessCounter:
    def __init__(self):
        object.__setattr__(self, '_counts', {})
        self.data = [1, 2, 3]
    
    def __getattribute__(self, name):
        if name not in ('_counts', '__dict__', '__class__'):
            counts = object.__getattribute__(self, '_counts')
            counts[name] = counts.get(name, 0) + 1
        return super().__getattribute__(name)
    
    def get_counts(self):
        return self._counts

obj = AccessCounter()
obj.data
obj.data
obj.data
print(obj.get_counts())  # {'data': 3}
```

## When to Use

### 1. Good Use Cases

✅ **Debugging and logging** - Track all attribute access
✅ **Proxies and wrappers** - Delegate to another object
✅ **Access control** - Enforce security policies
✅ **Attribute translation** - Map old names to new names

### 2. Avoid When

❌ **Simple attribute access** - Use normal attributes
❌ **Validation only** - Use `@property` instead
❌ **Missing attributes** - Use `__getattr__` instead
❌ **Performance critical** - Adds overhead

### 3. Comparison

| Scenario | Use |
|----------|-----|
| All attribute access | `__getattribute__` |
| Missing attributes only | `__getattr__` |
| Specific attributes | `@property` |
| Simple storage | Plain attributes |

## Common Mistakes

### 1. Infinite Recursion

```python
# ❌ BAD
def __getattribute__(self, name):
    if self.ready:  # Calls __getattribute__!
        return self.value
```

**Fix:**
```python
# ✅ GOOD
def __getattribute__(self, name):
    ready = super().__getattribute__('ready')
    if ready:
        return super().__getattribute__('value')
```

### 2. Forgetting to Return

```python
# ❌ BAD
def __getattribute__(self, name):
    print(f"Accessing {name}")
    # Forgot to return!

# Returns None for everything!
```

### 3. Breaking Built-ins

```python
# ❌ BAD
def __getattribute__(self, name):
    return "always this"  # Breaks __dict__, __class__, etc.
```
