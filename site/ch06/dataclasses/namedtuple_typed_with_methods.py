"""
TUTORIAL: Typed NamedTuple with Custom Methods - Adding Behavior to Tuples
===========================================================================

In this tutorial, you'll learn how to add custom methods to NamedTuple classes.
NamedTuple is immutable by default, but you can override methods like __str__
to customize how instances are displayed.

Key insight: NamedTuple is both a tuple AND a class. You can:
  - Keep immutability (for safety and hashability)
  - Add custom methods (for behavior and presentation)
  - Use all tuple operations (indexing, unpacking, iteration)

In this example, we override __str__ to display geographic coordinates in
human-readable format (e.g., "51.5°N, 0.1°W") while keeping the technical
__repr__ for debugging.

Why add methods to NamedTuple?
  - Custom __str__ for user-friendly output
  - Custom __repr__ for debugging information
  - Helper methods for common operations on the data
  - Validation or transformation methods
"""

from typing import NamedTuple


# ============ Example 1: NamedTuple with Custom __str__ ============

if __name__ == "__main__":
    print("=" * 70)
    print("EXAMPLE 1: Defining a NamedTuple with custom __str__ method")
    print("=" * 70)

    class Coordinate(NamedTuple):
        """A geographic coordinate with latitude and longitude.

        This NamedTuple extends the basic tuple with:
        - Named fields for clarity (lat, lon instead of [0], [1])
        - Type hints for documentation and IDE support
        - Custom __str__ for readable geographic format
        - Immutability for safety and hashability

        The __str__ method converts:
          (51.5074, -0.1278) → "51.5°N, 0.1°W"
        """
        lat: float
        lon: float

        def __str__(self):
            """Return a user-friendly string representation of the coordinate.

            This converts raw coordinates to geographic format:
            - 'N' for positive latitude (North), 'S' for negative (South)
            - 'E' for positive longitude (East), 'W' for negative (West)
            - One decimal place for readability

            Returns:
                str: Coordinate in "latitude°direction, longitude°direction" format
            """
            # Determine hemisphere indicators
            ns = 'N' if self.lat >= 0 else 'S'  # North or South
            we = 'E' if self.lon >= 0 else 'W'  # East or West

            # Format with absolute values and one decimal place
            return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


    # Create coordinate instances
    london = Coordinate(51.5074, -0.1278)
    sydney = Coordinate(-33.8688, 151.2093)
    tokyo = Coordinate(35.6762, 139.6503)

    print(f"\nCoordinates created:")
    print(f"  london = Coordinate(51.5074, -0.1278)")
    print(f"  sydney = Coordinate(-33.8688, 151.2093)")
    print(f"  tokyo = Coordinate(35.6762, 139.6503)")


    # ============ Example 2: __str__ vs __repr__ ============
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Comparing __str__ (user-friendly) vs __repr__ (technical)")
    print("=" * 70)

    print(f"\nUsing str() - our custom __str__ method:")
    print(f"  str(london) = {str(london)}")
    print(f"  str(sydney) = {str(sydney)}")
    print(f"  str(tokyo) = {str(tokyo)}")

    print(f"\nUsing repr() - automatic NamedTuple __repr__:")
    print(f"  repr(london) = {repr(london)}")
    print(f"  repr(sydney) = {repr(sydney)}")

    print(f"\nWhy both?")
    print(f"  - __str__(): For humans (e.g., print output, user interfaces)")
    print(f"  - __repr__(): For developers (e.g., debugging, interactive shell)")
    print(f"  - print() calls __str__() if it exists, otherwise __repr__()")


    # ============ Example 3: Using in print Statements ============
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Using coordinates in print statements")
    print("=" * 70)

    print(f"\nSimple print statements use __str__:")
    print(f"  print(london) outputs: {london}")
    print(f"  print(sydney) outputs: {sydney}")

    print(f"\nYou can format them in strings:")
    message = f"Meeting in London at {london}"
    print(f"  message = f'Meeting in London at {{london}}'")
    print(f"  Result: {message}")

    locations = [london, sydney, tokyo]
    print(f"\nPrinting a list of locations:")
    for name, loc in [('London', london), ('Sydney', sydney), ('Tokyo', tokyo)]:
        print(f"  {name}: {loc}")


    # ============ Example 4: NamedTuple Operations Still Work ============
    print("\n" + "=" * 70)
    print("EXAMPLE 4: NamedTuple is still a tuple - indexing and unpacking work")
    print("=" * 70)

    print(f"\nAccessing by field name (more readable):")
    print(f"  london.lat = {london.lat}")
    print(f"  london.lon = {london.lon}")

    print(f"\nAccessing by index (like regular tuple):")
    print(f"  london[0] = {london[0]}  (latitude)")
    print(f"  london[1] = {london[1]}  (longitude)")

    print(f"\nUnpacking:")
    lat, lon = london
    print(f"  lat, lon = london")
    print(f"  lat = {lat}, lon = {lon}")

    print(f"\nIteration:")
    print(f"  for value in london:")
    for value in london:
        print(f"    {value}")

    print(f"\nLength:")
    print(f"  len(london) = {len(london)}")


    # ============ Example 5: Immutability ============
    print("\n" + "=" * 70)
    print("EXAMPLE 5: NamedTuple instances are immutable")
    print("=" * 70)

    print(f"\nAttempting to modify: london.lat = 50.0")
    try:
        london.lat = 50.0
        print(f"  ERROR: This should have failed!")
    except AttributeError as e:
        print(f"  Result: AttributeError")
        print(f"  WHY? NamedTuple is immutable (inherits from tuple)")

    print(f"\nAttempting to add new attribute: london.city = 'London'")
    try:
        london.city = 'London'
        print(f"  ERROR: This should have failed!")
    except AttributeError as e:
        print(f"  Result: AttributeError")
        print(f"  WHY? Tuples don't support arbitrary attribute assignment")


    # ============ Example 6: Using as Dictionary Keys ============
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Hashable - can use as dictionary keys")
    print("=" * 70)

    # Create a dictionary with coordinates as keys
    cities = {
        london: 'London, UK',
        sydney: 'Sydney, Australia',
        tokyo: 'Tokyo, Japan',
    }

    print(f"\nUsing coordinates as dictionary keys:")
    print(f"  cities = {{")
    for coord, name in cities.items():
        print(f"    {coord}: '{name}',")
    print(f"  }}")

    print(f"\nLooking up cities:")
    print(f"  cities[london] = '{cities[london]}'")
    print(f"  cities[sydney] = '{cities[sydney]}'")

    print(f"\nWhy is this possible?")
    print(f"  - Dictionary keys must be hashable (immutable)")
    print(f"  - NamedTuple is immutable by default")
    print(f"  - Both __str__ and immutability make it a perfect key type")


    # ============ Example 7: Adding More Methods ============
    print("\n" + "=" * 70)
    print("EXAMPLE 7: Adding additional helper methods")
    print("=" * 70)

    class EnhancedCoordinate(NamedTuple):
        """Coordinate with additional helper methods."""
        lat: float
        lon: float

        def __str__(self):
            """User-friendly geographic format."""
            ns = 'N' if self.lat >= 0 else 'S'
            we = 'E' if self.lon >= 0 else 'W'
            return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

        def is_northern_hemisphere(self):
            """Check if coordinate is in Northern Hemisphere."""
            return self.lat > 0

        def is_equator(self):
            """Check if coordinate is on the equator."""
            return abs(self.lat) < 0.01  # Within 0.01 degrees

        def distance_from_prime_meridian(self):
            """Calculate absolute distance from prime meridian (0° longitude)."""
            return abs(self.lon)


    # Use the enhanced coordinate
    location = EnhancedCoordinate(51.5, 0.1)
    print(f"\nlocation = EnhancedCoordinate(51.5, 0.1)")
    print(f"  str(location) = {str(location)}")
    print(f"  location.is_northern_hemisphere() = {location.is_northern_hemisphere()}")
    print(f"  location.is_equator() = {location.is_equator()}")
    print(f"  location.distance_from_prime_meridian() = {location.distance_from_prime_meridian()}")

    equator_loc = EnhancedCoordinate(0.0, 30.0)
    print(f"\nequator_loc = EnhancedCoordinate(0.0, 30.0)")
    print(f"  str(equator_loc) = {str(equator_loc)}")
    print(f"  equator_loc.is_equator() = {equator_loc.is_equator()}")
    print(f"  equator_loc.is_northern_hemisphere() = {equator_loc.is_northern_hemisphere()}")


    # ============ Example 8: Summary - NamedTuple with Methods ============
    print("\n" + "=" * 70)
    print("EXAMPLE 8: Key benefits of NamedTuple with methods")
    print("=" * 70)

    print(f"\nNamedTuple combines the best of both worlds:")
    print(f"  1. Tuple benefits:")
    print(f"     - Immutable and hashable")
    print(f"     - Lightweight (lower memory than dataclass)")
    print(f"     - Can use in sets and as dict keys")
    print(f"     - Compatible with tuple unpacking/indexing")

    print(f"  2. Class benefits:")
    print(f"     - Named fields (self.lat instead of self[0])")
    print(f"     - Type hints for clarity and IDE support")
    print(f"     - Custom methods (__str__, __repr__, helpers)")
    print(f"     - Self-documenting code")

    print(f"\nWhen to use:")
    print(f"  - Small, immutable data structures")
    print(f"  - Need tuple-like operations (unpacking, iteration)")
    print(f"  - Want hashability (dict keys, set members)")
    print(f"  - Performance matters (lighter than dataclass)")

    print(f"\nWhen NOT to use:")
    print(f"  - Need mutability")
    print(f"  - Building complex objects with many methods")
    print(f"  - Want inheritance (NamedTuple has limitations)")

    print(f"\n" + "=" * 70)
