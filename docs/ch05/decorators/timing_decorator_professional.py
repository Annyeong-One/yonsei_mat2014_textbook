"""
TUTORIAL: Professional Timing Decorator Using functools.wraps

This tutorial covers how to write a PRODUCTION-QUALITY decorator that measures
function execution time.

The Key Concept: Decorators wrap functions to add behavior. But wrapping hides
the original function's metadata. The functools.wraps decorator solves this by
copying the wrapped function's metadata (__name__, __doc__, etc.) to the wrapper.

This tutorial demonstrates the CLOCK DECORATOR, which times function execution
and prints detailed information about calls, including arguments and results.
This is based on the clockdeco examples from Fluent Python.

Professional decorator pattern:
1. Use functools.wraps to preserve metadata
2. Handle *args and **kwargs for flexibility
3. Format output clearly
4. Don't hide function signature
5. Use functools.wraps ALWAYS
"""

import time
import functools

if __name__ == "__main__":

    print("=" * 70)
    print("TUTORIAL: Professional Timing Decorator with functools.wraps")
    print("=" * 70)

    # ============ EXAMPLE 1: The Problem Without functools.wraps
    print("\n# ============ EXAMPLE 1: The Problem Without functools.wraps")
    print("Why functools.wraps is essential:\n")


    def bad_timer(func):
        """A timer decorator WITHOUT functools.wraps"""
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"[{elapsed:.4f}s] Function executed")
            return result
        return wrapper


    @bad_timer
    def slow_function(n):
        """Compute factorial - this docstring will be lost!"""
        time.sleep(0.1)
        return n * (n - 1)


    print("Function with bad_timer decorator:")
    print(f"Function name: {slow_function.__name__}")
    print(f"Expected: slow_function")
    print(f"Actual: wrapper <- WRONG! We lost the original name!")
    print()

    print(f"Function docstring: {slow_function.__doc__}")
    print(f"Expected: 'Compute factorial - this docstring will be lost!'")
    print(f"Actual: {slow_function.__doc__} <- LOST!")
    print()

    print("""
    PROBLEM: When a decorator returns a wrapper function, it replaces
    the original function's metadata. The wrapper function has its own
    name, docstring, etc. This breaks:
      - help() documentation
      - __name__ inspection
      - __doc__ access
      - IDE autocomplete
      - Type stubs and type hints
    """)

    # ============ EXAMPLE 2: The Solution - functools.wraps
    print("\n" + "=" * 70)
    print("# ============ EXAMPLE 2: The Solution - functools.wraps")
    print("Using functools.wraps preserves original metadata:\n")


    def good_timer(func):
        """A timer decorator WITH functools.wraps"""
        @functools.wraps(func)  # This is the KEY line!
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"[{elapsed:.4f}s] Function executed")
            return result
        return wrapper


    @good_timer
    def factorial(n):
        """Compute factorial of n"""
        time.sleep(0.05)
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


    print("Function with good_timer decorator (using functools.wraps):")
    print(f"Function name: {factorial.__name__}")
    print(f"Expected: factorial")
    print(f"Actual: factorial <- CORRECT!")
    print()

    print(f"Function docstring: {factorial.__doc__}")
    print(f"Expected: 'Compute factorial of n'")
    print(f"Actual: {factorial.__doc__} <- CORRECT!")
    print()

    print("Calling the function:")
    result = factorial(5)
    print(f"Result: {result}\n")

    # ============ EXAMPLE 3: What functools.wraps Does
    print("\n" + "=" * 70)
    print("# ============ EXAMPLE 3: What functools.wraps Does")
    print("Understanding the metadata that gets preserved:\n")

    print("""
    @functools.wraps(func) copies these attributes from the original function:
      - __name__:      Function name
      - __doc__:       Docstring
      - __module__:    Module where defined
      - __qualname__:  Qualified name
      - __annotations__: Type hints
      - __dict__:      Function attributes
      - __wrapped__:   Reference to original function (for introspection!)

    EXAMPLE: Before functools.wraps
      wrapper.__name__ = 'wrapper'
      wrapper.__doc__ = None
      wrapper.__module__ = '__main__'

    AFTER functools.wraps(original_func)
      wrapper.__name__ = original_func.__name__
      wrapper.__doc__ = original_func.__doc__
      wrapper.__module__ = original_func.__module__
      wrapper.__wrapped__ = original_func  <- Can access original!
    """)

    # ============ EXAMPLE 4: The Clock Decorator - Professional Implementation
    print("\n" + "=" * 70)
    print("# ============ EXAMPLE 4: The Clock Decorator - Professional Implementation")
    print("A production-quality timing decorator:\n")


    def clock(func):
        """
        Decorator to time function execution and print details.

        Shows:
        - Elapsed time
        - Function name
        - All arguments (args and kwargs)
        - Return value

        Uses functools.wraps to preserve original function metadata.
        """
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            # Record the start time
            t0 = time.perf_counter()

            # Call the original function
            result = func(*args, **kwargs)

            # Calculate elapsed time
            elapsed = time.perf_counter() - t0

            # Get function name
            name = func.__name__

            # Format arguments
            arg_lst = [repr(arg) for arg in args]
            arg_lst.extend(f'{k}={v!r}' for k, v in kwargs.items())
            arg_str = ', '.join(arg_lst)

            # Print the result in a nice format
            print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')

            return result

        return clocked


    print("Define some test functions with the @clock decorator:\n")


    @clock
    def factorial_fast(n):
        """Compute n!"""
        if n < 2:
            return 1
        return n * factorial_fast(n - 1)


    @clock
    def fibonacci(n):
        """Compute Fibonacci number at position n"""
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)


    @clock
    def greet(name, greeting="Hello"):
        """Greet someone with a custom greeting"""
        time.sleep(0.01)
        return f"{greeting}, {name}!"


    print("Test 1: Simple function with one argument")
    result = factorial_fast(5)
    print()

    print("Test 2: Recursive function")
    result = fibonacci(5)
    print()

    print("Test 3: Function with keyword arguments")
    result = greet("Alice", greeting="Hi")
    print()

    print("Test 4: Function with positional and keyword args")
    result = greet("Bob")
    print()

    # ============ EXAMPLE 5: Accessing the Original Function
    print("\n" + "=" * 70)
    print("# ============ EXAMPLE 5: Accessing the Original Function")
    print("functools.wraps provides __wrapped__ for introspection:\n")

    print("Decorated function still accessible via __wrapped__:")
    print(f"factorial_fast.__wrapped__ = {factorial_fast.__wrapped__}")
    print(f"factorial_fast.__wrapped__ is the original function")

    print("\nYou can call the original function directly (bypassing decoration):")
    # This calls the original without timing
    original_result = factorial_fast.__wrapped__(5)
    print(f"Result: {original_result}\n")

    print(f"Compare metadata:")
    print(f"  factorial_fast.__name__ = {factorial_fast.__name__}")
    print(f"  factorial_fast.__doc__ = {factorial_fast.__doc__}")
    print(f"  factorial_fast.__wrapped__ = {factorial_fast.__wrapped__}")

    # ============ EXAMPLE 6: Comparing Decorated vs Non-Decorated
    print("\n" + "=" * 70)
    print("# ============ EXAMPLE 6: Comparing Decorated vs Non-Decorated")
    print("Timing the same function with and without decoration:\n")


    def undecorated_calculation(n):
        """Calculate something without timing"""
        return sum(range(n))


    @clock
    def decorated_calculation(n):
        """Calculate something with timing"""
        return sum(range(n))


    print("Calling undecorated version:")
    result1 = undecorated_calculation(1000000)
    print(f"Result: {result1}\n")

    print("Calling decorated version (note the timing output):")
    result2 = decorated_calculation(1000000)
    print(f"Result: {result2}")
    print("(Notice how the decorated version prints timing info)\n")

    # ============ EXAMPLE 7: Customizing the Clock Decorator
    print("\n" + "=" * 70)
    print("# ============ EXAMPLE 7: Customizing the Clock Decorator")
    print("Create a parameterized version that shows/hides details:\n")


    def clock_with_options(precision=8, show_args=True, show_result=True):
        """
        Decorator factory that creates customized timing decorators.

        Args:
            precision: Decimal places for elapsed time (default: 8)
            show_args: Whether to show arguments (default: True)
            show_result: Whether to show return value (default: True)
        """
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                t0 = time.perf_counter()
                result = func(*args, **kwargs)
                elapsed = time.perf_counter() - t0

                name = func.__name__

                # Build output string based on options
                if show_args:
                    arg_lst = [repr(arg) for arg in args]
                    arg_lst.extend(f'{k}={v!r}' for k, v in kwargs.items())
                    arg_str = ', '.join(arg_lst)
                    parts = [f'{name}({arg_str})']
                else:
                    parts = [f'{name}()']

                if show_result:
                    parts.append(f'-> {result!r}')

                output = ' '.join(parts)
                format_str = f'[{{:0.{precision}f}}s] {{}}'
                print(format_str.format(elapsed, output))

                return result
            return wrapper
        return decorator


    @clock_with_options()
    def func_full_info(x):
        """Shows everything"""
        time.sleep(0.01)
        return x * 2


    @clock_with_options(show_args=False, show_result=False)
    def func_minimal_info(x):
        """Shows only timing and function name"""
        time.sleep(0.01)
        return x * 2


    @clock_with_options(precision=3, show_result=False)
    def func_moderate_info(x):
        """Shows timing, name, and args, but not result"""
        time.sleep(0.01)
        return x * 2


    print("Full info (shows everything):")
    func_full_info(42)

    print("\nMinimal info (only timing and name):")
    func_minimal_info(42)

    print("\nModerate info (timing, name, args, but not result):")
    func_moderate_info(42)

    # ============ EXAMPLE 8: Multiple Decorators with functools.wraps
    print("\n" + "=" * 70)
    print("# ============ EXAMPLE 8: Multiple Decorators with functools.wraps")
    print("Stacking decorators while preserving metadata:\n")


    def trace(func):
        """Decorator that shows when functions enter/exit"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"  >> Entering {func.__name__}")
            result = func(*args, **kwargs)
            print(f"  << Exiting {func.__name__}")
            return result
        return wrapper


    @clock
    @trace
    def with_both_decorators(n):
        """Function with both decorators"""
        time.sleep(0.02)
        return n ** 2


    print("Function with @clock and @trace decorators:")
    print(f"Name: {with_both_decorators.__name__}")
    print(f"Doc: {with_both_decorators.__doc__}\n")

    print("Calling the function:")
    result = with_both_decorators(5)
    print(f"Result: {result}")

    # ============ EXAMPLE 9: Real-World Use Cases
    print("\n" + "=" * 70)
    print("# ============ EXAMPLE 9: Real-World Use Cases")
    print("Practical applications of timing decorators:\n")


    @clock
    def api_call(endpoint):
        """Simulate an API call"""
        time.sleep(0.1)
        return f"Data from {endpoint}"


    @clock
    def database_query(table, limit=10):
        """Simulate a database query"""
        time.sleep(0.05)
        return f"Fetched {limit} rows from {table}"


    @clock
    def process_data(data):
        """Process some data"""
        time.sleep(0.02)
        return f"Processed: {data}"


    print("API call timing:")
    api_call('/users')

    print("\nDatabase query timing:")
    database_query('users', limit=100)

    print("\nData processing timing:")
    process_data([1, 2, 3, 4, 5])

    # ============ EXAMPLE 10: Best Practices for Decorators
    print("\n" + "=" * 70)
    print("# ============ EXAMPLE 10: Best Practices for Decorators")
    print("Guidelines for writing professional decorators:\n")

    print("""
    BEST PRACTICES FOR DECORATORS:

    1. ALWAYS USE functools.wraps
       @functools.wraps(func)
       def wrapper(*args, **kwargs):
           ...

       This preserves:
       - Function name
       - Docstring
       - Type hints
       - __wrapped__ reference

    2. USE *args AND **kwargs FOR FLEXIBILITY
       def wrapper(*args, **kwargs):
           ...

       This allows the decorator to work with any function signature.

    3. PRESERVE RETURN VALUE
       Always return the result from calling the wrapped function.
       return func(*args, **kwargs)

    4. HANDLE EXCEPTIONS PROPERLY
       If you need to catch exceptions, re-raise them after cleanup.
       try:
           result = func(*args, **kwargs)
       finally:
           # cleanup

    5. DOCUMENT WHAT THE DECORATOR DOES
       Clearly explain:
       - What behavior is added
       - What performance impact it has
       - Any side effects
       - Usage examples

    6. FOR PARAMETERIZED DECORATORS, USE FACTORIES
       def decorator_factory(param1, param2):
           def decorator(func):
               @functools.wraps(func)
               def wrapper(*args, **kwargs):
                   ...
               return wrapper
           return decorator

       Usage: @decorator_factory(param1=value)

    7. CONSIDER DECORATOR ORDER
       - @clock above @trace means clock wraps trace
       - Execution order: clock -> trace -> original
       - Be aware of decorator stacking

    8. AVOID MODIFYING FUNCTION SIGNATURE
       - Decorator shouldn't change what parameters function accepts
       - Use *args, **kwargs to be transparent

    9. TEST THAT METADATA IS PRESERVED
       assert decorated_func.__name__ == original_func.__name__
       assert decorated_func.__doc__ == original_func.__doc__

    10. DOCUMENT PERFORMANCE IMPACT
        Decorators add overhead. If significant, document it.
        Consider making timing/tracing optional.
    """)

    # ============ EXAMPLE 11: Common Pitfalls and Solutions
    print("\n" + "=" * 70)
    print("# ============ EXAMPLE 11: Common Pitfalls and Solutions")
    print("Mistakes to avoid:\n")

    print("""
    PITFALL 1: Forgetting functools.wraps
    WRONG:
        def timer(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper

    RIGHT:
        def timer(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper


    PITFALL 2: Not preserving return value
    WRONG:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)  # Return value lost!
                return None
            return wrapper

    RIGHT:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)  # Preserve return!
            return wrapper


    PITFALL 3: Changing function signature
    WRONG:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(x):  # Only works for single arg!
                return func(x)
            return wrapper

    RIGHT:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):  # Works for any signature
                return func(*args, **kwargs)
            return wrapper


    PITFALL 4: Swallowing exceptions
    WRONG:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass  # Silent failure!
            return wrapper

    RIGHT:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}")
                    raise  # Re-raise the exception!
            return wrapper
    """)

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("""
    KEY TAKEAWAYS:

    1. FUNCTOOLS.WRAPS IS ESSENTIAL
       @functools.wraps(func) preserves the original function's metadata.
       Never write a decorator without it!

    2. BASIC PATTERN:
       import functools

       def decorator(func):
           @functools.wraps(func)
           def wrapper(*args, **kwargs):
               # Do something before
               result = func(*args, **kwargs)
               # Do something after
               return result
           return wrapper

    3. WHAT functools.wraps PRESERVES:
       - __name__: Function name
       - __doc__: Docstring
       - __module__: Module name
       - __wrapped__: Original function (for introspection)
       - __annotations__: Type hints
       - __dict__: Custom attributes

    4. USE *args, **kwargs ALWAYS
       Allows decorator to work with any function signature.

    5. ALWAYS RETURN THE RESULT
       return func(*args, **kwargs)

    6. CLOCK DECORATOR EXAMPLE:
       Times function execution and prints:
       - Elapsed time with 8 decimal places
       - Function name
       - All arguments (args and kwargs)
       - Return value

    7. FOR PARAMETERS, USE DECORATOR FACTORIES:
       @decorator_factory(param=value)
       Requires an extra level of nesting.

    8. STACKING DECORATORS:
       @clock
       @trace
       def func():
           ...

       Decorators applied bottom-up.
       clock wraps trace wraps func.

    9. REAL-WORLD USES:
       - Timing and performance monitoring
       - Logging and tracing
       - Authentication and authorization
       - Caching and memoization
       - Input validation
       - Retry logic

    10. REMEMBER:
        - Always use functools.wraps
        - Use *args and **kwargs
        - Return the result
        - Handle exceptions properly
        - Document the decorator's behavior
        - Test that metadata is preserved
    """)
