"""
TUTORIAL: Context Managers - The __enter__ and __exit__ Protocol

This tutorial teaches you how to implement the context manager protocol by
defining __enter__ and __exit__ methods. Context managers enable the 'with'
statement, which is Python's way of managing resource setup and cleanup
safely and reliably.

Real-world uses: file handling, database connections, locks, temporary
redirects, transaction management, and anything that needs setup/teardown.

Key Learning Goals:
  - Understand when and why context managers matter
  - Implement __enter__ and __exit__ properly
  - Handle exceptions in __exit__
  - See how the 'with' statement works under the hood
"""

import sys

if __name__ == "__main__":

    print("=" * 70)
    print("TUTORIAL: Context Managers - __enter__ and __exit__")
    print("=" * 70)

    # ============ EXAMPLE 1: The Problem Context Managers Solve ============
    print("\n# Example 1: Resource Cleanup Without Context Managers")
    print("=" * 70)

    print("""
    Imagine you have a resource that needs setup and teardown:

    WRONG WAY (without context manager):
        resource = acquire_resource()
        resource.do_work()
        resource.cleanup()  # Oops! What if do_work() raises an exception?
        # cleanup() never runs!

    SAFER WAY (manual try/finally):
        resource = acquire_resource()
        try:
            resource.do_work()
        finally:
            resource.cleanup()  # Always runs, even if exception occurs

    PYTHONIC WAY (context manager):
        with acquire_resource() as resource:
            resource.do_work()  # cleanup() automatically happens after

    The 'with' statement guarantees cleanup happens, even on exceptions.
    It's cleaner, safer, and more readable than try/finally.
    """)

    # ============ EXAMPLE 2: The Context Manager Protocol ============
    print("\n# Example 2: Understanding __enter__ and __exit__")
    print("=" * 70)

    print("""
    A context manager is any object with two dunder methods:

        class ContextManager:
            def __enter__(self):
                # Called when entering the with block
                # Setup goes here
                # Return a value (or None) to assign to 'as variable'
                return something

            def __exit__(self, exc_type, exc_value, traceback):
                # Called when exiting the with block (always!)
                # Cleanup goes here
                # If it returns True, the exception is suppressed
                # If it returns False or None, exception propagates
                return False  # Don't suppress exceptions

    When you write:
        with obj:
            # ... code ...

    Python does this:
        mgr = obj
        exit = type(mgr).__exit__
        value = type(mgr).__enter__(mgr)
        try:
            # ... code ...
        except:
            exc_info = sys.exc_info()
            if not exit(mgr, *exc_info):
                raise  # Exception propagates
        else:
            exit(mgr, None, None, None)  # Normal exit
    """)

    # ============ EXAMPLE 3: A Simple Example - Stdout Redirection ============
    print("\n# Example 3: The LookingGlass Context Manager")
    print("=" * 70)

    class LookingGlass:
        """
        A context manager that reverses stdout output (mirror effect).

        This is a playful example but demonstrates the protocol perfectly.
        While active, all print output is reversed - it appears backwards.
        """

        def __enter__(self):
            """
            Called when entering the with block.

            Tasks:
            1. Save the original sys.stdout.write method
            2. Replace it with our reverse_write method
            3. Return a value to be assigned to 'as variable'

            This is the setup phase.
            """
            # Save the original so we can restore it later
            self.original_write = sys.stdout.write

            # Replace with our custom function
            sys.stdout.write = self.reverse_write

            # Return a value for the 'as' variable
            return 'JABBERWOCKY'

        def reverse_write(self, text):
            """
            Our custom stdout.write that reverses text.

            This will be called by print() internally, so output appears
            backwards. We call the original write with reversed text.
            """
            self.original_write(text[::-1])

        def __exit__(self, exc_type, exc_value, traceback):
            """
            Called when exiting the with block (always!).

            Parameters:
                exc_type: Exception class if an exception occurred (None otherwise)
                exc_value: Exception instance if one occurred (None otherwise)
                traceback: Exception traceback if one occurred (None otherwise)

            Tasks:
            1. Restore the original stdout.write
            2. Optionally handle exceptions (return True to suppress)

            Return value:
                True: suppress the exception (don't re-raise)
                False/None: let exception propagate normally
            """
            # Always restore the original write method
            sys.stdout.write = self.original_write

            # Handle ZeroDivisionError specially
            if exc_type is ZeroDivisionError:
                print('Please DO NOT divide by zero!')
                return True  # Suppress this specific exception

            # All other exceptions propagate normally (implicit return None)


    # Demonstrate the context manager
    print("Before entering context manager:")
    print("This text is printed normally")
    print()

    print("Entering context manager with LookingGlass():")

    with LookingGlass() as what:
        print('Alice, Kitty and Snowdrop')
        print(f"The variable 'what' is: {what}")

    print()
    print("After exiting context manager:")
    print("Output is back to normal")

    print("""
    WHY: The context manager handles all the complexity for you.
    You don't have to remember try/finally or manual cleanup.
    The 'with' statement makes it impossible to forget.
    """)

    # ============ EXAMPLE 4: Understanding the Execution Order ============
    print("\n# Example 4: Step-by-Step Execution")
    print("=" * 70)

    class Tracer:
        """Context manager that logs when things happen."""

        def __enter__(self):
            print("  1. __enter__ called (setup phase)")
            return "Inside the with block"

        def __exit__(self, exc_type, exc_value, traceback):
            print("  3. __exit__ called (cleanup phase)")
            if exc_type is not None:
                print(f"     Exception occurred: {exc_type.__name__}")
            return False  # Don't suppress exceptions


    print("Normal execution:")
    with Tracer() as var:
        print(f"  2. Inside with block, var = {var}")

    print()
    print("Execution with exception:")
    try:
        with Tracer() as var:
            print(f"  2. Inside with block")
            x = 1 / 0  # Raise exception
    except ZeroDivisionError:
        print("  4. Exception propagated and caught by outer try/except")

    print("""
    KEY INSIGHT: __exit__ is ALWAYS called, whether the block completes
    normally or an exception occurs. This guarantee is what makes context
    managers so powerful for cleanup.
    """)

    # ============ EXAMPLE 5: Handling Exceptions ============
    print("\n# Example 5: Exception Handling in __exit__")
    print("=" * 70)

    class ErrorHandler:
        """
        Context manager that can suppress certain exceptions.

        Shows how returning True from __exit__ suppresses exceptions.
        """

        def __init__(self, exception_type):
            self.exception_type = exception_type

        def __enter__(self):
            print(f"  __enter__: Will suppress {self.exception_type.__name__}")
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type is None:
                print("  __exit__: Normal exit (no exception)")
                return False
            elif exc_type is self.exception_type:
                print(f"  __exit__: Caught {exc_type.__name__} - suppressing it")
                return True  # Suppress this exception
            else:
                print(f"  __exit__: Caught {exc_type.__name__} - NOT suppressing")
                return False  # Don't suppress


    print("Suppressing ValueError:")
    with ErrorHandler(ValueError):
        print("  Inside block, raising ValueError")
        raise ValueError("This will be suppressed")
    print("  Block exited - exception was suppressed!")
    print()

    print("NOT suppressing TypeError:")
    try:
        with ErrorHandler(ValueError):
            print("  Inside block, raising TypeError")
            raise TypeError("This will NOT be suppressed")
    except TypeError:
        print("  Block exited - exception propagated and caught!")

    print("""
    WHY: Some context managers (like pytest fixtures) suppress expected
    exceptions. Returning True says "I handled this, don't propagate."
    Returning False or None says "I didn't handle this, propagate it."

    Most context managers return None or False - they don't suppress.
    """)

    # ============ EXAMPLE 6: Real-World Example - File Handling ============
    print("\n# Example 6: File Handling (Real-World Context Manager)")
    print("=" * 70)

    class ManagedFile:
        """
        A context manager for file operations.

        This demonstrates why context managers matter in real code:
        files need to be opened and closed reliably.
        """

        def __init__(self, name, mode):
            self.name = name
            self.mode = mode
            self.file = None

        def __enter__(self):
            print(f"  __enter__: Opening file '{self.name}'")
            self.file = open(self.name, self.mode)
            return self.file

        def __exit__(self, exc_type, exc_value, traceback):
            if self.file:
                print(f"  __exit__: Closing file '{self.name}'")
                self.file.close()
            if exc_type is not None:
                print(f"  __exit__: Exception occurred: {exc_type.__name__}")
            return False


    # Demonstrate file handling
    print("Writing to a file:")
    with ManagedFile('/tmp/test.txt', 'w') as f:
        f.write("Hello, World!\n")
        f.write("This is a test file.\n")

    print()
    print("Reading from the file:")
    with ManagedFile('/tmp/test.txt', 'r') as f:
        for line in f:
            print(f"  Read: {line.rstrip()}")

    print()
    print("File closed automatically after each with block!")

    print("""
    WHY: Built-in file objects already implement the context manager protocol,
    so you can use:
        with open('file.txt') as f:
            # ...

    This is so common that it's the Pythonic way to open files. Files are
    automatically closed when exiting the with block, even if an exception
    occurs.
    """)

    # ============ EXAMPLE 7: Multiple Resources ============
    print("\n# Example 7: Managing Multiple Resources")
    print("=" * 70)

    class Resource:
        """Simulates a resource that needs cleanup."""

        def __init__(self, name):
            self.name = name

        def __enter__(self):
            print(f"  Acquired {self.name}")
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            print(f"  Released {self.name}")
            return False

        def use(self):
            print(f"  Using {self.name}")


    print("Managing multiple resources with nested with statements:")
    with Resource("Resource A") as a:
        with Resource("Resource B") as b:
            with Resource("Resource C") as c:
                a.use()
                b.use()
                c.use()

    print()
    print("More readable: use comma syntax (Python 3.10+):")
    print("""
        with Resource("A") as a, \\
             Resource("B") as b, \\
             Resource("C") as c:
            a.use()
            b.use()
            c.use()

    Resources are acquired and released in the correct order (LIFO - Last In,
    First Out). C is released first, then B, then A.
    """)

    # ============ EXAMPLE 8: The Complete Pattern ============
    print("\n# Example 8: Context Manager Checklist")
    print("=" * 70)

    print("""
    When implementing a context manager, follow this pattern:

    class MyContextManager:
        def __init__(self, ...):
            # Store initialization parameters
            self.resource = None

        def __enter__(self):
            # 1. Acquire resource
            self.resource = acquire_resource()
            # 2. Perform any setup
            self.resource.setup()
            # 3. Return a value for 'as variable' (or self)
            return self.resource

        def __exit__(self, exc_type, exc_value, traceback):
            # 1. Always clean up resources
            if self.resource:
                self.resource.cleanup()

            # 2. Optional: handle specific exceptions
            if exc_type is SomeException:
                # Handle it
                return True  # Suppress

            # 3. Return False/None to propagate exceptions
            return False

    USAGE:
        with MyContextManager(...) as resource:
            resource.do_something()
        # Cleanup guaranteed to happen here

    KEY RULES:
        - __enter__ runs when entering the with block
        - __exit__ ALWAYS runs when exiting (normal or exception)
        - __exit__ receives exception info (or None, None, None if normal)
        - Return True to suppress exception, False/None to propagate
        - Use __exit__ for cleanup, not for normal work
    """)

    # ============ EXAMPLE 9: Common Pattern - Lock Management ============
    print("\n# Example 9: Lock Management (Concurrency Pattern)")
    print("=" * 70)

    class SimpleLock:
        """Context manager for thread synchronization."""

        def __init__(self, name):
            self.name = name
            self.acquired = False

        def __enter__(self):
            print(f"  Acquiring lock: {self.name}")
            self.acquired = True
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            if self.acquired:
                print(f"  Releasing lock: {self.name}")
                self.acquired = False


    print("Lock acquisition and release:")
    with SimpleLock("data_lock"):
        print("  Critical section protected by lock")
        print("  Can safely access shared data")
    print("  Lock automatically released")

    print("""
    WHY: Context managers are essential for thread-safe code. Locks are
    acquired on __enter__ and released on __exit__, even if exceptions occur.
    This prevents deadlocks and data corruption.

    This pattern is used in threading.Lock, threading.RLock, and many
    concurrency libraries.
    """)

    # ============ EXAMPLE 10: Summary ============
    print("\n# Example 10: When to Use Context Managers")
    print("=" * 70)

    print("""
    USE CONTEXT MANAGERS FOR:
        1. File operations (open, read, write, close)
        2. Database transactions (begin, commit, rollback)
        3. Network connections (connect, disconnect)
        4. Thread locks (acquire, release)
        5. Temporary state changes (redirect stdout, change directory)
        6. Resource pooling (acquire from pool, return to pool)
        7. Timing operations (start timer, stop and report)
        8. Error suppression (catch specific exceptions)

    PATTERN CHECKLIST:
        ✓ __enter__ acquires resources and returns them
        ✓ __exit__ releases resources (cleanup)
        ✓ __exit__ always runs, even on exceptions
        ✓ Suppressing exceptions is optional (usually don't)
        ✓ Use 'with' statement (never call __enter__/__exit__ directly)
        ✓ Can stack multiple with statements for multiple resources

    BENEFITS:
        ✓ Guaranteed cleanup (no forgotten cleanup calls)
        ✓ Clean, readable code
        ✓ Exception-safe
        ✓ Clear intent (anyone sees 'with' knows resource is managed)
        ✓ Pythonic (idiomatic Python style)

    NEXT: If you find context managers verbose, learn about @contextmanager
    decorator in the next tutorial - it simplifies many common cases!
    """)

    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS")
    print("=" * 70)
    print("""
    1. CONTEXT MANAGERS ARE FOR RESOURCE MANAGEMENT: Use them whenever
       something needs setup and cleanup (files, locks, transactions, etc).

    2. __enter__ AND __exit__ ARE THE PROTOCOL: Implement these two methods
       and any object becomes a context manager usable with 'with'.

    3. __exit__ IS GUARANTEED TO RUN: This is what makes context managers
       so powerful - cleanup is guaranteed even if exceptions occur.

    4. RETURN VALUE MATTERS: Return True to suppress exceptions, False/None
       to propagate them. Most context managers propagate.

    5. WITH STATEMENT IS CLEANER: 'with' is more readable and safer than
       manual try/finally. Always prefer 'with' when possible.

    6. USE THE PROTOCOL EVERYWHERE APPLICABLE: Any resource that needs
       cleanup should be managed through a context manager. It's a sign
       of professional Python code.

    7. YOU'RE PROBABLY ALREADY USING THEM: File objects, database
       connections, and many libraries use context managers. Now you can
       build your own!
    """)
