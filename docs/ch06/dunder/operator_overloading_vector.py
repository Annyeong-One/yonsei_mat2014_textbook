"""
TUTORIAL: Comprehensive Vector Class - Production-Ready Operator Overloading

This tutorial builds a professional-grade 2D vector class implementing a
comprehensive set of dunder methods. We'll cover operator overloading, type
checking, immutability, hashing, formatting, binary serialization, and more.

This is what a real, production-quality implementation looks like, not a toy example.

Key Learning Goals:
  - Implement multiple operators safely with type checking
  - Use properties for read-only attributes
  - Support binary serialization with __bytes__
  - Implement __hash__ and __eq__ for use in sets and dicts
  - Use __format__ for flexible string formatting
  - Understand __iter__ and unpacking
"""

from array import array
import math

print("=" * 70)
print("TUTORIAL: Comprehensive Vector2d - Production-Quality Implementation")
print("=" * 70)

# ============ EXAMPLE 1: Basic Class Structure ============
print("\n# Example 1: Private Attributes and Properties")
print("=" * 70)

class Vector2d:
    """
    A 2D vector with comprehensive operator support.

    Key design decisions:
    - Use private attributes (__x, __y) to prevent accidental modification
    - Use properties to expose them as read-only (can read, not write)
    - Ensure immutability (vectors don't change after creation)
    - Support rich comparisons and hashing
    """

    typecode = 'd'  # for array.array and binary serialization

    def __init__(self, x, y):
        """Initialize with x and y coordinates, converted to float."""
        # Private attributes (name mangling with __) prevent direct modification
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        """Read-only x coordinate. You can read but not set."""
        return self.__x

    @property
    def y(self):
        """Read-only y coordinate. You can read but not set."""
        return self.__y


# Create and use a vector
v = Vector2d(3, 4)

print(f"Created: {v.__class__.__name__}")
print(f"v.x = {v.x}")
print(f"v.y = {v.y}")
print(f"Type of v.x: {type(v.x)}")  # Always float, even if you passed int
print()

print("Attempting to modify v.x (read-only property):")
try:
    v.x = 10
except AttributeError as e:
    print(f"  Error: {e}")

print("""
WHY: Properties let us expose attributes while preventing modification.
This is important for vectors because changing them would violate the
principle of immutability. A vector (3, 4) should always be (3, 4).
""")

# ============ EXAMPLE 2: String Representations ============
print("\n# Example 2: __repr__ and __str__")
print("=" * 70)

class Vector2d:
    """Vector with string representations."""

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __repr__(self):
        """
        Developer-friendly representation.

        This uses the class name dynamically (type(self).__name__), so if you
        subclass Vector2d, it will show the subclass name. The !r format
        ensures values are precisely represented.

        We unpack self with *self, which requires __iter__ to work.
        This is shown in the next example.
        """
        class_name = type(self).__name__
        return f'{class_name}({self.__x!r}, {self.__y!r})'

    def __str__(self):
        """
        Human-readable representation: show as a coordinate pair.

        Simpler than __repr__, easier to read but less precise.
        Used by print() when __repr__ isn't needed.
        """
        return str(tuple(self))  # Uses __iter__ via tuple()


v = Vector2d(3, 4)

print(f"repr(v) = {repr(v)}")
print(f"str(v) = {str(v)}")
print(f"print(v) output: {v}")
print()

print(f"Type information in repr: {type(v).__name__}")
print("""
WHY: __repr__ should be unambiguous (you could copy it to recreate the
object), while __str__ is just for readability. In REPL:
  >>> v
  Vector2d(3.0, 4.0)  <- calls __repr__

With print():
  >>> print(v)
  (3.0, 4.0)  <- calls __str__
""")

# ============ EXAMPLE 3: Iteration and Unpacking ============
print("\n# Example 3: __iter__ - Unpacking and Iteration")
print("=" * 70)

class Vector2d:
    """Vector supporting unpacking."""

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        """
        Yield x and y in sequence, enabling unpacking.

        This generator yields coordinates one at a time. With __iter__,
        you can:
          x, y = vector
          for coord in vector:
          tuple(vector)
          list(vector)

        All work because Python knows how to iterate.
        """
        return (i for i in (self.__x, self.__y))

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.__x!r}, {self.__y!r})'

    def __str__(self):
        return str(tuple(self))


v = Vector2d(3, 4)

print(f"Vector: {v}")
print()

