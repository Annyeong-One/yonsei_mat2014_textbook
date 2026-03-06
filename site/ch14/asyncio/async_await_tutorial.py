"""
Beginner Tutorial 1: Introduction to async/await Syntax

This file introduces the fundamental async/await syntax in Python.
We'll learn:
- What makes a function "async"
- How to call async functions with "await"
- The difference between sync and async execution
- Basic asyncio.run() usage

Learning objectives:
1. Understand async def syntax
2. Learn when and how to use await
3. See the difference between blocking and non-blocking code
"""

import asyncio
import time


# ============================================================================
# PART 1: Understanding Synchronous vs Asynchronous
# ============================================================================

def synchronous_function():
    """
    A regular (synchronous) function.
    When called, it runs from start to finish without yielding control.
    """
    print("Starting synchronous function")
    time.sleep(1)  # This BLOCKS the entire program for 1 second
    print("Finished synchronous function")
    return "Sync result"


async def asynchronous_function():
    """
    An asynchronous function (coroutine).
    Defined with 'async def' instead of just 'def'.
    
    When called WITHOUT await, it returns a coroutine object.
    When called WITH await, it executes and returns the result.
    """
    print("Starting asynchronous function")
    # asyncio.sleep() is non-blocking - it yields control to event loop
    await asyncio.sleep(1)
    print("Finished asynchronous function")
    return "Async result"


# ============================================================================
# PART 2: Basic async/await Patterns
# ============================================================================

async def simple_async_example():
    """
    A simple async function demonstrating await.
    
    Key points:
    - async def creates a coroutine function
    - await pauses this function and lets other tasks run
    - await can only be used inside async functions
    """
    print("Step 1: Before await")
    
    # await pauses execution here and yields to event loop
    # Other tasks could run during this 1 second
    await asyncio.sleep(1)
    
    print("Step 2: After await")
    return "Complete!"


async def calling_async_functions():
    """
    Demonstrates how to call one async function from another.
    
    Important:
    - To get the result, you must use 'await'
    - Without 'await', you just get a coroutine object
    """
    print("\n--- Calling async functions ---")
    
    # WRONG: Without await, this just creates a coroutine object
    # It doesn't actually run the function!
    coro = asynchronous_function()
    print(f"Without await: {coro}")
    print(f"Type: {type(coro)}")
    
    # We need to clean up the coroutine we created
    coro.close()
    
    # CORRECT: With await, the function runs and we get the result
    result = await asynchronous_function()
    print(f"With await: {result}")
    
    return result


# ============================================================================
# PART 3: Sequential Async Execution
# ============================================================================

async def fetch_data(data_id: int, delay: float):
    """
    Simulates fetching data from a source (like a database or API).
    
    Args:
        data_id: Identifier for the data
        delay: How long the fetch takes (simulated)
    
    Returns:
        The fetched data
    """
    print(f"  Fetching data {data_id}...")
    await asyncio.sleep(delay)  # Simulate I/O operation
    print(f"  Data {data_id} retrieved!")
    return f"Data_{data_id}"


async def sequential_execution():
    """
    Demonstrates sequential async execution.
    
    Even though we're using async/await, if we await each operation
    one after another, they still run sequentially (one at a time).
    
    This is like having async superpowers but choosing not to use them!
    """
    print("\n--- Sequential Execution ---")
    start_time = time.time()
    
    # Each await blocks until the operation completes
    # Total time: 1 + 1 + 1 = 3 seconds
    data1 = await fetch_data(1, 1.0)
    data2 = await fetch_data(2, 1.0)
    data3 = await fetch_data(3, 1.0)
    
    elapsed = time.time() - start_time
    print(f"Sequential execution took {elapsed:.2f} seconds")
    print(f"Retrieved: {data1}, {data2}, {data3}")
    
    return [data1, data2, data3]


# ============================================================================
# PART 4: Understanding await Behavior
# ============================================================================

async def demonstrate_await_behavior():
    """
    Shows what happens during await - control is yielded to event loop.
    
    When you 'await' something:
    1. Current function pauses
    2. Control returns to event loop
    3. Event loop can run other tasks
    4. When awaited operation completes, function resumes
    """
    print("\n--- Await Behavior ---")
    
    print("Before first await")
    await asyncio.sleep(0.5)  # Pause for 0.5 seconds
    print("Between awaits")
    await asyncio.sleep(0.5)  # Pause for another 0.5 seconds
    print("After second await")
    
    # Multiple awaits in sequence
    results = []
    for i in range(3):
        print(f"  Iteration {i+1}")
        await asyncio.sleep(0.1)
        results.append(i)
    
    return results


