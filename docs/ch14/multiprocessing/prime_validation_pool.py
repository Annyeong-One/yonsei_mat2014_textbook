"""
Prime Number Validation: Serial vs Multiprocessing Pool

This tutorial demonstrates how to use multiprocessing for CPU-bound tasks.

WHAT IS CPU-BOUND WORK?
Tasks that spend most time doing computation (not waiting for I/O).
Examples: prime checking, calculations, data processing, compression.

WHY MULTIPROCESSING HELPS:
- Python's GIL (Global Interpreter Lock) prevents true parallelism with threads
- Multiprocessing creates separate processes (each has own GIL)
- On multi-core CPUs, processes can run truly in parallel
- Can achieve near-linear speedup with N cores

THE TASK:
Check if large numbers are prime. This is computationally expensive:
- Even with optimization, checking a large number takes millions of divisions
- No I/O involved, so it's pure CPU work
- Perfect for multiprocessing!

TECHNIQUES:
1. Serial: Check primes one at a time in main process
2. Pool: Use multiprocessing.Pool to distribute work across cores

Learning Goals:
- Understand when multiprocessing is appropriate
- Learn to use multiprocessing.Pool
- See real speedup from parallelization
- Understand the overhead involved
"""

import math
import time
from multiprocessing import Pool, cpu_count

