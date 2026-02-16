"""
Intermediate Tutorial 4: gather() vs wait()

Compares asyncio.gather() and asyncio.wait() for different use cases.
"""

import asyncio

async def demonstrate_gather_vs_wait():
    print("\n--- gather() vs wait() ---")
    print("""
    gather():
    • Returns results in order
    • Simple API
    • Best for: Getting all results
    
    wait():
    • Returns (done, pending) sets
    • More control
    • Best for: Processing as completed, timeouts
    
    Example - gather():
    results = await asyncio.gather(task1(), task2(), task3())
    
    Example - wait():
    done, pending = await asyncio.wait([task1(), task2()])
    for task in done:
        result = await task
    
    Use gather() for most cases!
    """)

async def main():
    await demonstrate_gather_vs_wait()

if __name__ == "__main__":
    asyncio.run(main())
