# deck.py

from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []     # This list will hold all our Card Objects
        self.build()        # Call the function to fill the deck immediatley

    def build(self):
        self.cards = []     # Reset the list
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

        # 1. Create the Standard 52 Card Deck Using A Nested Loop
        for suit in suits:
            for rank in range(2, 15):
                new_card = Card(rank, suit)
                self.cards.append(new_card)

        # 2. Add the 2 Jokers
        self.cards.append(Card(15, None))
        self.cards.append(Card(15, None))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number_of_cards):
        dealt_cards = []
        for _ in range(number_of_cards):
            if len(self.cards) > 0:
                card = self.cards.pop()
                dealt_cards.append(card)
        return dealt_cards

# Sanity Check
if __name__ == "__main__":
    # Create the deck
    my_deck = Deck()
    print(f"A new deck with {len(my_deck.cards)} cards.")

    # 2. Shuffle it
    my_deck.shuffle()
    print("Deck Shuffled.")

    # 3. Deal 5 cards
    hand = my_deck.deal(5)
    print("\nHere is our hand:")
    for card in hand:
        print(card)

    print(f"\nCards remaining in the deck: {len(my_deck.cards)}")

    


