# Descriptor Use Cases


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Validation

### 1. Type Checking

```python
class TypedAttribute:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} must be {self.expected_type.__name__}"
            )
        instance.__dict__[self.name] = value

class Person:
    name = TypedAttribute('name', str)
    age = TypedAttribute('age', int)
    height = TypedAttribute('height', (int, float))

p = Person()
p.name = "Alice"  # ✅ OK
p.age = 30        # ✅ OK
# p.age = "30"    # ❌ TypeError
```

### 2. Range Validation

```python
class BoundedNumber:
    def __init__(self, name, min_value=None, max_value=None):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be <= {self.max_value}")
        instance.__dict__[self.name] = value

class Temperature:
    celsius = BoundedNumber('celsius', min_value=-273.15)
    fahrenheit = BoundedNumber('fahrenheit', min_value=-459.67)

t = Temperature()
t.celsius = 25    # ✅ OK
# t.celsius = -300  # ❌ ValueError
```

### 3. Pattern Validation

```python
import re

class RegexValidated:
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = re.compile(pattern)
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not self.pattern.match(value):
            raise ValueError(
                f"{self.name} must match pattern: {self.pattern.pattern}"
            )
        instance.__dict__[self.name] = value

class User:
    email = RegexValidated('email', r'^[\w\.-]+@[\w\.-]+\.\w+$')
    phone = RegexValidated('phone', r'^\d{3}-\d{3}-\d{4}$')

user = User()
user.email = "alice@example.com"  # ✅ OK
# user.email = "invalid"          # ❌ ValueError
```

## ORM Patterns

### 1. Database Field

```python
class Field:
    def __init__(self, field_type, required=False, default=None):
        self.field_type = field_type
        self.required = required
        self.default = default
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, self.default)
    
    def __set__(self, instance, value):
        if value is None and self.required:
            raise ValueError(f"{self.name} is required")
        if value is not None and not isinstance(value, self.field_type):
            raise TypeError(f"{self.name} must be {self.field_type.__name__}")
        instance.__dict__[self.name] = value

class Model:
    def save(self):
        data = {}
        for name, field in type(self).__dict__.items():
            if isinstance(field, Field):
                value = getattr(self, name)
                if value is not None:
                    data[name] = value
        print(f"Saving to database: {data}")
        return data

class User(Model):
    username = Field(str, required=True)
    email = Field(str, required=True)
    age = Field(int, default=0)

user = User()
user.username = "alice"
user.email = "alice@example.com"
user.age = 30
user.save()  # Saving to database: {'username': 'alice', 'email': 'alice@example.com', 'age': 30}
```

### 2. Foreign Key

```python
class ForeignKey:
    def __init__(self, model_class):
        self.model_class = model_class
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        fk_id = instance.__dict__.get(f"{self.name}_id")
        if fk_id is not None:
            # Simulate database lookup
            return self.model_class.get(fk_id)
        return None
    
    def __set__(self, instance, value):
        if not isinstance(value, self.model_class):
            raise TypeError(f"Must be instance of {self.model_class.__name__}")
        instance.__dict__[f"{self.name}_id"] = value.id

class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    @staticmethod
    def get(id):
        # Simulate database lookup
        return Department(id, f"Department {id}")

class Employee:
    department = ForeignKey(Department)

dept = Department(1, "Engineering")
emp = Employee()
emp.department = dept
```

### 3. Lazy Relationship

```python
class LazyRelationship:
    def __init__(self, model_class, foreign_key):
        self.model_class = model_class
        self.foreign_key = foreign_key
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # Check cache
        cache_key = f"_{self.name}_cache"
        if cache_key not in instance.__dict__:
            # Load from database
            fk_value = getattr(instance, self.foreign_key)
            instance.__dict__[cache_key] = self.model_class.query(fk_value)
        
        return instance.__dict__[cache_key]
```

## Performance Optimization

### 1. Lazy Loading

```python
class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # Load once and cache
        value = self.func(instance)
        instance.__dict__[self.name] = value
        return value

class DataProcessor:
    def __init__(self, filename):
        self.filename = filename
    
    @LazyProperty
    def data(self):
        print(f"Loading {self.filename}...")
        # Expensive I/O operation
        with open(self.filename) as f:
            return f.read()

processor = DataProcessor('data.txt')
# Not loaded yet
print(processor.data)  # Loading data.txt...
print(processor.data)  # No loading (cached)
```

