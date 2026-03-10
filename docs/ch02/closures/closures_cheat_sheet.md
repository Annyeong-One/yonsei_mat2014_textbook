# Python Closures - Quick Reference Cheat Sheet


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

A **closure** is a function that:
1. Is defined inside another function (nested)
2. References variables from the outer function's scope
3. Can be returned and called later, still remembering those variables

```python
def outer(x):
    def inner(y):
        return x + y  # inner "closes over" x
    return inner

add_5 = outer(5)  # add_5 is a closure
print(add_5(3))   # 8
```

## Basic Template

```python
def outer_function(outer_var):
    # outer_var is captured by the closure
    
    def inner_function(inner_var):
        # Can access both outer_var and inner_var
        return outer_var + inner_var
    
    return inner_function  # Return without calling ()

# Create closure
my_closure = outer_function(10)
result = my_closure(5)  # 15
```

## The nonlocal Keyword

Use `nonlocal` to modify variables from the enclosing scope:

```python
def make_counter():
    count = 0
    
    def increment():
        nonlocal count  # Required to modify count
        count += 1
        return count
    
    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
```

**Without nonlocal:**
- Can READ outer variables ✓
- Cannot MODIFY outer variables ✗ (creates local variable instead)

**With nonlocal:**
- Can both READ and MODIFY outer variables ✓

## Common Patterns

### 1. Factory Functions
Create specialized functions:

```python
def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

times_2 = make_multiplier(2)
times_10 = make_multiplier(10)
```

### 2. Data Encapsulation (Private Variables)
Hide implementation details:

```python
def make_account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    
    def withdraw(amount):
        nonlocal balance
        balance -= amount
        return balance
    
    def get_balance():
        return balance
    
    return {'deposit': deposit, 'withdraw': withdraw, 'balance': get_balance}
```

### 3. Configuration Functions
Store settings:

```python
def make_formatter(prefix, suffix):
    def format(text):
        return f"{prefix}{text}{suffix}"
    return format

html_bold = make_formatter("<b>", "</b>")
html_italic = make_formatter("<i>", "</i>")
```

### 4. Callbacks with State
Event handlers that remember:

```python
def make_click_handler(element_id):
    click_count = 0
    
    def handle_click():
        nonlocal click_count
        click_count += 1
        print(f"{element_id}: {click_count} clicks")
    
    return handle_click
```

### 5. Memoization/Caching
Cache expensive results:

```python
def make_memoized(func):
    cache = {}
    
    def memoized(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return memoized
```

### 6. Counters and Accumulators
Maintain state between calls:

```python
def make_counter(start=0):
    count = start
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter
```

## LEGB Rule (Variable Lookup Order)

Python searches for variables in this order:
1. **L**ocal: Inside current function
2. **E**nclosing: In enclosing functions (closures!)
3. **G**lobal: Module level
4. **B**uilt-in: Python built-ins

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # Prints "local"
    
    inner()
```

## Multiple Closures Sharing State

```python
def make_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def get():
        return count
    
    return increment, decrement, get

inc, dec, get = make_counter()
```

## Common Pitfall: Closures in Loops

### ❌ WRONG:
```python
def create_funcs():
    funcs = []
    for i in range(3):
        funcs.append(lambda x: x * i)
    return funcs

f = create_funcs()
print(f[0](2))  # Expected: 0, Got: 4
print(f[1](2))  # Expected: 2, Got: 4
print(f[2](2))  # Expected: 4, Got: 4
# All closures share the same 'i' which is 2 after loop!
```

### ✅ SOLUTION 1: Default Argument
```python
def create_funcs():
    funcs = []
    for i in range(3):
        funcs.append(lambda x, i=i: x * i)  # Capture current i
    return funcs
```

### ✅ SOLUTION 2: Factory Function
```python
def make_multiplier(i):
    return lambda x: x * i

def create_funcs():
    return [make_multiplier(i) for i in range(3)]
```

## Closures vs Classes

### Use Closure When:
- ✓ Simple, single-method behavior
- ✓ Private data without class overhead
- ✓ Functional programming style
- ✓ Quick factory functions

### Use Class When:
- ✓ Multiple related methods
- ✓ Complex state management
- ✓ Need inheritance
- ✓ Need special methods (`__str__`, `__repr__`, etc.)

### Example Comparison:

**Closure:**
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```

**Class:**
```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
```

## Inspecting Closures

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(5)

# See captured variables
print(f.__closure__)          # (<cell at 0x...: int object at 0x...>,)
print(f.__code__.co_freevars) # ('x',)

# Get value
print(f.__closure__[0].cell_contents)  # 5
```

## Decorators (Built on Closures)

Decorators are just closures used to wrap functions:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")
```

## Partial Application

Create specialized functions from general ones:

```python
def partial(func, *fixed_args):
    def wrapper(*args):
        return func(*fixed_args, *args)
    return wrapper

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
```

## Function Composition

Combine functions:

```python
def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed

def add_10(x):
    return x + 10

def multiply_2(x):
    return x * 2

add_then_multiply = compose(multiply_2, add_10)
print(add_then_multiply(5))  # 30: (5 + 10) * 2
```

## Best Practices

### ✅ DO:
- Keep closures simple and focused
- Use descriptive names for captured variables
- Document what the closure captures
- Use `nonlocal` only when necessary
- Consider readability

### ❌ DON'T:
- Create deeply nested closures (2-3 levels max)
- Capture mutable objects without care
- Use closures for complex state (use classes)
- Forget about the loop variable pitfall
- Sacrifice clarity for cleverness

## Quick Reference Table

| Feature | Syntax | Use Case |
|---------|--------|----------|
| Basic closure | `def outer(): def inner(): pass` | Remember variables |
| Modify outer var | `nonlocal var` | Change enclosing scope |
| Multiple returns | `return f1, f2, f3` | Multiple closures |
| Private data | Return dict of functions | Encapsulation |
| Factory | `make_thing(config)` | Specialized functions |
| Decorator | `def deco(func): def wrap(): pass` | Wrap functions |

## Common Use Cases Summary

```python
# 1. Counter
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

# 2. Adder
def make_adder(n):
    return lambda x: x + n

# 3. Formatter
def make_formatter(pre, suf):
    return lambda text: f"{pre}{text}{suf}"

# 4. Range checker
def make_range_checker(min, max):
    return lambda x: min <= x <= max

# 5. Cache
def make_cached(func):
    cache = {}
    def cached(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return cached
```

## Memory Tip

**Closures = Functions + Their Environment**

Think of closures as a "backpack" that the function carries around, containing all the variables it needs from its birthplace.

---

**Key Insight**: Closures are not just about nested functions - they're about functions that **remember their environment**. Master this concept, and decorators, callbacks, and functional programming patterns become much easier!
