"""
TUTORIAL: The @property Decorator - Computed Attributes

This tutorial teaches you how to use the @property decorator to create
computed attributes that look like simple instance attributes but actually
run custom code. Properties let you write foo.bar instead of foo.get_bar()
while still controlling access, validation, and computation.

This is one of Python's most useful and commonly used features.

Key Learning Goals:
  - Understand why properties are useful
  - Implement basic properties with getters and setters
  - Learn property documentation and introspection
  - See how properties enforce encapsulation without boilerplate
  - Understand performance implications
"""

if __name__ == "__main__":

    print("=" * 70)
    print("TUTORIAL: The @property Decorator - Computed Attributes")
    print("=" * 70)

    # ============ EXAMPLE 1: The Problem - Boilerplate Without Properties ============
    print("\n# Example 1: Without Properties - The Verbose Way")
    print("=" * 70)

    class BankAccountBad:
        """
        Bank account WITHOUT properties (the verbose, non-Pythonic way).

        This is how you might write code in Java or C#. Not in Python!
        """

        def __init__(self, name, balance):
            self._name = name
            self._balance = balance

        def get_name(self):
            """Get the account holder name."""
            return self._name

        def set_name(self, value):
            """Set the account holder name."""
            if not isinstance(value, str) or not value.strip():
                raise ValueError("Name must be non-empty string")
            self._name = value

        def get_balance(self):
            """Get the current balance."""
            return self._balance

        def set_balance(self, value):
            """Set the balance (with validation)."""
            if value < 0:
                raise ValueError("Balance cannot be negative")
            self._balance = value


    print("Without properties, you write:")
    account = BankAccountBad("Alice", 1000)
    print(f"Name: {account.get_name()}")
    print(f"Balance: {account.get_balance()}")
    print()

    print("This is verbose and repetitive!")
    print("Users have to remember: get_name(), get_balance(), etc.")
    print("And we lost the nice attribute syntax: account.name")
    print("""
    WHY THIS IS BAD:
        - Too much boilerplate (get_/set_ methods)
        - Ugly syntax: account.get_name() vs account.name
        - Hard to add validation later (breaks API)
        - Not Pythonic (Python prefers simple attribute access)
    """)

    # ============ EXAMPLE 2: Basic Property - Read-Only ============
    print("\n# Example 2: Basic Property - Read-Only Access")
    print("=" * 70)

    class Person:
        """
        Person class with a read-only name property.

        The @property decorator turns a method into a readable attribute.
        """

        def __init__(self, name):
            self._name = name  # Private attribute (convention: leading underscore)

        @property
        def name(self):
            """
            The name property.

            After @property decorator, you access this as person.name
            (attribute syntax) not person.name() (method syntax).

            The method becomes a property getter.
            """
            print(f"  [Getting name: {self._name}]")  # Show that code runs
            return self._name


    person = Person("Bob")

    print(f"Accessing person.name (attribute syntax, not method):")
    name = person.name
    print(f"Got: {name}")
    print()

    print("Try to set it:")
    try:
        person.name = "Charlie"
    except AttributeError as e:
        print(f"  Error: {e}")

    print("""
    WHY: The @property decorator makes the method look like an attribute.
    You write person.name not person.name(). Clean and intuitive!

    Since we only have @property (getter), the attribute is read-only.
    Attempting to set it raises AttributeError.
    """)

    # ============ EXAMPLE 3: Property with Setter ============
    print("\n# Example 3: Property with Getter and Setter")
    print("=" * 70)

    class Rectangle:
        """
        Rectangle with width and height properties that allow getting and setting.

        Use @property for the getter, @name.setter for the setter.
        Both run custom code (like validation).
        """

        def __init__(self, width, height):
            self._width = width
            self._height = height

        @property
        def width(self):
            """Get the width."""
            return self._width

        @width.setter
        def width(self, value):
            """
            Set the width with validation.

            The setter method name must match the property name.
            The decorator is @name.setter, not @property.
            """
            if not isinstance(value, (int, float)):
                raise TypeError("Width must be a number")
            if value <= 0:
                raise ValueError("Width must be positive")
            print(f"  [Setting width to {value}]")
            self._width = value

        @property
        def height(self):
            """Get the height."""
            return self._height

        @height.setter
        def height(self, value):
            """Set the height with validation."""
            if not isinstance(value, (int, float)):
                raise TypeError("Height must be a number")
            if value <= 0:
                raise ValueError("Height must be positive")
            print(f"  [Setting height to {value}]")
            self._height = value

        @property
        def area(self):
            """
            Computed property: area is calculated, not stored.

            This is read-only (no setter) - it's always computed from width/height.
            """
            return self._width * self._height


    rect = Rectangle(3, 4)

    print(f"Width: {rect.width}, Height: {rect.height}")
    print(f"Area: {rect.area} (computed, not stored)")
    print()

    print("Setting width to 5:")
    rect.width = 5
    print(f"New area: {rect.area}")
    print()

    print("Validation works:")
    try:
        rect.width = -10
    except ValueError as e:
        print(f"  Error: {e}")

    try:
        rect.height = "invalid"
    except TypeError as e:
        print(f"  Error: {e}")

    print("""
    WHY: Properties let you:
        1. Use attribute syntax (rect.width not rect.get_width())
        2. Run validation code transparently
        3. Compute values on-the-fly (rect.area)
        4. Control access (read-only, write-only, or both)
        5. Change implementation without breaking the API

    If you later want to add validation or computation, users don't know
    or care - they still use attribute syntax.
    """)

    # ============ EXAMPLE 4: Property Documentation ============
    print("\n# Example 4: Property Documentation and Introspection")
    print("=" * 70)

    class Foo:
        """Example class with documented properties."""

        @property
        def bar(self):
            """
            The bar attribute.

            This docstring becomes the property's documentation.
            Visible via help() and IDE tooltips.
            """
            return self.__dict__.get('bar', 'default')

        @bar.setter
        def bar(self, value):
            self.__dict__['bar'] = value


    # Access property documentation
    print("Property documentation:")
    print(f"  Foo.bar.__doc__ = {repr(Foo.bar.__doc__)}")
    print()

    foo = foo_instance = Foo()

    # Inspect properties
    print("Introspection:")
    print(f"  type(Foo.bar) = {type(Foo.bar)}")
    print(f"  isinstance(Foo.bar, property) = {isinstance(Foo.bar, property)}")
    print()

    # Help on property
    print("Help for property:")
    print(f"  Foo.bar.fget = {Foo.bar.fget}")  # getter function
    print(f"  Foo.bar.fset = {Foo.bar.fset}")  # setter function
    print(f"  Foo.bar.fdel = {Foo.bar.fdel}")  # deleter function (None if not defined)

    print("""
    WHY: Properties have introspectable metadata:
        - __doc__: The docstring
        - fget, fset, fdel: The getter, setter, deleter functions
        - You can check isinstance(attr, property) to detect properties

    This is useful for frameworks and tools that need to understand
    your class structure.
    """)

    # ============ EXAMPLE 5: Using __dict__ Directly (Storage Pattern) ============
    print("\n# Example 5: Storing in __dict__ (Instance Dictionary)")
    print("=" * 70)

    class Thermostat:
        """
        Thermostat with temperature property that stores in __dict__.

        The common pattern: store attributes in self.__dict__ instead of
        private attributes like self._temp.
        """

        @property
        def celsius(self):
            """
            Get temperature in Celsius.

            This gets/sets directly in the __dict__ dictionary.
            """
            return self.__dict__.get('celsius', 20)  # default 20 degrees

        @celsius.setter
        def celsius(self, value):
            """Set temperature with bounds checking."""
            if not -50 <= value <= 50:
                raise ValueError("Temperature must be between -50 and 50 Celsius")
            self.__dict__['celsius'] = value

        @property
        def fahrenheit(self):
            """Get temperature in Fahrenheit (computed)."""
            return (self.celsius * 9/5) + 32

        @fahrenheit.setter
        def fahrenheit(self, value):
            """Set temperature from Fahrenheit."""
            self.celsius = (value - 32) * 5/9


    thermo = Thermostat()

    print(f"Default temperature: {thermo.celsius}C = {thermo.fahrenheit}F")
    print()

    print("Setting to 25C:")
    thermo.celsius = 25
    print(f"  {thermo.celsius}C = {thermo.fahrenheit}F")
    print()

    print("Setting to 68F:")
    thermo.fahrenheit = 68
    print(f"  {thermo.celsius:.1f}C = {thermo.fahrenheit:.1f}F")
    print()

    print("Instance __dict__:")
    print(f"  {thermo.__dict__}")

    print("""
    WHY: Using __dict__ directly is clean and idiomatic Python.
    You don't need separate private attributes when properties manage
    access to __dict__.

    PATTERN:
        @property
        def attr(self):
            return self.__dict__.get('attr', default)

        @attr.setter
        def attr(self, value):
            self.__dict__['attr'] = value
    """)

    # ============ EXAMPLE 6: Common Anti-Pattern - Avoid This ============
    print("\n# Example 6: Anti-Pattern - Storing in Private Attribute")
    print("=" * 70)

    class BadDesign:
        """Example of property anti-pattern (stores in _attr for no reason)."""

        def __init__(self):
            self._value = None

        @property
        def value(self):
            # Unnecessary indirection!
            return self._value

        @value.setter
        def value(self, x):
            self._value = x  # Just copying to self._value. Why?


    print("This is an anti-pattern - the property adds no value:")
    print("  - No validation")
    print("  - No computation")
    print("  - Just stores in _value")
    print()

    print("""
    BETTER: Just use self.value = x directly

    If you later need validation:
        @property
        def value(self):
            return self.__dict__.get('value')

        @value.setter
        def value(self, x):
            if not validate(x):
                raise ValueError("Invalid")
            self.__dict__['value'] = x

    Only use @property when you need custom behavior (validation,
    computation, access control). Don't use it for trivial getters/setters.
    """)

    # ============ EXAMPLE 7: Deleter and Other Tricks ============
    print("\n# Example 7: Property Deleter - Handling Deletion")
    print("=" * 70)

    class Cache:
        """
        Cache with a value property that can be deleted.

        @name.deleter defines what happens when you delete the property.
        """

        def __init__(self):
            self._value = None
            self._cached = False

        @property
        def value(self):
            """Get the cached value."""
            return self._value

        @value.setter
        def value(self, x):
            """Set and mark as cached."""
            self._value = x
            self._cached = True

        @value.deleter
        def value(self):
            """Delete and invalidate cache."""
            print("  [Cache invalidated]")
            self._value = None
            self._cached = False


    cache = Cache()

    print("Setting cache value:")
    cache.value = "important data"
    print(f"  Value: {cache.value}, Cached: {cache._cached}")
    print()

    print("Deleting cache:")
    del cache.value
    print(f"  Value: {cache.value}, Cached: {cache._cached}")

    print("""
    WHY: The deleter lets you handle del obj.property.

    COMMON USES:
        - Invalidate caches
        - Close resources
        - Reset state
        - Trigger cleanup

    Most properties don't need deleters, but they're there when needed.
    """)

    # ============ EXAMPLE 8: Lazy Evaluation with Properties ============
    print("\n# Example 8: Lazy Evaluation - Compute Only When Needed")
    print("=" * 70)

    class ExpensiveComputation:
        """
        Properties for lazy evaluation: compute only when accessed.

        This pattern defers expensive work until the value is actually needed.
        """

        def __init__(self, name):
            self.name = name
            self._result = None  # None means "not computed yet"

        @property
        def result(self):
            """
            Compute expensive result, but only on first access.

            Subsequent accesses return the cached result.
            """
            if self._result is None:
                print(f"  [Computing result for {self.name}...]")
                import time
                time.sleep(0.1)  # Simulate expensive work
                self._result = f"Result of {self.name}"
            else:
                print(f"  [Using cached result for {self.name}]")
            return self._result


    obj = ExpensiveComputation("task")

    print("First access (computes):")
    r1 = obj.result
    print(f"  Got: {r1}")
    print()

    print("Second access (cached):")
    r2 = obj.result
    print(f"  Got: {r2}")

    print("""
    WHY: Lazy evaluation defers expensive computations:
        - If the result is never accessed, work isn't done
        - If accessed multiple times, work is done once
        - Client code uses simple property access

    PATTERN:
        @property
        def expensive_attr(self):
            if self._cached_value is None:
                self._cached_value = do_expensive_work()
            return self._cached_value
    """)

    # ============ EXAMPLE 9: Properties vs Methods ============
    print("\n# Example 9: Choosing Between Properties and Methods")
    print("=" * 70)

    print("""
    USE @property WHEN:
        ✓ Value looks like an attribute (singular noun)
        ✓ Access is fast (cached or simple computation)
        ✓ Logically feels like an attribute (name, age, area)
        ✓ No side effects beyond computation
        ✓ You might want to change to simple attribute later

    USE A METHOD WHEN:
        ✓ Operation name is a verb (get_user(), save())
        ✓ Computation is expensive (database query)
        ✓ Has side effects (I/O, modifies state)
        ✓ Takes parameters (get(key), find(pattern))
        ✓ Might take variable time (network request)

    EXAMPLES:

    PROPERTY:
        class Circle:
            @property
            def area(self):  # Noun, fast, pure computation
                return math.pi * self.radius ** 2

    METHOD:
        class Database:
            def query(self, sql):  # Verb, expensive, I/O
                return self.execute(sql)

        class User:
            def save(self):  # Verb, side effects
                self.db.insert(self)

    PROPERTY:
        class Point:
            @property
            def magnitude(self):  # Noun, fast, pure
                return math.hypot(self.x, self.y)

    METHOD:
        class API:
            def fetch(self, url):  # Verb, expensive, I/O
                return requests.get(url)
    """)

    # ============ EXAMPLE 10: Summary - The Property Checklist ============
    print("\n# Example 10: Property Implementation Checklist")
    print("=" * 70)

    class CompleteExample:
        """Example showing all property features together."""

        def __init__(self, name):
            self._name = name
            self._active = True

        @property
        def name(self):
            """
            Get the name.

            Always include documentation for properties!
            """
            return self._name

        @name.setter
        def name(self, value):
            """Set name with validation."""
            if not isinstance(value, str) or not value.strip():
                raise ValueError("Name must be non-empty string")
            self._name = value

        @name.deleter
        def name(self):
            """Deleting name disables the object."""
            self._active = False

        @property
        def is_active(self):
            """Read-only property (no setter)."""
            return self._active


    print("Complete example:")
    obj = CompleteExample("Alice")
    print(f"Name: {obj.name}")
    print(f"Active: {obj.is_active}")
    print()

    obj.name = "Bob"
    print(f"After setting name: {obj.name}")
    print()

    del obj.name
    print(f"After deleting name: {obj.is_active}")

    print("""
    PROPERTY CHECKLIST:
        ✓ Use @property for getter
        ✓ Use @name.setter for setter (if needed)
        ✓ Use @name.deleter for deleter (rarely needed)
        ✓ Store in __dict__ or private attribute
        ✓ Validate in setter
        ✓ Include docstring
        ✓ Handle None defaults gracefully
        ✓ Make computation fast or lazy-load
        ✓ Don't use for expensive I/O (use methods instead)
        ✓ Document return type in docstring

    PERFORMANCE:
        - Properties have slightly more overhead than attributes
        - But far less than method calls
        - Use lazy-loading for expensive computations
        - Cache results when appropriate
    """)

    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS")
    print("=" * 70)
    print("""
    1. PROPERTIES LOOK LIKE ATTRIBUTES: @property makes methods look like
       simple attributes. You write obj.name not obj.name().

    2. POWERFUL ENCAPSULATION: Properties let you validate, compute, or
       control access without breaking the API.

    3. CHANGE IMPLEMENTATION WITHOUT BREAKING CODE: Start with simple
       attributes. Add @property later if you need custom behavior.

    4. FOLLOW NAMING CONVENTIONS: Name properties like nouns (name, area,
       is_active) and methods like verbs (get_data(), save()).

    5. USE __dict__ STORAGE: Store properties in self.__dict__ directly
       for a clean, idiomatic pattern.

    6. DOCUMENT YOUR PROPERTIES: Include docstrings explaining what the
       property does, its type, and any constraints.

    7. LAZY-LOAD EXPENSIVE COMPUTATIONS: Cache results to avoid recomputing
       on every access.

    8. DON'T OVERUSE PROPERTIES: Only use them when you need custom behavior.
       Simple attributes are fine as-is.

    9. PROPERTIES ARE PYTHONIC: They're one of Python's most elegant features.
       Used everywhere in professional code.

    10. COMBINATION WITH OTHER FEATURES: Properties work great with
        descriptors, metaclasses, and other advanced features - but you
        usually don't need them.
    """)
