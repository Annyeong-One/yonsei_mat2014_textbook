"""
Asyncio: Coroutines with asyncio.gather()

Demonstrates concurrent coroutines running cooperative tasks.
Two async tasks (prime filtering and square mapping) run
concurrently using asyncio.gather().

Topics covered:
- async/await syntax
- asyncio.gather() for concurrent coroutines
- yield from for delegation to sub-generators
- Cooperative multitasking with await asyncio.sleep()

Based on concepts from Python-100-Days example23 and ch14/asyncio materials.
"""

import asyncio
from math import sqrt


# =============================================================================
# Example 1: Helper Functions
# =============================================================================

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for factor in range(2, int(sqrt(num)) + 1):
        if num % factor == 0:
            return False
    return True


def number_range(start: int, end: int):
    """Generator that yields numbers in range.

    Using 'yield from' to delegate to range().
    """
    yield from range(start, end + 1)


# =============================================================================
# Example 2: Concurrent Coroutines
# =============================================================================

async def prime_filter(start: int, end: int) -> tuple[int, ...]:
    """Async coroutine that filters prime numbers from a range.

    The await asyncio.sleep(0) call yields control to the event loop,
    allowing other coroutines to run. This is cooperative multitasking.
    """
    primes = []
    for n in number_range(start, end):
        if is_prime(n):
            primes.append(n)
        # Yield control to event loop periodically
        if n % 10 == 0:
            await asyncio.sleep(0)
    return tuple(primes)


async def square_mapper(start: int, end: int) -> list[int]:
    """Async coroutine that computes squares of numbers in a range."""
    squares = []
    for n in number_range(start, end):
        squares.append(n * n)
        if n % 10 == 0:
            await asyncio.sleep(0)
    return squares


# =============================================================================
# Example 3: Running Coroutines Concurrently
# =============================================================================

async def demo_gather():
    """Run multiple coroutines concurrently with asyncio.gather().

    gather() starts all coroutines at once and returns results
    in the same order as the coroutines were passed.
    """
    print("=== asyncio.gather() Demo ===")
    print("Running prime_filter and square_mapper concurrently...\n")

    # Both coroutines run concurrently (interleaved at await points)
    primes, squares = await asyncio.gather(
        prime_filter(2, 50),
        square_mapper(1, 10),
    )

    print(f"Primes (2-50):  {primes}")
    print(f"Squares (1-10): {squares}")
    print()


# =============================================================================
# Example 4: Progress Reporting with Async
# =============================================================================

async def prime_filter_with_progress(start: int, end: int) -> list[int]:
    """Prime filter that reports progress."""
    primes = []
    total = end - start + 1
    for i, n in enumerate(number_range(start, end)):
        if is_prime(n):
            primes.append(n)
        # Report progress every 25%
        if (i + 1) % (total // 4) == 0:
            pct = (i + 1) / total * 100
            print(f"  Prime filter: {pct:.0f}% complete ({len(primes)} found)")
            await asyncio.sleep(0)
    return primes


async def countdown(name: str, n: int) -> str:
    """Simple countdown coroutine (runs alongside prime filter)."""
    for i in range(n, 0, -1):
        print(f"  {name}: {i}")
        await asyncio.sleep(0.01)
    return f"{name} done"


async def demo_concurrent_progress():
    """Show interleaved execution of concurrent coroutines."""
    print("=== Concurrent Coroutines with Progress ===")

    results = await asyncio.gather(
        prime_filter_with_progress(2, 1000),
        countdown("Timer-A", 5),
        countdown("Timer-B", 3),
    )

    primes, msg_a, msg_b = results
    print(f"\nFound {len(primes)} primes between 2 and 1000")
    print(f"Messages: {msg_a}, {msg_b}")
    print()


# =============================================================================
# Example 5: gather() vs wait() Comparison
# =============================================================================

async def demo_comparison():
    """Compare gather() and wait() approaches."""
    print("=== gather() vs wait() ===")
    print("""
    asyncio.gather(*coroutines):
      - Returns results in ORDER (same as input)
      - Simple API: results = await gather(a, b, c)
      - Best for: getting all results together

    asyncio.wait(tasks):
      - Returns (done, pending) sets
      - Results in COMPLETION order (not input order)
      - Supports timeout and FIRST_COMPLETED
      - Best for: processing as tasks complete, timeouts
    """)

    # gather: ordered results
    results = await asyncio.gather(
        prime_filter(2, 30),
        square_mapper(1, 5),
    )
    print(f"gather results (ordered): {results}")
    print()

    # wait: done/pending sets
    tasks = [
        asyncio.create_task(prime_filter(2, 30)),
        asyncio.create_task(square_mapper(1, 5)),
    ]
    done, pending = await asyncio.wait(tasks)
    print(f"wait: {len(done)} done, {len(pending)} pending")
    for task in done:
        print(f"  Result: {task.result()}")


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    asyncio.run(demo_gather())
    asyncio.run(demo_concurrent_progress())
    asyncio.run(demo_comparison())
