# Pythonic Patterns

Idiomatic Python patterns for clean, efficient, and readable code.

## EAFP vs LBYL

Python favors "Easier to Ask Forgiveness than Permission" (EAFP) over "Look Before You Leap" (LBYL).

### EAFP Style (Pythonic)

```python
# Try the operation, handle exceptions
try:
    value = dictionary[key]
except KeyError:
    value = default

# File operations
try:
    with open('file.txt') as f:
        data = f.read()
except FileNotFoundError:
    data = ""
```

### LBYL Style (Less Pythonic)

```python
# Check before operating
if key in dictionary:
    value = dictionary[key]
else:
    value = default

# File check
if os.path.exists('file.txt'):
    with open('file.txt') as f:
        data = f.read()
```

### When to Use Each

- **EAFP**: When the operation usually succeeds
- **LBYL**: When checking is cheaper than exception handling

---

## Context Managers

Use `with` statements for resource management:

```python
# File handling
with open('file.txt') as f:
    data = f.read()
# File automatically closed

# Multiple resources
with open('in.txt') as src, open('out.txt', 'w') as dst:
    dst.write(src.read())

# Database connections
with connection.cursor() as cursor:
    cursor.execute(query)

# Locks
with threading.Lock():
    shared_resource.modify()
```

---

## Comprehensions

### List Comprehensions

```python
# Pythonic
squares = [x**2 for x in range(10)]
evens = [x for x in numbers if x % 2 == 0]

# With condition
positive = [x for x in data if x > 0]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
```

### Dictionary Comprehensions

```python
# Create dict from lists
pairs = {k: v for k, v in zip(keys, values)}

# Transform dict
upper_dict = {k.upper(): v for k, v in original.items()}

# Filter dict
filtered = {k: v for k, v in data.items() if v > 0}
```

### Set Comprehensions

```python
unique_lengths = {len(word) for word in words}
```

### Generator Expressions

```python
# Memory efficient for large data
total = sum(x**2 for x in range(1000000))

# Lazy evaluation
gen = (expensive(x) for x in data)
```

---

## Common Design Patterns

### Factory Functions

```python
def create_user(name, email, role='user'):
    """Factory function for user creation."""
    return {
        'name': name,
        'email': email,
        'role': role,
        'created_at': datetime.now()
    }

# Usage
admin = create_user('Alice', 'alice@example.com', role='admin')
```

### Builder Pattern

```python
class QueryBuilder:
    def __init__(self):
        self._table = None
        self._columns = ['*']
        self._conditions = []
    
    def table(self, name):
        self._table = name
        return self
    
    def select(self, *columns):
        self._columns = columns
        return self
    
    def where(self, condition):
        self._conditions.append(condition)
        return self
    
    def build(self):
        query = f"SELECT {', '.join(self._columns)} FROM {self._table}"
        if self._conditions:
            query += f" WHERE {' AND '.join(self._conditions)}"
        return query

# Fluent interface
query = (QueryBuilder()
    .table('users')
    .select('name', 'email')
    .where('active = 1')
    .build())
```

### Registry Pattern

```python
_handlers = {}

def register(name):
    """Decorator to register handlers."""
    def decorator(func):
        _handlers[name] = func
        return func
    return decorator

def get_handler(name):
    return _handlers.get(name)

# Usage
@register('csv')
def process_csv(data):
    return parse_csv(data)

@register('json')
def process_json(data):
    return json.loads(data)

# Dispatch
handler = get_handler(file_type)
result = handler(data)
```

---

## Assignment Patterns

### Tuple Unpacking

```python
# Multiple assignment
a, b = 1, 2
x, y, z = point

# Extended unpacking
first, *rest = [1, 2, 3, 4, 5]
head, *middle, tail = data

# Ignore values
_, important, _ = get_values()
first, *_, last = sequence
```

### Swapping

```python
# Pythonic swap (no temp variable)
a, b = b, a

# Multiple swaps
a, b, c = c, a, b
```

### Walrus Operator

```python
# Assign and test in one expression
if (n := len(data)) > 10:
    print(f"Large dataset: {n} items")

# In while loops
while (line := file.readline()):
    process(line)

# In list comprehensions
results = [y for x in data if (y := transform(x)) is not None]
```

### Default Values

```python
# Or pattern for defaults
name = user_input or "Anonymous"
config = options.get('config') or default_config

# Conditional expression
result = value if condition else default
```

---

## Summary

| Pattern | Use Case | Example |
|---------|----------|---------|
| EAFP | Operations that usually succeed | `try/except` |
| Context managers | Resource management | `with open()` |
| Comprehensions | Transform/filter collections | `[x for x in data]` |
| Factory functions | Object creation | `create_user()` |
| Registry | Plugin systems | `@register('name')` |
| Unpacking | Multiple assignment | `a, *rest = data` |
| Walrus | Assign in expressions | `if (n := len(x)):` |

Key principles:
- Prefer EAFP for cleaner code
- Always use context managers for resources
- Use comprehensions for clarity and performance
- Choose patterns that fit your problem
