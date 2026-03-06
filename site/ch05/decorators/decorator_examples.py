"""
Python Decorators - Practical Examples
This file contains various practical examples of decorators in Python.
Run this file to see decorators in action!
"""

import time
import functools

if __name__ == "__main__":

    print("=" * 70)
    print("PYTHON DECORATORS - EXAMPLES")
    print("=" * 70)

    # ============================================================================
    # EXAMPLE 1: Basic Decorator
    # ============================================================================
    print("\n1. BASIC DECORATOR")
    print("-" * 70)

    def simple_decorator(func):
        @functools.wraps(func)
        def wrapper():
            print("Before function call")
            result = func()
            print("After function call")
            return result
        return wrapper

    @simple_decorator
    def say_hello():
        print("Hello, World!")
        return "Greeting complete"

    result = say_hello()
    print(f"Return value: {result}")

    # ============================================================================
    # EXAMPLE 2: Decorator with Function Arguments
    # ============================================================================
    print("\n\n2. DECORATOR WITH FUNCTION ARGUMENTS")
    print("-" * 70)

    def logger(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with:")
            print(f"  args: {args}")
            print(f"  kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"  result: {result}")
            return result
        return wrapper

    @logger
    def add(a, b):
        return a + b

    @logger
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    add(5, 3)
    print()
    greet("Alice", greeting="Hi")

    # ============================================================================
    # EXAMPLE 3: Timing Decorator
    # ============================================================================
    print("\n\n3. TIMING DECORATOR")
    print("-" * 70)

    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} executed in {end - start:.4f} seconds")
            return result
        return wrapper

    @timer
    def fast_function():
        return sum(range(100))

    @timer
    def slow_function():
        time.sleep(0.5)
        return sum(range(1000000))

    print(f"Fast function result: {fast_function()}")
    print(f"Slow function result: {slow_function()}")

    # ============================================================================
    # EXAMPLE 4: Decorator with Parameters
    # ============================================================================
    print("\n\n4. DECORATOR WITH PARAMETERS")
    print("-" * 70)

    def repeat(times):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                results = []
                for i in range(times):
                    print(f"  Execution {i+1}/{times}:")
                    result = func(*args, **kwargs)
                    results.append(result)
                return results
            return wrapper
        return decorator

    @repeat(times=3)
    def greet(name):
        greeting = f"Hello, {name}!"
        print(f"    {greeting}")
        return greeting

    print("Calling decorated function:")
    results = greet("Bob")
    print(f"All results: {results}")

    # ============================================================================
    # EXAMPLE 5: Multiple Decorators (Stacking)
    # ============================================================================
    print("\n\n5. STACKING MULTIPLE DECORATORS")
    print("-" * 70)

    def uppercase(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result.upper()
        return wrapper

    def exclaim(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result + "!!!"
        return wrapper

    def quote(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'"{result}"'
        return wrapper

    @quote
    @uppercase
    @exclaim
    def greet(name):
        return f"hello, {name}"

    print(greet("Alice"))
    print("Note: Decorators are applied bottom-to-top")

    # ============================================================================
    # EXAMPLE 6: Caching/Memoization Decorator
    # ============================================================================
    print("\n\n6. CACHING/MEMOIZATION DECORATOR")
    print("-" * 70)

    def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            if args in cache:
                print(f"  Returning cached result for {args}")
                return cache[args]
            print(f"  Computing result for {args}")
            result = func(*args)
            cache[args] = result
            return result
        return wrapper

    @memoize
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    print("Calculating fibonacci(5):")
    print(f"Result: {fibonacci(5)}")
    print("\nCalculating fibonacci(5) again:")
    print(f"Result: {fibonacci(5)}")

    # ============================================================================
    # EXAMPLE 7: Authentication/Authorization Decorator
    # ============================================================================
    print("\n\n7. AUTHENTICATION DECORATOR")
    print("-" * 70)

    # Simulated user system
    current_user = {"name": "Alice", "role": "admin"}

    def require_auth(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if current_user is None:
                print("Access denied: Not logged in")
                return None
            return func(*args, **kwargs)
        return wrapper

    def require_role(role):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if current_user.get("role") != role:
                    print(f"Access denied: Requires '{role}' role")
                    return None
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @require_auth
    def view_profile():
        return f"Viewing profile for {current_user['name']}"

    @require_role("admin")
    def delete_user(username):
        return f"User {username} deleted by {current_user['name']}"

    print(view_profile())
    print(delete_user("Bob"))

    # Change user role
    current_user["role"] = "user"
    print("\nAfter changing role to 'user':")
    print(delete_user("Bob"))

    # ============================================================================
    # EXAMPLE 8: Validation Decorator
    # ============================================================================
    print("\n\n8. VALIDATION DECORATOR")
    print("-" * 70)

    def validate_positive(func):
        @functools.wraps(func)
        def wrapper(n):
            if n < 0:
                raise ValueError(f"Argument must be positive, got {n}")
            return func(n)
        return wrapper

    def validate_range(min_val, max_val):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(n):
                if not (min_val <= n <= max_val):
                    raise ValueError(f"Argument must be between {min_val} and {max_val}")
                return func(n)
            return wrapper
        return decorator

    @validate_positive
    def square_root(n):
        return n ** 0.5

    @validate_range(0, 100)
    def percentage_to_grade(score):
        if score >= 90: return "A"
        if score >= 80: return "B"
        if score >= 70: return "C"
        return "F"

    print(f"Square root of 16: {square_root(16)}")
    print(f"Grade for 85: {percentage_to_grade(85)}")

    print("\nTrying invalid inputs:")
    try:
        square_root(-4)
    except ValueError as e:
        print(f"  Error: {e}")

    try:
        percentage_to_grade(150)
    except ValueError as e:
        print(f"  Error: {e}")

    # ============================================================================
    # EXAMPLE 9: Retry Decorator
    # ============================================================================
    print("\n\n9. RETRY DECORATOR")
    print("-" * 70)

    def retry(max_attempts=3, delay=0.5):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                attempts = 0
                while attempts < max_attempts:
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        attempts += 1
                        if attempts == max_attempts:
                            print(f"  Failed after {max_attempts} attempts")
                            raise
                        print(f"  Attempt {attempts} failed: {e}. Retrying...")
                        time.sleep(delay)
            return wrapper
        return decorator

    # Simulate unreliable function
    call_count = 0

    @retry(max_attempts=3, delay=0.1)
    def unreliable_function():
        global call_count
        call_count += 1
        print(f"  Attempt {call_count}")
        if call_count < 2:
            raise ConnectionError("Network error")
        return "Success!"

    print("Calling unreliable function:")
    result = unreliable_function()
    print(f"Final result: {result}")

    # ============================================================================
    # EXAMPLE 10: Class-Based Decorator
    # ============================================================================
    print("\n\n10. CLASS-BASED DECORATOR")
    print("-" * 70)

    class CountCalls:
        def __init__(self, func):
            functools.update_wrapper(self, func)
            self.func = func
            self.count = 0

        def __call__(self, *args, **kwargs):
            self.count += 1
            print(f"Call #{self.count} to {self.func.__name__}")
            return self.func(*args, **kwargs)

    @CountCalls
    def say_hello(name):
        return f"Hello, {name}!"

    print(say_hello("Alice"))
    print(say_hello("Bob"))
    print(say_hello("Charlie"))
    print(f"\nTotal calls: {say_hello.count}")

    # ============================================================================
    # EXAMPLE 11: Debug Decorator
    # ============================================================================
    print("\n\n11. DEBUG DECORATOR")
    print("-" * 70)

    def debug(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            print(f"Calling {func.__name__}({signature})")
            result = func(*args, **kwargs)
            print(f"{func.__name__!r} returned {result!r}")
            return result
        return wrapper

    @debug
    def calculate(x, y, operation="+"):
        if operation == "+":
            return x + y
        elif operation == "*":
            return x * y
        return None

    calculate(5, 3, operation="+")
    calculate(5, 3, operation="*")

    # ============================================================================
    # EXAMPLE 12: Rate Limiting Decorator
    # ============================================================================
    print("\n\n12. RATE LIMITING DECORATOR")
    print("-" * 70)

    def rate_limit(max_calls, time_period):
        """Limit function calls to max_calls per time_period seconds"""
        def decorator(func):
            calls = []

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                now = time.time()
                # Remove old calls outside the time window
                calls[:] = [call for call in calls if now - call < time_period]

                if len(calls) >= max_calls:
                    wait_time = time_period - (now - calls[0])
                    print(f"  Rate limit reached. Wait {wait_time:.2f}s")
                    return None

                calls.append(now)
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @rate_limit(max_calls=3, time_period=2)
    def api_call(endpoint):
        return f"Calling {endpoint}"

    print("Making API calls (max 3 per 2 seconds):")
    for i in range(5):
        result = api_call(f"endpoint_{i}")
        if result:
            print(f"  {result}")
        time.sleep(0.3)

    print("\n" + "=" * 70)
    print("END OF EXAMPLES")
    print("=" * 70)
