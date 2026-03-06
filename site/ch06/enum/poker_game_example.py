"""
OOP Case Study: Poker Card Game with Enumerations

A practical OOP example combining Enum, classes, properties,
magic methods, and composition to build a card game simulator.

Topics covered:
- Enum with @unique for card suits
- Dunder methods: __str__, __repr__, __lt__
- @property for computed attributes
- Composition: Poker has Cards, Player has Cards
- List comprehensions with nested loops
- random.shuffle for shuffling

Based on concepts from Python-100-Days example14 and ch06/enum materials.
"""

import random
from enum import Enum, unique


# =============================================================================
# Example 1: Card Suit Enumeration
# =============================================================================

@unique
class Suit(Enum):
    """Card suits as an enumeration.

    @unique ensures no duplicate values.
    Custom __lt__ enables sorting by suit order.
    """
    SPADE = 0
    HEART = 1
    CLUB = 2
    DIAMOND = 3

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    @property
    def symbol(self) -> str:
        symbols = {
            Suit.SPADE: 'S', Suit.HEART: 'H',
            Suit.CLUB: 'C', Suit.DIAMOND: 'D',
        }
        return symbols[self]


# =============================================================================
# Example 2: Card Class
# =============================================================================

class Card:
    """A playing card with suit and face value.

    Face values: 1=Ace, 2-10, 11=Jack, 12=Queen, 13=King
    """

    FACE_NAMES = {
        1: 'A', 11: 'J', 12: 'Q', 13: 'K'
    }

    def __init__(self, suit: Suit, face: int):
        self.suit = suit
        self.face = face

    def __str__(self):
        face_str = self.FACE_NAMES.get(self.face, str(self.face))
        return f'{self.suit.symbol}{face_str}'

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        """Sort by suit first, then by face value."""
        if self.suit != other.suit:
            return self.suit < other.suit
        return self.face < other.face


# =============================================================================
# Example 3: Deck Class (Composition)
# =============================================================================

class Deck:
    """A standard 52-card deck.

    Demonstrates:
    - List comprehension with nested loops
    - @property for state checking
    - Iterator-like dealing interface
    """

    def __init__(self):
        self._index = 0
        self._cards = [
            Card(suit, face)
            for suit in Suit
            for face in range(1, 14)
        ]

    def shuffle(self) -> None:
        """Shuffle the deck and reset the deal position."""
        self._index = 0
        random.shuffle(self._cards)

    def deal(self) -> Card:
        """Deal the next card from the deck.

        Raises:
            IndexError: If no more cards to deal.
        """
        if not self.has_cards:
            raise IndexError("No more cards in deck")
        card = self._cards[self._index]
        self._index += 1
        return card

    @property
    def has_cards(self) -> bool:
        """Check if there are cards remaining to deal."""
        return self._index < len(self._cards)

    @property
    def remaining(self) -> int:
        """Number of cards remaining in deck."""
        return len(self._cards) - self._index

    def __len__(self):
        return len(self._cards)


# =============================================================================
# Example 4: Player Class
# =============================================================================

class Player:
    """A card game player who can receive and organize cards."""

    def __init__(self, name: str):
        self.name = name
        self.hand: list[Card] = []

    def receive(self, card: Card) -> None:
        """Add a card to the player's hand."""
        self.hand.append(card)

    def sort_hand(self) -> None:
        """Sort cards in hand by suit and face value."""
        self.hand.sort()

    def show_hand(self) -> str:
        """Display the player's hand."""
        return f"{self.name}: {self.hand}"

    def __repr__(self):
        return f"Player('{self.name}', {len(self.hand)} cards)"


# =============================================================================
# Example 5: Game Simulation
# =============================================================================

def deal_game(num_players: int = 4, cards_each: int = 13) -> None:
    """Simulate dealing cards to players."""
    player_names = ['North', 'East', 'South', 'West']

    deck = Deck()
    deck.shuffle()

    players = [Player(name) for name in player_names[:num_players]]

    print(f"=== Dealing {cards_each} cards to {num_players} players ===")
    print(f"Deck size: {len(deck)} cards")
    print()

    # Deal cards round-robin
    for _ in range(cards_each):
        for player in players:
            if deck.has_cards:
                player.receive(deck.deal())

    # Sort and display each player's hand
    for player in players:
        player.sort_hand()
        print(player.show_hand())

    print(f"\nRemaining in deck: {deck.remaining}")


# =============================================================================
# Example 6: Enum Iteration and Access Patterns
# =============================================================================

def demo_enum_features():
    """Demonstrate Enum features used in this example."""
    print("\n=== Enum Features ===")

    # Iteration
    print("All suits:", [s.name for s in Suit])
    print("All values:", [s.value for s in Suit])

    # Access by name and value
    print(f"By name: Suit['HEART'] = {Suit['HEART']}")
    print(f"By value: Suit(2) = {Suit(2)}")

    # Comparison
    print(f"SPADE < HEART: {Suit.SPADE < Suit.HEART}")

    # Identity
    print(f"Suit.SPADE is Suit(0): {Suit.SPADE is Suit(0)}")


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    deal_game()
    demo_enum_features()
