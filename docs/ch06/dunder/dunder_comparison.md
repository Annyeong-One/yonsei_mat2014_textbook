# Comparison Operators

Comparison dunder methods enable custom comparison logic and sorting for your objects.

## Basic Comparison Methods

### Equality: `__eq__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)  # True
print(p1 == p3)  # False
print(p1 == "not a point")  # False (NotImplemented → False)
```

### All Comparison Methods

| Method | Operator | Example |
|--------|----------|---------|
| `__eq__` | `==` | `a == b` |
| `__ne__` | `!=` | `a != b` |
| `__lt__` | `<` | `a < b` |
| `__le__` | `<=` | `a <= b` |
| `__gt__` | `>` | `a > b` |
| `__ge__` | `>=` | `a >= b` |

### Complete Implementation

```python
class Version:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch
    
    def _to_tuple(self):
        return (self.major, self.minor, self.patch)
    
    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._to_tuple() == other._to_tuple()
    
    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result
    
    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._to_tuple() < other._to_tuple()
    
    def __le__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._to_tuple() <= other._to_tuple()
    
    def __gt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._to_tuple() > other._to_tuple()
    
    def __ge__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._to_tuple() >= other._to_tuple()
    
    def __repr__(self):
        return f"Version({self.major}, {self.minor}, {self.patch})"

v1 = Version(1, 0, 0)
v2 = Version(2, 0, 0)
v3 = Version(1, 5, 0)

print(v1 < v2)   # True
print(v1 < v3)   # True
print(v2 > v3)   # True
print(sorted([v2, v1, v3]))  # [Version(1, 0, 0), Version(1, 5, 0), Version(2, 0, 0)]
```

## Using @total_ordering

The `functools.total_ordering` decorator reduces boilerplate by deriving missing comparison methods from `__eq__` and one ordering method.

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade == other.grade
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade < other.grade
    
    def __repr__(self):
        return f"Student({self.name!r}, {self.grade})"

# All comparisons work!
alice = Student("Alice", 90)
bob = Student("Bob", 85)
charlie = Student("Charlie", 90)

print(alice > bob)    # True  (derived from __lt__)
print(alice >= bob)   # True  (derived from __lt__ and __eq__)
print(alice <= bob)   # False (derived from __lt__ and __eq__)
print(alice == charlie)  # True
print(alice != bob)   # True  (derived from __eq__)
```

### How @total_ordering Works

You provide `__eq__` + one of (`__lt__`, `__le__`, `__gt__`, `__ge__`), and it derives the rest:

| You Implement | Decorator Derives |
|---------------|-------------------|
| `__eq__` + `__lt__` | `__le__`, `__gt__`, `__ge__` |
| `__eq__` + `__le__` | `__lt__`, `__gt__`, `__ge__` |
| `__eq__` + `__gt__` | `__lt__`, `__le__`, `__ge__` |
| `__eq__` + `__ge__` | `__lt__`, `__le__`, `__gt__` |

### Performance Note

```python
# @total_ordering has slight performance overhead
# For performance-critical code, implement all methods manually

# Or use __slots__ with manual implementation
class FastPoint:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    
    def __le__(self, other):
        return (self.x, self.y) <= (other.x, other.y)
    
    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)
    
    def __ge__(self, other):
        return (self.x, self.y) >= (other.x, other.y)
```

## Hashing and Equality

Objects that compare equal should have equal hashes. If you define `__eq__`, you should also define `__hash__`.

```python
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def __eq__(self, other):
        if not isinstance(other, Color):
            return NotImplemented
        return (self.r, self.g, self.b) == (other.r, other.g, other.b)
    
    def __hash__(self):
        return hash((self.r, self.g, self.b))
    
    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b})"

# Now Color can be used in sets and as dict keys
red = Color(255, 0, 0)
also_red = Color(255, 0, 0)

colors = {red, also_red}
print(len(colors))  # 1 (same hash and equal)

color_names = {red: "red", Color(0, 255, 0): "green"}
print(color_names[also_red])  # "red"
```

### Hash Rules

```python
# Rule 1: Equal objects must have equal hashes
a == b  →  hash(a) == hash(b)

# Rule 2: Unequal objects CAN have equal hashes (collisions are OK)
hash(a) == hash(b)  ↛  a == b

# Rule 3: Mutable objects should not be hashable
# (their hash could change, breaking dict/set invariants)
```

### Making Objects Unhashable

