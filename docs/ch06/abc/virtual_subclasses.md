# Virtual Subclasses (register)

The `register()` method allows classes to be registered as virtual subclasses of an ABC without inheriting from it. This enables duck typing with formal guarantees.

---

## Basic Register Usage

```python
from abc import ABC, abstractmethod

class DataStore(ABC):
    @abstractmethod
    def save(self, key, value):
        pass
    
    @abstractmethod
    def load(self, key):
        pass

# Register an existing class as virtual subclass
class FileStore:
    def save(self, key, value):
        # Implementation
        pass
    
    def load(self, key):
        # Implementation
        pass

DataStore.register(FileStore)

# Now FileStore is considered a subclass
print(isinstance(FileStore(), DataStore))           # True
print(issubclass(FileStore, DataStore))             # True
```

## Practical Example: Multiple Storage Backends

```python
from abc import ABC, abstractmethod

class Cache(ABC):
    @abstractmethod
    def get(self, key):
        pass
    
    @abstractmethod
    def set(self, key, value):
        pass

class RedisCache:
    def __init__(self):
        self.data = {}
    
    def get(self, key):
        return self.data.get(key)
    
    def set(self, key, value):
        self.data[key] = value

class MemcachedCache:
    def __init__(self):
        self.data = {}
    
    def get(self, key):
        return self.data.get(key)
    
    def set(self, key, value):
        self.data[key] = value

# Register both as Cache implementations
Cache.register(RedisCache)
Cache.register(MemcachedCache)

def use_cache(cache: Cache):
    cache.set('key', 'value')
    return cache.get('key')

# Works with either cache
redis = RedisCache()
memcached = MemcachedCache()

print(isinstance(redis, Cache))        # True
print(isinstance(memcached, Cache))    # True

print(use_cache(redis))                # 'value'
print(use_cache(memcached))            # 'value'
```

## Chained Register

```python
from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass
    
    @abstractmethod
    def deserialize(self, data):
        pass

class JsonSerializer:
    def serialize(self, obj):
        import json
        return json.dumps(obj)
    
    def deserialize(self, data):
        import json
        return json.loads(data)

class PickleSerializer:
    def serialize(self, obj):
        import pickle
        return pickle.dumps(obj)
    
    def deserialize(self, data):
        import pickle
        return pickle.loads(data)

# Chain registrations
Serializer.register(JsonSerializer)
Serializer.register(PickleSerializer)

def process_data(serializer: Serializer, obj):
    serialized = serializer.serialize(obj)
    return serializer.deserialize(serialized)

data = {'name': 'Alice', 'age': 30}
js = JsonSerializer()
print(isinstance(js, Serializer))  # True
print(process_data(js, data))      # {'name': 'Alice', 'age': 30}
```

## Subclass Checking

```python
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger:
    def log(self, message):
        print(message)

class FileLogger:
    def log(self, message):
        with open('log.txt', 'a') as f:
            f.write(message + '
')

Logger.register(ConsoleLogger)
Logger.register(FileLogger)

# Check subclass relationship
print(issubclass(ConsoleLogger, Logger))   # True
print(issubclass(FileLogger, Logger))      # True

# Check instance relationship
console = ConsoleLogger()
print(isinstance(console, Logger))         # True

# Use in type checking
def get_logger(config) -> Logger:
    if config.get('output') == 'console':
        return ConsoleLogger()
    else:
        return FileLogger()
```

## Virtual Subclass Benefits

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount):
        pass

# Existing third-party class
class StripeProcessor:
    def process(self, amount):
        return f"Processing ${amount} with Stripe"

# Register without modifying the original class
PaymentProcessor.register(StripeProcessor)

# Now you can write functions expecting PaymentProcessor
def charge_user(processor: PaymentProcessor, amount: float):
    '''Works with any registered PaymentProcessor'''
    return processor.process(amount)

stripe = StripeProcessor()
print(charge_user(stripe, 100))  # Works!
```

## Limitations of Virtual Subclasses

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle:
    def draw(self):
        print("Drawing circle")

# Register Circle as virtual Drawable
Drawable.register(Circle)

# This doesn't enforce the interface!
class BadCircle:
    pass

# Still creates virtual subclass, but doesn't implement interface
Drawable.register(BadCircle)

# isinstance checks pass but interface isn't guaranteed
print(isinstance(BadCircle(), Drawable))  # True!
bad = BadCircle()
# bad.draw()  # AttributeError - draw method doesn't exist!
```

## Best Practices

- Use register() for adapting existing classes
- Ensure registered classes actually implement the interface
- Document the expected interface clearly
- Consider inheritance for new classes (enforces interface)
- Use ABC with abstractmethod for strict enforcement
- Register for duck typing compatibility
