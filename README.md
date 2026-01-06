#video_poker
# Python Video Poker 🎰

A command-line Video Poker game built with Python. This project was created to practice **Object-Oriented Programming (OOP)**, algorithm design, and Python syntax logic.

## 📖 Project Overview

This is a text-based implementation of standard "Jacks or Better" poker. The program simulates a standard 52-card deck (plus Jokers logic), handles card dealing, and evaluates hands using a custom ranking algorithm.

### Key Concepts Implemented
* **Object-Oriented Programming:** Classes for `Card` and `Deck` management.
* **Algorithm Design:** Logic to detect winning hands (Royal Flush, Straight, Full House) using "Hand Signatures."
* **Data Structures:** Using Lists for the deck and Dictionaries/Sets for hand evaluation.
* **Module Management:** Splitting code into multiple files (`main.py`, `deck.py`, etc.) for clean architecture.

## 📂 File Structure

* `main.py`: The controller. Runs the game loop, manages user input, and displays results.
* `deck.py`: The manager. Handles building the deck, shuffling, and dealing cards to the player.
* `card.py`: The data blueprint. Defines the properties of a single card (Rank/Suit) and handles its string representation (e.g., "Ace of Spades").
* `hand_evaluator.py`: The brain. Contains the logic functions (`check_flush`, `check_straight`) to determine the rank of the player's hand.

## 🚀 How to Run

1.  **Clone the repository** (or download the files):
    ```bash
    git clone [https://github.com/YOUR-USERNAME/video-poker.git](https://github.com/YOUR-USERNAME/video-poker.git)
    ```
2.  **Navigate to the folder**:
    ```bash
    cd video-poker
    ```
3.  **Run the game**:
    ```bash
    python main.py
    ```

## 🧠 Logic Highlights

### The "Hand Signature" Method
Instead of writing complex `if/else` chains for every pair combination, the `hand_evaluator.py` uses `collections.Counter` to create a "signature" of the hand.

* **Four of a Kind** always has counts: `[4, 1]`
* **Full House** always has counts: `[3, 2]`
* **Two Pair** always has counts: `[2, 2, 1]`

This makes the evaluation logic cleaner and more scalable.

## 🛠 Future Roadmap

* [ ] **Hold & Draw Mechanics:** Allow the player to choose which cards to keep and which to discard.
* [ ] **Betting System:** Add a bankroll and betting logic.
* [ ] **GUI:** Migrate from command line to a visual interface using `Pygame` or `Tkinter`.

---
*Created as part of a Python learning journey.*