"""
Generator Functions with yield - A Simpler Way to Create Iterators
This tutorial demonstrates how to use generator functions with yield
to create iterators with much less code than the iterator protocol.
Run this file to see generators in action!
"""

import re
import reprlib

print("=" * 70)
print("GENERATOR FUNCTIONS WITH YIELD - EXAMPLES")
print("=" * 70)

# ============================================================================
# EXAMPLE 1: The Problem - Iterator Protocol is Verbose
# ============================================================================
print("\n1. THE PROBLEM - ITERATOR PROTOCOL IS VERBOSE")
print("-" * 70)

print("\nFrom the previous tutorial, we needed TWO classes:")
print("- Sentence class with __iter__()")
print("- SentenceIterator class with __iter__() and __next__()")
print("\nThis is a lot of boilerplate code for something conceptually simple!")
print("\nWhat if we could write iteration logic like a simple function?")

# ============================================================================
# EXAMPLE 2: Introduction to Generators and yield
# ============================================================================
print("\n2. INTRODUCTION TO GENERATORS AND YIELD")
print("-" * 70)

print("\nA generator function is a regular function that uses 'yield'")
print("instead of 'return'.\n")

print("When you call a generator function:")
print("1. It returns a GENERATOR OBJECT (an iterator)")
print("2. It doesn't execute the function body immediately")
print("3. Each call to next() executes until the next yield")
print("4. The function suspends at yield, remembering its state")
print("5. The next call to next() resumes from where it stopped\n")

print("This is MUCH simpler than implementing __iter__ and __next__!")

# ============================================================================
# EXAMPLE 3: Simple Generator Example
# ============================================================================
print("\n3. SIMPLE GENERATOR EXAMPLE")
print("-" * 70)

def simple_generator():
    """A simple generator to demonstrate yield."""
    print("  [Generator] Starting")
    yield 1
    print("  [Generator] After yield 1")
    yield 2
    print("  [Generator] After yield 2")
    yield 3
    print("  [Generator] After yield 3 (done)")

print("\nDefined simple_generator():\n")

gen = simple_generator()
print(f"Called: gen = simple_generator()")
print(f"Result: {gen}")
print(f"Type: {type(gen)}\n")

print("Notice: The function body hasn't executed yet!")
print("The generator just sits there, waiting.\n")

print("Now let's iterate:\n")
for value in gen:
    print(f"Got: {value}")

print("\nWHY THIS MATTERS:")
print("- yield pauses execution and returns a value")
print("- Execution resumes where it left off")
print("- State is automatically saved!")

# ============================================================================
# EXAMPLE 4: The Sentence Class with yield
# ============================================================================
print("\n4. THE SENTENCE CLASS - SIMPLIFIED WITH YIELD")
print("-" * 70)

RE_WORD = re.compile(r'\w+')

class Sentence:
    """
    A sequence of words extracted from a string.

    This version uses a generator function (with yield) instead of
    creating a separate iterator class. Much simpler!
    """

    def __init__(self, text):
        """Initialize with a text string."""
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        """Nice representation of the sentence."""
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        """
        Make Sentence iterable using a generator function.

        This is SO much simpler than creating a separate iterator class!
        Instead of managing state in __next__, we just yield each word.
        Python handles all the iteration logic for us.
        """
        for word in self.words:
            yield word

print("\nDefined Sentence class with:")
print("- __init__(text): Extract words from text")
print("- __repr__(): Nice representation")
print("- __iter__(): Generator function that yields words")
print("\nCompare this to the previous version with SentenceIterator!")
print("Much simpler, much clearer!\n")

# ============================================================================
# EXAMPLE 5: Using the Generator-Based Sentence
# ============================================================================
print("\n5. USING THE GENERATOR-BASED SENTENCE")
print("-" * 70)

text = 'To be, or not to be, that is the question'
s = Sentence(text)

print(f"\nCreated: s = Sentence('{text}')\n")

print("Iterating with for loop:")
print("-" * 40)

for i, word in enumerate(s, 1):
    print(f"  Word {i}: {word}")

print("\nWHY THIS WORKS:")
print("- __iter__() returns a generator object")
print("- for loop calls next() on the generator")
print("- Each yield returns a word to the for loop")
print("- When the loop in __iter__ ends, StopIteration is raised automatically")

# ============================================================================
# EXAMPLE 6: Generators are Lazy
# ============================================================================
print("\n6. GENERATORS ARE LAZY - MEMORY EFFICIENT")
print("-" * 70)

def count_up_to(n):
    """Generate numbers from 1 to n."""
    print(f"  [Generator] count_up_to({n}) starting")
    for i in range(1, n + 1):
        print(f"  [Generator] About to yield {i}")
        yield i
        print(f"  [Generator] Resumed after yield {i}")
    print(f"  [Generator] Finished")

print("\nDefined count_up_to(n)\n")

