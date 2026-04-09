# auto() Function

The `auto()` function automatically assigns values to enum members, eliminating tedious manual assignment.

---

## Basic auto() Usage

```python
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(Color.RED)        # Color.RED
print(Color.RED.value)  # 1
print(Color.GREEN.value)  # 2
print(Color.BLUE.value)   # 3

# Values are auto-incremented starting from 1
for color in Color:
    print(f"{color.name} = {color.value}")
```

## auto() with Flag

```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()      # 1
    WRITE = auto()     # 2
    EXECUTE = auto()   # 4

# Flag auto() uses powers of 2
for perm in Permission:
    print(f"{perm.name} = {perm.value}")

# Allows bitwise operations
user_perms = Permission.READ | Permission.WRITE
print(user_perms)  # Permission.READ|WRITE
```

## Customizing auto() Behavior

```python
from enum import Enum, auto

class Priority(Enum):
    def _generate_next_value_(name, start, count, last_values):
        # Custom logic for auto values
        # name: member name
        # start: starting value
        # count: number of members so far
        # last_values: list of previous values
        return name.lower()
    
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

print(Priority.LOW.value)        # 'low'
print(Priority.CRITICAL.value)   # 'critical'
```

## auto() with Strings

```python
from enum import Enum, auto

class HttpMethod(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.upper()
    
    GET = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()
    PATCH = auto()

print(HttpMethod.GET.value)     # 'GET'
print(HttpMethod.DELETE.value)  # 'DELETE'
```

## Mixing auto() and Manual Values

```python
from enum import Enum, auto

class Status(Enum):
    PENDING = auto()      # 1
    APPROVED = auto()     # 2
    CUSTOM = "special"    # manual value
    REJECTED = auto()     # 3
    ARCHIVED = auto()     # 4

for status in Status:
    print(f"{status.name}: {status.value}")
```

## auto() with IntEnum

```python
from enum import IntEnum, auto

class HttpStatus(IntEnum):
    # Custom auto for specific patterns
    def _generate_next_value_(name, start, count, last_values):
        if count == 0:
            return 100
        elif count < 3:
            return 100 + (count - 1) * 10 + 1
        elif count < 6:
            return 200 + (count - 3) * 100
        else:
            return 400 + (count - 6) * 50
    
    CONTINUE = auto()          # 100
    SWITCHING = auto()         # 101
    PROCESSING = auto()        # 102
    OK = auto()                # 200
    CREATED = auto()           # 300
    BAD_REQUEST = auto()       # 400

print(HttpStatus.CONTINUE.value)     # 100
print(HttpStatus.OK.value)           # 200
print(HttpStatus.BAD_REQUEST.value)  # 400
```

## auto() for String Slugs

```python
from enum import Enum, auto

class ContentType(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower().replace('_', '-')
    
    PLAIN_TEXT = auto()
    RICH_TEXT = auto()
    HTML_PAGE = auto()
    JSON_DATA = auto()

print(ContentType.PLAIN_TEXT.value)   # 'plain-text'
print(ContentType.HTML_PAGE.value)    # 'html-page'
print(ContentType.JSON_DATA.value)    # 'json-data'
```

## When to Use auto()

- Ordering matters but exact value doesn't
- Avoiding manual typos in value assignment
- Natural progression (1, 2, 3, ...)
- Combined with custom `_generate_next_value_` for domain-specific values

---

## Exercises

**Exercise 1.**
Create a `Direction` enum using `auto()` for values. Then create a `LogLevel` enum that uses a custom `_generate_next_value_` to set values as the lowercase member name (e.g., `DEBUG` gets value `"debug"`). Print all members and their values for both enums.

??? success "Solution to Exercise 1"

        from enum import Enum, auto

        class Direction(Enum):
            NORTH = auto()
            SOUTH = auto()
            EAST = auto()
            WEST = auto()

        for d in Direction:
            print(f"{d.name} = {d.value}")
        # NORTH = 1, SOUTH = 2, EAST = 3, WEST = 4

        class LogLevel(Enum):
            def _generate_next_value_(name, start, count, last_values):
                return name.lower()

            DEBUG = auto()
            INFO = auto()
            WARNING = auto()
            ERROR = auto()

        for level in LogLevel:
            print(f"{level.name} = {level.value!r}")
        # DEBUG = 'debug', INFO = 'info', etc.

---

**Exercise 2.**
Define a `Permission` Flag enum using `auto()`. Members should be `READ`, `WRITE`, `EXECUTE`, and `ADMIN`. Demonstrate combining permissions with `|`, checking with `in`, and removing a permission with `& ~`. Show that `auto()` assigns powers of 2 for Flag.

??? success "Solution to Exercise 2"

        from enum import Flag, auto

        class Permission(Flag):
            READ = auto()      # 1
            WRITE = auto()     # 2
            EXECUTE = auto()   # 4
            ADMIN = auto()     # 8

        # Combine
        user_perms = Permission.READ | Permission.WRITE
        print(user_perms)  # Permission.READ|WRITE

        # Check
        print(Permission.READ in user_perms)     # True
        print(Permission.ADMIN in user_perms)    # False

        # Remove
        user_perms = user_perms & ~Permission.WRITE
        print(user_perms)  # Permission.READ

---

**Exercise 3.**
Create a `APIEndpoint` enum with a custom `_generate_next_value_` that converts member names to URL-style slugs (e.g., `USER_PROFILE` becomes `"/user-profile"`). Add members `HOME`, `USER_PROFILE`, `SETTINGS_PAGE`, and `API_DOCS`. Print each member's value to verify the slug conversion.

??? success "Solution to Exercise 3"

        from enum import Enum, auto

        class APIEndpoint(Enum):
            def _generate_next_value_(name, start, count, last_values):
                return "/" + name.lower().replace("_", "-")

            HOME = auto()
            USER_PROFILE = auto()
            SETTINGS_PAGE = auto()
            API_DOCS = auto()

        for endpoint in APIEndpoint:
            print(f"{endpoint.name}: {endpoint.value}")
        # HOME: /home
        # USER_PROFILE: /user-profile
        # SETTINGS_PAGE: /settings-page
        # API_DOCS: /api-docs
