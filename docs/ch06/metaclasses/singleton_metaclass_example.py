"""
Metaclass Example: Thread-Safe Singleton

A metaclass is a "class of a class" - it controls how classes
are created and how instances are constructed.

This tutorial implements a singleton pattern using a metaclass,
where __call__ on the metaclass intercepts instance creation.

Topics covered:
- Custom metaclass (inheriting from type)
- __init__ on metaclass (called when class is defined)
- __call__ on metaclass (called when class() is invoked)
- Thread-safe double-checked locking
- Comparison with decorator approach

Based on concepts from Python-100-Days example18 and ch06/metaclasses materials.
"""

import threading


# =============================================================================
# Example 1: Singleton Metaclass
# =============================================================================

class SingletonMeta(type):
    """Metaclass that makes any class using it a singleton.

    How it works:
    1. When the class is DEFINED (class Foo(metaclass=SingletonMeta):),
       SingletonMeta.__init__ runs, initializing _instance and _lock.
    2. When Foo() is CALLED to create an instance,
       SingletonMeta.__call__ runs instead of the normal type.__call__.
    3. __call__ checks if an instance already exists (thread-safely).
    """

    def __init__(cls, *args, **kwargs):
        """Called when the class is first defined (not when instantiated)."""
        cls._instance = None
        cls._lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        """Called every time cls() is invoked (instead of creating new instance).

        Uses double-checked locking for thread safety:
        1. Fast check without lock (avoids lock overhead after first creation)
        2. Acquire lock and check again (prevents race condition)
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


# =============================================================================
# Example 2: Using the Singleton Metaclass
# =============================================================================

class DatabaseConnection(metaclass=SingletonMeta):
    """Database connection that should only exist once.

    Using metaclass=SingletonMeta ensures that DatabaseConnection()
    always returns the same instance.
    """

    def __init__(self, host: str = "localhost", port: int = 5432):
        self.host = host
        self.port = port
        self.connected = True

    def __str__(self):
        return f"DB({self.host}:{self.port})"


class AppLogger(metaclass=SingletonMeta):
    """Application logger (separate singleton from DatabaseConnection)."""

    def __init__(self, name: str = "app"):
        self.name = name
        self.entries: list[str] = []

    def log(self, message: str):
        self.entries.append(message)

    def __str__(self):
        return f"Logger('{self.name}', {len(self.entries)} entries)"


# =============================================================================
# Example 3: Demonstrating Singleton Behavior
# =============================================================================

def demo_singleton():
    """Show that the metaclass enforces singleton behavior."""
    print("=== Singleton Metaclass Demo ===")

    # First call creates the instance
    db1 = DatabaseConnection("postgres.example.com", 5432)
    # Second call returns the SAME instance (args ignored)
    db2 = DatabaseConnection("mysql.example.com", 3306)
    # Even __call__ returns the same instance
    db3 = DatabaseConnection.__call__("oracle.example.com", 1521)

    print(f"db1: {db1}")
    print(f"db2: {db2}")
    print(f"db3: {db3}")
    print(f"db1 is db2: {db1 is db2}")
    print(f"db1 is db3: {db1 is db3}")
    print()

    # Different classes have independent singletons
    logger = AppLogger("main")
    print(f"logger: {logger}")
    print(f"logger is db1: {logger is db1}")
    print()


# =============================================================================
# Example 4: isinstance() Works (Unlike Decorator Approach)
# =============================================================================

def demo_isinstance():
    """Show that isinstance works correctly with metaclass singleton."""
    print("=== isinstance() Works Correctly ===")

    db = DatabaseConnection()

    print(f"isinstance(db, DatabaseConnection): {isinstance(db, DatabaseConnection)}")
    print(f"type(db): {type(db).__name__}")
    print(f"type(DatabaseConnection): {type(DatabaseConnection).__name__}")
    print()

    print("Note: With a decorator singleton, isinstance() would fail")
    print("because the decorator replaces the class with a function.")
    print("The metaclass approach preserves the class identity.")
    print()


# =============================================================================
# Example 5: The Metaclass Chain
# =============================================================================

def demo_metaclass_chain():
    """Visualize the metaclass relationship."""
    print("=== Metaclass Chain ===")
    print("""
    Normal chain:    instance -> class -> type (default metaclass)
    Singleton chain: instance -> class -> SingletonMeta -> type

    The chain:
    - db = DatabaseConnection()     # db is an instance
    - type(db) is DatabaseConnection  # class of db
    - type(DatabaseConnection) is SingletonMeta  # metaclass
    - type(SingletonMeta) is type     # meta-metaclass (always type)
    """)

    db = DatabaseConnection()
    print(f"Instance:  {db}")
    print(f"Class:     {type(db).__name__}")
    print(f"Metaclass: {type(type(db)).__name__}")
    print(f"Meta-meta: {type(type(type(db))).__name__}")


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    demo_singleton()
    demo_isinstance()
    demo_metaclass_chain()
