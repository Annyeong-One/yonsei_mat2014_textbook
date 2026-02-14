"""
Python Closures - Practical Examples
This file contains various practical examples of closures in Python.
Run this file to see closures in action!
"""

print("=" * 70)
print("PYTHON CLOSURES - EXAMPLES")
print("=" * 70)

# ============================================================================
# EXAMPLE 1: Basic Closure
# ============================================================================
print("\n1. BASIC CLOSURE")
print("-" * 70)

def outer(message):
    # message is captured by the closure
    def inner():
        print(message)
    return inner

greet = outer("Hello, World!")
greet()  # Prints: Hello, World!

print("\nEven though outer() finished, inner() remembers 'message'")

# ============================================================================
# EXAMPLE 2: Multiple Closures with Different Environments
# ============================================================================
print("\n\n2. MULTIPLE CLOSURES WITH DIFFERENT ENVIRONMENTS")
print("-" * 70)

def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

times_2 = make_multiplier(2)
times_3 = make_multiplier(3)
times_10 = make_multiplier(10)

print(f"5 * 2 = {times_2(5)}")
print(f"5 * 3 = {times_3(5)}")
print(f"5 * 10 = {times_10(5)}")
print("\nEach closure maintains its own 'factor' value")

# ============================================================================
# EXAMPLE 3: Using nonlocal to Modify Enclosing Variables
# ============================================================================
print("\n\n3. USING NONLOCAL TO MODIFY ENCLOSING VARIABLES")
print("-" * 70)

def make_counter(start=0):
    count = start
    
    def increment():
        nonlocal count  # Allow modification of outer variable
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def get_count():
        return count
    
    return increment, decrement, get_count

inc, dec, get = make_counter(10)
print(f"Initial count: {get()}")
print(f"After increment: {inc()}")
print(f"After increment: {inc()}")
print(f"After increment: {inc()}")
print(f"After decrement: {dec()}")
print(f"Final count: {get()}")

# ============================================================================
# EXAMPLE 4: Factory Functions
# ============================================================================
print("\n\n4. FACTORY FUNCTIONS")
print("-" * 70)

def make_power(exponent):
    def power(base):
        return base ** exponent
    return power

square = make_power(2)
cube = make_power(3)
fourth_power = make_power(4)

number = 3
print(f"{number}^2 = {square(number)}")
print(f"{number}^3 = {cube(number)}")
print(f"{number}^4 = {fourth_power(number)}")

# ============================================================================
# EXAMPLE 5: Data Encapsulation (Private Variables)
# ============================================================================
print("\n\n5. DATA ENCAPSULATION (PRIVATE VARIABLES)")
print("-" * 70)

def make_account(initial_balance):
    balance = initial_balance  # Private variable
    
    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount
            return f"Deposited ${amount}. New balance: ${balance}"
        return "Invalid amount"
    
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        if amount > 0:
            balance -= amount
            return f"Withdrew ${amount}. New balance: ${balance}"
        return "Invalid amount"
    
    def get_balance():
        return f"Current balance: ${balance}"
    
    return {
        'deposit': deposit,
        'withdraw': withdraw,
        'get_balance': get_balance
    }

account = make_account(1000)
print(account['get_balance']())
print(account['deposit'](500))
print(account['withdraw'](200))
print(account['withdraw'](2000))  # Insufficient funds
print(account['get_balance']())

# Note: There's no way to directly access 'balance' from outside!

# ============================================================================
# EXAMPLE 6: Function Decorators (Built on Closures)
# ============================================================================
print("\n\n6. FUNCTION DECORATORS (BUILT ON CLOSURES)")
print("-" * 70)

def make_logger(func):
    def wrapper(*args, **kwargs):
        print(f"🔍 Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ {func.__name__} returned {result}")
        return result
    return wrapper

@make_logger
def add(a, b):
    return a + b

@make_logger
def multiply(x, y):
    return x * y

result1 = add(3, 5)
print(f"Result: {result1}\n")
result2 = multiply(4, 7)
print(f"Result: {result2}")

# ============================================================================
# EXAMPLE 7: Configuration Functions
# ============================================================================
print("\n\n7. CONFIGURATION FUNCTIONS")
print("-" * 70)

def make_formatter(prefix, suffix):
    def format_text(text):
        return f"{prefix}{text}{suffix}"
    return format_text

html_bold = make_formatter("<b>", "</b>")
html_italic = make_formatter("<i>", "</i>")
parentheses = make_formatter("(", ")")
quotes = make_formatter('"', '"')

text = "Hello"
print(f"Original: {text}")
print(f"Bold: {html_bold(text)}")
print(f"Italic: {html_italic(text)}")
print(f"Parentheses: {parentheses(text)}")
print(f"Quoted: {quotes(text)}")

# ============================================================================
# EXAMPLE 8: Closures with Multiple Free Variables
# ============================================================================
print("\n\n8. CLOSURES WITH MULTIPLE FREE VARIABLES")
print("-" * 70)

def make_linear_function(slope, intercept):
    """Create a linear function: y = slope * x + intercept"""
    def linear(x):
        return slope * x + intercept
    return linear

line1 = make_linear_function(2, 3)   # y = 2x + 3
line2 = make_linear_function(-1, 5)  # y = -x + 5

x_value = 4
print(f"For x = {x_value}:")
print(f"  y = 2x + 3 = {line1(x_value)}")
print(f"  y = -x + 5 = {line2(x_value)}")

# ============================================================================
# EXAMPLE 9: Closures for Callbacks with State
# ============================================================================
print("\n\n9. CLOSURES FOR CALLBACKS WITH STATE")
print("-" * 70)

def make_click_handler(element_id):
    click_count = 0
    
    def handle_click():
        nonlocal click_count
        click_count += 1
        print(f"  {element_id} clicked {click_count} time(s)")
    
    return handle_click