# ============================================================================
# PART 5: Async Function Return Values
# ============================================================================

async def async_function_with_return():
    """
    Async functions can return values just like regular functions.
    The return value is accessed by awaiting the function call.
    """
    await asyncio.sleep(0.1)
    return {"status": "success", "value": 42}


async def async_function_with_error():
    """
    Async functions can raise exceptions.
    These exceptions are raised when the function is awaited.
    """
    await asyncio.sleep(0.1)
    raise ValueError("Something went wrong!")


async def handling_returns_and_errors():
    """
    Demonstrates returning values and handling errors in async functions.
    """
    print("\n--- Returns and Errors ---")
    
    # Getting return value
    result = await async_function_with_return()
    print(f"Received result: {result}")
    
    # Handling errors
    try:
        await async_function_with_error()
    except ValueError as e:
        print(f"Caught exception: {e}")


# ============================================================================
# PART 6: Common Mistakes and Gotchas
# ============================================================================

async def common_mistakes():
    """
    Demonstrates common mistakes when learning async/await.
    """
    print("\n--- Common Mistakes ---")
    
    # Mistake 1: Forgetting await
    print("Mistake 1: Forgetting await")
    coro = asyncio.sleep(1)  # This creates a coroutine but doesn't run it
    print(f"  Without await: {coro}")
    coro.close()  # Clean up
    
    # Correct way
    print("  Correct way with await:")
    await asyncio.sleep(0.1)
    print("  Sleep completed!")
    
    # Mistake 2: Using time.sleep instead of asyncio.sleep
    print("\nMistake 2: Using time.sleep (blocking)")
    print("  DON'T do this in async code:")
    print("  time.sleep(1)  # This blocks the entire event loop!")
    
    print("  DO this instead:")
    await asyncio.sleep(0.1)  # Non-blocking
    print("  asyncio.sleep completed!")
    
    # Mistake 3: Trying to await non-async functions
    print("\nMistake 3: Can't await regular functions")
    print("  Regular functions must be called normally")
    regular_result = synchronous_function()  # No await!
    print(f"  Result: {regular_result}")


# ============================================================================
# PART 7: Running Async Code
# ============================================================================

async def main():
    """
    Main async function that demonstrates all concepts.
    
    This is the entry point for our async program.
    asyncio.run() creates an event loop, runs this coroutine,
    and then closes the event loop.
    """
    print("=" * 70)
    print("ASYNC/AWAIT BASICS TUTORIAL")
    print("=" * 70)
    
    # Run basic example
    result = await simple_async_example()
    print(f"Result: {result}")
    
    # Call async functions
    await calling_async_functions()
    
    # Sequential execution
    await sequential_execution()
    
    # Await behavior
    await demonstrate_await_behavior()
    
    # Returns and errors
    await handling_returns_and_errors()
    
    # Common mistakes
    await common_mistakes()
    
    print("\n" + "=" * 70)
    print("Tutorial complete!")
    print("=" * 70)


# ============================================================================
# Running the code
# ============================================================================

if __name__ == "__main__":
    """
    asyncio.run() is the recommended way to run async programs.
    
    What it does:
    1. Creates a new event loop
    2. Runs the provided coroutine (main)
    3. Closes the event loop when done
    
    This should be called only once per program, at the top level.
    Don't call asyncio.run() inside async functions!
    """
    
    # This is the standard way to run async code
    asyncio.run(main())
    
    # Note: You can't do this in an async function:
    # async def some_function():
    #     asyncio.run(main())  # ❌ Error! Already in async context


"""
KEY TAKEAWAYS:

1. async def: Defines an asynchronous function (coroutine)
2. await: Pauses execution and yields control to event loop
3. asyncio.run(): Entry point to run async code (use once)
4. await can only be used inside async functions
5. Async functions return coroutines that must be awaited
6. Use asyncio.sleep(), not time.sleep() in async code

MENTAL MODEL:
- Think of async/await as a way to write concurrent code that looks synchronous
- 'await' is like saying "I'm going to wait here, you can do other stuff"
- The event loop is the conductor that switches between tasks

NEXT STEPS:
- Learn about coroutines in detail (02_first_coroutine.py)
- Understand the event loop (03_event_loop_basics.py)
- Run multiple tasks concurrently (04_multiple_coroutines.py)
"""
