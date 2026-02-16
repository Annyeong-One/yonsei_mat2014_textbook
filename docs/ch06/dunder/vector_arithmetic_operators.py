"""
TUTORIAL: Vector Arithmetic with Operator Overloading

This tutorial teaches you how to implement dunder methods that let custom
objects work with Python's arithmetic operators (+, *, abs()). We'll build a
Vector class and overload operators so that mathematical operations on vectors
feel natural and intuitive.

Key Learning Goals:
  - Understand how Python's operators are just method calls
  - Learn to implement __add__, __mul__, __abs__, __bool__
  - See why operator overloading makes code more readable
  - Understand how these operators combine with __repr__ for clarity
"""

import math

print("=" * 70)
print("TUTORIAL: Vector Arithmetic with Operator Overloading")
print("=" * 70)

# ============ EXAMPLE 1: Basic Vector Class ============
print("\n# Example 1: Creating a Basic Vector Class")
print("=" * 70)

class Vector:
    """
    A simple 2D vector supporting arithmetic operations.

    This class demonstrates how operator overloading makes mathematical
    objects intuitive. Instead of v1.add(v2), you can write v1 + v2.
    """

    def __init__(self, x=0, y=0):
        """Initialize a vector with x and y components."""
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Return a developer-friendly string representation.

        This is crucial for debugging. When you print a vector or inspect
        it in the interactive interpreter, you see exactly what you need.
        The !r format specifier ensures the values are clearly shown as numbers.
        """
        return f'Vector({self.x!r}, {self.y!r})'

    def __str__(self):
        """Human-readable string representation (optional)."""
        return f'({self.x}, {self.y})'


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(f"Created v1 = {v1}")
print(f"Created v2 = {v2}")
print(f"v1.x = {v1.x}, v1.y = {v1.y}")
print("""
WHY: The __repr__ method is your first step. It makes vectors readable
in the Python interpreter, which is essential when learning and debugging.
""")

# ============ EXAMPLE 2: The __abs__ Method ============
print("\n# Example 2: Magnitude with abs() - __abs__")
print("=" * 70)

class Vector:
    """Vector with magnitude calculation."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        """
        Return the magnitude (length) of the vector.

        The magnitude of a 2D vector (x, y) is sqrt(x^2 + y^2).
        Python's abs() function calls __abs__, so you can write:
          abs(v)  instead of  v.magnitude()

        This uses the Pythagorean theorem via math.hypot, which is
        numerically stable and handles edge cases.
        """
        return math.hypot(self.x, self.y)


v1 = Vector(3, 4)

print(f"Vector: {v1}")
print(f"abs(v1) = {abs(v1)}")
print(f"Explanation: sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5")
print()

v2 = Vector(5, 12)
print(f"Vector: {v2}")
print(f"abs(v2) = {abs(v2)}")
print(f"Explanation: sqrt(5^2 + 12^2) = sqrt(25 + 144) = sqrt(169) = 13")
print("""
WHY: Using abs() for magnitude is more readable than v.magnitude().
It's shorter and feels natural because we use abs() for magnitudes
in mathematics.
""")

# ============ EXAMPLE 3: The __bool__ Method ============
print("\n# Example 3: Truthiness with __bool__")
print("=" * 70)

class Vector:
    """Vector with magnitude and boolean evaluation."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """
        Return False if the vector has zero magnitude, True otherwise.

        In Python, objects are "truthy" or "falsy". By implementing __bool__,
        we define when a vector should be considered "empty" or "zero".

        We use abs(self) because a vector is zero only if its magnitude is 0.
        For any non-zero vector, the magnitude is positive.
        """
        return bool(abs(self))


zero_vector = Vector(0, 0)
unit_vector = Vector(1, 0)
normal_vector = Vector(3, 4)

print(f"Zero vector: {zero_vector}")
print(f"  abs(zero_vector) = {abs(zero_vector)}")
print(f"  bool(zero_vector) = {bool(zero_vector)}")
print()

print(f"Unit vector: {unit_vector}")
print(f"  abs(unit_vector) = {abs(unit_vector)}")
print(f"  bool(unit_vector) = {bool(unit_vector)}")
print()

print(f"Normal vector: {normal_vector}")
print(f"  abs(normal_vector) = {abs(normal_vector)}")
print(f"  bool(normal_vector) = {bool(normal_vector)}")
print()

print("Using vectors in if statements:")
if zero_vector:
    print("  Zero vector is truthy")
else:
    print("  Zero vector is falsy")

if normal_vector:
    print("  Normal vector is truthy")
else:
    print("  Normal vector is falsy")

print("""
WHY: __bool__ lets us treat vectors intuitively in boolean context.
A zero vector "doesn't exist" in a sense, so it's falsy. This makes
code like 'if vector:' feel natural.
""")

# ============ EXAMPLE 4: The __add__ Method ============
print("\n# Example 4: Addition with __add__")
print("=" * 70)

class Vector:
    """Vector with arithmetic operations."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        """
        Add two vectors component-wise.

        Vector addition in mathematics:
          (x1, y1) + (x2, y2) = (x1+x2, y1+y2)

        By implementing __add__, you can write:
          v1 + v2  instead of  v1.add(v2)

        When you write v1 + v2, Python actually calls v1.__add__(v2).
        This is how ALL operators work in Python - they're just method calls!
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print()

