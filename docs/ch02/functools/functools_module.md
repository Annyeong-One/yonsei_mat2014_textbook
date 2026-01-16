# functools Module

The `functools` module provides higher-order functions and operations on callable objects. It's essential for functional programming patterns in Python.

```python
import functools
# or
from functools import partial, wraps, lru_cache, reduce
```

---

## partial — Partial Function Application

`partial` freezes some arguments of a function, creating a new function with fewer parameters.

### Basic Usage

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

# Create specialized functions
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))    # 125

# Freeze positional argument
double = partial(pow, 2)  # pow(2, x)
print(double(8))  # 256 (2^8)
```

### Practical Examples

```python
from functools import partial

# Customize print
debug_print = partial(print, "[DEBUG]", end="\n\n")
debug_print("Starting process")  # [DEBUG] Starting process

# Configure API calls
import requests
api_get = partial(requests.get, headers={"Authorization": "Bearer TOKEN"})

# Sorting with fixed key
from operator import itemgetter
sort_by_name = partial(sorted, key=itemgetter('name'))
users = [{'name': 'Bob'}, {'name': 'Alice'}]
print(sort_by_name(users))  # [{'name': 'Alice'}, {'name': 'Bob'}]
```

### partial vs lambda

```python
# These are equivalent:
f1 = partial(pow, 2)
f2 = lambda x: pow(2, x)

# partial advantages:
# - More readable
# - Preserves function metadata
# - Slightly faster
# - Shows frozen args: f1.func, f1.args, f1.keywords
```

---

## wraps — Preserve Function Metadata

When creating decorators, `wraps` preserves the original function's metadata.

### The Problem Without wraps

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Return a greeting."""
    return f"Hello, {name}"

print(greet.__name__)  # 'wrapper' — Wrong!
print(greet.__doc__)   # 'Wrapper docstring' — Wrong!
```

