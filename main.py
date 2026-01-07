# main.py
import os
from deck import Deck
from hand_evaluator import evaluate_hand

def clear_screen():
    # A simple command to clean the terminal window
    # 'nt' = Windows. 'clear' = Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def get_held_indices():
    """
    Asks the user which cards to hold.
    Returns a list of integers representing the INDICES (0-4) to keep.
    e.g., User types "1 3" -> Returns [0, 2]
    """
    while True:
        user_input = input("\nEnter Position of Cards to HOLD (e.g., '1 3 5) or press ENTER to discard All: ").capitalize()

        # If user presses Enter, they hold nothing (discard all)
        if user_input.strip() == "":
            return []
        
        try: 
            # 1. Split string into list of strings: "1 3" -> ["1", "3"]
            # 2. Convert to integers: -> [1, 3]
            # 3. Subtract 1 to match computer index (0-4): -> [0, 2]
            choices = [int(x) - 1 for x in user_input.split()]

            # Make sure the numbers are between 0 and 4
            if all(0 <= x <= 4 for x in choices):
                return choices
            else:
                print("Error: Please enter numbers between 1 and 5.")
        
        except ValueError:
            print("Error: Please enter numbers only.")

def play_game():
    print("Welcome to Pyhton Video Poker!")

    # 1. Initialize the Deck
    # We create the deck ONCE per game session
    game_deck = Deck()
    game_deck.shuffle()

    while True:
        # 2. Check if deck is running low
        # If we have less than 20 cards, let's rebuild and reshuffle
        if len(game_deck.cards) < 10:
            print("Shuffling new deck...")
            game_deck.build()
            game_deck.shuffle()

        input("\nPress Enter to deal a hand...")
        clear_screen()

        # Phase 1: Deal
        hand = game_deck.deal(5)

        print("\n--- INITIAL DEAL ---")
        for i, card in enumerate(hand):
            print(f"{i+1}: {card}")

        # Phase 2: Hold
        held_indices = get_held_indices()

        # Create a new list containing only the cards the user chose
        final_hand = [hand[i] for i in held_indices]

        # Calculate how many cards we threw away
        cards_needed = 5 - len(final_hand)

        # Phase 3: Draw
        if cards_needed > 0:
            print(f"\nDiscarding {cards_needed} cards...")
            new_cards = game_deck.deal(cards_needed)
            final_hand.extend(new_cards)
        else:
            print("\nStanding pat.")

        # Phase 4: Evaluate
        print("\n--- FINAL HAND---")
        for card in final_hand:
            print(card)
        
        result = evaluate_hand(final_hand)

        print("-" * 90)
        print(f"RESULT: {result}")
        print("-" * 90)

        choice = input("Play again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break





if __name__=="__main__":
    play_game()