v3 = v1 + v2
print(f"v1 + v2 = {v3}")
print(f"Explanation: Vector(2+4, 3+5) = Vector(6, 8)")
print()

v4 = Vector(10, 20)
v5 = Vector(1, 2)
result = v4 + v5
print(f"Vector(10, 20) + Vector(1, 2) = {result}")
print("""
WHY: The __add__ method makes vector math readable. The syntax matches
mathematical notation exactly, so code is easier to understand and verify.

Behind the scenes:
  v1 + v2
  ↓ (Python translates + to __add__)
  v1.__add__(v2)
  ↓ (method executes and returns a new Vector)
  Vector(6, 8)
""")

# ============ EXAMPLE 5: The __mul__ Method ============
print("\n# Example 5: Scalar Multiplication with __mul__")
print("=" * 70)

class Vector:
    """Vector with full arithmetic support."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """
        Multiply a vector by a scalar (number).

        Scalar multiplication in mathematics:
          c * (x, y) = (c*x, c*y)

        This scales the vector by stretching or shrinking it, but maintains
        its direction. A scalar of 2 doubles the vector, 0.5 halves it,
        -1 reverses its direction.
        """
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 3)

print(f"v1 = {v1}")
print(f"abs(v1) = {abs(v1)}")
print()

v2 = v1 * 2
print(f"v1 * 2 = {v2}")
print(f"Explanation: Vector(2*2, 3*2) = Vector(4, 6)")
print(f"abs(v1 * 2) = {abs(v2)} (twice the magnitude)")
print()

v3 = v1 * 0.5
print(f"v1 * 0.5 = {v3}")
print(f"Explanation: Vector(2*0.5, 3*0.5) = Vector(1.0, 1.5)")
print(f"abs(v1 * 0.5) = {abs(v3)} (half the magnitude)")
print()

v4 = v1 * -1
print(f"v1 * -1 = {v4}")
print(f"Explanation: Vector(2*-1, 3*-1) = Vector(-2, -3)")
print(f"Reverses direction, same magnitude: abs(v1 * -1) = {abs(v4)}")
print("""
WHY: Scalar multiplication is fundamental in vector math. By overloading
__mul__, we make scaling vectors as simple as multiplication: v * 2.

