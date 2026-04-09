# Enum Members and Values

Access and manipulate enum members and their values. Understand the differences between names, values, and member objects.

---

## Accessing Names and Values

```python
from enum import Enum

class Fruit(Enum):
    APPLE = "apple"
    BANANA = "banana"
    ORANGE = "orange"

# Get member object
apple = Fruit.APPLE
print(apple)              # Fruit.APPLE
print(type(apple))        # <enum 'Fruit'>

# Access name and value separately
print(apple.name)         # 'APPLE'
print(apple.value)        # 'apple'

# Both directions
print(Fruit['APPLE'])     # Fruit.APPLE
print(Fruit('apple'))     # Fruit.APPLE
```

## Listing All Members

```python
from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Access _member_names_ (tuple)
print(Day._member_names_)  # ('MONDAY', 'TUESDAY', ...)

# Access _member_map_ (dict name -> member)
print(Day._member_map_['FRIDAY'])  # Day.FRIDAY

# Access _value2member_map_ (dict value -> member)
print(Day._value2member_map_[5])   # Day.FRIDAY

# Iterate
for day in Day:
    print(f"{day.name}: {day.value}")
```

## Creating Enums with Complex Values

```python
from enum import Enum
from dataclasses import dataclass

@dataclass
class Config:
    code: str
    description: str

class ErrorType(Enum):
    NOT_FOUND = Config("404", "Resource not found")
    FORBIDDEN = Config("403", "Access denied")
    SERVER_ERROR = Config("500", "Internal server error")

error = ErrorType.NOT_FOUND
print(f"{error.value.code}: {error.value.description}")
# Output: 404: Resource not found
```

## Alias Members

```python
from enum import Enum

class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2
    PENDING = 3
    # Aliases - multiple names for same value
    WAITING = 3
    ON_HOLD = 3

# Aliases are hidden in iteration
for status in Status:
    print(status)
# Output: Status.ACTIVE, Status.INACTIVE, Status.PENDING

# Access by alias
print(Status.WAITING)           # Status.PENDING (canonical member)
print(Status.WAITING.name)      # 'PENDING'
print(Status.WAITING == Status.PENDING)  # True

# Canonical and aliases have same object
print(Status.PENDING is Status.WAITING)  # True
```

## Conditional Access

```python
from enum import Enum

class PaymentMethod(Enum):
    CREDIT_CARD = "cc"
    DEBIT_CARD = "dc"
    BANK_TRANSFER = "bt"
    PAYPAL = "pp"
    CRYPTOCURRENCY = "crypto"

def get_fee_percentage(method: PaymentMethod) -> float:
    fee_map = {
        PaymentMethod.CREDIT_CARD: 2.9,
        PaymentMethod.DEBIT_CARD: 0.5,
        PaymentMethod.BANK_TRANSFER: 0.0,
        PaymentMethod.PAYPAL: 3.49,
        PaymentMethod.CRYPTOCURRENCY: 1.0
    }
    return fee_map.get(method, 0)

fee = get_fee_percentage(PaymentMethod.CREDIT_CARD)
print(f"Fee: {fee}%")
```

## Serialization

```python
from enum import Enum
import json

class Color(Enum):
    RED = "#FF0000"
    GREEN = "#00FF00"
    BLUE = "#0000FF"

# Serialize by value
color = Color.RED
json_str = json.dumps({'color': color.value})
print(json_str)  # {'color': '#FF0000'}

# Deserialize back
data = json.loads(json_str)
restored_color = Color(data['color'])
print(restored_color)  # Color.RED
```

## Safe Member Access

```python
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"

def safe_get_status(value: str) -> Status:
    try:
        return Status(value)
    except ValueError:
        return Status.PENDING  # Default

status = safe_get_status("unknown")
print(status)  # Status.PENDING
```

---

## Exercises

**Exercise 1.**
Create a `Planet` enum with members and tuple values containing `(mass, radius)`. Access a planet's mass and radius via `planet.value[0]` and `planet.value[1]`. Write a function `heaviest(planets)` that returns the planet with the greatest mass from a list of `Planet` members.

??? success "Solution to Exercise 1"

        from enum import Enum

        class Planet(Enum):
            MERCURY = (3.303e+23, 2.4397e6)
            VENUS = (4.869e+24, 6.0518e6)
            EARTH = (5.976e+24, 6.37814e6)
            MARS = (6.421e+23, 3.3972e6)

        earth = Planet.EARTH
        print(f"Mass: {earth.value[0]:.2e}")    # Mass: 5.98e+24
        print(f"Radius: {earth.value[1]:.2e}")  # Radius: 6.38e+06

        def heaviest(planets):
            return max(planets, key=lambda p: p.value[0])

        print(heaviest(list(Planet)))  # Planet.EARTH

---

**Exercise 2.**
Define a `Status` enum with an alias: `ACTIVE = 1`, `ENABLED = 1` (alias), `INACTIVE = 2`, `DISABLED = 2` (alias). Show how to iterate over only canonical members (using `Status.__members__`) vs all members. Demonstrate that `Status.ACTIVE is Status.ENABLED`.

??? success "Solution to Exercise 2"

        from enum import Enum

        class Status(Enum):
            ACTIVE = 1
            ENABLED = 1   # Alias for ACTIVE
            INACTIVE = 2
            DISABLED = 2  # Alias for INACTIVE

        # Canonical members only (no aliases)
        for s in Status:
            print(s.name, s.value)
        # ACTIVE 1, INACTIVE 2

        # All members including aliases
        for name, member in Status.__members__.items():
            print(f"{name} -> {member.name}")
        # ACTIVE -> ACTIVE, ENABLED -> ACTIVE, ...

        print(Status.ACTIVE is Status.ENABLED)  # True

---

**Exercise 3.**
Create a `Currency` enum with values as 3-letter codes. Write a `from_value(value)` class method that converts a string value to the enum member (using `Currency(value)`). Handle invalid values by raising `ValueError` with a helpful message listing all valid values.

??? success "Solution to Exercise 3"

        from enum import Enum

        class Currency(Enum):
            USD = "USD"
            EUR = "EUR"
            GBP = "GBP"
            JPY = "JPY"

            @classmethod
            def from_value(cls, value):
                try:
                    return cls(value)
                except ValueError:
                    valid = [m.value for m in cls]
                    raise ValueError(f"Invalid currency '{value}'. Valid: {valid}")

        print(Currency.from_value("EUR"))  # Currency.EUR

        try:
            Currency.from_value("XYZ")
        except ValueError as e:
            print(f"Error: {e}")
