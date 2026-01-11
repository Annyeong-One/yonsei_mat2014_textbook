# Advanced Dunder Methods

Advanced dunder methods enable callable objects, boolean contexts, bitwise operations, and context management.

---

## Boolean Context

### 1. `__bool__`

```python
class SmartBox:
    def __init__(self, items):
        self.items = items
    
    def __bool__(self):
        return bool(self.items)

box = SmartBox([1, 2, 3])
if box:  # Calls __bool__
    print("Box has items")
```

### 2. Truthy/Falsy

```python
empty_box = SmartBox([])
if not empty_box:
    print("Box is empty")
```

### 3. Fallback to `__len__`

```python
class Container:
    def __len__(self):
        return 5
    # No __bool__ - uses __len__ != 0

c = Container()
print(bool(c))  # True (len is 5)
```

---

## Boolean Behavior

### 1. Default Behavior

```python
# Without __bool__ or __len__
class Always:
    pass

a = Always()
print(bool(a))  # True (objects are truthy by default)
```

### 2. Custom Logic

```python
class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def __bool__(self):
        return self.balance > 0

acc = Account(100)
if acc:
    print("Account has funds")
```

### 3. Short-Circuit Evaluation

```python
if box and box.items[0] > 10:
    # __bool__ called on box
    pass
```

---

## Callable Objects

### 1. `__call__`

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

times3 = Multiplier(3)
print(times3(10))  # 30
```

### 2. Function-like Objects

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        return self.count

c = Counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

### 3. With State

```python
class Accumulator:
    def __init__(self):
        self.total = 0
    
    def __call__(self, value):
        self.total += value
        return self.total

acc = Accumulator()
print(acc(5))   # 5
print(acc(10))  # 15
```

---

## Context Managers

### 1. `__enter__` and `__exit__`

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

with FileManager("data.txt", "w") as f:
    f.write("Hello")
```

### 2. Resource Management

```python
class DatabaseConnection:
    def __enter__(self):
        self.conn = create_connection()
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        return False  # Don't suppress exceptions
```

### 3. Exception Handling

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    self.cleanup()
    if exc_type is ValueError:
        print("Caught ValueError")
        return True  # Suppress exception
    return False  # Propagate other exceptions
```

---

## Bitwise Operators

### 1. AND: `__and__`

```python
class BitSet:
    def __init__(self, value):
        self.value = value
    
    def __and__(self, other):
        return BitSet(self.value & other.value)

a = BitSet(0b1100)
b = BitSet(0b1010)
c = a & b  # BitSet(0b1000)
```

### 2. OR: `__or__`

```python
def __or__(self, other):
    return BitSet(self.value | other.value)

c = a | b  # BitSet(0b1110)
```

### 3. XOR: `__xor__`

```python
def __xor__(self, other):
    return BitSet(self.value ^ other.value)

c = a ^ b  # BitSet(0b0110)
```

---

## Bitwise Table

### 1. Binary Operators

| Operator | Method | Example |
|----------|--------|---------|
| `&` | `__and__` | `a & b` |
| `\|` | `__or__` | `a \| b` |
| `^` | `__xor__` | `a ^ b` |
| `<<` | `__lshift__` | `a << 2` |
| `>>` | `__rshift__` | `a >> 2` |

### 2. Unary Operator

| Operator | Method | Example |
|----------|--------|---------|
| `~` | `__invert__` | `~a` |

### 3. In-Place Variants

```python
__iand__, __ior__, __ixor__
__ilshift__, __irshift__
```

---

## Shift Operators

### 1. Left Shift: `__lshift__`

```python
class BitSet:
    def __lshift__(self, n):
        return BitSet(self.value << n)

a = BitSet(0b0001)
b = a << 2  # BitSet(0b0100)
```

### 2. Right Shift: `__rshift__`

```python
def __rshift__(self, n):
    return BitSet(self.value >> n)

b = a >> 1  # BitSet(0b0000)
```

### 3. Bit Manipulation

```python
class Flags:
    def __init__(self, value=0):
        self.value = value
    
    def __lshift__(self, n):
        return Flags(self.value << n)
    
    def __or__(self, other):
        return Flags(self.value | other.value)
```

---

## Invert Operator

### 1. `__invert__`

```python
class BitSet:
    def __init__(self, value, width=8):
        self.value = value
        self.width = width
    
    def __invert__(self):
        mask = (1 << self.width) - 1
        return BitSet(self.value ^ mask, self.width)

a = BitSet(0b00001111, 8)
b = ~a  # BitSet(0b11110000, 8)
```

### 2. Logical Negation

```python
class BoolValue:
    def __init__(self, value):
        self.value = value
    
    def __invert__(self):
        return BoolValue(not self.value)
```

### 3. Custom Semantics

Define meaning appropriate for your class.

---

## Attribute Access

### 1. `__getattr__`

```python
class DynamicObject:
    def __getattr__(self, name):
        return f"Attribute '{name}' not found"

obj = DynamicObject()
print(obj.anything)  # "Attribute 'anything' not found"
```

### 2. `__setattr__`

```python
class ValidatedObject:
    def __setattr__(self, name, value):
        if name == "age" and value < 0:
            raise ValueError("Age cannot be negative")
        super().__setattr__(name, value)

obj = ValidatedObject()
obj.age = 25  # OK
obj.age = -5  # ValueError
```

### 3. `__delattr__`

```python
def __delattr__(self, name):
    if name == "id":
        raise AttributeError("Cannot delete ID")
    super().__delattr__(name)
```

---

## Descriptor Protocol

### 1. `__get__`

```python
class Descriptor:
    def __get__(self, obj, objtype=None):
        return "Getting value"
    
    def __set__(self, obj, value):
        print(f"Setting value: {value}")

class MyClass:
    attr = Descriptor()

obj = MyClass()
print(obj.attr)    # "Getting value"
obj.attr = 42      # "Setting value: 42"
```

### 2. Property Alternative

```python
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
```

### 3. Data Validation

Descriptors enable reusable validation logic.

---

## Symbolic Algebra

### 1. Expression Trees

```python
class Expr:
    def __add__(self, other):
        return Add(self, other)
    
    def __mul__(self, other):
        return Mul(self, other)

class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"({self.left} + {self.right})"

class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"({self.left} * {self.right})"
```

### 2. Build Expressions

```python
class Var(Expr):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

x = Var('x')
y = Var('y')
expr = x + y * 2
print(expr)  # (x + (y * 2))
```

### 3. Domain-Specific Languages

Used by SymPy, TensorFlow, PyTorch.

---

## Best Practices

### 1. `__bool__` Logic

```python
def __bool__(self):
    # Clear, intuitive condition
    return len(self.items) > 0
```

### 2. Context Manager Cleanup

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    # Always cleanup
    self.cleanup()
    # Don't suppress exceptions by default
    return False
```

### 3. Bitwise Semantics

```python
# Use bitwise operators for bit manipulation
# Not for unrelated operations
```

---

## Key Takeaways

- `__bool__` controls truthiness.
- `__call__` makes objects callable.
- `__enter__`/`__exit__` enable `with` statements.
- Bitwise operators: `&`, `|`, `^`, `~`, `<<`, `>>`.
- Use for DSLs and symbolic computation.
- Follow clear, intuitive semantics.
