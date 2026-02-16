"""
TUTORIAL: ThreadPoolExecutor.map() for Concurrent Execution
============================================================

In this tutorial, you'll learn how to use ThreadPoolExecutor.map() to run
multiple functions concurrently with a pool of worker threads.

KEY CONCEPTS:
- ThreadPoolExecutor: A pool of reusable worker threads
- executor.map(): Apply a function to multiple arguments concurrently
- Iterator pattern: Results are returned as an iterator
- Lazy evaluation: Results computed on-demand as you iterate
- Thread pooling: Reuses threads instead of creating new ones

WHY THIS MATTERS:
- Much faster than creating a new thread for each task
- Perfect for I/O-bound work (network, file operations)
- Cleaner API than managing individual threads manually
"""

from time import sleep, strftime
from concurrent import futures


print("=" * 70)
print("THREADPOOLEXECUTOR.MAP() FOR CONCURRENT EXECUTION")
print("=" * 70)
print()


# ============ HELPER FUNCTIONS FOR LOGGING
# ===========================================

def display(*args):
    """
    Print with a timestamp prefix.

    WHY: This helps us see exactly when each task starts and finishes.
    The [HH:MM:SS] prefix shows the precise timing of concurrent operations.
    """
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


# ============ EXAMPLE 1: Understanding the Concurrent Task
# ==========================================================

print("EXAMPLE 1: The Task We'll Run Concurrently")
print("-" * 70)
print()
print("We'll create a function that simulates work by sleeping.")
print("This represents I/O-bound tasks like network requests.")
print()


def loiter(n):
    """
    Simulate work that takes n seconds.

    WHY THIS DESIGN:
    - Sleeping simulates network I/O or file operations
    - The function takes n seconds and returns n*10
    - With threads, all these can run in parallel!

    Args:
        n: Number of seconds to sleep (simulating work)

    Returns:
        n * 10 (a processed result)
    """

    msg = '{}loiter({}): doing nothing for {}s...'
    # \t adds indentation proportional to n - helps visualize which task
    display(msg.format('\t' * n, n, n))

    # Sleep to simulate I/O-bound work
    sleep(n)

    msg = '{}loiter({}): done.'
    display(msg.format('\t' * n, n))

    return n * 10


print("Function loiter(n) defined:")
print("• Takes n seconds (simulates I/O)")
print("• Returns n * 10")
print()
print("About to call loiter(1), loiter(2), loiter(3), loiter(4), loiter(5)")
print()


# ============ EXAMPLE 2: Sequential vs Concurrent Timing
# ========================================================

print("EXAMPLE 2: Understanding the Difference")
print("-" * 70)
print()
print("SEQUENTIAL APPROACH (without threading):")
print("  loiter(1): 1 second")
print("  loiter(2): 2 seconds")
print("  loiter(3): 3 seconds")
print("  loiter(4): 4 seconds")
print("  loiter(5): 5 seconds")
print("  Total: 15 seconds (everything waits for the previous task)")
print()
print("CONCURRENT APPROACH (with ThreadPoolExecutor):")
print("  All tasks run in parallel!")
print("  Total: ~5 seconds (longest task determines total time)")
print()
print("Watch the timestamps below - you'll see multiple tasks running")
print("at the SAME TIME when we use executor.map():")
print()


# ============ EXAMPLE 3: Using ThreadPoolExecutor.map()
# ======================================================

def main():
    """
    Demonstrate ThreadPoolExecutor.map() for concurrent execution.
    """

    print("=" * 70)
    print("STARTING CONCURRENT EXECUTION")
    print("=" * 70)
    print()

    # Record the start time to see total elapsed time
    display('Script starting.')
    print()

    # Create a ThreadPoolExecutor with 3 worker threads
    # WHY 3 workers?
    # - With max_workers=3, we can run 3 tasks in parallel
    # - Task 1,2,3 start immediately
    # - When task 1 finishes, task 4 starts
    # - When task 2 finishes, task 5 starts
    # - This is much more efficient than 5 threads!
    executor = futures.ThreadPoolExecutor(max_workers=3)

    print(f"Created ThreadPoolExecutor with max_workers=3")
    print()
    print("executor.map(loiter, range(5)) will:")
    print("  • Create 5 tasks: loiter(0), loiter(1), loiter(2), loiter(3), loiter(4)")
    print("  • Run them across 3 worker threads concurrently")
    print("  • Return an iterator of results")
    print()

    # Execute all the tasks concurrently
    # WHY map()? It applies loiter() to each number in range(5)
    # and returns an iterator of results
    results = executor.map(loiter, range(5))

    # Important: results is an ITERATOR, not a list!
    # WHY? Because results haven't been computed yet.
    # They're computed lazily as we iterate over them below.
    display('results:', results)
    print()
    print("Note: 'results' is an iterator, not a list of values yet")
    print("The actual computation hasn't happened - it starts when we")
    print("iterate over the results below!")
    print()

    # Now iterate over the results
    # WHY iterate instead of just accessing results?
    # 1. Lets us get results as they complete (lazy evaluation)
    # 2. Blocks until each result is ready
    # 3. Respects the order of the original tasks
    display('Waiting for individual results:')
    print()

    for i, result in enumerate(results):
        # Each iteration here blocks until that result is ready
        # Result 0 finishes first (loiter(0) is instant)
        # Then results appear in order as they complete
        display(f'result {i}: {result}')

    print()
    print("=" * 70)
    print("All tasks completed!")
    print("=" * 70)


# ============ EXAMPLE 4: Key Concepts Explained
# ==============================================

print()
print("=" * 70)
print("KEY CONCEPTS:")
print("=" * 70)
print()
print("1. ThreadPoolExecutor: Manages a fixed number of worker threads")
print()
print("2. executor.map(func, iterable):")
print("   • Applies func to each item in iterable")
print("   • Returns an ITERATOR of results (computed lazily)")
print("   • Maintains order of results (even if tasks finish out of order)")
print()
print("3. max_workers:")
print("   • Number of threads in the pool")
print("   • Use max_workers=3 for 5 tasks = efficient reuse")
print("   • Don't use max_workers=5 for 5 tasks (wastes resources)")
print()
print("4. Lazy Evaluation:")
print("   • Results iterator doesn't compute anything until you iterate")
print("   • Each iteration blocks until that specific result is ready")
print("   • This saves memory and allows result streaming")
print()
print("5. When to Use ThreadPoolExecutor:")
print("   • I/O-bound tasks (network, file, database operations)")
print("   • NOT CPU-bound tasks (use multiprocessing.Pool instead)")
print()
print("=" * 70)
print()


if __name__ == '__main__':
    main()