# Unpacking
x, y = v
print(f"Unpacking: x={x}, y={y}")

# Iteration
print("Iterating:")
for i, coord in enumerate(v):
    print(f"  [{i}] = {coord}")

# Conversion
print(f"tuple(v) = {tuple(v)}")
print(f"list(v) = {list(v)}")

print("""
WHY: __iter__ makes your custom objects work with Python's standard
iteration patterns. Users don't need to know about Vector2d internals.
They can unpack, iterate, and convert just like built-in sequences.
""")

# ============ EXAMPLE 4: Equality and Hashing ============
print("\n# Example 4: __eq__ and __hash__ - Comparison and Hashing")
print("=" * 70)

class Vector2d:
    """Vector supporting equality and hashing."""

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.__x!r}, {self.__y!r})'

    def __eq__(self, other):
        """
        Two vectors are equal if their coordinates are equal.

        We convert both to tuples for comparison. This works because
        __iter__ yields coordinates in a well-defined order.

        Important: If you define __eq__, Python sets __hash__ to None
        unless you explicitly define __hash__ too. This prevents bugs
        where equal objects would have different hashes.
        """
        return tuple(self) == tuple(other)

    def __hash__(self):
        """
        Hash based on the XOR of coordinate hashes.

        This is a common pattern: combine hashes of components using XOR.
        The hash must be stable (same vector = same hash always) and
        consistent with equality (equal vectors = equal hashes).

        Important: Vectors MUST be immutable to be hashable. If a vector
        changes, its hash would become wrong, breaking dict/set lookups.
        """
        return hash(self.__x) ^ hash(self.__y)


# Test equality
v1 = Vector2d(3, 4)
v2 = Vector2d(3, 4)
v3 = Vector2d(4, 5)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}")
print()

print(f"v1 == v2: {v1 == v2} (same coordinates)")
print(f"v1 == v3: {v1 == v3} (different coordinates)")
print(f"v1 is v2: {v1 is v2} (different objects!)")
print()

# Test hashing
print("Hashing vectors:")
print(f"hash(v1) = {hash(v1)}")
print(f"hash(v2) = {hash(v2)}")
print(f"hash(v3) = {hash(v3)}")
print()

# Use in a set (requires __hash__ and __eq__)
vectors = {v1, v2, v3}
print(f"Set of {v1}, {v2}, {v3}: {vectors}")
print(f"Length: {len(vectors)} (v1 and v2 are equal, so one is dropped)")
print()

# Use as dict keys
vector_data = {v1: "origin area", v3: "far away"}
print(f"Using vectors as dict keys: {vector_data}")

print("""
WHY: __hash__ lets vectors work in sets and as dict keys. Combined
with __eq__, it enables reliable comparison and storage. This is
essential for data structures that rely on equality and hashing.

Important: Only define __hash__ for immutable objects. If a vector's
coordinates changed, code like dict[v] would break because v's hash
would be wrong.
""")

# ============ EXAMPLE 5: Magnitude and Boolean ============
print("\n# Example 5: __abs__ and __bool__")
print("=" * 70)

class Vector2d:
    """Vector with magnitude and truthiness."""

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __abs__(self):
        """Return magnitude using Pythagorean theorem."""
        return math.hypot(self.__x, self.__y)

    def __bool__(self):
        """Zero vector is falsy, any other vector is truthy."""
        return bool(abs(self))

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.__x!r}, {self.__y!r})'


v_zero = Vector2d(0, 0)
v_unit = Vector2d(1, 0)
v_normal = Vector2d(3, 4)

print(f"v_zero = {v_zero}, abs = {abs(v_zero)}, bool = {bool(v_zero)}")
print(f"v_unit = {v_unit}, abs = {abs(v_unit)}, bool = {bool(v_unit)}")
print(f"v_normal = {v_normal}, abs = {abs(v_normal)}, bool = {bool(v_normal)}")
print()

print("In if statements:")
if v_zero:
    print("  v_zero is truthy")
else:
    print("  v_zero is falsy")

if v_normal:
    print(f"  v_normal is truthy (magnitude: {abs(v_normal)})")

print("""
WHY: Magnitude and truthiness are core vector properties.
abs() gives you the length, while bool() lets you treat zero
vectors specially in conditional logic.
""")

# ============ EXAMPLE 6: Binary Serialization ============
print("\n# Example 6: __bytes__ and frombytes() - Binary Format")
print("=" * 70)

