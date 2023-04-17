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
                self.update_scores(winner)  # Update scores
                self.print_scores()  # Print scores
                replay = input("Do you want to play again? (y/n): ")
                if replay.lower() == 'y':
                    self.reset_game_state()  # Reset game state except for scores
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
