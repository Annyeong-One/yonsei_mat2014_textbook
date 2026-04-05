# IntEnum and StrEnum

IntEnum and StrEnum are specialized enum types that behave like their base types, enabling easier comparisons and operations.

---

## IntEnum

```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

# IntEnum members are integers
priority = Priority.HIGH
print(priority)           # Priority.HIGH
print(priority.value)     # 3

# Can compare with integers
print(priority > 2)       # True
print(priority == 3)      # True

# Can use in arithmetic
result = priority + 1
print(result)             # 4 (integer, not enum member)

# Can use in array indexing
levels = ['none', 'low', 'medium', 'high', 'critical']
print(levels[Priority.HIGH])  # 'high'
```

## IntEnum Comparison

```python
from enum import IntEnum

class HttpStatus(IntEnum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    SERVER_ERROR = 500

def handle_response(status: int):
    if status < 400:
        print("Success")
    elif status < 500:
        print("Client error")
    else:
        print("Server error")

# Works with numeric values directly
handle_response(HttpStatus.OK)
handle_response(200)  # Same result

# Sorting
statuses = [
    HttpStatus.SERVER_ERROR,
    HttpStatus.OK,
    HttpStatus.NOT_FOUND
]
sorted_statuses = sorted(statuses)
print([s.value for s in sorted_statuses])  # [200, 404, 500]
```

## StrEnum (Python 3.11+)

```python
from enum import StrEnum

class Color(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

# StrEnum members are strings
color = Color.RED
print(color)           # Color.RED
print(color.value)     # 'red'

# Can compare with strings
print(color == "red")  # True
print(color.upper())   # 'RED' (string method)

# Can use in string operations
message = f"Color: {color}"
print(message)         # 'Color: Color.RED'

# String methods work
print(color.startswith('r'))  # True
```

## IntEnum Practical Example

```python
from enum import IntEnum

class ServerState(IntEnum):
    STOPPED = 0
    STARTING = 1
    RUNNING = 2
    STOPPING = 3

def is_operational(state: int) -> bool:
    return state == ServerState.RUNNING

def is_transitioning(state: int) -> bool:
    return state in (ServerState.STARTING, ServerState.STOPPING)

state = ServerState.RUNNING
print(f"Operational: {is_operational(state)}")      # True
print(f"Transitioning: {is_transitioning(state)}")  # False

# Works with raw integers too
print(f"Operational: {is_operational(2)}")          # True
```

## StrEnum Practical Example

```python
from enum import StrEnum

class ContentType(StrEnum):
    JSON = "application/json"
    XML = "application/xml"
    FORM = "application/x-www-form-urlencoded"
    TEXT = "text/plain"

def get_content_type_header(ct: ContentType) -> str:
    return f"Content-Type: {ct}"

# Can use in HTTP headers directly
print(get_content_type_header(ContentType.JSON))

# Can compare with strings
header_value = "application/json"
if header_value == ContentType.JSON:
    print("JSON content detected")
```

## Compatibility

```python
from enum import IntEnum, Enum

class Number(IntEnum):
    ONE = 1
    TWO = 2

class Letter(Enum):
    A = "A"
    B = "B"

# IntEnum works with numeric comparisons
print(Number.TWO > Number.ONE)          # True

# Regular Enum doesn't (TypeError)
try:
    print(Letter.B > Letter.A)
except TypeError as e:
    print(f"Cannot compare: {e}")
```

## When to Use

**IntEnum:**
- Numeric codes (HTTP status, error codes)
- Need comparison with numbers
- Using as array indices

**StrEnum (3.11+):**
- String representations (color names, content types)
- Need string operations
- Serialization to strings

**Regular Enum:**
- Arbitrary values
- No numeric/string compatibility needed
- Mixed value types

---

## Exercises

**Exercise 1.**
Create an `IntEnum` called `Grade` with `A = 4`, `B = 3`, `C = 2`, `D = 1`, `F = 0`. Write a function `calculate_gpa(grades)` that takes a list of `Grade` members and returns the average as a float. Demonstrate that `Grade` values can be used directly in arithmetic.

??? success "Solution to Exercise 1"

        from enum import IntEnum

        class Grade(IntEnum):
            A = 4
            B = 3
            C = 2
            D = 1
            F = 0

        def calculate_gpa(grades):
            return sum(grades) / len(grades)

        grades = [Grade.A, Grade.B, Grade.A, Grade.C, Grade.B]
        gpa = calculate_gpa(grades)
        print(f"GPA: {gpa:.2f}")  # GPA: 3.20

        # IntEnum works in arithmetic
        print(Grade.A + Grade.B)    # 7
        print(Grade.A > Grade.C)    # True

---

**Exercise 2.**
Define a `StrEnum` called `Color` with lowercase values. Show that `Color` members can be compared directly with strings (`Color.RED == "red"`), used in string operations (`.upper()`, `.startswith()`), and used as dictionary keys interchangeably with strings.

??? success "Solution to Exercise 2"

        from enum import StrEnum

        class Color(StrEnum):
            RED = "red"
            GREEN = "green"
            BLUE = "blue"

        # Compare with strings
        print(Color.RED == "red")        # True

        # String operations
        print(Color.RED.upper())         # RED
        print(Color.GREEN.startswith("gr"))  # True

        # Use as dictionary keys
        prices = {Color.RED: 10, "green": 20}
        print(prices[Color.RED])     # 10
        print(prices[Color.GREEN])   # 20

---

**Exercise 3.**
Create an `IntEnum` called `HTTPStatus` with common codes (200, 201, 400, 404, 500). Write a function `categorize(status)` that uses integer comparison (`< 300`, `< 400`, `< 500`) to return "success", "redirect", "client error", or "server error". Show that the function works with both `HTTPStatus` members and plain integers.

??? success "Solution to Exercise 3"

        from enum import IntEnum

        class HTTPStatus(IntEnum):
            OK = 200
            CREATED = 201
            BAD_REQUEST = 400
            NOT_FOUND = 404
            SERVER_ERROR = 500

        def categorize(status):
            if status < 300:
                return "success"
            elif status < 400:
                return "redirect"
            elif status < 500:
                return "client error"
            else:
                return "server error"

        print(categorize(HTTPStatus.OK))          # success
        print(categorize(HTTPStatus.NOT_FOUND))   # client error
        print(categorize(HTTPStatus.SERVER_ERROR)) # server error
        print(categorize(301))                     # redirect (plain int works)
