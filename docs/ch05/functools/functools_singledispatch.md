# functools.singledispatch

`singledispatch` transforms a function into a **single-dispatch generic function**. It dispatches to different implementations based on the type of the **first argument**, providing a clean alternative to `if/elif isinstance()` chains.

```python
from functools import singledispatch
```

---

## Basic Usage

```python
from functools import singledispatch

@singledispatch
def process(data):
    """Default implementation — called when no type matches."""
    raise NotImplementedError(f"Cannot process {type(data).__name__}")

@process.register(list)
def _(data):
    return [x * 2 for x in data]

@process.register(dict)
def _(data):
    return {k: v * 2 for k, v in data.items()}

@process.register(str)
def _(data):
    return data.upper()

print(process([1, 2, 3]))     # [2, 4, 6]
print(process({'a': 1}))      # {'a': 2}
print(process("hello"))       # HELLO
# process(42)                 # NotImplementedError
```

---

## How It Works

1. The `@singledispatch` decorator marks the **base function** (default implementation)
2. `.register(type)` registers specialized implementations for specific types
3. At call time, Python checks the type of the **first argument** and dispatches accordingly

```
process(data) called
    ↓
Check type(data)
    ↓
list  → registered list handler
dict  → registered dict handler
str   → registered str handler
other → default (base) function
```

---

## Registration Methods

### Explicit Type Registration

```python
from functools import singledispatch

@singledispatch
def serialize(obj):
    return str(obj)

@serialize.register(int)
def _(obj):
    return f"int:{obj}"

@serialize.register(float)
def _(obj):
    return f"float:{obj:.2f}"

@serialize.register(list)
def _(obj):
    return f"list[{len(obj)} items]"
```

### Type Hint Registration (Python 3.7+)

```python
from functools import singledispatch

@singledispatch
def serialize(obj):
    return str(obj)

@serialize.register
def _(obj: int):
    return f"int:{obj}"

@serialize.register
def _(obj: float):
    return f"float:{obj:.2f}"

@serialize.register
def _(obj: list):
    return f"list[{len(obj)} items]"
```

### Register Multiple Types

```python
from functools import singledispatch

@singledispatch
def normalize(data):
    raise NotImplementedError()

# Same implementation for multiple types
@normalize.register(int)
@normalize.register(float)
def _(data):
    return float(data) / 100.0

print(normalize(50))    # 0.5
print(normalize(75.0))  # 0.75
```

### Register with Named Functions

```python
from functools import singledispatch

@singledispatch
def format_value(val):
    return str(val)

def format_int(val):
    return f"{val:,}"

def format_float(val):
    return f"{val:.4f}"

# Register named functions explicitly
format_value.register(int, format_int)
format_value.register(float, format_float)

print(format_value(1000000))  # 1,000,000
print(format_value(3.14))     # 3.1400
```

---

## singledispatch vs if/elif isinstance

### Before: isinstance Chains

```python
def process(data):
    if isinstance(data, list):
        return [x * 2 for x in data]
    elif isinstance(data, dict):
        return {k: v * 2 for k, v in data.items()}
    elif isinstance(data, str):
        return data.upper()
    elif isinstance(data, (int, float)):
        return data * 2
    else:
        raise NotImplementedError(f"Cannot process {type(data)}")
```

### After: singledispatch

```python
from functools import singledispatch

@singledispatch
def process(data):
    raise NotImplementedError(f"Cannot process {type(data).__name__}")

@process.register(list)
def _(data):
    return [x * 2 for x in data]

@process.register(dict)
def _(data):
    return {k: v * 2 for k, v in data.items()}

@process.register(str)
def _(data):
    return data.upper()

@process.register(int)
@process.register(float)
def _(data):
    return data * 2
```

### Comparison

