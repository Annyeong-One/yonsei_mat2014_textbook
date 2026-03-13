# Constructor & Destructor

Constructor (`__init__`) and destructor (`__del__`) manage object lifecycle in Python.

---

## Constructor: `__init__`

### 1. Purpose

Initializes new objects immediately after creation.

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

alice = Student("Alice", "Math")
```

### 2. Automatic Call

Python automatically calls `__init__` during instantiation.

```python
# These are equivalent:
a = Student("Lee", "Math")
# Student.__init__(a, "Lee", "Math")
```

### 3. Not Optional

Every class should define `__init__` for clarity.

---

## Bad Practice: No Constructor

### 1. Dynamic Assignment

```python
class Student:
    pass

a = Student()
a.name = "Lee"
a.major = "Math"
```

### 2. Problems

- No enforcement of required fields
- Runtime errors from typos
- Unclear object requirements
- Violates encapsulation

### 3. Fragile Code

```python
b = Student()
b.name = "Kim"
# Forgot to set major!
print(b.major)  # AttributeError
```

---

## Good Practice: With Constructor

### 1. Structured Initialization

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

a = Student("Lee", "Math")
```

### 2. Benefits

- Parameters are explicit
- Required fields enforced
- Self-documenting code
- Enables validation

### 3. With Validation

```python
class Student:
    def __init__(self, name, major):
        if not name:
            raise ValueError("Name required")
        self.name = name
        self.major = major
```

---

## Introspection with `vars()`

### 1. View Attributes

```python
alice = Student("Alice", "Statistics")
print(vars(alice))
# {'name': 'Alice', 'major': 'Statistics'}
```

### 2. Same as `__dict__`

```python
print(alice.__dict__)
# Same output as vars(alice)
```

### 3. Debugging Aid

Useful for inspecting object state.

---

## Constructor Patterns

### 1. Simple Assignment

```python
class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
```

### 2. With Defaults

```python
class Car:
    def __init__(self, speed=0, color="black"):
        self.speed = speed
        self.color = color
```

### 3. With Computation

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height  # computed
```

---

## Destructor: `__del__`

### 1. Purpose

Called when object is about to be destroyed.

```python
class IceCream:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"{self.name} created")
    
    def __del__(self):
        print(f"{self.name} destroyed")
```

### 2. Non-Deterministic

Timing is unpredictable—depends on garbage collection.

```python
obj = IceCream("Cone", 1500)
del obj
# Destructor may or may not run immediately
```

### 3. Reference Counting

```python
obj1 = IceCream("Cone", 1500)
obj2 = obj1  # Two references
del obj1     # __del__ NOT called yet
del obj2     # Now __del__ is called
```

---

## Destructor Limitations

### 1. Unreliable Timing

```python
def create_objects():
    obj = IceCream("Cone", 1500)
    # When is __del__ called? Unknown!

create_objects()
```

### 2. Circular References

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
a.next = b
b.next = a  # Circular reference
# Destructors may never run!
```

### 3. No Guarantees

Python doesn't guarantee `__del__` will be called.

---

## Better Alternatives

### 1. Context Managers

```python
class FileHandler:
    def __enter__(self):
        self.file = open("data.txt", "w")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileHandler() as f:
    f.write("data")
# Guaranteed cleanup
```

### 2. Explicit Methods

```python
class Resource:
    def __init__(self):
        self.resource = acquire_resource()
    
    def close(self):
        release_resource(self.resource)

r = Resource()
try:
    # Use resource
    pass
finally:
    r.close()
```

### 3. `contextlib`

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    resource = acquire_resource()
    try:
        yield resource
    finally:
        release_resource(resource)
```

---

## Constructor Best Practices

### 1. Keep Simple

```python
# Good
def __init__(self, name):
    self.name = name

# Bad - too much logic
def __init__(self, name):
    self.name = name
    self.connect_to_database()
    self.load_all_data()
```

### 2. Validate Input

```python
def __init__(self, age):
    if age < 0:
        raise ValueError("Age must be positive")
    self.age = age
```

### 3. Document Parameters

```python
def __init__(self, name, age):
    """
    Initialize a Person.
    
    Args:
        name (str): Person's name
        age (int): Person's age
    """
    self.name = name
    self.age = age
```

---

## Key Takeaways

- `__init__` initializes objects—always define it.
- Use constructors to enforce required fields.
- `vars()` and `__dict__` inspect object state.
- `__del__` is unreliable—avoid for cleanup.
- Use context managers for resource management.
