"""
TUTORIAL: Strategy Pattern with First-Class Functions

This tutorial covers the STRATEGY PATTERN, a classic design pattern that lets
you define different algorithms and switch between them dynamically.

The Traditional Approach: Object-oriented languages use classes for strategies.
You create an abstract Strategy class, then subclass it for each algorithm.

The Pythonic Way: Python's first-class functions are perfect for strategies!
Instead of strategy classes, just use functions. This is simpler, more elegant,
and often just as powerful.

The Example: An e-commerce system with different discount strategies based on
customer loyalty, bulk purchases, or order size. Each strategy is a simple
function that calculates a discount.

Key Insight: "Encapsulate what varies" - the discount calculation varies,
so we encapsulate it in strategy functions. The Order class is strategy-agnostic.
"""

from decimal import Decimal
from typing import Callable, NamedTuple, Optional, Sequence
from dataclasses import dataclass

print("=" * 70)
print("TUTORIAL: Strategy Pattern with First-Class Functions")
print("=" * 70)

# ============ EXAMPLE 1: The Data Structures
print("\n# ============ EXAMPLE 1: The Data Structures")
print("Define the core data structures for our e-commerce system:\n")


class Customer(NamedTuple):
    """A customer with a name and fidelity points"""
    name: str
    fidelity: int


class LineItem(NamedTuple):
    """A single line item in an order"""
    product: str
    quantity: int
    price: Decimal

    def total(self):
        """Calculate total price for this line item"""
        return self.price * self.quantity


@dataclass(frozen=True)
class Order:
    """
    An order with a customer and line items.

    The KEY innovation: strategy is just a function parameter!
    promotion: Optional[Callable[['Order'], Decimal]]
    """
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = None

    def total(self) -> Decimal:
        """Calculate total price before discount"""
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def due(self) -> Decimal:
        """Calculate final price after applying promotion strategy"""
        if self.promotion is None:
            discount = Decimal(0)
        else:
            # STRATEGY PATTERN: Call the strategy function!
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'


print("Created Customer, LineItem, and Order classes")
print("""
KEY DESIGN:
The Order class accepts a 'promotion' parameter that is a FUNCTION.
This function is the strategy - it calculates the discount.

Order(customer, cart, promotion=fidelity_promo)

The Order doesn't care what the strategy is - it just calls it!
""")

# ============ EXAMPLE 2: Defining Strategy Functions
print("\n" + "=" * 70)
print("# ============ EXAMPLE 2: Defining Strategy Functions")
print("Create different discount strategy functions:\n")


def fidelity_promo(order: Order) -> Decimal:
    """
    STRATEGY 1: Fidelity promotion
    Give 5% discount to customers with 1000+ fidelity points
    """
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


def bulk_item_promo(order: Order) -> Decimal:
    """
    STRATEGY 2: Bulk item promotion
    Give 10% discount for each line item with 20+ units
    """
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount


def large_order_promo(order: Order) -> Decimal:
    """
    STRATEGY 3: Large order promotion
    Give 7% discount for orders with 10+ distinct items
    """
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)


print("Defined three strategy functions:")
print("  - fidelity_promo: 5% discount for loyal customers (1000+ points)")
print("  - bulk_item_promo: 10% discount for bulk items (20+ units)")
print("  - large_order_promo: 7% discount for large orders (10+ items)")
print()

# ============ EXAMPLE 3: Demonstrating Strategy Pattern
print("\n" + "=" * 70)
print("# ============ EXAMPLE 3: Demonstrating Strategy Pattern")
print("Use different strategies with the same Order class:\n")

# Create some sample customers
joe = Customer('John Doe', 0)  # No fidelity points
ann = Customer('Ann Smith', 1100)  # High fidelity points

# Create a shopping cart
cart = [
    LineItem('banana', 4, Decimal('.5')),
    LineItem('apple', 10, Decimal('1.5')),
    LineItem('watermelon', 5, Decimal(5))
]