| Aspect | `isinstance` chains | `singledispatch` |
|--------|-------------------|------------------|
| Extensibility | Must modify original function | Register new types anywhere |
| Open/closed | Closed — editing required | Open — extend without editing |
| Readability | All logic in one place | Implementations separated |
| New types | Add more `elif` | Call `.register()` |
| Discovery | Read the whole function | Check `.registry` |

---

## Practical Examples

### Data Serialization

```python
from functools import singledispatch
from datetime import datetime, date
from decimal import Decimal

@singledispatch
def to_json(obj):
    """Convert Python objects to JSON-serializable form."""
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

@to_json.register(str)
@to_json.register(int)
@to_json.register(float)
@to_json.register(bool)
def _(obj):
    return obj  # Already JSON-compatible

@to_json.register(datetime)
def _(obj):
    return obj.isoformat()

@to_json.register(date)
def _(obj):
    return obj.isoformat()

@to_json.register(Decimal)
def _(obj):
    return float(obj)

@to_json.register(list)
@to_json.register(tuple)
def _(obj):
    return [to_json(item) for item in obj]

@to_json.register(dict)
def _(obj):
    return {str(k): to_json(v) for k, v in obj.items()}

# Usage
data = {
    'name': 'Alice',
    'balance': Decimal('1234.56'),
    'created': datetime(2024, 1, 15),
    'scores': [95, 87, 92],
}
print(to_json(data))
# {'name': 'Alice', 'balance': 1234.56, 'created': '2024-01-15T00:00:00', 'scores': [95, 87, 92]}
```

### Pretty Printing

```python
from functools import singledispatch

@singledispatch
def pprint(obj, indent=0):
    print(" " * indent + repr(obj))

@pprint.register(dict)
def _(obj, indent=0):
    prefix = " " * indent
    print(f"{prefix}{{")
    for k, v in obj.items():
        print(f"{prefix}  {k!r}:", end=" ")
        pprint(v, indent + 4)
    print(f"{prefix}}}")

@pprint.register(list)
def _(obj, indent=0):
    prefix = " " * indent
    print(f"{prefix}[")
    for item in obj:
        pprint(item, indent + 2)
    print(f"{prefix}]")

pprint({'name': 'Alice', 'scores': [95, 87], 'active': True})
```

### Input Validation

```python
from functools import singledispatch

@singledispatch
def validate(value, field_name="value"):
    raise TypeError(f"Cannot validate {type(value).__name__}")

@validate.register(str)
def _(value, field_name="value"):
    if not value.strip():
        raise ValueError(f"{field_name} cannot be empty")
    return value.strip()

@validate.register(int)
@validate.register(float)
def _(value, field_name="value"):
    if value < 0:
        raise ValueError(f"{field_name} must be non-negative")
    return value

@validate.register(list)
def _(value, field_name="value"):
    if len(value) == 0:
        raise ValueError(f"{field_name} cannot be empty")
    return value

print(validate("  hello  "))  # 'hello'
print(validate(42))           # 42
# validate("")                # ValueError: value cannot be empty
# validate(-5)                # ValueError: value must be non-negative
```

---

## Inspecting the Registry

```python
from functools import singledispatch

@singledispatch
def process(data):
    pass

@process.register(int)
def _(data): pass

@process.register(str)
def _(data): pass

# View all registered types
print(process.registry)
# {<class 'object'>: <function process>, <class 'int'>: ..., <class 'str'>: ...}

print(process.registry.keys())
# dict_keys([<class 'object'>, <class 'int'>, <class 'str'>])

# Check which implementation handles a type
print(process.dispatch(int))    # The int handler
print(process.dispatch(float))  # Falls back to default (object)
```

---

## Subclass Dispatch

`singledispatch` respects inheritance — a registered base class handler catches subclasses:

