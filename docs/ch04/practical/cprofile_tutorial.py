"""
PYTHON CODE PROFILING & OPTIMIZATION - INTERMEDIATE LEVEL
==========================================================
Module 5: cProfile Basics - Function-Level Profiling

LEARNING OBJECTIVES:
- Master cProfile for function-level profiling
- Understand profiling output metrics
- Learn to identify performance bottlenecks
- Profile scripts and functions
- Interpret profiling data effectively

Author: Python Course Development Team
Date: 2024
"""

import cProfile
import pstats
from io import StringIO


def fibonacci_recursive(n):
    """Inefficient recursive Fibonacci"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    """Efficient iterative Fibonacci"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def demonstrate_basic_profiling():
    """Basic cProfile usage"""
    print("=" * 70)
    print("BASIC CPROFILE USAGE")
    print("=" * 70)
    
    print("\nProfiling recursive Fibonacci(20):\n")
    
    # Profile using cProfile.run()
    cProfile.run('fibonacci_recursive(20)')


def profile_with_stats():
    """Profile and analyze with pstats"""
    print("\n" + "=" * 70)
    print("PROFILING WITH PSTATS")
    print("=" * 70)
    
    # Create profiler
    profiler = cProfile.Profile()
    
    # Profile the code
    profiler.enable()
    result = fibonacci_recursive(25)
    profiler.disable()
    
    # Analyze results
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    
    print(f"\nFibonacci(25) = {result}\n")
    print("Top 10 functions by cumulative time:")
    stats.print_stats(10)


def compare_implementations():
    """Compare recursive vs iterative"""
    print("\n" + "=" * 70)
    print("COMPARING IMPLEMENTATIONS")
    print("=" * 70)
    
    n = 30
    
    print(f"\n1. Recursive Fibonacci({n}):")
    profiler1 = cProfile.Profile()
    profiler1.enable()
    result1 = fibonacci_recursive(n)
    profiler1.disable()
    
    stats1 = pstats.Stats(profiler1)
    print(f"   Result: {result1}")
    print(f"   Total calls: {stats1.total_calls:,}")
    
    print(f"\n2. Iterative Fibonacci({n}):")
    profiler2 = cProfile.Profile()
    profiler2.enable()
    result2 = fibonacci_iterative(n)
    profiler2.disable()
    
    stats2 = pstats.Stats(profiler2)
    print(f"   Result: {result2}")
    print(f"   Total calls: {stats2.total_calls:,}")
    
    print(f"\nRecursive made {stats1.total_calls:,} function calls!")
    print(f"Iterative made {stats2.total_calls:,} function calls!")


def main():
    """Run all demonstrations"""
    print("\n" + "=" * 70)
    print("CPROFILE BASICS - COMPREHENSIVE TUTORIAL")
    print("=" * 70 + "\n")
    
    demonstrate_basic_profiling()
    profile_with_stats()
    compare_implementations()
    
    print("\n" + "=" * 70)
    print("KEY METRICS IN CPROFILE OUTPUT")
    print("=" * 70)
    print("""
    ncalls:    Number of calls to the function
    tottime:   Total time spent in function (excluding subcalls)
    percall:   tottime / ncalls
    cumtime:   Cumulative time (including subcalls)
    percall:   cumtime / ncalls
    filename:lineno(function)
    
    Key Insights:
    - High cumtime: Function takes significant total time
    - High tottime: Function itself is slow (not subcalls)
    - High ncalls: Function is called very frequently
    - Focus optimization on high cumtime AND high tottime
    """)

if __name__ == "__main__":
    main()