This is more intuitive and mathematically concise than v.scale(2).
""")

# ============ EXAMPLE 6: Combining Operations ============
print("\n# Example 6: Combining Multiple Operations")
print("=" * 70)

# Using all our Vector methods together
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}, magnitude = {abs(v1)}")
print(f"v2 = {v2}, magnitude = {abs(v2)}")
print()

# Complex expression combining operators
result = (v1 + v2) * 2
print(f"(v1 + v2) * 2")
print(f"  = ({v1} + {v2}) * 2")
print(f"  = Vector(4, 6) * 2")
print(f"  = {result}")
print(f"  magnitude = {abs(result)}")
print()

# Using boolean context
v_zero = Vector(0, 0)
if v_zero:
    print("Zero vector is truthy")
else:
    print("Zero vector is falsy (correct!)")

if v1:
    print(f"v1 is truthy (magnitude: {abs(v1)})")

print("""
WHY: When operators are overloaded properly, you can compose them in
expressions that read almost like mathematical notation. This is far
superior to:
  Vector.multiply(Vector.add(v1, v2), 2)

which is what you'd write without operator overloading.
""")

# ============ EXAMPLE 7: Understanding __mul__ Semantics ============
print("\n# Example 7: Why __mul__ Takes a Scalar")
print("=" * 70)

v = Vector(2, 3)

print(f"v = {v}")
print()

print("Scalar multiplication (what we support):")
print(f"  v * 3 = {v * 3}")
print(f"  Result: components scaled by 3")
print()

print("""
NOTE: We don't support vector * vector multiplication (dot product).
That would require a different design:
  - __mul__ could call it "cross product" (confusing)
  - Better: use a separate method v1.dot(v2) for clarity

The rule: Use __mul__ only for operations that feel like multiplication.
Don't force every operation into operator syntax.
""")

# ============ EXAMPLE 8: The Complete Vector Class ============
print("\n# Example 8: Complete Vector Class Summary")
print("=" * 70)

print("""
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # For debugging and inspection
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        # For abs(v) - returns magnitude
        return math.hypot(self.x, self.y)

    def __bool__(self):
        # For if v: - zero vector is falsy
        return bool(abs(self))

    def __add__(self, other):
        # For v1 + v2 - component-wise addition
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        # For v * n - scalar multiplication
        return Vector(self.x * scalar, self.y * scalar)

With just 5 methods (6 lines of code each), we've built a powerful,
intuitive vector class that feels like a first-class Python object.
""")

# ============ EXAMPLE 9: Real-World Usage ============
print("\n# Example 9: Real-World Vector Math")
print("=" * 70)

# Simulate a particle with velocity
position = Vector(0, 0)
velocity = Vector(1, 2)
acceleration = Vector(0.1, 0)

print("Simulating object movement:")
print(f"Initial position: {position}")
print(f"Velocity: {velocity}")
print(f"Acceleration: {acceleration}")
print()

# Simulate physics: position += velocity; velocity += acceleration
for step in range(3):
    position = position + velocity
    velocity = velocity + acceleration
    print(f"Step {step+1}: pos={position}, vel={velocity}, speed={abs(velocity):.2f}")

print("""
WHY: With operator overloading, physics simulation code reads naturally.
The physics equations map directly to Python code:
  position = position + velocity
  velocity = velocity + acceleration

Without overloading, it would be:
  position = position.add(velocity)
  velocity = velocity.add(acceleration)

Much more verbose and harder to read!
""")

print("\n" + "=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. OPERATORS ARE METHOD CALLS: When you write v1 + v2, Python calls
   v1.__add__(v2). All operators (+, -, *, /) are just methods!

2. READABLE MATH: Overloading operators makes mathematical code match
   mathematical notation. This reduces cognitive load and prevents bugs.

3. MATCH THE SEMANTICS: Only overload operators where they make sense.
   For vectors, + is addition, * is scalar multiplication. Clear and
   intuitive.

4. IMMUTABILITY: Our operations (+ and *) return new vectors rather
   than modifying existing ones. This is the Pythonic style for operators.

5. COMPOSE OPERATIONS: With proper operator overloading, you can compose
   complex expressions that read naturally: (v1 + v2) * 2 - v3

6. __repr__ IS IMPORTANT: Always implement __repr__ with any dunder
   methods. It makes debugging vastly easier.
""")
