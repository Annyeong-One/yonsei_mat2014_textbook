"""
Decorator Factory with Strategy Pattern

This example demonstrates a decorator factory that accepts different
output strategies (console, file) for recording function execution.
This combines decorator factories with the strategy design pattern.

Topics covered:
- Decorator factories (decorators that accept parameters)
- Strategy pattern (swappable behavior via function arguments)
- functools.wraps for preserving function metadata
- Timing function execution

Based on concepts from Python-100-Days example09 and ch05/decorators materials.
"""

from functools import wraps
from time import time, sleep


# =============================================================================
# Example 1: Output Strategy Functions
# =============================================================================

def output_to_console(func_name: str, duration: float) -> None:
    """Strategy: print timing info to console."""
    print(f'  [{func_name}] completed in {duration:.3f}s')


def output_to_file(func_name: str, duration: float,
                   filename: str = 'timing_log.txt') -> None:
    """Strategy: append timing info to a log file."""
    with open(filename, 'a') as f:
        f.write(f'{func_name}: {duration:.3f}s\n')
    print(f'  [{func_name}] logged to {filename}')


# =============================================================================
# Example 2: Decorator Factory with Strategy Parameter
# =============================================================================

def record(output_strategy):
    """Decorator factory: create a timing decorator with a given output strategy.

    This is a three-level nesting pattern:
    1. record(strategy) -> returns the actual decorator
    2. decorator(func) -> wraps the target function
    3. wrapper(*args, **kwargs) -> executes and times the function

    Usage:
        @record(output_to_console)
        def my_function():
            ...
    """
    def decorator(func):
        @wraps(func)  # Preserve original function's __name__, __doc__, etc.
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            duration = time() - start
            output_strategy(func.__name__, duration)
            return result
        return wrapper
    return decorator


# =============================================================================
# Example 3: Using the Decorator Factory
# =============================================================================

@record(output_to_console)
def simulate_api_call(endpoint: str, delay: float = 0.1) -> str:
    """Simulate an API call with artificial delay."""
    sleep(delay)
    return f"Response from {endpoint}"


@record(output_to_file)
def simulate_db_query(query: str, delay: float = 0.05) -> list:
    """Simulate a database query with artificial delay."""
    sleep(delay)
    return [{"id": 1, "data": query}]


# =============================================================================
# Example 4: Flexible Strategy with Lambda
# =============================================================================

@record(lambda name, dur: print(f'  >>> {name} took {dur*1000:.1f}ms'))
def quick_operation():
    """A fast operation with inline strategy."""
    return sum(range(10000))


# =============================================================================
# Example 5: Accessing __wrapped__ to Bypass Decorator
# =============================================================================

def demo_unwrap():
    """functools.wraps adds __wrapped__ attribute for accessing the original."""
    print("\n=== Bypassing Decorator ===")
    print(f"Decorated name: {simulate_api_call.__name__}")

    # Access original function without timing
    original = simulate_api_call.__wrapped__
    result = original("/api/test", delay=0.01)
    print(f"  Direct call (no timing): {result}")


# =============================================================================
# Example 6: Configurable Decorator Factory
# =============================================================================

def timed(*, threshold: float = 0.0, label: str = ""):
    """Decorator factory that only reports when execution exceeds threshold.

    This is a more practical version showing how decorator factories
    can accept keyword arguments for configuration.

    Usage:
        @timed(threshold=0.5, label="SLOW")
        def my_function():
            ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            duration = time() - start
            if duration >= threshold:
                tag = f" [{label}]" if label else ""
                print(f"  {func.__name__}{tag}: {duration:.3f}s "
                      f"(threshold: {threshold:.3f}s)")
            return result
        return wrapper
    return decorator


@timed(threshold=0.1, label="SLOW")
def fast_function():
    """This function is fast, so timing won't be reported."""
    return sum(range(100))


@timed(threshold=0.01, label="DB")
def slow_function():
    """This function is slow, so timing will be reported."""
    sleep(0.05)
    return "done"


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    print("=== Decorator Factory with Strategy Pattern ===\n")

    print("--- Console Strategy ---")
    result = simulate_api_call("/api/users", delay=0.1)
    print(f"  Result: {result}")

    print("\n--- File Strategy ---")
    result = simulate_db_query("SELECT * FROM users")
    print(f"  Result: {result}")

    print("\n--- Lambda Strategy ---")
    result = quick_operation()
    print(f"  Result: {result}")

    demo_unwrap()

    print("\n=== Configurable Threshold Decorator ===")
    fast_function()   # Won't print (under threshold)
    slow_function()   # Will print (over threshold)
    print("  fast_function: no output (under threshold)")
