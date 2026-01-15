# Class Methods

Class methods receive the class itself as the first argument, enabling operations on class-level data and alternative constructors.

---

## What are Class Methods

### 1. Decorated with `@classmethod`

```python
class Student:
    count = 0
    
    @classmethod
    def increment_count(cls):
        cls.count += 1
```

### 2. Receive `cls`

First parameter is the class, not instance.

### 3. Operate on Class

Modify or access class-level attributes.

---

## Defining Class Methods

### 1. Basic Syntax

```python
class MyClass:
    class_var = 0
    
    @classmethod
    def class_method(cls):
        cls.class_var += 1
```

### 2. Call via Class

```python
MyClass.class_method()
print(MyClass.class_var)  # 1
```

### 3. Call via Instance

```python
obj = MyClass()
obj.class_method()  # Works but not idiomatic
```

---

## Class Method Use Cases

### 1. Modify Class Attributes

```python
class Student:
    university = 'Yonsei'
    
    @classmethod
    def change_university(cls, new_name):
        cls.university = new_name

Student.change_university('YonHei')
```

### 2. Track All Instances

```python
class Student:
    students_list = []
    mandatory = ['Chapel']
    
    @classmethod
    def add_mandatory(cls, course):
        if course not in cls.mandatory:
            cls.mandatory.append(course)
            for student in cls.students_list:
                student.subject.append(course)
```

### 3. Global Configuration

```python
class Logger:
    enable_debug = False
    
    @classmethod
    def set_debug(cls):
        cls.enable_debug = True
```

---

## Alternative Constructors

### 1. Factory Pattern

```python
from datetime import date

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    @classmethod
    def from_age(cls, name, age):
        current_year = date.today().year
        return cls(name, current_year - age)

p = Person.from_age("Alice", 30)
```

### 2. Parse Data

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @classmethod
    def from_string(cls, point_str):
        x, y = map(float, point_str.split(','))
        return cls(x, y)

p = Point.from_string("3.5,2.1")
```

### 3. Multiple Formats

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_str):
        y, m, d = map(int, date_str.split('-'))
        return cls(y, m, d)
    
    @classmethod
    def today(cls):
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)
```

---

## Student Example

### 1. Class Setup

```python
class Student:
    students_list = []
    mandatory = ['Chapel']
    
    def __init__(self, name, major, courses):
        self.name = name
        self.major = major
        self.courses = courses
        Student.students_list.append(self)
```

### 2. Add Mandatory Course

```python
@classmethod
def add_mandatory(cls, course):
    if course not in cls.mandatory:
        cls.mandatory.append(course)
        for student in cls.students_list:
            student.courses.append(course)
```

### 3. Drop Mandatory Course

```python
@classmethod
def drop_mandatory(cls, course):
    if course in cls.mandatory:
        cls.mandatory.remove(course)
        for student in cls.students_list:
            if course in student.courses:
                student.courses.remove(course)
```

---

## `cls` vs `self`

### 1. `cls` Parameter

```python
@classmethod
def class_method(cls):
    # cls refers to the class
    cls.class_var = 10
```

### 2. `self` Parameter

```python
def instance_method(self):
    # self refers to the instance
    self.instance_var = 10
```

### 3. Different Scopes

Class methods operate on class, instance methods on instances.

---

## Inheritance Behavior

### 1. Inherited Methods

```python
class Parent:
    count = 0
    
    @classmethod
    def increment(cls):
        cls.count += 1

class Child(Parent):
    pass

Child.increment()
print(Child.count)  # 1
print(Parent.count) # 0
```

### 2. `cls` is Dynamic

`cls` refers to the calling class.

### 3. Polymorphic Behavior

```python
class Shape:
    @classmethod
    def create_default(cls):
        return cls()  # Creates instance of calling class

class Circle(Shape):
    pass

c = Circle.create_default()  # Creates Circle
```

---

## When to Use

### 1. Modify Class State

```python
@classmethod
def reset_counter(cls):
    cls.counter = 0
```

### 2. Alternative Constructors

```python
@classmethod
def from_json(cls, json_str):
    data = json.loads(json_str)
    return cls(**data)
```

### 3. Affect All Instances

```python
@classmethod
def enable_feature_for_all(cls):
    cls.feature_enabled = True
```

---

## Common Patterns

### 1. Configuration

```python
class Config:
    debug_mode = False
    
    @classmethod
    def enable_debug(cls):
        cls.debug_mode = True
    
    @classmethod
    def disable_debug(cls):
        cls.debug_mode = False
```

### 2. Registry

```python
class Plugin:
    _plugins = []
    
    @classmethod
    def register(cls, plugin):
        cls._plugins.append(plugin)
    
    @classmethod
    def get_plugins(cls):
        return cls._plugins[:]
```

### 3. Singleton Pattern

```python
class Singleton:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
```

---

## Class vs Static

### 1. Class Method

```python
@classmethod
def class_method(cls, param):
    # Has access to cls
    cls.class_var = param
```

### 2. Static Method

```python
@staticmethod
def static_method(param):
    # No access to cls or self
    return param * 2
```

### 3. Choose Based on Need

Use class method if you need class reference.

---

## Key Takeaways

- Class methods receive `cls` as first parameter.
- Use `@classmethod` decorator.
- Modify class-level attributes.
- Create alternative constructors.
- Affect all instances of the class.
