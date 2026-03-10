# Instance Attributes


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Instance attributes are variables that belong to individual object instances, storing unique state for each object.

---

## What are Instances

### 1. Definition

Attributes specific to each object instance.

```python
class Student:
    def __init__(self, name, major):
        self.name = name    # instance attribute
        self.major = major  # instance attribute

a = Student("Lee", "Math")
b = Student("Kim", "Physics")
```

### 2. Independent State

```python
print(a.name)  # "Lee"
print(b.name)  # "Kim"
# Each instance has its own values
```

### 3. Created in `__init__`

Best practice: define in constructor.

---

## Creating Attributes

### 1. In Constructor (Good)

```python
class Student:
    def __init__(self, name, major, courses):
        self.name = name
        self.major = major
        self.courses = courses

a = Student("Lee", "Math", ["Calculus", "Algebra"])
```

### 2. Dynamic (Bad)

```python
class Student:
    pass

a = Student()
a.name = "Lee"      # Created dynamically
a.major = "Math"    # Not recommended
```

### 3. In Methods (Sometimes)

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def start(self):
        self.start_time = time.time()  # Created in method
```

---

## Accessing Attributes

### 1. Direct Access

```python
student = Student("Lee", "Math", [])
print(student.name)   # Read
student.name = "Kim"  # Write
```

### 2. Via Methods

```python
class Student:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
```

### 3. Using `getattr`/`setattr`

```python
name = getattr(student, 'name')
setattr(student, 'name', 'Park')
```

---

## Mutable Attributes

### 1. List Attributes

```python
class Student:
    def __init__(self, name, courses):
        self.courses = courses  # mutable list

student = Student("Lee", ["Math"])
student.courses.append("Physics")
print(student.courses)  # ["Math", "Physics"]
```

### 2. Careful with Defaults

```python
# WRONG - mutable default
class Student:
    def __init__(self, name, courses=[]):
        self.courses = courses

# CORRECT - create new list
class Student:
    def __init__(self, name, courses=None):
        self.courses = courses if courses else []
```

### 3. Dictionary Attributes

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}  # mutable dict
    
    def add_grade(self, subject, grade):
        self.grades[subject] = grade
```

---

## Attribute Patterns

### 1. Simple Data

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### 2. Computed Once

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height  # computed once
```

### 3. Lazy Initialization

```python
class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self._data = None  # lazy load
    
    @property
    def data(self):
        if self._data is None:
            self._data = load_file(self.filename)
        return self._data
```

---

## Special Attributes

### 1. `__dict__`

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

a = Student("Lee", "Math")
print(a.__dict__)
# {'name': 'Lee', 'major': 'Math'}
```

### 2. Modifying `__dict__`

```python
a.__dict__['age'] = 20  # Adds age attribute
print(a.age)  # 20
```

### 3. `vars()` Function

```python
print(vars(a))
# Same as a.__dict__
```

---

## Attribute Methods

### 1. Adding Attributes

```python
class Student:
    def __init__(self, name, major, courses):
        self.name = name
        self.major = major
        self.courses = courses
    
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
```

### 2. Removing Attributes

```python
def drop_course(self, course):
    if course in self.courses:
        self.courses.remove(course)
```

### 3. Querying Attributes

```python
def has_course(self, course):
    return course in self.courses
```

---

## Instance vs Class

### 1. Instance Attributes

```python
class Student:
    def __init__(self, name):
        self.name = name  # instance

a = Student("Lee")
b = Student("Kim")
# Each has own name
```

### 2. Different Values

```python
a.name = "Park"
print(a.name)  # "Park"
print(b.name)  # "Kim" - unchanged
```

### 3. Independence

Changes to one instance don't affect others.

---

## Common Mistakes

### 1. Forgetting `self`

```python
# WRONG
class Student:
    def __init__(self, name):
        name = name  # local variable!

# CORRECT
class Student:
    def __init__(self, name):
        self.name = name
```

### 2. Mutable Defaults

```python
# WRONG
def __init__(self, courses=[]):
    self.courses = courses

# CORRECT
def __init__(self, courses=None):
    self.courses = courses or []
```

### 3. Shadowing Names

```python
class Student:
    def __init__(self, name):
        self.name = name
    
    def process(self, name):  # parameter shadows attribute
        # Use self.name for attribute
        # Use name for parameter
        return f"{self.name} processes {name}"
```

---

## Key Takeaways

- Instance attributes store object-specific state.
- Define in `__init__` for clarity.
- Each instance has independent attributes.
- Access via `self` inside methods.
- Avoid mutable default arguments.