```python
class MutablePoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if not isinstance(other, MutablePoint):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    # Explicitly make unhashable
    __hash__ = None

p = MutablePoint(1, 2)
# hash(p)  # TypeError: unhashable type: 'MutablePoint'
# {p}      # TypeError: unhashable type: 'MutablePoint'
```

## Identity vs Equality

```python
class Box:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        return self.value == other.value

a = Box(42)
b = Box(42)
c = a

# Equality (==) uses __eq__
print(a == b)  # True (same value)
print(a == c)  # True (same value)

# Identity (is) compares memory addresses
print(a is b)  # False (different objects)
print(a is c)  # True (same object)
```

## Comparing with None

```python
class OptionalValue:
    def __init__(self, value=None):
        self.value = value
    
    def __eq__(self, other):
        # Handle None comparison
        if other is None:
            return self.value is None
        if not isinstance(other, OptionalValue):
            return NotImplemented
        return self.value == other.value

empty = OptionalValue()
filled = OptionalValue(42)

print(empty == None)   # True
print(filled == None)  # False
```

## Comparison with Different Types

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def __eq__(self, other):
        if isinstance(other, Temperature):
            return self.celsius == other.celsius
        if isinstance(other, (int, float)):
            return self.celsius == other
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Temperature):
            return self.celsius < other.celsius
        if isinstance(other, (int, float)):
            return self.celsius < other
        return NotImplemented

t = Temperature(20)
print(t == 20)              # True
print(t == Temperature(20)) # True
print(t < 25)               # True
print(t > Temperature(15))  # True
```

## Chained Comparisons

Python's chained comparisons (like `a < b < c`) work automatically:

```python
from functools import total_ordering

@total_ordering
class Score:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value
    
    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value

low = Score(10)
mid = Score(50)
high = Score(90)

# Chained comparison
print(low < mid < high)  # True
# Equivalent to: low < mid and mid < high
```

## Practical Example: Priority Queue Item

```python
from functools import total_ordering

@total_ordering
class PriorityItem:
    """Item for priority queue with (priority, data) comparison."""
    
    _counter = 0  # Tie-breaker for equal priorities
    
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
        PriorityItem._counter += 1
        self._order = PriorityItem._counter
    
    def __eq__(self, other):
        if not isinstance(other, PriorityItem):
            return NotImplemented
        return (self.priority, self._order) == (other.priority, other._order)
    
    def __lt__(self, other):
        if not isinstance(other, PriorityItem):
            return NotImplemented
        # Lower priority number = higher priority
        # Earlier insertion = higher priority (for ties)
        return (self.priority, self._order) < (other.priority, other._order)
    
    def __repr__(self):
        return f"PriorityItem({self.priority}, {self.data!r})"

import heapq

tasks = []
heapq.heappush(tasks, PriorityItem(2, "low priority"))
heapq.heappush(tasks, PriorityItem(1, "high priority"))
heapq.heappush(tasks, PriorityItem(1, "also high priority"))

while tasks:
    item = heapq.heappop(tasks)
    print(item)

# Output:
# PriorityItem(1, 'high priority')
# PriorityItem(1, 'also high priority')
# PriorityItem(2, 'low priority')
```

## Sorting Custom Objects

```python
from functools import total_ordering

@total_ordering
class Employee:
    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years
    
    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return (self.salary, self.years) == (other.salary, other.years)
    
    def __lt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        # Sort by salary (desc), then years (desc)
        return (-self.salary, -self.years) < (-other.salary, -other.years)
    
    def __repr__(self):
        return f"Employee({self.name!r}, ${self.salary}, {self.years}y)"

employees = [
    Employee("Alice", 75000, 5),
    Employee("Bob", 80000, 3),
    Employee("Charlie", 75000, 8),
]

# Using default sort (uses __lt__)
for emp in sorted(employees):
    print(emp)

# Output:
# Employee('Bob', \$80000, 3y)
# Employee('Charlie', \$75000, 8y)
# Employee('Alice', \$75000, 5y)
```

## Key Takeaways

- Implement `__eq__` for equality; Python provides `__ne__` automatically
- Use `@total_ordering` to avoid boilerplate—just implement `__eq__` and one of `__lt__`, `__le__`, `__gt__`, `__ge__`
- Return `NotImplemented` (not `False`) for unsupported types
- If you define `__eq__`, also define `__hash__` for hashable objects
- Set `__hash__ = None` for mutable objects that shouldn't be hashable
- Tuple comparison is a clean way to implement multi-field comparisons
- Identity (`is`) and equality (`==`) are different concepts
