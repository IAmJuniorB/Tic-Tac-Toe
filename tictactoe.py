class TicTacToe:
    BOARD_SIZE = 3

    def __init__(self):
        self.board = [[" " for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.players = ["X", "O"]
        self.current_player = 0
        self.scores = {player: 0 for player in self.players}
        
    def print_board(self):
        for row in self.board:
            print(row)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.players[self.current_player]
            return True
        return False

    def get_move(self):
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
        for row in self.board:
            for slot in row:
                if slot == " ":
                    return False
        return True

    def reset_game_state(self):
        self.board = [[" " for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.current_player = 0

    def update_scores(self, winner):
        if winner:
            self.scores[winner] += 1

    def print_scores(self):
        print("Scores:")
        for player, score in self.scores.items():
            print("Player", player, ": ", score)

    def play(self):
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
