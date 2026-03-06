"""
Python Pattern Matching with Guards - Python 3.10+ Structural Matching
This tutorial demonstrates how to use match/case statements with guards
and tuple destructuring to filter and extract data elegantly.
Run this file to see pattern matching in action!
"""

if __name__ == "__main__":

    print("=" * 70)
    print("PATTERN MATCHING WITH GUARDS - EXAMPLES")
    print("=" * 70)

    # ============================================================================
    # EXAMPLE 1: Basic Pattern Matching with Tuple Destructuring
    # ============================================================================
    print("\n1. BASIC PATTERN MATCHING WITH TUPLE DESTRUCTURING")
    print("-" * 70)

    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    print("\nMetro areas data structure:")
    print("Each entry: (city_name, country_code, population_millions, (latitude, longitude))\n")

    for record in metro_areas:
        print(f"Raw record: {record}")

    # ============================================================================
    # EXAMPLE 2: Match/Case with Guards - Filtering by Longitude
    # ============================================================================
    print("\n2. MATCH/CASE WITH GUARDS - FILTERING WESTERN CITIES")
    print("-" * 70)

    print("\nUsing match/case to filter cities with NEGATIVE longitude (West)")
    print("This is much cleaner than if/elif chains!\n")

    print(f'{"City Name":15} | {"Latitude":>9} | {"Longitude":>9}')
    print("-" * 40)

    for record in metro_areas:
        # The match/case statement with a GUARD (the 'if' clause)
        # This pattern extracts name, _, _, (lat, lon) from the tuple
        # Then the guard 'if lon <= 0' filters for western cities
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

    print("\nWHY THIS MATTERS:")
    print("- The guard (if lon <= 0) happens AFTER destructuring")
    print("- We only print cities with negative longitude (Western Hemisphere)")
    print("- The syntax is readable: match structure, then apply condition")

    # ============================================================================
    # EXAMPLE 3: Multiple Guards - Different Filtering Criteria
    # ============================================================================
    print("\n3. MULTIPLE PATTERNS WITH DIFFERENT GUARDS")
    print("-" * 70)

    print("\nLet's filter for Eastern cities (positive longitude):")
    print(f'{"City Name":15} | {"Latitude":>9} | {"Longitude":>9}')
    print("-" * 40)

    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon > 0:  # Eastern cities
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

    print("\nNow let's filter for Northern cities (positive latitude):")
    print(f'{"City Name":15} | {"Latitude":>9} | {"Longitude":>9}')
    print("-" * 40)

    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lat > 0:  # Northern cities
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

    # ============================================================================
    # EXAMPLE 4: Why Underscore (_) is Used
    # ============================================================================
    print("\n4. UNDERSTANDING THE UNDERSCORE (_) IN PATTERNS")
    print("-" * 70)

    print("\nIn our pattern: [name, _, _, (lat, lon)]")
    print("- 'name': We CARE about this - capture the city name")
    print("- '_': We DON'T care about this - country code (placeholder)")
    print("- '_': We DON'T care about this - population (placeholder)")
    print("- (lat, lon): We CARE about this - extract coordinates\n")

    print("Using _ is Python convention for 'I'm not using this value'")
    print("It makes code more readable and shows intent!\n")

    # ============================================================================
    # EXAMPLE 5: Practical Example - Data Processing with Match/Case
    # ============================================================================
    print("\n5. PRACTICAL EXAMPLE - CATEGORIZING CITIES BY LOCATION")
    print("-" * 70)

    def categorize_city(record):
        """Use pattern matching to categorize cities by hemisphere."""
        match record:
            case [name, country, _, (lat, lon)] if lon < 0 and lat > 0:
                return f"{name} is in the NORTHWEST"
            case [name, country, _, (lat, lon)] if lon < 0 and lat < 0:
                return f"{name} is in the SOUTHWEST"
            case [name, country, _, (lat, lon)] if lon > 0 and lat > 0:
                return f"{name} is in the NORTHEAST"
            case [name, country, _, (lat, lon)] if lon > 0 and lat < 0:
                return f"{name} is in the SOUTHEAST"
            case _:  # Default case
                return "Unknown location"

    print("\nCategorizing each city:\n")
    for record in metro_areas:
        print(f"  {categorize_city(record)}")

    print("\nKEY INSIGHTS:")
    print("- Pattern matching with guards is more readable than nested if/elif")
    print("- Destructuring extracts values in one operation")
    print("- Guards allow conditional logic after pattern matching")
    print("- The 'case _' acts as a default fallback")
