"""
TUTORIAL: Method Resolution Order (MRO) - Understanding the Diamond Problem
===========================================================================

In this tutorial, you'll learn how Python's Method Resolution Order (MRO)
handles the "diamond problem" in multiple inheritance.

The Diamond Problem:
  A class (Leaf) inherits from two classes (A and B) which both inherit from
  a common parent (Root). When you call a method on Leaf, which version runs?
  This is the diamond problem.

Python uses C3 Linearization to solve this:
  1. Each class is visited in a specific order
  2. Each class appears only once in the order
  3. A class never appears before its parents
  4. The order respects the order in which parents are listed

Key Insight: super() uses MRO to call the next method in the chain.
This allows cooperative multiple inheritance where methods can be properly
delegated up the inheritance hierarchy.

In this example, we see:
  - How print(ClassName.__mro__) shows the resolution order
  - How super() uses MRO to call methods
  - Which methods get called from which classes
  - Why the order matters
"""


# ============ Example 1: Defining the Diamond Inheritance Hierarchy ============
print("=" * 70)
print("EXAMPLE 1: Diamond inheritance - Root > A, B > Leaf")
print("=" * 70)

class Root:
    """The common parent at the top of the diamond.

    Both A and B inherit from Root. Methods here are called when
    neither A, B, nor Leaf override them.
    """
    def ping(self):
        print(f'{self}.ping() in Root')

    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'


class A(Root):
    """Left side of the diamond.

    Inherits from Root. Both ping() and pong() use super() to call
    the parent implementation, continuing the method chain.
    """
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()


class B(Root):
    """Right side of the diamond.

    Inherits from Root. ping() calls super(), but pong() does NOT.
    This demonstrates how different classes can handle the chain differently.
    """
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')
        # Note: No super().pong() call - chain stops here


class Leaf(A, B):
    """Bottom of the diamond - inherits from both A and B.

    Leaf specifies inheritance order: A first, then B.
    This order affects the MRO.
    """
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()


print(f"\nDiamond hierarchy defined:")
print(f"         Root")
print(f"        /    \\")
print(f"       A      B")
print(f"        \\    /")
print(f"         Leaf")
print(f"\nClass definitions:")
print(f"  class Root: ping(), pong()")
print(f"  class A(Root): ping() with super(), pong() with super()")
print(f"  class B(Root): ping() with super(), pong() WITHOUT super()")
print(f"  class Leaf(A, B): ping() with super()")


# ============ Example 2: Understanding the Method Resolution Order ============
print("\n" + "=" * 70)
print("EXAMPLE 2: Method Resolution Order (MRO)")
print("=" * 70)

print(f"\nLeaf.__mro__ shows the order methods are looked up:")
mro = Leaf.__mro__
print(f"  {Leaf.__mro__}")

print(f"\nBreaking it down:")
for i, cls in enumerate(mro):
    print(f"  {i}. {cls}")

print(f"\nWhat this means:")
print(f"  - When Leaf.method() is called, Python looks in Leaf first")
print(f"  - Then A (from Leaf(A, B) left-to-right order)")
print(f"  - Then B")
print(f"  - Then Root")
print(f"  - Finally object (implicit parent of all classes)")

print(f"\nWhy this order?")
print(f"  1. Leaf inherits from A first, so A has priority")
print(f"  2. A and B both inherit from Root, but Root comes after both")
print(f"  3. This respects the inheritance hierarchy")
print(f"  4. C3 Linearization ensures consistency")


# ============ Example 3: Calling ping() - Method Chain with super() ============
print("\n" + "=" * 70)
print("EXAMPLE 3: Calling ping() - tracing the super() chain")
print("=" * 70)

leaf1 = Leaf()
print(f"\nleaf1 = Leaf()")
print(f"leaf1.ping()  # Trace the method chain:")
print()
leaf1.ping()

print(f"\nExplanation of ping() call chain:")
print(f"  1. Leaf.ping() called")
print(f"     - Prints: '<instance of Leaf>.ping() in Leaf'")
print(f"     - Calls: super().ping()")
print(f"     - super() uses MRO: next class after Leaf is A")
print(f"\n  2. A.ping() called via super()")
print(f"     - Prints: '<instance of Leaf>.ping() in A'")
print(f"     - Calls: super().ping()")
print(f"     - super() uses MRO: next class after A is B")
print(f"\n  3. B.ping() called via super()")
print(f"     - Prints: '<instance of Leaf>.ping() in B'")
print(f"     - Calls: super().ping()")
print(f"     - super() uses MRO: next class after B is Root")
print(f"\n  4. Root.ping() called via super()")
print(f"     - Prints: '<instance of Leaf>.ping() in Root'")
print(f"     - No super() call, chain ends")


# ============ Example 4: Calling pong() - Super Chain Stops Early ============
print("\n" + "=" * 70)
print("EXAMPLE 4: Calling pong() - where the super() chain stops")
print("=" * 70)

print(f"\nleaf1.pong()  # Trace the pong() chain:")
print()
leaf1.pong()