if __name__ == "__main__":


    print("=" * 70)
    print("PRIME VALIDATION: SERIAL vs MULTIPROCESSING")
    print("=" * 70)


    # ============ EXAMPLE 1: Understanding Prime Checking ============
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Understanding Prime Number Checking")
    print("=" * 70)

    print("""
    A prime number is only divisible by 1 and itself.

    NAIVE APPROACH: Check all numbers up to n
        Too slow! For n = 10^18, this would take forever.

    OPTIMIZED APPROACH (used here):
    1. If n is even, it's not prime (except 2)
    2. Only check odd divisors from 3 to sqrt(n)
    3. If no divisor found, n is prime

    WHY ONLY UP TO sqrt(n)?
    If n = a * b where a <= b, then a <= sqrt(n).
    So if n has a factor, we'll find one <= sqrt(n).

    Example: Is 97 prime?
    - sqrt(97) ≈ 9.8
    - Check: 97 % 3, 97 % 5, 97 % 7, 97 % 9
    - None divide evenly, so 97 is prime!

    Example: Is 99 prime?
    - sqrt(99) ≈ 9.9
    - Check: 99 % 3 = 0, so 99 = 3 * 33, not prime!

    Even with this optimization, checking large primes (15+ digits) takes
    significant CPU time. This is why it's good for demonstrating multiprocessing.
    """)


    # ============ EXAMPLE 2: Prime Checking Function ============
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Implement Prime Checking Function")
    print("=" * 70)

    def check_prime(n):
        """
        Check if n is a prime number.

        Algorithm:
        1. Even numbers (except 2) are not prime
        2. Check odd divisors from 3 to sqrt(n)
        3. Use step of 2 to skip even numbers

        This is CPU-bound work: pure computation, no I/O.

        Time complexity: O(sqrt(n))
        For n ~ 10^18, sqrt(n) ~ 10^9, so millions of checks.
        """
        if n % 2 == 0:
            return False

        # Only need to check up to sqrt(n)
        from_i = 3
        to_i = math.sqrt(n) + 1

        # Check odd numbers only (step by 2)
        for i in range(from_i, int(to_i), 2):
            if n % i == 0:
                return False

        return True


    # Test with some examples
    test_numbers = [
        (2, True),
        (97, True),
        (100, False),
        (10007, True),
    ]

    print("\nTesting check_prime():")
    for num, expected in test_numbers:
        result = check_prime(num)
        status = "PASS" if result == expected else "FAIL"
        print(f"  check_prime({num:6}) = {result:5} (expected {expected:5}) [{status}]")


    # ============ EXAMPLE 3: Expensive Test Numbers ============
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Test with Large Numbers")
    print("=" * 70)

    print("""
    We'll test with large numbers that take significant time to check.

    These are actual large primes and non-primes from cryptography:
    - Large primes are expensive to verify
    - Large composites are also expensive (must check many divisors before confirming)

    Expected checking times (on modern CPU):
    - 12-15 digit numbers: milliseconds
    - 18 digit numbers: seconds
    - 20+ digit numbers: tens of seconds
    """)

    # Test numbers - these are real cryptographic numbers
    test_cases = [
        ("trivial non-prime", 112272535095295),
        ("15-digit composite", 100109100129100369),
        ("15-digit composite 2", 100109100129101027),
        ("18-digit prime", 100109100129100151),
        ("18-digit prime 2", 100109100129162907),
    ]

    print(f"\nQuick validation on one number:")
    num, label = test_cases[0]
    print(f"  Testing {label}: {num}")
    start = time.time()
    is_prime = check_prime(num)
    elapsed = time.time() - start
    print(f"  Result: {is_prime} (checked in {elapsed:.4f}s)")


    # ============ EXAMPLE 4: Serial Processing ============
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Serial Processing (One at a time)")
    print("=" * 70)

    print("""
    Process each number one at a time in the main process.

    WHY IT'S SLOW:
    - CPU can only do one thing at a time
    - No parallelism at all
    - Wastes cores on multi-core machines

    Complexity:
    - 4 numbers, each taking 1-2 seconds
    - Total: ~4-8 seconds
    - Only using 1 of your N cores
    """)

    print(f"\nProcessing {len(test_cases)} numbers serially:")
    print(f"Current CPU count: {cpu_count()} cores\n")

    results_serial = []
    start_total = time.time()

    for label, number in test_cases:
        start = time.time()
        is_prime = check_prime(number)
        elapsed = time.time() - start
        results_serial.append((label, number, is_prime, elapsed))
        print(f"  {label:20} ({number}): {is_prime:5} ({elapsed:.4f}s)")

    elapsed_total_serial = time.time() - start_total
    print(f"\nTotal serial time: {elapsed_total_serial:.4f}s")
    print(f"Average per number: {elapsed_total_serial/len(test_cases):.4f}s")


    # ============ EXAMPLE 5: Multiprocessing Pool ============
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Multiprocessing Pool (Parallel)")
    print("=" * 70)

    print("""
    Use multiprocessing.Pool to distribute work across multiple processes.

    HOW IT WORKS:
    1. Create a Pool with N worker processes (default: CPU count)
    2. Submit jobs using pool.apply_async() or pool.map()
    3. Each worker process runs jobs in parallel
    4. Collect results

    WHY IT'S FASTER:
    - Each process runs on a separate CPU core
    - True parallelism (not limited by GIL)
    - Can check multiple numbers simultaneously
    - Speedup approximately = min(num_jobs, num_cores)

    OVERHEAD:
    - Creating processes takes time (~0.1s each)
    - Serializing data to pass to processes (pickling)
    - For small jobs, overhead might exceed speedup!
    - For large jobs, speedup dominates

    In this case:
    - Each job takes 1-2 seconds
    - Process creation overhead (~0.5s total) is small
    - Clear speedup expected
    """)

    print(f"\nProcessing {len(test_cases)} numbers with multiprocessing Pool:")

    start_total = time.time()

    # Create a Pool with default number of workers (CPU count)
    with Pool() as pool:
        # Use map() to apply check_prime to each number
        # Returns results in same order as input
        numbers = [num for label, num in test_cases]
        results_list = pool.map(check_prime, numbers)

    elapsed_total_parallel = time.time() - start_total

    # Print results
    for (label, number), is_prime in zip(test_cases, results_list):
        print(f"  {label:20} ({number}): {is_prime:5}")

    print(f"\nTotal parallel time: {elapsed_total_parallel:.4f}s")
    print(f"Average per number: {elapsed_total_parallel/len(test_cases):.4f}s")


    # ============ EXAMPLE 6: Performance Comparison ============
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Performance Comparison")
    print("=" * 70)

    speedup = elapsed_total_serial / elapsed_total_parallel
    num_cores = cpu_count()

    print(f"\nSpeedup Analysis:")
    print(f"  Serial time:     {elapsed_total_serial:.4f}s")
    print(f"  Parallel time:   {elapsed_total_parallel:.4f}s")
    print(f"  Speedup:         {speedup:.2f}x")
    print(f"  CPU cores:       {num_cores}")
    print(f"  Efficiency:      {speedup/num_cores*100:.1f}% (speedup / cores)")

    print(f"\nInterpretation:")
    if speedup > 1:
        print(f"  Multiprocessing is {speedup:.1f}x faster!")
        if speedup > num_cores * 0.8:
            print(f"  Good efficiency: Using cores well (>80%)")
        else:
            print(f"  Okay efficiency: Using cores okay (overhead present)")
    else:
        print(f"  Serial is faster (overhead > benefit)")
        print(f"  This can happen with small jobs or I/O-bound work")

    print(f"\n{'*' * 70}")
    print("WHEN MULTIPROCESSING HELPS")
    print("{'*' * 70}")

    print(f"""
    GOOD FOR MULTIPROCESSING:
    - CPU-bound tasks (pure computation)
    - Long-running jobs (seconds or more)
    - Many independent items to process
    - Available CPU cores to distribute to

    BAD FOR MULTIPROCESSING:
    - I/O-bound tasks (use threading or async instead)
    - Quick jobs (overhead > benefit)
    - Need to share mutable state
    - On single-core machines

    FOR THIS TASK (prime checking):
    - Job time: 1-2 seconds each (large numbers)
    - CPU-bound: Pure math, no I/O
    - Independent: Each number is independent
    - Result: Multiprocessing is clearly beneficial
    """)


    # ============ EXAMPLE 7: Advanced Pool Usage ============
    print("\n" + "=" * 70)
    print("EXAMPLE 7: Advanced Pool Usage - apply_async()")
    print("=" * 70)

    print("""
    Different ways to use Pool:

    1. pool.map(func, iterable)
       - Apply func to each item
       - Blocks until all results ready
       - Returns list of results

    2. pool.apply_async(func, args)
       - Submit single job
       - Returns immediately with AsyncResult object
       - Get result later with .get()

    3. pool.imap(func, iterable)
       - Like map, but returns iterator
       - Results available as they complete

    For this example, map() is fine. For more complex scenarios,
    async methods let you submit jobs without waiting.
    """)

    print(f"\nDemonstration with apply_async():")

    start_total = time.time()

    with Pool() as pool:
        # Submit all jobs without waiting
        async_results = []
        for label, number in test_cases:
            async_result = pool.apply_async(check_prime, (number,))
            async_results.append((label, number, async_result))

        # Collect results as they complete
        print("Jobs submitted, waiting for results...\n")

        for label, number, async_result in async_results:
            is_prime = async_result.get()  # Blocks until this specific job completes
            print(f"  {label:20} ({number}): {is_prime:5}")

    elapsed_async = time.time() - start_total
    print(f"\nTotal time with async: {elapsed_async:.4f}s")


    # ============ EXAMPLE 8: Overhead Analysis ============
    print("\n" + "=" * 70)
    print("EXAMPLE 8: Understanding Multiprocessing Overhead")
    print("=" * 70)

    print("""
    Multiprocessing has overhead:

    1. PROCESS CREATION: ~0.1-0.2s per process
       - Creating processes is expensive
       - Pool reuses processes to amortize this

    2. PICKLING/SERIALIZATION: Time to send data to processes
       - Data must be converted to bytes and sent via IPC
       - Getting results back has same cost
       - Small data: negligible
       - Large data: can be significant

    3. CONTEXT SWITCHING: OS switching between processes
       - Not a huge factor on modern systems

    WHEN OVERHEAD DOMINATES:
    - Small jobs (microseconds)
    - Frequent small submissions
    - Large data to transfer

    WHEN SPEEDUP DOMINATES:
    - Long jobs (seconds+)
    - Batch submissions
    - Small data transfer

    FOR THIS TASK:
    - Process creation: ~0.5s total (5 processes, once at start)
    - Per-job overhead: Negligible (just int, bool transfer)
    - Job time: 1-2 seconds each
    - Result: Overhead is <20% of time, speedup dominates!
    """)


    print("\n" + "=" * 70)
    print("KEY TAKEAWAY")
    print("=" * 70)
    print(f"""
    Multiprocessing provides {speedup:.1f}x speedup for this CPU-bound task.

    USE MULTIPROCESSING WHEN:
    1. Task is CPU-bound (computation, not I/O)
    2. Jobs take significant time (seconds+)
    3. You have multiple cores available
    4. Data transfer overhead is small

    USE THREADING FOR:
    - I/O-bound tasks (network, disk, databases)
    - Quick tasks with frequent context switches

    USE ASYNCIO FOR:
    - I/O-bound tasks with many concurrent operations
    - Modern, efficient I/O multiplexing

    FOR PEAK PERFORMANCE:
    1. Profile to confirm it's worth optimizing
    2. Start with simple Pool.map() approach
    3. Use apply_async() for more control if needed
    4. Consider process count (default: CPU count)
    5. Measure actual speedup vs single-threaded baseline

    Remember: Don't optimize prematurely! Use multiprocessing
    only when profiling shows it's needed for CPU-bound work.
    """)
