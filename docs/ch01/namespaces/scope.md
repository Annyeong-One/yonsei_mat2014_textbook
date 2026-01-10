# Global vs Local Variables

## Introduction

Understanding the distinction between **global** and **local** variables is fundamental to writing correct Python programs. This distinction affects:
- Where variables can be accessed
- How long variables exist
- How to modify variables from different scopes
- Code organization and maintainability

This chapter provides a comprehensive guide to global and local variables, their differences, when to use each, and best practices for managing scope in Python programs.

## Local Variables

### What are Local Variables?

**Local variables** are variables defined inside a function. They:
- Exist only within the function
- Are created when the function is called
- Are destroyed when the function returns
- Cannot be accessed from outside the function

### Basic Local Variables

```python
def calculate_area(length, width):
    area = length * width  # Local variable
    return area

result = calculate_area(5, 3)
print(result)  # 15
# print(area)  # NameError: name 'area' is not defined
```

### Function Parameters are Local

```python
def greet(name, age):  # name and age are local
    message = f"Hello {name}, you are {age} years old"
    print(message)

greet("Alice", 25)
# print(name)  # NameError: name and age don't exist here
```

### Lifetime of Local Variables

```python
def counter():
    count = 0  # Created when function is called
    count += 1
    print(count)
    # count is destroyed when function returns

counter()  # Output: 1
counter()  # Output: 1 (new count created each time)
counter()  # Output: 1
```

### Multiple Local Scopes

Each function call creates its own local scope:

```python
def process(x):
    result = x * 2  # Local to this call
    return result

a = process(5)  # result = 10 (then destroyed)
b = process(3)  # Different result = 6 (then destroyed)

print(a, b)  # 10 6
```

### Nested Functions Have Separate Local Scopes

```python
def outer():
    x = "outer local"  # Local to outer()
    
    def inner():
        x = "inner local"  # Local to inner() (different variable)
        print(f"Inner: {x}")
    
    inner()
    print(f"Outer: {x}")

outer()
# Output:
# Inner: inner local
# Outer: outer local
```

## Global Variables

### What are Global Variables?

**Global variables** are variables defined at the module level (outside all functions). They:
- Exist for the entire program execution
- Are accessible from anywhere in the module
- Persist between function calls
- Can be read by functions without special keywords

### Basic Global Variables

```python
# Global variables
name = "Alice"
age = 25

def display_info():
    # Can read global variables
    print(f"Name: {name}")
    print(f"Age: {age}")

display_info()
# Output:
# Name: Alice
# Age: 25
```

### Lifetime of Global Variables

```python
counter = 0  # Created when module loads

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1

increment()
print(counter)  # 2

increment()
print(counter)  # 3
# counter persists between calls
```

### Reading Global Variables

Functions can read global variables without any special keywords:

```python
PI = 3.14159
MAX_SIZE = 100

def calculate_circle_area(radius):
    # Reading PI (no global keyword needed)
    return PI * radius ** 2

def check_size(value):
    # Reading MAX_SIZE (no global keyword needed)
    return value <= MAX_SIZE

print(calculate_circle_area(5))  # Uses PI
print(check_size(50))            # Uses MAX_SIZE
```

## Modifying Variables

### The Key Difference

This is where local and global variables behave very differently:

```python
x = 10  # Global

def try_modify():
    x = 20  # Creates NEW local variable (doesn't modify global)
    print(f"Inside function: {x}")

try_modify()
print(f"Outside function: {x}")

# Output:
# Inside function: 20
# Outside function: 10 (unchanged!)
```

### The global Keyword

To modify a global variable from inside a function, use the `global` keyword:

```python
count = 0  # Global

def increment():
    global count  # Declare intent to modify global
    count += 1

print(f"Before: {count}")  # 0
increment()
print(f"After: {count}")   # 1
```

### Why global is Needed

```python
x = 5

def buggy_function():
    # Python sees x = ..., so treats x as local
    # But we try to read x first!
    # x = x + 1  # UnboundLocalError!
    pass

def correct_function():
    global x  # Now Python knows we mean the global x
    x = x + 1

correct_function()
print(x)  # 6
```

### Multiple Global Variables

```python
a = 1
b = 2
c = 3

def modify_all():
    global a, b, c  # Declare all three
    a = 10
    b = 20
    c = 30

modify_all()
print(a, b, c)  # 10 20 30
```

## Local vs Global: Direct Comparison

