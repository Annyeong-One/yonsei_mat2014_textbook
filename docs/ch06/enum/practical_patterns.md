# Enum Practical Patterns

Real-world enum patterns that solve common application needs: state machines, configuration, and domain modeling.

---

## State Machine Pattern

```python
from enum import Enum
from typing import Optional

class OrderState(Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    
    def can_transition_to(self, next_state) -> bool:
        '''Check if transition is allowed'''
        valid_transitions = {
            OrderState.PENDING: {OrderState.PAID, OrderState.CANCELLED},
            OrderState.PAID: {OrderState.SHIPPED, OrderState.CANCELLED},
            OrderState.SHIPPED: {OrderState.DELIVERED},
            OrderState.DELIVERED: set(),
            OrderState.CANCELLED: set()
        }
        return next_state in valid_transitions.get(self, set())

order_state = OrderState.PENDING
print(order_state.can_transition_to(OrderState.PAID))      # True
print(order_state.can_transition_to(OrderState.SHIPPED))   # False
```

## Configuration with Enums

```python
from enum import Enum
from dataclasses import dataclass

class Environment(Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    
    @property
    def config(self):
        '''Get configuration for environment'''
        configs = {
            Environment.DEVELOPMENT: {
                'debug': True,
                'log_level': 'DEBUG',
                'database_url': 'sqlite:///:memory:'
            },
            Environment.STAGING: {
                'debug': False,
                'log_level': 'INFO',
                'database_url': 'postgresql://staging-db'
            },
            Environment.PRODUCTION: {
                'debug': False,
                'log_level': 'WARNING',
                'database_url': 'postgresql://prod-db'
            }
        }
        return configs[self]

env = Environment.PRODUCTION
config = env.config
print(f"Debug: {config['debug']}, DB: {config['database_url']}")
```

## HTTP Method and Status Codes

```python
from enum import Enum, IntEnum

class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    
    def is_idempotent(self) -> bool:
        '''Check if method is idempotent'''
        idempotent = {HttpMethod.GET, HttpMethod.PUT, HttpMethod.DELETE}
        return self in idempotent

class HttpStatus(IntEnum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    SERVER_ERROR = 500
    
    @property
    def is_success(self) -> bool:
        '''Check if status indicates success'''
        return 200 <= self.value < 300
    
    @property
    def is_client_error(self) -> bool:
        '''Check if status indicates client error'''
        return 400 <= self.value < 500

method = HttpMethod.PUT
print(f"PUT is idempotent: {method.is_idempotent()}")  # True

status = HttpStatus.CREATED
print(f"201 is success: {status.is_success}")  # True
```

## User Roles and Permissions

```python
from enum import Enum

class UserRole(Enum):
    GUEST = 0
    USER = 1
    MODERATOR = 2
    ADMIN = 3
    
    def can_perform(self, action: str) -> bool:
        '''Check if role can perform action'''
        permissions = {
            'view_content': {UserRole.GUEST, UserRole.USER, UserRole.MODERATOR, UserRole.ADMIN},
            'edit_own': {UserRole.USER, UserRole.MODERATOR, UserRole.ADMIN},
            'edit_others': {UserRole.MODERATOR, UserRole.ADMIN},
            'delete_content': {UserRole.MODERATOR, UserRole.ADMIN},
            'manage_users': {UserRole.ADMIN}
        }
        return self in permissions.get(action, set())

admin = UserRole.ADMIN
user = UserRole.USER

print(f"Admin can manage users: {admin.can_perform('manage_users')}")  # True
print(f"User can manage users: {user.can_perform('manage_users')}")    # False
print(f"User can edit own: {user.can_perform('edit_own')}")            # True
```

## Notification Types and Handling

```python
from enum import Enum
from typing import Callable, Dict

class NotificationType(Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
    WEBHOOK = "webhook"
    
    def get_handler(self) -> Callable:
        '''Get handler function for notification type'''
        handlers = {
            NotificationType.EMAIL: self._send_email,
            NotificationType.SMS: self._send_sms,
            NotificationType.PUSH: self._send_push,
            NotificationType.WEBHOOK: self._send_webhook
        }
        return handlers[self]
    
    @staticmethod
    def _send_email(message: str) -> bool:
        print(f"Sending email: {message}")
        return True
    
    @staticmethod
    def _send_sms(message: str) -> bool:
        print(f"Sending SMS: {message}")
        return True
    
    @staticmethod
    def _send_push(message: str) -> bool:
        print(f"Sending push notification: {message}")
        return True
    
    @staticmethod
    def _send_webhook(message: str) -> bool:
        print(f"Posting webhook: {message}")
        return True

notif_type = NotificationType.EMAIL
handler = notif_type.get_handler()
handler("Hello, World!")
```

## File Type and Handler

```python
from enum import Enum

class FileType(Enum):
    JSON = ".json"
    CSV = ".csv"
    XML = ".xml"
    YAML = ".yaml"
    
    @property
    def parser_module(self) -> str:
        '''Get module name for parsing this file type'''
        modules = {
            FileType.JSON: "json",
            FileType.CSV: "csv",
            FileType.XML: "xml.etree.ElementTree",
            FileType.YAML: "yaml"
        }
        return modules[self]
    
    def validate_content(self, content: str) -> bool:
        '''Basic validation for file type'''
        validators = {
            FileType.JSON: lambda c: c.strip().startswith(('{', '[')),
            FileType.CSV: lambda c: True,  # Minimal validation
            FileType.XML: lambda c: c.strip().startswith('<'),
            FileType.YAML: lambda c: True
        }
        return validators[self](content)

file_type = FileType.JSON
print(f"JSON uses: {file_type.parser_module}")      # json
print(f"Valid JSON: {file_type.validate_content('{}')}")  # True
```

## Color and Formatting

```python
from enum import Enum

class ColorCode(Enum):
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    
    def format_text(self, text: str) -> str:
        '''Format text with ANSI color code'''
        return f"[{self.value}m{text}[0m"

text = "Important!"
print(ColorCode.RED.format_text(text))      # Displays in red
print(ColorCode.GREEN.format_text("Good"))  # Displays in green
```

## Time Period Enums

```python
from enum import Enum
from datetime import timedelta

class TimePeriod(Enum):
    HOURLY = timedelta(hours=1)
    DAILY = timedelta(days=1)
    WEEKLY = timedelta(days=7)
    MONTHLY = timedelta(days=30)
    YEARLY = timedelta(days=365)
    
    def get_seconds(self) -> int:
        '''Get period duration in seconds'''
        return int(self.value.total_seconds())

period = TimePeriod.WEEKLY
print(f"Weekly period: {period.get_seconds()} seconds")  # 604800
```
