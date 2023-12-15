import random

class Card:
    def __init__(self, suit, value):
        if suit not in ['clubs', 'diamonds', 'hearts', 'spades']:
            raise ValueError("Invalid suit")
        if value not in [2, 3, 4, 5, 6, 7, 8, 9, 'A', 'K', 'J', 'Q']:
            raise ValueError("Invalid value")

        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Pair:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def __repr__(self):
        return f"Pair: ({self.card1}, {self.card2})"

class Cards:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.cards = cards

    def __repr__(self):
        return f"Pack with {len(self.cards)} cards"

    def __add__(self, other):
        if not isinstance(other, Cards):
            raise ValueError
        new_value = sum(card.value for card in self.cards + other.cards)
        return new_value

    def __sub__(self, other):
        if not isinstance(other, Cards):
            raise ValueError
        new_cards = [card for card in self.cards if card not in other.cards]
        return Cards(new_cards)

# Example:
card1 = Card('hearts', 4)
card2 = Card('diamonds', 3)

pair1 = Pair(card1, card2)

print('Pair 1 is:', pair1)

# Add pairs' values
added_values = Cards([pair1]) + Cards()
print("Added values:", added_values)

# Subtract pairs from an empty set
removed_pairs = Cards() - Cards([pair1])
print("Removed pairs:", removed_pairs)
