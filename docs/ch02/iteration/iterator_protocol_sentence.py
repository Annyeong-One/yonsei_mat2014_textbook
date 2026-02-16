"""
Iterator Protocol Implementation - Building a Sentence Class with __iter__
This tutorial demonstrates how to implement the iterator protocol by
creating a Sentence class that can be iterated over like a native Python object.
Run this file to see the iterator protocol in action!
"""

import re
import reprlib

print("=" * 70)
print("ITERATOR PROTOCOL - IMPLEMENTING __iter__")
print("=" * 70)

# ============================================================================
# EXAMPLE 1: Understanding Iterables and Iterators
# ============================================================================
print("\n1. UNDERSTANDING ITERABLES AND ITERATORS")
print("-" * 70)

print("\nIn Python, there's an important distinction:")
print("- ITERABLE: Object that implements __iter__() method")
print("  Returns an iterator")
print("  Examples: lists, tuples, strings, dicts")
print("")
print("- ITERATOR: Object that implements both:")
print("  __iter__() - returns itself")
print("  __next__() - returns the next value and raises StopIteration when done")
print("")
print("When you write 'for x in iterable:', Python:")
print("  1. Calls iterable.__iter__() to get an iterator")
print("  2. Repeatedly calls iterator.__next__() until StopIteration")

# ============================================================================
# EXAMPLE 2: The Sentence Class - A Custom Iterable
# ============================================================================
print("\n2. THE SENTENCE CLASS - MAKING TEXT ITERABLE")
print("-" * 70)

# Regular expression to find words (letters and digits)
RE_WORD = re.compile(r'\w+')

class Sentence:
    """
    A sequence of words extracted from a string.

    This class implements the iterable protocol, allowing you to:
    - Access words by index: sentence[0], sentence[1]
    - Get the number of words: len(sentence)
    - Iterate over words: for word in sentence
    """

    def __init__(self, text):
        """
        Initialize with a text string.

        We extract all words (sequences of alphanumeric chars) from the text.
        """
        self.text = text
        # Use regex to find all words - this does the hard work
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        """
        Allow indexing: sentence[0], sentence[1], etc.

        This makes Sentence a sequence-like object.
        Python uses this for iteration as a fallback if __iter__ isn't defined.
        """
        return self.words[index]

    def __len__(self):
        """Allow len() function: len(sentence)"""
        return len(self.words)

    def __repr__(self):
        """
        Nice string representation that abbreviates long text.

        reprlib.repr() shows a summary of the text.
        """
        return 'Sentence(%s)' % reprlib.repr(self.text)

print("\nDefined the Sentence class with:")
print("- __init__(text): Initializes and extracts words using regex")
print("- __getitem__(index): Allows indexing like a list")
print("- __len__(): Returns the number of words")
print("- __repr__(): Nice representation")

# ============================================================================
# EXAMPLE 3: Using Sentence - Indexing and Length
# ============================================================================
print("\n3. USING SENTENCE - INDEXING AND LENGTH")
print("-" * 70)

text = 'To be, or not to be, that is the question'
s = Sentence(text)

print(f"\nCreated: s = Sentence('{text}')\n")

print(f"s[0] = {s[0]!r} (first word)")
print(f"s[1] = {s[1]!r} (second word)")
print(f"s[5] = {s[5]!r} (sixth word)")
print(f"\nlen(s) = {len(s)} (total words)")

print(f"\nrepr(s) = {repr(s)}")

print("\nWHY THIS WORKS:")
print("- __getitem__ allows indexing notation [index]")
print("- __len__ makes len() work on our custom object")
print("- __repr__ shows a nice representation in the interpreter")

# ============================================================================
# EXAMPLE 4: Adding __iter__ - Making Sentence Iterable in for loops
# ============================================================================
print("\n4. IMPLEMENTING __iter__ - FOR LOOP SUPPORT")
print("-" * 70)

print("\nThe current Sentence class supports indexing, but what about for loops?")
print("Python has a fallback: if __iter__ isn't defined, it tries __getitem__")
print("But it's better to explicitly implement __iter__ for clarity!\n")

print("Here's what we need to add:\n")

code_example = '''
def __iter__(self):
    """
    Make Sentence iterable.

    This method should return an iterator object.
    We could return a custom iterator, or use a generator.
    For this example, we'll use a helper iterator class.
    """
    return SentenceIterator(self.words)
'''

