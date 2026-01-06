# hand_evaluator.py

import collections

def evaluate_hand(hand):
    """
    Main function to determine the best ranking for a given hand of 5 cards.
    """
    # 1. EXTRACT DATA
    # We separate the card objects into simple lists of numbers and strings.
    # This makes the math much easier.
    ranks = [card.rank for card in hand]
    suits = [card.suit for card in hand]

    # 2. CHECK BOOLEAN FLAGS (True/False)
    # We check these first because they are "Global" rules (involving all 5 cards)
    is_flush = check_flush(suits)
    is_straight = check_straight(ranks)

    # 3. EVALUATE COMBINATIONS
    # Priority 1: Royal Flush & Straight Flush
    if is_flush and is_straight:
        if 14 in ranks and 13 in ranks: 
            return "Royal Flush"
        return "Straight Flush"
    
    # Priority 2: Four of a Kind (Checked via signature below, but stronger than flush)
    # We let the "Signature Check" handle this to keep code clean.

    # Priority 3 & 4: Flush or Straight
    if is_flush: return "Flush"
    if is_straight: return "Straight"

    # Priority 5: Pairs, Full House, 4-of-a-Kind
    # We use the "Hand Signature" method here.
    
    # Count how many times each rank appears (e.g., {'King': 2, '8': 3})
    counter = collections.Counter(ranks)
    
    # Extract just the counts and sort them highest-to-lowest
    # This creates a unique "Signature" for the hand structure.
    # Example: A Full House always looks like [3, 2]
    counts = sorted(counter.values(), reverse=True)

    if counts == [4, 1]:
        return "Four of a Kind"
    elif counts == [3, 2]:
        return "Full House"
    elif counts == [3, 1, 1]:
        return "Three of a Kind"
    elif counts == [2, 2, 1]:
        return "Two Pair"
    elif counts == [2, 1, 1, 1]:
        return "Pair"
    else:
        return "High Card"

# --- HELPER FUNCTIONS ---

def check_flush(suits):
    """Returns True if all suits are identical."""
    # Create a counter. If the most common suit appears 5 times, it's a flush.
    counter = collections.Counter(suits)
    most_common = counter.most_common(1)[0] # Returns ('Hearts', 5)
    count = most_common[1]                  # Grab the number 5
    
    return count == 5

def check_straight(ranks):
    """Returns True if ranks are consecutive."""
    sorted_ranks = sorted(ranks)
    
    # Special Rule: Ace Low Straight (A, 2, 3, 4, 5)
    # In our game, Ace is 14. So we look for [2, 3, 4, 5, 14]
    if set(sorted_ranks) == {2, 3, 4, 5, 14}:
        return True

    # Standard Rule: Check if each card is exactly 1 higher than the previous
    for i in range(4):
        # If current card + 1 is NOT equal to the next card...
        if sorted_ranks[i] + 1 != sorted_ranks[i+1]:
            return False
            
    return True