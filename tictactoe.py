class TicTacToe:
    """
    Class representing a Tic-Tac-Toe game.

    Attributes:
        BOARD_SIZE (int): Size of the Tic-Tac-Toe board.
        board (list): 2D list representing the Tic-Tac-Toe board.
        players (list): List of players ('X' and 'O').
        current_player (int): Index of the current player in the players list.
        scores (dict): Dictionary to keep track of players' scores.

    Methods:
        print_board(): Print the current state of the Tic-Tac-Toe board.
        make_move(row, col): Make a move on the Tic-Tac-Toe board.
        get_move(): Get user input for row and column to make a move.
        check_win(): Check if any player has won the game.
        is_game_over(): Check if the game is over (board is fully occupied).
        reset_game_state(): Reset the game state (except for scores) for a new game.
        update_scores(winner): Update the scores based on the winner of the game.
        print_scores(): Print the current scores of the players.
        play(): Start the Tic-Tac-Toe game and handle game logic.
    """
    BOARD_SIZE = 3

    def __init__(self):
        """Initialize the Tic-Tac-Toe game."""
        self.board = [[" " for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.players = ["X", "O"]
        self.current_player = 0
        self.scores = {player: 0 for player in self.players}
        
    def print_board(self):
        """Print the current game board."""
        for row in self.board:
            print(row)

    def make_move(self, row, col):
        """Make a move on the game board.

        Args:
            row (int): The row index of the move (0-2).
            col (int): The column index of the move (0-2).

        Returns:
            bool: True if the move is valid and made successfully, False otherwise.
        """
        if self.board[row][col] == " ":
            self.board[row][col] = self.players[self.current_player]
            return True
        return False

    def get_move(self):
        """Get a move from the current player.

        Returns:
            tuple: A tuple of row and column indices entered by the player.
        """
        while True:
            try:
                row = int(input("Enter row (1-3): ")) - 1
                col = int(input("Enter column (1-3): ")) - 1
                if 0 <= row < self.BOARD_SIZE and 0 <= col < self.BOARD_SIZE:
                    return row, col
                else:
                    print("Invalid input. Please enter row and column values between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter integer values for row and column.")

    def check_win(self):
        """Check if there is a winner in the current game state.

        Returns:
            str or None: The symbol of the winning player ('X' or 'O'), or None if no winner.
        """
        for row in self.board:
            if row[0] == row[1] and row[1] == row[2] and row[0] != " ":
                return row[0]

        for col in range(self.BOARD_SIZE):
            if self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col] and \
                    self.board[0][col] != " ":
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != " ":
            return self.board[0][0]

        if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and self.board[2][0] != " ":
            return self.board[0][0]

        return None

    def is_game_over(self):
        """Check if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        for row in self.board:
            for slot in row:
                if slot == " ":
                    return False
        return True

    def reset_game_state(self):
        """Reset the game state (except for scores) for a new game"""
        self.board = [[" " for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.current_player = 0

    def update_scores(self, winner):
        """Adds one point to the winning player's score"""
        if winner:
            self.scores[winner] += 1

    def print_scores(self):
        """Prints the player's scores"""
        print("Scores:")
        for player, score in self.scores.items():
            print("Player", player, ": ", score)

    def play(self):
        """Start a game of Tic-Tac-Toe."""
        print("Welcome to Tic-Tac-Toe!")
        while True:
            self.print_board()
            row, col = self.get_move()
            if self.make_move(row, col):
                self.current_player = (self.current_player + 1) % len(self.players)
            else:
                print("Invalid move. The selected cell is already occupied. Please choose another cell.")
                continue

            winner = self.check_win()
            if winner:
                self.print_board()
                print("Player", winner, "wins!")
                self.update_scores(winner)
                self.print_scores()
                replay = input("Do you want to play again? (y/n): ")
                if replay.lower() == 'y':
                    self.reset_game_state()
                else:
                    print("Thank you for playing Tic-Tac-Toe!")
                    break

            if self.is_game_over():
                self.print_board()
                print("It's a draw!")
                replay = input("Do you want to play again? (y/n): ")
                if replay.lower() == 'y':
                    self.reset_game_state()  # Reset game state except for scores
                else:
                    print("Thank you for playing Tic-Tac-Toe!")
                    break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
