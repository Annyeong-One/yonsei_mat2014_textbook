"""
TUTORIAL: NamedTuple Basics - Typed Named Tuples vs Dataclasses
================================================================

In this tutorial, you'll learn about NamedTuple, Python's typed alternative
to the regular tuple. NamedTuple provides:

  - Named fields for accessing data (e.g., person.name instead of person[0])
  - Type hints for clarity and IDE support
  - Immutability (tuples cannot be modified after creation)
  - Unpacking capability (like regular tuples)
  - Smaller memory footprint than dataclasses

The main difference from @dataclass:
  - NamedTuple is immutable by default (dataclass is mutable by default)
  - NamedTuple is a tuple subclass (dataclass is not)
  - NamedTuple has smaller memory overhead
  - Dataclass offers more flexibility with the frozen= parameter

In this file, we show the basic NamedTuple syntax and compare it to the
equivalent dataclass version. Notice the three types of attributes:
  1. Typed fields with no default: REQUIRED
  2. Typed fields with defaults: OPTIONAL
  3. Class attributes without type hints: NOT fields
"""

import typing


# ============ Example 1: Basic NamedTuple Definition ============

if __name__ == "__main__":
    print("=" * 70)
    print("EXAMPLE 1: Defining a basic NamedTuple")
    print("=" * 70)

    class DemoNTClass(typing.NamedTuple):
        """A NamedTuple with three attributes following the same pattern as dataclass.

        Attributes:
            a (int): Required field - must provide when creating instances.
                     Has type hint, so it's a named tuple field.

            b (float): Optional field with default value.
                       If not provided, instances will use 1.1.
                       Has type hint, so it's a named tuple field.

            c: Class attribute without type hint.
               Not treated as a field, unlike 'a' and 'b'.
        """
        # Field 1: Required - has type hint, no default
        a: int           # <1> Required when creating instance

        # Field 2: Optional - has type hint and default value
        b: float = 1.1   # <2> Optional, defaults to 1.1

        # Not a field - no type hint, so treated as class attribute
        c = 'spam'       # <3> Class attribute, not field


    print(f"\nNamedTuple definition complete.\n")


    # ============ Example 2: Creating NamedTuple Instances ============
    print("=" * 70)
    print("EXAMPLE 2: Creating instances and accessing fields")
    print("=" * 70)

    # Create with required field only
    instance1 = DemoNTClass(42)
    print(f"\ninstance1 = DemoNTClass(42)")
    print(f"  instance1.a = {instance1.a}")
    print(f"  instance1.b = {instance1.b}  (uses default)")
    print(f"  Accessing by name: instance1.a (more readable than instance1[0])")

    # Create with both fields
    instance2 = DemoNTClass(100, 2.5)
    print(f"\ninstance2 = DemoNTClass(100, 2.5)")
    print(f"  instance2.a = {instance2.a}")
    print(f"  instance2.b = {instance2.b}")

    # Create using keyword arguments
    instance3 = DemoNTClass(a=50, b=1.5)
    print(f"\ninstance3 = DemoNTClass(a=50, b=1.5)  (using keyword arguments)")
    print(f"  instance3.a = {instance3.a}")
    print(f"  instance3.b = {instance3.b}")


    # ============ Example 3: NamedTuple vs Regular Tuple ============
    print("\n" + "=" * 70)
    print("EXAMPLE 3: NamedTuple advantages over regular tuple")
    print("=" * 70)

    # Regular tuple - unclear what each value represents
    regular_tuple = (100, 2.5)
    print(f"\nRegular tuple:")
    print(f"  my_tuple = (100, 2.5)")
    print(f"  my_tuple[0] = {regular_tuple[0]}  (What is this? Need documentation)")
    print(f"  my_tuple[1] = {regular_tuple[1]}  (What is this? Need documentation)")

    # NamedTuple - clear field names
    named_tuple = DemoNTClass(100, 2.5)
    print(f"\nNamedTuple:")
    print(f"  my_tuple = DemoNTClass(100, 2.5)")
    print(f"  my_tuple.a = {named_tuple.a}  (Clear: this is 'a')")
    print(f"  my_tuple.b = {named_tuple.b}  (Clear: this is 'b')")

    print(f"\nWhy NamedTuple is better:")
    print(f"  1. Names make code self-documenting")
    print(f"  2. IDE autocomplete works with named fields")
    print(f"  3. Type hints help catch errors before runtime")
    print(f"  4. Still has tuple efficiency and immutability")


    # ============ Example 4: Immutability - NamedTuples Cannot Be Modified ============
    print("\n" + "=" * 70)
    print("EXAMPLE 4: NamedTuples are immutable by default")
    print("=" * 70)

    print(f"\nAttempting to modify a NamedTuple:")
    print(f"  instance1.a = 50  # Try to change field 'a'")

    try:
        instance1.a = 50
        print(f"  ERROR: This should not succeed!")
    except AttributeError as e:
        print(f"  Result: AttributeError: {e}")
        print(f"  WHY? NamedTuples are immutable (like regular tuples)")

    print(f"\nThis is a key difference from mutable dataclasses:")
    print(f"  - NamedTuple: Immutable by default (like tuple)")
    print(f"  - Dataclass: Mutable by default (can use frozen=True)")


    # ============ Example 5: Tuple Operations Still Work ============
    print("\n" + "=" * 70)
    print("EXAMPLE 5: NamedTuple still supports tuple operations")
    print("=" * 70)

    # Indexing
    print(f"\nIndexing (like a regular tuple):")
    print(f"  instance2[0] = {instance2[0]}  (first field: a)")
    print(f"  instance2[1] = {instance2[1]}  (second field: b)")

    # Unpacking
    print(f"\nUnpacking (like a regular tuple):")
    a_val, b_val = instance2
    print(f"  a_val, b_val = instance2")
    print(f"  a_val = {a_val}, b_val = {b_val}")

    # Iteration
    print(f"\nIteration (like a regular tuple):")
    print(f"  for value in instance2:")
    for value in instance2:
        print(f"    {value}")

    # Length
    print(f"\nLength:")
    print(f"  len(instance2) = {len(instance2)}")

    # String representation
    print(f"\nString representation:")
    print(f"  str(instance2) = {str(instance2)}")
    print(f"  repr(instance2) = {repr(instance2)}")


    # ============ Example 6: Class Attributes in NamedTuple ============
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Class attributes without type hints")
    print("=" * 70)

    print(f"\nThe 'c' attribute is a class attribute (like in dataclass):")
    print(f"  DemoNTClass.c = '{DemoNTClass.c}'")
    print(f"  instance1.c = '{instance1.c}'")
    print(f"  instance2.c = '{instance2.c}'")

    print(f"\nIt's shared across all instances:")
    print(f"  (Accessing it through instances shows the class-level value)")

    print(f"\nIt's NOT in the NamedTuple fields:")
    print(f"  len(instance2) = {len(instance2)}  (only a and b, not c)")


    # ============ Example 7: NamedTuple vs Dataclass Comparison ============
    print("\n" + "=" * 70)
    print("EXAMPLE 7: NamedTuple vs Dataclass")
    print("=" * 70)

    print(f"\nNamedTuple advantages:")
    print(f"  1. Immutable by default (safer for dict keys/sets)")
    print(f"  2. Lighter memory footprint (still a tuple)")
    print(f"  3. Compatible with any tuple operation")
    print(f"  4. Great for simple data structures")

    print(f"\nDataclass advantages:")
    print(f"  1. Mutable by default (easier to work with)")
    print(f"  2. More flexible (add methods, use field())")
    print(f"  3. order=True generates comparison methods")
    print(f"  4. Better for complex data structures")

    print(f"\nChoose NamedTuple when:")
    print(f"  - You need immutability")
    print(f"  - You want tuple-like behavior")
    print(f"  - Memory efficiency matters")
    print(f"  - Your data is simple (few fields, no methods)")

    print(f"\nChoose Dataclass when:")
    print(f"  - You need mutability")
    print(f"  - You want to add methods to your data structure")
    print(f"  - You need customizable initialization or comparison")
    print(f"  - You need field validation")

    print(f"\n" + "=" * 70)
