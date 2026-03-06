"""
Topic 45.4 - Process Pools with multiprocessing.Pool

Complete guide to using process pools for efficient parallel task execution.
Pools manage a set of worker processes and distribute work automatically.

Learning Objectives:
- Create and use process pools
- Use map, imap, starmap for parallel execution
- Handle async operations with apply_async and map_async
- Manage pool lifecycle
- Error handling in pools
- Performance optimization

Author: Python Educator
Date: 2024
"""

import multiprocessing
from multiprocessing import Pool, cpu_count
import time
import random
import math


# ============================================================================
# PART 1: BEGINNER - Pool Basics and map()
# ============================================================================

def basic_pool_usage():
    """
    The simplest way to use a pool: map() a function over data.
    This is like built-in map() but runs in parallel across processes.
    """
    print("=" * 70)
    print("BEGINNER: Basic Pool with map()")
    print("=" * 70)
    
    def square(x):
        """
        Calculate square of a number.
        
        Args:
            x: Number to square
            
        Returns:
            Square of x
        """
        # Add delay to simulate real work
        time.sleep(0.1)
        return x ** 2
    
    # Input data
    numbers = list(range(10))
    
    print(f"\n📝 Input: {numbers}")
    print(f"   We want to square each number in parallel\n")
    
    # Method 1: Sequential (for comparison)
    print("⏱️  Sequential execution:")
    start = time.time()
    results_sequential = [square(x) for x in numbers]
    seq_time = time.time() - start
    print(f"   Time: {seq_time:.2f}s")
    print(f"   Results: {results_sequential}")
    
    # Method 2: Parallel with Pool
    print("\n⏱️  Parallel execution with Pool:")
    start = time.time()
    
    # Create a pool with 4 worker processes
    with Pool(processes=4) as pool:
        # Map the function over the data
        results_parallel = pool.map(square, numbers)
    
    parallel_time = time.time() - start
    print(f"   Time: {parallel_time:.2f}s")
    print(f"   Results: {results_parallel}")
    
    # Analysis
    print(f"\n📊 Speedup: {seq_time/parallel_time:.2f}x faster!")
    print(f"   4 workers can process multiple items simultaneously")
    
    print("\n💡 Pool.map() advantages:")
    print("   ✓ Automatic work distribution")
    print("   ✓ Process reuse (no startup overhead)")
    print("   ✓ Simple API (like built-in map)")
    print("   ✓ Handles all the complexity for you")
    
    print("\n" + "=" * 70 + "\n")


def pool_with_different_sizes():
    """
    Experiment with different pool sizes to find optimal performance.
    """
    print("=" * 70)
    print("BEGINNER: Choosing Pool Size")
    print("=" * 70)
    
    def cpu_task(x):
        """CPU-intensive task"""
        # Calculate factorial (CPU work)
        result = math.factorial(x % 15 + 5)
        time.sleep(0.05)  # Small delay
        return result % 1000
    
    numbers = list(range(40))
    
    print(f"\n🖥️  Your system has {cpu_count()} CPU cores")
    print(f"   Testing different pool sizes on {len(numbers)} tasks:\n")
    
    # Test different pool sizes
    for pool_size in [1, 2, 4, cpu_count(), cpu_count() * 2]:
        start = time.time()
        
        with Pool(processes=pool_size) as pool:
            results = pool.map(cpu_task, numbers)
        
        elapsed = time.time() - start
        print(f"   {pool_size:2d} processes: {elapsed:.3f}s")
    
    print("\n💡 Guidelines for pool size:")
    print("   • CPU-bound: pool_size = cpu_count()")
    print("   • I/O-bound: pool_size = cpu_count() * 2 or more")
    print("   • Mixed: Start with cpu_count() and experiment")
    print("   • Too many processes = overhead from context switching")
    
    print("\n" + "=" * 70 + "\n")


def pool_context_manager():
    """
    Demonstrate proper pool lifecycle management with context manager.
    """
    print("=" * 70)
    print("BEGINNER: Pool Lifecycle Management")
    print("=" * 70)
    
    def worker(x):
        """Simple worker function"""
        return x * 2
    
    print("\n📝 Recommended: Use context manager (with statement)")
    print("   with Pool(4) as pool:")
    print("       results = pool.map(worker, data)")
    print("   # Pool automatically closed and terminated")
    
    # Good practice: context manager
    with Pool(4) as pool:
        results = pool.map(worker, range(10))
        print(f"\n✓ Results: {results}")
    print("✓ Pool automatically cleaned up\n")
    
    print("📝 Alternative: Manual management")
    print("   pool = Pool(4)")
    print("   results = pool.map(worker, data)")
    print("   pool.close()  # No more tasks accepted")
    print("   pool.join()   # Wait for workers to finish")
    
    # Manual management (less preferred)
    pool = Pool(4)
    results = pool.map(worker, range(10, 20))
    print(f"\n✓ Results: {results}")
    pool.close()  # Stop accepting new tasks
    pool.join()   # Wait for completion
    print("✓ Pool manually cleaned up")
    
    print("\n💡 Best Practice:")
    print("   Always use 'with Pool() as pool:' for automatic cleanup")
    
    print("\n" + "=" * 70 + "\n")


