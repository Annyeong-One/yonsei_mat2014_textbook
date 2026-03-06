"""
TUTORIAL: The Sequence Protocol - Making Custom Objects Behave Like Lists

This tutorial teaches you how to implement __len__ and __getitem__ dunder methods
to make a custom class support the sequence protocol. We'll build a FrenchDeck class
that behaves like a sequence - you can call len() on it, index into it, and slice it,
just like with built-in lists and tuples.

Key Learning Goals:
  - Understand why dunder methods make Python more intuitive
  - Learn how __len__ and __getitem__ enable sequence behavior
  - See how minimal code enables powerful functionality
"""

import collections

if __name__ == "__main__":

    print("=" * 70)
    print("TUTORIAL: The Sequence Protocol - Custom Sequence Objects")
    print("=" * 70)

    # ============ EXAMPLE 1: Understanding Namedtuples ============
    print("\n# Example 1: Creating a Card with namedtuple")
    print("=" * 70)

    Card = collections.namedtuple('Card', ['rank', 'suit'])

    # A namedtuple is a lightweight data structure. It's perfect for simple objects
    # that need readable field names instead of just index positions.
    card1 = Card('7', 'hearts')
    card2 = Card('A', 'spades')

    print(f"Card 1: {card1}")
    print(f"Card 2: {card2}")
    print(f"Accessing card1.rank: {card1.rank}")
    print(f"Accessing card1.suit: {card1.suit}")
    print("""
    WHY: A namedtuple is perfect here because a card is just two pieces of data.
    It's more readable than Card(7, 'hearts') and faster than a full class.
    """)

    # ============ EXAMPLE 2: Building the FrenchDeck Class ============
    print("\n# Example 2: Implementing the Sequence Protocol")
    print("=" * 70)

    class FrenchDeck:
        """
        A standard 52-card French deck that implements the sequence protocol.

        By implementing __len__ and __getitem__, instances can be used wherever
        Python expects a sequence (like lists or tuples). This is a powerful example
        of "duck typing" - if it walks like a sequence and quacks like a sequence,
        Python will treat it as one.
        """

        # Class attributes: these are defined once and shared by all instances
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 2-10, J, Q, K, A
        suits = 'spades diamonds clubs hearts'.split()

        def __init__(self):
            """
            Initialize the deck with all 52 cards.

            We create cards by combining each suit with each rank.
            The order matters: suits loop on the outside, ranks on the inside.
            This creates: [Card(2, spades), Card(3, spades), ..., Card(A, hearts)]
            """
            self._cards = [Card(rank, suit)
                           for suit in self.suits
                           for rank in self.ranks]

        def __len__(self):
            """
            Return the number of cards in the deck.

            By implementing __len__, our deck now supports:
              - len(deck)  # returns 52
              - if deck:   # works as a boolean (empty deck = False)
              - for loop iteration works better

            This is a tiny method but incredibly powerful. Python now treats
            FrenchDeck as a sequence!
            """
            return len(self._cards)

        def __getitem__(self, position):
            """
            Return a card at a specific position or a slice of cards.

            By implementing __getitem__, our deck now supports:
              - deck[0]        # get first card
              - deck[-1]       # get last card
              - deck[1:3]      # slice operations work automatically!
              - for card in deck:  # iteration works too

            This is the key to making our class behave like a real sequence.
            We don't need separate slicing logic - Python handles it for us
            because __getitem__ can receive slice objects.
            """
            return self._cards[position]


    # ============ EXAMPLE 3: Creating and Using a Deck ============
    print("\n# Example 3: Creating a FrenchDeck")
    print("=" * 70)

    deck = FrenchDeck()

    print(f"Number of cards in deck: {len(deck)}")
    print(f"First card: {deck[0]}")
    print(f"Last card: {deck[-1]}")
    print(f"""
    WHY: We don't need to write special methods for these operations.
    By implementing __getitem__ with a list inside, Python automatically
    gives us indexing, negative indexing, and even slicing!
    """)

    # ============ EXAMPLE 4: Slicing Works Automatically ============
    print("\n# Example 4: Slicing Operations (Free From __getitem__)")
    print("=" * 70)

    first_three = deck[0:3]
    print(f"First three cards: {first_three}")

    last_five = deck[-5:]
    print(f"Last five cards: {last_five}")

    every_nth = deck[::13]  # Every 13th card (one from each suit, roughly)
    print(f"Every 13th card (samples): {every_nth}")
    print("""
    WHY: Slicing is automatic! When you write deck[0:3], Python calls
    __getitem__ with a slice(0, 3) object, and that gets passed to our
    internal list's __getitem__, which already knows how to handle slices.
    """)

    # ============ EXAMPLE 5: Iteration Works Automatically ============
    print("\n# Example 5: Iteration (Also Free From __getitem__)")
    print("=" * 70)

    print("First 5 cards when iterating:")
    for i, card in enumerate(deck):
        if i < 5:
            print(f"  Card {i}: {card}")
        else:
            break
    print("  ...")
    print(f"Total cards iterated: {len(deck)}")
    print("""
    WHY: For loops work because Python falls back to __getitem__ when __iter__
    isn't defined. It starts at index 0 and keeps incrementing until it gets
    an IndexError. This is how iteration works on sequences!
    """)

    # ============ EXAMPLE 6: Boolean Context (Free From __len__) ============
    print("\n# Example 6: Using Deck in Boolean Context")
    print("=" * 70)

    non_empty_deck = FrenchDeck()
    empty_list = []

    print(f"if deck: {bool(non_empty_deck)} (deck has {len(non_empty_deck)} cards)")
    print(f"if empty_list: {bool(empty_list)} (list is empty)")
    print("""
    WHY: Python uses __len__ to determine truthiness. Any object with a
    non-zero length is truthy. By implementing __len__, we get free boolean
    behavior!
    """)

    # ============ EXAMPLE 7: The Complete Picture ============
    print("\n# Example 7: What We Get With Just Two Methods")
    print("=" * 70)

    print("""
    By implementing just __len__ and __getitem__, FrenchDeck gets:

      ✓ len(deck)           - calls __len__
      ✓ deck[i]             - calls __getitem__
      ✓ deck[i:j]           - calls __getitem__ with slice object
      ✓ deck[-1]            - negative indexing
      ✓ for card in deck:   - iteration
      ✓ if deck: ...        - boolean context
      ✓ reversed(deck)      - calls __getitem__ with negative indices
      ✓ list(deck)          - conversion to list
      ✓ print(deck[0])      - card representation

    This is the power of the sequence protocol. Python recognizes the pattern
    and automatically enables a whole family of operations.

    KEY INSIGHT: By following Python's protocols (implementing the right dunder
    methods), we write less code and users can interact with our objects using
    all the standard Python operations they already know.
    """)

    # ============ EXAMPLE 8: Practical Use Case ============
    print("\n# Example 8: Practical Code with Our Deck")
    print("=" * 70)

    # Because we implemented the sequence protocol, we can use standard Python tools
    import random

    small_hand = random.sample(deck, 5)
    print(f"Random hand of 5 cards: {small_hand}")

    # Convert to list if needed (though it's already sequence-like)
    as_list = list(deck[:3])
    print(f"First 3 cards as list: {as_list}")

    # Use in any place that expects sequences
    def show_first_card(sequence):
        """Works with any sequence"""
        if sequence:
            return sequence[0]
        return None

    print(f"Works with functions expecting sequences: {show_first_card(deck)}")

    print("""
    WHY: Because we implemented the sequence protocol correctly, FrenchDeck
    instances work seamlessly with all standard Python tools and functions
    that expect sequences. This is duck typing in action.
    """)

    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS")
    print("=" * 70)
    print("""
    1. DUNDER METHODS ARE PROTOCOLS: Implementing __len__ and __getitem__
       is not about those specific methods - it's about implementing the
       sequence protocol, which tells Python "I'm sequence-like."

    2. MINIMAL CODE, MAXIMUM POWER: With just two methods, we unlocked
       indexing, slicing, iteration, boolean context, and more.

    3. DUCK TYPING: We don't inherit from list, we don't have a special base
       class - we just implement the right methods. Python doesn't care about
       our type, only our behavior.

    4. USERS GET FAMILIAR PYTHON: Since our deck behaves like a sequence,
       users can use all the standard Python operations they already know.
       No learning curve required.
    """)
