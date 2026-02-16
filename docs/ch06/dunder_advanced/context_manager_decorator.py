"""
TUTORIAL: The @contextmanager Decorator - Simpler Context Managers

This tutorial teaches you how to use @contextmanager decorator from the
contextlib module. Instead of writing classes with __enter__ and __exit__
methods, you can write a simple generator function that's much more concise.

This is the Pythonic way to create context managers when you don't need
the full power of a class.

Key Learning Goals:
  - Understand how @contextmanager transforms generators into context managers
  - Write context managers as functions instead of classes
  - Learn when to use decorator vs class approach
  - Master the yield pattern for setup/teardown
"""

import contextlib
import sys

print("=" * 70)
print("TUTORIAL: @contextmanager Decorator - Simpler Context Managers")
print("=" * 70)

# ============ EXAMPLE 1: Why the Decorator Exists ============
print("\n# Example 1: Class vs Function Approaches")
print("=" * 70)

print("""
REMINDER: Context managers can be classes:

    class LookingGlass:
        def __enter__(self):
            self.original = sys.stdout.write
            sys.stdout.write = self.reverse_write
            return 'JABBERWOCKY'

        def reverse_write(self, text):
            self.original(text[::-1])

        def __exit__(self, exc_type, exc_value, traceback):
            sys.stdout.write = self.original
            return False

This is verbose and has a lot of boilerplate. If your context manager
just does setup (before), then cleanup (after), there's a simpler way.

WITH @contextmanager:

    @contextlib.contextmanager
    def looking_glass():
        original = sys.stdout.write
        sys.stdout.write = lambda text: original(text[::-1])
        try:
            yield 'JABBERWOCKY'
        finally:
            sys.stdout.write = original

Much more concise! The decorator handles __enter__ and __exit__ for you.
""")

# ============ EXAMPLE 2: Basic @contextmanager Usage ============
print("\n# Example 2: Your First @contextmanager")
print("=" * 70)

@contextlib.contextmanager
def simple_context():
    """
    A simple context manager using the decorator.

    The pattern:
    1. Do setup before yield
    2. Yield a value to return from __enter__
    3. Do cleanup after yield (in finally block)

    The decorator automatically:
    - Wraps the yield value in a context manager
    - Runs code before yield in __enter__
    - Runs code after yield in __exit__
    - Handles exceptions properly
    """
    print("  Entering context (setup)")
    yield "setup complete"
    print("  Exiting context (cleanup)")


print("Using the context manager:")
with simple_context() as value:
    print(f"  Inside with block, value = {value}")

print()
print("Notice how clean this is:")
print("  - No class definition needed")
print("  - No __enter__ and __exit__ methods")
print("  - Setup and cleanup are adjacent in the code")
print("""
WHY: For simple setup/cleanup patterns, the decorator is more readable.
The yield statement clearly marks what gets returned and when cleanup happens.
""")

# ============ EXAMPLE 3: The LookingGlass with Decorator ============
print("\n# Example 3: LookingGlass Revisited (Much Simpler)")
print("=" * 70)

@contextlib.contextmanager
def looking_glass():
    """
    Reverse stdout output using the decorator.

    Compare this to the class version in the previous tutorial.
    This is so much simpler!

    HOW IT WORKS:
    1. Save original sys.stdout.write
    2. Yield the magic word to be returned by __enter__
    3. In finally block, restore the original write
    4. Everything between yield and end of function runs in __exit__
    """
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    try:
        yield 'JABBERWOCKY'  # This value is returned by __enter__
    finally:
        sys.stdout.write = original_write  # Always runs in __exit__


print("Before context:")
print("Normal output here")
print()

with looking_glass() as word:
    print('Alice, Kitty and Snowdrop')
    print(f"The magic word: {word}")

print()
print("After context:")
print("Back to normal output")

print("""
WHY: The try/finally ensures cleanup happens even if an exception occurs
inside the with block. The decorator handles all the __enter__/__exit__
machinery for you.
""")

# ============ EXAMPLE 4: Yielding None ============
print("\n# Example 4: Yielding None (No Return Value)")
print("=" * 70)

@contextlib.contextmanager
def timed_operation(operation_name):
    """
    Context manager that measures execution time.

    Sometimes you don't yield a value - you just yield None or nothing.
    The context manager still works; 'as variable' will be None.
    """
    import time
    start_time = time.time()
    print(f"  Starting {operation_name}")
    try:
        yield  # No value returned
    finally:
        elapsed = time.time() - start_time
        print(f"  Finished {operation_name} in {elapsed:.4f} seconds")


print("Measuring operation time:")
with timed_operation("file read"):
    # Simulate work
    data = sum(range(1000000))

print()
print("Another operation:")
with timed_operation("file write"):
    # Simulate work
    temp = [x for x in range(100000)]

print("""
WHY: Not all context managers need to return a value. Sometimes they just
manage state or timing. Yielding None (or nothing) is perfectly valid.
""")

