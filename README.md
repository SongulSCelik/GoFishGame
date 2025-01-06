# 🐟 Go Fish Game

A Python implementation of the classic card game **Go Fish**, where players aim to collect books (sets of four cards of the same rank) by asking opponents for specific cards. This project demonstrates object-oriented programming principles, modular design, and user interaction in Python.

---

## 📝 Features

- **Interactive Gameplay:**
  - Play as a human against a CPU opponent.
  - Ask for specific card ranks, draw cards, and collect books.
- **Dynamic Deck Management:**
  - A standard 52-card deck with suits (Hearts, Diamonds, Clubs, Spades) and ranks (Ace to King).
  - Cards are shuffled at the start and managed dynamically.
- **Hand Sorting & Searching:**
  - Players’ hands are automatically sorted.
  - Efficient card searching using binary search.
- **CPU AI:**
  - The CPU strategically decides which card ranks to ask for based on its hand.
- **Error Handling:**
  - Validates player input and ensures smooth gameplay.
- **Two Versions:**
  - **Modular Version:** Classes and logic split into separate files for maintainability.
  - **Single-File Version:** All code in a single file for quick setup and execution.

---

## 📚 How to Play

1. **Objective:**
   - Collect as many books (sets of 4 cards of the same rank) as possible before the game ends.

2. **Gameplay:**
   - The game alternates between a human player and a CPU opponent.
   - On your turn:
     - Ask the opponent for a specific rank (e.g., "Ace", "5", "Queen").
     - If the opponent has cards of that rank, they must give them to you.
     - If not, you "Go Fish" and draw a card from the deck.
   - If you collect all four cards of a rank, you complete a "book," which counts toward your score.
   - The game ends when the deck is empty and no valid moves remain.

3. **Win Condition:**
   - The player with the most books at the end of the game wins.

---

### 🎲 Example Gameplay
Welcome to the Go Fish Game! Please enter your name: Alex

Welcome, Alex! You will be playing against CPU. Alex's Initial Hand: Ace ♥, 5 ♦, 7 ♣, King ♠, 3 ♥, Jack ♦, 8 ♠ CPU's hand is hidden.

Alex's Turn: Your Hand: Ace ♥, 5 ♦, 7 ♣, King ♠, 3 ♥, Jack ♦, 8 ♠ Enter the rank you want to ask for (e.g., '5', 'Ace', 'Queen'): Ace Alex asks CPU: Do you have any Aces? CPU says: Go Fish! Alex draws a card: Ace ♣

...

Game Over! Final Books: Alex's Books: ['Ace', '7'] CPU's Books: ['King'] The winner is Alex with 2 books!



---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher

---

### **Option 1: Modular Version**
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/SongulSCelik/GoFishGame.git
   cd GoFishGame
2.Run the Modular Version:
python main.py
3.File Structure:
GoFishGame/
├── README.md
├── LICENSE
├── card.py              # Contains the Card class
├── deck.py              # Contains the Deck class
├── player.py            # Contains the Player class
├── go_fish_game.py      # Contains the GoFishGame class
├── main.py              # Entry point for the modular version

---
### **Option 2: Single-File Version**
---
Run the Single-File Version:
python GoFish_SingleFile.py
File Structure:
GoFishGame/
├── README.md
├── LICENSE
├── GoFish_SingleFile.py 

🌟 Features to Add in the Future
---

Multiplayer Mode: Allow multiple human players to join the game.
Advanced CPU AI: Implement smarter decision-making strategies for the CPU.
Game Statistics: Track books collected, cards drawn, and rounds played.
GUI Version: Create a graphical interface for the game.