print("Customer Joe (no fidelity points):")
print(f"Cart: {cart}")

print("\nOrder with NO strategy (no discount):")
order1 = Order(joe, cart, promotion=None)
print(f"  {order1}")

print("\nOrder with fidelity strategy:")
order2 = Order(joe, cart, promotion=fidelity_promo)
print(f"  {order2}")
print("  (No discount because Joe has 0 fidelity points)")

print("\nCustomer Ann (1100 fidelity points):")
print("Order with same fidelity strategy:")
order3 = Order(ann, cart, promotion=fidelity_promo)
print(f"  {order3}")
print(f"  (5% discount: {order3.total() * Decimal('0.05'):.2f})")

# ============ EXAMPLE 4: Bulk Order Strategy
print("\n" + "=" * 70)
print("# ============ EXAMPLE 4: Bulk Order Strategy")
print("Test the bulk item discount strategy:\n")

banana_cart = [
    LineItem('banana', 30, Decimal('.5')),  # 30 bananas - qualifies for bulk
    LineItem('apple', 10, Decimal('1.5'))
]

print("Order with large banana quantity:")
print(f"Cart: {banana_cart}")

order4 = Order(joe, banana_cart, promotion=bulk_item_promo)
print(f"  {order4}")
print(f"  (10% discount on banana: {LineItem('banana', 30, Decimal('0.5')).total() * Decimal('0.1'):.2f})")

# ============ EXAMPLE 5: Large Order Strategy
print("\n" + "=" * 70)
print("# ============ EXAMPLE 5: Large Order Strategy")
print("Test the large order discount strategy:\n")

long_cart = [
    LineItem(str(item_code), 1, Decimal(1))
    for item_code in range(10)  # 10 distinct items
]

print("Order with 10 distinct items:")
print(f"Cart has {len(long_cart)} items")

order5 = Order(joe, long_cart, promotion=large_order_promo)
print(f"  {order5}")
print(f"  (7% discount: {order5.total() * Decimal('0.07'):.2f})")

print("\nSame order without large order promotion:")
order6 = Order(joe, long_cart, promotion=None)
print(f"  {order6}")

# ============ EXAMPLE 6: Understanding the Benefits
print("\n" + "=" * 70)
print("# ============ EXAMPLE 6: Understanding the Benefits")
print("Why this pattern is elegant:\n")

print("""
TRADITIONAL OOP STRATEGY PATTERN:

    class Promotion:
        def discount(self, order):
            pass

    class FidelityPromo(Promotion):
        def discount(self, order):
            if order.customer.fidelity >= 1000:
                return order.total() * Decimal('0.05')
            return Decimal(0)

    class BulkItemPromo(Promotion):
        def discount(self, order):
            # ...implementation...

PROBLEMS:
- Lots of boilerplate with classes
- Each strategy needs its own class
- Heavy and verbose

PYTHONIC FUNCTION-BASED APPROACH:

    def fidelity_promo(order):
        if order.customer.fidelity >= 1000:
            return order.total() * Decimal('0.05')
        return Decimal(0)

    def bulk_item_promo(order):
        # ...implementation...

BENEFITS:
- Simple and concise
- Each strategy is just a function
- No need for base class or inheritance
- Easy to add new strategies
- Highly readable and maintainable
""")

# ============ EXAMPLE 7: Adding New Strategies
print("\n" + "=" * 70)
print("# ============ EXAMPLE 7: Adding New Strategies")
print("Easy to add new strategies without modifying existing code:\n")


def new_customer_promo(order: Order) -> Decimal:
    """
    BONUS STRATEGY: Special discount for new customers
    Discount if customer has less than 50 total fidelity points
    """
    if order.customer.fidelity < 50:
        return order.total() * Decimal('0.02')  # 2% welcome discount
    return Decimal(0)


print("New strategy added: new_customer_promo (2% for new customers)")

