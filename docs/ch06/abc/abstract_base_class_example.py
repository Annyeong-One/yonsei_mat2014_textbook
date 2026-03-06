"""
TUTORIAL: Abstract Base Classes (ABC) - Defining Contracts for Subclasses
==========================================================================

In this tutorial, you'll learn how to use Python's abc module to create
Abstract Base Classes. An ABC is a blueprint that enforces what methods
subclasses MUST implement.

Key concepts:
  1. ABC: A class that cannot be instantiated directly
  2. @abstractmethod: Marks methods that subclasses MUST override
  3. Concrete methods: Can provide default implementation in the ABC
  4. Inheritance: Subclasses must implement all abstract methods

Why use ABC?
  - Enforce a consistent interface across subclasses
  - Prevent accidental incomplete implementations
  - Document what subclasses must do
  - Catch errors at class definition time, not runtime

In this example, we define a Tombola (lottery machine) ABC with:
  - Abstract methods: load() and pick() that subclasses must implement
  - Concrete methods: loaded() and inspect() that use the abstract methods

This demonstrates how abstract methods serve as hooks that concrete methods
depend on, creating a reusable pattern for subclasses.
"""

import abc


# ============ Example 1: Defining an Abstract Base Class ============

if __name__ == "__main__":
    print("=" * 70)
    print("EXAMPLE 1: Creating the Tombola ABC")
    print("=" * 70)

    class Tombola(abc.ABC):
        """Abstract Base Class for a lottery machine (tombola).

        A Tombola must be able to:
        - load() items from an iterable
        - pick() random items and remove them
        - report loaded() status
        - inspect() current contents

        Subclasses MUST implement load() and pick().
        The load() and inspect() methods depend on these abstract methods
        to provide complete functionality.
        """

        @abc.abstractmethod
        def load(self, iterable):
            """Add items from an iterable to the tombola.

            This is an abstract method. Every subclass MUST override it
            with its own implementation. Without it, you cannot instantiate
            the subclass.

            Args:
                iterable: A collection of items to add to the tombola.
            """

        @abc.abstractmethod
        def pick(self):
            """Remove item at random from the tombola, returning it.

            This is an abstract method. Every subclass MUST override it
            with its own implementation.

            Returns:
                A randomly selected item from the tombola.

            Raises:
                LookupError: When the tombola is empty.
            """

        def loaded(self):
            """Return True if there's at least 1 item, False otherwise.

            This is a concrete method. It provides a default implementation
            that uses the abstract method pick() as a hook.

            Note: This method works with ANY subclass that implements
            load() and pick(), making it reusable across all subclasses.
            """
            return bool(self.inspect())

        def inspect(self):
            """Return a sorted tuple with the items currently inside.

            This is a concrete method that uses the abstract methods:
            1. Calls pick() repeatedly to get all items
            2. Calls load() to restore the items after inspection

            This demonstrates how concrete methods can depend on
            abstract methods to provide sophisticated behavior.

            Returns:
                tuple: Sorted tuple of all items in the tombola.
            """
            items = []
            while True:
                try:
                    # Keep picking items until empty
                    items.append(self.pick())
                except LookupError:
                    # Empty - break the loop
                    break

            # Restore the items we removed
            self.load(items)

            # Return sorted tuple of contents
            return tuple(items)


    print(f"\nTombola ABC defined with:")
    print(f"  - Abstract methods: load(), pick()")
    print(f"  - Concrete methods: loaded(), inspect()")
    print(f"\nTrying to instantiate Tombola directly...")

    try:
        tombola = Tombola()
        print(f"  ERROR: This should have failed!")
    except TypeError as e:
        print(f"  Result: TypeError")
        print(f"  Message: {e}")
        print(f"  WHY? ABC classes cannot be instantiated directly")


    # ============ Example 2: Creating a Concrete Subclass ============
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Implementing a concrete subclass (BingoTombola)")
    print("=" * 70)

    import random

    class BingoTombola(Tombola):
        """A Tombola implementation using a list to store items.

        This concrete subclass implements the two abstract methods
        that Tombola requires.
        """

        def __init__(self):
            """Initialize an empty bingo tombola."""
            self._items = []

        def load(self, iterable):
            """Load items from an iterable into the list.

            Args:
                iterable: Items to add to the tombola.
            """
            self._items.extend(iterable)

        def pick(self):
            """Remove and return a random item.

            Returns:
                A random item from _items.

            Raises:
                LookupError: When the list is empty.
            """
            try:
                position = random.randrange(len(self._items))
            except ValueError:
                raise LookupError('pick from empty Tombola') from None
            return self._items.pop(position)

        def __call__(self):
            """Return self for compatibility."""
            return self


    print(f"\nBingoTombola created - a concrete subclass of Tombola")
    print(f"It implements both abstract methods:")
    print(f"  - load(iterable): Stores items in self._items")
    print(f"  - pick(): Removes and returns a random item")

    # Create an instance
    bingo = BingoTombola()
    print(f"\nbingo = BingoTombola()")
    print(f"  Instance created successfully (it's a proper subclass)")


    # ============ Example 3: Using the Concrete Subclass ============
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Using BingoTombola - load and inspect")
    print("=" * 70)

    # Load some items
    numbers = range(1, 7)
    bingo.load(numbers)

    print(f"\nbingo.load(range(1, 7))  # Load numbers 1-6")
    print(f"  Items loaded into tombola")

    # Check if loaded
    print(f"\nbingo.loaded()  # Check if anything is loaded")
    print(f"  Result: {bingo.loaded()}")
    print(f"  WHY? inspect() called pick() and found items")

    # Inspect contents
    contents = bingo.inspect()
    print(f"\nbingo.inspect()  # Get all items without modifying")
    print(f"  Result: {contents}")
    print(f"  Note: Still loaded after inspect (load() restored items)")


    # ============ Example 4: Picking Items and Emptying ============
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Picking items one at a time")
    print("=" * 70)

    bingo2 = BingoTombola()
    bingo2.load(['a', 'b', 'c', 'd', 'e'])

    print(f"\nbingo2.load(['a', 'b', 'c', 'd', 'e'])")
    print(f"bingo2.loaded() = {bingo2.loaded()}")

    print(f"\nPicking 3 items:")
    for i in range(3):
        item = bingo2.pick()
        print(f"  Pick {i+1}: {item}")

    print(f"\nRemaining items via inspect():")
    print(f"  bingo2.inspect() = {bingo2.inspect()}")

    print(f"\nbingo2.loaded() = {bingo2.loaded()}")
    print(f"  Still has items")

    # Pick remaining items
    print(f"\nPicking remaining items until empty:")
    try:
        while True:
            item = bingo2.pick()
            print(f"  Picked: {item}")
    except LookupError as e:
        print(f"  LookupError: {e}")
        print(f"  WHY? No more items in tombola")

    print(f"\nbingo2.loaded() = {bingo2.loaded()}")
    print(f"  Now empty after all picks")


    # ============ Example 5: Why Abstract Methods Matter ============
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Attempted incomplete subclass - this would fail")
    print("=" * 70)

    print(f"\nAttempting to create incomplete subclass:")
    print(f"  class IncompleteTombola(Tombola):")
    print(f"      def load(self, iterable): pass")
    print(f"      # Missing pick() implementation\n")

    try:
        class IncompleteTombola(Tombola):
            def load(self, iterable):
                pass
            # Forgot to implement pick()

        incomplete = IncompleteTombola()
        print(f"  ERROR: This should have failed!")
    except TypeError as e:
        print(f"  Result: TypeError")
        print(f"  Message: {e}")
        print(f"  WHY? Class definition fails if not all abstract methods")
        print(f"       are implemented. This catches errors early!")


    # ============ Example 6: How Concrete Methods Depend on Abstract Methods ============
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Concrete methods using abstract method hooks")
    print("=" * 70)

    print(f"\nThe inspect() method is elegant because:")
    print(f"  1. It's defined once in the ABC")
    print(f"  2. It works for ANY concrete subclass")
    print(f"  3. It 'hooks' into pick() and load()")

    print(f"\nFlow of inspect() for BingoTombola:")
    print(f"  1. Loop: bingo.pick() [abstract hook]")
    print(f"     - Removes items from _items list")
    print(f"     - Raises LookupError when empty")
    print(f"  2. Collect all items into a list")
    print(f"  3. Restore: bingo.load(items) [abstract hook]")
    print(f"     - Puts items back without modification")
    print(f"  4. Return tuple(items)")

    print(f"\nBecause load() and pick() are abstract hooks,")
    print(f"each subclass can have different storage mechanisms")
    print(f"but inspect() works the same way for all of them!")


    # ============ Example 7: Another Subclass - Different Implementation ============
    print("\n" + "=" * 70)
    print("EXAMPLE 7: Alternative subclass with different storage (LotteryTombola)")
    print("=" * 70)

    class LotteryTombola(Tombola):
        """A Tombola implementation using a set instead of a list.

        This shows that different implementations can use different
        internal data structures while satisfying the same interface.
        """

        def __init__(self):
            """Initialize an empty lottery tombola."""
            self._numbers = set()

        def load(self, iterable):
            """Add numbers to the set.

            Args:
                iterable: Numbers to add.
            """
            self._numbers.update(iterable)

        def pick(self):
            """Remove and return a random number.

            Returns:
                A random number from the set.

            Raises:
                LookupError: When the set is empty.
            """
            if not self._numbers:
                raise LookupError('pick from empty LotteryTombola')
            # Convert to list, pick random, remove from set
            value = random.choice(list(self._numbers))
            self._numbers.discard(value)
            return value


    lottery = LotteryTombola()
    lottery.load([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(f"\nlottery = LotteryTombola()")
    print(f"lottery.load(range(1, 11))")

    print(f"\nlottery.loaded() = {lottery.loaded()}")
    print(f"lottery.inspect() = {lottery.inspect()}")

    print(f"\nLotteryTombola uses a different storage mechanism (set)")
    print(f"but provides the SAME interface as BingoTombola!")
    print(f"This is the power of ABC - enforcing a contract.")


    # ============ Example 8: Summary - Why Use ABC? ============
    print("\n" + "=" * 70)
    print("EXAMPLE 8: Summary - Benefits of Abstract Base Classes")
    print("=" * 70)

    print(f"\nBenefits of ABC:")
    print(f"  1. CONTRACT: Forces subclasses to implement required methods")
    print(f"     - TypeError raised at class definition if incomplete")
    print(f"     - Errors caught early, not at runtime")

    print(f"  2. REUSABILITY: Concrete methods work for all subclasses")
    print(f"     - inspect() works the same for BingoTombola and LotteryTombola")
    print(f"     - Hooks (load, pick) allow customization")

    print(f"  3. DOCUMENTATION: Clear what subclasses must do")
    print(f"     - Docstrings on abstract methods guide implementers")
    print(f"     - Self-documenting code")

    print(f"  4. CONSISTENCY: All subclasses have same interface")
    print(f"     - Users know what methods exist")
    print(f"     - Polymorphism works correctly")

    print(f"\nWhen to use ABC:")
    print(f"  - Designing a framework or library")
    print(f"  - Multiple related classes should follow same interface")
    print(f"  - Want to prevent incomplete implementations")
    print(f"  - Need polymorphic behavior")

    print(f"\n" + "=" * 70)
