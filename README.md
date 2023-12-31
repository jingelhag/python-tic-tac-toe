# Tic-Tac-Toe Game in Python

This is a simple implementation of the classic Tic-Tac-Toe game in Python. 

## Getting Started

To run the game, make sure you have Python installed on your system. You can then follow these steps:

1. Clone this repository or download the `tic_tac_toe.py` file.

2. Open your terminal or command prompt and navigate to the directory where `tic_tac_toe.py` is located.

3. Run the game using the following command:

   ```bash
   python tic_tac_toe.py

# Tic-Tac-Toe Game in Python

**How to Play:**

- The game is played on a 3x3 grid.

- You can choose to be either X or O.

- The computer opponent uses the minimax algorithm to make its moves.

- To make a move, enter your choice using the format "row-column," for example, "top-Left" or "mid-Middle."

- The first player to get three in a row (horizontally, vertically, or diagonally) wins.

- If the board is filled and no player wins, it's a draw.

**Features:**

- Random selection of who starts the game, you or the computer.

- Simple text-based user interface.

- You can play again after a game ends.

**Code Explanation:**

The code is organized into functions and follows a standard Tic-Tac-Toe game structure. Key functions include:

- `printBoard()`: Prints the current state of the game board.

- `isBoardFull()`: Checks if the board is full.

- `minMax(depth, isMaximizing)`: Implements the minimax algorithm for the computer opponent.

- `move(choice, piece)`: Updates the board with a player's move.

- `playerMove(piece)`: Allows the player to make a move.

- `computerMove(piece)`: Lets the computer make a random move.

- `computerAiMove()`: Allows the computer to make a strategic move using the minimax algorithm.

- `nextMove(currentPlayer, setup)`: Determines the next move based on the current player.

- `isWinner(piece)`: Checks if a player has won.

**Author:**

This Tic-Tac-Toe game was created by Justus Ingelhag as a fun python project.

Feel free to modify and extend the code to add more features or improve the user experience. Enjoy playing!

