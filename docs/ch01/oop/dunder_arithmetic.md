# Arithmetic Operators

Arithmetic dunder methods enable mathematical operations on custom objects through operator overloading.

---

## Basic Arithmetic

### 1. Addition: `__add__`

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Vector(4, 6)
```

### 2. Subtraction: `__sub__`

```python
def __sub__(self, other):
    return Vector(self.x - other.x, self.y - other.y)

v3 = v1 - v2  # Vector(-2, -2)
```

### 3. Multiplication: `__mul__`

```python
def __mul__(self, scalar):
    return Vector(self.x * scalar, self.y * scalar)

v3 = v1 * 3  # Vector(3, 6)
```

---

## Division Operators

### 1. True Division: `__truediv__`

```python
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    
    def __truediv__(self, other):
        return Fraction(
            self.num * other.den,
            self.den * other.num
        )

f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
result = f1 / f2  # 1/2 ÷ 3/4 = 4/6
```

### 2. Floor Division: `__floordiv__`

```python
def __floordiv__(self, other):
    return self.num // other.num

result = f1 // f2
```

### 3. Modulo: `__mod__`

```python
def __mod__(self, other):
    return self.value % other.value
```

---

## Power and Unary

### 1. Power: `__pow__`

```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __pow__(self, exponent):
        return Number(self.value ** exponent)

n = Number(2)
result = n ** 3  # Number(8)
```

### 2. Negation: `__neg__`

```python
def __neg__(self):
    return Vector(-self.x, -self.y)

v = Vector(1, 2)
v_neg = -v  # Vector(-1, -2)
```

### 3. Positive: `__pos__`

```python
def __pos__(self):
    return Vector(abs(self.x), abs(self.y))
```

---

## Operator Table

### 1. Binary Operators

| Operator | Method | Example |
|----------|--------|---------|
| `+` | `__add__` | `a + b` |
| `-` | `__sub__` | `a - b` |
| `*` | `__mul__` | `a * b` |
| `/` | `__truediv__` | `a / b` |
| `//` | `__floordiv__` | `a // b` |
| `%` | `__mod__` | `a % b` |
| `**` | `__pow__` | `a ** b` |

### 2. Unary Operators

| Operator | Method | Example |
|----------|--------|---------|
| `-` | `__neg__` | `-a` |
| `+` | `__pos__` | `+a` |
| `abs()` | `__abs__` | `abs(a)` |

### 3. Call Signatures

```python
def __add__(self, other): ...
def __neg__(self): ...
def __abs__(self): ...
```

---

## Reversed Operations

### 1. Right-Hand Operations

```python
class Vector:
    def __add__(self, other):
        return Vector(self.x + other, self.y + other)
    
    def __radd__(self, other):
        # Called when: other + self
        return Vector(other + self.x, other + self.y)

v = Vector(1, 2)
result = v + 5    # Uses __add__
result = 5 + v    # Uses __radd__
```

### 2. When Used

Python tries `__radd__` if left operand doesn't support operation.

### 3. Common Pattern

```python
def __radd__(self, other):
    return self.__add__(other)  # Delegate to __add__
```

---

## In-Place Operations

### 1. In-Place Addition: `__iadd__`

```python
class Counter:
    def __init__(self, count):
        self.count = count
    
    def __iadd__(self, other):
        self.count += other
        return self  # Important!

c = Counter(5)
c += 3  # Calls __iadd__
print(c.count)  # 8
```

### 2. Mutable vs Immutable

```python
# Mutable - modify in place
def __iadd__(self, other):
    self.value += other.value
    return self

# Immutable - return new object
def __iadd__(self, other):
    return MyClass(self.value + other.value)
```

### 3. Must Return Self

```python
def __iadd__(self, other):
    self.value += other.value
    return self  # Required!
```

---

## In-Place Table

### 1. In-Place Operators

| Operator | Method | Example |
|----------|--------|---------|
| `+=` | `__iadd__` | `a += b` |
| `-=` | `__isub__` | `a -= b` |
| `*=` | `__imul__` | `a *= b` |
| `/=` | `__itruediv__` | `a /= b` |
| `//=` | `__ifloordiv__` | `a //= b` |
| `%=` | `__imod__` | `a %= b` |
| `**=` | `__ipow__` | `a **= b` |

### 2. Fallback Behavior

If `__iadd__` not defined, Python uses `__add__`.

### 3. Optimization

In-place can be more efficient for mutable types.

---

## Vector Example

### 1. Complete Implementation

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

### 2. Usage Examples

```python
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)   # Vector(4, 6)
print(v1 - v2)   # Vector(2, 2)
print(v1 * 2)    # Vector(6, 8)
print(v1 / 2)    # Vector(1.5, 2.0)
print(-v1)       # Vector(-3, -4)
```

### 3. Chaining Operations

```python
result = (v1 + v2) * 2 - v1
```

---

## Best Practices

### 1. Return New Objects

```python
# Good - immutable
def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

# Bad - mutates self
def __add__(self, other):
    self.x += other.x
    return self
```

### 2. Type Checking

```python
def __add__(self, other):
    if not isinstance(other, Vector):
        return NotImplemented
    return Vector(self.x + other.x, self.y + other.y)
```

### 3. Symmetric Operations

```python
def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

def __radd__(self, other):
    return self.__add__(other)
```

---

## Key Takeaways

- Arithmetic operators map to dunder methods.
- `__add__`, `__sub__`, `__mul__`, `__truediv__` are most common.
- Reversed methods (`__radd__`) handle right-hand operations.
- In-place methods (`__iadd__`) optimize mutations.
- Return new objects for immutable types.