```python
from functools import singledispatch
from collections import OrderedDict

@singledispatch
def describe(obj):
    return f"Unknown: {type(obj).__name__}"

@describe.register(dict)
def _(obj):
    return f"Dict with {len(obj)} keys"

# OrderedDict is a subclass of dict — dispatches to dict handler
print(describe(OrderedDict(a=1, b=2)))  # Dict with 2 keys

# Register more specific handler to override
@describe.register(OrderedDict)
def _(obj):
    return f"OrderedDict with {len(obj)} keys (ordered)"

print(describe(OrderedDict(a=1, b=2)))  # OrderedDict with 2 keys (ordered)
```

The most specific registered type wins (MRO-based resolution).

---

## singledispatchmethod (Python 3.8+)

For methods inside classes, use `singledispatchmethod`:

```python
from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    def format(self, data):
        raise NotImplementedError(f"Cannot format {type(data).__name__}")

    @format.register(int)
    def _(self, data):
        return f"{data:,}"

    @format.register(float)
    def _(self, data):
        return f"{data:.2f}"

    @format.register(str)
    def _(self, data):
        return data.title()

f = Formatter()
print(f.format(1000000))   # 1,000,000
print(f.format(3.14159))   # 3.14
print(f.format("hello"))   # Hello
```

### Combining with classmethod or staticmethod

```python
from functools import singledispatchmethod

class Parser:
    @singledispatchmethod
    @classmethod
    def parse(cls, data):
        raise NotImplementedError()

    @parse.register(str)
    @classmethod
    def _(cls, data):
        return data.split(',')

    @parse.register(bytes)
    @classmethod
    def _(cls, data):
        return data.decode().split(',')

print(Parser.parse("a,b,c"))       # ['a', 'b', 'c']
print(Parser.parse(b"a,b,c"))      # ['a', 'b', 'c']
```

**Note**: `@singledispatchmethod` must be the **outermost** decorator.

---

## Abstract Base Class Registration

You can register against ABCs for broader type matching:

```python
from functools import singledispatch
from collections.abc import Sequence, Mapping, Set

@singledispatch
def summarize(collection):
    return f"Unknown collection: {type(collection).__name__}"

@summarize.register(Sequence)
def _(collection):
    return f"Sequence with {len(collection)} items"

@summarize.register(Mapping)
def _(collection):
    return f"Mapping with {len(collection)} keys"

@summarize.register(Set)
def _(collection):
    return f"Set with {len(collection)} elements"

print(summarize([1, 2, 3]))       # Sequence with 3 items
print(summarize((1, 2)))          # Sequence with 2 items
print(summarize({'a': 1}))        # Mapping with 1 keys
print(summarize(frozenset({1})))  # Set with 1 elements
```

---

## Limitations

### First Argument Only

`singledispatch` only considers the **first** argument's type:

```python
@singledispatch
def combine(a, b):
    pass

# Cannot dispatch on type of 'b'
# Cannot dispatch on combination of (type(a), type(b))
```

For multi-argument dispatch, consider third-party libraries like `multipledispatch` or `plum`.

### No Union Type Support (before 3.11)

```python
# Python 3.11+
from functools import singledispatch

@singledispatch
def process(data):
    pass

@process.register(int | float)  # Works in 3.11+
def _(data):
    return data * 2

# Before 3.11: stack decorators
@process.register(int)
@process.register(float)
def _(data):
    return data * 2
```

---

## Summary

| Feature | Details |
|---------|---------|
| Import | `from functools import singledispatch` |
| Dispatches on | Type of the **first** argument |
| Registration | `.register(type)` decorator or type hints |
| Inheritance | Respects MRO — most specific type wins |
| Methods | Use `singledispatchmethod` (Python 3.8+) |
| Inspection | `.registry`, `.dispatch(type)` |

**Key Takeaways**:

- `singledispatch` replaces `if/elif isinstance()` chains with extensible type dispatch
- Register implementations with `@func.register(type)` or type hints
- The default (base) function handles unregistered types
- Subclass dispatch works automatically via MRO
- Use `singledispatchmethod` for methods inside classes
- Only dispatches on the first argument — use third-party tools for multi-dispatch
- Register against ABCs (`Sequence`, `Mapping`) for broad type matching