print(f"\nExplanation of pong() call chain:")
print(f"  1. Leaf doesn't override pong(), so MRO looks further")
print(f"     - Next class with pong() is A")
print(f"\n  2. A.pong() called")
print(f"     - Prints: '<instance of Leaf>.pong() in A'")
print(f"     - Calls: super().pong()")
print(f"     - super() uses MRO: next class is B")
print(f"\n  3. B.pong() called via super()")
print(f"     - Prints: '<instance of Leaf>.pong() in B'")
print(f"     - NOTE: No super().pong() call!")
print(f"     - Chain STOPS here, Root.pong() is never called!")

print(f"\nKey insight:")
print(f"  - A calls super(), so chain continues to B")
print(f"  - B does NOT call super(), so chain stops")
print(f"  - Root.pong() is never reached")
print(f"  - This is a design choice - B can intentionally end the chain")


# ============ Example 5: MRO Affects Behavior ============
print("\n" + "=" * 70)
print("EXAMPLE 5: MRO affects which implementation runs")
print("=" * 70)

print(f"\nWhat if we changed Leaf(A, B) to Leaf(B, A)?")
print(f"  class Leaf(B, A):  # B first, then A")
print(f"      def ping(self):")
print(f"          print(f'{{self}}.ping() in Leaf')")
print(f"          super().ping()")

class LeafReversed(B, A):
    """Same as Leaf but with inheritance order reversed."""
    def ping(self):
        print(f'{self}.ping() in LeafReversed')
        super().ping()

print(f"\nLeafReversed.__mro__:")
print(f"  {LeafReversed.__mro__}")

print(f"\nNotice: B comes before A now!")
print(f"  (because Leaf(B, A) puts B first)")

leaf2 = LeafReversed()
print(f"\nleaf2 = LeafReversed()")
print(f"leaf2.ping():")
print()
leaf2.ping()


# ============ Example 6: Multiple Inheritance with Shared Methods ============
print("\n" + "=" * 70)
print("EXAMPLE 6: Why super() is better than explicit parent calls")
print("=" * 70)

print(f"\nWithout super() (explicit parent calls):")
print(f"  class A(Root):")
print(f"      def ping(self):")
print(f"          print('ping in A')")
print(f"          Root.ping(self)  # EXPLICIT call")

print(f"\nProblem: If we change inheritance (Leaf inherits from B, A),")
print(f"A still calls Root directly, skipping B in the chain!")

print(f"\nWith super() (uses MRO):")
print(f"  class A(Root):")
print(f"      def ping(self):")
print(f"          print('ping in A')")
print(f"          super().ping()  # Uses MRO")

print(f"\nAdvantage: super() automatically uses the MRO,")
print(f"so it works correctly regardless of inheritance order!")

print(f"\nIn Leaf(A, B): super() in A calls B (correct chain)")
print(f"In LeafReversed(B, A): super() in A calls Root (still correct)")


# ============ Example 7: Real-World MRO Example ============
print("\n" + "=" * 70)
print("EXAMPLE 7: Practical example - Mixin classes with MRO")
print("=" * 70)

class TimestampMixin:
    """A mixin that adds timestamp capability."""
    def get_info(self):
        return f'{super().get_info()} [timestamped]'

class SerializableMixin:
    """A mixin that adds serialization capability."""
    def get_info(self):
        return f'{super().get_info()} [serializable]'

class DataObject:
    """Base class for data objects."""
    def get_info(self):
        return 'DataObject'

class Document(TimestampMixin, SerializableMixin, DataObject):
    """Document with multiple capabilities via mixins."""
    pass

print(f"\nDocument.__mro__:")
print(f"  {Document.__mro__}")

doc = Document()
print(f"\ndoc = Document()")
print(f"doc.get_info() = '{doc.get_info()}'")

print(f"\nMethod chain:")
print(f"  1. Document.get_info() → not found, use MRO")
print(f"  2. TimestampMixin.get_info() → adds '[timestamped]'")
print(f"     → calls super().get_info()")
print(f"  3. SerializableMixin.get_info() → adds '[serializable]'")
print(f"     → calls super().get_info()")
print(f"  4. DataObject.get_info() → returns 'DataObject'")


# ============ Example 8: Summary - MRO Best Practices ============
print("\n" + "=" * 70)
print("EXAMPLE 8: Summary - MRO Best Practices")
print("=" * 70)

print(f"\nRules for MRO (C3 Linearization):")
print(f"  1. Child classes come before parents")
print(f"  2. Parents are listed in inheritance order")
print(f"  3. Each class appears only once")

print(f"\nUsing super() effectively:")
print(f"  1. Always use super() instead of explicit parent calls")
print(f"  2. super() respects MRO and works with multiple inheritance")
print(f"  3. Mixins should always use super() to continue the chain")
print(f"  4. Remember: super() doesn't call the parent - it calls the NEXT class in MRO")

print(f"\nDebugging MRO:")
print(f"  1. Print ClassName.__mro__ to see the resolution order")
print(f"  2. Use print() statements to trace method chains")
print(f"  3. Remember that inheritance order matters!")

print(f"\nCommon mistakes:")
print(f"  1. Forgetting super() in a cooperative hierarchy")
print(f"  2. Not understanding that inheritance order affects MRO")
print(f"  3. Calling parent explicitly instead of using super()")

print(f"\n" + "=" * 70)
