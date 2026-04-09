# Enum Basics

Enums represent a fixed set of values, providing type safety and code clarity. They're useful for representing distinct states or choices.

---

## Creating Basic Enums

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    XLARGE = "XL"

# Access members
print(Color.RED)          # Color.RED
print(Color.RED.name)     # 'RED'
print(Color.RED.value)    # 1

print(Size.MEDIUM)        # Size.MEDIUM
print(Size.MEDIUM.value)  # 'M'
```

## Enum Iteration

```python
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

# Iterate over all members
for status in Status:
    print(f"{status.name}: {status.value}")

# Get all values
values = [s.value for s in Status]
print(values)  # ['pending', 'running', 'completed', 'failed']

# Get all names
names = [s.name for s in Status]
print(names)   # ['PENDING', 'RUNNING', 'COMPLETED', 'FAILED']
```

## Accessing Enum Members

```python
from enum import Enum

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

# By name
priority1 = Priority['HIGH']        # Priority.HIGH
priority2 = Priority.HIGH           # Priority.HIGH

# By value
priority3 = Priority(3)             # Priority.HIGH

# Comparison
print(Priority.HIGH == Priority.HIGH)      # True
print(Priority.HIGH == Priority.MEDIUM)    # False
print(Priority.HIGH.value == 3)            # True
```

## Type Checking with Enums

```python
from enum import Enum
from typing import Union

class Environment(Enum):
    DEVELOPMENT = "dev"
    STAGING = "staging"
    PRODUCTION = "prod"

def deploy(env: Environment):
    if env == Environment.PRODUCTION:
        print("⚠️ Deploying to PRODUCTION")
    elif env == Environment.STAGING:
        print("Deploying to staging")
    else:
        print("Deploying to development")

deploy(Environment.PRODUCTION)
# deploy("production")  # Type error - caught by linters
```

## Enum Membership Testing

```python
from enum import Enum

class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"

def handle_request(method: str):
    try:
        http_method = HTTPMethod[method.upper()]
        print(f"Handling {http_method.value} request")
    except KeyError:
        print(f"Unknown HTTP method: {method}")

handle_request("GET")      # Works
handle_request("TRACE")    # Unknown HTTP method: TRACE
```

## Enum Comparison and Ordering

```python
from enum import Enum

class Grade(Enum):
    F = 1
    D = 2
    C = 3
    B = 4
    A = 5

grade1 = Grade.A
grade2 = Grade.C

print(grade1 == Grade.A)        # True
print(grade1 != grade2)         # True
# Can't use <, >, <=, >= on regular Enums
```

## Best Practices

- Use Enums for fixed sets of values
- Provide descriptive names (not `E1`, `E2`, etc.)
- Keep enum definitions at module level
- Use type hints with Enum types
- Document what each member represents

---

## Exercises

**Exercise 1.**
Create a `Season` enum with members `SPRING`, `SUMMER`, `AUTUMN`, `WINTER` and string values (`"spring"`, etc.). Write a function `describe_season(season: Season)` that returns a description. Iterate over all seasons and print name, value, and description.

??? success "Solution to Exercise 1"

        from enum import Enum

        class Season(Enum):
            SPRING = "spring"
            SUMMER = "summer"
            AUTUMN = "autumn"
            WINTER = "winter"

        def describe_season(season: Season):
            descriptions = {
                Season.SPRING: "Flowers bloom",
                Season.SUMMER: "Hot and sunny",
                Season.AUTUMN: "Leaves fall",
                Season.WINTER: "Cold and snowy",
            }
            return descriptions[season]

        for s in Season:
            print(f"{s.name} ({s.value}): {describe_season(s)}")

---

**Exercise 2.**
Define a `HTTPMethod` enum with members `GET`, `POST`, `PUT`, `DELETE`. Write a function that accepts a string (like `"get"`) and returns the corresponding enum member using bracket notation (`HTTPMethod[...]`). Handle invalid input with a try/except that catches `KeyError`.

??? success "Solution to Exercise 2"

        from enum import Enum

        class HTTPMethod(Enum):
            GET = "GET"
            POST = "POST"
            PUT = "PUT"
            DELETE = "DELETE"

        def parse_method(method_str):
            try:
                return HTTPMethod[method_str.upper()]
            except KeyError:
                print(f"Unknown method: {method_str}")
                return None

        print(parse_method("get"))     # HTTPMethod.GET
        print(parse_method("post"))    # HTTPMethod.POST
        print(parse_method("PATCH"))   # Unknown method: PATCH -> None

---

**Exercise 3.**
Create a `Priority` enum with members `LOW = 1`, `MEDIUM = 2`, `HIGH = 3`, `CRITICAL = 4`. Write a function `filter_by_priority(tasks, min_priority)` where each task is a tuple of `(name, Priority)`. It should return only tasks with priority >= `min_priority` by comparing `.value`. Demonstrate with a list of tasks.

??? success "Solution to Exercise 3"

        from enum import Enum

        class Priority(Enum):
            LOW = 1
            MEDIUM = 2
            HIGH = 3
            CRITICAL = 4

        def filter_by_priority(tasks, min_priority):
            return [(name, p) for name, p in tasks if p.value >= min_priority.value]

        tasks = [
            ("Fix typo", Priority.LOW),
            ("Update docs", Priority.MEDIUM),
            ("Security patch", Priority.CRITICAL),
            ("New feature", Priority.HIGH),
        ]

        urgent = filter_by_priority(tasks, Priority.HIGH)
        for name, p in urgent:
            print(f"[{p.name}] {name}")
        # [CRITICAL] Security patch
        # [HIGH] New feature
