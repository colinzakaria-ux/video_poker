# main.py
import os
from deck import Deck
from hand_evaluator import evaluate_hand

def clear_screen():
    # A simple command to clean the terminal window
    # 'nt' = Windows. 'clear' = Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

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

        # 3. Deal the Hand
        # Ask the deck for 5 cards
        hand = game_deck.deal(5)

        # 4. Display the Hand
        print("\n--- YOUR HAND ---")
        for card in hand:
            print(card)

        # 5. Send the hand to our evaluator\
        result = evaluate_hand(hand)

    
        line=("-" * 90)
        
        print(line)
        print(f"Result: {result}")
        print(line)

        # 6. Play Again?
        choice = input("Play again (y/n): ").lower()
        if choice != 'y':
            print("Thanks for Playing!")
            break

if __name__=="__main__":
    play_game()