# ============================================================================
# PART 2: INTERMEDIATE - Advanced Mapping Functions
# ============================================================================

def pool_starmap_multiple_arguments():
    """
    Use starmap() when your function takes multiple arguments.
    starmap unpacks argument tuples for you.
    """
    print("=" * 70)
    print("INTERMEDIATE: starmap() for Multiple Arguments")
    print("=" * 70)
    
    def calculate_power(base, exponent):
        """
        Calculate base raised to exponent.
        
        Args:
            base: Base number
            exponent: Exponent
            
        Returns:
            base ** exponent
        """
        time.sleep(0.1)
        return base ** exponent
    
    # Data: list of (base, exponent) tuples
    tasks = [
        (2, 3),   # 2^3 = 8
        (3, 4),   # 3^4 = 81
        (5, 2),   # 5^2 = 25
        (10, 3),  # 10^3 = 1000
        (7, 2),   # 7^2 = 49
    ]
    
    print(f"\n📝 Tasks: {tasks}")
    print("   Each tuple is (base, exponent)\n")
    
    # Use starmap to unpack tuples
    with Pool(3) as pool:
        results = pool.starmap(calculate_power, tasks)
    
    print("📊 Results:")
    for (base, exp), result in zip(tasks, results):
        print(f"   {base}^{exp} = {result}")
    
    print("\n💡 starmap vs map:")
    print("   map(f, [x1, x2])     → f(x1), f(x2)")
    print("   starmap(f, [(a,b)])  → f(a, b)  # unpacks tuple")
    
    print("\n" + "=" * 70 + "\n")


def pool_imap_lazy_iteration():
    """
    Use imap() for lazy iteration over results.
    Unlike map(), imap() returns results as they complete.
    """
    print("=" * 70)
    print("INTERMEDIATE: imap() for Lazy Results")
    print("=" * 70)
    
    def slow_square(x):
        """Square with variable delay"""
        delay = random.uniform(0.5, 1.5)
        time.sleep(delay)
        return x ** 2, delay
    
    numbers = list(range(8))
    
    print(f"\n📝 Processing {len(numbers)} items with variable delays\n")
    
    # Method 1: map() - waits for ALL results
    print("⏱️  Using map() (blocks until all complete):")
    start = time.time()
    with Pool(4) as pool:
        results = pool.map(slow_square, numbers)
    elapsed = time.time() - start
    print(f"   Got all results after {elapsed:.2f}s")
    print(f"   Results: {[r[0] for r in results]}")
    
    # Method 2: imap() - yields results as they arrive
    print("\n⏱️  Using imap() (yields results incrementally):")
    start = time.time()
    with Pool(4) as pool:
        # imap returns an iterator
        for i, (result, delay) in enumerate(pool.imap(slow_square, numbers)):
            elapsed = time.time() - start
            print(f"   [{elapsed:.2f}s] Got result #{i}: {result} (took {delay:.2f}s)")
    
    print("\n💡 When to use imap():")
    print("   ✓ Process results as they complete")
    print("   ✓ Show progress updates")
    print("   ✓ Lower memory usage (streaming)")
    print("   ✓ Start processing early results while others compute")
    
    print("\n" + "=" * 70 + "\n")


def pool_imap_unordered():
    """
    Use imap_unordered() when result order doesn't matter.
    This can be faster as it returns results immediately.
    """
    print("=" * 70)
    print("INTERMEDIATE: imap_unordered() for Faster Results")
    print("=" * 70)
    
    def process_item(x):
        """Process with random delay"""
        delay = random.uniform(0.1, 1.0)
        time.sleep(delay)
        return x, delay
    
    numbers = list(range(12))
    
    print(f"\n📝 Processing {len(numbers)} items\n")
    
    # Ordered iteration
    print("⏱️  imap() - Maintains order:")
    with Pool(4) as pool:
        start = time.time()
        for i, (num, delay) in enumerate(pool.imap(process_item, numbers)):
            elapsed = time.time() - start
            print(f"   [{elapsed:.2f}s] Position {i}: item {num}")
    
    # Unordered iteration
    print("\n⏱️  imap_unordered() - Returns as completed:")
    with Pool(4) as pool:
        start = time.time()
        for i, (num, delay) in enumerate(pool.imap_unordered(process_item, numbers)):
            elapsed = time.time() - start
            print(f"   [{elapsed:.2f}s] Completed #{i}: item {num}")
    
    print("\n💡 imap_unordered() advantages:")
    print("   ✓ Faster - returns results immediately")
    print("   ✓ No waiting for slow tasks to maintain order")
    print("   ✓ Good for independent tasks")
    
    print("\n" + "=" * 70 + "\n")