new_customer = Customer('Jane Newcomer', 30)
print(f"\nCustomer: {new_customer}")

order7 = Order(new_customer, cart, promotion=new_customer_promo)
print(f"Order with new_customer_promo: {order7}")
print("\nNo Order class modifications needed - strategy is just a parameter!")

# ============ EXAMPLE 8: Dynamic Strategy Selection
print("\n" + "=" * 70)
print("# ============ EXAMPLE 8: Dynamic Strategy Selection")
print("Select the best strategy dynamically:\n")


def select_best_promotion(order: Order) -> Callable[[Order], Decimal]:
    """
    STRATEGY SELECTOR: Choose the best promotion for an order
    This shows that strategies are just functions that can be passed around!
    """
    promotions = [fidelity_promo, bulk_item_promo, large_order_promo]
    discounts = [promo(order) for promo in promotions]
    best_discount = max(discounts)
    best_promo = promotions[discounts.index(best_discount)]
    return best_promo


print("Create an order that qualifies for multiple strategies:")
multi_cart = [
    LineItem('product_' + str(i), 25, Decimal(10))  # 25 each, 10+ items
    for i in range(10)
]

multi_customer = Customer('VIP Customer', 1500)  # High fidelity

order8 = Order(multi_customer, multi_cart, promotion=None)
print(f"Best promotion? Let me check...")

best_promo = select_best_promotion(order8)
print(f"Selected: {best_promo.__name__}")

order8_with_best = Order(multi_customer, multi_cart, promotion=best_promo)
print(f"Order with best promotion: {order8_with_best}")

# ============ EXAMPLE 9: Real-World Application
print("\n" + "=" * 70)
print("# ============ EXAMPLE 9: Real-World Application")
print("Processing multiple orders with different strategies:\n")


def process_order(order: Order, strategy: Optional[Callable] = None) -> dict:
    """
    Process an order and return summary
    Strategy is optional - can use None or any promotion function
    """
    if strategy:
        order_with_promo = Order(order.customer, order.cart, promotion=strategy)
    else:
        order_with_promo = order

    return {
        'customer': order_with_promo.customer.name,
        'total': float(order_with_promo.total()),
        'discount': float(order_with_promo.total() - order_with_promo.due()),
        'due': float(order_with_promo.due()),
    }


orders_to_process = [
    (Order(Customer('Alice', 500), cart, None), fidelity_promo),
    (Order(Customer('Bob', 1500), cart, None), fidelity_promo),
    (Order(Customer('Charlie', 0), banana_cart, None), bulk_item_promo),
    (Order(Customer('Diana', 0), long_cart, None), large_order_promo),
]

print("Processing multiple orders:\n")
for order, strategy in orders_to_process:
    result = process_order(order, strategy)
    print(f"{result['customer']:15} -> Total: ${result['total']:7.2f}, "
          f"Discount: ${result['discount']:6.2f}, "
          f"Due: ${result['due']:7.2f}")

# ============ EXAMPLE 10: When to Use Strategy Pattern
print("\n" + "=" * 70)
print("# ============ EXAMPLE 10: When to Use Strategy Pattern")
print("Guidance on when to use this pattern:\n")

print("""
USE THE STRATEGY PATTERN WHEN:

1. You have multiple algorithms for a task
   - Different discount calculations
   - Different sorting algorithms
   - Different rendering engines
   - Different validation rules

2. Algorithms should be interchangeable
   - Switch between them at runtime
   - Client code doesn't depend on specific algorithm
   - Same interface for all strategies

3. You want to avoid conditionals
   - No big if/elif/else chains
   - No switch statements
   - Each strategy is self-contained

4. Strategies need to be extended
   - Easy to add new strategies
   - No modification to existing code
   - Open/closed principle

EXAMPLES:

- E-commerce discounts (our example!)
- Payment methods (credit card, PayPal, cryptocurrency)
- Sorting/filtering algorithms
- Rendering engines (HTML, PDF, JSON)
- Compression algorithms (ZIP, GZIP, RAR)
- Authentication methods (password, OAuth, SAML)
- Caching strategies (LRU, FIFO, LFU)


DON'T USE THE PATTERN WHEN:

- You only have one or two algorithms
- Algorithm selection is one-time
- Strategies are too simple to warrant abstraction
- Client code needs algorithm-specific knowledge


PYTHONIC ADVANTAGES:

Python functions are first-class, so:
- No need for strategy classes
- Just pass functions as parameters
- Simple, concise, readable
- Perfect for this pattern!
""")

