"""
Example 2: Comparison Operators
Demonstrates: __eq__, __ne__, __lt__, __le__, __gt__, __ge__
"""


class Student:
    """A student with grade-based comparisons."""
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __repr__(self):
        return f"Student('{self.name}', {self.grade})"
    
    def __eq__(self, other):
        """Check if two students have the same grade."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade == other.grade
    
    def __ne__(self, other):
        """Check if two students have different grades."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade != other.grade
    
    def __lt__(self, other):
        """Check if this student's grade is less than another's."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade < other.grade
    
    def __le__(self, other):
        """Check if this student's grade is less than or equal to another's."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade <= other.grade
    
    def __gt__(self, other):
        """Check if this student's grade is greater than another's."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade > other.grade
    
    def __ge__(self, other):
        """Check if this student's grade is greater than or equal to another's."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade >= other.grade


class Version:
    """A version class that can be compared (e.g., 1.2.3)."""
    
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch
    
    def __repr__(self):
        return f"Version({self.major}, {self.minor}, {self.patch})"
    
    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"
    
    def _as_tuple(self):
        """Convert to tuple for easy comparison."""
        return (self.major, self.minor, self.patch)
    
    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._as_tuple() == other._as_tuple()
    
    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._as_tuple() < other._as_tuple()
    
    def __le__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._as_tuple() <= other._as_tuple()
    
    def __gt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._as_tuple() > other._as_tuple()
    
    def __ge__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._as_tuple() >= other._as_tuple()


# Examples
if __name__ == "__main__":

    # ============================================================================
    print("=== Student Comparison Examples ===")
    alice = Student("Alice", 85)
    bob = Student("Bob", 92)
    charlie = Student("Charlie", 85)
    
    print(f"{alice.name}: {alice.grade}")
    print(f"{bob.name}: {bob.grade}")
    print(f"{charlie.name}: {charlie.grade}")
    
    print(f"\nAlice == Charlie: {alice == charlie}")
    print(f"Alice == Bob: {alice == bob}")
    print(f"Alice < Bob: {alice < bob}")
    print(f"Bob > Alice: {bob > alice}")
    print(f"Alice <= Charlie: {alice <= charlie}")
    
    # Sorting students by grade
    students = [bob, alice, charlie, Student("David", 78), Student("Eve", 95)]
    print("\n=== Sorting Students ===")
    print("Original:", students)
    sorted_students = sorted(students)
    print("Sorted by grade:", sorted_students)
    
    print("\n\n=== Version Comparison Examples ===")
    v1 = Version(1, 2, 3)
    v2 = Version(1, 2, 4)
    v3 = Version(2, 0, 0)
    v4 = Version(1, 2, 3)
    
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"v3: {v3}")
    print(f"v4: {v4}")
    
    print(f"\nv1 == v4: {v1 == v4}")
    print(f"v1 < v2: {v1 < v2}")
    print(f"v2 < v3: {v2 < v3}")
    print(f"v3 > v1: {v3 > v1}")
    
    versions = [v3, v1, v2, Version(0, 9, 5)]
    print("\n=== Sorting Versions ===")
    print("Original:", versions)
    print("Sorted:", sorted(versions))
