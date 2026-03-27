# Strategy Pattern

The Strategy Pattern lets you define a family of algorithms, encapsulate each one, and make them interchangeable at runtime. In Python, first-class functions replace the strategy classes required in traditional OOP implementations.

**Key Insight**: "Encapsulate what varies" — the algorithm varies, so pass it as a function parameter. The context class remains algorithm-agnostic.

---

## Core Structure

```python
class Context:
    def __init__(self, ..., strategy=None):
        self.strategy = strategy  # A function reference

    def do_something(self):
        if self.strategy:
            result = self.strategy(self)  # Call the strategy function
        return result

def strategy_a(context):
    # Algorithm A
    return result

def strategy_b(context):
    # Algorithm B
    return result

# Usage — swap strategies without touching Context
context = Context(..., strategy=strategy_a)
```

---

## Example: E-Commerce Discount System

### Data Structures

```python
from decimal import Decimal
from typing import Callable, Optional, Sequence
from dataclasses import dataclass
from typing import NamedTuple


class Customer(NamedTuple):
    name: str
    fidelity: int  # loyalty points


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self):
        return self.price * self.quantity


@dataclass(frozen=True)
class Order:
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = None  # ← strategy function

    def total(self) -> Decimal:
        return sum((item.total() for item in self.cart), start=Decimal(0))

    def due(self) -> Decimal:
        discount = self.promotion(self) if self.promotion else Decimal(0)
        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'
```

The `Order` class accepts any callable as `promotion`. It doesn't know or care which strategy is used — it just calls it.

### Strategy Functions

```python
def fidelity_promo(order: Order) -> Decimal:
    """5% discount for customers with 1000+ fidelity points."""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


def bulk_item_promo(order: Order) -> Decimal:
    """10% discount on any line item with 20+ units."""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount


def large_order_promo(order: Order) -> Decimal:
    """7% discount for orders with 10+ distinct products."""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)


def new_customer_promo(order: Order) -> Decimal:
    """2% welcome discount for customers with fewer than 50 fidelity points."""
    if order.customer.fidelity < 50:
        return order.total() * Decimal('0.02')
    return Decimal(0)
```

### Using Strategies

```python
joe = Customer('John Doe', 0)      # no fidelity points
ann = Customer('Ann Smith', 1100)  # high fidelity

cart = [
    LineItem('banana', 4, Decimal('.5')),
    LineItem('apple', 10, Decimal('1.5')),
    LineItem('watermelon', 5, Decimal(5)),
]

# No discount
Order(joe, cart)
# <Order total: 17.00 due: 17.00>

# fidelity_promo — Joe has 0 points, no discount
Order(joe, cart, promotion=fidelity_promo)
# <Order total: 17.00 due: 17.00>

# fidelity_promo — Ann has 1100 points, 5% discount
Order(ann, cart, promotion=fidelity_promo)
# <Order total: 17.00 due: 16.15>

# bulk_item_promo — 30 bananas qualifies
banana_cart = [LineItem('banana', 30, Decimal('.5')), LineItem('apple', 10, Decimal('1.5'))]
Order(joe, banana_cart, promotion=bulk_item_promo)
# <Order total: 30.00 due: 28.50>
```

---

## Adding New Strategies

No modifications to `Order` needed — just write a new function:

```python
def flash_sale_promo(order: Order) -> Decimal:
    """15% discount on all orders during flash sale period."""
    return order.total() * Decimal('0.15')

# Plug it straight in
Order(joe, cart, promotion=flash_sale_promo)
```

This satisfies the **Open/Closed Principle**: open for extension, closed for modification.

---

## Dynamic Strategy Selection

Because strategies are plain functions, they can be stored in lists and selected programmatically:

```python
promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order: Order) -> Decimal:
    """Apply whichever promotion gives the largest discount."""
    return max(promo(order) for promo in promos)

Order(ann, cart, promotion=best_promo)
```

---

## Python vs Traditional OOP

=== "Pythonic (functions)"

    ```python
    def fidelity_promo(order):
        if order.customer.fidelity >= 1000:
            return order.total() * Decimal('0.05')
        return Decimal(0)

    order = Order(customer, cart, promotion=fidelity_promo)
    ```

=== "Traditional OOP (classes)"

    ```python
    class Promotion:
        def discount(self, order): ...

    class FidelityPromo(Promotion):
        def discount(self, order):
            if order.customer.fidelity >= 1000:
                return order.total() * Decimal('0.05')
            return Decimal(0)

    order = Order(customer, cart, strategy=FidelityPromo())
    ```

The function-based approach is shorter, requires no inheritance hierarchy, and is easier to test each strategy in isolation.

---

## When to Use the Strategy Pattern

**Use it when:**

- You have multiple interchangeable algorithms for the same task
- You want to swap algorithms at runtime
- You want to eliminate large `if/elif/else` chains
- New strategies should be addable without modifying existing code

**Common applications:**

| Domain | Strategies |
|--------|-----------|
| E-commerce | Discount calculations, shipping methods |
| Payments | Credit card, PayPal, cryptocurrency |
| Sorting | Bubble sort, quicksort, merge sort |
| Rendering | HTML, PDF, JSON output |
| Compression | ZIP, GZIP, BZIP2 |
| Authentication | Password, OAuth, SAML |
| Caching | LRU, FIFO, LFU eviction |

**Skip it when:**

- You only have one or two algorithms that never change
- The algorithms are trivial one-liners
- Client code genuinely needs algorithm-specific knowledge

---

## Summary

| Concept | Description |
|---------|-------------|
| Context | The class that delegates to a strategy (`Order`) |
| Strategy | A callable that implements one algorithm (`fidelity_promo`) |
| Selection | Pass strategy as a constructor or method argument |
| Extension | Add new strategies as new functions — no class changes |
| Python advantage | First-class functions eliminate the need for strategy classes |

**The one-line version**: pass a function where behaviour varies; keep everything else the same.
