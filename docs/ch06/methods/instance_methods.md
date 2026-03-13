# Instance Methods

Instance methods are functions that belong to class instances, operating on instance-specific data.

---

## What are Instance Methods

### 1. Functions in Class

```python
class Student:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses
    
    def add_course(self, course):  # Instance method
        self.courses.append(course)
```

### 2. Receive `self`

First parameter is always `self`.

### 3. Operate on Instance

Methods modify or access instance attributes.

---

## The `self` Parameter

### 1. Reference to Instance

```python
class Student:
    def greet(self):
        print(f"Hello, I'm {self.name}")

a = Student("Lee")
a.greet()  # self = a
```

### 2. Automatic Passing

```python
# These are equivalent:
a.greet()
Student.greet(a)
```

### 3. Access Instance Data

```python
def get_info(self):
    return f"{self.name}, {self.major}"
```

---

## Defining Methods

### 1. Basic Method

```python
class Student:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses
    
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
```

### 2. Multiple Parameters

```python
def enroll(self, course, semester):
    enrollment = {
        'course': course,
        'semester': semester
    }
    self.enrollments.append(enrollment)
```

### 3. Return Values

```python
def has_course(self, course):
    return course in self.courses
```

---

## Method Examples

### 1. Getter Method

```python
class Student:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
```

### 2. Setter Method

```python
def set_name(self, name):
    if name:
        self.name = name
```

### 3. Action Method

```python
def drop_course(self, course):
    if course in self.courses:
        self.courses.remove(course)
```

---

## Calling Methods

### 1. Via Instance

```python
student = Student("Lee", ["Math"])
student.add_course("Physics")
```

### 2. Via Class

```python
Student.add_course(student, "Physics")
# Equivalent but not idiomatic
```

### 3. Chaining Methods

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self  # Return self for chaining
    
    def reset(self):
        self.count = 0
        return self

c = Counter().increment().increment().reset()
```

---

## `self` Mechanics

### 1. Must Use `self`

```python
# WRONG
def add_course(self, course):
    courses.append(course)  # NameError!

# CORRECT
def add_course(self, course):
    self.courses.append(course)
```

### 2. Access Attributes

```python
def print_info(self):
    print(f"Name: {self.name}")
    print(f"Major: {self.major}")
```

### 3. Call Other Methods

```python
def enroll_and_notify(self, course):
    self.add_course(course)
    self.send_notification()
```

---

## Instance vs Class Variables

### 1. Accessing Instance Variable

```python
class Student:
    def __init__(self, name):
        self.name = name  # instance variable
    
    def greet(self):
        return f"Hello, {self.name}"
```

### 2. Accessing Class Variable

```python
class Student:
    university = 'Yonsei'  # class variable
    
    def get_university(self):
        return Student.university  # or self.university
```

### 3. Modifying Class Variable

```python
def change_university(self, new_name):
    self.university = new_name  # WRONG - creates instance attr
    
@classmethod
def change_university(cls, new_name):
    cls.university = new_name  # CORRECT
```

---

## Method vs Function

### 1. Function Attribute

```python
def f():
    return 1

print(f)      # <function f>
print(f())    # 1
```

### 2. Method Attribute

```python
import numpy as np
x = np.array([1, 2, 3])

print(x.sum)    # <built-in method sum>
print(x.sum())  # 6
```

### 3. Bound Methods

```python
class Student:
    def greet(self):
        return "Hello"

a = Student()
print(Student.greet)  # <function greet>
print(a.greet)        # <bound method greet>
```

---

## Common Patterns

### 1. Validation

```python
def set_age(self, age):
    if 0 <= age <= 120:
        self.age = age
    else:
        raise ValueError("Invalid age")
```

### 2. Computation

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
```

### 3. State Change

```python
class Car:
    def __init__(self, speed):
        self.speed = speed
    
    def accelerate(self, amount):
        self.speed += amount
```

---

## Helper Methods

### 1. Private Methods

```python
class Student:
    def process(self):
        self._validate()
        self._compute()
    
    def _validate(self):  # "private" by convention
        if not self.name:
            raise ValueError("Name required")
    
    def _compute(self):
        pass
```

### 2. Public Interface

```python
def enroll(self, course):
    self._validate_prerequisites(course)
    self._add_to_schedule(course)
    self._update_credits()
```

### 3. Internal Logic

Keep complex logic in separate methods.

---

## Method Signatures

### 1. No Parameters

```python
def reset(self):
    self.count = 0
```

### 2. With Parameters

```python
def add(self, item, priority=0):
    self.items.append((item, priority))
```

### 3. Variable Arguments

```python
def add_multiple(self, *courses):
    for course in courses:
        self.add_course(course)
```

---

## Key Takeaways

- Instance methods operate on instance data.
- First parameter is always `self`.
- Access instance attributes via `self`.
- Call methods via instance: `obj.method()`.
- Use `_method` for internal helpers.