class Vector2d:
    """Vector supporting binary serialization."""

    typecode = 'd'  # typecode tells array.array how to store numbers

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __bytes__(self):
        """
        Serialize to bytes: typecode + binary data.

        First byte is the typecode (identifies the format).
        Remaining bytes are raw binary representations.

        This is compact and fast for saving to disk or network.
        """
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    @classmethod
    def frombytes(cls, octets):
        """
        Deserialize from bytes created by __bytes__.

        Read typecode from first byte, then interpret remaining bytes
        using that typecode. Return a new Vector2d instance.
        """
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.__x!r}, {self.__y!r})'


v1 = Vector2d(3, 4)

print(f"Original vector: {v1}")
print()

# Serialize to bytes
data = bytes(v1)
print(f"Serialized to bytes: {data!r}")
print(f"Byte length: {len(data)}")
print()

# Deserialize from bytes
v2 = Vector2d.frombytes(data)
print(f"Deserialized vector: {v2}")
print(f"v1 == v2: {v1 == v2}")
print()

print(f"Typecode '{Vector2d.typecode}' is: float64 (8 bytes per number)")
print(f"Total bytes: 1 (typecode) + 8 (x) + 8 (y) = 17 bytes")
print("""
WHY: Binary serialization is fast and compact. Useful for:
  - Saving vectors to files
  - Sending over network
  - Storing in databases
  - Speed-critical applications

The typecode makes deserialization unambiguous - the byte stream
completely describes itself.
""")

# ============ EXAMPLE 7: Custom Formatting ============
print("\n# Example 7: __format__ - Flexible String Formatting")
print("=" * 70)

class Vector2d:
    """Vector supporting custom formatting."""

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def angle(self):
        """Return angle in radians from positive x-axis."""
        return math.atan2(self.__y, self.__x)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    def __abs__(self):
        return math.hypot(self.__x, self.__y)

    def __format__(self, fmt_spec=''):
        """
        Custom formatting supporting Cartesian and polar coordinates.

        fmt_spec examples:
          'p'       -> polar format: <magnitude, angle>
          '.2f'     -> 2 decimal places (Cartesian)
          '.3ep'    -> 3 decimals, scientific, polar
          '.5fp'    -> 5 decimals, polar

        This is flexible formatting that respects both format spec
        and coordinate system preference.
        """
        if fmt_spec.endswith('p'):
            # Polar format: remove 'p', convert to polar
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            # Cartesian format (default)
            coords = self
            outer_fmt = '({}, {})'

        # Format each coordinate with the format spec
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.__x!r}, {self.__y!r})'


v = Vector2d(1, 1)

print(f"Vector: {v}")
print(f"Magnitude: {abs(v):.6f}, Angle: {v.angle():.6f} radians")
print()

print("Cartesian formatting (default):")
print(f"  format(v, '') = {format(v)}")
print(f"  format(v, '.2f') = {format(v, '.2f')}")
print(f"  format(v, '.3e') = {format(v, '.3e')}")
print()

print("Polar formatting (endswith 'p'):")
print(f"  format(v, 'p') = {format(v, 'p')}")
print(f"  format(v, '.2fp') = {format(v, '.2fp')}")
print()

v2 = Vector2d(3, 4)
print(f"v2 = {v2}")
print(f"  Cartesian: {format(v2, '.2f')}")
print(f"  Polar: {format(v2, '.2fp')}")

print("""
WHY: __format__ provides flexible, user-friendly output. Users can
choose between representations (Cartesian vs polar) with simple syntax:
  f"{v:.2f}"    # Cartesian: (3.00, 4.00)
  f"{v:.2fp}"   # Polar: <5.00, 0.93>

This is much better than having two separate methods.
""")

# ============ EXAMPLE 8: Arithmetic Operators ============
print("\n# Example 8: __add__ and Type Checking")
print("=" * 70)

class Vector2d:
    """Vector with safe arithmetic operations."""

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    def __add__(self, other):
        """
        Add two vectors (or raise a clear error if 'other' isn't compatible).

        Type checking prevents cryptic errors. Without it, you might add
        a Vector and a tuple by accident, leading to confusing results.
        With explicit checking, errors are immediate and clear.
        """
        if isinstance(other, Vector2d):
            return Vector2d(*tuple(self) + tuple(other))
        return NotImplemented  # Let Python try other.__radd__(self)

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.__x!r}, {self.__y!r})'


