# Encapsulation

Encapsulation restricts direct access to an object's data and controls how it can be modified through well-defined interfaces.

---

## What is Encapsulation

Encapsulation is the mechanism of restricting access to certain details and controlling access to an object's data.

### 1. Bundling Data

```python
class Person:
    def __init__(self, name, age):
        self.__name = name  # private
        self.__age = age    # private
```

Data and methods are bundled into a single unit.

### 2. Controlled Access

```python
def get_name(self):
    return self.__name

def set_age(self, age):
    if 0 < age < 120:
        self.__age = age
```

Access is controlled through public methods.

### 3. Information Hiding

Internal implementation details are hidden from the outside.

---

## Access Levels

### 1. Public Attributes

```python
class Hello:
    def __init__(self):
        self.a = 1  # public
```

Accessible from anywhere.

### 2. Weak Private (`_`)

```python
class Hello:
    def __init__(self):
        self._b = 2  # weak private
```

Convention: internal use only, but still accessible.

### 3. Private (`__`)

```python
class Hello:
    def __init__(self):
        self.__c = 3  # private
```

Name mangling prevents direct external access.

---

## Private Attributes

### 1. Cannot Access Directly

```python
class Person:
    def __init__(self, name):
        self.__name = name

person = Person("John")
print(person.__name)  # AttributeError
```

### 2. Use Getter Methods

```python
class Person:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

person = Person("John")
print(person.get_name())  # Works
```

### 3. Use Setter Methods

```python
def set_age(self, age):
    if 0 < age < 120:
        self.__age = age
    else:
        raise ValueError("Invalid age")
```

Setters enable validation logic.

---

## Private Methods

### 1. Internal Logic

```python
class Hello:
    def __print_c(self):  # private method
        print(self.__c)
```

Private methods are for internal use only.

### 2. Cannot Call Externally

```python
m = Hello()
m.__print_c()  # AttributeError
```

### 3. Expose via Public

```python
def print_c(self):  # public method
    self.__print_c()

m.print_c()  # Works
```

---

## Getters and Setters

### 1. Basic Pattern

```python
class Person:
    def __init__(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
```

### 2. With Validation

```python
def set_age(self, age):
    if 0 < age < 120:
        self.__age = age
    else:
        raise ValueError("Invalid age")
```

### 3. Read-Only Attributes

```python
def get_name(self):
    return self.__name
# No setter - read-only
```

---

## Why Encapsulation

### 1. Data Protection

Prevents accidental modification of internal state.

### 2. Controlled Interface

Changes to internal implementation don't break external code.

### 3. Validation Logic

Setters can enforce business rules and constraints.

---

## Inheritance Example

### 1. Cannot Access Private

```python
class Polygon:
    def set_values(self, width, height):
        self.__width = width
        self.__height = height

class Rectangle(Polygon):
    def compute_area(self):
        return self.__width * self.__height  # Error!
```

### 2. Use Public Methods

```python
class Polygon:
    def set_values(self, width, height):
        self.__width = width
        self.__height = height
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height

class Rectangle(Polygon):
    def compute_area(self):
        return self.get_width() * self.get_height()
```

---

## Key Takeaways

- Encapsulation bundles data and methods.
- Use `__` for truly private attributes.
- Use `_` for internal-use conventions.
- Provide getters/setters for controlled access.
- Enables validation and data protection.