# ============ EXAMPLE 5: Exception Handling ============
print("\n# Example 5: Handling Exceptions in Decorated Generators")
print("=" * 70)

@contextlib.contextmanager
def error_handler(exception_type):
    """
    A decorator-based context manager that can suppress exceptions.

    The key insight: exceptions raised in the with block propagate to
    the code after yield. You can catch them with try/except.
    """
    print(f"  Entering (will handle {exception_type.__name__})")
    try:
        yield
    except exception_type as e:
        print(f"  Caught and suppressed: {exception_type.__name__}")
        # Exception is suppressed by not re-raising
    except Exception as e:
        print(f"  Caught but re-raising: {type(e).__name__}")
        raise
    finally:
        print(f"  Always cleaning up")


print("Suppressing ValueError:")
with error_handler(ValueError):
    print("  Doing work...")
    raise ValueError("Something went wrong")
print("  After with block (exception was suppressed)")
print()

print("Not suppressing TypeError:")
try:
    with error_handler(ValueError):
        print("  Doing work...")
        raise TypeError("Wrong type!")
except TypeError:
    print("  After with block (exception propagated)")

print("""
WHY: Decorated generators let you handle exceptions elegantly.
- Don't re-raise to suppress
- Re-raise to propagate
- finally block always runs (cleanup guaranteed)
""")

# ============ EXAMPLE 6: Resource Management Pattern ============
print("\n# Example 6: Database-Like Resource Management")
print("=" * 70)

class FakeDatabase:
    """Simulates a database connection."""

    def __init__(self, name):
        self.name = name
        self.is_open = False

    def open(self):
        self.is_open = True
        print(f"    Database '{self.name}' opened")

    def close(self):
        self.is_open = False
        print(f"    Database '{self.name}' closed")

    def query(self, sql):
        if not self.is_open:
            raise RuntimeError("Database is closed")
        return f"Results of: {sql}"


@contextlib.contextmanager
def database_session(db_name):
    """
    Context manager for database operations.

    Pattern: open connection, yield it, close on exit.
    This is how many real database libraries work.
    """
    db = FakeDatabase(db_name)
    db.open()
    try:
        yield db
    finally:
        db.close()


print("Using database context manager:")
with database_session("mydb") as db:
    print(f"  Database open: {db.is_open}")
    result = db.query("SELECT * FROM users")
    print(f"  Query result: {result}")

print(f"  After with block: {db.is_open}")

print()
print("Exception handling in database context:")
try:
    with database_session("tempdb") as db:
        print(f"  Database open: {db.is_open}")
        # Simulate error
        raise ValueError("Invalid query")
except ValueError:
    print("  Exception propagated and caught")
    print(f"  Database closed during exception: {db.is_open}")

print("""
WHY: Real libraries (SQLAlchemy, psycopg2, etc.) use this pattern.
The decorator makes it simple to write context managers that acquire
and release resources safely.
""")

# ============ EXAMPLE 7: Complex Setup and Teardown ============
print("\n# Example 7: Multi-Step Setup and Cleanup")
print("=" * 70)

@contextlib.contextmanager
def multi_step_context():
    """
    Context manager with multiple setup/teardown steps.

    Even complex operations stay clean with the decorator.
    """
    print("  Step 1: Initialize resources")
    resource1 = "resource_1"

    print("  Step 2: Configure resource")
    resource2 = "resource_2"

    print("  Step 3: Open connections")
    print("  SETUP COMPLETE")

    try:
        yield (resource1, resource2)
    finally:
        print("  Step 1: Close connections")
        print("  Step 2: Save state")
        print("  Step 3: Release resources")
        print("  CLEANUP COMPLETE")


print("Multi-step context manager:")
with multi_step_context() as (r1, r2):
    print(f"  Working with {r1} and {r2}")

print("""
WHY: Complex initialization and cleanup is still readable with decorators.
The setup code is grouped at the top, cleanup at the bottom (in finally).
""")

# ============ EXAMPLE 8: Nesting and Composition ============
print("\n# Example 8: Combining Multiple Context Managers")
print("=" * 70)

@contextlib.contextmanager
def lock_context(name):
    """Simulates acquiring and releasing a lock."""
    print(f"  Acquired lock: {name}")
    try:
        yield
    finally:
        print(f"  Released lock: {name}")


@contextlib.contextmanager
def transaction_context():
    """Simulates a database transaction."""
    print("  BEGIN TRANSACTION")
    try:
        yield
    finally:
        print("  COMMIT TRANSACTION")


print("Combining context managers with nesting:")
with lock_context("data_lock"):
    with transaction_context():
        print("  Executing operations under lock and transaction")

print()
print("Cleaner syntax with multiple contexts (Python 3.10+):")
print("""
    with lock_context("lock"), transaction_context():
        # operations here
""")