v1 = Vector2d(2, 3)
v2 = Vector2d(4, 5)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print()

print("Type checking prevents bugs:")
try:
    result = v1 + (1, 2)
except TypeError as e:
    print(f"  v1 + (1, 2) raises TypeError: {e}")

print("""
WHY: Type checking in operators prevents silent bugs. If you try to add
incompatible types, you get a clear error immediately rather than getting
garbage data later. The NotImplemented return allows Python to try the
reverse operation (other.__radd__(v1)).
""")

# ============ EXAMPLE 9: Complete Professional Implementation ============
print("\n# Example 9: The Complete Vector2d Class")
print("=" * 70)

print("""
Key design principles in a production Vector2d:

1. IMMUTABILITY: Private attributes (__x, __y) and read-only properties
   ensure vectors can't be modified. Essential for hashing!

2. TYPE SAFETY: __float__ conversion on inputs, type checking in operators

3. RICH COMPARISON: __eq__ for equality, __hash__ for use in collections

4. ITERATION: __iter__ for unpacking (x, y = v), conversion to tuple/list

5. NUMERIC PROTOCOL: __abs__ for magnitude, __bool__ for truthiness

6. SERIALIZATION: __bytes__ and frombytes() for persistence

7. FORMATTING: __format__ for flexible output (Cartesian vs polar)

8. OPERATORS: __add__ with type checking, NotImplemented for compatibility

9. REPRESENTATION: __repr__ for debugging, __str__ for readability

10. METADATA: __match_args__ for pattern matching, typecode for flexibility

All these features work together to make Vector2d feel like a native
Python type, not a bolt-on class. Users don't have to learn special
methods - they use standard Python idioms.
""")

# ============ EXAMPLE 10: Practical Usage ============
print("\n# Example 10: Real-World Vector Operations")
print("=" * 70)

class Vector2d:
    """Complete Vector2d for real use."""

    __match_args__ = ('x', 'y')  # enables pattern matching
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.__x!r}, {self.__y!r})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.__x) ^ hash(self.__y)

    def __abs__(self):
        return math.hypot(self.__x, self.__y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.__y, self.__x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def __add__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(*tuple(self) + tuple(other))
        return NotImplemented

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


# Practical scenario: navigation system
print("Navigation system with vectors:")
print()

# Starting position and direction
position = Vector2d(0, 0)
direction = Vector2d(1, 1)  # NE direction

print(f"Starting at: {position}")
print(f"Moving in direction: {direction}")
print(f"Direction magnitude: {abs(direction):.2f}")
print()

# Move in direction
distance = 10
movement = Vector2d(direction.x * distance / abs(direction),
                    direction.y * distance / abs(direction))
position = Vector2d(position.x + movement.x, position.y + movement.y)

print(f"After moving 10 units: {position}")
print(f"Distance from origin: {abs(position):.2f}")
print()

# Store in a collection
waypoints = {
    Vector2d(0, 0): "start",
    Vector2d(10, 10): "checkpoint",
    Vector2d(20, 20): "end"
}

print("Navigation waypoints:")
for point, name in waypoints.items():
    print(f"  {point} ({format(point, '.1fp')}) -> {name}")

print("""
This demonstrates real usage: vectors work seamlessly in collections,
arithmetic, formatting, and comparisons. Users don't think about dunder
methods - they just use vectors naturally.
""")

print("\n" + "=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. IMMUTABILITY: Use private attributes and properties to prevent
   modification. This is essential for hashing and predictability.

2. DUNDER METHODS ENABLE PROTOCOLS: Each dunder method (like __eq__)
   enables a specific Python protocol (hashability, comparability).

3. TYPE SAFETY: Check types in operators, use NotImplemented to allow
   Python to try the other operand's methods.

4. CONSISTENCY: If you define __eq__, define __hash__. If you implement
   __iter__, you get unpacking for free. Dunder methods work together.

5. DOCUMENTATION: Each method needs clear docs explaining why and when
   to use it. These are important design decisions.

6. COMPLETENESS: A professional class doesn't just have __add__ - it has
   __repr__, __str__, __eq__, __hash__, __iter__, and more working
   together smoothly.

7. PROTOCOLS OVER INHERITANCE: You don't inherit from list or need a
   special base class. You just implement the right dunder methods.

8. PYTHONIC DESIGN: Make your objects work with standard Python features:
   collections, iteration, formatting, arithmetic. Users should never
   feel like they're using a special library type.
""")
