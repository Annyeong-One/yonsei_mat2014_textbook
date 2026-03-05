"""
Magic Methods: __hash__, __eq__, and __slots__

When using custom objects in sets or as dict keys, Python needs:
- __hash__() to compute a hash code (for bucket placement)
- __eq__() to check if two objects are "equal"

Rule: Objects that compare equal MUST have the same hash.
      Same hash does NOT mean equal (hash collisions exist).

Topics covered:
- __hash__ and __eq__ for hashable objects
- __slots__ for memory-efficient classes
- __setitem__ and __getitem__ for container-like classes

Based on concepts from Python-100-Days example16 and ch06/dunder materials.
"""


# =============================================================================
# Example 1: Making Objects Hashable
# =============================================================================

class Student:
    """A student that can be used in sets and as dict keys.

    __slots__ restricts attributes to save memory.
    __hash__ and __eq__ make instances hashable.

    >>> s1 = Student(1001, 'Alice')
    >>> s2 = Student(1001, 'Alice')
    >>> s1 == s2
    True
    >>> hash(s1) == hash(s2)
    True
    >>> s1 is s2  # Different objects
    False
    """
    __slots__ = ('student_id', 'name', 'grade')

    def __init__(self, student_id: int, name: str):
        self.student_id = student_id
        self.name = name

    def __hash__(self) -> int:
        """Hash based on student_id and name.

        Must be consistent with __eq__: if a == b, then hash(a) == hash(b).
        Using tuple hashing is a clean pattern.
        """
        return hash((self.student_id, self.name))

    def __eq__(self, other) -> bool:
        """Two students are equal if they have the same ID and name."""
        if not isinstance(other, Student):
            return NotImplemented
        return (self.student_id == other.student_id and
                self.name == other.name)

    def __str__(self):
        return f'{self.student_id}: {self.name}'

    def __repr__(self):
        return f'Student({self.student_id}, {self.name!r})'


def demo_hashable():
    """Demonstrate hashable objects in sets and dicts."""
    print("=== Hashable Objects in Sets ===")

    students = set()
    students.add(Student(1001, 'Alice'))
    students.add(Student(1001, 'Alice'))  # Duplicate - won't be added
    students.add(Student(1002, 'Bob'))

    print(f"Set size: {len(students)} (added 3, but 2 unique)")
    print(f"Students: {students}")
    print()


# =============================================================================
# Example 2: __slots__ for Memory Efficiency
# =============================================================================

def demo_slots():
    """Demonstrate __slots__ behavior."""
    print("=== __slots__ Behavior ===")

    stu = Student(1234, 'Charlie')
    stu.grade = 'A'  # OK - 'grade' is in __slots__
    print(f"Student: {stu}, Grade: {stu.grade}")

    try:
        stu.email = 'charlie@example.com'  # Error - not in __slots__
    except AttributeError as e:
        print(f"AttributeError: {e}")

    print(f"Allowed attributes: {Student.__slots__}")
    print(f"Has __dict__: {hasattr(stu, '__dict__')}")  # False with __slots__
    print()


# =============================================================================
# Example 3: Container-Like Class with __setitem__ and __getitem__
# =============================================================================

class Registry:
    """A registry that stores items by key using dict-like syntax.

    Implements __setitem__ and __getitem__ so you can use
    bracket notation: registry[key] = value
    """

    def __init__(self, name: str):
        self.name = name
        self._items: dict = {}

    def __setitem__(self, key, value):
        """Enable registry[key] = value syntax."""
        self._items[key] = value

    def __getitem__(self, key):
        """Enable registry[key] syntax."""
        return self._items[key]

    def __contains__(self, key) -> bool:
        """Enable 'key in registry' syntax."""
        return key in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self):
        return f"Registry('{self.name}', {len(self)} items)"


def demo_container():
    """Demonstrate container-like class usage."""
    print("=== Container Protocol (__setitem__, __getitem__) ===")

    school = Registry('Python Academy')
    school[1001] = Student(1001, 'Alice')
    school[1002] = Student(1002, 'Bob')
    school[1003] = Student(1003, 'Charlie')

    print(f"Registry: {school}")
    print(f"school[1002] = {school[1002]}")
    print(f"1003 in school: {1003 in school}")
    print(f"9999 in school: {9999 in school}")
    print()


# =============================================================================
# Example 4: Why Both __hash__ and __eq__ Matter
# =============================================================================

def demo_hash_eq_relationship():
    """Explain the relationship between __hash__ and __eq__."""
    print("=== Hash and Equality Relationship ===")

    s1 = Student(1001, 'Alice')
    s2 = Student(1001, 'Alice')
    s3 = Student(1001, 'Bob')

    print(f"s1 = {s1!r}")
    print(f"s2 = {s2!r}")
    print(f"s3 = {s3!r}")
    print()

    print(f"s1 == s2: {s1 == s2}  (same id and name)")
    print(f"s1 is s2: {s1 is s2}  (different objects)")
    print(f"hash(s1) == hash(s2): {hash(s1) == hash(s2)}  (equal -> same hash)")
    print()

    print(f"s1 == s3: {s1 == s3}  (different name)")
    print(f"hash(s1) == hash(s3): {hash(s1) == hash(s3)}  (may differ)")

    print()
    print("Rules:")
    print("  1. Equal objects MUST have the same hash")
    print("  2. Same hash does NOT mean equal (collisions)")
    print("  3. If you define __eq__, define __hash__ too")
    print("  4. Mutable objects generally should NOT be hashable")


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    demo_hashable()
    demo_slots()
    demo_container()
    demo_hash_eq_relationship()