print(code_example)

# ============================================================================
# EXAMPLE 5: Creating a Custom Iterator Class
# ============================================================================
print("\n5. CUSTOM ITERATOR CLASS")
print("-" * 70)

class SentenceIterator:
    """
    An iterator for the Sentence class.

    This class implements the iterator protocol:
    - __iter__() returns itself
    - __next__() returns the next word or raises StopIteration
    """

    def __init__(self, words):
        """Store the words and initialize index to 0."""
        self.words = words
        self.index = 0

    def __iter__(self):
        """An iterator returns itself."""
        return self

    def __next__(self):
        """
        Return the next word, or raise StopIteration when done.

        This is the key method that makes iteration work!
        """
        try:
            word = self.words[self.index]
        except IndexError:
            # No more words, signal the end of iteration
            raise StopIteration
        self.index += 1
        return word

print("Defined SentenceIterator class:")
print("- __init__(words): Stores words and sets starting index to 0")
print("- __iter__(): Returns itself (required by iterator protocol)")
print("- __next__(): Returns next word or raises StopIteration")

# ============================================================================
# EXAMPLE 6: Adding __iter__ to Sentence
# ============================================================================
print("\n6. ADDING __iter__ TO SENTENCE")
print("-" * 70)

# Extend the Sentence class with __iter__
class Sentence:
    """
    A sequence of words extracted from a string.
    Now with full iterator support!
    """

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        """
        Return an iterator for this sentence.

        This is the crucial method that makes 'for word in sentence' work!
        """
        return SentenceIterator(self.words)

print("\nAdded __iter__ method to Sentence:")
print("Now Sentence objects work with for loops!")

# ============================================================================
# EXAMPLE 7: Using the Iterable Sentence
# ============================================================================
print("\n7. USING SENTENCE WITH FOR LOOPS")
print("-" * 70)

s = Sentence(text)

print(f"\nCreated: s = Sentence('{text}')\n")

print("Iterating with for loop:")
print("-" * 40)

for i, word in enumerate(s, 1):
    print(f"  Word {i}: {word}")

print("\nWHY THIS WORKS:")
print("- for loop calls s.__iter__() to get an iterator")
print("- Each iteration calls iterator.__next__() to get next word")
print("- When StopIteration is raised, the loop ends")
print("- No explicit iterator management needed!")

# ============================================================================
# EXAMPLE 8: Practical Example - Sentence Analysis
# ============================================================================
print("\n8. PRACTICAL EXAMPLE - SENTENCE ANALYSIS")
print("-" * 70)

def analyze_sentence(text):
    """Analyze a sentence and print various statistics."""
    s = Sentence(text)

    print(f"\nText: {text}")
    print(f"Number of words: {len(s)}")
    print(f"\nWords:")
    for i, word in enumerate(s, 1):
        print(f"  {i:2}. {word}")

    print(f"\nWord lengths:")
    for word in s:
        print(f"  '{word}' -> {len(word)} characters")

test_texts = [
    "Hello world",
    "Python is awesome",
    "The quick brown fox jumps over the lazy dog"
]

for test_text in test_texts:
    analyze_sentence(test_text)
    print()

# ============================================================================
# SUMMARY: The Iterator Protocol
# ============================================================================
print("\n" + "=" * 70)
print("SUMMARY - THE ITERATOR PROTOCOL")
print("=" * 70)

print("""
To make an object iterable (usable in for loops):

1. Implement __iter__():
   - Should return an iterator object
   - This method is called at the start of a for loop

2. Create an iterator class that implements:
   - __iter__(): Returns itself
   - __next__(): Returns next value or raises StopIteration

EXAMPLE FLOW for 'for word in sentence':
   1. Python calls sentence.__iter__() -> gets iterator
   2. Python calls iterator.__next__() -> gets first word
   3. Process word in loop body
   4. Back to step 2, repeat until StopIteration
   5. Loop exits

KEY BENEFITS:
- Make custom objects work with Python's for loops
- Compatible with other iteration tools (list comprehensions, etc.)
- Elegant, Pythonic interface
- Lazy evaluation (iterator can be memory efficient)

REMEMBER:
- Iterable: Has __iter__() method
- Iterator: Has __iter__() and __next__() methods
- You often need both for full iterator support!
""")
