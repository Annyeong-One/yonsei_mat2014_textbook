# Comparison Operators

Comparison dunder methods enable equality testing and ordering operations on custom objects.

---

## Equality Operators

### 1. Equal: `__eq__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True
```

### 2. Not Equal: `__ne__`

```python
def __ne__(self, other):
    return not self.__eq__(other)

print(p1 != p2)  # False
```

### 3. Default Behavior

Without `__eq__`, Python uses identity (`is`).

---

## Ordering Operators

### 1. Less Than: `__lt__`

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __lt__(self, other):
        return self.salary < other.salary

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)
print(e1 < e2)  # True
```

### 2. Less or Equal: `__le__`

```python
def __le__(self, other):
    return self.salary <= other.salary
```

### 3. Greater Than: `__gt__`

```python
def __gt__(self, other):
    return self.salary > other.salary
```

---

## Comparison Table

### 1. All Operators

| Operator | Method | Example |
|----------|--------|---------|
| `==` | `__eq__` | `a == b` |
| `!=` | `__ne__` | `a != b` |
| `<` | `__lt__` | `a < b` |
| `<=` | `__le__` | `a <= b` |
| `>` | `__gt__` | `a > b` |
| `>=` | `__ge__` | `a >= b` |

### 2. No Automatic Inference

```python
# Defining __eq__ does NOT give you __ne__
# Defining __lt__ does NOT give you __le__
```

### 3. Must Implement Each

Each comparison needs its own method.

---

## `@total_ordering`

### 1. Reduce Redundancy

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        return self.grade == other.grade
    
    def __lt__(self, other):
        return self.grade < other.grade
    # __le__, __gt__, __ge__ auto-generated!
```

### 2. Requirements

Must define `__eq__` and one ordering method.

### 3. Auto-Generated

```python
# Only define:
__eq__ and __lt__

# Get for free:
__ne__, __le__, __gt__, __ge__
```

---

## Complete Example

### 1. Employee Class

```python
from functools import total_ordering

@total_ordering
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.salary == other.salary
    
    def __lt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.salary < other.salary
    
    def __repr__(self):
        return f"Employee({self.name}, ${self.salary})"
```

### 2. Usage

```python
e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)
e3 = Employee("Charlie", 50000)

print(e1 == e3)  # True
print(e1 < e2)   # True
print(e2 > e1)   # True (auto-generated)
print(e1 <= e3)  # True (auto-generated)
```

### 3. Sorting

```python
employees = [e2, e1, e3]
sorted_emp = sorted(employees)
# [Employee(Alice, $50000), Employee(Charlie, $50000), Employee(Bob, $60000)]
```

---

## Type Checking

### 1. Check Type

```python
def __eq__(self, other):
    if not isinstance(other, Point):
        return NotImplemented
    return self.x == other.x and self.y == other.y
```

### 2. `NotImplemented`

```python
def __eq__(self, other):
    if not isinstance(other, MyClass):
        return NotImplemented  # Not False!
    return self.value == other.value
```

### 3. Allows Delegation

`NotImplemented` lets Python try reversed comparison.

---

## Common Patterns

### 1. Single Attribute

```python
class Student:
    def __eq__(self, other):
        return self.grade == other.grade
    
    def __lt__(self, other):
        return self.grade < other.grade
```

### 2. Multiple Attributes

```python
class Person:
    def __eq__(self, other):
        return (self.last_name == other.last_name and
                self.first_name == other.first_name)
    
    def __lt__(self, other):
        return ((self.last_name, self.first_name) <
                (other.last_name, other.first_name))
```

### 3. Tuple Comparison

```python
def __lt__(self, other):
    return (self.year, self.month, self.day) < \
           (other.year, other.month, other.day)
```

---

## Equality vs Identity

### 1. Equality: `==`

```python
p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True (calls __eq__)
```

### 2. Identity: `is`

```python
print(p1 is p2)  # False (different objects)
```

### 3. Use Cases

- `==`: value comparison
- `is`: object identity

---

## Hash Consistency

### 1. The Rule

If `__eq__` is defined, `__hash__` should also be defined.

### 2. Hash Requirement

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
```

### 3. Immutable Only

Only define `__hash__` for immutable objects.

---

## Sorting Integration

### 1. Built-in `sorted()`

```python
employees = [
    Employee("Alice", 50000),
    Employee("Bob", 60000),
    Employee("Charlie", 45000)
]

sorted_emp = sorted(employees)
# Sorts by salary (uses __lt__)
```

### 2. Custom Key

```python
sorted_by_name = sorted(employees, key=lambda e: e.name)
```

### 3. Reverse Order

```python
sorted_desc = sorted(employees, reverse=True)
```

---

## Rich Comparison

### 1. All Six Methods

```python
class Version:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor
    
    def __eq__(self, other):
        return (self.major, self.minor) == (other.major, other.minor)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return (self.major, self.minor) < (other.major, other.minor)
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        return not self.__le__(other)
    
    def __ge__(self, other):
        return not self.__lt__(other)
```

### 2. Consistency

Ensure all methods are logically consistent.

### 3. Transitivity

If `a < b` and `b < c`, then `a < c`.

---

## Best Practices

### 1. Use `@total_ordering`

```python
from functools import total_ordering

@total_ordering
class MyClass:
    def __eq__(self, other): ...
    def __lt__(self, other): ...
```

### 2. Type Check

```python
def __eq__(self, other):
    if not isinstance(other, MyClass):
        return NotImplemented
    return self.value == other.value
```

### 3. Implement `__hash__`

If defining `__eq__`, also define `__hash__` for immutable objects.

---

## Key Takeaways

- Six comparison operators: `==`, `!=`, `<`, `<=`, `>`, `>=`.
- Each needs its own dunder method.
- Use `@total_ordering` to reduce boilerplate.
- Return `NotImplemented` for unsupported types.
- Define `__hash__` if defining `__eq__`.
