"""
Example 3: Arithmetic Operators
Demonstrates: __add__, __sub__, __mul__, __truediv__, __pow__, etc.
"""


class Vector:
    """A 2D vector class with arithmetic operations."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self):
        return f"<{self.x}, {self.y}>"
    
    def __add__(self, other):
        """Add two vectors or add a scalar to both components."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        return NotImplemented
    
    def __radd__(self, other):
        """Right-side addition (when left operand doesn't support +)."""
        return self.__add__(other)
    
    def __sub__(self, other):
        """Subtract two vectors or subtract a scalar."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        return NotImplemented
    
    def __mul__(self, other):
        """Multiply vector by scalar."""
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented
    
    def __rmul__(self, other):
        """Right-side multiplication (allows scalar * vector)."""
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Divide vector by scalar."""
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Vector(self.x / other, self.y / other)
        return NotImplemented
    
    def __neg__(self):
        """Negate the vector."""
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        """Return the magnitude of the vector."""
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Money:
    """A money class with currency support."""
    
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency
    
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"
    
    def __str__(self):
        return f"{self.currency} ${self.amount:.2f}"
    
    def __add__(self, other):
        """Add two money amounts (must be same currency)."""
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"Cannot add {self.currency} and {other.currency}")
            return Money(self.amount + other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        return NotImplemented
    
    def __sub__(self, other):
        """Subtract two money amounts."""
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"Cannot subtract {other.currency} from {self.currency}")
            return Money(self.amount - other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount - other, self.currency)
        return NotImplemented
    
    def __mul__(self, other):
        """Multiply money by a number."""
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        return NotImplemented
    
    def __rmul__(self, other):
        """Right-side multiplication."""
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Divide money by a number."""
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Money(self.amount / other, self.currency)
        return NotImplemented


# Examples
if __name__ == "__main__":
    print("=== Vector Arithmetic Examples ===")
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    
    print(f"\nv1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3 = {v1 * 3}")
    print(f"2 * v1 = {2 * v1}")  # Uses __rmul__
    print(f"v1 / 2 = {v1 / 2}")
    print(f"-v1 = {-v1}")
    print(f"abs(v1) = {abs(v1)}")
    
    print("\n=== Vector with Scalar ===")
    v3 = v1 + 5  # Add 5 to both components
    print(f"v1 + 5 = {v3}")
    
    print("\n\n=== Money Arithmetic Examples ===")
    price1 = Money(25.50)
    price2 = Money(10.25)
    
    print(f"price1 = {price1}")
    print(f"price2 = {price2}")
    
    print(f"\nTotal: {price1 + price2}")
    print(f"Difference: {price1 - price2}")
    print(f"Double price1: {price1 * 2}")
    print(f"Split price1 3 ways: {price1 / 3}")
    
    print("\n=== Currency Mismatch Example ===")
    usd = Money(100, "USD")
    eur = Money(85, "EUR")
    print(f"usd = {usd}")
    print(f"eur = {eur}")
    
    try:
        result = usd + eur
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n=== Tax Calculation Example ===")
    subtotal = Money(50.00)
    tax_rate = 0.08
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    print(f"Subtotal: {subtotal}")
    print(f"Tax (8%): {tax}")
    print(f"Total: {total}")
