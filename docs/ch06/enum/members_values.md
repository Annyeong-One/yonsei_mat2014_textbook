# Enum Members and Values


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

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