### 2. Memoization

```python
class Memoized:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        def memoized_func(*args):
            if args not in self.cache:
                self.cache[args] = self.func(instance, *args)
            return self.cache[args]
        
        return memoized_func

class Calculator:
    @Memoized
    def fibonacci(self, n):
        print(f"Computing fib({n})")
        if n <= 1:
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)

calc = Calculator()
print(calc.fibonacci(5))  # Computes each value once
print(calc.fibonacci(5))  # All from cache
```

### 3. Weak References

```python
import weakref

class WeakAttribute:
    def __init__(self):
        self.data = weakref.WeakValueDictionary()
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(id(instance))
    
    def __set__(self, instance, value):
        self.data[id(instance)] = value

class Node:
    parent = WeakAttribute()
```

## Access Control

### 1. Read-Only After Init

```python
class ReadOnlyAfterInit:
    def __init__(self, name):
        self.name = name
        self.initialized = weakref.WeakSet()
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if instance in self.initialized:
            raise AttributeError(f"{self.name} is read-only after initialization")
        instance.__dict__[self.name] = value
        self.initialized.add(instance)

class Config:
    api_key = ReadOnlyAfterInit('api_key')

config = Config()
config.api_key = "secret123"  # ✅ OK (first time)
# config.api_key = "new"      # ❌ AttributeError (read-only)
```

### 2. Permission-Based Access

```python
class PermissionRequired:
    def __init__(self, name, read_perm=None, write_perm=None):
        self.name = name
        self.read_perm = read_perm
        self.write_perm = write_perm
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.read_perm and not instance.has_permission(self.read_perm):
            raise PermissionError(f"No read access to {self.name}")
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if self.write_perm and not instance.has_permission(self.write_perm):
            raise PermissionError(f"No write access to {self.name}")
        instance.__dict__[self.name] = value
```

### 3. Audit Trail

```python
from datetime import datetime

class AuditedAttribute:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        # Log change
        if not hasattr(instance, '_audit_log'):
            instance._audit_log = []
        
        old_value = instance.__dict__.get(self.name)
        instance._audit_log.append({
            'field': self.name,
            'old': old_value,
            'new': value,
            'timestamp': datetime.now()
        })
        
        instance.__dict__[self.name] = value

class AuditedModel:
    name = AuditedAttribute('name')
    value = AuditedAttribute('value')

model = AuditedModel()
model.name = "Alice"
model.value = 100
model.value = 200
print(model._audit_log)
```

## Type Conversion

### 1. Auto-Converting

```python
class AutoConvert:
    def __init__(self, name, converter):
        self.name = name
        self.converter = converter
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.converter(value)

class DataRecord:
    count = AutoConvert('count', int)
    price = AutoConvert('price', float)
    active = AutoConvert('active', bool)

record = DataRecord()
record.count = "42"      # Stored as int(42)
record.price = "19.99"   # Stored as float(19.99)
record.active = "yes"    # Stored as bool("yes") = True
```

### 2. JSON Serialization

```python
import json

class JSONField:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        json_str = instance.__dict__.get(self.name)
        return json.loads(json_str) if json_str else None
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = json.dumps(value)

class Config:
    settings = JSONField('settings')

config = Config()
config.settings = {'debug': True, 'port': 8080}
print(config.settings)  # {'debug': True, 'port': 8080}
```

### 3. Unit Conversion

```python
class Temperature:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        # Stored in Celsius
        return instance.__dict__.get(self.name, 0)
    
    def __set__(self, instance, value):
        # Value can be dict with unit
        if isinstance(value, dict):
            if value.get('unit') == 'F':
                # Convert F to C
                celsius = (value['value'] - 32) * 5/9
                instance.__dict__[self.name] = celsius
            else:
                instance.__dict__[self.name] = value['value']
        else:
            instance.__dict__[self.name] = value

class Weather:
    temp = Temperature('temp')

weather = Weather()
weather.temp = {'value': 77, 'unit': 'F'}
print(weather.temp)  # 25.0 (Celsius)
```
