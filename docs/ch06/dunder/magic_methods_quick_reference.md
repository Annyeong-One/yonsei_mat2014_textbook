# Python Magic Methods Quick Reference

## Most Commonly Used Magic Methods

### Initialization & Representation
| Method | Purpose | Example |
|--------|---------|---------|
| `__init__(self, ...)` | Constructor | `obj = MyClass(args)` |
| `__repr__(self)` | Developer-friendly string | `repr(obj)` |
| `__str__(self)` | User-friendly string | `str(obj)`, `print(obj)` |

### Comparison Operators
| Method | Operator | Example |
|--------|----------|---------|
| `__eq__(self, other)` | `==` | `a == b` |
| `__ne__(self, other)` | `!=` | `a != b` |
| `__lt__(self, other)` | `<` | `a < b` |
| `__le__(self, other)` | `<=` | `a <= b` |
| `__gt__(self, other)` | `>` | `a > b` |
| `__ge__(self, other)` | `>=` | `a >= b` |

### Arithmetic Operators
| Method | Operator | Example |
|--------|----------|---------|
| `__add__(self, other)` | `+` | `a + b` |
| `__sub__(self, other)` | `-` | `a - b` |
| `__mul__(self, other)` | `*` | `a * b` |
| `__truediv__(self, other)` | `/` | `a / b` |
| `__floordiv__(self, other)` | `//` | `a // b` |
| `__mod__(self, other)` | `%` | `a % b` |
| `__pow__(self, other)` | `**` | `a ** b` |

### Reverse Arithmetic (for `other + self`)
| Method | Operator | Example |
|--------|----------|---------|
| `__radd__(self, other)` | `+` | `5 + obj` |
| `__rsub__(self, other)` | `-` | `5 - obj` |
| `__rmul__(self, other)` | `*` | `5 * obj` |

### In-place Operations
| Method | Operator | Example |
|--------|----------|---------|
| `__iadd__(self, other)` | `+=` | `a += b` |
| `__isub__(self, other)` | `-=` | `a -= b` |
| `__imul__(self, other)` | `*=` | `a *= b` |

### Unary Operators
| Method | Operator | Example |
|--------|----------|---------|
| `__neg__(self)` | `-` | `-obj` |
| `__pos__(self)` | `+` | `+obj` |
| `__abs__(self)` | `abs()` | `abs(obj)` |
| `__invert__(self)` | `~` | `~obj` |

### Container Methods
| Method | Purpose | Example |
|--------|---------|---------|
| `__len__(self)` | Length | `len(obj)` |
| `__getitem__(self, key)` | Get item | `obj[key]` |
| `__setitem__(self, key, val)` | Set item | `obj[key] = val` |
| `__delitem__(self, key)` | Delete item | `del obj[key]` |
| `__contains__(self, item)` | Membership | `item in obj` |
| `__iter__(self)` | Iteration | `for x in obj` |
| `__next__(self)` | Next item | `next(obj)` |
| `__reversed__(self)` | Reverse | `reversed(obj)` |

### Type Conversion
| Method | Purpose | Example |
|--------|---------|---------|
| `__int__(self)` | Convert to int | `int(obj)` |
| `__float__(self)` | Convert to float | `float(obj)` |
| `__bool__(self)` | Convert to bool | `bool(obj)`, `if obj:` |
| `__str__(self)` | Convert to string | `str(obj)` |
| `__bytes__(self)` | Convert to bytes | `bytes(obj)` |

### Special Methods
| Method | Purpose | Example |
|--------|---------|---------|
| `__call__(self, ...)` | Make callable | `obj(args)` |
| `__hash__(self)` | Hash value | `hash(obj)`, `set([obj])` |
| `__format__(self, spec)` | String format | `f"{obj:spec}"` |

### Context Managers
| Method | Purpose | Example |
|--------|---------|---------|
| `__enter__(self)` | Enter context | `with obj:` |
| `__exit__(self, ...)` | Exit context | (automatic) |

### Attribute Access
| Method | Purpose | When Called |
|--------|---------|-------------|
| `__getattr__(self, name)` | Get missing attr | `obj.name` (if not found) |
| `__setattr__(self, name, val)` | Set any attr | `obj.name = val` |
| `__delattr__(self, name)` | Delete attr | `del obj.name` |
| `__getattribute__(self, name)` | Get any attr | `obj.name` (always) |

## Quick Tips

### When implementing `__eq__`, also implement `__hash__`
```python
def __eq__(self, other):
    return self.value == other.value

def __hash__(self):
    return hash(self.value)
```

### Return `NotImplemented` for unsupported types
```python
def __add__(self, other):
    if not isinstance(other, MyClass):
        return NotImplemented
    return MyClass(self.value + other.value)
```

### Use `object.__setattr__()` to avoid recursion
```python
def __setattr__(self, name, value):
    # Validate here
    object.__setattr__(self, name, value)
```

### Context manager pattern
```python
def __enter__(self):
    # Setup code
    return self  # or resource

def __exit__(self, exc_type, exc_val, exc_tb):
    # Cleanup code
    return False  # False = propagate exceptions
```

## Common Patterns

### Immutable Class (tuple-like)
Implement: `__init__`, `__repr__`, `__str__`, `__eq__`, `__hash__`, `__getitem__`, `__len__`

### Container Class (list-like)
Implement: `__init__`, `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__iter__`

### Numeric Class
Implement: `__init__`, `__repr__`, `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__neg__`, `__abs__`, `__eq__`, `__lt__`

### Callable Class (function-like)
Implement: `__init__`, `__call__`, `__repr__`

### Context Manager Class
Implement: `__init__`, `__enter__`, `__exit__`

## Remember
- Magic methods should be intuitive - follow the principle of least surprise
- Always document your magic methods
- Test edge cases thoroughly
- Use `super()` when inheriting
- Consider performance implications
