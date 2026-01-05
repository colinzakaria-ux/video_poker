# hand_evaluator.py
#

import collections

winning_hands={
     10:"High Card",
     20:"Pair",
     30:"Two Pair",
     40:"Three of A Kind",
     50:"Straight",
     60:"Flush",
     70:"Full-House",
     80:"Four of a Kind",
     90:"Straight Flush",
    100:"Royal Flush"
    }





# hand_evaluator.py
import collections

def evaluate_hand(hand):
    # 1. EXTRACT DATA
    # Create a list of just the ranks (integers)
    ranks = [card.rank for card in hand]
    # Create a list of just the suits (strings)
    suits = [card.suit for card in hand]

    # 2. CHECK COMBINATIONS
    # We pass these simple lists to our helper functions
    if check_flush(suits):
        return "Flush"
    elif check_straight(ranks):
        return "Straight"
    else:
        return "High Card" # (Placeholder for now)

def check_flush(suits):
    # Your Logic: Count the suits
    counter = collections.Counter(suits)
    
    # Check the most common suit
    # .most_common(1) returns a list like [('Hearts', 5)]
    most_common_suit = counter.most_common(1)[0]
    
    count = most_common_suit[1] # Grab the number (5)
    
    if count >= 5:
        return True
    return False

def check_straight(ranks):
    sorted_ranks = sorted(ranks)
    
    # Special Logic: Handle Ace (14) acting as 1 (A-2-3-4-5)
    # If we have 2, 3, 4, 5, 14... change 14 to 1 and re-sort
    if set(sorted_ranks) == {14, 2, 3, 4, 5}:
        return True

    for i in range(4):
        # Is the next number exactly 1 bigger than the current number?
        if sorted_ranks[i] + 1 != sorted_ranks[i+1]:
            return False
            
    return True