# ============================================================================
# PART 3: ADVANCED - Async Operations and Error Handling
# ============================================================================

def pool_apply_async():
    """
    Use apply_async() for single tasks with callbacks.
    More flexible than map, but requires manual result handling.
    """
    print("=" * 70)
    print("ADVANCED: apply_async() with Callbacks")
    print("=" * 70)
    
    def compute_factorial(n):
        """Compute factorial of n"""
        time.sleep(0.5)
        result = math.factorial(n)
        return n, result
    
    def success_callback(result):
        """Called when task completes successfully"""
        n, factorial = result
        print(f"   ✓ Success: {n}! = {factorial}")
    
    def error_callback(error):
        """Called when task raises exception"""
        print(f"   ✗ Error: {error}")
    
    print("\n⚙️  Submitting async tasks with callbacks:\n")
    
    with Pool(3) as pool:
        # Submit multiple async tasks
        async_results = []
        
        for n in [5, 10, 15, 20]:
            result = pool.apply_async(
                compute_factorial,
                args=(n,),
                callback=success_callback,
                error_callback=error_callback
            )
            async_results.append(result)
        
        # Wait for all tasks
        pool.close()
        pool.join()
    
    print("\n💡 apply_async() features:")
    print("   ✓ Submit individual tasks")
    print("   ✓ Callbacks for success/error")
    print("   ✓ Non-blocking submission")
    print("   ✓ Flexible task management")
    
    print("\n" + "=" * 70 + "\n")


def pool_map_async_with_progress():
    """
    Use map_async() for non-blocking batch operations with progress tracking.
    """
    print("=" * 70)
    print("ADVANCED: map_async() with Progress Tracking")
    print("=" * 70)
    
    def heavy_computation(x):
        """CPU-intensive task"""
        time.sleep(0.3)
        return x ** 3
    
    numbers = list(range(20))
    
    print(f"\n⚙️  Processing {len(numbers)} items asynchronously...\n")
    
    with Pool(4) as pool:
        # Submit all tasks at once (non-blocking)
        result = pool.map_async(heavy_computation, numbers)
        
        # Do other work while tasks execute
        while not result.ready():
            remaining = result._number_left
            print(f"   Tasks remaining: {remaining}")
            time.sleep(0.5)
        
        # Get final results (will wait if not ready)
        final_results = result.get()
    
    print(f"\n✓ All tasks completed!")
    print(f"   First 5 results: {final_results[:5]}")
    
    print("\n💡 map_async() advantages:")
    print("   ✓ Non-blocking submission")
    print("   ✓ Can check progress with ready()")
    print("   ✓ Can track remaining tasks")
    print("   ✓ Main thread free for other work")
    
    print("\n" + "=" * 70 + "\n")


def pool_error_handling():
    """
    Handle errors in pool tasks gracefully.
    """
    print("=" * 70)
    print("ADVANCED: Error Handling in Pools")
    print("=" * 70)
    
    def risky_division(args):
        """
        Division that might fail.
        
        Args:
            args: (numerator, denominator) tuple
            
        Returns:
            Result of division
            
        Raises:
            ZeroDivisionError: If denominator is 0
        """
        numerator, denominator = args
        time.sleep(0.1)
        
        # This will raise exception for denominator=0
        return numerator / denominator
    
    # Some operations will fail
    tasks = [
        (10, 2),   # OK: 5.0
        (20, 4),   # OK: 5.0
        (15, 0),   # ERROR: division by zero
        (30, 6),   # OK: 5.0
        (25, 0),   # ERROR: division by zero
    ]
    
    print("\n📝 Method 1: Let exceptions propagate (default)")
    try:
        with Pool(2) as pool:
            # This will raise exception when it encounters error
            results = pool.starmap(risky_division, tasks)
    except Exception as e:
        print(f"   ✗ Caught exception: {type(e).__name__}: {e}")
    
    print("\n📝 Method 2: Handle errors individually")
    
    def safe_division(args):
        """Wrap risky function with error handling"""
        try:
            return risky_division(args), None
        except Exception as e:
            return None, str(e)
    
    with Pool(2) as pool:
        results = pool.starmap(safe_division, tasks)
    
    print("\n📊 Results:")
    for (num, denom), (result, error) in zip(tasks, results):
        if error:
            print(f"   {num}/{denom}: ✗ Error: {error}")
        else:
            print(f"   {num}/{denom}: ✓ {result}")
    
    print("\n💡 Error handling strategies:")
    print("   1. Try-except around pool.map() - stops on first error")
    print("   2. Wrap worker in try-except - continue on errors")
    print("   3. Use error_callback in apply_async()")
    
    print("\n" + "=" * 70 + "\n")


