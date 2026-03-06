"""
Singleton Pattern: Decorator vs Metaclass Approaches

The singleton pattern ensures a class has only one instance.
This tutorial shows how to implement it using a class decorator
with thread-safety via double-checked locking.

Topics covered:
- Class decorators (decorators applied to classes)
- Singleton pattern implementation
- Thread safety with threading.Lock
- functools.wraps on classes
- Comparison: decorator vs metaclass singleton

Based on concepts from Python-100-Days examples 10 & 18, and ch05/decorators materials.
"""

import threading
from functools import wraps


# =============================================================================
# Example 1: Thread-Safe Singleton Decorator
# =============================================================================

def singleton(cls):
    """Decorator that makes a class a singleton (only one instance ever created).

    Uses double-checked locking for thread safety:
    1. First check without lock (fast path for existing instance)
    2. Acquire lock and check again (prevent race condition)

    >>> @singleton
    ... class Database:
    ...     def __init__(self, url):
    ...         self.url = url
    >>> db1 = Database("localhost:5432")
    >>> db2 = Database("localhost:3306")  # Returns same instance!
    >>> db1 is db2
    True
    """
    instances = {}
    lock = threading.Lock()

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:          # Fast check (no lock)
            with lock:                     # Acquire lock
                if cls not in instances:   # Double-check under lock
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


# =============================================================================
# Example 2: Singleton in Action
# =============================================================================

@singleton
class AppConfig:
    """Application configuration (should only exist once)."""

    def __init__(self, debug=False, db_url="sqlite:///app.db"):
        self.debug = debug
        self.db_url = db_url

    def __str__(self):
        return f"AppConfig(debug={self.debug}, db_url='{self.db_url}')"


def demo_singleton():
    """Demonstrate that singleton always returns the same instance."""
    print("=== Singleton Decorator Demo ===")

    config1 = AppConfig(debug=True, db_url="postgres://localhost/mydb")
    config2 = AppConfig(debug=False, db_url="mysql://localhost/other")

    print(f"config1: {config1}")
    print(f"config2: {config2}")
    print(f"Same object? {config1 is config2}")  # True
    print(f"Class name preserved: {AppConfig.__name__}")
    print()


# =============================================================================
# Example 3: Thread-Safety Verification
# =============================================================================

@singleton
class Counter:
    """Thread-safe singleton counter."""

    def __init__(self):
        self.count = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.count += 1


def demo_thread_safety():
    """Verify singleton works correctly under concurrent access."""
    print("=== Thread Safety Verification ===")

    def worker():
        c = Counter()  # Always gets the same instance
        for _ in range(1000):
            c.increment()

    threads = [threading.Thread(target=worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    counter = Counter()
    print(f"Expected count: 10000")
    print(f"Actual count:   {counter.count}")
    print(f"Thread safe:    {counter.count == 10000}")
    print()


# =============================================================================
# Example 4: Metaclass Alternative (for comparison)
# =============================================================================

class SingletonMeta(type):
    """Metaclass approach to singleton pattern.

    Instead of decorating the class, we use a custom metaclass that
    intercepts instance creation via __call__.
    """

    def __init__(cls, *args, **kwargs):
        cls._instance = None
        cls._lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Logger(metaclass=SingletonMeta):
    """Logger using metaclass singleton."""

    def __init__(self, name="default"):
        self.name = name
        self.messages = []

    def log(self, message):
        self.messages.append(message)

    def __str__(self):
        return f"Logger('{self.name}', {len(self.messages)} messages)"


def demo_metaclass_singleton():
    """Compare metaclass singleton with decorator singleton."""
    print("=== Metaclass Singleton Comparison ===")

    log1 = Logger("app")
    log1.log("Started")
    log2 = Logger("other")  # Returns same instance
    log2.log("Continued")

    print(f"log1: {log1}")
    print(f"log2: {log2}")
    print(f"Same object? {log1 is log2}")

    print()
    print("Decorator singleton:")
    print("  + Simple to apply (@singleton)")
    print("  + Works with functools.wraps")
    print("  - isinstance() won't work (returns function)")
    print()
    print("Metaclass singleton:")
    print("  + isinstance() works correctly")
    print("  + More 'proper' OOP approach")
    print("  - More complex to understand")
    print("  - Can't combine with other metaclasses easily")


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    demo_singleton()
    demo_thread_safety()
    demo_metaclass_singleton()
