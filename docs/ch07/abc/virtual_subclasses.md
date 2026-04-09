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

---

## Runnable Example: `factory_pattern_with_abc_example.py`

```python
"""
Factory Pattern with Abstract Base Classes

Combines ABCs for defining contracts with the Factory Pattern
for creating objects. This is a payroll system where different
employee types have different salary calculation methods.

Topics covered:
- Abstract base classes (ABCMeta, abstractmethod)
- Factory pattern (centralized object creation)
- Polymorphism (same interface, different behavior)
- Static methods in factory classes

Based on concepts from Python-100-Days examples 12-13 and ch06/abc materials.
"""

from abc import ABCMeta, abstractmethod


# =============================================================================
# Example 1: Abstract Employee Class
# =============================================================================

class Employee(metaclass=ABCMeta):
    """Abstract base class defining the employee contract.

    All employee types must implement get_salary().
    This ensures polymorphic salary calculation.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_salary(self) -> float:
        """Calculate monthly salary. Must be implemented by subclasses."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}')"

    def __repr__(self):
        return self.__str__()


# =============================================================================
# Example 2: Concrete Employee Subclasses
# =============================================================================

class Manager(Employee):
    """Department manager with fixed salary."""

    def __init__(self, name: str, monthly_salary: float = 15000.0):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_salary(self) -> float:
        return self.monthly_salary


class Programmer(Employee):
    """Programmer paid by hours worked."""

    def __init__(self, name: str, hourly_rate: float = 200.0,
                 hours_worked: int = 0):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_salary(self) -> float:
        return self.hourly_rate * self.hours_worked


class Salesperson(Employee):
    """Salesperson with base salary plus commission."""

    def __init__(self, name: str, base_salary: float = 1800.0,
                 sales: float = 0.0, commission_rate: float = 0.05):
        super().__init__(name)
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate

    def get_salary(self) -> float:
        return self.base_salary + self.sales * self.commission_rate


# =============================================================================
# Example 3: Factory for Employee Creation
# =============================================================================

class EmployeeFactory:
    """Factory class for creating employees.

    The Factory Pattern decouples object creation from usage.
    Client code doesn't need to know the specific class - just
    the type code. This makes it easy to add new employee types.
    """

    _registry = {
        'M': Manager,
        'P': Programmer,
        'S': Salesperson,
    }

    @staticmethod
    def create(emp_type: str, *args, **kwargs) -> Employee:
        """Create an employee by type code.

        Args:
            emp_type: 'M' for Manager, 'P' for Programmer, 'S' for Salesperson.
            *args, **kwargs: Passed to the employee constructor.

        Raises:
            ValueError: If emp_type is not recognized.

        >>> emp = EmployeeFactory.create('P', 'Alice', hours_worked=160)
        >>> emp.get_salary()
        32000.0
        """
        cls = EmployeeFactory._registry.get(emp_type.upper())
        if cls is None:
            valid = ', '.join(EmployeeFactory._registry.keys())
            raise ValueError(f"Unknown type '{emp_type}'. Valid: {valid}")
        return cls(*args, **kwargs)

    @classmethod
    def register(cls, type_code: str, employee_class: type):
        """Register a new employee type dynamically.

        This makes the factory extensible without modifying its source.
        """
        if not issubclass(employee_class, Employee):
            raise TypeError(f"{employee_class} must be a subclass of Employee")
        cls._registry[type_code.upper()] = employee_class


# =============================================================================
# Example 4: Polymorphic Payroll Processing
# =============================================================================

def process_payroll(employees: list[Employee]) -> None:
    """Calculate and display payroll for all employees.

    Thanks to polymorphism, we don't need to check employee types.
    Each employee knows how to calculate its own salary.
    """
    print("=== Monthly Payroll ===")
    print(f"{'Name':<15} {'Type':<15} {'Salary':>10}")
    print("-" * 42)

    total = 0.0
    for emp in employees:
        salary = emp.get_salary()
        total += salary
        emp_type = emp.__class__.__name__
        print(f"{emp.name:<15} {emp_type:<15} ${salary:>9,.2f}")

    print("-" * 42)
    print(f"{'Total':<30} ${total:>9,.2f}")
    print()


# =============================================================================
# Example 5: Extending the Factory
# =============================================================================

class Intern(Employee):
    """Intern with stipend (extending the system)."""

    def __init__(self, name: str, stipend: float = 500.0):
        super().__init__(name)
        self.stipend = stipend

    def get_salary(self) -> float:
        return self.stipend


def demo_extensibility():
    """Show how to add new employee types without modifying existing code."""
    print("=== Extending with New Types ===")

    # Register new type at runtime
    EmployeeFactory.register('I', Intern)

    intern = EmployeeFactory.create('I', 'New Intern', stipend=800)
    print(f"{intern.name}: ${intern.get_salary():.2f}")

    # Demonstrate that abstract class can't be instantiated
    print("\nTrying to instantiate abstract Employee...")
    try:
        emp = Employee("Nobody")
    except TypeError as e:
        print(f"  TypeError: {e}")


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    # Create employees using factory
    employees = [
        EmployeeFactory.create('M', 'Alice'),
        EmployeeFactory.create('P', 'Bob', hours_worked=120),
        EmployeeFactory.create('P', 'Charlie', hours_worked=85),
        EmployeeFactory.create('S', 'Diana', sales=123000),
    ]

    process_payroll(employees)
    demo_extensibility()
```