print("Creating: gen = count_up_to(3)")
gen = count_up_to(3)
print(f"Type: {type(gen)}\n")

print("Notice: count_up_to(3) printed NOTHING!")
print("The generator function body hasn't run yet.\n")

print("Now iterating:\n")
result = next(gen)
print(f"First next() returned: {result}\n")

result = next(gen)
print(f"Second next() returned: {result}\n")

result = next(gen)
print(f"Third next() returned: {result}\n")

print("This is LAZY EVALUATION:")
print("- Values are computed only when requested")
print("- Memory-efficient for large sequences")
print("- Can even be infinite (with a while True loop)")

# ============================================================================
# EXAMPLE 7: Generator Expressions
# ============================================================================
print("\n7. GENERATOR EXPRESSIONS")
print("-" * 70)

print("\nYou can also create generators with expressions (like list comprehensions):")
print("\nSyntax: (expression for item in iterable if condition)\n")

squares = (x * x for x in range(10) if x % 2 == 0)
print(f"Created: squares = (x*x for x in range(10) if x % 2 == 0)")
print(f"Type: {type(squares)}\n")

print("Note: Parentheses instead of square brackets!")
print("This creates a generator, not a list.\n")

print("Values:")
for sq in squares:
    print(f"  {sq}")

# Compare with list comprehension
print("\nCompare with list comprehension:")
squares_list = [x * x for x in range(10) if x % 2 == 0]
print(f"List: {squares_list}")
print(f"Type: {type(squares_list)}\n")

print("Generator expression: Lazy, memory-efficient")
print("List comprehension: Eager, all values in memory")

# ============================================================================
# EXAMPLE 8: Practical Example - Reading Large Files
# ============================================================================
print("\n8. PRACTICAL EXAMPLE - READING LINES EFFICIENTLY")
print("-" * 70)

def read_lines(filename):
    """
    Read a file line by line using a generator.

    This is more memory-efficient than reading the entire file
    with readlines() because it yields one line at a time.
    """
    with open(filename, 'r') as f:
        for line in f:
            yield line.rstrip('\n')  # Remove newline

print("\nDefined read_lines(filename)")
print("This reads a file line-by-line using a generator.\n")

print("Why generators are perfect for this:")
print("- You don't load the entire file into memory")
print("- Works with files of any size")
print("- Can process each line immediately")
print("- Yields one line at a time on demand")

# ============================================================================
# EXAMPLE 9: Using iter() to Manually Control Generators
# ============================================================================
print("\n9. MANUALLY ITERATING WITH iter() AND next()")
print("-" * 70)

def countdown(n):
    """Count down from n to 1."""
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)
print(f"Created: gen = countdown(5)\n")

print("Using next() manually:")
print(f"  next(gen) = {next(gen)}")
print(f"  next(gen) = {next(gen)}")
print(f"  next(gen) = {next(gen)}")

print("\nContinue with for loop:")
for val in gen:
    print(f"  {val}")

print("\nYou can mix manual next() calls with for loops!")

# ============================================================================
# EXAMPLE 10: Comparing Approaches
# ============================================================================
print("\n10. COMPARING ITERATOR PROTOCOLS VS GENERATORS")
print("-" * 70)

print("""
ITERATOR PROTOCOL (Previous Tutorial):
  - Must create a separate iterator class
  - Need to implement __iter__() and __next__()
  - Manual state management with instance variables
  - More boilerplate code
  + More control over iteration

GENERATORS (This Tutorial):
  - Use 'yield' in a regular function
  - Python handles __iter__() and __next__() automatically
  - State is saved automatically between yields
  - Much less code, cleaner and more readable
  + Simpler, more Pythonic

GENERATOR EXPRESSIONS:
  - Like list comprehensions but with parentheses
  - Even shorter syntax for simple cases
  + Most concise for simple iterations

RECOMMENDATION:
Use generators (yield) for most cases!
The iterator protocol is great when you need more control.
""")

# ============================================================================
# EXAMPLE 11: Key Insight - yield is Syntactic Sugar
# ============================================================================
print("\n" + "=" * 70)
print("KEY INSIGHT - yield IS SYNTACTIC SUGAR")
print("=" * 70)

print("""
When you write:

    def __iter__(self):
        for word in self.words:
            yield word

Python automatically creates the iterator machinery for you!

Equivalently, without yield:

    def __iter__(self):
        return SentenceIterator(self.words)

    class SentenceIterator:
        def __init__(self, words):
            self.words = words
            self.index = 0
        def __iter__(self):
            return self
        def __next__(self):
            try:
                word = self.words[self.index]
            except IndexError:
                raise StopIteration
            self.index += 1
            return word

The generator version does exactly the same thing,
but with a fraction of the code!

GENERATORS ARE THE PYTHONIC WAY TO CREATE ITERATORS!
""")