### Side-by-Side Example

```python
# Global scope
global_var = "I'm global"

def demonstrate_scope():
    # Local scope
    local_var = "I'm local"
    
    print(f"Inside function:")
    print(f"  Local: {local_var}")   # Can access local
    print(f"  Global: {global_var}")  # Can access global

demonstrate_scope()

print(f"\nOutside function:")
print(f"  Global: {global_var}")  # Can access global
# print(f"  Local: {local_var}")  # NameError! Can't access local
```

### Comparison Table

| Feature | Local Variables | Global Variables |
|---------|----------------|------------------|
| **Defined** | Inside functions | Outside all functions |
| **Lifetime** | Function call duration | Entire program |
| **Accessibility** | Only within function | Anywhere in module |
| **Creation** | When function called | When module loads |
| **Destruction** | When function returns | When program ends |
| **Modification** | Direct | Requires `global` keyword |
| **Memory** | Stack | Heap |
| **Best for** | Temporary computation | Configuration, shared state |

## Shadowing: When Local Hides Global

### Basic Shadowing

When a local variable has the same name as a global variable, the local "shadows" (hides) the global:

```python
x = "global"

def shadow_demo():
    x = "local"  # Shadows global x
    print(x)     # Prints local x

shadow_demo()  # Output: local
print(x)       # Output: global (unchanged)
```

### Intentional vs Accidental Shadowing

```python
# Configuration constant
DEBUG = True

def process_data(data):
    # Accidentally shadows global DEBUG
    DEBUG = False  # Oops! Local variable, not the global
    if DEBUG:
        print("Debugging...")  # This won't run!

process_data([1, 2, 3])
print(DEBUG)  # Still True (global unchanged)
```

### Avoiding Shadowing

```python
# Use different names
DEBUG = True  # Global

def process_data(data, debug_mode=None):
    # Use different name for local
    if debug_mode is None:
        debug_mode = DEBUG  # Read from global
    
    if debug_mode:
        print("Debugging...")
```

## Common Patterns and Use Cases

### Pattern 1: Configuration Variables

```python
# Global configuration
DATABASE_URL = "localhost:5432"
MAX_CONNECTIONS = 100
TIMEOUT = 30

def connect_to_database():
    # Read configuration
    print(f"Connecting to {DATABASE_URL}")
    print(f"Max connections: {MAX_CONNECTIONS}")
    print(f"Timeout: {TIMEOUT}")
```

### Pattern 2: State Management

```python
# Global state (use sparingly!)
user_logged_in = False
current_user = None

def login(username):
    global user_logged_in, current_user
    # Authenticate user...
    user_logged_in = True
    current_user = username

def logout():
    global user_logged_in, current_user
    user_logged_in = False
    current_user = None

def get_current_user():
    return current_user if user_logged_in else None
```

### Pattern 3: Counters and Accumulators

```python
# Global counter
request_count = 0

def handle_request():
    global request_count
    request_count += 1
    print(f"Request #{request_count}")

handle_request()  # Request #1
handle_request()  # Request #2
handle_request()  # Request #3
```

### Pattern 4: Temporary Computation

```python
def calculate_statistics(numbers):
    # All local - temporary computation
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)
    
    return {
        'average': average,
        'max': maximum,
        'min': minimum
    }

result = calculate_statistics([1, 2, 3, 4, 5])
# total, count, average, etc. no longer exist
```

## Mutable Objects: A Special Case

### Modifying Mutable Global Objects

```python
# Global list (mutable)
tasks = []

def add_task(task):
    # Can modify the list object without global keyword
    tasks.append(task)
    print(f"Added: {task}")

def clear_tasks():
    # But reassigning requires global
    global tasks
    tasks = []  # Reassignment needs global

add_task("Buy groceries")
add_task("Write code")
print(tasks)  # ['Buy groceries', 'Write code']

clear_tasks()
print(tasks)  # []
```

### Why This Works

```python
# Modifying vs Reassigning

data = [1, 2, 3]  # Global

def modify_list():
    # Modifying the list object (no global needed)
    data.append(4)  # Calls method on existing object

def reassign_list():
    # Reassigning the variable (global needed)
    # data = [5, 6, 7]  # Would create local variable!
    global data
    data = [5, 6, 7]  # Reassigns global variable

modify_list()
print(data)  # [1, 2, 3, 4]

reassign_list()
print(data)  # [5, 6, 7]
```