print("""
WHY: Context managers compose well. You can nest them when you need
multiple resources, or use comma syntax for cleaner code.
""")

# ============ EXAMPLE 9: When to Use Decorator vs Class ============
print("\n# Example 9: Decorator vs Class - When to Use Each")
print("=" * 70)

print("""
USE @contextmanager (DECORATOR) WHEN:
    ✓ Simple setup/cleanup pattern
    ✓ Just need to yield a value once
    ✓ Logic is straightforward
    ✓ Less than ~50 lines of code

EXAMPLE: File cleanup, timing, simple redirects, database transactions

    @contextlib.contextmanager
    def simple():
        setup()
        try:
            yield value
        finally:
            cleanup()


USE A CLASS WHEN:
    ✓ Need complex initialization
    ✓ Need multiple methods
    ✓ State management is complex
    ✓ Need to support multiple protocols (__enter__, __exit__, and others)
    ✓ Plan to reuse in multiple contexts

EXAMPLE: Database connection pool, transaction with savepoints, API wrapper

    class ComplexManager:
        def __init__(self, ...):
            # Complex init
        def __enter__(self):
            # Setup
        def __exit__(self, ...):
            # Cleanup
        def helper_method(self):
            # Additional methods

RULE OF THUMB: Start with @contextmanager. If you find yourself adding
complexity, convert to a class. The decorator is for simple cases.
""")

# ============ EXAMPLE 10: Real-World Example - Temporary Directory ============
print("\n# Example 10: Real-World Example - Temporary File Management")
print("=" * 70)

import tempfile
import os

@contextlib.contextmanager
def temporary_directory():
    """
    Context manager for temporary directory.

    This shows a realistic use case: manage a temporary resource
    that needs cleanup.
    """
    tmpdir = tempfile.mkdtemp()
    print(f"  Created temporary directory: {tmpdir}")
    try:
        yield tmpdir
    finally:
        # Clean up
        if os.path.exists(tmpdir):
            print(f"  Removing temporary directory: {tmpdir}")
            # In real code: shutil.rmtree(tmpdir)
            # Here we just print it


print("Using temporary directory:")
with temporary_directory() as tmpdir:
    print(f"  Working in {tmpdir}")
    # Create files, do work, etc.
    print(f"  Directory exists: {os.path.exists(tmpdir)}")

print(f"  Directory cleaned up after with block")

print("""
WHY: Real libraries (tempfile, sqlite3, requests, etc.) use decorated
context managers extensively. This pattern is idiomatic Python.

REAL-WORLD USAGE:
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create files, do work
    # tmpdir automatically cleaned up

    with requests.Session() as session:
        response = session.get(url)
    # Connection automatically closed

    with open('file.txt') as f:
        data = f.read()
    # File automatically closed
""")

# ============ EXAMPLE 11: Summary and Comparison ============
print("\n# Example 11: Summary - Class vs Decorator")
print("=" * 70)

print("""
CONTEXT MANAGER AS CLASS:

    class ManagedResource:
        def __init__(self, name):
            self.name = name

        def __enter__(self):
            print(f"Opening {self.name}")
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            print(f"Closing {self.name}")
            return False

    with ManagedResource("file") as res:
        # use res

SAME CONTEXT MANAGER WITH DECORATOR:

    @contextlib.contextmanager
    def managed_resource(name):
        print(f"Opening {name}")
        try:
            yield type('Resource', (), {'name': name})()
        finally:
            print(f"Closing {name}")

    with managed_resource("file") as res:
        # use res

The decorator is simpler for straightforward cases. The class is better
for complex logic.
""")

print("\n" + "=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. @contextmanager TURNS GENERATORS INTO CONTEXT MANAGERS: Decorate a
   generator function and it becomes usable with 'with' statements.

2. THE YIELD PATTERN IS CLEAR: Code before yield = __enter__,
   code after yield = __exit__. Very readable!

3. try/finally ENSURES CLEANUP: Always use try/finally around yield
   to guarantee cleanup happens, even on exceptions.

4. DECORATOR SIMPLIFIES COMMON CASE: For simple setup/cleanup patterns,
   the decorator is far less verbose than a class.

5. EXCEPTION HANDLING WORKS NATURALLY: Exceptions in the with block
   propagate to the code after yield. Catch them with try/except.

6. YIELD NOTHING FOR SIDE-EFFECT MANAGERS: Not all context managers
   return values. Some just manage state (timing, locks, transactions).

7. CHOOSE BASED ON COMPLEXITY: Decorator for simple cases, class for
   complex cases. Start with the decorator, convert to class if needed.

8. STANDARD LIBRARIES USE THIS: Many real libraries use @contextmanager.
   Understanding it helps you read and use library code confidently.

NEXT: Explore advanced patterns like ExitStack for managing multiple
contexts dynamically, or write your own context managers for domain
-specific resources (database transactions, API sessions, etc.).
""")
