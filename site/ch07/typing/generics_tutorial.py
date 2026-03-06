"""
Tutorial 07: Generic Types and TypeVar
======================================

Level: Advanced

This tutorial covers generic types, TypeVar, and how to create
flexible, reusable functions and classes that work with multiple types.

Learning Objectives:
- Understand and use TypeVar
- Create generic functions
- Build generic classes
- Use constraints and bounds on TypeVars
- Work with multiple TypeVars

Prerequisites:
- All previous tutorials
"""

from typing import TypeVar, Generic, List, Optional, Sequence, Callable

# =============================================================================
# SECTION 1: TypeVar Basics
# =============================================================================

# TypeVar creates a type variable that can represent any type
T = TypeVar('T')

def identity(value: T) -> T:
    """Return the same value - preserves type."""
    return value

# Usage:
x: int = identity(5)  # T is int
y: str = identity("hello")  # T is str


def get_first(items: Sequence[T]) -> Optional[T]:
    """Get first item, preserving type."""
    return items[0] if items else None


def reverse_list(items: List[T]) -> List[T]:
    """Reverse a list, preserving element type."""
    return list(reversed(items))


# =============================================================================
# SECTION 2: Multiple TypeVars
# =============================================================================

T1 = TypeVar('T1')
T2 = TypeVar('T2')

def pair(first: T1, second: T2) -> tuple[T1, T2]:
    """Create a pair of potentially different types."""
    return (first, second)


def map_pair(pair: tuple[T1, T2], func1: Callable[[T1], T1], func2: Callable[[T2], T2]) -> tuple[T1, T2]:
    """Apply functions to both elements of a pair."""
    return (func1(pair[0]), func2(pair[1]))


# =============================================================================
# SECTION 3: Generic Classes
# =============================================================================

class Stack(Generic[T]):
    """Generic stack data structure."""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self._items.append(item)
    
    def pop(self) -> T:
        """Pop an item from the stack."""
        if not self._items:
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> Optional[T]:
        """Peek at top item without removing."""
        return self._items[-1] if self._items else None
    
    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._items) == 0


class Pair(Generic[T1, T2]):
    """Generic pair of two potentially different types."""
    
    def __init__(self, first: T1, second: T2) -> None:
        self.first = first
        self.second = second
    
    def get_first(self) -> T1:
        return self.first
    
    def get_second(self) -> T2:
        return self.second
    
    def swap(self) -> 'Pair[T2, T1]':
        """Return a new pair with swapped elements."""
        return Pair(self.second, self.first)


# =============================================================================
# SECTION 4: Constrained TypeVars
# =============================================================================

from typing import Union

# TypeVar with constraints
NumberType = TypeVar('NumberType', int, float)

def add(x: NumberType, y: NumberType) -> NumberType:
    """Add two numbers (int or float)."""
    return x + y  # type: ignore


def multiply(x: NumberType, y: NumberType) -> NumberType:
    """Multiply two numbers."""
    return x * y  # type: ignore


# =============================================================================
# SECTION 5: Bounded TypeVars
# =============================================================================

class Comparable:
    """Base class for comparable objects."""
    def __lt__(self, other: 'Comparable') -> bool:
        raise NotImplementedError

ComparableType = TypeVar('ComparableType', bound=Comparable)

def find_min(items: Sequence[ComparableType]) -> Optional[ComparableType]:
    """Find minimum item (must be comparable)."""
    if not items:
        return None
    return min(items)


# =============================================================================
# SECTION 6: Practical Examples
# =============================================================================

class Box(Generic[T]):
    """A container that holds a value."""
    
    def __init__(self, value: T) -> None:
        self._value = value
    
    def get(self) -> T:
        """Get the contained value."""
        return self._value
    
    def set(self, value: T) -> None:
        """Set a new value."""
        self._value = value
    
    def map(self, func: Callable[[T], T]) -> 'Box[T]':
        """Apply a function to the contained value."""
        return Box(func(self._value))


def filter_list(items: List[T], predicate: Callable[[T], bool]) -> List[T]:
    """Filter items using a predicate."""
    return [item for item in items if predicate(item)]


if __name__ == "__main__":
    print("=== Generic Types Examples ===\n")
    
    # Basic TypeVar
    print("TypeVar:")
    print(f"  identity(5): {identity(5)}")
    print(f"  identity('hello'): {identity('hello')}")
    print(f"  get_first([1,2,3]): {get_first([1,2,3])}")
    print()
    
    # Generic classes
    print("Generic Classes:")
    int_stack: Stack[int] = Stack()
    int_stack.push(1)
    int_stack.push(2)
    print(f"  Stack pop: {int_stack.pop()}")
    
    str_stack: Stack[str] = Stack()
    str_stack.push("hello")
    print(f"  String stack peek: {str_stack.peek()}")
    print()
    
    # Pair
    p = Pair(10, "hello")
    print(f"  Pair: ({p.get_first()}, {p.get_second()})")
    swapped = p.swap()
    print(f"  Swapped: ({swapped.get_first()}, {swapped.get_second()})")
