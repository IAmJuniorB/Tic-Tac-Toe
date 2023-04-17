# Tic-Tac-Toe Game

  - This is a Python program that implements the game of Tic-Tac-Toe. It allows two players to play the game on a 3x3 game board. The game supports input validation, checks for wins or draws, keeps track of scores, and offers the option to replay the game.

# Usage

- To play the game, run the program using a Python interpreter. The game will start with a welcome message and an empty game board. Players take turns entering their moves by specifying the row and column of their desired move using integers from 1 to 3. The game validates the input and updates the game board accordingly.

- The game ends when there is a winner or a draw. The program will prompt the players if they want to play again. If they choose to play again, the game board will be reset, but the scores will be retained. If they choose not to play again, the program will display a farewell message and exit.

# Class Description

##### The program defines a TicTacToe class that encapsulates the logic of the game. The class has the following methods:

    - __init__(): Initializes the game state, including the game board, players, current player, and scores.
    - print_board(): Prints the current game board.
    - make_move(row, col): Makes a move on the game board at the specified row and column, if the cell is unoccupied. Returns True if the move is valid and False otherwise.
    - get_move(): Prompts the current player to enter their move (row and column) and validates the input. Returns the row and column as integers.
    - check_win(): Checks if there is a winner on the game board. Returns the winning player ("X" or "O") or None if there is no winner.
    - is_game_over(): Checks if the game is over due to a draw (all cells occupied). Returns True if the game is over and False otherwise.
    - reset_game_state(): Resets the game board and current player, but retains the scores.
    - update_scores(winner): Updates the scores with the winner of the game.
    - print_scores(): Prints the current scores.
    - play(): Starts the game loop and manages the flow of the game, including handling player moves, checking for wins or draws, updating scores, and offering replay option.

- The program also includes a __main__ block that creates an instance of the TicTacToe class and starts the game by calling the play() method.
Dependencies

- The program does not have any external dependencies and only requires a Python interpreter to run.

# License

- This program is released under the MIT License. You are free to use, modify, and distribute the code as long as you include the original license in your distribution. Refer to the LICENSE file for more information.

Enjoy!