# ============ EXAMPLE 11: Comparison with Traditional OOP
print("\n" + "=" * 70)
print("# ============ EXAMPLE 11: Comparison with Traditional OOP")
print("Function-based vs Class-based approaches:\n")

print("""
TRADITIONAL CLASS-BASED STRATEGY:

    class Order:
        def __init__(self, customer, cart, strategy):
            self.customer = customer
            self.cart = cart
            self.strategy = strategy  # Strategy object

        def due(self):
            discount = self.strategy.discount(self)  # Call method
            return self.total() - discount

    class FidelityPromo:
        def discount(self, order):
            ...

    order = Order(customer, cart, FidelityPromo())

LINES OF CODE: ~15-20
COMPLEXITY: Medium
REUSABILITY: Good with inheritance


PYTHON FUNCTION-BASED STRATEGY:

    class Order:
        def __init__(self, customer, cart, promotion=None):
            self.customer = customer
            self.cart = cart
            self.promotion = promotion  # Function reference

        def due(self):
            discount = self.promotion(self)  # Call function
            return self.total() - discount

    def fidelity_promo(order):
        ...

    order = Order(customer, cart, fidelity_promo)

LINES OF CODE: ~8-10
COMPLEXITY: Simple
REUSABILITY: Excellent with functions

ADVANTAGES OF FUNCTION APPROACH:

1. Less code - no boilerplate classes
2. More readable - strategies are simple functions
3. Easier to add strategies - just write a function
4. Better composability - functions can be composed
5. More Pythonic - leverages first-class functions
6. Less coupling - no inheritance hierarchies
""")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("""
KEY TAKEAWAYS:

1. STRATEGY PATTERN ENCAPSULATES ALGORITHMS
   Different ways to do something go in different strategy functions.
   The context (Order) is agnostic to which strategy is used.

2. PYTHONIC APPROACH: USE FUNCTIONS
   Instead of strategy classes, just use functions.
   Python functions are first-class - perfect for this!

3. BASIC STRUCTURE:

   class Context:
       def __init__(self, ...., strategy=None):
           self.strategy = strategy

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

   # Usage
   context = Context(..., strategy=strategy_a)

4. BENEFITS:
   - Encapsulates varying algorithms
   - Avoids complicated if/elif chains
   - Strategies can be swapped at runtime
   - Easy to add new strategies
   - Simple, Pythonic code

5. PERFECT FOR:
   - Discount calculation (our example)
   - Payment processing
   - Sorting/filtering
   - Rendering
   - Validation
   - Any interchangeable algorithm

6. KEY DIFFERENCE FROM OOP:
   - OOP: Create strategy classes and objects
   - Python: Just pass functions around
   - Simpler, more elegant, more Pythonic

7. REAL-WORLD PATTERN:
   "Context receives a strategy function that it calls to vary behavior"

8. DESIGN PRINCIPLE:
   Encapsulate what varies (the algorithm) from what stays the same
   (the rest of the code that uses the algorithm)

9. ADVANTAGES OVER CONDITIONALS:
   - No if/elif/else chains
   - Each strategy is separate and focused
   - Easy to test each strategy independently
   - Easy to add new strategies without modifying existing code

10. REMEMBER:
    Functions are first-class citizens in Python.
    Use them for the strategy pattern instead of classes.
    It's simpler, cleaner, and more Pythonic!
""")
