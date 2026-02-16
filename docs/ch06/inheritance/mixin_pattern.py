"""
TUTORIAL: Mixin Pattern - Adding Functionality Through Multiple Inheritance
============================================================================

In this tutorial, you'll learn about the Mixin Pattern, a powerful technique
for adding functionality to classes without using traditional inheritance.

What is a Mixin?
  - A class designed to provide a specific piece of functionality
  - Not meant to stand alone (doesn't define the core behavior)
  - Combined with other classes through multiple inheritance
  - Provides methods that enhance or modify the behavior of other classes

Key characteristics:
  1. Mixins are combined in specific positions in the inheritance order
  2. They typically override specific methods to add functionality
  3. They use super() to allow chaining with other mixins
  4. They're small, focused, and reusable across different classes

In this example:
  - UpperCaseMixin overrides key methods (__setitem__, __getitem__, get, etc.)
  - These methods transform string keys to uppercase
  - UpperDict combines the mixin with dict functionality
  - UpperCounter combines the mixin with Counter functionality

The power: With ONE mixin class, we enhance TWO different collection types!
"""

import collections


# ============ Example 1: The UpperCaseMixin ============
print("=" * 70)
print("EXAMPLE 1: Defining UpperCaseMixin - case-insensitive string keys")
print("=" * 70)

def _upper(key):
    """Helper function to uppercase a key if it's a string.

    This function safely handles non-string keys (like integers)
    by returning them unchanged if they don't support .upper().

    Args:
        key: Any value, could be a string or something else.

    Returns:
        The uppercased key (if string) or the original key.
    """
    try:
        return key.upper()
    except AttributeError:
        # Not a string (e.g., int, tuple) - return as-is
        return key


class UpperCaseMixin:
    """Mixin that makes string keys case-insensitive by uppercasing them.

    This mixin overrides four key methods to uppercase all string keys:
    1. __setitem__: When setting items (d[key] = value)
    2. __getitem__: When getting items (d[key])
    3. get: When using .get(key, default)
    4. __contains__: When checking membership (key in d)

    Why a mixin?
    - We want to add this behavior to multiple collection types
    - Instead of creating two separate subclasses, one mixin handles both
    - UpperDict and UpperCounter both benefit from the same mixin code

    How it works:
    - All methods call _upper(key) before calling super()
    - super() passes the uppercased key to the actual implementation
    - This lets dict and Counter handle the uppercased keys normally
    """

    def __setitem__(self, key, item):
        """Store item with uppercased key.

        When you do: d['hello'] = value
        Internally: super().__setitem__('HELLO', value)

        Args:
            key: The key to store under (will be uppercased if string).
            item: The value to store.
        """
        super().__setitem__(_upper(key), item)

    def __getitem__(self, key):
        """Retrieve item by uppercased key.

        When you do: value = d['hello']
        Internally: super().__getitem__('HELLO')

        Args:
            key: The key to look up (will be uppercased if string).

        Returns:
            The value associated with the uppercased key.
        """
        return super().__getitem__(_upper(key))

    def get(self, key, default=None):
        """Get item with optional default.

        When you do: d.get('hello', 'default')
        Internally: super().get('HELLO', 'default')

        Args:
            key: The key to look up (will be uppercased if string).
            default: Value returned if key not found.

        Returns:
            The value associated with the uppercased key, or default.
        """
        return super().get(_upper(key), default)

    def __contains__(self, key):
        """Check if key exists (case-insensitive).

        When you do: 'hello' in d
        Internally: super().__contains__('HELLO')

        Args:
            key: The key to check (will be uppercased if string).

        Returns:
            True if the uppercased key exists, False otherwise.
        """
        return super().__contains__(_upper(key))


print(f"\nUpperCaseMixin defined with:")
print(f"  - __setitem__: Uppercases key before storing")
print(f"  - __getitem__: Uppercases key before retrieving")
print(f"  - get: Uppercases key before looking up")
print(f"  - __contains__: Uppercases key before checking membership")


# ============ Example 2: UpperDict - Mixin + UserDict ============
print("\n" + "=" * 70)
print("EXAMPLE 2: UpperDict - Combining mixin with UserDict")
print("=" * 70)

