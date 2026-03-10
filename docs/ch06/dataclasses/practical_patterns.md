# Practical Patterns


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Real-world dataclass patterns that solve common problems: configuration objects, API models, and domain entities.

---

## Configuration Objects

```python
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class DatabaseConfig:
    host: str
    port: int = 5432
    username: str = "admin"
    password: str = field(repr=False)  # Don't show in repr
    options: Dict[str, str] = field(default_factory=dict)
    
    @property
    def connection_string(self) -> str:
        return f"postgres://{self.username}@{self.host}:{self.port}"

config = DatabaseConfig("localhost", password="secret")
print(f"Connecting to {config.connection_string}")
```

## API Request/Response Models

```python
from dataclasses import dataclass, asdict
from typing import Optional
from datetime import datetime

@dataclass
class User:
    id: int
    name: str
    email: str
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
    
    def to_dict(self):
        return asdict(self)

user = User(1, "Alice", "alice@example.com")
print(user.to_dict())
```

## Domain Model with Validation

```python
from dataclasses import dataclass
from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

@dataclass
class Order:
    order_id: str
    customer: str
    amount: float
    status: OrderStatus = OrderStatus.PENDING
    
    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount must be positive")
        if not self.order_id:
            raise ValueError("Order ID required")
    
    def ship(self):
        if self.status != OrderStatus.PENDING:
            raise ValueError("Can only ship pending orders")
        self.status = OrderStatus.SHIPPED
    
    def deliver(self):
        if self.status != OrderStatus.SHIPPED:
            raise ValueError("Can only deliver shipped orders")
        self.status = OrderStatus.DELIVERED

order = Order("ORD-001", "Alice", 99.99)
order.ship()
order.deliver()
print(f"Order {order.order_id}: {order.status.value}")
```

## Nested Dataclasses

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Address:
    street: str
    city: str
    country: str

@dataclass
class Contact:
    email: str
    phone: str

@dataclass
class Company:
    name: str
    address: Address
    contact: Contact
    employees: int = 0

company = Company(
    name="TechCorp",
    address=Address("123 Main St", "San Francisco", "USA"),
    contact=Contact("info@techcorp.com", "555-1234"),
    employees=50
)

print(f"{company.name} in {company.address.city}")
```

## Builder Pattern with Dataclasses

```python
from dataclasses import dataclass, field

@dataclass
class QueryBuilder:
    table: str
    where_conditions: list = field(default_factory=list)
    select_fields: list = field(default_factory=lambda: ["*"])
    limit_value: int = None
    
    def where(self, condition: str):
        self.where_conditions.append(condition)
        return self
    
    def select(self, *fields):
        self.select_fields = list(fields)
        return self
    
    def limit(self, count: int):
        self.limit_value = count
        return self
    
    def build(self) -> str:
        query = f"SELECT {', '.join(self.select_fields)} FROM {self.table}"
        if self.where_conditions:
            query += " WHERE " + " AND ".join(self.where_conditions)
        if self.limit_value:
            query += f" LIMIT {self.limit_value}"
        return query

query = (QueryBuilder("users")
         .select("id", "name", "email")
         .where("age > 18")
         .where("country = 'USA'")
         .limit(10)
         .build())

print(query)
```

## Data Validation with __post_init__

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class EmailList:
    emails: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        # Validate and normalize emails
        validated = []
        for email in self.emails:
            if '@' in email:
                validated.append(email.lower())
        self.emails = validated
    
    def add_email(self, email: str):
        if '@' in email:
            self.emails.append(email.lower())

email_list = EmailList(["Alice@Example.com", "Bob@Test.com"])
print(email_list.emails)  # ['alice@example.com', 'bob@test.com']
```
