# practice.py
#
from card import Card
import random

class Deck:
    def __init__(self):
        self.cards=[]
        self.build()

    def build(self):
        self.cards= []
        suits = ["Hearts", "Diamonds", "Hearts", "Spades"]

        # 1. Create the standard 52 card deck plus 2 jokers
        for suit in suits:
            for rank in range(2, 15):
                new_card=Card(rank, suit)
                self.cards.append(new_card)

        self.cards.append(Card(15, None))
        self.cards.append(Card(15, None))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number_of_cards):
        dealt_cards=[]
        for _ in range(number_of_cards):
            if len(self.cards) > 0:
                card = self.cards.pop()
                dealt_cards.append(card)
        return dealt_cards