class UpperDict(UpperCaseMixin, collections.UserDict):
    """A dict-like object with case-insensitive string keys.

    Inheritance order:
    1. UpperCaseMixin (provides case-insensitive behavior)
    2. UserDict (provides dict functionality)

    When a method like __setitem__ is called:
    1. Python looks in UpperDict (not found)
    2. Then UpperCaseMixin (found!)
    3. UpperCaseMixin.super().__setitem__ calls UserDict.__setitem__
    4. UserDict stores the item normally

    Why UserDict instead of dict?
    - dict doesn't allow method overriding (implemented in C)
    - UserDict is a pure Python wrapper that allows subclassing
    """
    pass


print(f"\nUpperDict created: UpperCaseMixin + UserDict")
print(f"Result: Dict with case-insensitive string keys")

# Create and use an UpperDict
d = UpperDict([('a', 'letter A'), (2, 'digit two')])

print(f"\nd = UpperDict([('a', 'letter A'), (2, 'digit two')])")
print(f"  Keys stored: {list(d.keys())}")

print(f"\nSetting items (case-insensitive):")
print(f"  d['b'] = 'letter B'")
d['b'] = 'letter B'

print(f"\nChecking membership (case-insensitive):")
print(f"  'b' in d = {('b' in d)}  # lowercase works")
print(f"  'B' in d = {('B' in d)}  # uppercase works")
print(f"  'z' in d = {('z' in d)}  # not in dict")

print(f"\nRetrieving values (case-insensitive):")
print(f"  d['a'] = '{d['a']}'  # lowercase works")
print(f"  d['A'] = '{d['A']}'  # uppercase works")

print(f"\nUsing get() (case-insensitive):")
print(f"  d.get('A') = '{d.get('A')}'")
print(f"  d.get('B') = '{d.get('B')}'")
print(f"  d.get('z', 'not found') = '{d.get('z', 'not found')}'")

print(f"\nInteger keys are unaffected:")
print(f"  d[2] = '{d[2]}'  (integers don't get uppercased)")
print(f"  Keys now: {list(d.keys())}")


# ============ Example 3: UpperCounter - Same Mixin, Different Class ============
print("\n" + "=" * 70)
print("EXAMPLE 3: UpperCounter - Same mixin, different parent class")
print("=" * 70)

class UpperCounter(UpperCaseMixin, collections.Counter):
    """A Counter with case-insensitive string keys.

    Same UpperCaseMixin, but combined with Counter instead of UserDict!
    This demonstrates the power of mixins: one mixin, multiple uses.

    Counter counts occurrences of items. With the mixin, it counts
    case-insensitively, treating 'a' and 'A' as the same key.
    """
    pass


print(f"\nUpperCounter created: UpperCaseMixin + Counter")
print(f"Result: Counter with case-insensitive string keys")

# Create and use an UpperCounter
c = UpperCounter('BaNanA')

print(f"\nc = UpperCounter('BaNanA')")
print(f"  Internal storage (all uppercase): {dict(c)}")

print(f"\nmost_common():")
print(f"  c.most_common() = {c.most_common()}")
print(f"  A=3, N=2, B=1 (case-insensitive counting)")

print(f"\nAccessing counts (case-insensitive):")
print(f"  c['a'] = {c['a']}  (lowercase works)")
print(f"  c['A'] = {c['A']}  (uppercase works)")
print(f"  c['b'] = {c['b']}  (lowercase)")

print(f"\nAdding items (case-insensitive):")
c['a'] += 1
print(f"  c['a'] += 1")
print(f"  c.most_common() = {c.most_common()}")
print(f"  'A' count is now 4 (merged with 'a')")


# ============ Example 4: How Mixin Methods Work ============
print("\n" + "=" * 70)
print("EXAMPLE 4: Understanding how mixin method delegation works")
print("=" * 70)

print(f"\nExecution flow for d['hello'] = 'world':")
print(f"  1. User code: d['hello'] = 'world'")
print(f"  2. Python calls: UpperDict.__setitem__(d, 'hello', 'world')")
print(f"  3. Not in UpperDict, check MRO:")
print(f"     UpperDict.__mro__ = {UpperDict.__mro__}")
print(f"  4. Found in UpperCaseMixin:")
print(f"     def __setitem__(self, key, item):")
print(f"         super().__setitem__(_upper(key), item)")
print(f"  5. _upper('hello') → 'HELLO'")
print(f"  6. super().__setitem__('HELLO', 'world')")
print(f"     (super() refers to next in MRO: UserDict)")
print(f"  7. UserDict.__setitem__ stores key='HELLO', value='world'")

