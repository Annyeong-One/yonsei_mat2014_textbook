"""
TUTORIAL: Frozen Dataclass with Custom Methods - Immutability and __str__
=========================================================================

In this tutorial, you'll learn how to create immutable dataclasses using the
frozen=True parameter. Immutable objects cannot be modified after creation,
which is useful for:

  - Data that should never change (like coordinates or dates)
  - Using instances as dictionary keys (requires immutability)
  - Thread-safe code where no synchronization is needed
  - Making intent clear: "this data is final"

We'll also override the __str__ method to create a custom string representation.
Unlike __repr__ (which shows the internal structure), __str__ shows a user-friendly
format. For geographic coordinates, we'll display them as "latitude degrees
direction, longitude degrees direction" format (e.g., "51.5°N, 0.1°W").

Why override __str__ in a frozen dataclass? Even though @dataclass generates
__repr__, you can provide a more readable __str__ for end users while keeping
the technical __repr__ for debugging.
"""

from dataclasses import dataclass


# ============ Example 1: Creating a Frozen Dataclass ============

if __name__ == "__main__":
    print("=" * 70)
    print("EXAMPLE 1: Defining a frozen (immutable) Coordinate dataclass")
    print("=" * 70)

    @dataclass(frozen=True)
    class Coordinate:
        """A geographic coordinate with latitude and longitude.

        The frozen=True parameter makes instances immutable. You cannot modify
        lat or lon after the Coordinate is created. Python will raise a
        FrozenInstanceError if you try.

        This class also overrides __str__ to display coordinates in a
        human-readable format (e.g., "51.5°N, 0.1°W").
        """
        lat: float
        lon: float

        def __str__(self):
            """Return a user-friendly string representation of the coordinate.

            We override __str__ to provide a geographic format:
            - Convert latitude to absolute value with N/S hemisphere indicator
            - Convert longitude to absolute value with E/W hemisphere indicator
            - Format with one decimal place for readability
            """
            # 'N' for positive latitude (North), 'S' for negative (South)
            ns = 'N' if self.lat >= 0 else 'S'
            # 'E' for positive longitude (East), 'W' for negative (West)
            we = 'E' if self.lon >= 0 else 'W'
            # Return formatted string with absolute values and direction indicators
            return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


    # Create some coordinate instances
    london = Coordinate(51.5074, -0.1278)
    sydney = Coordinate(-33.8688, 151.2093)
    equator = Coordinate(0.0, 0.0)

    print(f"\nCoordinates created:")
    print(f"  london = Coordinate(51.5074, -0.1278)")
    print(f"  sydney = Coordinate(-33.8688, 151.2093)")
    print(f"  equator = Coordinate(0.0, 0.0)")


    # ============ Example 2: __str__ vs __repr__ ============
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Understanding __str__ vs __repr__")
    print("=" * 70)

    print(f"\nUsing str() - our custom __str__ method (user-friendly):")
    print(f"  str(london) = {str(london)}")
    print(f"  str(sydney) = {str(sydney)}")
    print(f"  str(equator) = {str(equator)}")

    print(f"\nUsing repr() - dataclass-generated __repr__ (technical):")
    print(f"  repr(london) = {repr(london)}")
    print(f"  repr(sydney) = {repr(sydney)}")

    print(f"\nWhy both?")
    print(f"  - __str__(): For humans reading output")
    print(f"  - __repr__(): For developers debugging code")
    print(f"  - str() calls __str__() if it exists")
    print(f"  - repr() calls __repr__() and shows the 'official' representation")


    # ============ Example 3: Immutability - Trying to Modify ============
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Testing immutability - frozen=True prevents changes")
    print("=" * 70)

    print(f"\nAttempting to modify a frozen dataclass:")
    print(f"  london.lat = 50.0  # Try to change latitude")

    try:
        london.lat = 50.0
        print(f"  ERROR: This should not succeed!")
    except Exception as e:
        print(f"  Result: {type(e).__name__}: {e}")
        print(f"  WHY? frozen=True makes the instance immutable")

    print(f"\nAttempting to add a new attribute:")
    print(f"  london.name = 'London'  # Try to add new attribute")

    try:
        london.name = 'London'
        print(f"  ERROR: This should not succeed!")
    except Exception as e:
        print(f"  Result: {type(e).__name__}: {e}")
        print(f"  WHY? frozen=True prevents any attribute modification")


    # ============ Example 4: Using Frozen Dataclasses as Dictionary Keys ============
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Frozen dataclasses are hashable - use as dict keys")
    print("=" * 70)

    # Immutable objects can be used as dictionary keys
    print(f"\nCreating a dictionary with coordinates as keys:")
    cities = {
        london: 'London, UK',
        sydney: 'Sydney, Australia',
        equator: 'Null Island',
    }

    print(f"  cities = {{")
    for coord, name in cities.items():
        print(f"    {coord}: '{name}',")
    print(f"  }}")

    print(f"\nLooking up cities by coordinate:")
    print(f"  cities[london] = '{cities[london]}'")
    print(f"  cities[sydney] = '{cities[sydney]}'")

    print(f"\nWhy is this only possible with frozen=True?")
    print(f"  - Dictionary keys must be hashable (immutable)")
    print(f"  - Mutable objects change after insertion, breaking the dictionary")
    print(f"  - frozen=True makes Coordinate instances hashable")


    # ============ Example 5: Hemisphere Direction Logic ============
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Understanding the geographic direction logic")
    print("=" * 70)

    # Test coordinates in all four hemispheres
    north_east = Coordinate(45.0, 90.0)
    north_west = Coordinate(45.0, -90.0)
    south_east = Coordinate(-45.0, 90.0)
    south_west = Coordinate(-45.0, -90.0)

    print(f"\nCoordinates in all four hemispheres:")
    print(f"  North/East: lat=45.0, lon=90.0   →  {north_east}")
    print(f"  North/West: lat=45.0, lon=-90.0  →  {north_west}")
    print(f"  South/East: lat=-45.0, lon=90.0  →  {south_east}")
    print(f"  South/West: lat=-45.0, lon=-90.0 →  {south_west}")

    print(f"\nHow the __str__ method works:")
    print(f"  1. Check lat >= 0 → 'N' (North) or 'S' (South)")
    print(f"  2. Check lon >= 0 → 'E' (East) or 'W' (West)")
    print(f"  3. Use abs() to get positive values")
    print(f"  4. Format with .1f for one decimal place")


    # ============ Example 6: Summary of Frozen Dataclass Benefits ============
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Key benefits of frozen dataclasses")
    print("=" * 70)

    print(f"\nFrozen dataclasses provide:")
    print(f"  1. Immutability: Values never change after creation")
    print(f"  2. Hashability: Can be used as dictionary keys or in sets")
    print(f"  3. Safety: Accidental modifications are caught as errors")
    print(f"  4. Intent clarity: Frozen = 'this data is final and safe'")

    print(f"\nCustom __str__ method provides:")
    print(f"  1. User-friendly output (geographic format, not raw numbers)")
    print(f"  2. Domain-specific representation")
    print(f"  3. Cleaner print() output for end users")

    print(f"\n" + "=" * 70)
