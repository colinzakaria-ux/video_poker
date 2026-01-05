import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []     # This list will hold all our Card Objects
        self.build()        # This calls the build function immediatley

    def build(self):
        self.cards = []     # Reset the list
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

        # 1. Create the standard 52 Card Deck
        for suit in suits:
            for rank in ranks(2, 15):
                new_card=Card(suit, rank)
                append.self.card(new_card)

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

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number_of_cards):
        dealt_cards=[]
        for _ in range(number_of cards):
            if len(self.cards) > 0:
                card = self.cards.pop()
                dealt_cards.append(card)
        return dealt_cards

    def build(self):
        self.cards=[]
        suits=["Hearts", "Diamonds", "Clubs", "Spades"]

        for suit in suits:
            for rank in ranks:
                new_card=Card(rank, suit)
                self.card.append(new_card)

        self.card.append(Card(15, None))
        self.card.append(Card(15, None))

        def shuffle(self):
            random.shuffle(self.cards)

        def deal(self, number_of_cards):
            dealt_cards=[]
            for _ in range(number_of_cards):
                if len(self.cards)>0:
                    card=self.cards.pop()
                    dealt_cards.append(card)
            return dealt_cards




