"""
Function Practice: Practical Applications

A collection of practical function examples demonstrating proper
function design, type hints, keyword-only arguments, and building
reusable utility functions.

Examples covered:
1. Random verification code generator
2. Prime number checker (with type hints)
3. GCD and LCM (function composition)
4. Descriptive statistics from scratch
5. Lottery number generator (random sampling)

Based on Python-100-Days Day15 function practice examples.
"""

import random
import string
from math import sqrt


# =============================================================================
# Example 1: Random Verification Code
# =============================================================================

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(*, length: int = 4) -> str:
    """Generate a random verification code of alphanumeric characters.

    Uses keyword-only argument (after *) to prevent positional mistakes.
    random.choices() does sampling WITH replacement (can repeat characters).

    >>> len(generate_code())
    4
    >>> len(generate_code(length=8))
    8
    """
    return ''.join(random.choices(ALL_CHARS, k=length))


# =============================================================================
# Example 2: Prime Number Checker
# =============================================================================

def is_prime(num: int) -> bool:
    """Check if a positive integer greater than 1 is prime.

    Optimization: only check divisors up to sqrt(num).
    If no divisor found up to sqrt(num), none exists beyond it.

    Type hints (: int, -> bool) document expected types
    without affecting execution.

    >>> is_prime(17)
    True
    >>> is_prime(15)
    False
    >>> is_prime(2)
    True
    """
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# =============================================================================
# Example 3: GCD and LCM (Function Composition)
# =============================================================================

def gcd(x: int, y: int) -> int:
    """Compute Greatest Common Divisor using Euclidean algorithm.

    The algorithm repeatedly replaces the larger number with the
    remainder of dividing the two numbers, until the remainder is 0.

    >>> gcd(12, 8)
    4
    >>> gcd(17, 5)
    1
    """
    while y != 0:
        x, y = y, x % y
    return x


def lcm(x: int, y: int) -> int:
    """Compute Least Common Multiple.

    LCM = (x * y) / GCD(x, y)
    This function CALLS gcd() - functions can compose together.

    >>> lcm(12, 8)
    24
    >>> lcm(3, 5)
    15
    """
    return x * y // gcd(x, y)


# =============================================================================
# Example 4: Descriptive Statistics from Scratch
# =============================================================================

def mean(data: list[float]) -> float:
    """Arithmetic mean (average).

    >>> mean([1, 2, 3, 4, 5])
    3.0
    """
    return sum(data) / len(data)


def median(data: list[float]) -> float:
    """Median (middle value of sorted data).

    For odd count: the middle element.
    For even count: average of the two middle elements.

    >>> median([1, 3, 5, 7, 9])
    5
    >>> median([1, 2, 3, 4])
    2.5
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 != 0:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2


def ptp(data: list[float]) -> float:
    """Range (peak-to-peak): max - min.

    >>> ptp([3, 1, 4, 1, 5, 9])
    8
    """
    return max(data) - min(data)


def variance(data: list[float], ddof: int = 1) -> float:
    """Sample variance (ddof=1) or population variance (ddof=0).

    ddof = degrees of freedom adjustment.
    Sample variance uses (n-1) in denominator (Bessel's correction).

    >>> variance([2, 4, 4, 4, 5, 5, 7, 9])
    4.0
    """
    x_bar = mean(data)
    squared_diffs = [(x - x_bar) ** 2 for x in data]
    return sum(squared_diffs) / (len(data) - ddof)


def std(data: list[float], ddof: int = 1) -> float:
    """Standard deviation (square root of variance).

    >>> std([2, 4, 4, 4, 5, 5, 7, 9])
    2.0
    """
    return variance(data, ddof) ** 0.5


def cv(data: list[float], ddof: int = 1) -> float:
    """Coefficient of variation: std / mean.

    Measures relative variability (unitless).
    Useful for comparing spread between datasets with different scales.
    """
    return std(data, ddof) / mean(data)


def describe(data: list[float]) -> None:
    """Print descriptive statistics summary.

    Similar to pandas DataFrame.describe() but implemented from scratch.
    """
    print(f"  Count:    {len(data)}")
    print(f"  Mean:     {mean(data):.4f}")
    print(f"  Median:   {median(data):.4f}")
    print(f"  Range:    {ptp(data):.4f}")
    print(f"  Variance: {variance(data):.4f}")
    print(f"  Std Dev:  {std(data):.4f}")
    print(f"  CV:       {cv(data):.4f}")


# =============================================================================
# Example 5: Lottery Number Generator
# =============================================================================

def generate_lottery() -> list[int]:
    """Generate a set of lottery numbers.

    6 numbers from 1-33 (sorted, no replacement) + 1 bonus from 1-16.
    Uses random.sample() for sampling WITHOUT replacement.

    >>> numbers = generate_lottery()
    >>> len(numbers)
    7
    >>> all(1 <= n <= 33 for n in numbers[:6])
    True
    """
    main_numbers = sorted(random.sample(range(1, 34), 6))
    bonus = random.choice(range(1, 17))
    return main_numbers + [bonus]


def display_lottery(numbers: list[int]) -> None:
    """Display lottery numbers with formatting."""
    main = ' '.join(f'{n:02d}' for n in numbers[:-1])
    bonus = f'{numbers[-1]:02d}'
    print(f"  {main}  |  {bonus}")


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    print("=== Verification Codes ===")
    for _ in range(5):
        print(f"  {generate_code(length=6)}")
    print()

    print("=== Prime Numbers (2-50) ===")
    primes = [n for n in range(2, 51) if is_prime(n)]
    print(f"  {primes}")
    print()

    print("=== GCD and LCM ===")
    for a, b in [(12, 8), (17, 5), (36, 24)]:
        print(f"  gcd({a}, {b}) = {gcd(a, b)},  lcm({a}, {b}) = {lcm(a, b)}")
    print()

    print("=== Descriptive Statistics ===")
    data = [85, 92, 78, 90, 88, 76, 95, 89, 82, 91]
    print(f"  Data: {data}")
    describe(data)
    print()

    print("=== Lottery Numbers (5 draws) ===")
    for _ in range(5):
        display_lottery(generate_lottery())