### Dictionary Example

```python
config = {'debug': False, 'verbose': False}  # Global

def enable_debug():
    # Modifying dictionary (no global needed)
    config['debug'] = True

def reset_config():
    # Reassigning dictionary (global needed)
    global config
    config = {}

enable_debug()
print(config)  # {'debug': True, 'verbose': False}
```

## Best Practices

### 1. Minimize Global Variables

```python
# Poor - heavy reliance on globals
total = 0
count = 0

def add_number(n):
    global total, count
    total += n
    count += 1

def get_average():
    return total / count if count > 0 else 0

# Better - use class or pass parameters
class Statistics:
    def __init__(self):
        self.total = 0
        self.count = 0
    
    def add_number(self, n):
        self.total += n
        self.count += 1
    
    def get_average(self):
        return self.total / self.count if self.count > 0 else 0
```

### 2. Use Constants for Global Configuration

```python
# Good - uppercase for constants
API_KEY = "your-api-key"
MAX_RETRIES = 3
TIMEOUT = 30

def make_request():
    # Read configuration (no modification)
    if retry_count < MAX_RETRIES:
        # Make request with TIMEOUT
        pass
```

### 3. Use Function Parameters Instead of Globals

```python
# Poor
threshold = 100

def filter_values(values):
    return [v for v in values if v > threshold]

# Better
def filter_values(values, threshold):
    return [v for v in values if v > threshold]

result = filter_values([50, 150, 200], 100)
```

### 4. Return Values Instead of Modifying Globals

```python
# Poor
result = 0

def calculate(x, y):
    global result
    result = x + y

# Better
def calculate(x, y):
    return x + y

result = calculate(5, 3)
```

### 5. Use Descriptive Names

```python
# Poor - unclear scope
x = 10
y = 20

def process():
    z = x + y
    return z

# Better - clear naming
CONFIG_MAX_SIZE = 10
CONFIG_MIN_SIZE = 20

def process_data():
    data_size = CONFIG_MAX_SIZE + CONFIG_MIN_SIZE
    return data_size
```

### 6. Document Global Dependencies

```python
# Global state used by this module
DATABASE_CONNECTION = None
CACHE = {}

def init_database(connection_string):
    """
    Initialize database connection.
    
    Modifies global: DATABASE_CONNECTION
    """
    global DATABASE_CONNECTION
    DATABASE_CONNECTION = create_connection(connection_string)
```

## Common Pitfalls

### 1. UnboundLocalError

```python
count = 0

def increment():
    # Trying to read before assignment
    # count = count + 1  # UnboundLocalError!
    pass

# Fix: Use global
def increment_fixed():
    global count
    count = count + 1
```

### 2. Forgetting global Keyword

```python
total = 0

def add_to_total(value):
    # Creates local total instead of modifying global
    total = total + value  # UnboundLocalError!

# Fix
def add_to_total_fixed(value):
    global total
    total = total + value
```

### 3. Namespace Pollution

```python
# Poor - cluttered global namespace
temp1 = 0
temp2 = 0
temp3 = 0
result1 = 0
result2 = 0

# Better - use local variables
def calculate():
    temp1 = 0
    temp2 = 0
    temp3 = 0
    # Process...
    return result
```

### 4. Hidden Dependencies

```python
# Poor - hidden global dependency
RATE = 0.1

def calculate_tax(amount):
    return amount * RATE  # Depends on global RATE

# Better - explicit dependency
def calculate_tax(amount, rate):
    return amount * rate

result = calculate_tax(100, 0.1)
```

### 5. Testing Difficulties

```python
# Poor - hard to test due to global state
score = 0

def add_points(points):
    global score
    score += points

# Better - testable function
def add_points(current_score, points):
    return current_score + points

score = add_points(score, 10)
```

## Advanced Topics

### globals() and locals()

```python
# Access global namespace
x = 10
y = 20

print(globals()['x'])  # 10
print(globals()['y'])  # 20

def show_locals():
    a = 1
    b = 2
    
    print(locals())  # {'a': 1, 'b': 2}
    
    # Can access but modifying locals() doesn't affect variables
    locals()['c'] = 3
    # print(c)  # NameError - locals() is a copy

show_locals()
```

### Dynamic Global Access

```python
# Access globals dynamically
globals()['dynamic_var'] = 100

print(dynamic_var)  # 100

# Modify existing global
x = 5
globals()['x'] = 10
print(x)  # 10
```

