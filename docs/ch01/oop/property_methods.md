# Getter Setter Deleter

## Property Methods

### 1. The Three Methods

A property can define three methods:

- **Getter** (`@property`): Controls read access
- **Setter** (`@name.setter`): Controls write access
- **Deleter** (`@name.deleter`): Controls deletion

### 2. Complete Example

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property  # getter
    def name(self):
        return self._name

    @name.setter  # setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError("Name must be alphabetic")
        self._name = value

    @name.deleter  # deleter
    def name(self):
        print("Deleting name")
        del self._name
```

### 3. Usage Pattern

```python
p = Person("Alice")
print(p.name)        # calls the getter → "Alice"
p.name = "Bob"       # calls the setter → OK
# p.name = "1234"    # ValueError: Name must be alphabetic
del p.name           # Deleting name
```

## Getter Method

### 1. Basic Getter

The `@property` decorator transforms a method into a read-only property:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
```

### 2. Computed Getter

Getters can return computed values:

```python
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
```

### 3. Validation in Getter

You can add logic in getters:

```python
@property
def age(self):
    if not hasattr(self, '_age'):
        return 0
    return self._age
```

## Setter Method

### 1. Basic Setter

Define setter using `@property_name.setter`:

```python
@name.setter
def name(self, value):
    if not value.isalpha():
        raise ValueError("Name must be alphabetic")
    self._name = value
```

### 2. Validation Logic

Setters enforce invariants:

```python
class Person:
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be integer")
        if value < 0 or value > 150:
            raise ValueError("Invalid age range")
        self._age = value
```

### 3. Transformation

Setters can transform input:

```python
@name.setter
def name(self, value):
    self._name = value.strip().title()
```

## Deleter Method

### 1. Basic Deleter

Define deleter using `@property_name.deleter`:

```python
@name.deleter
def name(self):
    print("Deleting name")
    del self._name
```

### 2. Cleanup Actions

Deleters can perform cleanup:

```python
class Database:
    @property
    def connection(self):
        return self._connection
    
    @connection.deleter
    def connection(self):
        if hasattr(self, '_connection'):
            self._connection.close()
            del self._connection
```

### 3. After Deletion

After deletion, accessing raises `AttributeError`:

```python
p = Person("Alice")
del p.name
print(p.name)  # ❌ AttributeError
```

## Practical Examples

### 1. Temperature Conversion

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9
```

### 2. Lazy Loading

```python
class DataLoader:
    @property
    def data(self):
        if not hasattr(self, '_data'):
            print("Loading data...")
            self._data = self._load_from_disk()
        return self._data
    
    def _load_from_disk(self):
        # Heavy operation
        return [1, 2, 3, 4, 5]
```

### 3. Dependent Properties

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Must be positive")
        self._width = value
    
    @property
    def area(self):
        return self._width * self._height
```
