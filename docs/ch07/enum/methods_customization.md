# Enum Methods and Customization

Add methods to enums and customize their behavior to create powerful, expressive types.

---

## Adding Methods to Enums

```python
from enum import Enum

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    XLARGE = 4
    
    def get_next_size(self):
        '''Get the next larger size'''
        members = list(Size)
        idx = members.index(self)
        if idx < len(members) - 1:
            return members[idx + 1]
        return self
    
    def get_price_multiplier(self):
        '''Get price multiplier for this size'''
        multipliers = {
            Size.SMALL: 1.0,
            Size.MEDIUM: 1.25,
            Size.LARGE: 1.5,
            Size.XLARGE: 1.75
        }
        return multipliers[self]

small = Size.SMALL
print(small.get_next_size())        # Size.MEDIUM
print(small.get_price_multiplier()) # 1.0
```

## Properties in Enums

```python
from enum import Enum
from functools import cached_property

class UserRole(Enum):
    GUEST = "guest"
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"
    
    @property
    def can_delete_posts(self):
        '''Check if role can delete posts'''
        return self in (UserRole.MODERATOR, UserRole.ADMIN)
    
    @property
    def can_ban_users(self):
        '''Check if role can ban users'''
        return self == UserRole.ADMIN
    
    @property
    def display_name(self):
        '''Human-readable role name'''
        return self.value.capitalize()

role = UserRole.MODERATOR
print(f"Role: {role.display_name}")          # Role: Moderator
print(f"Can delete posts: {role.can_delete_posts}")  # True
print(f"Can ban users: {role.can_ban_users}")        # False
```

## Class Methods in Enums

```python
from enum import Enum

class Environment(Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    
    @classmethod
    def from_string(cls, value: str):
        '''Create from string, case-insensitive'''
        for member in cls:
            if member.value.lower() == value.lower():
                return member
        raise ValueError(f"Unknown environment: {value}")
    
    @classmethod
    def is_production(cls, env):
        '''Check if environment is production'''
        return env == cls.PRODUCTION

env = Environment.from_string("PRODUCTION")
print(env)                                  # Environment.PRODUCTION
print(Environment.is_production(env))       # True
```

## Custom Enum with __str__

```python
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    
    def __str__(self):
        '''Custom string representation'''
        symbols = {
            Status.PENDING: "⏳",
            Status.RUNNING: "▶️",
            Status.COMPLETED: "✅",
            Status.FAILED: "❌"
        }
        return f"{symbols[self]} {self.value}"

status = Status.RUNNING
print(status)           # ▶️ running
print(str(status))      # ▶️ running
```

## Enum with __repr__

```python
from enum import Enum

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4
    
    def __repr__(self):
        '''Detailed representation'''
        return f"<Priority: {self.name} (level {self.value})>"

priority = Priority.HIGH
print(repr(priority))   # <Priority: HIGH (level 3)>
```

## Computed Enum Values

```python
from enum import Enum
from datetime import datetime

class LogLevel(Enum):
    DEBUG = (1, "DEBUG", "🔍")
    INFO = (2, "INFO", "ℹ️")
    WARNING = (3, "WARNING", "⚠️")
    ERROR = (4, "ERROR", "❌")
    CRITICAL = (5, "CRITICAL", "🔴")
    
    def __init__(self, level, name_str, symbol):
        self.level = level
        self.name_str = name_str
        self.symbol = symbol
    
    def format_message(self, message: str) -> str:
        '''Format log message'''
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] {self.symbol} {self.name_str}: {message}"

log = LogLevel.ERROR
print(log.format_message("Database connection failed"))
```

## Customizing Lookup

```python
from enum import Enum

class ErrorCode(Enum):
    NOT_FOUND = 404
    FORBIDDEN = 403
    SERVER_ERROR = 500
    
    def __init__(self, code):
        self.code = code
    
    @classmethod
    def from_http_status(cls, status_code: int):
        '''Look up by HTTP status code'''
        for member in cls:
            if member.code == status_code:
                return member
        raise ValueError(f"No enum for status code: {status_code}")
    
    def get_message(self) -> str:
        '''Get friendly error message'''
        messages = {
            404: "Resource not found",
            403: "Access forbidden",
            500: "Internal server error"
        }
        return messages.get(self.code, "Unknown error")

error = ErrorCode.from_http_status(404)
print(f"{error.code}: {error.get_message()}")  # 404: Resource not found
```

## When to Add Methods

- Validation logic
- Conversion operations
- Related computations
- Display formatting
- Lookup functionality

---

## Exercises

**Exercise 1.**
Create a `Season` enum with a method `is_warm()` that returns `True` for `SUMMER` and `SPRING`. Add a `__str__` override that returns a formatted string like `"Season: Spring"`. Iterate over all seasons and print which are warm.

??? success "Solution to Exercise 1"

        from enum import Enum

        class Season(Enum):
            SPRING = 1
            SUMMER = 2
            AUTUMN = 3
            WINTER = 4

            def is_warm(self):
                return self in (Season.SPRING, Season.SUMMER)

            def __str__(self):
                return f"Season: {self.name.capitalize()}"

        for s in Season:
            warm = "warm" if s.is_warm() else "cold"
            print(f"{s} ({warm})")

---

**Exercise 2.**
Define a `Coin` enum with `PENNY = 1`, `NICKEL = 5`, `DIME = 10`, `QUARTER = 25`. Add a `dollar_value` property that returns the value in dollars (e.g., `0.25` for QUARTER). Add a class method `total(coins)` that returns the total dollar value of a list of coins.

??? success "Solution to Exercise 2"

        from enum import Enum

        class Coin(Enum):
            PENNY = 1
            NICKEL = 5
            DIME = 10
            QUARTER = 25

            @property
            def dollar_value(self):
                return self.value / 100

            @classmethod
            def total(cls, coins):
                return sum(c.dollar_value for c in coins)

        coins = [Coin.QUARTER, Coin.DIME, Coin.NICKEL, Coin.PENNY]
        print(f"Total: ${Coin.total(coins):.2f}")  # Total: $0.41

---

**Exercise 3.**
Create a `Direction` enum with a `opposite` property that returns the opposite direction (NORTH returns SOUTH, etc.). Also add a `rotate(steps)` method that rotates clockwise by the given number of 90-degree steps. Demonstrate both features.

??? success "Solution to Exercise 3"

        from enum import Enum

        class Direction(Enum):
            NORTH = 0
            EAST = 1
            SOUTH = 2
            WEST = 3

            @property
            def opposite(self):
                return Direction((self.value + 2) % 4)

            def rotate(self, steps=1):
                return Direction((self.value + steps) % 4)

        print(Direction.NORTH.opposite)    # Direction.SOUTH
        print(Direction.EAST.opposite)     # Direction.WEST
        print(Direction.NORTH.rotate(1))   # Direction.EAST
        print(Direction.NORTH.rotate(3))   # Direction.WEST
