# card.py

class Card:
    def __init__(self, rank, suit):
        self.rank = rank # Integer: 2-14 (where 11=Jack, 12=Queen, 13=King, 14=Ace)
        self.suit = suit # String: 'Hearts', 'Diamonds', 'Clubs', 'Spades'

    # This method controls what happens whe you print a Card object
    def __str__(self):

        if self.rank == 15:
            return "Joker"

        # Translating 11>'J', 12>'Q', 13>'K', 14>'A' Using a dictionary
        rank_names ={
            11: 'J',
            12: 'Q',
            13: 'K',
            14: 'A'
        }

        # If the rank is in the dictionary, use the corresponding name
        display_rank = rank_names.get(self.rank, self.rank)
        return f"{display_rank} of {self.suit}"
        
    
# Sanity check
#c1 = Card(14, "Hearts")
#print(c1)