### The Solution With wraps

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves func's metadata
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Return a greeting."""
    return f"Hello, {name}"

print(greet.__name__)  # 'greet' — Correct!
print(greet.__doc__)   # 'Return a greeting.' — Correct!
```

### Complete Decorator Template

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before
        result = func(*args, **kwargs)
        # After
        return result
    return wrapper

# Decorator with arguments
def decorator_with_args(arg1, arg2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use arg1, arg2 here
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### What wraps Preserves

```python
# wraps copies these attributes:
# __name__    - function name
# __doc__     - docstring
# __module__  - module name
# __qualname__ - qualified name
# __annotations__ - type hints
# __dict__    - function attributes

# Also sets:
# __wrapped__ - reference to original function
```

---

## lru_cache — Memoization

`lru_cache` caches function results for repeated calls with the same arguments.

### Basic Usage

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))  # Instant! Without cache, this would be impossibly slow

# Check cache stats
print(fibonacci.cache_info())
# CacheInfo(hits=98, misses=101, maxsize=128, currsize=101)

# Clear cache
fibonacci.cache_clear()
```

### maxsize Options

```python
# maxsize=128 (default) - LRU eviction when full
@lru_cache(maxsize=128)
def func1(x): pass

# maxsize=None - unlimited cache, never evicts
@lru_cache(maxsize=None)
def func2(x): pass

# Python 3.9+ shorthand for unlimited cache
@cache  # Same as @lru_cache(maxsize=None)
def func3(x): pass
```

### Requirements

Arguments must be **hashable** (immutable):

```python
@lru_cache
def process(data):
    return sum(data)

# Works with tuples
process((1, 2, 3))  # OK

# Fails with lists
process([1, 2, 3])  # TypeError: unhashable type: 'list'

# Solution: convert to tuple
process(tuple([1, 2, 3]))  # OK
```

### Practical Examples

```python
from functools import lru_cache

# Expensive computation
@lru_cache(maxsize=1000)
def expensive_query(user_id, date):
    # Simulate database query
    return fetch_from_database(user_id, date)

# Recursive algorithms
@lru_cache(maxsize=None)
def edit_distance(s1, s2):
    if not s1: return len(s2)
    if not s2: return len(s1)
    if s1[0] == s2[0]:
        return edit_distance(s1[1:], s2[1:])
    return 1 + min(
        edit_distance(s1[1:], s2),
        edit_distance(s1, s2[1:]),
        edit_distance(s1[1:], s2[1:])
    )
```

### typed Parameter (Python 3.3+)

```python
@lru_cache(maxsize=128, typed=True)
def func(x):
    return x * 2

# With typed=True, these are cached separately:
func(3)    # int
func(3.0)  # float

# With typed=False (default), they share cache entry
```

---

## cache — Simple Memoization (Python 3.9+)

`cache` is a simpler alias for `@lru_cache(maxsize=None)`:

```python
from functools import cache

@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1

print(factorial(10))  # 3628800
```

---

## reduce — Cumulative Operations

`reduce` applies a function cumulatively to items, reducing to a single value.

### Basic Usage

```python
from functools import reduce

# Sum of list
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15

# How it works:
# Step 1: acc=1, x=2 -> 3
# Step 2: acc=3, x=3 -> 6
# Step 3: acc=6, x=4 -> 10
# Step 4: acc=10, x=5 -> 15
```

### With Initial Value

```python
from functools import reduce

# With initializer
result = reduce(lambda acc, x: acc + x, [1, 2, 3], 10)
print(result)  # 16 (10 + 1 + 2 + 3)

# Useful for empty sequences
result = reduce(lambda acc, x: acc + x, [], 0)
print(result)  # 0 (without initializer, this would raise TypeError)
```

### Practical Examples

```python
from functools import reduce
import operator

# Product of all numbers
numbers = [1, 2, 3, 4, 5]
product = reduce(operator.mul, numbers)
print(product)  # 120

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda acc, x: acc + x, nested)
print(flat)  # [1, 2, 3, 4, 5, 6]

# Find maximum
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)  # 9

# Compose functions
def compose(*funcs):
    return reduce(lambda f, g: lambda x: f(g(x)), funcs)

add_one = lambda x: x + 1
double = lambda x: x * 2
square = lambda x: x ** 2

pipeline = compose(square, double, add_one)  # square(double(add_one(x)))
print(pipeline(3))  # 64 = (3+1)*2)^2
```

### reduce vs Built-ins

```python
# Often, built-ins are clearer:
numbers = [1, 2, 3, 4, 5]

# reduce vs sum
reduce(lambda a, b: a + b, numbers)  # 15
sum(numbers)                          # 15 — clearer!

# reduce vs max
reduce(lambda a, b: a if a > b else b, numbers)  # 5
max(numbers)                                       # 5 — clearer!

# reduce vs any/all
reduce(lambda a, b: a or b, [False, True, False])  # True
any([False, True, False])                           # True — clearer!

# Use reduce for complex accumulations without built-in equivalents
```

---

## total_ordering — Complete Comparison Methods

Define `__eq__` and one other comparison method; `total_ordering` fills in the rest.

```python
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor
    
    def __eq__(self, other):
        return (self.major, self.minor) == (other.major, other.minor)
    
    def __lt__(self, other):
        return (self.major, self.minor) < (other.major, other.minor)

# Now all comparisons work:
v1 = Version(1, 0)
v2 = Version(2, 0)

print(v1 < v2)   # True (defined)
print(v1 <= v2)  # True (auto-generated)
print(v1 > v2)   # False (auto-generated)
print(v1 >= v2)  # False (auto-generated)
print(v1 == v2)  # False (defined)
print(v1 != v2)  # True (auto-generated)
```

---

## cached_property — Lazy Attribute (Python 3.8+)

Computes property once and caches the result.

```python
from functools import cached_property

class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def processed(self):
        print("Processing...")  # Only prints once
        return [x * 2 for x in self.data]

dp = DataProcessor([1, 2, 3])
print(dp.processed)  # Processing... [2, 4, 6]
print(dp.processed)  # [2, 4, 6] — cached, no "Processing..."
```

### cached_property vs lru_cache

```python
# cached_property: for object attributes
class Foo:
    @cached_property
    def bar(self):
        return expensive_computation()

# lru_cache: for function calls with arguments
@lru_cache
def compute(x, y):
    return expensive_computation(x, y)
```

---

## singledispatch — Function Overloading

Implement function overloading based on the first argument's type.

```python
from functools import singledispatch

@singledispatch
def process(data):
    """Default implementation"""
    raise NotImplementedError(f"Cannot process {type(data)}")

@process.register(list)
def _(data):
    return [x * 2 for x in data]

@process.register(dict)
def _(data):
    return {k: v * 2 for k, v in data.items()}

@process.register(str)
def _(data):
    return data.upper()

print(process([1, 2, 3]))       # [2, 4, 6]
print(process({'a': 1}))        # {'a': 2}
print(process("hello"))         # HELLO
# process(42)                   # NotImplementedError
```

### Type Hints Registration (Python 3.7+)

```python
from functools import singledispatch

@singledispatch
def process(data):
    raise NotImplementedError()

@process.register
def _(data: list):
    return sum(data)

@process.register
def _(data: str):
    return len(data)
```

---

## cmp_to_key — Legacy Comparison

Convert old-style comparison function to key function for sorting.

```python
from functools import cmp_to_key

# Old-style comparison function
def compare(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0

# Use with sorted
numbers = [3, 1, 4, 1, 5]
sorted(numbers, key=cmp_to_key(compare))  # [1, 1, 3, 4, 5]

# Practical: custom sorting
def compare_versions(v1, v2):
    parts1 = list(map(int, v1.split('.')))
    parts2 = list(map(int, v2.split('.')))
    if parts1 < parts2:
        return -1
    elif parts1 > parts2:
        return 1
    return 0

versions = ['1.2', '1.10', '1.1', '2.0']
sorted(versions, key=cmp_to_key(compare_versions))
# ['1.1', '1.2', '1.10', '2.0']
```

---

## Summary

| Function | Purpose | Use Case |
|----------|---------|----------|
| `partial` | Freeze function arguments | Create specialized functions |
| `wraps` | Preserve function metadata | Writing decorators |
| `lru_cache` | Memoize function results | Cache expensive computations |
| `cache` | Simple memoization (3.9+) | Unlimited cache |
| `reduce` | Cumulative operation | Fold sequence to single value |
| `total_ordering` | Complete comparison ops | Define all comparisons from two |
| `cached_property` | Lazy cached attribute (3.8+) | Expensive property computation |
| `singledispatch` | Type-based overloading | Different implementations per type |
| `cmp_to_key` | Convert comparison function | Legacy sorting compatibility |

**Key Points**:

- `partial` creates cleaner code than lambdas for freezing arguments
- Always use `@wraps` when writing decorators
- `lru_cache` dramatically speeds up recursive algorithms
- `reduce` is powerful but often less clear than built-in alternatives
- `singledispatch` enables clean type-based dispatch without if/elif chains
