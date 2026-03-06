"""
Iterator Protocol: Prime Number and Fibonacci Iterators

Custom iterators implementing __iter__() and __next__() for
generating mathematical sequences on demand.

Topics covered:
- Iterator protocol (__iter__ / __next__)
- StopIteration for signaling end of iteration
- Lazy evaluation (values computed one at a time)
- itertools for combinatorial generation

Based on concepts from Python-100-Days example15 and ch02/iteration materials.
"""

import itertools
from math import sqrt


# =============================================================================
# Example 1: Prime Number Iterator
# =============================================================================

def is_prime(num: int) -> bool:
    """Check if a number is prime.

    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    """
    if num < 2:
        return False
    for factor in range(2, int(sqrt(num)) + 1):
        if num % factor == 0:
            return False
    return True


class PrimeIterator:
    """Iterator that yields prime numbers in a given range.

    Implements the iterator protocol:
    - __iter__() returns self (the iterator object)
    - __next__() returns the next prime or raises StopIteration

    >>> primes = list(PrimeIterator(2, 20))
    >>> primes
    [2, 3, 5, 7, 11, 13, 17, 19]
    """

    def __init__(self, start: int, end: int):
        if start < 2:
            start = 2
        self._current = start - 1  # Will be incremented before first check
        self._end = end

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self._current += 1
        while self._current <= self._end:
            if is_prime(self._current):
                return self._current
            self._current += 1
        raise StopIteration()


# =============================================================================
# Example 2: Fibonacci Iterator
# =============================================================================

class FibonacciIterator:
    """Iterator that yields Fibonacci numbers.

    Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    Each number is the sum of the two preceding ones.

    >>> list(FibonacciIterator(8))
    [1, 1, 2, 3, 5, 8, 13, 21]
    """

    def __init__(self, count: int):
        self._count = count
        self._a = 0
        self._b = 1
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self._index >= self._count:
            raise StopIteration()
        self._a, self._b = self._b, self._a + self._b
        self._index += 1
        return self._a


# =============================================================================
# Example 3: Using Iterators in for Loops
# =============================================================================

def demo_iterator_usage():
    """Show how custom iterators work with Python's iteration machinery."""
    print("=== Prime Iterator (primes from 2 to 50) ===")
    for prime in PrimeIterator(2, 50):
        print(prime, end=' ')
    print('\n')

    print("=== Fibonacci Iterator (first 15 numbers) ===")
    for fib in FibonacciIterator(15):
        print(fib, end=' ')
    print('\n')

    # Manual iteration with next()
    print("=== Manual next() calls ===")
    fib_iter = FibonacciIterator(5)
    print(f"next() -> {next(fib_iter)}")  # 1
    print(f"next() -> {next(fib_iter)}")  # 1
    print(f"next() -> {next(fib_iter)}")  # 2
    # Remaining values consumed by for loop
    print("for loop consumes rest:", list(fib_iter))
    print()


# =============================================================================
# Example 4: Iterator vs Generator Comparison
# =============================================================================

def fib_generator(count: int):
    """Generator function equivalent of FibonacciIterator.

    Generators are more concise than iterator classes but
    classes offer more control (reset, state inspection, etc.).
    """
    a, b = 0, 1
    for _ in range(count):
        a, b = b, a + b
        yield a


def demo_iterator_vs_generator():
    """Compare iterator class vs generator function."""
    print("=== Iterator Class vs Generator Function ===")

    # Both produce the same sequence
    from_class = list(FibonacciIterator(10))
    from_generator = list(fib_generator(10))

    print(f"Iterator class: {from_class}")
    print(f"Generator func: {from_generator}")
    print(f"Same result:    {from_class == from_generator}")
    print()


# =============================================================================
# Example 5: itertools with Custom Iterators
# =============================================================================

def demo_itertools():
    """Demonstrate itertools functions with our iterators."""
    print("=== itertools with Custom Iterators ===")

    # Take first 5 primes using islice
    first_5_primes = list(itertools.islice(PrimeIterator(2, 1000), 5))
    print(f"First 5 primes: {first_5_primes}")

    # Chain two iterators
    small_primes = PrimeIterator(2, 10)
    small_fibs = FibonacciIterator(5)
    combined = list(itertools.chain(small_primes, small_fibs))
    print(f"Primes(2-10) + Fib(5): {combined}")

    # Permutations and combinations
    print(f"Permutations of ABC: {list(itertools.permutations('ABC'))}")
    print(f"Combinations C(4,2): {list(itertools.combinations('ABCD', 2))}")
    print(f"Product of AB x 12:  {list(itertools.product('AB', '12'))}")
    print()


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    demo_iterator_usage()
    demo_iterator_vs_generator()
    demo_itertools()
