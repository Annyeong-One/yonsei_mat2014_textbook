# Arithmetic Operators

Arithmetic dunder methods enable mathematical operations on custom objects through operator overloading.

## Basic Arithmetic Operations

### Addition: `__add__`

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
```

### All Basic Operations

```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):       # self + other
        return Number(self.value + other.value)
    
    def __sub__(self, other):       # self - other
        return Number(self.value - other.value)
    
    def __mul__(self, other):       # self * other
        return Number(self.value * other.value)
    
    def __truediv__(self, other):   # self / other
        return Number(self.value / other.value)
    
    def __floordiv__(self, other):  # self // other
        return Number(self.value // other.value)
    
    def __mod__(self, other):       # self % other
        return Number(self.value % other.value)
    
    def __pow__(self, other):       # self ** other
        return Number(self.value ** other.value)
    
    def __repr__(self):
        return f"Number({self.value})"
```

### Operator Summary Table

| Method | Operator | Example |
|--------|----------|---------|
| `__add__` | `+` | `a + b` |
| `__sub__` | `-` | `a - b` |
| `__mul__` | `*` | `a * b` |
| `__truediv__` | `/` | `a / b` |
| `__floordiv__` | `//` | `a // b` |
| `__mod__` | `%` | `a % b` |
| `__pow__` | `**` | `a ** b` |
| `__matmul__` | `@` | `a @ b` |

## Unary Operators

```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __neg__(self):      # -self
        return Number(-self.value)
    
    def __pos__(self):      # +self
        return Number(+self.value)
    
    def __abs__(self):      # abs(self)
        return Number(abs(self.value))
    
    def __invert__(self):   # ~self (bitwise NOT)
        return Number(~self.value)
    
    def __repr__(self):
        return f"Number({self.value})"

n = Number(-5)
print(-n)      # Number(5)
print(abs(n))  # Number(5)
```

## Reflected (Right) Operations

When the left operand doesn't support the operation, Python tries the right operand's reflected method.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __mul__(self, scalar):
        """Vector * scalar"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar):
        """scalar * Vector (when scalar.__mul__ fails)"""
        return self.__mul__(scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v = Vector(1, 2)
print(v * 3)    # Vector(3, 6)  - uses __mul__
print(3 * v)    # Vector(3, 6)  - uses __rmul__
```

### How Reflected Operations Work

```
3 * v
  ↓
int.__mul__(3, v) → NotImplemented
  ↓
Vector.__rmul__(v, 3) → Vector(3, 6)
```

### All Reflected Methods

| Regular | Reflected | When Used |
|---------|-----------|-----------|
| `__add__` | `__radd__` | `other + self` |
| `__sub__` | `__rsub__` | `other - self` |
| `__mul__` | `__rmul__` | `other * self` |
| `__truediv__` | `__rtruediv__` | `other / self` |
| `__floordiv__` | `__rfloordiv__` | `other // self` |
| `__mod__` | `__rmod__` | `other % self` |
| `__pow__` | `__rpow__` | `other ** self` |
| `__matmul__` | `__rmatmul__` | `other @ self` |

## In-Place Operations

In-place operations modify the object and return `self`.

```python
class Counter:
    def __init__(self, value=0):
        self.value = value
    
    def __iadd__(self, other):
        """self += other"""
        self.value += other
        return self  # Must return self!
    
    def __isub__(self, other):
        """self -= other"""
        self.value -= other
        return self
    
    def __imul__(self, other):
        """self *= other"""
        self.value *= other
        return self
    
    def __repr__(self):
        return f"Counter({self.value})"

c = Counter(10)
print(id(c))    # 140234567890
c += 5
print(c)        # Counter(15)
print(id(c))    # 140234567890 (same object!)
```

### Mutable vs Immutable In-Place

```python
# Mutable: modify in place
class MutableVector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self  # Same object

# Immutable: return new object
class ImmutableVector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, other):
        return ImmutableVector(self.x + other.x, self.y + other.y)
    
    # No __iadd__ - += will use __add__ and rebind
```

### All In-Place Methods

| Method | Operator | Effect |
|--------|----------|--------|
| `__iadd__` | `+=` | Add in place |
| `__isub__` | `-=` | Subtract in place |
| `__imul__` | `*=` | Multiply in place |
| `__itruediv__` | `/=` | Divide in place |
| `__ifloordiv__` | `//=` | Floor divide in place |
| `__imod__` | `%=` | Modulo in place |
| `__ipow__` | `**=` | Power in place |
| `__imatmul__` | `@=` | Matrix multiply in place |

## Bitwise Operations

```python
class Flags:
    def __init__(self, value=0):
        self.value = value
    
    def __and__(self, other):       # self & other
        return Flags(self.value & other.value)
    
    def __or__(self, other):        # self | other
        return Flags(self.value | other.value)
    
    def __xor__(self, other):       # self ^ other
        return Flags(self.value ^ other.value)
    
    def __invert__(self):           # ~self
        return Flags(~self.value)
    
    def __lshift__(self, n):        # self << n
        return Flags(self.value << n)
    
    def __rshift__(self, n):        # self >> n
        return Flags(self.value >> n)
    
    def __repr__(self):
        return f"Flags(0b{self.value:08b})"

READ = Flags(0b001)
WRITE = Flags(0b010)
EXECUTE = Flags(0b100)

permissions = READ | WRITE
print(permissions)           # Flags(0b00000011)
print(permissions & READ)    # Flags(0b00000001)
```

### Bitwise Method Summary

| Method | Operator | Reflected | In-Place |
|--------|----------|-----------|----------|
| `__and__` | `&` | `__rand__` | `__iand__` |
| `__or__` | `\|` | `__ror__` | `__ior__` |
| `__xor__` | `^` | `__rxor__` | `__ixor__` |
| `__lshift__` | `<<` | `__rlshift__` | `__ilshift__` |
| `__rshift__` | `>>` | `__rrshift__` | `__irshift__` |

## Matrix Multiplication (@)

Python 3.5+ added the `@` operator for matrix multiplication.

```python
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
    
    def __matmul__(self, other):
        """Matrix multiplication: self @ other"""
        if self.cols != other.rows:
            raise ValueError("Incompatible dimensions")
        
        result = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)
    
    def __repr__(self):
        return f"Matrix({self.data})"

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])
C = A @ B
print(C)  # Matrix([[19, 22], [43, 50]])
```

## Practical Example: Money Class

```python
from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, amount, currency='USD'):
        self.amount = round(amount, 2)
        self.currency = currency
    
    def _check_currency(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f"Cannot mix {self.currency} and {other.currency}")
        return True
    
    def __add__(self, other):
        self._check_currency(other)
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        self._check_currency(other)
        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Money(self.amount * scalar, self.currency)
        return NotImplemented
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Money(self.amount / scalar, self.currency)
        return NotImplemented
    
    def __neg__(self):
        return Money(-self.amount, self.currency)
    
    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency
    
    def __lt__(self, other):
        self._check_currency(other)
        return self.amount < other.amount
    
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"
    
    def __str__(self):
        return f"${self.amount:.2f} {self.currency}"

# Usage
price = Money(19.99)
tax = Money(1.60)
total = price + tax
print(total)        # \$21.59 USD
print(total * 2)    # \$43.18 USD
print(2 * total)    # \$43.18 USD (uses __rmul__)
```

## Returning NotImplemented

Always return `NotImplemented` (not raise `NotImplementedError`) when an operation doesn't make sense:

```python
class Vector:
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        # DON'T: raise TypeError("unsupported operand type")
        # DO: return NotImplemented
        return NotImplemented
```

This allows Python to try the reflected operation on the other operand.

## divmod and Power with Modulo

```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __divmod__(self, other):
        """divmod(self, other) → (quotient, remainder)"""
        q = self.value // other.value
        r = self.value % other.value
        return (Number(q), Number(r))
    
    def __pow__(self, exp, mod=None):
        """pow(self, exp[, mod])"""
        if mod is None:
            return Number(self.value ** exp.value)
        return Number(pow(self.value, exp.value, mod.value))
    
    def __repr__(self):
        return f"Number({self.value})"

a = Number(17)
b = Number(5)
q, r = divmod(a, b)
print(q, r)  # Number(3) Number(2)

# Modular exponentiation
print(pow(Number(2), Number(10), Number(100)))  # Number(24)
```

## Key Takeaways

- Arithmetic dunders enable natural mathematical syntax
- Always return `NotImplemented` for unsupported types
- Implement `__rmul__` etc. for commutative operations with scalars
- In-place methods (`__iadd__` etc.) must return `self`
- Use `@total_ordering` to reduce comparison boilerplate
- Type check with `isinstance()` before operations
- Bitwise operators work similarly with `&`, `|`, `^`, `~`, `<<`, `>>`
