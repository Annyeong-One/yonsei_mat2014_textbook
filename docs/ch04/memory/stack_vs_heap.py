"""
01_stack_vs_heap.py - Stack vs Heap Memory (Conceptual Foundation)
Topic #23: Memory and Namespace
"""

print("=" * 70)
print("STACK VS HEAP MEMORY")
print("=" * 70)

print("""
COMPUTER MEMORY (RAM) IS DIVIDED INTO:

STACK                          HEAP
- Organized (frames)          - Unorganized (flexible)
- Automatic management        - Requires GC
- Fixed size per frame        - Variable size allocations
- Very fast                   - Slower
- LIFO structure              - Random access
- Function calls              - All Python objects
- Local variable NAMES        - Everything is an object!

KEY INSIGHT:
Variable NAMES live on stack
Variable OBJECTS live on heap
""")

# Simple example
x = 42
name = "Alice"
numbers = [1, 2, 3]

print(f"\nCreated: x={x}, name='{name}', numbers={numbers}")

print("""
MEMORY MODEL:

STACK:                  HEAP:
┌──────────┐           ┌─────────────┐
│ x    ────┼──────────→│ int: 42     │
│ name ────┼──────────→│ str: "Alice"│
│ numbers ─┼──────────→│ list: [...]│
└──────────┘           └─────────────┘

Stack holds NAMES (references)
Heap holds OBJECTS (actual data)
""")

# Function call stack
def outer():
    print("  → outer() called")
    inner()
    print("  ← outer() returns")

def inner():
    print("    → inner() called")
    x = 100
    print(f"    x = {x}")
    print("    ← inner() returns")

print("\nFunction call stack demonstration:")
outer()

print("""
STACK FRAMES:

Start:           [global]
Call outer():    [outer] [global]
Call inner():    [inner] [outer] [global]  ← Stack grows
inner returns:   [outer] [global]
outer returns:   [global]                  ← Stack shrinks

Each function gets its own frame!
""")

print("\nKey takeaways:")
print("1. Stack: Fast, automatic, organized")
print("2. Heap: Flexible, requires GC, all objects")
print("3. Names on stack point to objects on heap")
print("4. Understanding this helps debug memory issues")

print("\nSee exercises.py for practice!")