### exec() with Globals

```python
global_vars = {'x': 10, 'y': 20}
local_vars = {}

code = "result = x + y"
exec(code, global_vars, local_vars)

print(local_vars['result'])  # 30
```

## When to Use Global vs Local

### Use Global Variables When:

✅ Configuration that doesn't change:
```python
API_ENDPOINT = "https://api.example.com"
MAX_RETRIES = 3
```

✅ Constants:
```python
PI = 3.14159
SPEED_OF_LIGHT = 299792458
```

✅ Shared resources (with caution):
```python
database_connection = None
cache = {}
```

### Use Local Variables When:

✅ Temporary computation:
```python
def calculate_stats(numbers):
    total = sum(numbers)      # Local
    count = len(numbers)      # Local
    average = total / count   # Local
    return average
```

✅ Function-specific data:
```python
def process_order(order):
    subtotal = calculate_subtotal(order)  # Local
    tax = calculate_tax(subtotal)         # Local
    total = subtotal + tax                # Local
    return total
```

✅ Loop variables:
```python
def find_maximum(numbers):
    max_value = numbers[0]  # Local
    for num in numbers:     # num is local
        if num > max_value:
            max_value = num
    return max_value
```

## Practical Examples

### Example 1: Configuration Manager

```python
# Global configuration
CONFIG = {
    'debug': False,
    'log_level': 'INFO',
    'max_connections': 100
}

def set_debug(enabled):
    """Enable or disable debug mode."""
    global CONFIG
    CONFIG = CONFIG.copy()  # Create new dict
    CONFIG['debug'] = enabled

def is_debug():
    """Check if debug mode is enabled."""
    return CONFIG['debug']  # Just reading - no global needed

# Usage
print(is_debug())  # False
set_debug(True)
print(is_debug())  # True
```

### Example 2: Counter System

```python
# Global counters
_counters = {}

def create_counter(name):
    """Create a new counter."""
    global _counters
    _counters[name] = 0

def increment(name):
    """Increment a counter."""
    global _counters
    if name in _counters:
        _counters[name] += 1

def get_count(name):
    """Get counter value."""
    return _counters.get(name, 0)

# Usage
create_counter('requests')
increment('requests')
increment('requests')
print(get_count('requests'))  # 2
```

### Example 3: Clean Local Processing

```python
def process_transaction(amount, fee_rate=0.02):
    """Process transaction with fee calculation."""
    # All local - no global dependencies
    fee = amount * fee_rate
    net_amount = amount - fee
    
    # Validate
    if net_amount <= 0:
        raise ValueError("Amount too small after fees")
    
    # Format for display
    formatted = {
        'gross': f"${amount:.2f}",
        'fee': f"${fee:.2f}",
        'net': f"${net_amount:.2f}"
    }
    
    return formatted

# Clean, testable, no global state
result = process_transaction(100.00)
print(result)
```

## Quick Reference

### Creating Variables
```python
# Global (module level)
global_var = 10

# Local (inside function)
def func():
    local_var = 20
```

### Reading Variables
```python
x = 10  # Global

def read_global():
    print(x)  # No keyword needed to read
```

### Modifying Variables
```python
x = 10  # Global

def modify_global():
    global x  # Keyword needed to modify
    x = 20

def create_local():
    x = 30  # Creates new local variable
```

### Common Patterns
```python
# Constants (never modified)
MAX_SIZE = 100

# State (modified carefully)
counter = 0

def increment():
    global counter
    counter += 1

# Temporary (always local)
def calculate():
    temp = 10
    result = temp * 2
    return result
```

## Summary

- **Local variables**: Defined in functions, exist only during function execution
- **Global variables**: Defined at module level, exist for entire program
- **Reading globals**: No special keyword needed
- **Modifying globals**: Requires `global` keyword
- **Shadowing**: Local variables hide globals with same name
- **Mutable objects**: Can modify without `global`, but reassignment needs it
- **Best practices**: Minimize globals, use constants, prefer parameters and return values
- **Common pitfalls**: UnboundLocalError, forgetting `global`, namespace pollution
- **Use locals for**: Temporary computation, function-specific data
- **Use globals for**: Configuration, constants, shared resources (sparingly)

Understanding global and local variables is essential for managing scope, avoiding bugs, and writing maintainable Python code. Always prefer local variables and function parameters unless there's a clear need for global state.