button1 = make_click_handler("Button 1")
button2 = make_click_handler("Button 2")

print("Simulating button clicks:")
button1()  # Button 1 clicked 1 time
button1()  # Button 1 clicked 2 times
button2()  # Button 2 clicked 1 time
button1()  # Button 1 clicked 3 times
button2()  # Button 2 clicked 2 times

# ============================================================================
# EXAMPLE 10: Closure vs Class Comparison
# ============================================================================
print("\n\n10. CLOSURE VS CLASS COMPARISON")
print("-" * 70)

# Using a closure
def make_counter_closure(start=0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

# Using a class
class CounterClass:
    def __init__(self, start=0):
        self.count = start
    
    def increment(self):
        self.count += 1
        return self.count

print("Closure implementation:")
counter_closure = make_counter_closure(5)
print(f"  {counter_closure()}")
print(f"  {counter_closure()}")

print("\nClass implementation:")
counter_class = CounterClass(5)
print(f"  {counter_class.increment()}")
print(f"  {counter_class.increment()}")

print("\nBoth achieve the same result!")

# ============================================================================
# EXAMPLE 11: Closures in Loops (Common Pitfall and Solution)
# ============================================================================
print("\n\n11. CLOSURES IN LOOPS (PITFALL AND SOLUTION)")
print("-" * 70)

# WRONG WAY
print("❌ Common mistake:")
def create_multipliers_wrong():
    multipliers = []
    for i in range(5):
        multipliers.append(lambda x: x * i)
    return multipliers

funcs_wrong = create_multipliers_wrong()
print(f"  Expected: 0 * 2 = 0, Got: {funcs_wrong[0](2)}")
print(f"  Expected: 1 * 2 = 2, Got: {funcs_wrong[1](2)}")
print("  All closures reference the same 'i', which is 4 after the loop!")

# RIGHT WAY - Solution 1: Default argument
print("\n✅ Solution 1: Default argument:")
def create_multipliers_correct1():
    multipliers = []
    for i in range(5):
        multipliers.append(lambda x, i=i: x * i)  # Capture current i
    return multipliers

funcs_correct1 = create_multipliers_correct1()
print(f"  0 * 2 = {funcs_correct1[0](2)}")
print(f"  1 * 2 = {funcs_correct1[1](2)}")
print(f"  2 * 2 = {funcs_correct1[2](2)}")

# RIGHT WAY - Solution 2: Factory function
print("\n✅ Solution 2: Factory function:")
def make_multiplier(i):
    return lambda x: x * i

def create_multipliers_correct2():
    return [make_multiplier(i) for i in range(5)]

funcs_correct2 = create_multipliers_correct2()
print(f"  0 * 2 = {funcs_correct2[0](2)}")
print(f"  1 * 2 = {funcs_correct2[1](2)}")
print(f"  2 * 2 = {funcs_correct2[2](2)}")

# ============================================================================
# EXAMPLE 12: Memoization Using Closures
# ============================================================================
print("\n\n12. MEMOIZATION USING CLOSURES")
print("-" * 70)

def make_memoized(func):
    cache = {}
    
    def memoized(*args):
        if args in cache:
            print(f"  💾 Cache hit for {args}")
            return cache[args]
        print(f"  🔄 Computing for {args}")
        result = func(*args)
        cache[args] = result
        return result
    
    return memoized

@make_memoized
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Calculating fibonacci(5):")
result = fibonacci(5)
print(f"Result: {result}")

print("\nCalculating fibonacci(5) again:")
result = fibonacci(5)
print(f"Result: {result}")

# ============================================================================
# EXAMPLE 13: Partial Function Application
# ============================================================================
print("\n\n13. PARTIAL FUNCTION APPLICATION")
print("-" * 70)

def partial(func, *fixed_args, **fixed_kwargs):
    def wrapper(*args, **kwargs):
        return func(*fixed_args, *args, **fixed_kwargs, **kwargs)
    return wrapper

def greet(greeting, name, punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

# Create specialized greeting functions
say_hello = partial(greet, "Hello")
say_goodbye = partial(greet, "Goodbye")
say_hi_excited = partial(greet, "Hi", punctuation="!!!")

print(say_hello("Alice"))
print(say_goodbye("Bob"))
print(say_hi_excited("Charlie"))

# ============================================================================
# EXAMPLE 14: Function Composition
# ============================================================================
print("\n\n14. FUNCTION COMPOSITION")
print("-" * 70)

def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed

def add_10(x):
    return x + 10

def multiply_2(x):
    return x * 2

def square(x):
    return x ** 2

# Create composed functions
add_then_multiply = compose(multiply_2, add_10)
multiply_then_square = compose(square, multiply_2)

x = 5
print(f"Input: {x}")
print(f"Add 10, then multiply by 2: {add_then_multiply(x)}")  # (5+10)*2 = 30
print(f"Multiply by 2, then square: {multiply_then_square(x)}")  # (5*2)^2 = 100

# ============================================================================
# EXAMPLE 15: Stateful Generators with Closures
# ============================================================================
print("\n\n15. STATEFUL GENERATORS WITH CLOSURES")
print("-" * 70)

def make_id_generator(prefix="ID"):
    counter = 0
    
    def generate_id():
        nonlocal counter
        counter += 1
        return f"{prefix}-{counter:04d}"
    
    return generate_id

user_id = make_id_generator("USER")
order_id = make_id_generator("ORDER")

print("Generating user IDs:")
for _ in range(3):
    print(f"  {user_id()}")

print("\nGenerating order IDs:")
for _ in range(3):
    print(f"  {order_id()}")

print("\n" + "=" * 70)
print("END OF EXAMPLES")
print("=" * 70)
