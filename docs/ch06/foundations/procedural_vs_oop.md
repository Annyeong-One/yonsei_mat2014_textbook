# Procedural vs OOP

Understanding the fundamental differences between procedural and object-oriented programming paradigms.

---

## Programming Paradigms

### 1. Procedural Focus

Organized around **procedures or functions** that operate on data.

```python
def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

width = 5
height = 3
area = calculate_area(width, height)
```

### 2. OOP Focus

Organized around **objects** that encapsulate data and behavior.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
area = rect.area()
```

### 3. Key Shift

From function-centric to object-centric design.

---

## Comparison Table

$$

\begin{array}{lcc}
\textbf{Feature} & \textbf{Procedural} & \textbf{OOP} \\
\hline
\text{Primary Abstraction} & \text{Function} & \text{Class/Object} \\
\text{Data Encapsulation} & \text{No} & \text{Yes} \\
\text{Modularity} & \text{Function-centric} & \text{Class-centric} \\
\text{Code Reuse} & \text{Limited} & \text{Inheritance} \\
\text{State Management} & \text{External} & \text{Internal} \\
\end{array}

$$

---

## State Management

### 1. Procedural State

```python
# State is external to functions
speed = 200
color = "red"

def speed_up(speed):
    return speed + 10

def print_car(speed, color):
    print(f"Speed: {speed}, Color: {color}")

speed = speed_up(speed)
print_car(speed, color)
```

### 2. OOP State

```python
# State is internal to objects
class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
    
    def speed_up(self):
        self.speed += 10
    
    def print_all(self):
        print(f"Speed: {self.speed}, Color: {self.color}")

ford = Car(200, "red")
ford.speed_up()
ford.print_all()
```

### 3. State Cohesion

OOP keeps related data and operations together.

---

## Code Organization

### 1. Procedural Organization

```python
# Functions scattered
def create_student(name, major):
    return {"name": name, "major": major}

def add_course(student, course):
    if "courses" not in student:
        student["courses"] = []
    student["courses"].append(course)

def drop_course(student, course):
    if "courses" in student:
        student["courses"].remove(course)
```

### 2. OOP Organization

```python
# Everything bundled in class
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.courses = []
    
    def add_course(self, course):
        self.courses.append(course)
    
    def drop_course(self, course):
        self.courses.remove(course)
```

### 3. Logical Grouping

Classes provide natural organization boundaries.

---

## When to Use Each

### 1. Use Procedural

- Simple scripts and utilities
- Mathematical computations
- Data transformations
- Quick prototypes

### 2. Use OOP

- Complex systems
- Multiple related entities
- Need for inheritance
- Long-term maintenance

### 3. Hybrid Approach

Modern Python often mixes both paradigms.

---

## Code Reuse

### 1. Procedural Reuse

```python
# Limited to function calls
def process_data(data):
    return sorted(data)

result1 = process_data(data1)
result2 = process_data(data2)
```

### 2. OOP Reuse

```python
# Inheritance and composition
class BaseProcessor:
    def process(self, data):
        return sorted(data)

class CustomProcessor(BaseProcessor):
    def process(self, data):
        data = super().process(data)
        return [x * 2 for x in data]
```

### 3. Extensibility

OOP provides more mechanisms for extension.

---

## Key Takeaways

- Procedural: functions operating on data.
- OOP: objects encapsulating data and behavior.
- OOP provides better encapsulation and reuse.
- Choose based on problem complexity.
- Modern code often uses both paradigms.
