# Mastermind - Mini Game  
A simple two-player Mastermind game built with Python.  

## 📌 Game Overview  
Mastermind is a code-breaking game where Player 1 sets a secret code, and Player 2 tries to guess it. The game provides hints after each guess to help Player 2 get closer to the correct answer.  

## 🎮 How to Play  
1. **Player 1** enters a secret code.  
2. **Player 2** attempts to guess the code.  
3. After each guess, a hint is displayed showing:  
   - 🔢 How many numbers are correct.  
   - 🎯 How many numbers are both correct and in the right position.  
   - 🔄 Additional hints for Level 2.  
4. The game continues until Player 2 correctly guesses the code.  

## 🏆 Game Levels  
The game has two levels of difficulty:  

### 🔹 Level 1  
- **Code Length:** 4-digit code  
- **Rules:** Each digit must be unique (no repetitions).  
- **Hints Given:**  
  - ✅ Number of correct digits.  
  - 🎯 Number of correct digits in the right position.  

### 🔹 Level 2  
- **Code Length:** 9-digit code  
- **Rules:** Digits can repeat.  
- **Hints Given:**  
  - ✅ Number of correct digits.  
  - 🎯 Number of correct digits in the right position.  
  - 🔄 Number of repeated digits that match the correct code.  
  - 🔄 Total count of repeated numbers in the correct code based on the correct digits guessed by Player 2.


## 🖥️ Running the Game  
Simply **double-click** the `mastermind.exe` to start the game.  