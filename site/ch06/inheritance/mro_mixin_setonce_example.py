"""
Multiple Inheritance: MRO, Diamond Problem, and Mixins

When a class inherits from multiple parents, Python uses the C3
Linearization algorithm to determine Method Resolution Order (MRO).

Topics covered:
- Diamond inheritance problem
- C3 Linearization (MRO)
- Mixin pattern for composable behavior
- SetOnceMixin: preventing key overwrites

Based on concepts from Python-100-Days example17 and ch06/inheritance materials.
"""


# =============================================================================
# Example 1: Diamond Problem and MRO
# =============================================================================

class A:
    def greet(self):
        return 'Hello from A'


class B(A):
    pass  # Inherits A.greet


class C(A):
    def greet(self):
        return 'Hello from C'


class D(B, C):
    pass  # Which greet() does D inherit?


def demo_diamond():
    """Demonstrate the diamond problem and C3 linearization."""
    print("=== Diamond Problem ===")
    print("""
    Class hierarchy:
        A           (defines greet)
       / \\
      B   C         (C overrides greet)
       \\ /
        D           (inherits from both B and C)
    """)

    d = D()
    print(f"D().greet() = '{d.greet()}'")
    print()

    # MRO determines the search order
    print("Method Resolution Order (C3 Linearization):")
    print(f"  D.mro() = {[cls.__name__ for cls in D.mro()]}")
    print()

    print("Python 3 uses C3 algorithm (breadth-first-like):")
    print("  D -> B -> C -> A -> object")
    print("  So D.greet() calls C.greet() because C comes before A in MRO")
    print()


# =============================================================================
# Example 2: SetOnce Mixin
# =============================================================================

class SetOnceMixin:
    """Mixin that prevents overwriting existing keys.

    A mixin is a class designed to be combined with other classes
    via multiple inheritance. It adds a single focused behavior.

    This mixin overrides __setitem__ to raise KeyError if the key
    already exists, enforcing write-once semantics.
    """
    __slots__ = ()  # Mixins typically don't add instance attributes

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(f"Key '{key}' already set (write-once policy)")
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMixin, dict):
    """A dictionary where keys can only be set once.

    MRO: SetOnceDict -> SetOnceMixin -> dict -> object
    When setting a key, SetOnceMixin.__setitem__ runs first,
    then delegates to dict.__setitem__ via super().
    """
    pass


def demo_setonce():
    """Demonstrate the SetOnce mixin."""
    print("=== SetOnce Mixin ===")
    print(f"SetOnceDict MRO: {[c.__name__ for c in SetOnceDict.__mro__]}")
    print()

    config = SetOnceDict()
    config['database'] = 'postgres'
    config['port'] = 5432
    print(f"Config: {config}")

    try:
        config['database'] = 'mysql'  # Raises KeyError
    except KeyError as e:
        print(f"KeyError: {e}")
    print()


# =============================================================================
# Example 3: Composable Mixins
# =============================================================================

class LoggingMixin:
    """Mixin that logs all item assignments."""
    __slots__ = ()

    def __setitem__(self, key, value):
        print(f"  [LOG] Setting '{key}' = {value!r}")
        super().__setitem__(key, value)


class ValidatingMixin:
    """Mixin that validates keys are strings."""
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError(f"Key must be str, got {type(key).__name__}")
        super().__setitem__(key, value)


class StrictDict(ValidatingMixin, LoggingMixin, SetOnceMixin, dict):
    """A dict with validation, logging, and write-once behavior.

    MRO: StrictDict -> ValidatingMixin -> LoggingMixin
         -> SetOnceMixin -> dict -> object

    Each mixin's __setitem__ calls super().__setitem__(),
    creating a chain of responsibility.
    """
    pass


def demo_composable():
    """Show how multiple mixins compose together."""
    print("=== Composable Mixins ===")
    print(f"StrictDict MRO: {[c.__name__ for c in StrictDict.__mro__]}")
    print()

    d = StrictDict()

    # Normal operation: validation -> logging -> set-once -> dict
    d['name'] = 'Alice'
    print(f"Result: {d}")
    print()

    # Try non-string key (ValidatingMixin catches it)
    print("Trying integer key:")
    try:
        d[42] = 'invalid'
    except TypeError as e:
        print(f"  TypeError: {e}")
    print()

    # Try duplicate key (SetOnceMixin catches it)
    print("Trying duplicate key:")
    try:
        d['name'] = 'Bob'
    except KeyError as e:
        print(f"  KeyError: {e}")
    print()


# =============================================================================
# Example 4: Mixin Best Practices
# =============================================================================

def demo_best_practices():
    """Summarize mixin design guidelines."""
    print("=== Mixin Best Practices ===")
    print("""
    1. Single Responsibility: Each mixin adds ONE behavior
    2. No __init__: Mixins should not define __init__
    3. Use __slots__ = (): Mixins shouldn't add instance attributes
    4. Always call super(): Enable cooperative multiple inheritance
    5. Name with 'Mixin' suffix: Makes intent clear
    6. Keep mixins focused and composable
    7. Document MRO expectations
    """)


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    demo_diamond()
    demo_setonce()
    demo_composable()
    demo_best_practices()