---

## Exercises

**Exercise 1.**
Create an ABC `Storage` with abstract methods `save(key, value)` and `load(key)`. Then create two classes---`DictStorage` and `ListStorage`---that do NOT inherit from `Storage`. Register both as virtual subclasses using `Storage.register()`. Demonstrate that `isinstance()` and `issubclass()` checks pass for both, and call their methods through a function typed to accept `Storage`.

??? success "Solution to Exercise 1"

        from abc import ABC, abstractmethod

        class Storage(ABC):
            @abstractmethod
            def save(self, key, value):
                pass

            @abstractmethod
            def load(self, key):
                pass

        class DictStorage:
            def __init__(self):
                self._data = {}

            def save(self, key, value):
                self._data[key] = value

            def load(self, key):
                return self._data.get(key)

        class ListStorage:
            def __init__(self):
                self._entries = []

            def save(self, key, value):
                self._entries.append((key, value))

            def load(self, key):
                for k, v in reversed(self._entries):
                    if k == key:
                        return v
                return None

        Storage.register(DictStorage)
        Storage.register(ListStorage)

        print(isinstance(DictStorage(), Storage))   # True
        print(isinstance(ListStorage(), Storage))   # True
        print(issubclass(DictStorage, Storage))     # True
        print(issubclass(ListStorage, Storage))     # True

        def use_storage(store: Storage):
            store.save("color", "blue")
            return store.load("color")

        print(use_storage(DictStorage()))   # blue
        print(use_storage(ListStorage()))   # blue

---

**Exercise 2.**
Define an ABC `Formatter` with an abstract method `format(text)`. Create a concrete subclass `UpperFormatter` that inherits from `Formatter`. Then create a third-party class `HTMLFormatter` (no inheritance) and register it as a virtual subclass. Show the key limitation: create a `BrokenFormatter` class with no `format` method, register it, and demonstrate that `isinstance()` still returns `True` even though calling `format()` raises `AttributeError`.

??? success "Solution to Exercise 2"

        from abc import ABC, abstractmethod

        class Formatter(ABC):
            @abstractmethod
            def format(self, text):
                pass

        class UpperFormatter(Formatter):
            def format(self, text):
                return text.upper()

        class HTMLFormatter:
            def format(self, text):
                return f"<p>{text}</p>"

        Formatter.register(HTMLFormatter)

        print(isinstance(UpperFormatter(), Formatter))  # True
        print(isinstance(HTMLFormatter(), Formatter))   # True

        # Limitation: BrokenFormatter has no format method
        class BrokenFormatter:
            pass

        Formatter.register(BrokenFormatter)
        print(isinstance(BrokenFormatter(), Formatter))  # True!

        try:
            BrokenFormatter().format("hello")
        except AttributeError as e:
            print(f"Error: {e}")
            # Error: 'BrokenFormatter' object has no attribute 'format'

---

**Exercise 3.**
Build a plugin system using virtual subclasses. Define an ABC `Plugin` with abstract methods `name()` (as a property) and `execute(data)`. Write a `PluginRegistry` class that keeps a list of registered plugin classes. Add a `register_plugin(cls)` method that calls `Plugin.register(cls)` and stores the class. Then create three plugin classes without inheritance, register them, and iterate through the registry to run `execute` on each.

??? success "Solution to Exercise 3"

        from abc import ABC, abstractmethod

        class Plugin(ABC):
            @property
            @abstractmethod
            def name(self):
                pass

            @abstractmethod
            def execute(self, data):
                pass

        class PluginRegistry:
            def __init__(self):
                self._plugins = []

            def register_plugin(self, cls):
                Plugin.register(cls)
                self._plugins.append(cls)

            def run_all(self, data):
                results = {}
                for cls in self._plugins:
                    instance = cls()
                    results[instance.name] = instance.execute(data)
                return results

        class UpperPlugin:
            @property
            def name(self):
                return "upper"

            def execute(self, data):
                return data.upper()

        class ReversePlugin:
            @property
            def name(self):
                return "reverse"

            def execute(self, data):
                return data[::-1]

        class LengthPlugin:
            @property
            def name(self):
                return "length"

            def execute(self, data):
                return len(data)

        registry = PluginRegistry()
        registry.register_plugin(UpperPlugin)
        registry.register_plugin(ReversePlugin)
        registry.register_plugin(LengthPlugin)

        results = registry.run_all("hello world")
        for name, result in results.items():
            print(f"{name}: {result}")
        # upper: HELLO WORLD
        # reverse: dlrow olleh
        # length: 11