print(f"\nExecution flow for value = d['hello']:")
print(f"  1. User code: value = d['hello']")
print(f"  2. Python calls: UpperDict.__getitem__(d, 'hello')")
print(f"  3. Found in UpperCaseMixin:")
print(f"     return super().__getitem__(_upper(key))")
print(f"  4. _upper('hello') → 'HELLO'")
print(f"  5. super().__getitem__('HELLO')")
print(f"  6. UserDict.__getitem__ retrieves and returns 'world'")


# ============ Example 5: Mixin Benefits ============
print("\n" + "=" * 70)
print("EXAMPLE 5: Benefits of the Mixin Pattern")
print("=" * 70)

print(f"\nDRY (Don't Repeat Yourself):")
print(f"  - Without mixin: would need two classes")
print(f"    class UpperDict(dict): ... (with all 4 methods)")
print(f"    class UpperCounter(Counter): ... (with same 4 methods)")
print(f"  - With mixin: write once, use twice")
print(f"    UpperCaseMixin (1 definition)")
print(f"    UpperDict = UpperCaseMixin + UserDict")
print(f"    UpperCounter = UpperCaseMixin + Counter")

print(f"\nComposability:")
print(f"  - Could create UpperSet = UpperCaseMixin + set")
print(f"  - Could create UpperDefaultDict = UpperCaseMixin + defaultdict")
print(f"  - Single mixin works with any dict-like class")

print(f"\nSeparation of Concerns:")
print(f"  - UpperCaseMixin: handles key transformation")
print(f"  - UserDict/Counter: handles storage")
print(f"  - Each class has a single responsibility")

print(f"\nFlexibility:")
print(f"  - Can be combined with other mixins too")
print(f"  - Can be used with future collection types")


# ============ Example 6: Mixin Pattern in Real Code ============
print("\n" + "=" * 70)
print("EXAMPLE 6: Real-world mixin example")
print("=" * 70)

class ReprMixin:
    """Mixin that adds a nice string representation."""
    def __repr__(self):
        items = ', '.join(f'{k}={v!r}' for k, v in self.items())
        return f'{self.__class__.__name__}({{{items}}})'

class CaselessDict(UpperCaseMixin, ReprMixin, collections.UserDict):
    """UserDict with case-insensitive keys AND nice repr!"""
    pass

cd = CaselessDict([('Name', 'Alice'), ('AGE', 30)])
print(f"\ncd = CaselessDict([('Name', 'Alice'), ('AGE', 30)])")
print(f"  repr(cd) = {repr(cd)}")
print(f"  cd['name'] = '{cd['name']}'  (case-insensitive)")
print(f"  cd['age'] = {cd['age']}  (case-insensitive)")

print(f"\nWe combined TWO mixins:")
print(f"  - UpperCaseMixin: case-insensitive access")
print(f"  - ReprMixin: nice string representation")
print(f"  - Result: a fully-featured case-insensitive dict")


# ============ Example 7: When to Use Mixins ============
print("\n" + "=" * 70)
print("EXAMPLE 7: Mixin Pattern Best Practices")
print("=" * 70)

print(f"\nUse mixins when:")
print(f"  1. Adding functionality to multiple unrelated classes")
print(f"  2. The functionality is orthogonal (doesn't create hierarchy)")
print(f"  3. Code would be duplicated across classes")
print(f"  4. You want composition over inheritance")

print(f"\nDon't use mixins when:")
print(f"  1. Creating a primary class hierarchy (use inheritance)")
print(f"  2. The mixin would be used alone (needs a main class)")
print(f"  3. Mixing in creates unclear code or confusing MRO")

print(f"\nMixin naming convention:")
print(f"  - Typically end with 'Mixin' (UpperCaseMixin, ReprMixin)")
print(f"  - Or end with descriptor (TimestampedMixin, ValidatedMixin)")
print(f"  - Helps readers understand they're not primary classes")

print(f"\nMixin placement in inheritance:")
print(f"  - Usually: YourMixin, BaseClass")
print(f"  - Mixin comes FIRST so its methods are found first")
print(f"  - super() in mixin calls the next class in MRO")

print(f"\n" + "=" * 70)
