# getattr setattr delattr

## Built-In Functions

### 1. Overview

Python provides three powerful built-in functions to dynamically interact with object attributes:

- `getattr(obj, name[, default])` - retrieve attribute value
- `setattr(obj, name, value)` - set attribute value  
- `delattr(obj, name)` - delete attribute

### 2. Why Dynamic Access?

**Dynamic** means determined at **runtime**, not hardcoded:

```python
# Static (fixed) access
person.name = "Alice"

# Dynamic access
attr = "name"
setattr(person, attr, "Alice")
```

### 3. Key Use Cases

- Generic code that works with any attribute
- Frameworks that don't know class structure ahead of time
- Serialization/deserialization systems
- Configuration-driven applications
- Reflection and metaprogramming

## getattr Function

### 1. Basic Syntax

```python
value = getattr(obj, 'attr_name')
value = getattr(obj, 'attr_name', default_value)
```

### 2. Simple Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)

# Static access
print(p.name)  # "Alice"

# Dynamic access
print(getattr(p, 'name'))  # "Alice"
print(getattr(p, 'age'))   # 30
```

### 3. With Default Value

```python
# Attribute exists
print(getattr(p, 'name', 'Unknown'))  # "Alice"

# Attribute missing - returns default
print(getattr(p, 'email', 'no-email'))  # "no-email"

# Without default - raises AttributeError
# print(getattr(p, 'email'))  # ❌ AttributeError
```

## setattr Function

### 1. Basic Syntax

```python
setattr(obj, 'attr_name', value)
```

Equivalent to:
```python
obj.attr_name = value
```

### 2. Simple Example

```python
class Person:
    pass

p = Person()

# Static assignment
p.name = "Alice"

# Dynamic assignment
setattr(p, 'age', 30)
setattr(p, 'city', 'New York')

print(p.name)  # "Alice"
print(p.age)   # 30
print(p.city)  # "New York"
```

### 3. Dynamic Attribute Names

```python
person = Person()

# Set multiple attributes from dictionary
data = {'name': 'Bob', 'age': 25, 'city': 'Boston'}
for key, value in data.items():
    setattr(person, key, value)

print(person.name)  # "Bob"
print(person.age)   # 25
```

## delattr Function

### 1. Basic Syntax

```python
delattr(obj, 'attr_name')
```

Equivalent to:
```python
del obj.attr_name
```

### 2. Simple Example

```python
class Person:
    def __init__(self):
        self.name = "Alice"
        self.age = 30

p = Person()
print(p.name)  # "Alice"

# Delete attribute
delattr(p, 'name')

# Now accessing raises error
# print(p.name)  # ❌ AttributeError
```

### 3. Conditional Deletion

```python
def remove_attribute(obj, attr):
    if hasattr(obj, attr):
        delattr(obj, attr)
        print(f"Deleted {attr}")
    else:
        print(f"{attr} doesn't exist")

remove_attribute(p, 'age')    # Deleted age
remove_attribute(p, 'email')  # email doesn't exist
```

## Practical Examples

### 1. Configuration Loading

```python
class Config:
    pass

def load_config(filename):
    config = Config()
    with open(filename) as f:
        for line in f:
            key, value = line.strip().split('=')
            setattr(config, key, value)
    return config

# config.txt:
# host=localhost
# port=8080
# debug=true

config = load_config('config.txt')
print(config.host)   # "localhost"
print(config.port)   # "8080"
```

### 2. Dynamic Method Calls

```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b

calc = Calculator()
operation = 'add'  # from user input

# Get method dynamically
method = getattr(calc, operation)
result = method(5, 3)  # 8
```

### 3. Object Serialization

```python
def to_dict(obj):
    """Convert object attributes to dictionary"""
    result = {}
    for attr in dir(obj):
        if not attr.startswith('_'):
            value = getattr(obj, attr)
            if not callable(value):
                result[attr] = value
    return result

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(to_dict(p))  # {'age': 30, 'name': 'Alice'}
```

## hasattr Helper

### 1. Check Existence

`hasattr(obj, name)` checks if attribute exists:

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")

print(hasattr(p, 'name'))   # True
print(hasattr(p, 'age'))    # False
```

### 2. Safe Access Pattern

```python
# Instead of try/except
value = getattr(obj, 'attr', None)

# Or check first
if hasattr(obj, 'attr'):
    value = getattr(obj, 'attr')
```

### 3. Combined Example

```python
def safe_get(obj, attr, default=None):
    """Safely get attribute with default"""
    if hasattr(obj, attr):
        return getattr(obj, attr)
    return default

age = safe_get(person, 'age', 0)
```

## Comparison

### 1. Static vs Dynamic

| Aspect | Static Access | Dynamic Access |
|--------|---------------|----------------|
| Syntax | `obj.attr` | `getattr(obj, 'attr')` |
| Speed | Faster | Slightly slower |
| Flexibility | Fixed at write time | Determined at runtime |
| Use case | Known attributes | Generic/framework code |

### 2. When to Use Each

**Use static access (`obj.attr`) when:**
- You know the attribute name at coding time
- Performance is critical
- Code clarity is priority

**Use dynamic access (`getattr/setattr`) when:**
- Attribute name comes from user input, config, or database
- Writing generic utilities or frameworks
- Need to iterate over arbitrary attributes
- Implementing serialization/deserialization
