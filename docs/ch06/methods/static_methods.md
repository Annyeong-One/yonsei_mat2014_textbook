# Static Methods


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Static methods are utility functions that belong to a class but don't access instance or class data.

---

## What are Static Methods

### 1. Decorated with `@staticmethod`

```python
class MathTools:
    @staticmethod
    def add(a, b):
        return a + b
```

### 2. No `self` or `cls`

Don't receive implicit first parameter.

### 3. Namespace Functions

Logically grouped with class but independent.

---

## Defining Static Methods

### 1. Basic Syntax

```python
class MyClass:
    @staticmethod
    def utility_function(param):
        return param * 2
```

### 2. Call via Class

```python
result = MyClass.utility_function(5)
```

### 3. Call via Instance

```python
obj = MyClass()
result = obj.utility_function(5)
```

---

## Static vs Instance

### 1. Instance Method

```python
class Student:
    def greet(self):
        return f"Hello, {self.name}"

a = Student()
print(Student.greet)  # <function>
print(a.greet)        # <bound method>
```

### 2. Static Method

```python
class Student:
    @staticmethod
    def is_workday(day):
        # implementation
        pass

print(Student.is_workday)  # <function>
print(a.is_workday)        # <function> (not bound!)
```

### 3. Not Bound

Static methods are never bound to instances.

---

## Use Cases

### 1. Utility Functions

```python
class StringUtils:
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]
    
    @staticmethod
    def capitalize_words(s):
        return ' '.join(word.capitalize() for word in s.split())
```

### 2. Validation

```python
class Validator:
    @staticmethod
    def is_valid_email(email):
        return '@' in email and '.' in email
    
    @staticmethod
    def is_valid_phone(phone):
        return len(phone) == 10 and phone.isdigit()
```

### 3. Formatting

```python
class Formatter:
    @staticmethod
    def format_currency(amount):
        return f"${amount:,.2f}"
    
    @staticmethod
    def format_date(date):
        return date.strftime("%Y-%m-%d")
```

---

## Workday Example

### 1. Date Validation

```python
from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def is_workday(day):
        day_obj = datetime.strptime(day, '%Y-%m-%d')
        # Saturday = 5, Sunday = 6
        return day_obj.weekday() not in [5, 6]
```

### 2. Usage

```python
student = Student("Lee")
for day in range(10, 20):
    date = f"2024-04-{day}"
    if student.is_workday(date):
        print(f"{date} is a workday")
```

### 3. No Instance Access

Static method doesn't use `self.name`.

---

## When to Use Static

### 1. Pure Utility

```python
class Math:
    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * Math.factorial(n - 1)
```

### 2. No Class/Instance Data

Function doesn't need access to `self` or `cls`.

### 3. Logical Grouping

```python
class DateUtils:
    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    @staticmethod
    def days_in_month(month, year):
        # implementation
        pass
```

---

## Static vs Class Method

### 1. Static Method

```python
class Config:
    @staticmethod
    def validate_port(port):
        return 1 <= port <= 65535
```

No access to class or instance.

### 2. Class Method

```python
class Config:
    default_port = 8080
    
    @classmethod
    def set_default_port(cls, port):
        cls.default_port = port
```

Has access to class via `cls`.

### 3. Choose Appropriately

Use static if no class access needed.

---

## Comparison Example

### 1. Three Method Types

```python
class Demo:
    class_var = 10
    
    def instance_method(self):
        return f"Instance: {self.class_var}"
    
    @classmethod
    def class_method(cls):
        return f"Class: {cls.class_var}"
    
    @staticmethod
    def static_method(value):
        return f"Static: {value}"
```

### 2. Calling Methods

```python
obj = Demo()

obj.instance_method()           # Needs instance
Demo.class_method()             # Works on class
Demo.static_method(42)          # Independent
```

### 3. Different Purposes

Each serves distinct needs.

---

## Real-World Examples

### 1. Conversion Utilities

```python
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9/5 + 32
    
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9
```

### 2. String Processing

```python
class TextProcessor:
    @staticmethod
    def remove_punctuation(text):
        import string
        return text.translate(str.maketrans('', '', string.punctuation))
    
    @staticmethod
    def word_count(text):
        return len(text.split())
```

### 3. Data Validation

```python
class InputValidator:
    @staticmethod
    def is_positive(num):
        return num > 0
    
    @staticmethod
    def is_in_range(num, low, high):
        return low <= num <= high
```

---

## Design Considerations

### 1. Alternative: Module Function

```python
# Could be a module-level function
def is_workday(day):
    # implementation
    pass

# vs class static method
class DateUtils:
    @staticmethod
    def is_workday(day):
        # implementation
        pass
```

### 2. Use Static When

- Function relates to class conceptually
- Want to group related utilities
- Might need polymorphism later

### 3. Use Module Function When

- Truly independent utility
- No relationship to any class

---

## Inheritance

### 1. Can Override

```python
class Parent:
    @staticmethod
    def method():
        return "Parent"

class Child(Parent):
    @staticmethod
    def method():
        return "Child"

print(Child.method())  # "Child"
```

### 2. Still Not Bound

```python
c = Child()
print(c.method)  # <function> (not bound method)
```

### 3. Polymorphic Behavior

Static methods can be overridden in subclasses.

---

## Key Takeaways

- Static methods don't receive `self` or `cls`.
- Use `@staticmethod` decorator.
- For utility functions grouped with class.
- Not bound to instances.
- Use when no class/instance access needed.