def pool_chunksize_optimization():
    """
    Optimize performance with chunksize parameter.
    """
    print("=" * 70)
    print("ADVANCED: Chunksize Optimization")
    print("=" * 70)
    
    def quick_task(x):
        """Very quick task"""
        return x * 2
    
    # Many small tasks
    numbers = list(range(1000))
    
    print(f"\n⏱️  Processing {len(numbers)} quick tasks:")
    print("   Testing different chunksizes...\n")
    
    # Test different chunksizes
    for chunksize in [1, 10, 50, 100]:
        start = time.time()
        
        with Pool(4) as pool:
            results = pool.map(quick_task, numbers, chunksize=chunksize)
        
        elapsed = time.time() - start
        print(f"   Chunksize {chunksize:3d}: {elapsed:.4f}s")
    
    print("\n💡 Chunksize guidelines:")
    print("   • Default: chunksize = len(data) / (processes * 4)")
    print("   • Many quick tasks: larger chunksize (less overhead)")
    print("   • Few slow tasks: smaller chunksize (better distribution)")
    print("   • Experiment to find optimal value")
    
    print("\n" + "=" * 70 + "\n")


def real_world_example_image_processing():
    """
    Realistic example: Parallel image processing simulation.
    """
    print("=" * 70)
    print("ADVANCED: Real-World Example - Batch Processing")
    print("=" * 70)
    
    def process_image(image_id):
        """
        Simulate image processing.
        
        Args:
            image_id: Image identifier
            
        Returns:
            Processing result
        """
        # Simulate different processing times
        time.sleep(random.uniform(0.2, 0.8))
        
        # Simulate processing operations
        operations = ["resize", "filter", "compress"]
        
        return {
            'id': image_id,
            'operations': operations,
            'size_mb': random.uniform(1.0, 5.0),
            'status': 'success'
        }
    
    # Simulate 50 images to process
    image_ids = [f"IMG_{i:04d}" for i in range(50)]
    
    print(f"\n📷 Processing {len(image_ids)} images...\n")
    
    start = time.time()
    
    # Process with pool
    with Pool(cpu_count()) as pool:
        # Use imap_unordered for best performance
        results = list(pool.imap_unordered(
            process_image,
            image_ids,
            chunksize=5  # Process 5 images per worker at a time
        ))
    
    elapsed = time.time() - start
    
    # Statistics
    total_size = sum(r['size_mb'] for r in results)
    avg_size = total_size / len(results)
    
    print(f"✓ Processed {len(results)} images in {elapsed:.2f}s")
    print(f"  Total size: {total_size:.1f} MB")
    print(f"  Average size: {avg_size:.2f} MB")
    print(f"  Throughput: {len(results)/elapsed:.1f} images/sec")
    
    print("\n💡 This pattern works for:")
    print("   • Image/video processing")
    print("   • Data transformation")
    print("   • File conversion")
    print("   • API requests")
    print("   • Report generation")
    
    print("\n" + "=" * 70 + "\n")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Run all pool demonstrations."""
    print("\n" + "=" * 70)
    print(" " * 20 + "PROCESS POOLS")
    print(" " * 15 + "multiprocessing.Pool Tutorial")
    print("=" * 70 + "\n")
    
    # Beginner level
    basic_pool_usage()
    pool_with_different_sizes()
    pool_context_manager()
    
    # Intermediate level
    pool_starmap_multiple_arguments()
    pool_imap_lazy_iteration()
    pool_imap_unordered()
    
    # Advanced level
    pool_apply_async()
    pool_map_async_with_progress()
    pool_error_handling()
    pool_chunksize_optimization()
    real_world_example_image_processing()
    
    print("\n" + "=" * 70)
    print("Process Pools Tutorial Complete!")
    print("=" * 70)
    print("\n💡 Key Takeaways:")
    print("1. Pool manages worker processes automatically")
    print("2. map() is simplest - like built-in map")
    print("3. starmap() for functions with multiple arguments")
    print("4. imap() yields results incrementally")
    print("5. imap_unordered() returns results faster")
    print("6. apply_async() for fine-grained control")
    print("7. Use chunksize to optimize performance")
    print("8. Always use context manager for cleanup")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    # IMPORTANT: This guard is required on Windows
    main()
