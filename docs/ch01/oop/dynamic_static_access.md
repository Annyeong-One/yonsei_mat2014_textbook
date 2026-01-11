# Dynamic vs Static

## Definitions

### 1. Static Access

**Static access** means attribute names are **hardcoded** in your source code:

```python
person = Person()
print(person.name)      # Fixed: we write 'name' directly
person.age = 30         # Fixed: we write 'age' directly
del person.email        # Fixed: we write 'email' directly
```

The attribute names are known at **coding time**.

### 2. Dynamic Access

**Dynamic access** means attribute names are determined at **runtime** using variables or strings:

```python
attr_name = 'name'
print(getattr(person, attr_name))    # Dynamic: attr_name is a variable

setattr(person, 'age', 30)           # Dynamic: string determines attribute

delattr(person, 'email')             # Dynamic: string determines deletion
```

The attribute names come from **variables, config files, user input, or databases**.

### 3. Key Difference

| Aspect | Static | Dynamic |
|--------|--------|---------|
| Determined | Compile/write time | Runtime |
| Syntax | `obj.attr` | `getattr(obj, 'attr')` |
| Flexibility | Fixed | Variable |
| Speed | Faster | Slightly slower |

## When to Use Static

### 1. Known Attributes

When you know exactly which attributes you need:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

# Static access - clear and direct
print(person.name)
print(person.age)
```

### 2. Performance Critical

Static access is faster:

```python
# Faster
for i in range(1000000):
    x = obj.value

# Slower
for i in range(1000000):
    x = getattr(obj, 'value')
```

### 3. Code Clarity

Static access is more readable:

```python
# Clear what's happening
user.email = "alice@example.com"
user.save()

# Less clear
setattr(user, 'email', "alice@example.com")
getattr(user, 'save')()
```

## When to Use Dynamic

### 1. Generic Functions

When writing functions that work with any object:

```python
def copy_attributes(source, target, attrs):
    """Copy specified attributes from source to target"""
    for attr in attrs:
        if hasattr(source, attr):
            value = getattr(source, attr)
            setattr(target, attr, value)

# Works with any class
copy_attributes(person1, person2, ['name', 'age', 'email'])
```

### 2. Configuration-Driven

When attributes come from configuration:

```python
def load_config(obj, config_dict):
    """Load configuration into object"""
    for key, value in config_dict.items():
        setattr(obj, key, value)

config = {
    'host': 'localhost',
    'port': 8080,
    'debug': True
}
server = Server()
load_config(server, config)
```

### 3. User Input

When attribute names come from user input:

```python
def get_user_preference(user, preference_name):
    """Get user preference by name"""
    return getattr(user.preferences, preference_name, None)

# User chooses what to view
pref = input("Enter preference name: ")
value = get_user_preference(current_user, pref)
```

## Practical Comparisons

### 1. Object Serialization

**Static approach** (limited):
```python
def person_to_dict(person):
    return {
        'name': person.name,
        'age': person.age,
        'email': person.email
    }
```

**Dynamic approach** (flexible):
```python
def to_dict(obj, fields):
    return {field: getattr(obj, field) for field in fields}

# Works with any object
person_dict = to_dict(person, ['name', 'age', 'email'])
product_dict = to_dict(product, ['name', 'price', 'stock'])
```

### 2. Validation

**Static approach**:
```python
def validate_person(person):
    if not person.name:
        raise ValueError("Name required")
    if person.age < 0:
        raise ValueError("Age must be positive")
    if '@' not in person.email:
        raise ValueError("Invalid email")
```

**Dynamic approach**:
```python
def validate(obj, rules):
    for attr, validator in rules.items():
        value = getattr(obj, attr)
        if not validator(value):
            raise ValueError(f"Invalid {attr}")

rules = {
    'name': lambda x: bool(x),
    'age': lambda x: x >= 0,
    'email': lambda x: '@' in x
}
validate(person, rules)
```

### 3. Attribute Iteration

**Static approach** (tedious):
```python
def print_person(person):
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
    print(f"Email: {person.email}")
```

**Dynamic approach** (scalable):
```python
def print_object(obj, attrs):
    for attr in attrs:
        value = getattr(obj, attr, 'N/A')
        print(f"{attr}: {value}")

print_object(person, ['name', 'age', 'email'])
```

## Framework Examples

### 1. ORM Pattern

```python
class Model:
    def save(self):
        """Save model to database"""
        data = {}
        for field in self._fields:
            # Dynamic access to get all field values
            data[field] = getattr(self, field)
        db.insert(self._table, data)

class User(Model):
    _table = 'users'
    _fields = ['name', 'email', 'age']
    
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
```

### 2. API Response Builder

```python
class APIResponse:
    def to_json(self, fields=None):
        """Convert object to JSON with specified fields"""
        if fields is None:
            fields = [k for k in dir(self) if not k.startswith('_')]
        
        result = {}
        for field in fields:
            if hasattr(self, field):
                value = getattr(self, field)
                if not callable(value):
                    result[field] = value
        return result
```

### 3. Form Handler

```python
class FormHandler:
    def populate_from_request(self, request_data):
        """Populate object from request data"""
        for key, value in request_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    def validate(self):
        """Validate all fields"""
        for field in self._required_fields:
            if not getattr(self, field, None):
                raise ValueError(f"{field} is required")
```

## Performance Considerations

### 1. Speed Comparison

```python
import timeit

class Example:
    def __init__(self):
        self.value = 42

obj = Example()

# Static access
static_time = timeit.timeit(
    'x = obj.value',
    globals={'obj': obj},
    number=1000000
)

# Dynamic access
dynamic_time = timeit.timeit(
    'x = getattr(obj, "value")',
    globals={'obj': obj},
    number=1000000
)

print(f"Static: {static_time:.4f}s")
print(f"Dynamic: {dynamic_time:.4f}s")
# Dynamic is ~2-3x slower
```

### 2. When Performance Matters

**Use static** for:
- Hot paths in performance-critical code
- Inner loops
- Frequently accessed attributes

**Dynamic is fine** for:
- Configuration loading
- Serialization/deserialization
- Generic utilities
- Framework code

## Best Practices

### 1. Principle

> Use **static access** by default. Use **dynamic access** when you need runtime flexibility.

### 2. Hybrid Approach

Combine both for optimal results:

```python
class DataProcessor:
    def __init__(self):
        self.results = []  # Static for known attribute
    
    def process(self, data, field_name):
        # Dynamic for user-specified field
        value = getattr(data, field_name)
        self.results.append(value)  # Static for known attribute
```

### 3. Documentation

When using dynamic access, document which attributes are expected:

```python
def update_object(obj, updates):
    """
    Update object attributes dynamically.
    
    Args:
        obj: Object to update
        updates: Dict of {attr_name: value}
        
    Expected attributes:
        - name (str)
        - age (int)
        - email (str)
    """
    for attr, value in updates.items():
        setattr(obj, attr, value)
```
